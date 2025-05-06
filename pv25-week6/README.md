# Font Size and Color Adjuster (pv25-week6)

Aplikasi ini dibuat menggunakan **PyQt5** untuk memenuhi tugas minggu ke-6 mata kuliah _Pemrograman Visual 2025_. Aplikasi ini memungkinkan pengguna untuk menyesuaikan ukuran font, warna font, dan warna latar belakang dari label yang menampilkan NIM mahasiswa.

- **Nama:** Muhammad Rizki Assamsuli
- **NIM:** F1D022146

---

## 🎯 Tujuan Aplikasi

Membuat antarmuka interaktif dengan komponen PyQt5 seperti:

- `QLabel` untuk menampilkan teks.
- `QSlider` untuk mengatur properti tampilan secara real-time.
- Pemisahan antara **UI** dan **logic aplikasi** untuk menjaga struktur kode tetap rapi dan modular.

---

## 🛠️ Fitur Aplikasi

1. **Menampilkan NIM di tengah layar** dengan latar belakang hitam.
2. **3 Slider kontrol utama:**
   - **Font Size Slider**: Mengubah ukuran huruf antara 20 - 60 pt.
   - **Background Color Slider**: Mengatur intensitas warna latar belakang label dalam skala grayscale (0 - 255).
   - **Font Color Slider**: Mengubah warna huruf dalam skala grayscale (0 - 255).
3. **Label watermark** di bawah aplikasi yang menampilkan nama dan NIM.

---

## 🧩 Alur Kerja Aplikasi

1. Aplikasi dijalankan dan jendela ut ama ditampilkan.
2. Teks NIM (`QLabel`) ditampilkan di tengah dengan latar belakang hitam.
3. Saat pengguna menggeser:
   - **Font Size Slider** → Ukuran teks pada label berubah sesuai nilai slider (20–60 pt).
   - **Background Color Slider** → Background `QLabel` berubah dari hitam ke putih (skala grayscale).
   - **Font Color Slider** → Warna teks berubah dari hitam ke putih (skala grayscale).
4. Semua perubahan bersifat **real-time** dan langsung terlihat saat slider digerakkan.

---

## 📷 Hasil Run Aplikasi

![Hasil Run](resultProgram1.png)
