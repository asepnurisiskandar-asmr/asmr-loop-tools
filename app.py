from flask import Flask, request, send_file, render_template_string
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

app = Flask(__name__)

HTML = """
<!doctype html>
<title>ASMR Loop Tool</title>
<h2>ASMR Smooth Loop Video Tool</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=video required>
  <br><br>
  Durasi akhir (menit): <input type=number name=minutes value=10>
  <br><br>
  <input type=submit value="Render Video">
</form>
{% if done %}
<br>
<a href="/download">Download Video</a>
{% endif %}
"""

OUTPUT = "output.mp4"

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        f = request.files["video"]
        minutes = int(request.form
