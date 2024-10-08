from flask import Flask, render_template, request, redirect, url_for, flash
from flask_htmx import HTMX
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a strong secret key
htmx = HTMX(app)

# Cloudinary configuration
cloudinary.config(
    cloud_name="dq1sftvg7",
    api_key="698374586166968",
    api_secret="Y2qenB92c4abxclLrJjPI6N1mX8",
    secure=True
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Upload the image to Cloudinary
    try:
        upload_result = cloudinary.uploader.upload(file)
        return render_template('partials/upload_response.html', upload_result=upload_result)
    except Exception as e:
        flash(str(e))
        return redirect(request.url)


@app.route('/get-response')
def get_response():
    return render_template('partials/response.html')


if __name__ == '__main__':
    app.run(debug=True)
