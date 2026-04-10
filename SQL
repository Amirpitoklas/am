CREATE DATABASE lelang;
USE lelang;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin','petugas','masyarakat') DEFAULT 'masyarakat'
);

CREATE TABLE barang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(100),
    tgl DATE,
    harga_awal INT,
    deskripsi TEXT,
    foto VARCHAR(255),
    status ENUM('open','closed') DEFAULT 'open'
);

CREATE TABLE lelang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_barang INT,
    id_user INT,
    harga_akhir INT,
    tgl_lelang TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
