import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import pickle

# Set Page Layout
st.set_page_config(layout='wide')

#-----------------------------------------------------------------------
# Load the Dataset
# df = sns.load_dataset('tips')
#-----------------------------------------------------------------------
df = pd.read_csv("C:/Users/andry/Documents/project_adv/data/insurance_claims.csv")
# Title
st.title('TANGKAP')

# Subheader

#Separator
st.markdown('---')

#-----------------------------------------------------------------------


# Columns Input

st.subheader('| CLAIM DATAS')
st.markdown('## Data Tertanggung')

tanggal_lahir=st.date_input("Tanggal Lahir Tertangguna: ",value="default_value_today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False, label_visibility="visible")

gender = st.radio("Jenis Kelamin Tertanggung: ", ('Female', 'Male'))
if gender == "Female" :
    gender = 0
elif gender == "Male" :
    gender = 1

pendidikan = st.selectbox("Pendidikan Tertanggung: ",options=['High School','College','JD','MD','Masters','PhD','Associate'])
if pendidikan == "High School" :
    pendidikan = 1
elif pendidikan == "College" :
    pendidikan = 6
elif pendidikan == "JD" :
    pendidikan = 4
elif pendidikan == "MD" :
    pendidikan = 3
elif pendidikan == "Masters" :
    pendidikan = 0
elif pendidikan == "PhD" :
    pendidikan = 5
elif pendidikan == "Associate" :
    pendidikan = 2

pekerjaan = st.selectbox("Profesi Tertanggung: ",options=['craft-repair','machine-op-inspct', 'sales', 'armed-forces','tech-support', 'prof-specialty', 'other-service','priv-house-serv', 'exec-managerial', 'protective-serv','transport-moving', 'handlers-cleaners', 'adm-clerical','farming-fishing'])
if pekerjaan == "craft-repair" :
    pekerjaan = 12
elif pekerjaan == "handlers-cleaners" :
    pekerjaan = 4
elif pekerjaan == "machine-op-inspct" :
    pekerjaan = 7
elif pekerjaan == "sales" :
    pekerjaan = 9
elif pekerjaan == "adm-clerical" :
    pekerjaan = 3
elif pekerjaan == "farming-fishing" :
    pekerjaan = 13
elif pekerjaan == "armed-forces" :
    pekerjaan = 8
elif pekerjaan == "tech-support" :
    pekerjaan = 10
elif pekerjaan == "transport-moving" :
    pekerjaan = 11
elif pekerjaan == "prof-specialty" :
    pekerjaan = 5
elif pekerjaan == "protective-serv" :
    pekerjaan = 6
elif pekerjaan == "other-service" :
    pekerjaan = 2
elif pekerjaan == "exec-managerial" :
    pekerjaan = 14
elif pekerjaan == "priv-house-serv" :
    pekerjaan = 1

hobi = st.selectbox("Hobi Tertanggung: ",options=['sleeping', 'reading', 'board-games', 'bungie-jumping','base-jumping', 'golf', 'camping', 'dancing', 'skydiving','movies', 'hiking', 'yachting', 'paintball', 'chess', 'kayaking','polo', 'basketball', 'video-games', 'cross-fit', 'exercise'])
if hobi == "sleeping" :
    hobi = 8
elif hobi == "reading" :
    hobi = 14
elif hobi == "board-games" :
    hobi = 16
elif hobi == "bungie-jumping" :
    hobi = 4
elif hobi == "base-jumping" :
    hobi = 13
elif hobi == "golf" :
    hobi = 2
elif hobi == "camping" :
    hobi = 0
elif hobi == "kayaking" :
    hobi = 1
elif hobi == "dancing" :
    hobi = 3
elif hobi == "skydiving" :
    hobi = 10
elif hobi == "movies" :
    hobi = 5
elif hobi == "basketball" :
    hobi = 6
elif hobi == "hiking" :
    hobi = 12
elif hobi == "yachting" :
    hobi = 17
elif hobi == "paintball" :
    hobi = 11
elif hobi == "chess" :
    hobi = 19
elif hobi == "polo" :
    hobi = 15
elif hobi == "video-games" :
    hobi = 9
elif hobi == "cross-fit" :
    hobi = 18
elif hobi == "exercise" :
    hobi = 7

pernikahan = st.selectbox("Status Tertanggung: ",options=['Suami', 'Istri', 'Memiliki Anak', 'Belum Menikah','Lainnya','HTS'])
if pernikahan == "Suami" :
    pernikahan = 0
elif pernikahan == "Istri" :
    pernikahan = 3
elif pernikahan == "Memiliki Anak" :
    pernikahan = 1
elif pernikahan == "Belum Menikah" :
    pernikahan = 2
elif pernikahan == "Lainnya" :
    pernikahan = 4

st.markdown('---')
st.markdown('## Data Polis')
nomor_polis=st.text_input("Masukan No Polis", "No Polis")
tanggal_polis=st.date_input("Tanggal Polis Diterbitkan: ",value="default_value_today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
lokasi_polis = st.selectbox("Lokasi Polis Diterbitkan: ",options=['IL', 'IN', 'OH'])
if lokasi_polis == "OH" :
    lokasi_polis = 2
elif lokasi_polis == "IN" :
    lokasi_polis = 1
elif lokasi_polis == "IL" :
    lokasi_polis = 0
tipe_polis = st.selectbox("Tipe Pertanggungan: ",options=['250/500', '100/300', '500/1000'])
if tipe_polis == "100/300" :
    tipe_polis = 1
elif tipe_polis == "250/500" :
    tipe_polis = 2
elif tipe_polis == "500/1000" :
    tipe_polis = 0
deductible = st.radio("Jumlah Deductible: ", ('500','1000','2000'))
if deductible == "500" :
    surat_polisi = 2
elif deductible == "1000" :
    surat_polisi = 0
elif deductible == "2000" :
    surat_polisi = 1
#premi=st.slider("Jumlah Premi", 0, 10000)
umbrela_limit=st.slider("Limit Tambahan",0,9000000,step=1000000)

st.markdown('---')
st.markdown('## Data Objek Pertanggungan')
merek_kendaraan = st.selectbox("Merek Kendaraan: ",options=['Saab','Mercedes','Dodge','Chevrolet','Accura','Nissan','Audi','Toyota','Ford','Subaru','BMW','Jeep','Honda','Volkswagen'])
if merek_kendaraan == "Saab" :
    merek_kendaraan = 1
elif merek_kendaraan == "Mercedes" :
    merek_kendaraan = 2
elif merek_kendaraan == "Dodge" :
    merek_kendaraan = 1
elif merek_kendaraan == "Chevrolet" :
    merek_kendaraan = 0
elif merek_kendaraan == "Accura" :
    merek_kendaraan = 2
elif merek_kendaraan == "Nissan" :
    merek_kendaraan = 0
elif merek_kendaraan == "Audi" :
    merek_kendaraan = 2
elif merek_kendaraan == "Toyota" :
    merek_kendaraan = 0
elif merek_kendaraan == "Ford" :
    merek_kendaraan = 1
elif merek_kendaraan == "Subaru" :
    merek_kendaraan = 1
elif merek_kendaraan == "BMW" :
    merek_kendaraan = 2
elif merek_kendaraan == "Jeep" :
    merek_kendaraan = 2
elif merek_kendaraan == "Honda" :
    merek_kendaraan = 0
elif merek_kendaraan == "Volkswagen" :
    merek_kendaraan = 2

# tipe_kendaraan = st.selectbox("Tipe Kendaraan: ",options=['Luxury/Sports', 'SUV/Truck','Midsize SUV/Sedan'])
# if tipe_kendaraan == "Luxury/Sports" :
#     tipe_kendaraan = 1
# elif tipe_kendaraan == "SUV/Truck" :
#     tipe_kendaraan = 2
# elif tipe_kendaraan == "Midsize SUV/Sedan" :
#     tipe_kendaraan = 0

tahun_kendaraan=st.slider("Tahun Kendaraan", 1990, 2024)

#umbrela_limit=st.selectbox("Limit Tambahan: ",options=[0,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000])
st.markdown('---')
st.markdown('## Data Kecelakaan')
jumlah_kerugian=st.text_input("Masukan jumlah kerugian", "Nilai Kerugian")
lokasi_kecelakaan=st.selectbox("Lokasi Kecelakaan: ",options=['NC','NY','OH','PA','SC','VA','WV'])
if lokasi_kecelakaan == "SC" :
    lokasi_kecelakaan = 4
elif lokasi_kecelakaan == "VA" :
    lokasi_kecelakaan = 1
elif lokasi_kecelakaan == "NY" :
    lokasi_kecelakaan = 3
elif lokasi_kecelakaan == "OH" :
    lokasi_kecelakaan = 6
elif lokasi_kecelakaan == "WV" :
    lokasi_kecelakaan = 0
elif lokasi_kecelakaan == "NC" :
    lokasi_kecelakaan = 5
elif lokasi_kecelakaan == "PA" :
    lokasi_kecelakaan = 2

Lokasi_benturan=st.selectbox("Lokasi Benturan: ",options=['Belakang', 'Depan', 'Samping', 'Tidak Diketahui'])
if Lokasi_benturan == "Belakang" :
    Lokasi_benturan = 2
elif Lokasi_benturan == "Depan" :
    Lokasi_benturan = 2
elif Lokasi_benturan == "Samping" :
    Lokasi_benturan = 1
elif Lokasi_benturan == "Tidak Diketahui" :
    Lokasi_benturan = 0

saksi=st.slider("Jumlah Saksi", 0, 3)
jumlah_orang_luka=st.slider("Jumlah Orang Luka", 0, 2)
jumlah_kendaraan_terlibat=st.slider("Jumlah Kendaraan Terlibat", 0, 3)
tanggal_kejadian=st.date_input("Tanggal Kejadian: ",value="default_value_today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
surat_polisi = st.radio("Surat Keterangan Polisi: ", ('Ada','Tidak','Tidak Diketahui'))
if surat_polisi == "Ada" :
    surat_polisi = 0
elif surat_polisi == "Tidak" :
    surat_polisi = 1
elif surat_polisi == "Tidak Diketahui" :
    surat_polisi = 2

kerusakan_properti = st.radio("kerusakan_properti:", ('Ada','Tidak','Tidak diketahui'))
if kerusakan_properti == "Ada" :
    kerusakan_properti = 1
elif kerusakan_properti == "Tidak" :
    kerusakan_properti = 0
elif kerusakan_properti == "Tidak diketahui" :
    kerusakan_properti = 2

tingkat_kerusakan=st.selectbox("Tingkat Kerusakan: ",options=['Minor Damage','Trivial Damage','Major Damage','Total Loss'])
if tingkat_kerusakan == "Minor Damage" :
    tingkat_kerusakan = 1
elif tingkat_kerusakan == "Trivial Damage" :
    tingkat_kerusakan = 0
elif tingkat_kerusakan == "Major Damage" :
    tingkat_kerusakan = 3
elif tingkat_kerusakan == "Total Loss" :
    tingkat_kerusakan = 2

tipe_kecelakaan=st.selectbox("Tipe Kecelakaan: ",options=['Single Vehicle Collision','Vehicle Theft','Multi-vehicle Collision','Parked Car'])
if tipe_kecelakaan == "Single Vehicle Collision" :
    tipe_kecelakaan = 3
elif tipe_kecelakaan == "Vehicle Theft" :
    tipe_kecelakaan = 0
elif tipe_kecelakaan == "Multi-vehicle Collision" :
    tipe_kecelakaan = 2
elif tipe_kecelakaan == "Parked Car" :
    tipe_kecelakaan = 1

pihak_berwenang=st.selectbox("Pihak Berwenang: ",options=['Polisi','Pemadam Kebakaran','Ambulans','Lainnya'])
if pihak_berwenang == "Polisi" :
    pihak_berwenang = 0
elif pihak_berwenang == "Pemadam Kebakaran" :
    pihak_berwenang = 1
elif pihak_berwenang == "Ambulans" :
    pihak_berwenang = 2
elif pihak_berwenang == "Lainnya" :
    pihak_berwenang = 4

a=lokasi_polis
b=tipe_polis
c=deductible
#d=premi
e=umbrela_limit
f=gender
g=pendidikan
h=pekerjaan
i=hobi
j=pernikahan
k=tipe_kecelakaan
l=Lokasi_benturan
m=tingkat_kerusakan
n=pihak_berwenang
o=lokasi_kecelakaan
p=jumlah_kendaraan_terlibat
q=kerusakan_properti
r=jumlah_orang_luka
s=saksi
t=surat_polisi
u=jumlah_kerugian
#v=tipe_kendaraan
w=merek_kendaraan
umur_polis=(tanggal_kejadian-tanggal_polis)
umur_polis=umur_polis.days/365
# x=umur_polis
if (umur_polis)<=3:
    x=5
if (umur_polis)<=5:
    x=0
if (umur_polis)<=10:
    x=1
if (umur_polis)<=15:
    x=3
if (umur_polis)<=20:
    x=4
else:
    x=2
umur_kendaraan = int(tanggal_kejadian.year)-tahun_kendaraan
# y=umur_kendaraan
if (umur_kendaraan)<=1:
    y=4
elif (umur_kendaraan)<=3:
    y=3
elif (umur_kendaraan)<=5:
    y=0
elif (umur_kendaraan)<=10:
    y=5
elif (umur_kendaraan)<=15:
    y=2
else:
    y=1
data_pred=[[a,b,c,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,w,x,y]]
if (st.button("Submitted")):
    model1 = pickle.load(open('model/KNN2_ds.pkl', 'rb'))
    model2 = pickle.load(open('model/LogisticReg2_ds.pkl', 'rb'))
    model3 = pickle.load(open('model/SVM2_ds.pkl', 'rb'))
    model4 = pickle.load(open('model/DecisionTree_ds.pkl', 'rb'))
    model5 = pickle.load(open('model/XGBoost_ds.pkl', 'rb'))
    scaler2 = pickle.load(open('model/scaler2_ds.pkl', 'rb'))
    data_pred = scaler2.transform(data_pred)
    prediksi1 = int(model1.predict(data_pred))
    prediksi2 = int(model2.predict(data_pred))
    prediksi3 = int(model3.predict(data_pred))
    prediksi4 = int(model4.predict(data_pred))
    prediksi5 = int(model5.predict(data_pred))

    #-----------------------------------------------------------------------
    st.markdown('---')
    st.subheader('| RESULTS')
    if prediksi1 == 1:
        st.error("Hasil KNN: Indikasi Fraud")
    elif prediksi1 == 0:
        st.success("Hasil KNN: Indikasi Aman")
    if prediksi2 == 1:
        st.error("Hasil Logistic Regression: Indikasi Fraud")
    elif prediksi2 == 0:
        st.success("Hasil Logistic Regression: Indikasi Aman")
    if prediksi3 == 1:
        st.error("Hasil SVM: Indikasi Fraud")
    elif prediksi3 == 0:
        st.success("Hasil SVM: Indikasi Aman")
    if prediksi4 == 1:
         st.error("Hasil Decision Tree: Indikasi Fraud")
    elif prediksi4 == 0:
         st.success("Hasil Decision Tree: Indikasi Aman")
    if prediksi5 == 1:
        st.error("Hasil XGBoost: Indikasi Fraud")
    elif prediksi5 == 0:
        st.success("Hasil XGBoost: Indikasi Aman")
    # st.write ('button is Unclicked')


#-----------------------------------------------------------------------
