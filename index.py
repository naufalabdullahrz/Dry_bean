import streamlit as st
import numpy as np
import aksi
import time
import webbrowser
import pandas as pd
import joblib
# Memuat model SVM dari file .pkl
# rf_model_path = open('Model\saved_data.joblib','rb')
# svm_model = joblib.load(rf_model_path)

with st.sidebar:
    kolom = st.columns((1, 1, 2.7))
    home = kolom[1].button('Home',type='primary')
    Tools = kolom[2].button('Tools')

if Tools==False and home==True:
   # Memuat file 
    df = pd.read_excel('Model\Dry_Bean_Dataset.xlsx')

    # Set judul halaman
    st.title('Dry Bean')

    # Menampilkan tabel
    st.write('## Dataset Overview')
    st.dataframe(df)

    # Menampilkan penjelasan dataset
    st.write('## Penjelasan Dataset')
    st.markdown('1. **Area : Luas zona kacang dan jumlah piksel dalam batasnya.')
    st.markdown('2. **Perimeter : Keliling kacang didefinisikan sebagai panjang tepinya.')
    st.markdown('3. **Major axis length : Jarak antara ujung-ujung garis terpanjang yang dapat ditarik dari sebuah kacang.')
    st.markdown('4. **Minor axis length : Garis terpanjang yang dapat ditarik dari kacang sambil berdiri tegak lurus terhadap sumbu utama.')
    st.markdown('5. **Aspect ratio : Mendefinisikan hubungan antara L dan l.')
    st.markdown('6. **Eccentricity : Eksentrisitas elips yang momennya sama dengan daerah.')
    st.markdown('7. **Convex area : Jumlah piksel dalam poligon cembung terkecil yang dapat memuat luas biji kacang.')
    st.markdown('8. **Equivalent diameter : Diameter lingkaran yang luasnya sama dengan luas biji kacang.')
    st.markdown('9. **Extent : Rasio piksel dalam kotak pembatas dengan area kacang.')
    st.markdown('10. **Solidity : Juga dikenal sebagai konveksitas. Rasio piksel pada cangkang cembung dengan piksel pada kacang.')
    st.markdown('11. **Roundness : Dihitung dengan rumus berikut: (4piA)/(P^2)')
    st.markdown('12. **Compactness : Mengukur kebulatan suatu benda: Ed/L')
    st.markdown('13. **ShapeFactor1 : Faktor Bentuk 1')
    st.markdown('14. **ShapeFactor2 : Faktor Bentuk 2')
    st.markdown('15. **ShapeFactor3 : Faktor Bentuk 3')
    st.markdown('16. **ShapeFactor4 : Faktor Bentuk 4')

if home == False and Tools == False or home == False and Tools == True:
    st.title('Tools')
    st.write("""
    Harap Isi Data Sesuai Kolom, Data Tidak Boleh Kosong
    """)
    Area = st.number_input("Area", format="%.5f")  # Set step ke nilai pecahan
    Perimeter = st.number_input("Perimeter", format="%.5f")
    MajorAxisLength = st.number_input("Major_Axis_Length", format="%.5f")
    Eccentricity = st.number_input("Eccentricity", format="%.5f")
    ConvexArea = st.number_input("Convex_Area", format="%.5f")
    EquivDiameter = st.number_input("EquivDiameter", format="%.5f")
    Extent = st.number_input("Extent", format="%.5f")
    Compactness = st.number_input("Compactness", format="%.5f")
    ShapeFactor1 = st.number_input("ShapeFactor1", format="%.5f")
    ShapeFactor2 = st.number_input("ShapeFactor2", format="%.5f")
    ShapeFactor3 = st.number_input("ShapeFactor3", format="%.5f")


  
    if st.button("submit"):
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        from sklearn.feature_selection import SelectKBest, f_classif
        from sklearn.preprocessing import MinMaxScaler
        import pandas as pd

        # Memuat file CSV
        df = pd.read_excel('Model\Dry_Bean_Dataset.xlsx')
        X = df.drop(['Class'], axis=1)
        y = df["Class"]
        X = df.drop(['MinorAxisLength','AspectRation','Solidity','roundness','ShapeFactor4','Class'], axis=1)
        from sklearn.model_selection import train_test_split


        # Pembagian data menjadi data latih dan data uji (80% data latih, 20% data uji)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = MinMaxScaler()
        X_train_scaler = scaler.fit_transform(X_train)
        X_test_scaler = scaler.transform(X_test)
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score, classification_report


        #Buat model Random Forest
        random_forest_model = RandomForestClassifier(n_estimators=100)
        #Latih model
        random_forest_model.fit(X_train, y_train)
        #Prediksi dengan model
        data = [Area, Perimeter, MajorAxisLength, Eccentricity, ConvexArea, EquivDiameter, Extent, Compactness, ShapeFactor1, ShapeFactor2, ShapeFactor3]
        random_forest_predictions = random_forest_model.predict([data])

        

        # Normalisasi data menggunakan fungsi normalisasi yang telah ditambahkan
        

        # Melakukan prediksi dengan model SVM
        

        # Menampilkan hasil prediksi
        st.header('Hasil Prediksi')
        st.write(f'Model SVM memprediksi kelas: {random_forest_predictions}')


# with st.sidebar:
#     st.write('Link:')
#     link = '[GitHub](https://github.com/Revichi/appdataset)'
#     st.markdown(link, unsafe_allow_html=True)
#     link = '[Jupyter Book](https://revichi.github.io/datamining/App.html?highlight=penambangan)'
#     st.markdown(link, unsafe_allow_html=True)