import streamlit as st
import pandas as pd
from datetime import datetime
import os

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(
    page_title="Evaluasi Dashboard Pengawasan Pupuk",
    layout="centered"
)

# =====================
# JUDUL & DESKRIPSI
# =====================
st.title("Kuesioner Evaluasi Dashboard Pengawasan Pupuk")
st.write("**Tugas Latar CPNS 2025 – Ditjen Prasarana dan Sarana Pertanian**")

st.markdown("""
Kuesioner ini bertujuan untuk memperoleh masukan dan evaluasi terhadap
Dashboard Pengawasan Pupuk yang dikembangkan sebagai bagian dari Tugas Latar CPNS 2025.

🔗 **Link Dashboard:**  
https://public.tableau.com/app/profile/izzah.nofitasari/viz/Book1_17645791542780/Dashboard?publish=yes
""")

st.divider()

# =====================
# BAGIAN 1 – IDENTITAS
# =====================
st.header("Bagian 1 – Identitas Responden")

unit = st.text_input("Unit Kerja")
jabatan = st.text_input("Jabatan")

peran = st.selectbox(
    "Peran Responden",
    [
        "Pimpinan",
        "Pejabat Struktural",
        "Pejabat Fungsional",
        "Staf",
        "Lainnya"
    ]
)

st.divider()

# =====================
# BAGIAN 2 – AKSES & PEMAHAMAN
# =====================
st.header("Bagian 2 – Akses dan Pemahaman Dashboard")

q1 = st.slider(
    "Saya dapat mengakses dashboard tanpa kendala teknis",
    1, 5
)

q2 = st.slider(
    "Tampilan awal dashboard mudah dipahami",
    1, 5
)

q3 = st.slider(
    "Informasi yang disajikan pada dashboard mudah dibaca dan dimengerti",
    1, 5
)

st.divider()

# =====================
# BAGIAN 3 – KUALITAS VISUALISASI & DATA
# =====================
st.header("Bagian 3 – Kualitas Visualisasi dan Data")

q4 = st.slider(
    "Visualisasi (grafik, peta, tabel) sudah jelas dan informatif",
    1, 5
)

q5 = st.slider(
    "Pemilihan jenis grafik sudah sesuai dengan informasi yang ditampilkan",
    1, 5
)

q6 = st.slider(
    "Dashboard membantu memahami kondisi pengawasan pupuk secara cepat",
    1, 5
)

q7 = st.slider(
    "Data yang ditampilkan relevan dengan kebutuhan Ditjen PSP",
    1, 5
)

st.divider()

# =====================
# BAGIAN 4 – MANFAAT KEPUTUSAN
# =====================
st.header("Bagian 4 – Manfaat untuk Pengambilan Keputusan")

q8 = st.slider(
    "Dashboard berpotensi mendukung monitoring dan evaluasi pengawasan pupuk",
    1, 5
)

q9 = st.slider(
    "Dashboard dapat membantu pimpinan dalam pengambilan keputusan",
    1, 5
)

q10 = st.slider(
    "Dashboard layak dikembangkan lebih lanjut untuk penggunaan internal Ditjen PSP",
    1, 5
)

st.divider()

# =====================
# BAGIAN 5 – PENILAIAN UMUM
# =====================
st.header("Bagian 5 – Penilaian Umum")

penilaian_umum = st.radio(
    "Penilaian keseluruhan terhadap dashboard",
    [
        "Sangat Baik",
        "Baik",
        "Cukup",
        "Kurang",
        "Sangat Kurang"
    ]
)

st.divider()

# =====================
# BAGIAN 6 – SARAN
# =====================
st.header("Bagian 6 – Saran dan Masukan")

kelebihan = st.text_area("Kelebihan utama dashboard ini")
kekurangan = st.text_area("Kekurangan atau hal yang perlu diperbaiki")
saran = st.text_area("Saran pengembangan dashboard ke depan")

st.divider()

# =====================
# SUBMIT
# =====================
if st.button("Kirim Kuesioner"):
    data = {
        "Timestamp": datetime.now(),
        "Unit Kerja": unit,
        "Jabatan": jabatan,
        "Peran Responden": peran,
        "Akses Tanpa Kendala": q1,
        "Tampilan Mudah Dipahami": q2,
        "Informasi Mudah Dimengerti": q3,
        "Visualisasi Informatif": q4,
        "Kesesuaian Grafik": q5,
        "Pemahaman Cepat": q6,
        "Relevansi Data": q7,
        "Monitoring & Evaluasi": q8,
        "Pengambilan Keputusan": q9,
        "Layak Dikembangkan": q10,
        "Penilaian Umum": penilaian_umum,
        "Kelebihan": kelebihan,
        "Kekurangan": kekurangan,
        "Saran": saran
    }

    df = pd.DataFrame([data])
    file_name = "hasil_kuesioner_dashboard_psp.csv"

    if os.path.exists(file_name):
        df.to_csv(file_name, mode="a", header=False, index=False)
    else:
        df.to_csv(file_name, index=False)

    st.success("Terima kasih 🙏 Kuesioner berhasil dikirim.")
