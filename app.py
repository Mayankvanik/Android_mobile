import streamlit as st
import pandas as pd
import pickle



pipe = pickle.load(open('pipexg.pkl','rb'))
df = pickle.load(open('d1.pkl','rb'))

st.title('Android Mobile Price Predictor')

#brand
company = st.selectbox('Brand',df ['brand'].unique())

#display_quality
display = st.selectbox('Display Quality',df ['display_quality'].unique())

#processor
processor = st.selectbox('Processor',df ['processor_brand'].unique())

#5G
g5 = st.selectbox('5G',['Yes','No'])

#camera
camera = st.selectbox('Primary Camera MP',df ['primary_rear_lens'].unique())

#nfc
nfc = st.selectbox('NFC',['Yes','No'])

#processor speed
processor_speed = st.selectbox('Processor Performance',df ['processor_speed'].unique())

#ram
ram = st.selectbox('RAM',df ['ram_capacity'].unique())

#memory
internal = st.selectbox('Internal Memory',df ['internal_memory'].unique())

if st.button('Predict Price'):

    if g5 == 'Yes':
        g5 = 1
    else:
        g5 = 0

    if nfc == 'Yes':
        nfc = 1
    else:
        nfc = 0


    new_data = pd.DataFrame({
        'brand': [company],
        'display_quality': [display],
        'processor_brand': [processor],
        'has_5g': [g5],
        'primary_rear_lens': [camera],
        'has_nfc': [nfc],
        'processor_speed': [processor_speed],
        'ram_capacity': [ram],
        'internal_memory': [internal]
    })
    #query = np.array([company,display,processor,g5,camera,nfc,processor_speed,ram,internal])

    #query = query.reshape(1,9)
    #print(query)
    st.title("The Predicted price of This Mobile Is "+ str(pipe.predict(new_data)[0]))
