# Laporan Praktikum Kriptografi
Minggu ke-: 15 
Topik: Proyek Kelompok – TinyCoin ERC20 (MELODIA)
Nama: purnomo yusgiantoro
NIM: 230202774
Kelas: 5ikra

---

## Projek kelompok

https://github.com/purnomoyusgiantoro/melodia

## 1. Tujuan

    Mengembangkan proyek sederhana berbasis algoritma kriptografi.
    Mendokumentasikan proses implementasi proyek ke dalam repository Git.
    Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori

Blockchain merupakan teknologi buku besar terdistribusi (distributed ledger) yang memungkinkan pencatatan transaksi secara transparan, aman, dan tidak dapat diubah tanpa memerlukan pihak ketiga. Setiap transaksi diverifikasi oleh jaringan dan disimpan dalam blok yang saling terhubung menggunakan kriptografi. Karakteristik utama blockchain seperti desentralisasi, imutabilitas, dan transparansi menjadikannya cocok untuk sistem keuangan digital dan pengelolaan aset berbasis kepercayaan.

Smart contract adalah program yang berjalan di atas blockchain dan dieksekusi secara otomatis ketika kondisi tertentu terpenuhi. Pada ekosistem Ethereum dan jaringan kompatibel EVM, smart contract ditulis menggunakan bahasa Solidity dan memungkinkan implementasi logika bisnis tanpa perantara. Standar ERC-20 digunakan untuk menciptakan token fungible yang seragam, sehingga token dapat dengan mudah diintegrasikan dengan wallet, decentralized exchange (DEX), dan aplikasi Web3 lainnya.

Dalam konteks tokenisasi aset, blockchain dan smart contract memungkinkan representasi kepemilikan aset dunia nyata (Real World Assets/RWA) secara digital. Token ERC-20 dapat digunakan untuk membagi kepemilikan aset menjadi unit yang lebih kecil, meningkatkan likuiditas, dan memperluas akses investor. Pendekatan ini mendukung model bisnis baru yang lebih transparan, efisien, dan terdesentralisasi, khususnya pada industri kreatif seperti musik.

---

## 5. Source Code

```    event RequestSubmitted(uint256 indexed requestId, address indexed creator);
    event RequestApproved(uint256 indexed requestId, uint256 indexed tokenId);

    constructor() ERC721("Music IP NFT", "MIPNFT") Ownable(msg.sender) {
        tokenCounter = 0;
        requestCounter = 0; ...
```
)

---

## 7. Jawaban Pertanyaan

### 1. Fungsi Utama ERC-20 dalam Ekosistem Blockchain

ERC-20 adalah standar token fungible pada blockchain berbasis EVM.
Fungsi utamanya meliputi:

* Standarisasi pembuatan token agar kompatibel dengan wallet, DEX, dan dApp
* Media pertukaran dan alat pembayaran digital
* Representasi kepemilikan aset (utility, governance, atau RWA)
* Mendukung interoperabilitas antar aplikasi blockchain

---

### 2. Mekanisme Transfer Token ERC-20

Transfer token ERC-20 bekerja melalui pencatatan saldo berbasis `mapping`.

* **`transfer`**
  Mengirim token langsung dari pemilik ke penerima

* **`approve` + `transferFrom`**
  Memberi izin pihak ketiga (smart contract) untuk memindahkan token

Setiap transfer akan memicu event `Transfer` yang digunakan oleh wallet dan blockchain explorer untuk pelacakan transaksi.

---

### 3. Risiko Smart Contract dan Mitigasi

| Risiko               | Mitigasi                                     |
| -------------------- | -------------------------------------------- |
| Bug & logic error    | Gunakan OpenZeppelin, testing, code review   |
| Reentrancy           | ReentrancyGuard, checks-effects-interactions |
| Access control lemah | Ownable / AccessControl                      |
| Front-running        | Slippage limit, commit–reveal                |
| Dependensi eksternal | Validasi data & trusted oracle               |


---

## 8. Kesimpulan
Pemanfaatan teknologi blockchain dan smart contract memungkinkan pengelolaan aset digital yang lebih transparan, aman, dan terdesentralisasi. Dengan menerapkan standar ERC-20 dan jaringan berbasis EVM, proses tokenisasi kepemilikan dapat dilakukan secara efisien tanpa perantara. Pendekatan ini membuka peluang inovasi dalam pengelolaan dan distribusi nilai aset, khususnya pada industri kreatif, dengan meningkatkan kepercayaan, aksesibilitas, dan likuiditas bagi seluruh pihak yang terlibat.

---


## 10. Commit Log

```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
