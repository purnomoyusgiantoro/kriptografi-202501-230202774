# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: Digital Signature (RSA/DSA)
Nama: purnomo yusgiantoro
NIM: 230202774
Kelas: 5ikra

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

    Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
    Memverifikasi keaslian tanda tangan digital.
    Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

## 2. Dasar Teori
Digital Signature merupakan mekanisme kriptografi yang digunakan untuk menjamin keaslian (authentication) keutuhan data (integrity), dan non-repudiation pada suatu pesan atau dokumen digital. Algoritma digital signature yang umum digunakan adalah RSA dan DSA, yang keduanya berbasis kriptografi kunci publik. Pada proses penandatanganan, pengirim membuat tanda tangan digital dengan menggunakan kunci privat, sedangkan penerima memverifikasinya menggunakan kunci publik. RSA digital signature bekerja dengan melakukan operasi matematika eksponensial modular pada nilai hash pesan, sementara DSA menggunakan konsep logaritma diskrit dan bilangan acak dalam proses pembuatannya. Dengan penerapan digital signature berbasis RSA atau DSA, keamanan komunikasi digital dapat ditingkatkan karena pesan yang dikirim tidak dapat diubah tanpa terdeteksi dan identitas pengirim dapat dipastikan secara kriptografis.


---



## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())


```

---


## 7. Jawaban Pertanyaan
1. Perbedaan enkripsi RSA dan tanda tangan digital RSA
Enkripsi RSA bertujuan menjaga kerahasiaan pesan dengan menggunakan kunci publik penerima, sedangkan tanda tangan digital RSA bertujuan menjamin keaslian dan integritas pesan dengan menggunakan kunci privat pengirim.

2. Alasan tanda tangan digital menjamin integritas dan otentikasi
Karena tanda tangan dibuat dari hash pesan dan hanya dapat dibuat oleh pemilik kunci privat, sehingga perubahan pesan dapat terdeteksi dan identitas pengirim dapat dipastikan.

3. Peran Certificate Authority (CA)
CA adalah pihak tepercaya yang memverifikasi identitas dan menerbitkan sertifikat digital untuk memastikan kunci publik benar-benar milik pemilik yang sah.


---

## 8. Kesimpulan
Berdasarkan hasil pengujian, tanda tangan digital RSA berhasil dibuat menggunakan kunci privat dan dapat diverifikasi dengan benar menggunakan kunci publik selama pesan tidak mengalami perubahan. Verifikasi yang berhasil membuktikan bahwa pesan asli memiliki integritas terjaga dan benar berasal dari pemilik kunci privat. Ketika pesan dimodifikasi, proses verifikasi gagal, yang menunjukkan bahwa tanda tangan digital mampu mendeteksi perubahan data dan memastikan keaslian pesan, sehingga efektif untuk menjamin keamanan dan kepercayaan dalam komunikasi digital.


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
