# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)  
Nama: purnomo yusgiatoro  
NIM: 230202774  
Kelas: 5ikra  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

   1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
   2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
   3. Menghitung unicity distance untuk ciphertext tertentu.
   4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
   5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.



---

## 2. Dasar Teori
Entropy adalah ukuran tingkat ketidakpastian atau kerandoman dalam sebuah sistem kriptografi. Semakin tinggi nilai entropi sebuah kunci, semakin sulit kunci tersebut ditebak karena distribusi bit-nya semakin acak. Dalam konteks keamanan, entropi digunakan untuk menilai seberapa kuat kunci terhadap serangan brute force—semakin tinggi entropinya, semakin besar ruang kunci yang harus dicoba penyerang untuk menemukan kunci yang benar.

Unicity Distance adalah jumlah minimum ciphertext yang dibutuhkan agar kunci dapat diidentifikasi secara unik. Konsep ini menggambarkan batas di mana informasi dalam ciphertext cukup untuk menyingkirkan semua kemungkinan kunci palsu. Semakin panjang unicity distance, semakin kuat sistem kriptografi karena penyerang membutuhkan lebih banyak data terenkripsi untuk memecahkan kunci secara pasti melalui brute force atau analisis statistik.


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

```import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit") ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Entropy menunjukkan tingkat kerandoman kunci — semakin tinggi entropinya, semakin sulit kunci ditebak
- Pertanyaan 2: Unicity distance penting karena menentukan berapa banyak ciphertext yang dibutuhkan untuk memastikan kunci dapat dipecahkan secara unik.
- Pertanyaan 3: Brute force tetap ancaman karena jika panjang kunci lemah atau implementasi buruk, penyerang bisa mencoba semua kemungkinan hingga menemukan kunci yang benar.
)


---

## 8. Kesimpulan
Dari hasil eksekusi kode, dapat disimpulkan bahwa ruang kunci kecil seperti pada Caesar Cipher (26 kunci) memiliki entropi rendah dan unicity distance pendek, sehingga mudah dipecahkan dengan brute force hanya dalam waktu sangat singkat. Sebaliknya, algoritma modern seperti AES-128 memiliki entropi sangat tinggi dan unicity distance besar, membuatnya hampir mustahil dipecahkan dengan brute force karena membutuhkan waktu yang jauh melebihi umur alam semesta.

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
Date:   Sat Oct 25 19:04:35 2025 +0700

    week4-entropy-unicity

```
