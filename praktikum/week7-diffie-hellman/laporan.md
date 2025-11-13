# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange  
Nama: PUrnomo Yusgiantoro  
NIM: 230202774  
Kelas: 5ikra  

---

## 1. Tujuan
Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Diffie–Hellman adalah protokol untuk menghasilkan shared secret antara dua pihak melalui saluran publik. Secara matematis, protokol memakai sebuah bilangan prima p dan sebuah generator g dari grup perkalian modulo p. Dua pihak, sebut saja Alice dan Bob, masing-masing memilih bilangan privat a dan b. Alice menghitung nilai publik A = g^a mod p dan mengirimkan A kepada Bob. Bob menghitung nilai publik B = g^b mod p dan mengirimkan B kepada Alice.

Setelah pertukaran, Alice menggunakan B dan kunci privatnya a untuk menghitung shared secret s = B^a mod p. Bob menggunakan A dan kunci privatnya b untuk menghitung s = A^b mod p. Karena sifat perpangkatan modulo, kedua perhitungan identik: s = g^(a b) mod p. Dengan kata lain:
A = g^a mod p
B = g^b mod p
s = B^a mod p = A^b mod p = g^(a b) mod p

Shared secret s biasanya bukan langsung dipakai sebagai kunci enkripsi; s dikonversi menjadi kunci simetris yang aman melalui fungsi derivasi kunci (KDF), misalnya k = KDF(s) atau k = H(s) dengan hash seperti SHA-256.

Keamanan DH bergantung pada kesulitan masalah logaritma diskrit: diberi g dan g^x mod p, sulit (untuk p yang besar) menebak x. Namun DH sendiri tidak mengautentikasi lawan bicara. Ancaman paling nyata adalah Man-in-the-Middle (MITM): penyerang Mallory mengintersep A dan B dan menggantinya dengan A' dan B' yang dibuat Mallory. Akibatnya Alice menghitung shared secret dengan Mallory (bukan dengan Bob), dan Bob juga menghitung secret berbeda dengan Mallory. Mallory bisa menghitung kedua secret sehingga dapat membaca/memodifikasi pesan.


---


---


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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
