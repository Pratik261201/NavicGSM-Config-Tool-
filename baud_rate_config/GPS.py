import serial
import pynmea2
import folium
from folium.plugins import MarkerCluster, Search
import webbrowser
import os
from datetime import datetime
from geopy.distance import geodesic

# === SETUP ===
COM_PORT = 'COM5'    # Set your GPS module's COM port
BAUD_RATE = 9600     # Default baud rate for NEO-6M
MAP_FILE = 'gps_map.html'
gps_points = []
timestamps = []
map_initialized = False
total_distance = 0.0
# ==============

def calculate_distance(p1, p2):
    return geodesic(p1, p2).meters

def update_map(points, timestamps):
    global map_initialized, total_distance

    if not points:
        return

    m = folium.Map(
        location=points[-1],
        zoom_start=18,
        tiles=None
    )

    # === Add Satellite Base Layer ===
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri Satellite',
        name='Esri Satellite',
        overlay=False
    ).add_to(m)

    # === Add Labels Overlay ===
    folium.TileLayer(
        tiles='https://services.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}',
        attr='Esri Labels',
        name='Labels',
        overlay=True
    ).add_to(m)

    marker_cluster = MarkerCluster().add_to(m)

    locations_for_search = []

    for i, (latlon, ts) in enumerate(zip(points, timestamps)):
        icon = folium.Icon(color='red', icon='map-marker', prefix='fa')
        popup = folium.Popup(f"<b>Point {i+1}</b><br>Time: {ts}", max_width=200)
        tooltip = f"Lat: {latlon[0]:.5f}, Lon: {latlon[1]:.5f}"
        marker = folium.Marker(latlon, popup=popup, tooltip=tooltip, icon=icon)
        marker.add_to(marker_cluster)

        # Add to search index
        marker.add_child(folium.Popup(ts))
        locations_for_search.append({'loc': latlon, 'name': f'Point {i+1}'})

        if i > 0:
            total_distance += calculate_distance(points[i - 1], latlon)

    # Add path
    folium.PolyLine(points, color='deepskyblue', weight=3.5, opacity=0.9).add_to(m)

    # === Add Search Control ===
    search_data = folium.FeatureGroup(name="Searchable Points")
    for item in locations_for_search:
        folium.Marker(location=item['loc'], tooltip=item['name']).add_to(search_data)
    m.add_child(search_data)

    Search(
        layer=search_data,
        search_label='tooltip',
        placeholder='Search GPS Point...',
        collapsed=False
    ).add_to(m)

    # === Info Summary Box ===
    summary_html = f"""
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 280px; height: 120px;
                background-color: white;
                border: 2px solid gray; z-index: 9999; font-size: 14px;
                padding: 10px; border-radius: 10px; box-shadow: 2px 2px 8px rgba(0,0,0,0.3);">
        <b>GPS Tracking Summary</b><br>
        Total Points: {len(points)}<br>
        Distance Traveled: {total_distance:.2f} meters<br>
        Start Time: {timestamps[0]}<br>
        Last Updated: {timestamps[-1]}<br>
    </div>
    """
    m.get_root().html.add_child(folium.Element(summary_html))

    # Controls
    folium.LayerControl().add_to(m)

    # Save and open
    m.save(MAP_FILE)
    if not map_initialized:
        webbrowser.open('file://' + os.path.realpath(MAP_FILE))
        map_initialized = True

def main():
    global gps_points, timestamps

    try:
        with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"\n📡 Listening on {COM_PORT} at {BAUD_RATE} baud...\n")

            while True:
                try:
                    line = ser.readline().decode('ascii', errors='replace').strip()

                    if line.startswith('$GPRMC'):
                        msg = pynmea2.parse(line)

                        if msg.status == 'A':
                            lat = msg.latitude
                            lon = msg.longitude
                            ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                            speed = float(msg.spd_over_grnd) * 1.852

                            print(f"📍 Fix: Lat={lat:.5f}, Lon={lon:.5f}, Speed={speed:.2f} km/h, Time={ts}")

                            gps_points.append((lat, lon))
                            timestamps.append(ts)
                            update_map(gps_points, timestamps)
                        else:
                            print("⚠️ No valid GPS fix yet...")

                except pynmea2.ParseError:
                    continue
                except UnicodeDecodeError:
                    continue

    except serial.SerialException:
        print(f"❌ Could not open port {COM_PORT}.")
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")

if __name__ == '__main__':
    main()
