## Fixed-Wing Drone Path Planning Tool
This project is a web-based path planning tool developed specifically for fixed-wing MALE (Medium Altitude Long Endurance) drones. It enables operators, engineers, or mission planners to efficiently design, analyze, and export waypoint-based routes tailored to the capabilities and operational needs of fixed-wing UAVs.
![Image0](https://github.com/syedmohiuddinzia/pathplanner/blob/main/img/0.png)

### Key Features
- **Intuitive Web Interface:** Plan and edit waypoint routes using an easy-to-use browser interface. Waypoints can be computed based on distances and bearings, or entered directly with altitude information.
- **Customizable Waypoint Input:** Input and modify latitude, longitude, and altitude for each waypoint. The tool supports both manual entry and automated calculations based on flight geometry.
- **Automated Geodetic Calculations:** The application computes distances and bearings between waypoints using the haversine formula and can calculate new waypoint positions given a starting point, bearing, and distance.
- **Instant Visualization:** View the planned route and waypoints on an interactive Cesium 3D globe. Waypoints are shown with precise geographic positioning and altitude, with the ability to click on the map for live coordinate feedback.
- **Waypoint Management:** Easily append new waypoints based on computed results, and remove the last waypoint if needed.
- **Data Export:** Waypoints are saved in a standard JSON format, ready for export or integration with flight control software for actual mission upload to the UAV.

### Use Case
Designed for medium and long-range fixed-wing drones, such as MALE platforms used in surveillance, mapping, or scientific missions, this tool streamlines the crucial pre-flight planning stage. It supports the creation of safe, efficient, and airspace-compliant paths that respect the kinematic and altitude constraints of fixed-wing UAVs (such as minimum turning radius, cruising altitude, and waypoint spacing).

### Technical Highlights
- **Flask** is used for the backend, serving the application and managing waypoint data.
- **CesiumJS** powers the interactive globe, offering a modern, map-based visualization.
- **Geodetic calculations** are performed in Python, ensuring accurate distances and bearings for global operations.

### Intended Audience
This planner is ideal for:
-UAV mission planners
- Fixed-wing drone pilots/operators
- Engineers developing autonomous mission profiles
- Educators and researchers in unmanned aerial systems


## Working
- Install requirements for the software ```pip install -r requirements.txt```
- Create a cesium account and copy [API key](https://ion.cesium.com/tokens)
- Clone project [https://github.com/syedmohiuddinzia/pathplanner](https://github.com/syedmohiuddinzia/pathplanner)
```bash
git clone https://github.com/syedmohiuddinzia/pathplanner
```
- Open directory
```bash
cd pathplanner
```  
- Open **templates/cesium_map.html**
```bash
nano templates/cesium_map.html
```
- Paste API key instead of **API_KEY**
```html
Cesium.Ion.defaultAccessToken = 'API_KEY';
```
- Now run the application in terminal
```bash
python app.py
```
- The application will show something similar
```bash
smzia@smzia-LOQ:~/pathplanner$ python app.py 
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (inotify)
 * Debugger is active!
 * Debugger PIN: 113-524-878\
```
- Copy server link found in the terminal 
```text
http://127.0.0.1:5000
```
- Paste in any browser and enjoy the application locally
