# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern (DES, AES, RSA) 
Nama: purnomo yusgiantoro  
NIM: 230202774  
Kelas: 5ikra  

---

## 1. Tujuan
Mengimplementasikan algoritma DES untuk blok data sederhana.
Menerapkan algoritma AES dengan panjang kunci 128 bit.
Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
Cipher modern merupakan algoritma kriptografi yang digunakan untuk melindungi data digital dengan cara mengubah pesan asli (plaintext) menjadi bentuk terenkripsi (ciphertext) yang sulit dibaca tanpa kunci tertentu. Berbeda dengan cipher klasik yang hanya mengandalkan operasi sederhana seperti substitusi dan transposisi, cipher modern menggunakan operasi matematis kompleks dan kunci dengan panjang besar, sehingga lebih tahan terhadap serangan brute-force maupun analisis kripto.

DES (Data Encryption Standard) adalah algoritma simetris yang menggunakan kunci sepanjang 56 bit untuk mengenkripsi data dalam blok 64 bit. Meskipun dulu menjadi standar enkripsi pemerintah AS, kini DES dianggap kurang aman karena panjang kuncinya terlalu pendek dan rentan terhadap serangan brute-force. Sebagai penggantinya, digunakan AES (Advanced Encryption Standard), yang juga merupakan cipher simetris tetapi dengan panjang kunci 128, 192, atau 256 bit. AES dikenal cepat, efisien, dan aman, sehingga banyak dipakai pada sistem keamanan modern seperti Wi-Fi, VPN, dan enkripsi file.

Sementara itu, RSA (Rivest–Shamir–Adleman) merupakan algoritma asimetris yang menggunakan sepasang kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Keamanan RSA bergantung pada kesulitan faktorisasi bilangan besar menjadi dua bilangan prima. RSA banyak digunakan untuk pertukaran kunci dan tanda tangan digital, melengkapi cipher simetris seperti AES dalam sistem keamanan hybrid.


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
- Pertanyaan 1: DES dan AES merupakan algoritma enkripsi simetris, artinya proses enkripsi dan dekripsi menggunakan kunci yang sama. DES memiliki panjang kunci 56 bit sehingga mudah ditembus dengan brute-force di era komputasi modern. Sementara AES memiliki panjang kunci 128, 192, atau 256 bit, membuatnya jauh lebih aman dan efisien. Di sisi lain, RSA adalah algoritma asimetris, yang menggunakan dua kunci berbeda—kunci publik untuk enkripsi dan kunci privat untuk dekripsi—dengan keamanan bergantung pada kesulitan faktorisasi bilangan prima besar.

- Pertanyaan 2: AES lebih unggul karena memiliki struktur blok dan panjang kunci yang lebih besar, menjadikannya tahan terhadap serangan brute-force maupun analisis kripto. Selain itu, AES lebih efisien dalam perangkat keras maupun perangkat lunak, mampu memproses data lebih cepat dengan tingkat keamanan tinggi. DES dinilai sudah usang karena panjang kuncinya terlalu pendek dan telah berhasil dipecahkan dengan teknologi modern.

- Pertanyaan 3: RSA disebut asimetris karena menggunakan dua kunci berbeda—kunci publik (untuk mengenkripsi pesan) dan kunci privat (untuk mendekripsi pesan).

)

---

## 8. Kesimpulan
Berdasarkan hasil percobaan, ketiga algoritma modern—DES, AES, dan RSA—berhasil mengenkripsi dan mendekripsi data sesuai teori. DES menunjukkan proses enkripsi blok sederhana, AES memberikan hasil cepat dan efisien dengan tingkat keamanan tinggi, sedangkan RSA berhasil mengimplementasikan konsep kunci publik dan privat. Secara keseluruhan, percobaan ini membuktikan bahwa cipher modern mampu menjaga kerahasiaan data digital dengan mekanisme matematis yang kuat dan berbeda-beda sesuai karakteristik algoritmanya.


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
Author: purnomo yusgiantoro <pyxvin124@gmail.com>
Date:   Tue Nov 4 23:23:34 2025 +0700

    week6-cipher-modern

```
