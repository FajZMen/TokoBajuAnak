import streamlit as st
import pandas as pd
from Functions.Function import sesi_inisilasi, tambah_ke_keranjang, login, katalogfunc, keranjangfunc, historypesanan, vouchermaker, adminchat, accountbank, accountcreatortool
from Data.Datas import baju_anak, accounts, adminaccounts, superadminaccounts, historypesananlist, vouchers, adminchathistory
sesi_inisilasi()
loggedin = st.session_state.get("loggedin", False)
adminloggedin = st.session_state.get("adminloggedin", False)
superadminlogin = st.session_state.get("superadminlogin", False)

if not loggedin and not adminloggedin and not superadminlogin:
    halamanlogin = st.sidebar.radio(
        "Halaman",
        ["Login"]
    )
    
    if halamanlogin == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            login(username, password)

elif st.session_state.loggedin:
    st.sidebar.title(f"Hello {st.session_state.displayname}!")
    halamanuser = st.sidebar.radio(
        "Halaman User",
        ["Katalog", "Keranjang"]
    )

    if st.sidebar.button("Logout"):
        st.session_state["loggedin"] = False
        st.rerun()

    if halamanuser == "Katalog":
        st.title("Katalog Toko Baju Anak")
        katalogfunc()
    
    if halamanuser == "Keranjang":
        st.title("Keranjang Belanja")
        keranjangfunc()

elif st.session_state.adminloggedin:
    st.sidebar.title(f"Selamat Datang Admin {st.session_state.displayname}!")
    halamanadmin = st.sidebar.radio(
        "Halaman Admin",
        ["Pesanan", "Vouchers", "Admin Chat", "Katalog", "Keranjang"]
    )

    if st.sidebar.button("Logout"):
        st.session_state["adminloggedin"] = False
        st.rerun()

    if halamanadmin == "Pesanan":
        st.title("Pesanan")
        if historypesananlist:
            st.data_editor(historypesananlist, num_rows="dynamic")
        else:
            st.warning("Belum ada pesanan.")
    
    if halamanadmin == "Vouchers":
        st.title("Vouchers Activator")
        vouchermaker()
        st.write("Active Vouchers")
        if vouchers:
            st.data_editor(vouchers, num_rows="dynamic")
        else:
            st.warning("Belum ada voucher yang aktif.")

    if halamanadmin == "Admin Chat":
        st.title("Admin Chat")
        adminchat()
        if adminchathistory:
            st.data_editor(adminchathistory, column_config={"Message": st.column_config.TextColumn(width="large")})
        else:
            st.warning("Belum ada chat.")

    if halamanadmin == "Katalog":
        st.title("Katalog Toko Baju Anak")
        katalogfunc()
    
    if halamanadmin == "Keranjang":
        st.title("Keranjang Belanja")
        keranjangfunc()

elif st.session_state.superadminlogin:
    st.sidebar.title(f"Selamat Datang Developer {st.session_state.displayname}!")
    halamanspadmin = st.sidebar.radio(
        "Halaman Super Admin",
        ["Pesanan", "Vouchers", "Admin Chat", "Dev Tools", "Account Bank", "Katalog", "Keranjang"]
    )

    if st.sidebar.button("Logout"):
        st.session_state["superadminlogin"] = False
        st.rerun()

    if halamanspadmin == "Pesanan":
        st.title("Pesanan")
        if historypesananlist:
            st.data_editor(historypesananlist, num_rows="dynamic")
        else:
            st.warning("Belum ada pesanan.")
    
    if halamanspadmin == "Vouchers":
        st.title("Vouchers Activator")
        vouchermaker()
        st.write("Active Vouchers")
        if vouchers:
            st.data_editor(vouchers, num_rows="dynamic")
        else:
            st.warning("Belum ada voucher yang aktif.")

    if halamanspadmin == "Admin Chat":
        st.title("Admin Chat")
        adminchat()
        if adminchathistory:
            st.data_editor(adminchathistory, num_rows="dynamic", column_config={"Message": st.column_config.TextColumn(width="large")})
        else:
            st.warning("Belum ada chat.")
        
        if st.sidebar.button("Clear Chat"):
            adminchathistory.clear()
            st.rerun()

    if halamanspadmin == "Dev Tools":
        tabs = st.tabs(["Account Creator", "Funni"])
        with tabs[0]:
            st.title("Account Creator Tool")
            userinput = st.text_input("Username")
            passinput = st.text_input("Password", type="password")
            selectedtype = st.selectbox("Account Type", ["User Account", "Admin Account"])
            if st.button("Create Account"):
                accountcreatortool(userinput, passinput, selectedtype)
        with tabs[1]:
            st.title("Funni")


    if halamanspadmin == "Account Bank":
        st.title("Account Databank")
        accountbank()

    if halamanspadmin == "Katalog":
        st.title("Katalog Toko Baju Anak")
        katalogfunc()
    
    if halamanspadmin == "Keranjang":
        st.title("Keranjang Belanja")
        keranjangfunc()
