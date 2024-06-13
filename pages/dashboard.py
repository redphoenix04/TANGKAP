import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import warnings
import seaborn as sns
import plotly.express as px

warnings.filterwarnings("ignore")

# Set Page Layout
st.set_page_config(layout='wide')

####### Load Dataset #####################
GWP = pd.read_csv("data/GWP.csv")
GWP['Periode']= pd.to_datetime(GWP['Periode'])
GWP['year'] = GWP['Periode'].apply(lambda x: x.year)
GWP['month'] = GWP['Periode'].apply(lambda x: x.month)
#GWP=GWP[["bI_rate","kurs_dolar","inflasi","L_Real_Estate","H_Transportasi_dan_Pergudangan","G1_Perdagangan_Mobil_Sepeda_Motor_dan_Reparasinya","F_Konstruksi","K2_Asuransi_dan_Dana_Pensiun","C_PRODUK_DOMESTIK_BRUTO","Lini_Bisnis","Periode","year","month","Premi_akumulasi","Premi"]]
GWP=GWP[["Klaim","Lini_Bisnis","Periode","year","month","Premi_akumulasi","Klaim_akumulasi","Premi"]]
# SIDEBAR
# Let's add some functionalities in a sidebar
st.sidebar.subheader('Select to Filter the data')
filter_year = st.sidebar.selectbox("By Year: ",options=GWP['year'].unique(), index = GWP['year'].unique().tolist().index(GWP['year'].unique().max()))
filter_linibisnis = st.sidebar.multiselect("By Lini Bisnis: ",options=GWP['Lini_Bisnis'].unique(),default=GWP['Lini_Bisnis'].unique())
# filter_feature = st.sidebar.multiselect("Data Set Feature: ",options=list(GWP.columns),default=list(GWP.columns))
filter_trend_premi = st.sidebar.selectbox("Premi: ",options=['Premi','Premi_akumulasi'],index=['Premi','Premi_akumulasi'].index('Premi'))
filter_trend_klaim = st.sidebar.selectbox("Klaim: ",options=['Klaim','Klaim_akumulasi'],index=['Klaim','Klaim_akumulasi'].index('Klaim'))
filtered_GWP = GWP.query("year == @filter_year")
filtered_GWP2 = filtered_GWP.query("Lini_Bisnis == @filter_linibisnis")
Periode_max = filtered_GWP['Periode'].unique().max()
filtered_GWP3 = filtered_GWP2.query("Periode == @Periode_max")
filtered_GWP5 = GWP.query("Lini_Bisnis == @filter_linibisnis")
# Content

# Columns Summary
st.subheader('| QUICK SUMMARY')
col1, col2 = st.columns(2)
# column 1
with col1:
    total = f'Rp{int(filtered_GWP3.Premi_akumulasi.sum()):,}'
    st.write('###',total)
    st.write('#### GWP in Bio')
# column 2
with col2:
    total2 = f'Rp{int(filtered_GWP3.Klaim_akumulasi.sum()):,}'
    st.write('###',total2)
    st.write('#### Klaim in Bio')
st.markdown('---')
# # column 3
# with col3:
#     total2 =f'Rp{int((filtered_GWP3.kurs_dolar.sum()/filtered_GWP3.kurs_dolar.count())):,}'
#     st.write('###',total2)
#     st.text('Kurs Dollar')
# # column 4
# with col4:
#     total3 =f'{(filtered_GWP3.inflasi.sum()/filtered_GWP3.inflasi.count()):.2f}'
#     st.write('###',total3)    
#     st.text('Inflasi')
# with col5:
#     total4 = f'{(filtered_GWP3.C_PRODUK_DOMESTIK_BRUTO.sum()/filtered_GWP3.C_PRODUK_DOMESTIK_BRUTO.count()):.2f}'
#     st.write('###',total4)   
#     st.text('Produk Domestik Bruto')


st.subheader('| PREMIUM AND KLAIM TREND')
col11, col12 = st.columns(2)
with col11:
        GWP2=GWP[["Lini_Bisnis","Periode","Premi_akumulasi","Premi"]]
        filtered_GWP4 = GWP2.query("Lini_Bisnis == @filter_linibisnis")
        data1 = pd.DataFrame(filtered_GWP4.groupby(['Periode']).sum().reset_index())
        l1=px.line(data1, x="Periode" ,y=filter_trend_premi,title=filter_trend_premi)
        l1figure=st.plotly_chart(l1, use_container_width=True)
with col12:
        GWP1=GWP[["Lini_Bisnis","Periode","Klaim_akumulasi","Klaim"]]
        filtered_GWP4 = GWP1.query("Lini_Bisnis == @filter_linibisnis")
        data1 = pd.DataFrame(filtered_GWP4.groupby(['Periode']).sum().reset_index())
        l1=px.line(data1, x="Periode" ,y=filter_trend_klaim,title=filter_trend_klaim)
        l1figure=st.plotly_chart(l1, use_container_width=True)
        # l2=px.line(GWP, x="Periode" ,y=filter_trend_macro_economy,title=filter_trend_macro_economy)
        # l2figure=st.plotly_chart(l2, use_container_width=True)
st.markdown('---')
st.subheader('| BUSINESS LINI ANALYSIS')
col21, col22 = st.columns(2)
with col21:
    data1 = pd.DataFrame(filtered_GWP2.groupby(['Lini_Bisnis','Periode']).sum().reset_index())
    p1 = px.pie(data1,
            values='Premi',
            names='Lini_Bisnis',
            color='Lini_Bisnis',
            #color_discrete_map={'Male': 'royalblue','Female': 'pink'},
            title='Komposisi Premi by Lini Bisnis')
    p1.update_traces(textposition='inside',
            textinfo='percent+label',
            showlegend=False)
    p1figure=st.plotly_chart(p1, use_container_width=True)

with col22:
    data2 = pd.DataFrame(filtered_GWP5.groupby(['Lini_Bisnis','Periode']).sum().reset_index())
    b1=px.bar(data2,x="year",y="Premi",color='Lini_Bisnis',title='Growth Premi by Lini Bisnis')
    b1figure=st.plotly_chart(b1, use_container_width=True)

col31, col32 = st.columns(2)
with col31:
    data1 = pd.DataFrame(filtered_GWP2.groupby(['Lini_Bisnis','Periode']).sum().reset_index())
    p1 = px.pie(data1,
            values='Klaim',
            names='Lini_Bisnis',
            color='Lini_Bisnis',
            #color_discrete_map={'Male': 'royalblue','Female': 'pink'},
            title='Komposisi Klaim by Lini Bisnis')
    p1.update_traces(textposition='inside',
            textinfo='percent+label',
            showlegend=False)
    p1figure=st.plotly_chart(p1, use_container_width=True)

with col32:
    data2 = pd.DataFrame(filtered_GWP5.groupby(['Lini_Bisnis','Periode']).sum().reset_index())
    b1=px.bar(data2,x="year",y="Klaim",color='Lini_Bisnis',title='Growth Klaim by Lini Bisnis')
    b1figure=st.plotly_chart(b1, use_container_width=True)

plt.show()
st.markdown('---')
# column 3 - dataset
# st.subheader('| DATA')
# st.dataframe(filtered_GWP2[filter_feature].sort_values (by=["Lini_Bisnis","Periode"])) 

st.subheader('| CLAIM PROFILE')
st.write('##### Sumber Data: https://data.mendeley.com/datasets/992mh7dk9y/2')
df = pd.read_csv("data/insurance_claims.csv")
dfa = df.copy()
dfa['auto_model'] = dfa['auto_model'].map({'92x':'Luxury/Sports','E400':'Luxury/Sports','RAM':'SUV/Truck','Tahoe':'SUV/Truck','RSX':'Luxury/Sports','95':'Midsize SUV/Sedan','Pathfinder':'Midsize SUV/Sedan','A5':'Luxury/Sports','Camry':'Midsize SUV/Sedan','F150':'SUV/Truck','A3':'Luxury/Sports','Highlander':'SUV/Truck','Neon':'Midsize SUV/Sedan','MDX':'Midsize SUV/Sedan', 'Maxima':'Midsize SUV/Sedan','Legacy':'Midsize SUV/Sedan', 'TL':'Midsize SUV/Sedan', 'Impreza':'Midsize SUV/Sedan', 'Forrestor':'Midsize SUV/Sedan', 'Escape':'SUV/Truck', 'Corolla':'Midsize SUV/Sedan','3 Series':'Luxury/Sports', 'C300':'Luxury/Sports', 'Wrangler':'SUV/Truck', 'M5':'Luxury/Sports', 'X5':'Luxury/Sports', 'Civic':'Midsize SUV/Sedan', 'Passat':'Midsize SUV/Sedan','Silverado':'SUV/Truck', 'CRV':'Midsize SUV/Sedan', '93':'Midsize SUV/Sedan', 'Accord':'Midsize SUV/Sedan', 'X6':'Luxury/Sports', 'Malibu':'Midsize SUV/Sedan', 'Fusion':'Luxury/Sports','Jetta':'Midsize SUV/Sedan', 'ML350':'SUV/Truck','Ultima':'Luxury/Sports','Grand Cherokee':'SUV/Truck'})
dfa['auto_brand'] = dfa['auto_make'].map({'Saab':'High', 'Mercedes':'Luxury','Dodge':'High','Chevrolet':'Medium','Accura':'Luxury','Nissan':'Medium','Audi':'Luxury','Toyota':'Medium','Ford':'High','Suburu':'High','BMW':'Luxury','Jeep':'Luxury','Honda':'Medium','Volkswagen':'Luxury'})
criteria = [dfa['age'].between(0, 20), dfa['age'].between(21, 30), dfa['age'].between(31, 40), dfa['age'].between(41, 50),dfa['age'].between(51,60),dfa['age'].between(61,110)]
values = ['<= 20 Year','21-30 Year','31-40 Year','41-50 Year','50-60 Year','> 60 Year']
dfa['age_g']= np.select(criteria, values, 0)
dfa['incident_date']= pd.to_datetime(dfa['incident_date'])
dfa['incident_year'] = dfa['incident_date'].apply(lambda x: x.year)
dfa['car_age']=dfa['incident_year']-dfa['auto_year']
dfa['policy_bind_date']= pd.to_datetime(dfa['policy_bind_date'])
dfa['policy_age']=dfa['incident_date']-dfa['policy_bind_date']
dfa['policy_age'] =dfa['policy_age'].dt.days.astype('int16')
criteria1 = [dfa['policy_age'].between(-100000, 1095),dfa['policy_age'].between(1096, 1825),dfa['policy_age'].between(1826, 3650),dfa['policy_age'].between(3651,5475),dfa['policy_age'].between(5476,7300),dfa['policy_age'].between(7301,1000000)]
values1 = ['<=3 Year','3-5 Year','5-10 Year','10-15 Year','15-20 Year','>20 Year']
dfa['policy_age_g']= np.select(criteria1, values1, 0)
criteria2 = [dfa['car_age'].between(0,1),dfa['car_age'].between(2, 3),dfa['car_age'].between(4,5),dfa['car_age'].between(6,10),dfa['car_age'].between(11,15),dfa['car_age'].between(16,100)]
values2 = ['<= 1 Year','1-3 Year','3-5 Year','5-10 Year','10-15 Year','>15 Year']
dfa['car_age_g']= np.select(criteria2, values2, 0)
dfa=dfa.drop(['_c39'],axis=1)
st.markdown('---')
st.write('### Data Polis: ')
col41, col42 = st.columns(2)
with col41:
    data41 = pd.DataFrame(dfa.groupby(['policy_state','fraud_reported']).count().reset_index())
    b41=px.bar(data41,x="policy_state",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b41figure=st.plotly_chart(b41, use_container_width=True)

with col42:
    data42 = pd.DataFrame(dfa.groupby(['policy_csl','fraud_reported']).count().reset_index())
    b42=px.bar(data42,x="policy_csl",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by car_age_g')
    b42figure=st.plotly_chart(b42, use_container_width=True)

col43, col44 = st.columns(2)
with col43:
    data43 = pd.DataFrame(dfa.groupby(['policy_deductable','fraud_reported']).count().reset_index())
    b43=px.bar(data43,x="policy_deductable",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by policy_age_g')
    b43figure=st.plotly_chart(b43, use_container_width=True)

with col44:
    data44 = pd.DataFrame(dfa.groupby(['policy_age_g','fraud_reported']).count().reset_index())
    b44=px.bar(data44,x="policy_age_g",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b44figure=st.plotly_chart(b44, use_container_width=True)
st.markdown('---')
st.write('### Data Tertanggung: ')
col51, col52, col53 = st.columns(3)
with col51:
    data51 = pd.DataFrame(dfa.groupby(['insured_sex','fraud_reported']).count().reset_index())
    b51=px.bar(data51,x="insured_sex",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b51figure=st.plotly_chart(b51, use_container_width=True)

with col52:
    data52 = pd.DataFrame(dfa.groupby(['insured_education_level','fraud_reported']).count().reset_index())
    b52=px.bar(data52,x="insured_education_level",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by car_age_g')
    b52figure=st.plotly_chart(b52, use_container_width=True)

with col53:
    data53 = pd.DataFrame(dfa.groupby(['insured_occupation','fraud_reported']).count().reset_index())
    b53=px.bar(data53,x="insured_occupation",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by policy_age_g')
    b53figure=st.plotly_chart(b53, use_container_width=True)

col54, col55, col56 = st.columns(3)
with col54:
    data54 = pd.DataFrame(dfa.groupby(['insured_hobbies','fraud_reported']).count().reset_index())
    b54=px.bar(data54,x="insured_hobbies",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b54figure=st.plotly_chart(b54, use_container_width=True)

with col55:
    data55 = pd.DataFrame(dfa.groupby(['car_age_g','fraud_reported']).count().reset_index())
    b55=px.bar(data55,x="car_age_g",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by car_age_g')
    b55figure=st.plotly_chart(b55, use_container_width=True)

with col56:
    data56 = pd.DataFrame(dfa.groupby(['insured_relationship','fraud_reported']).count().reset_index())
    b56=px.bar(data56,x="insured_relationship",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by policy_age_g')
    b56figure=st.plotly_chart(b56, use_container_width=True)
st.markdown('---')
st.write('### Data Kendaraan: ')
col61, col62, col63 = st.columns(3)
with col61:
    data61 = pd.DataFrame(dfa.groupby(['auto_model','fraud_reported']).count().reset_index())
    b61=px.bar(data61,x="auto_model",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b61figure=st.plotly_chart(b61, use_container_width=True)

with col62:
    data62 = pd.DataFrame(dfa.groupby(['auto_brand','fraud_reported']).count().reset_index())
    b62=px.bar(data62,x="auto_brand",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by car_age_g')
    b62figure=st.plotly_chart(b62, use_container_width=True)

with col63:
    data63 = pd.DataFrame(dfa.groupby(['car_age_g','fraud_reported']).count().reset_index())
    b63=px.bar(data63,x="car_age_g",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by policy_age_g')
    b63figure=st.plotly_chart(b63, use_container_width=True)
st.markdown('---')
st.write('### Data Kejadian: ')
                #    'insured_sex',
                #    'insured_education_level',
                #    'insured_occupation',
                #    'insured_hobbies',
                #    'insured_relationship',
                #    'incident_type',
                #    'collision_type',
                #    'incident_severity',
                #    'authorities_contacted',
                #    'property_damage',
                #    'police_report_available',
                #    'auto_model',
                #    'auto_brand',
                #    'age_g',
                #    'car_age_g',
                #    'policy_age_g',
                #    'policy_deductable'
col71, col72, col73 = st.columns(3)
with col71:
    data71 = pd.DataFrame(dfa.groupby(['incident_type','fraud_reported']).count().reset_index())
    b71=px.bar(data71,x="incident_type",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b71figure=st.plotly_chart(b71, use_container_width=True)

with col72:
    data72 = pd.DataFrame(dfa.groupby(['collision_type','fraud_reported']).count().reset_index())
    b72=px.bar(data72,x="collision_type",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by car_age_g')
    b72figure=st.plotly_chart(b72, use_container_width=True)

with col73:
    data73 = pd.DataFrame(dfa.groupby(['incident_severity','fraud_reported']).count().reset_index())
    b73=px.bar(data73,x="incident_severity",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by policy_age_g')
    b73figure=st.plotly_chart(b73, use_container_width=True)

col74, col75, col76 = st.columns(3)
with col74:
    data74 = pd.DataFrame(dfa.groupby(['authorities_contacted','fraud_reported']).count().reset_index())
    b74=px.bar(data74,x="authorities_contacted",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by auto_brand')
    b74figure=st.plotly_chart(b74, use_container_width=True)

with col75:
    data75 = pd.DataFrame(dfa.groupby(['property_damage','fraud_reported']).count().reset_index())
    b75=px.bar(data75,x="property_damage",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by car_age_g')
    b75figure=st.plotly_chart(b75, use_container_width=True)

with col76:
    data76 = pd.DataFrame(dfa.groupby(['police_report_available','fraud_reported']).count().reset_index())
    b76=px.bar(data76,x="police_report_available",y="policy_number",color='fraud_reported',color_discrete_map={'Y':'red','N':'blue'},title='Fraud Report by policy_age_g')
    b76figure=st.plotly_chart(b76, use_container_width=True)
