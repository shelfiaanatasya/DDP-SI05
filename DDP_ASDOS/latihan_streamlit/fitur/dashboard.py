import streamlit as st

st.title("Halaman Dashboard")
st.image("rumah.jpg", caption="Gambar Rumah")

# Fungsi Menghitung dan Menyimpan Total
def total():
    total_nabung = sum(s['jumlah']
    for s in st.session_state['total_semua'] if s ['Tipe'] == 'Menabung')
    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("Total Menabung", f"Rp {total_nabung}")