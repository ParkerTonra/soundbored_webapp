from flask import Flask, render_template

app = Flask("Soundbored")

from app import routes

@app.template_filter('strip_extension')
def strip_extension_filter(s):
    return s.split('.')[0]