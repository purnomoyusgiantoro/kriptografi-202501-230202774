# Laporan Praktikum Kriptografi
Minggu ke-: 13
Topik: TinyChain – Proof of Work (PoW)
Nama: purnomo yusgiantoro
NIM: [23020774
Kelas: 5ikra

---

## 1. Tujuan

    Menjelaskan peran hash function dalam blockchain.
    Melakukan simulasi sederhana Proof of Work (PoW).
    Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
Hash function berperan sangat penting dalam blockchain karena berfungsi sebagai mekanisme kriptografi untuk menjaga integritas dan keamanan data. Setiap blok dalam blockchain berisi hash dari blok sebelumnya, sehingga membentuk rantai yang saling terhubung. Jika satu data pada blok diubah, maka nilai hash akan berubah secara drastis (avalanche effect), menyebabkan ketidaksesuaian dengan blok berikutnya. Sifat hash function yang satu arah (one-way) dan deterministik membuat data sulit dimanipulasi tanpa terdeteksi, sehingga menjamin keaslian transaksi dalam jaringan blockchain.

Proof of Work (PoW) merupakan mekanisme konsensus yang memanfaatkan hash function untuk memvalidasi transaksi dan menambahkan blok baru ke blockchain. Dalam PoW, penambang harus menemukan nilai nonce yang ketika digabungkan dengan data blok dan di-hash akan menghasilkan nilai hash dengan tingkat kesulitan tertentu, misalnya diawali dengan sejumlah nol. Proses ini membutuhkan komputasi tinggi dan bersifat trial-and-error, sehingga memerlukan biaya dan waktu. Kesulitan inilah yang membuat serangan menjadi mahal dan tidak efisien bagi pihak yang berniat memanipulasi blockchain.

Keamanan cryptocurrency berbasis kriptografi tidak hanya bergantung pada PoW, tetapi juga pada kombinasi hash function dan kriptografi kunci publik. Hash function menjamin integritas data, sementara kriptografi kunci publik digunakan untuk otentikasi dan verifikasi kepemilikan aset melalui tanda tangan digital. Selama algoritma kriptografi yang digunakan masih kuat dan kunci privat dijaga dengan baik oleh pengguna, sistem cryptocurrency relatif aman dari pemalsuan transaksi dan perubahan data secara sepihak.


---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash() ...
```


---



## 7. Jawaban Pertanyaan
1. Fungsi hash sangat penting dalam blockchain karena berperan menjaga integritas dan keamanan data. Setiap blok menyimpan hash dari blok sebelumnya sehingga membentuk rantai yang saling terhubung. Jika ada perubahan data pada satu blok, nilai hash akan berubah dan menyebabkan ketidaksesuaian pada blok berikutnya, sehingga manipulasi data dapat langsung terdeteksi. Selain itu, sifat hash yang satu arah membuat data asli sulit ditebak kembali dari nilai hash.

2. Proof of Work mencegah double spending dengan memastikan bahwa setiap transaksi harus divalidasi dan dicatat dalam satu blok yang disepakati oleh jaringan. Untuk menambahkan blok baru, penambang harus menyelesaikan perhitungan kriptografi yang sulit dan memakan waktu. Karena blockchain hanya mengakui rantai terpanjang atau dengan kerja terbanyak sebagai rantai yang sah, maka upaya untuk membelanjakan koin yang sama dua kali akan ditolak oleh jaringan karena tidak sesuai dengan riwayat transaksi yang telah tervalidasi.

3. Kelemahan utama Proof of Work dalam hal efisiensi energi adalah kebutuhan daya komputasi yang sangat besar. Proses penambangan mengharuskan banyak komputer bekerja secara terus-menerus untuk mencoba berbagai kemungkinan nilai hash, yang mengakibatkan konsumsi listrik tinggi. Hal ini tidak hanya meningkatkan biaya operasional, tetapi juga menimbulkan dampak lingkungan karena penggunaan energi yang berlebihan.


---

## 8. Kesimpulan

Sebelum kesimpulan, dapat dijelaskan bahwa proses mining pada blockchain dilakukan dengan cara mencari nilai hash yang memenuhi tingkat kesulitan tertentu (difficulty), yaitu hash yang diawali dengan sejumlah nol. Semakin tinggi nilai difficulty, semakin banyak percobaan yang harus dilakukan oleh komputer untuk menemukan hash yang sesuai. Hal ini menyebabkan waktu mining menjadi lebih lama dan membutuhkan sumber daya komputasi yang lebih besar.

Kondisi tersebut berpengaruh langsung terhadap keamanan blockchain. Karena setiap blok harus melalui proses perhitungan yang sulit dan memakan waktu, maka upaya untuk mengubah data pada satu blok akan sangat mahal dan tidak efisien. Penyerang harus menambang ulang blok tersebut dan seluruh blok setelahnya dengan difficulty yang sama atau lebih tinggi agar dapat menguasai jaringan, sehingga peluang manipulasi data menjadi sangat kecil.

Kesimpulannya, mekanisme difficulty dalam Proof of Work menjamin keamanan blockchain dengan meningkatkan biaya dan usaha yang dibutuhkan untuk memanipulasi data. Semakin tinggi difficulty, semakin kuat perlindungan terhadap serangan, karena proses mining menjadi lebih lambat dan mahal, sehingga blockchain tetap aman, transparan, dan dapat dipercaya.


---


## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 3f7ebf59f5b28210798a7d22aaaa5f468634cda4 (HEAD -> main)
Author: purnomo yusgiantoro <pyxvin124@gmail.com>
Date:   Sat Jan 3 19:15:12 2026 +0700

    week13-tinychain

```
