# 🌦️ Sistem Pemantauan Cuaca Real-Time Berbasis Raspberry Pi 5

## 📌 Abstrak
**RANCANG BANGUN SISTEM PEMANTAUAN CUACA REAL-TIME BERBASIS RASPBERRY PI 5 DENGAN INTEGRASI MODEL MOBILENETV2, CUSTOM CNN, DAN YOLOV5 UNTUK KLASIFIKASI AWAN, CUACA, DAN ESTIMASI VISIBILITY BERBASIS CITRA KAMERA TERINTEGRASI WEBSITE**  
**Oleh: Made Jaya Setiawan**

Penelitian ini bertujuan untuk merancang dan membangun sistem pemantauan cuaca real-time berbasis Raspberry Pi 5 dengan integrasi model **MobileNetV2**, **Custom CNN**, dan **YOLOv5**. Sistem ini memanfaatkan citra kamera untuk:
- Mengklasifikasikan jenis awan  
- Mendeteksi kondisi cuaca  
- Mengestimasi visibility  

Seluruh hasil analisis ditampilkan melalui **website lokal** yang dapat diakses oleh berbagai perangkat.  
Estimasi visibility menggunakan kombinasi metode **YOLOv5 (object detection)** dan **Laplacian Variance** (analisis ketajaman, kontras, keburaman).  

### 🎯 Hasil Pengujian
- **YOLOv5 (estimasi visibility):** Akurasi 95% dibanding data BMKG  
- **Custom CNN (klasifikasi cuaca):** Akurasi 70%  
- **MobileNetV2 (klasifikasi awan):** Akurasi 10% → tetap dipakai karena efisien untuk perangkat IoT  

Dengan integrasi pemrosesan citra dan antarmuka website, sistem ini mampu memberikan solusi pemantauan cuaca mandiri yang efisien, cepat, dan mudah diakses dalam jaringan terbatas.  

**Kata kunci:** Raspberry Pi 5, MobileNetV2, Custom CNN, YOLOv5  

---

## ⚙️ Fitur Utama
- 📷 Pengambilan citra menggunakan kamera Raspberry Pi 5  
- 🤖 Klasifikasi cuaca (Custom CNN)  
- ☁️ Klasifikasi awan (MobileNetV2)  
- 👁️ Estimasi visibility (YOLOv5 + Laplacian Variance)  
- 🌐 Website lokal untuk monitoring real-time  

---

## 🛠️ Teknologi yang Digunakan
- **Hardware:** Raspberry Pi 5, Kamera  
- **Machine Learning Models:** MobileNetV2, Custom CNN, YOLOv5  
- **Backend/Server:** Python, Flask/Django (sesuaikan dengan implementasi)  
- **Frontend:** HTML, CSS, JavaScript (Website Lokal)  

---

## 🚀 Cara Menjalankan
1. Clone repository ini  
   ```bash
   git clone https://github.com/MadeJaya755/SKRIPSI_Made_Jaya.git
   cd SKRIPSI_Made_Jaya
