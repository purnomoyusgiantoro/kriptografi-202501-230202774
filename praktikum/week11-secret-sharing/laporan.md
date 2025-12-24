Minggu ke-: 11
Topik: secret Sharing (Shamir’s Secret Sharing)
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
Shamir’s Secret Sharing adalah sebuah skema kriptografi yang digunakan untuk membagi sebuah rahasia menjadi beberapa bagian (shares) sehingga rahasia tersebut hanya dapat direkonstruksi jika sejumlah minimum bagian (threshold) digabungkan. Metode ini bekerja dengan memanfaatkan konsep matematika polinomial: sebuah rahasia disembunyikan sebagai konstanta dalam polinomial berderajat tertentu, lalu setiap share merupakan titik pada polinomial tersebut. Selama jumlah share yang dimiliki kurang dari ambang batas, tidak ada informasi apa pun tentang rahasia yang dapat diketahui. Skema ini banyak digunakan untuk meningkatkan keamanan penyimpanan kunci kriptografi, sistem multi-otoritas, dan pengamanan aset digital agar tidak bergantung pada satu pihak saja.

---




## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered) ...
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
**1. Keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung**
Keuntungan utama Shamir Secret Sharing (SSS) adalah rahasia tidak pernah disimpan atau dibagikan dalam bentuk utuh. Setiap pihak hanya memegang sebagian rahasia (share) yang secara individual tidak bermakna, sehingga jika satu atau beberapa share bocor, rahasia tetap aman. Hal ini jauh lebih aman dibanding membagikan salinan kunci secara langsung, karena kebocoran satu salinan saja sudah cukup untuk membahayakan seluruh sistem.

**2. Peran threshold (k) dalam keamanan secret sharing**
Threshold (k) menentukan jumlah minimum share yang harus digabungkan untuk merekonstruksi rahasia asli. Jika jumlah share yang dikumpulkan kurang dari k, maka rahasia sama sekali tidak dapat diketahui. Dengan mekanisme ini, keamanan meningkat karena rahasia hanya bisa diakses melalui kerja sama sejumlah pihak tertentu, sekaligus memberikan toleransi jika sebagian share hilang atau tidak tersedia.

**3. Contoh skenario nyata penggunaan Shamir Secret Sharing**
Shamir Secret Sharing sangat bermanfaat dalam pengelolaan kunci privat dompet kripto institusional. Misalnya, sebuah perusahaan membagi kunci privat ke beberapa eksekutif, di mana minimal tiga dari lima orang harus bekerja sama untuk mengakses dana. Dengan cara ini, dana tetap aman dari penyalahgunaan individu tunggal sekaligus terlindungi dari kehilangan kunci oleh satu orang.

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
