import streamlit as st

st.title('Selamat Datang!!')
st.header('Ini adalah simulasi untuk tahu kamu harus nabung berapa perbulan untuk punya barang impianmu.')

barang = st.text_input(label='Apa barang impianmu?',
                       value='Smartwatch')
harga = st.number_input(label='Berapa kira-kira harganya?', 
                        step=1,
                        value=1000000)

umurSekarang = st.slider(label='Umur berapa kamu sekarang?', 
                         step=1,
                         min_value=8,
                         max_value=70,
                         value=10)
umurNanti= st.slider(label='Umur berapa kamu pengen punya barang impianmu?',
                     step=1,
                     min_value=8,
                     max_value=70,
                     value=15)

nabung = st.number_input(label='Berapa kamu mau nabung perbulan?', 
                   step=1,
                   min_value=1000,
                   max_value=5000000)

bulan = (umurNanti - umurSekarang) * 12
revisi = int(harga/bulan)

if (bulan * nabung) >= harga:
    hasil =f'Yeayyy!!! Saat umur kamu {umurNanti}, kamu bakal punya {barang}.'
else:
    hasil = f'Aduuhh... Kayaknya kurang deh kalo nabung segitu. Kamu perlu nabung Rp{revisi:,} untuk beli {barang} impian kamu. Tetap semangat, yaaa...'

if st.button('kalkulasi'): st.title(hasil)