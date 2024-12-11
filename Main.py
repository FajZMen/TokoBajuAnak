import streamlit as st
import pandas as pd
from Functions.Function import sesi_inisilasi, tambah_ke_keranjang, login, katalogfunc, keranjangfunc, historypesanan, vouchermaker, voucherdeleter, adminchat, accountbank, accountcreatortool, accountdeletortool
from Data.Datas import baju_anak, accounts, adminaccounts, superadminaccounts, historypesananlist, vouchers, adminchathistory
sesi_inisilasi()
loggedin = st.session_state.get("loggedin", False)
adminloggedin = st.session_state.get("adminloggedin", False)
superadminlogin = st.session_state.get("superadminlogin", False)
dataaccess = st.session_state.get("databankaccess", False)

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
        st.title("Vouchers")
        vtab = st.tabs(["Activate Voucher", "Delete Voucher"])
        with vtab[0]:
            vouchermaker()
            st.write("Active Vouchers")
        with vtab[1]:
            voucherdeleter()

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
        st.title("Vouchers")
        vtab = st.tabs(["Activate Voucher", "Delete Voucher"])
        with vtab[0]:
            vouchermaker()
            st.write("Active Vouchers")
        with vtab[1]:
            voucherdeleter()

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
        tabs = st.tabs(["Account Creator", "Account Deleter"])
        with tabs[0]:
            st.title("Account Creation Tool")
            selectedtype = st.selectbox("Create what Account Type", ["User Account", "Admin Account"])
            userinput = st.text_input("Enter Account Username to Create")
            passinput = st.text_input("Enter the Account Password", type="password")
            if st.button("Create Account"):
                accountcreatortool(userinput, passinput, selectedtype)
        with tabs[1]:
            st.title("Account Deletion Tool")
            deluserinput = st.text_input("Enter Account Username to Delete")
            delselectedtype = st.selectbox("What Account Type you trying to delete", ["User Account", "Admin Account"])
            if st.button("Delete Account"):
                accountdeletortool(deluserinput, delselectedtype)

    if halamanspadmin == "Account Bank":
        st.title("Account Databank")
        if st.session_state.databankaccess:
            accountbank()
        else:
            st.write("Enter Password to enter")
            sneakypass = st.text_input("Password", type="password")
            if st.button("Enter Databank"):
                if sneakypass == "4202024":
                    st.session_state.databankaccess = True
                else:
                    st.write("Wrong")

    if halamanspadmin == "Katalog":
        st.title("Katalog Toko Baju Anak")
        katalogfunc()
    
    if halamanspadmin == "Keranjang":
        st.title("Keranjang Belanja")
        keranjangfunc()
