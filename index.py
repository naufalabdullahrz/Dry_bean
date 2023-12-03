import streamlit as st
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import MinMaxScaler



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

    # Memuat file CSV
    df = pd.read_excel('Dry_Bean_Dataset.xlsx')
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