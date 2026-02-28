# We import Flask and the tools we need from it.
# Flask is the framework itself.
# request lets us read data sent FROM the frontend (like form submissions).
# jsonify converts Python dictionaries/lists into JSON format that browsers understand.
from flask import Flask, request, jsonify

# CORS (Cross-Origin Resource Sharing) allows your HTML pages to talk to this
# Flask server even though they're on different ports. Without this, the browser
# would block all your fetch() calls as a security measure.
from flask_cors import CORS

# json is Python's built-in library for reading and writing .json files.
import json

# os lets us build file paths that work on both Windows and Mac.
import os

# This creates your Flask application. __name__ just tells Flask
# "this file is the main application file."
app = Flask(__name__)

# This enables CORS for ALL routes in your app.
CORS(app)

# ── FILE PATHS ──────────────────────────────────────────────────────────────
# We build the path to our JSON files relative to where app.py lives.
# This means it works no matter what computer you run it on.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GIGS_FILE = os.path.join(BASE_DIR, "gigs.json")
APPLICATIONS_FILE = os.path.join(BASE_DIR, "applications.json")

# ── HELPER FUNCTIONS ────────────────────────────────────────────────────────
# These two functions handle reading and writing JSON files.
# We reuse them in every route so we don't repeat the same code.

def read_json(filepath):
    # If the file doesn't exist yet (like applications.json on first run),
    # return an empty list instead of crashing.
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def write_json(filepath, data):
    with open(filepath, "w") as f:
        # indent=2 makes the JSON file human-readable with nice formatting.
        json.dump(data, f, indent=2)

# ── ROUTE 1: GET /gigs ───────────────────────────────────────────────────────
# This is the most important route. When your browse.html page calls
# fetch("http://localhost:5000/gigs"), THIS function runs.
# It reads all gigs from gigs.json and sends them back as JSON.
@app.route("/gigs", methods=["GET"])
def get_gigs():
    gigs = read_json(GIGS_FILE)
    return jsonify(gigs)

# ── ROUTE 2: POST /gigs ──────────────────────────────────────────────────────
# When an employer fills in the Post a Gig form and clicks submit,
# the frontend sends the form data here. This route receives it,
# adds a new ID and timestamp, and saves it into gigs.json.
@app.route("/gigs", methods=["POST"])
def post_gig():
    gigs = read_json(GIGS_FILE)
    
    # request.json reads the data sent by the frontend as a Python dictionary.
    new_gig = request.json
    
    # We auto-generate the ID based on how many gigs already exist.
    new_gig["id"] = str(len(gigs) + 1)
    from datetime import date
    new_gig["timestamp"] = str(date.today())   # adds today's date automatically
    gigs.append(new_gig)
    write_json(GIGS_FILE, gigs)
    
    # We send back the new gig and a 201 status code.
    # 201 means "Created" — it's the correct HTTP response for new data.
    return jsonify(new_gig), 201

# ── ROUTE 3: POST /apply ─────────────────────────────────────────────────────
# When a student fills in the Apply form and clicks submit,
# the frontend sends their application here. This saves it
# to applications.json linked to the gig they applied for.
@app.route("/apply", methods=["POST"])
def apply_to_gig():
    applications = read_json(APPLICATIONS_FILE)
    
    new_application = request.json
    new_application["id"] = str(len(applications) + 1)
    
    applications.append(new_application)
    write_json(APPLICATIONS_FILE, applications)
    
    return jsonify(new_application), 201

# ── ROUTE 4: GET /applications ───────────────────────────────────────────────
# This lets an employer see all students who applied to a specific gig.
# The gig_id comes from the URL — for example: /applications?gig_id=1
@app.route("/applications", methods=["GET"])
def get_applications():
    # request.args reads query parameters from the URL.
    gig_id = request.args.get("gig_id")
    applications = read_json(APPLICATIONS_FILE)
    
    if gig_id:
        # Filter to only return applications for the requested gig.
        filtered = [a for a in applications if a.get("gig_id") == gig_id]
        return jsonify(filtered)
    
    # If no gig_id was specified, return all applications.
    return jsonify(applications)

# ── START THE SERVER ─────────────────────────────────────────────────────────
# This is the entry point. When she runs "python app.py" in the terminal,
# Python reaches this line and starts the Flask server.
# debug=True means Flask will automatically restart whenever she saves a change
# — she won't need to stop and restart the server manually every time.
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
    


