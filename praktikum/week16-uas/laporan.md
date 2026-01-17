Minggu ke-: 16 UAS
Topik: Laporan Projek
Nama: Purnomo Yusgiantoro
NIM: 23020774
Kelas: 5IKRA

# 🎵 Melodia – Decentralized Music Royalty Platform

<p align="center">
  <img src="frontend/public/melodia_logo.png" width="200" />
</p>

**Melodia** adalah platform Web3 untuk **tokenisasi royalti musik** yang memungkinkan musisi menjual kepemilikan royalti lagu kepada fans dan investor secara transparan menggunakan **blockchain Mantle Network (L2)**.

🌐 **Live Demo**: [https://melodia-eth.netlify.app](https://melodia-eth.netlify.app)

---

## 🚀 Overview

Industri musik saat ini masih menghadapi:

* Kurangnya transparansi royalti
* Pembayaran yang lambat
* Akses pendanaan terbatas bagi musisi independen

**Melodia** menghadirkan solusi melalui:

* **NFT (ERC-721)** sebagai sertifikat hak cipta lagu
* **Token ERC-20** sebagai representasi kepemilikan royalti
* **Smart contract** untuk transparansi dan otomatisasi

---

## ✨ Key Features

* 🎤 **Creator Hub** – Deploy kontrak royalti lagu
* 🛒 **Marketplace** – Investasi kepemilikan lagu
* 📊 **Portfolio** – Lihat aset musik & token
* 🛡️ **Admin Dashboard** – Approval & kontrol listing
* 🔐 **Optional KYC System** – Untuk compliance

---

## 🧱 Tech Stack

### Blockchain

* **Mantle Network (L2)**
* Solidity `0.8.20`
* OpenZeppelin Contracts
* Hardhat
* ethers.js v6

### Frontend

* React.js
* Vite
* Tailwind CSS
* MetaMask Wallet

### Storage

* IPFS (simulasi untuk demo)

---

## 🏗️ System Architecture

```
User (Artist / Investor)
        │
        ▼
Frontend (React + Vite)
        │  ethers.js
        ▼
Mantle Network (L2)
 ├── MusicRoyalty (ERC-20)
 ├── MusicIPNFT (ERC-721)
 └── KYCRegistry
```

---

## 🔄 Business Flow

### 🎼 Song Publishing

1. Creator upload metadata lagu
2. Deploy `MusicRoyalty.sol`
3. Request listing ke `MusicIPNFT`
4. Admin approve
5. NFT tercetak & tampil di marketplace

### 💰 Royalty Investment

1. Investor pilih lagu
2. Panggil `buyShares()`
3. Kirim MNT
4. Token masuk ke wallet investor

---

## 📂 Project Structure

```
├── contracts
│   ├── KYCRegistry.sol
│   ├── MusicIPNFT.sol
│   └── MusicRoyalty.sol
├── docs
│   ├── COMPLIANCE.md
│   ├── DEPLOYMENT.md
│   ├── DOCUMENTATION.md
│   ├── PITCH.md
│   ├── ROADMAP.md
│   ├── SMART_CONTRACTS.md
│   └── TEAM.md
├── frontend
│   ├── src
│   │   ├── config
│   │   ├── pages
│   │   └── web3
│   └── vite.config.js
├── hardhat.config.js
├── package.json
└── README.md
```

---

## 🧠 Smart Contracts Overview

### 1️⃣ KYCRegistry.sol

Whitelist verification (optional for demo).

### 2️⃣ MusicRoyalty.sol

ERC-20 token per lagu.

* `buyShares()`
* `setPricePerShare()`
* `onlyVerifiedOrDemo`

### 3️⃣ MusicIPNFT.sol

ERC-721 NFT sebagai sertifikat IP musik.

* Listing request & approval

---

## 🧪 Testing Status

| Module            | Status    |
| ----------------- | --------- |
| Creator Hub       | ✅ Working |
| Marketplace       | ✅ Working |
| Genre Filter      | ✅ Working |
| Admin Permission  | ✅ Working |
| KYC (Demo Bypass) | ✅ Enabled |

---

## 🌐 Network Configuration

| Network        | Chain ID | RPC                                                              |
| -------------- | -------- | ---------------------------------------------------------------- |
| Mantle Sepolia | 5003     | [https://rpc.sepolia.mantle.xyz](https://rpc.sepolia.mantle.xyz) |
| Mantle Mainnet | 5000     | [https://rpc.mantle.xyz](https://rpc.mantle.xyz)                 |

---

## ⚠️ Compliance & Disclaimer

> Token pada platform ini **berpotensi dikategorikan sebagai sekuritas** di beberapa yurisdiksi.

Proyek ini:

* Dibangun untuk **edukasi & demo**
* Tidak menjamin keuntungan finansial
* Tidak menyediakan nasihat hukum atau investasi

---

## 🗺️ Roadmap

* ✅ MVP on Mantle Testnet
* ⏳ Royalty Distribution
* ⏳ Secondary Marketplace
* ⏳ Mainnet Launch

---

## 👥 Team

### Bagus Alfiyan Yusuf – Lead Developer

GitHub: [https://github.com/Fiyanz](https://github.com/Fiyanz)

### Purnomo Yusgiantoro – Team Lead

GitHub: [https://github.com/purnomoyusgiantoro](https://github.com/purnomoyusgiantoro)

---

## 🔗 Links

* 🌐 Live Demo: [https://melodia-eth.netlify.app](https://melodia-eth.netlify.app)
* 📦 GitHub Repository: [https://github.com/your-username/melodia](https://github.com/your-username/melodia)
  *(Update with official repo link)*

---

## 📜 License

MIT License

---

**Built with ❤️ on Mantle Network**


