from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder untuk menyimpan file yang diunggah
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Data terbaru yang akan ditampilkan di halaman utama
latest_data = {
    "image_path": None,
    "cuaca_label": None,
    "cuaca_acc": None,
    "awan_label": None,
    "awan_acc": None,
    "visibility": None,
    "status": None
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', **latest_data)

@app.route('/awan', methods=['GET'])
def awan():
    return render_template('awan.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify(status="error", message="No image part in the request"), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify(status="error", message="No selected file"), 400

    # Simpan gambar
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    # Ambil semua data dari form
    cuaca_label = request.form.get('label', 'Tidak Diketahui')
    cuaca_acc = request.form.get('accuracy', 0)
    awan_label = request.form.get('cloud', 'Tidak Diketahui')
    awan_acc = request.form.get('cloud_acc', 0)
    visibility = request.form.get('visibility', 'Tidak Diketahui')
    status = request.form.get('status', 'Tidak Diketahui')

    # Konversi akurasi menjadi float
    try:
        cuaca_acc = float(cuaca_acc)
    except ValueError:
        cuaca_acc = 0.0

    try:
        awan_acc = float(awan_acc)
    except ValueError:
        awan_acc = 0.0

    # Update data
    latest_data.update({
        "image_path": filename,
        "cuaca_label": cuaca_label,
        "cuaca_acc": cuaca_acc,
        "awan_label": awan_label,
        "awan_acc": awan_acc,
        "visibility": visibility,
        "status": status
    })

    return jsonify(status="ok", message="Data berhasil diterima")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
