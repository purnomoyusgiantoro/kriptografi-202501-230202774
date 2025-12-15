# Laporan Praktikum Kriptografi
Minggu ke-: 10
Topik: Public Key Infrastructure (PKI & Certificate Authority)
Nama: purnomo yusgiantoro
NIM: 230202774
Kelas: 5ikra

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

    Membuat sertifikat digital sederhana.
    Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
    Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).



---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah suatu kerangka kerja keamanan yang digunakan untuk mengelola, mendistribusikan, dan memverifikasi kunci publik dalam sistem kriptografi asimetris. PKI melibatkan komponen utama seperti Certificate Authority (CA), yang berfungsi sebagai pihak tepercaya untuk menerbitkan, memvalidasi, dan mencabut sertifikat digital, serta sertifikat digital yang mengaitkan identitas pengguna dengan kunci publiknya. Dengan adanya PKI dan CA, proses autentikasi, enkripsi, dan tanda tangan digital dapat dilakukan secara aman karena keaslian identitas dan kunci publik dapat dipercaya, sehingga membangun kepercayaan dalam komunikasi dan transaksi digital.



---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi") ...
```

---


## 7. Jawaban Pertanyaan
1. Fungsi utama Certificate Authority (CA)
CA berfungsi memverifikasi identitas dan menerbitkan sertifikat digital agar kunci publik dapat dipercaya.

2. Alasan self-signed certificate tidak cukup untuk sistem produksi
Karena **tidak diverifikasi oleh pihak tepercaya, sehingga rentan terhadap pemalsuan identitas.

3. Cara PKI mencegah serangan MITM pada TLS/HTTPS
PKI memastikan sertifikat server valid dan terpercaya, sehingga klien dapat memverifikasi identitas server dan mencegah penyusup di tengah komunikasi.


---

## 8. Kesimpulan
Program berhasil membuat sertifikat digital self-signed menggunakan algoritma RSA dan hash SHA-256, yang menunjukkan konsep dasar kerja Public Key Infrastructure (PKI). Sertifikat yang dihasilkan mengaitkan identitas subjek dengan kunci publik secara kriptografis dan dapat digunakan untuk keperluan pengujian atau pembelajaran. Peringatan eprecation menunjukkan bahdwa praktik pengelolaan waktu perlu diperbarui ke format timezone-aware, namun tidak memengaruhi keberhasilan pembuatan sertifikat secara fungsional.



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
