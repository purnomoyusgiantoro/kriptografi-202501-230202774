# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik:Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit) 
Nama: purnomo yusgiantoro  
NIM: 2302020774  
Kelas: 5ikra   

---

## 1. Tujuan

   1 Menyelesaikan operasi aritmetika modular.
   2 Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
   3 Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.


---

## 2. Dasar Teori

Aritmetika modular adalah cara menghitung dengan sisa pembagian. Misalnya setelah hasil operasi, nilainya dikembalikan ke sisa tertentu agar tetap dalam batas yang ditentukan.

Algoritma Euclidean digunakan untuk mencari pembagi terbesar dari dua angka (GCD). Cara kerjanya dengan membagi berulang sampai sisa pembagiannya nol.

Bilangan prima adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri. Logaritma diskrit adalah proses mencari pangkat dari suatu bilangan agar hasilnya sama dengan bilangan lain pada sistem modular.
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
- Pertanyaan 1:Aritmetika modular menjadi dasar hampir semua algoritma kriptografi modern. Sistem ini memastikan setiap hasil perhitungan tetap berada dalam rentang bilangan tertentu tanpa meluap, sehingga aman dan efisien digunakan pada komputer. Dalam kriptografi, operasi seperti enkripsi dan dekripsi dilakukan dengan perkalian atau perpangkatan dalam sistem modular, yang membuat hasilnya sulit ditebak meskipun diketahui sebagian informasi.  
- Pertanyaan 2:Invers modular dipakai untuk menemukan kunci dekripsi dalam sistem RSA. Setelah memilih dua bilangan prima dan menghasilkan nilai publik e, kita perlu mencari bilangan yang menjadi invers modular dari e terhadap p−1)(q−1)itulah pesan bisa didekripsi kembali. Tanpa invers modular, proses membuka pesan terenkripsi menjadi tidak mungkin dilakukan.
- Pertanyaan 3:Tantangan utamanya adalah tingkat kesulitannya meningkat sangat cepat ketika modulus menjadi besar. Tidak ada algoritma efisien yang bisa menyelesaikan logaritma diskrit dengan cepat untuk bilangan besar (misalnya ratusan digit)  
)
---

## 8. Kesimpulan
Berdasarkan percobaan, dapat disimpulkan bahwa operasi aritmetika modular seperti penjumlahan, perkalian, dan perpangkatan dapat dihitung dengan mudah menggunakan fungsi modular di Python. Algoritma Euclidean mampu menentukan GCD secara efisien, sedangkan algoritma Euclidean yang diperluas dapat digunakan untuk mencari invers modular. Selain itu, simulasi logaritma diskrit menunjukkan bagaimana nilai pangkat dapat ditemukan dalam sistem modular, yang menjadi dasar penting dalam kriptografi modern.

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
Date:   Sat Oct 18 18:58:57 2025 +0700

    week3-modmath-gcd

```
