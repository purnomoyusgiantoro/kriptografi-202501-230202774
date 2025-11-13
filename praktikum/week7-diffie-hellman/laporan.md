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

```p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob
 ...
```
)


---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Karena Diffie–Hellman menggunakan operasi matematika berupa perpangkatan modular dengan bilangan prima besar, yang didasarkan pada kesulitan logaritma diskrit.Hanya pihak yang memiliki eksponen rahasia masing-masing yang dapat menghitung shared secret
- Pertanyaan 2: Kelemahan utama protokol Diffie–Hellman murni adalah tidak adanya autentikasi. Protokol ini hanya menjamin bahwa dua pihak dapat menghasilkan kunci yang sama, tetapi tidak dapat memastikan dengan siapa mereka berkomunikasi. Akibatnya, penyerang dapat menyusup di tengah komunikasi dan melakukan serangan Man-in-the-Middle (MITM) dengan berpura-pura menjadi pihak yang sah bagi kedua belah pihak.
- Pertanyaan 3: Menggunakan sertifikat digital dan Public Key Infrastructure (PKI) untuk memverifikasi identitas pihak yang berkomunikasi, Menandatangani nilai publik Diffie–Hellman, Menggunakan Ephemeral Diffie–Hellman (DHE/ECDHE) agar setiap sesi memiliki kunci sementara (session key) baru.


)
---

## 8. Kesimpulan

Protokol Diffie–Hellman merupakan dasar penting dalam sistem kriptografi modern untuk pertukaran kunci rahasia melalui saluran publik tanpa harus mengirimkan kunci secara langsung. Mekanisme ini memanfaatkan konsep perpangkatan modular dan kesulitan logaritma diskrit sehingga sangat sulit bagi pihak ketiga untuk menebak kunci rahasia yang dihasilkan.

Namun, kelemahan utama Diffie–Hellman adalah tidak adanya proses autentikasi, sehingga rentan terhadap serangan *Man-in-the-Middle (MITM)* apabila nilai publik dapat dimodifikasi oleh penyerang. Oleh karena itu, penerapan autentikasi tambahan seperti tanda tangan digital atau sertifikat digital sangat diperlukan agar komunikasi benar-benar aman.

Dengan penggunaan parameter bilangan prima yang besar, penerapan *ephemeral key* (kunci sementara per sesi), dan penggabungan dengan protokol keamanan seperti TLS atau ECDHE, Diffie–Hellman mampu memberikan kerahasiaan, integritas, dan keamanan komunikasi yang kuat dalam berbagai aplikasi kriptografi modern.



---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
Author: purnomo yusgiantoro <pyxvin124@gmail.com>
Date:   Thu Nov 13 23:53:51 2025 +0700

    week7-diffie-hellman
```
