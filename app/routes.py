from flask import render_template, redirect, url_for, request, flash, send_from_directory, make_response
from app import app
import os

@app.after_request
def apply_frame_options(response):
    response.headers["X-Frame-Options"] = "ALLOWALL"
    return response

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    # get files in folder \static\sounds
    sound_dir = os.path.join(app.static_folder, 'sounds')
    sound_files = [f for f in os.listdir(sound_dir) if os.path.isfile(os.path.join(sound_dir, f))]
    return render_template('index.html', sounds=sound_files)

#Route to play a sound when a button is pressed
@app.route('/play_sound/<filename>')
def play_sound(filename):
    return send_from_directory(os.path.join(app.static_folder, 'sounds'), filename)