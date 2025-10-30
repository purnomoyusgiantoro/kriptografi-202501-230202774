# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: purnomo yusgiantoro  
NIM: 230202774  
Kelas: 5ikra  

---

## 1. Tujuan
   1 Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
   2 Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
   3 Mengimplementasikan algoritma transposisi sederhana.
   4 Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Cipher klasik merupakan metode penyandian pesan yang digunakan sebelum era komputer modern. Tujuannya adalah mengubah teks asli plaintext menjadi bentuk terenkripsi ciphertext agar tidak mudah dipahami oleh pihak yang tidak berwenang. Metode ini berfokus pada dua prinsip dasar: substitusi (penggantian huruf dengan huruf lain) dan transposisi (penyusunan ulang posisi huruf).

Cipher Caesar adalah bentuk paling sederhana dari cipher substitusi. Dalam metode ini, setiap huruf digeser sejumlah tertentu dalam alfabet. Misalnya, pergeseran tiga huruf membuat A menjadi D, B menjadi E, dan seterusnya. Meskipun mudah diterapkan, cipher Caesar sangat lemah karena hanya memiliki 25 kemungkinan kunci sehingga mudah dipecahkan melalui analisis frekuensi huruf.

Cipher Vigenère merupakan pengembangan dari Caesar dengan menggunakan kata kunci untuk menentukan pergeseran huruf secara berulang. Setiap huruf kunci menentukan jumlah pergeseran yang berbeda, sehingga pola enkripsi menjadi lebih kompleks dan sulit ditebak. Sementara itu, Cipher Transposisi bekerja dengan cara menyusun ulang posisi huruf pada pesan asli tanpa mengubah huruf itu sendiri. Contohnya, huruf-huruf bisa ditulis dalam bentuk tabel dan dibaca dalam urutan kolom tertentu. Ketiga cipher ini menjadi dasar dari banyak algoritma kriptografi modern, meskipun kini dianggap tidak cukup aman untuk penggunaan praktis.



---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan

Program di atas mengimplementasikan tiga jenis cipher klasik: Caesar, igenère, dan Transposisi. Pada pengujian, teks `"CLASSIC CIPHER"` dengan kunci `3` menghasilkan ciphertext `"FODVVLF FLSKHU"`, lalu berhasil didekripsi kembali ke teks asli. Cipher Vigenère dengan plaintext `"KRIPTOGRAFI"` dan kunci `"KEY"` menghasilkan ciphertext `"UVSDXSYVEBKM"`, juga dapat didekripsi sempurna. Cipher Transposisi dengan pesan `"TRANSPOSITIONCIPHER"` dan kunci `5` menghasilkan ciphertext `"TPTNHIAROSOCEINPSIC"`, yang juga berhasil dikembalikan ke bentuk aslinya. Hasil ini menunjukkan bahwa ketiga algoritma dapat bekerja dengan baik untuk enkripsi dan dekripsi, namun tetap tergolong tidak aman karena pola huruf masih bisa dianalisis dengan teknik kriptanalisis klasik seperti frequency analysis atau pattern matching.

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1: Caesar Cipher lemah karena ruang kuncinya kecil dan mudah ditebak. Vigenère Cipher lebih kuat, tapi bisa ditembus jika kuncinya pendek atau berulang, menggunakan analisis seperti Kasiski.
- Pertanyaan 2: Karena pola kemunculan huruf (seperti huruf “E” yang sering muncul) tetap terlihat di ciphertext, sehingga mudah ditebak.
- Pertanyaan 3: Substitusi: Ganti huruf → pola frekuensi tetap, urutan sama.
Transposisi: Urutan huruf diacak → frekuensi tetap, isi tidak berubah.
Keduanya mudah dipecahkan karena masih menyimpan pola bahasa asli.

---

## 8. Kesimpulan
Ketiga algoritma — Caesar Cipher, Vigenère Cipher, dan Transposisi Cipher— berhasil melakukan proses enkripsi dan dekripsi dengan benar, menunjukkan prinsip dasar kriptografi klasik berjalan baik. Namun, dari sisi keamanan, cipher klasik ini tergolong lemah karena pola huruf dan struktur bahasa asli masih dapat dianalisis. Oleh karena itu, meskipun berguna untuk pembelajaran konsep dasar enkripsi, algoritma ini tidak cocok digunakan dalam sistem keamanan modern.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
Author: purnomo <purnomo@purnomo-Mybook-14E>
Date:   Thu Oct 30 14:29:14 2025 +0700

    week5-cipher-klasik

```
