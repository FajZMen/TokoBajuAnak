import streamlit as st
from PIL import Image

historypesananlist = []
vouchers = []
adminchathistory = []

baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": 100000, "Gambar": "Dino.jpeg"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": 95000, "Gambar": "Bunga.jpeg"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": 105000, "Gambar": "Mobil.jpeg"},
    {"Nama": "Baju Anak Motif Hewan", "Harga": 110000, "Gambar": "Hewan.jpeg"},
    {"Nama": "Baju Anak Motif Buah", "Harga": 98000, "Gambar": "Buah.jpeg"},
    {"Nama": "Baju Anak Motif Kartun", "Harga": 120000, "Gambar": "Kartun.jpeg"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": 90000, "Gambar": "Polkadot.jpeg"},
    {"Nama": "Baju Anak Motif Pelangi", "Harga": 115000, "Gambar": "Pelangi.jpeg"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": 100000, "Gambar": "Bintang.jpeg"},
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "LuarAngkasa.jpeg"},
    # {"Nama": "Baju Anak Motif Panda", "Harga": 110000, "Gambar": "Panda.jpeg"}, --------- Ini 5 pada Gak ada fotonya
    # {"Nama": "Baju Anak Motif Superhero", "Harga": 130000, "Gambar": "Superhero.jpeg"},
    # {"Nama": "Baju Anak Motif Hutan", "Harga": 105000, "Gambar": "Hutan.jpeg"},
    # {"Nama": "Baju Anak Motif Geometri", "Harga": 95000, "Gambar": "Geometri.jpeg"},
    # {"Nama": "Baju Anak Motif Pahlawan Nasional", "Harga": 125000, "Gambar": "Pahlawan.jpeg"},
]

accounts = [
    {"username": "orang", "password": "1234"},
]

adminaccounts = [
    {"adminusername": "admin", "adminpassword": "adminorang"},
    {"adminusername": "Sabrina", "adminpassword": "15240233"},
    {"adminusername": "Putra", "adminpassword": "15240301"},
    {"adminusername": "Valenvia", "adminpassword": "15240234"},
    {"adminusername": "Ahmad", "adminpassword": "15240440"},
    {"adminusername": "Fahreza", "adminpassword": "15240204"},
]

superadminaccounts = [
    {"superadminusername": "FajZ", "superadminpassword": "ZSTLead"},
]

