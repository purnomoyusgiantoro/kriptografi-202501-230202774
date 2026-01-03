# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: Analisis Serangan Kriptografi
Nama: purnomo yusgiantoro
NIM: 230202774
Kelas: 5ikra

---

## 1. Tujuan

    Mengidentifikasi jenis serangan pada sistem informasi nyata.
    Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
    Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori

Dalam sistem informasi nyata, terdapat berbagai jenis serangan yang umum terjadi, seperti man-in-the-middle, brute force, phishing, dan replay attack. Serangan man-in-the-middle memungkinkan penyerang menyadap atau memodifikasi komunikasi antara dua pihak, terutama jika data tidak dienkripsi dengan baik. Brute force attack menargetkan sistem autentikasi dengan mencoba berbagai kombinasi kata sandi, sedangkan phishing memanfaatkan kelemahan manusia untuk memperoleh informasi sensitif. Serangan-serangan ini biasanya terjadi karena lemahnya mekanisme keamanan atau kesalahan dalam penerapan kriptografi.

Kelemahan algoritma kriptografi sering muncul ketika algoritma yang sudah usang atau konfigurasi yang tidak aman masih digunakan. Contohnya adalah penggunaan hash function lama seperti MD5 atau SHA-1 yang rentan terhadap collision, serta penggunaan kunci enkripsi dengan panjang yang terlalu pendek. Selain itu, kesalahan implementasi seperti manajemen kunci yang buruk, penggunaan kunci yang sama secara berulang, atau tidak adanya salting pada hash kata sandi juga dapat membuka celah keamanan meskipun algoritma yang digunakan secara teori masih kuat.

Untuk meningkatkan keamanan, sistem informasi sebaiknya menggunakan algoritma kriptografi yang modern dan telah teruji. Hash kata sandi dianjurkan menggunakan algoritma seperti bcrypt, scrypt, atau Argon2 yang dirancang tahan terhadap brute force. Untuk enkripsi data dan komunikasi, algoritma simetris seperti AES dengan panjang kunci yang memadai dan protokol aman seperti TLS perlu diterapkan. Selain pemilihan algoritma, penerapan yang benar dan manajemen kunci yang baik juga sangat penting agar sistem benar-benar aman.


---


## 7. Jawaban Pertanyaan
1. Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena menggunakan algoritma kriptografi yang sudah usang atau mekanisme autentikasi yang sederhana. Contohnya adalah penggunaan hash kata sandi tanpa salting, algoritma hash cepat seperti MD5 atau SHA-1, serta tidak adanya pembatasan percobaan login. Selain itu, sistem lama sering kali tidak diperbarui secara berkala sehingga tetap menggunakan standar keamanan yang sudah tidak relevan dengan perkembangan kemampuan komputasi saat ini.

2. Kelemahan algoritma berkaitan dengan kelemahan matematis atau kriptografis dari algoritma itu sendiri, misalnya kemungkinan collision atau mudahnya kunci ditebak karena desain yang sudah terbukti tidak aman. Sementara itu, kelemahan implementasi terjadi ketika algoritma yang sebenarnya kuat digunakan dengan cara yang salah, seperti manajemen kunci yang buruk, konfigurasi parameter yang tidak tepat, atau kesalahan pemrograman. Dengan kata lain, algoritma bisa aman secara teori, tetapi menjadi lemah karena penerapan yang keliru.

3. Organisasi dapat memastikan sistem kriptografi tetap aman di masa depan dengan menerapkan standar kriptografi terbaru dan melakukan pembaruan secara berkala. Audit keamanan, pengujian penetrasi, serta pemantauan terhadap perkembangan riset kriptografi juga perlu dilakukan. Selain itu, organisasi harus memiliki kebijakan manajemen kunci yang baik, menggunakan algoritma yang direkomendasikan oleh standar internasional, dan merancang sistem yang mudah diperbarui agar dapat beradaptasi dengan ancaman keamanan yang baru.


---

## 8. Kesimpulan
Base64 memiliki kelemahan utama karena tidak memberikan perlindungan keamanan sama sekali. Data yang di-encode dengan Base64 dapat dengan mudah dikembalikan ke bentuk aslinya tanpa memerlukan kunci, sehingga tidak cocok digunakan untuk melindungi informasi sensitif.

Sebagai rekomendasi solusi, Base64 sebaiknya hanya digunakan untuk kebutuhan kompatibilitas data, seperti pengiriman data melalui email atau penyimpanan dalam format teks. Untuk keamanan, Base64 harus dikombinasikan dengan algoritma kriptografi yang sebenarnya, seperti enkripsi AES untuk kerahasiaan data atau hash kriptografi yang aman untuk penyimpanan kata sandi. Dengan demikian, data tetap aman meskipun direpresentasikan dalam bentuk Base64.


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
