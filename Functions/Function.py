import streamlit as st
import PIL as Image
import pandas as pd
import datetime
from Data.Datas import accounts, adminaccounts, superadminaccounts, baju_anak, vouchers, historypesananlist, adminchathistory

def sesi_inisilasi():
    if "loggedin" not in st.session_state:
        st.session_state.loggedin = False
    if "adminloggedin" not in st.session_state:
        st.session_state.adminloggedin = False
    if "superadminlogin" not in st.session_state:
        st.session_state.superadminlogin = False
    if "keranjang" not in st.session_state:
        st.session_state.keranjang = []
    if "total_harga" not in st.session_state:
        st.session_state.total_harga = 0
    if "diskon" not in st.session_state:
        st.session_state.diskon = 0
    if "historypesanan" not in st.session_state:
        st.session_state.historypesanan = []
    if "stok" not in st.session_state:
        st.session_state.stok = {  # Inisialisasi stok produk
            "Baju Anak Motif Dinosaurus": 10,
            "Baju Anak Motif Bunga": 15,
            "Baju Anak Motif Mobil": 8,
            "Baju Anak Motif Hewan": 5,
            "Baju Anak Motif Buah": 12,
            "Baju Anak Motif Kartun": 7,
            "Baju Anak Motif Polkadot": 20,
            "Baju Anak Motif Pelangi": 18,
            "Baju Anak Motif Bintang": 12,
            "Baju Anak Motif Luar Angkasa": 10,
            "Baju Anak Motif Panda": 5,
            "Baju Anak Motif Superhero": 15,
            "Baju Anak Motif Hutan": 8,
            "Baju Anak Motif Geometri": 10,
            "Baju Anak Motif Pahlawan Nasional": 6,
    }
        
def login(username, password):
    for account in accounts:
        if account["username"] == username and account["password"] == password:
            st.session_state["loggedin"] = True
            st.session_state["displayname"] = username
            st.success("Login berhasil!")
            st.rerun()
            return
    for adminaccount in adminaccounts:
        if adminaccount["adminusername"] == username and adminaccount["adminpassword"] == password:
            st.session_state["adminloggedin"] = True
            st.session_state["displayname"] = username
            st.session_state["Role"] = "Admin"
            st.success("Login berhasil!")
            st.rerun()
            return
    for spadminacc in superadminaccounts:
        if spadminacc["superadminusername"] == username and spadminacc["superadminpassword"] == password:
            st.session_state["superadminlogin"] = True
            st.session_state["displayname"] = username
            st.session_state["Role"] = "Developer"
            st.success("Login berhasil!")
            st.rerun()
            return
    else:
        st.error("Username atau password salah.")

def tambah_ke_keranjang(nama, harga, jumlah, stok):
    if jumlah > 0 and jumlah <= stok:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah, "Subtotal": jumlah * harga})
        st.session_state.stok[nama] -= jumlah  # Kurangi stok sementara
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")
    elif jumlah > stok:
        st.error(f"Jumlah melebihi stok tersedia ({stok}).")
    else:
        st.error("Jumlah harus lebih dari 0.")

def katalogfunc():
    for baju in baju_anak:
        col1, col2, col3 = st.columns([1, 3, 2])
        stok = st.session_state.stok[baju["Nama"]]  # Dapatkan stok terkini
        
        with col1:
            st.image(f"Images/{baju["Gambar"]}", use_container_width=True)
        with col2:
            st.subheader(baju["Nama"])
            st.write(f"Harga: Rp {baju['Harga']:,}")
            st.write(f"Stok: {stok}")
        with col3:
            if stok > 0:
                jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=stok, step=1, key=baju["Nama"])
                if st.button(f"Tambah {baju['Nama']}", key=f"btn-{baju['Nama']}"):
                    tambah_ke_keranjang(nama=baju["Nama"], harga=baju["Harga"], jumlah=jumlah, stok=stok)
            else:
                st.error("Stok habis!")

def keranjangfunc():
    if st.session_state.keranjang:
        total_harga = sum(item["Subtotal"] for item in st.session_state.keranjang)
        st.session_state.total_harga = total_harga

        st.write("List Produk")
        for idx, item in enumerate(st.session_state.keranjang):
            st.write(f"{idx+1}. {item['Nama']} - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Subtotal']:,}")
        
        emailuser = st.text_input("Email:", placeholder="Masukan email anda")
        nohp = st.text_input("No. Hp:", placeholder="Masukan nomor HP/Whatsapp anda")
        alamatuser = st.text_input("Alamat:", placeholder="Masukan alamat anda")
        metodepembayaran = st.selectbox("Metode Pembayaran:", ["Transfer Bank", "Dana", "Gopay"], placeholder="Pilih metode pembayaran")
        
        voucher = st.text_input("Masukkan kode voucher (opsional):")
        hargadiskon = total_harga
        if st.button("Gunakan Voucher"):
            for vc in vouchers:
                if voucher == vc["kode"]:
                    st.session_state.diskon = vc["diskon"]
                    diskonvalue = total_harga * (st.session_state.diskon / 100)
                    hargadiskon = total_harga - diskonvalue
                    st.success(vc["Annouce"])
                    break
            else:
                st.error("Voucher tidak valid.")
        
        st.markdown("### Total Harga")
        st.write(f"Rp {hargadiskon:,}")

        if st.button("Beli"):
            st.success("Pesanan sudah dibuat!, mohon tunggu info dari Admin")
            historypesanan(emailuser, nohp, alamatuser, namaproduk=[item["Nama"] for item in st.session_state.keranjang], jumlah=[item["Jumlah"] for item in st.session_state.keranjang], totalharga=hargadiskon, metodepembayaran=metodepembayaran)
    
    else:
        st.write("Keranjang kosong.")

def historypesanan(emailuser, nohp, alamatuser, metodepembayaran, namaproduk, jumlah, totalharga):
    historypesananlist.append({
        "Tanggal": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Email": emailuser,
        "No. Hp": nohp,
        "Alamat": alamatuser,
        "Nama Produk": namaproduk,
        "Jumlah": jumlah,
        "Total Harga": totalharga,
        "Metode Pembayaran": metodepembayaran
    })

def vouchermaker():
    kode = st.text_input("Kode Voucher:")
    diskon = st.number_input("Diskon (%):", min_value=0, max_value=100, step=1)
    Annouce = st.text_input("Announcement:")

    if st.button("Aktifkan Voucher"):
        vouchers.append({"kode": kode, "diskon": diskon, "Annouce": Annouce})
        st.success("Voucher berhasil dibuat!")
    
    if vouchers:
        st.dataframe(vouchers)
    else:
        st.warning("Belum ada voucher yang aktif.")

def voucherdeleter():
    vouchertarget = st.text_input("Kode Voucher yang akan dihapus")
    if st.button("Hapus Voucher"):
        for vcs in vouchers:
            if vouchertarget == vcs["kode"]:
                vouchers.remove(vcs)
                st.success("Voucher berhasil dihapus!")
                break
        else:
            st.error("Voucher tidak ditemukan.")

    st.write("Active Vouchers")
    if vouchers:
        st.dataframe(vouchers)
    else:
        st.write("Belum ada Voucher yg aktif")
    
def adminchat():
    adminmessage = st.chat_input("Chat here")
    if st.button("Refresh Chat"):
        st.rerun()
    if adminmessage:
        adminchathistory.append({f"Tanggal": {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, "Role": {st.session_state["Role"]}, "Admin": {st.session_state.displayname}, "Message": adminmessage})

def accountbank():
    selectedlist = st.selectbox("Account List", ["User Accounts", "Admin Accounts", "Super Admin Accounts"])
    if selectedlist == "User Accounts":
        st.data_editor(accounts, num_rows="dynamic")
    elif selectedlist == "Admin Accounts":
        st.data_editor(adminaccounts, num_rows="dynamic")
    elif selectedlist == "Super Admin Accounts":
        st.data_editor(superadminaccounts, num_rows="dynamic")
    else:
        st.write("Nothing to show")

def accountcreatortool(userinput, passinput, selectedtype):
    if selectedtype == "User Account":
        accounts.append({"username": userinput, "password": passinput})
        st.success("Account created!")
    elif selectedtype == "Admin Account":
        adminaccounts.append({"adminusername": userinput, "adminpassword": passinput})
        st.success("Admin Account created!")
    else:
        st.write("You didnt select the account type bruh")

def accountdeletortool(userinput, selectedtype):
    if selectedtype == "User Account":
        for user in accounts:
            if userinput == user["username"]:
                accounts.remove(user)
                st.success("User Account deleted!")
                break
        else:
            st.error("User Account not found!")
    elif selectedtype == "Admin Account":
        for auser in adminaccounts:
            if userinput == auser["adminusername"]:
                adminaccounts.remove(auser)
                st.success("Admin Account deleted!")
                break
        else:
            st.error("Admin Account not found!")
    else:
        st.write("You didnt select the account type bruh")
