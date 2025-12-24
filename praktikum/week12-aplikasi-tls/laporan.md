Minggu ke-: 12
Topik: Aplikasi TLS & E-commerce
Nama: purnomo yusgiantoro
NIM: 230202774
Kelas: 5ikra

---

## Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan konsep **Shamir Secret Sharing** (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  
---

## 2. Dasar Teori
Aplikasi TLS dan e-commerce berperan penting dalam menjaga keamanan komunikasi dan transaksi digital di internet. TLS (Transport Layer Security) digunakan untuk mengenkripsi data yang dikirim antara pengguna dan server, sehingga informasi sensitif seperti kata sandi, nomor kartu kredit, dan data pribadi tidak dapat dibaca atau dimodifikasi oleh pihak ketiga. Dalam konteks e-commerce, TLS memastikan bahwa transaksi pembayaran, autentikasi pengguna, dan pertukaran data berlangsung secara aman, menjaga kepercayaan pelanggan serta melindungi bisnis dari serangan seperti penyadapan (sniffing) dan man-in-the-middle.

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


---

## 7. Jawaban Pertanyaan
**1. Perbedaan utama antara HTTP dan HTTPS**  
Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mengirimkan data dalam bentuk teks biasa tanpa enkripsi, sehingga informasi mudah disadap atau dimanipulasi oleh pihak ketiga. Sebaliknya, HTTPS menggunakan TLS untuk mengenkripsi komunikasi antara klien dan server, sehingga data menjadi lebih aman, terjaga kerahasiaannya, dan integritasnya dapat dipastikan.

**2. Pentingnya sertifikat digital dalam komunikasi TLS**  
Sertifikat digital berfungsi untuk memverifikasi identitas server yang berkomunikasi dengan pengguna. Dalam TLS, sertifikat digital dikeluarkan oleh Certificate Authority (CA) yang tepercaya dan memastikan bahwa pengguna benar-benar terhubung ke server yang sah, bukan server palsu. Dengan adanya sertifikat ini, TLS dapat mencegah serangan *man-in-the-middle* serta membangun kepercayaan dalam komunikasi digital.

**3. Peran kriptografi terhadap privasi serta tantangan hukum dan etika**  
Kriptografi mendukung privasi dengan melindungi data dan komunikasi dari akses tidak sah, sehingga informasi pribadi dan sensitif tetap aman. Namun, kekuatan kriptografi juga menimbulkan tantangan hukum dan etika karena dapat digunakan untuk menyembunyikan aktivitas ilegal dari penegak hukum. Hal ini memunculkan dilema antara perlindungan hak privasi

individu dan kebutuhan negara untuk melakukan pengawasan demi keamanan publik.
)
---

## 8. Kesimpulan

Pada praktikum ini dapat disimpulkan bahwa TLS memiliki peran yang sangat penting dalam menjaga keamanan komunikasi dan transaksi pada sistem e-commerce melalui mekanisme enkripsi dan autentikasi. Selain itu, konsep Shamir Secret Sharing menunjukkan bahwa pembagian rahasia ke beberapa pihak dengan ambang batas tertentu dapat meningkatkan keamanan penyimpanan dan distribusi data sensitif. Penerapan kriptografi secara tepat mampu melindungi privasi pengguna sekaligus menjaga kepercayaan dalam aktivitas digital, meskipun tetap menimbulkan tantangan dari sisi hukum dan etika.

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
commit e2f3c017295a450f5fe1191bad7a6bf50f0e6c24
Author: purnomo yusgiantoro <pyxvin124@gmail.com>
Date:   Wed Dec 24 22:00:11 2025 +0700

    week12-aplikasi-tls

```
