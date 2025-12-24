# 12 Aplikasi TLS & E-commerce

## Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menganalisis penggunaan kriptografi pada **email** dan **SSL/TLS**.  
2. Menjelaskan enkripsi dalam transaksi **e-commerce**.  
3. Mengevaluasi isu **etika & privasi** dalam penggunaan kriptografi di kehidupan sehari-hari.  

---

## Capaian Kegiatan
Pada akhir sesi ini mahasiswa menghasilkan:  
- Laporan studi kasus tentang penerapan SSL/TLS pada email dan e-commerce.  
- Analisis isu privasi dan etika penggunaan kriptografi.  
- Commit Git dengan format `week12-aplikasi-tls`.  

---

## Persiapan Lingkungan
1. Buat folder berikut:  
   ```
   praktikum/week12-aplikasi-tls/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Siapkan koneksi internet untuk mengamati penggunaan SSL/TLS (misalnya HTTPS pada browser).  
3. Materi rujukan: Stallings (2017), Bab 15.  

---

### Langkah 2 — Studi Kasus E-commerce
Enkripsi digunakan dalam transaksi online untuk melindungi data sensitif seperti kredensial login, nomor kartu pembayaran, dan informasi pribadi agar tidak dapat dibaca oleh pihak yang tidak berwenang. Saat pengguna login atau melakukan pembayaran, TLS mengenkripsi data sebelum dikirim dari browser ke server, sehingga meskipun data tersebut disadap di tengah perjalanan jaringan, isinya tetap tidak dapat dipahami. Selain menjaga kerahasiaan, enkripsi juga memastikan integritas data, yaitu menjamin bahwa informasi tidak diubah selama proses pengiriman, serta autentikasi, yaitu memastikan pengguna berkomunikasi dengan server yang sah.

Jika TLS tidak digunakan, transaksi online sangat rentan terhadap berbagai ancaman keamanan, terutama serangan *Man-in-the-Middle*. Dalam serangan ini, penyerang dapat menyadap, membaca, bahkan memodifikasi data yang dikirim antara pengguna dan server tanpa disadari oleh kedua belah pihak. Akibatnya, kata sandi dapat dicuri, data pembayaran disalahgunakan, dan transaksi dapat dimanipulasi. Selain merugikan pengguna, ketiadaan TLS juga dapat merusak reputasi penyedia layanan dan menghilangkan kepercayaan dalam sistem e-commerce.


---

### Langkah 3 — Analisis Etika & Privasi
Penggunaan email terenkripsi seperti PGP dan S/MIME membawa manfaat besar bagi privasi, tetapi juga menimbulkan sejumlah isu. Isu privasi utama muncul pada pengelolaan kunci kriptografi, karena jika kunci privat pengguna hilang atau diakses pihak lain, seluruh isi komunikasi dapat terbuka. Selain itu, enkripsi end-to-end membuat isi email tidak dapat dibaca oleh penyedia layanan, sehingga menyulitkan proses pemulihan data, pemantauan keamanan internal, atau investigasi insiden tanpa persetujuan pemilik kunci. Metadata email seperti pengirim, penerima, dan waktu pengiriman juga umumnya tidak terenkripsi, sehingga masih dapat dimanfaatkan untuk analisis pola komunikasi.

Dari sisi etika, muncul dilema apakah perusahaan boleh mendekripsi email karyawan untuk keperluan audit. Di satu sisi, perusahaan memiliki kepentingan untuk melindungi aset, mencegah kebocoran data, dan memastikan kepatuhan terhadap regulasi. Namun di sisi lain, dekripsi tanpa persetujuan jelas dapat melanggar privasi individu dan kepercayaan karyawan. Secara etis, praktik ini seharusnya dibatasi oleh kebijakan yang transparan, persetujuan tertulis, dan hanya dilakukan untuk tujuan yang sah.

Dalam konteks pemerintah, kebijakan pengawasan komunikasi terenkripsi juga menghadirkan dilema serupa. Enkripsi melindungi hak privasi dan kebebasan berekspresi warga, tetapi sekaligus dapat menghambat penegakan hukum terhadap kejahatan serius. Pemerintah dihadapkan pada pilihan sulit antara menjaga keamanan nasional dan menghormati hak privasi, sehingga kebijakan yang ideal biasanya menekankan keseimbangan, pengawasan berbasis hukum, serta mekanisme akuntabilitas agar kekuasaan tidak disalahgunakan.

---

## Pertanyaan Diskusi
**1. Perbedaan utama antara HTTP dan HTTPS**  
Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mengirimkan data dalam bentuk teks biasa tanpa enkripsi, sehingga informasi mudah disadap atau dimanipulasi oleh pihak ketiga. Sebaliknya, HTTPS menggunakan TLS untuk mengenkripsi komunikasi antara klien dan server, sehingga data menjadi lebih aman, terjaga kerahasiaannya, dan integritasnya dapat dipastikan.

**2. Pentingnya sertifikat digital dalam komunikasi TLS**  
Sertifikat digital berfungsi untuk memverifikasi identitas server yang berkomunikasi dengan pengguna. Dalam TLS, sertifikat digital dikeluarkan oleh Certificate Authority (CA) yang tepercaya dan memastikan bahwa pengguna benar-benar terhubung ke server yang sah, bukan server palsu. Dengan adanya sertifikat ini, TLS dapat mencegah serangan *man-in-the-middle* serta membangun kepercayaan dalam komunikasi digital.

**3. Peran kriptografi terhadap privasi serta tantangan hukum dan etika**  
Kriptografi mendukung privasi dengan melindungi data dan komunikasi dari akses tidak sah, sehingga informasi pribadi dan sensitif tetap aman. Namun, kekuatan kriptografi juga menimbulkan tantangan hukum dan etika karena dapat digunakan untuk menyembunyikan aktivitas ilegal dari penegak hukum. Hal ini memunculkan dilema antara perlindungan hak privasi
individu dan kebutuhan negara untuk melakukan pengawasan demi keamanan publik.

---


## Tugas yang Dikumpulkan
1. Laporan `laporan.md` berisi:  
   - Studi kasus penerapan SSL/TLS (email & e-commerce).  
   - Screenshot sertifikat digital dari minimal 2 website berbeda.  
   - Analisis isu etika & privasi.  
   - Jawaban pertanyaan diskusi.  
2. Screenshot hasil observasi TLS/SSL disimpan di folder `screenshots/`.  

Struktur akhir folder:
```
praktikum/week12-aplikasi-tls/
 ├─ screenshots/
 │   └─ sertifikat.png
 └─ laporan.md
```

Commit dengan pesan:  
```
week12-aplikasi-tls
```

---

## Rubrik Penilaian
Mengacu pada RPS Minggu 12: **Total bobot 5% (Studi kasus email/SSL/TLS 3%, Analisis privasi 2%)**  

| Aspek Penilaian       | Bobot | Kriteria                                                                 |
|------------------------|-------|--------------------------------------------------------------------------|
| Studi kasus TLS/email  | 3%    | Sertifikat berhasil dianalisis, laporan jelas, bukti screenshot ada      |
| Analisis privasi/etika | 2%    | Analisis kritis, relevan dengan kasus nyata, laporan rapi                |
| Evidence Git & repo    | -     | Commit sesuai format, struktur repo rapi, history commit jelas           |

---
