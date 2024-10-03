#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Daftar URL gambar yang dihosting di GitHub dan judulnya
images = [
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/5%20Kategori%20Produk%20dengan%20Penjualan%20Tertinggi.png",
        "title": "5 Kategori Produk dengan Penjualan Tertinggi"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Tren%20Penjualan%205%20Kategori%20Produk%20Teratas%20Per%20Bulan.png",
        "title": "Tren Penjualan 5 Kategori Produk Teratas Per Bulan"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/5%20Kategori%20Produk%20dengan%20Penjualan%20Tertendah.png",
        "title": "5 Kategori Produk dengan Penjualan Terendah"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Tren%20Penjualan%20Seiring%20Waktu.png",
        "title": "Tren Penjualan Seiring Waktu"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Perbandingan%20Jenis%20Pembayaran.png",
        "title": "Perbandingan Jenis Pembayaran"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Perbandingan%20Status%20Pesanan.png",
        "title": "Perbandingan Status Pesanan"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Distribusi%20Customers%20Berdasarkan%205%20Kota%20Teratas.png",
        "title": "Distribusi Customers Berdasarkan 5 Kota Teratas"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Hubungan%20antara%20Biaya%20Pengiriman%20dan%20Skor%20Ulasan%20per%20State.png",
        "title": "Hubungan antara Biaya Pengiriman dan Skor Ulasan per State"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Heatmap%20Hubungan%20antara%20Biaya%20Pengiriman%20dan%20Rata-rata%20Skor%20Ulasan%20per%20State.png",
        "title": "Heatmap Hubungan antara Biaya Pengiriman dan Rata-rata Skor Ulasan per State"
    },
    {
        "url": "https://github.com/dudinurdiyans/project_data_analisis_dudi/raw/main/Peta%20Penyebaran%20Seller%20Berdasarkan%20Kota.png",
        "title": "Peta Penyebaran Seller Berdasarkan Kota"
    },
]

# Menampilkan setiap gambar dengan judul
for image in images:
    st.image(image["url"], caption=image["title"])

