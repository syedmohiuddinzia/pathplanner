## Fixed-Wing Drone Path Planning Tool
This project is a web-based path planning tool developed specifically for fixed-wing MALE (Medium Altitude Long Endurance) drones. It enables operators, engineers, or mission planners to efficiently design, analyze, and export waypoint-based routes tailored to the capabilities and operational needs of fixed-wing UAVs.

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
