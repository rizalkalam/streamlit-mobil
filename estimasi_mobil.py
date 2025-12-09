import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), "estimasi_mobil_ford.sav")
model = pickle.load(open(model_path, "rb"))

st.title('Estimasi Harga Mobil Bekas Ford')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Jarak Tempuh (dalam mil)')
tax = st.number_input('Input Pajak Tahunan (dalam £)')
mpg = st.number_input('Input konsumsi bahan bakar (MPG)')
engine_size = st.number_input('Input engine size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engine_size]]
    )
    st.write(f'Estimasi Harga Mobil Bekas Ford: £{predict[0]:.2f}', predict)
    st.write('Estimasi Harga Mobil Bekas Ford dalam Rupiah: Rp{:,}'.format(int(predict*19000)))