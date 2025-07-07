from flask import Flask, render_template, request, redirect, url_for, jsonify
import math
import os
import json

app = Flask(__name__)
WAYPOINT_FILE = "waypoints.json"

# Earth radius in meters
R = 6371000

@app.template_filter('waypoints_inline_json')
def waypoints_inline_json(waypoints):
    lines = []
    for wp in waypoints:
        line = f'  {{ "lat": {wp["lat"]}, "lon": {wp["lon"]}, "alt": {wp["alt"]} }}'
        lines.append(line)
    return '[\n' + ',\n'.join(lines) + '\n]'

def haversine(lat1, lon1, lat2, lon2):
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2*R*math.asin(math.sqrt(a))

def bearing(lat1, lon1, lat2, lon2):
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dlambda = math.radians(lon2 - lon1)
    y = math.sin(dlambda) * math.cos(phi2)
    x = math.cos(phi1)*math.sin(phi2) - math.sin(phi1)*math.cos(phi2)*math.cos(dlambda)
    angle = math.atan2(y, x)
    return (math.degrees(angle) + 360) % 360

def destination_point(lat1, lon1, distance, bearing_deg):
    bearing = math.radians(bearing_deg)
    phi1 = math.radians(lat1)
    lambda1 = math.radians(lon1)
    delta = distance / R
    phi2 = math.asin(math.sin(phi1)*math.cos(delta) + math.cos(phi1)*math.sin(delta)*math.cos(bearing))
    lambda2 = lambda1 + math.atan2(math.sin(bearing)*math.sin(delta)*math.cos(phi1),
                                   math.cos(delta)-math.sin(phi1)*math.sin(phi2))
    return math.degrees(phi2), math.degrees(lambda2)

@app.route("/", methods=["GET", "POST"])
def index():
    # For Column 1
    lat1 = request.form.get("lat1", "")
    lon1 = request.form.get("lon1", "")
    alt1 = request.form.get("alt1", "")
    lat2 = request.form.get("lat2", "")
    lon2 = request.form.get("lon2", "")
    alt2 = request.form.get("alt2", "")
    dist1 = request.form.get("dist1", "")
    ang1 = request.form.get("ang1", "")

    # For Column 2
    lat1b = request.form.get("lat1b", "")
    lon1b = request.form.get("lon1b", "")
    alt1b = request.form.get("alt1b", "")
    dist2 = request.form.get("dist2", "")
    ang2 = request.form.get("ang2", "")
    alt2b = request.form.get("alt2b", "")
    lat2b = ""
    lon2b = ""

    result_dist, result_ang = "", ""

    msg = ""
    if request.method == "POST":
        action = request.form.get("action")
        # Column 1: Compute distance/angle
        if action == "compute_dist_angle":
            try:
                result_dist = haversine(float(lat1), float(lon1), float(lat2), float(lon2))
                result_ang = bearing(float(lat1), float(lon1), float(lat2), float(lon2))
            except Exception as e:
                msg = f"Error: {e}"
        elif action == "remove_last":
            try:
                if os.path.exists(WAYPOINT_FILE):
                    with open(WAYPOINT_FILE) as f:
                        waypoints = json.loads(f.read())
                else:
                    waypoints = []
                if waypoints:
                    waypoints.pop()
                    with open(WAYPOINT_FILE, "w") as f:
                        f.write('[\n')
                        for i, wp in enumerate(waypoints):
                            line = f'  {{ "lat": {wp["lat"]}, "lon": {wp["lon"]}, "alt": {wp["alt"]} }}'
                            if i != len(waypoints) - 1:
                                line += ','
                            f.write(line + '\n')
                        f.write(']')
                    msg = "Last waypoint removed."
                else:
                    msg = "No waypoints to remove."
            except Exception as e:
                msg = f"Error: {e}"

        # Column 2: Compute Lat2/Lon2 from Lat1, Lon1, Distance, Angle
        elif action == "compute_latlon":
            try:
                lat2b, lon2b = destination_point(float(lat1b), float(lon1b), float(dist2), float(ang2))
                # Append as a new waypoint
                alt2b_val = float(alt2b) if alt2b else 0.0
                if os.path.exists(WAYPOINT_FILE):
                    with open(WAYPOINT_FILE) as f:
                        waypoints = json.loads(f.read())
                else:
                    waypoints = []
                waypoints.append({"lat": lat2b, "lon": lon2b, "alt": alt2b_val})
                with open(WAYPOINT_FILE, "w") as f:
                    f.write('[\n')
                    for i, wp in enumerate(waypoints):
                        line = f'  {{ "lat": {wp["lat"]}, "lon": {wp["lon"]}, "alt": {wp["alt"]} }}'
                        if i != len(waypoints) - 1:
                            line += ','
                        f.write(line + '\n')
                    f.write(']')
                msg = "Waypoint computed and appended."
            except Exception as e:
                msg = f"Error: {e}"


    # List current waypoints
    if os.path.exists(WAYPOINT_FILE):
        with open(WAYPOINT_FILE) as f:
            waypoints = json.loads(f.read())
    else:
        waypoints = []

    return render_template("index.html",
        lat1=lat1, lon1=lon1, alt1=alt1, lat2=lat2, lon2=lon2, alt2=alt2, result_dist=result_dist, result_ang=result_ang,
        lat1b=lat1b, lon1b=lon1b, alt1b=alt1b, dist2=dist2, ang2=ang2, alt2b=alt2b, lat2b=lat2b, lon2b=lon2b, msg=msg,
        waypoints=waypoints)

@app.route("/waypoints.json")
def waypoints():
    if os.path.exists(WAYPOINT_FILE):
        with open(WAYPOINT_FILE) as f:
            return jsonify(json.loads(f.read()))
    return jsonify([])

@app.route("/cesium")
def cesium_map():
    return render_template("cesium_map.html")

if __name__ == "__main__":
    app.run(debug=True)

