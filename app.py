import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Muat model pipeline dan label encoder
try:
    full_pipeline = joblib.load('student_performance_pipeline.pkl')
    label_encoder = joblib.load('status_label_encoder.pkl')
except FileNotFoundError:
    st.error("Model atau encoder tidak ditemukan. Pastikan file .pkl ada di direktori yang sama.")
    st.stop()

# DEFINISI MAPPING UNTUK KOLOM KATEGORI
marital_status_map = {
    "Single": 1,
    "Married": 2,
    "Widower": 3,
    "Divorced": 4,
    "Facto Union": 5,
    "Legally Separated": 6
}

application_mode_map = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}

course_map = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

daytime_evening_map = {
    "Daytime": 1,
    "Evening": 0
}

previous_qualification_map = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

nationality_map = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

mother_qualification_map = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Technical-professional course": 22,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

father_qualification_map = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "2nd year complementary high school course": 13,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Complementary High School Course": 20,
    "Technical-professional course": 22,
    "Complementary High School Course - not concluded": 25,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "General Course of Administration and Commerce": 31,
    "Supplementary Accounting and Administration": 33,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

mother_occupation_map = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Health professionals": 122,
    "teachers": 123,
    "Specialists in information and communication technologies (ICT)": 125,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "personal service workers": 151,
    "sellers": 152,
    "Personal care workers and the like": 153,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "cleaning workers": 191,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194
}

father_occupation_map = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Armed Forces Officers": 101,
    "Armed Forces Sergeants": 102,
    "Other Armed Forces personnel": 103,
    "Directors of administrative and commercial services": 112,
    "Hotel, catering, trade and other services directors": 114,
    "Specialists in the physical sciences, mathematics, engineering and related techniques": 121,
    "Health professionals": 122,
    "teachers": 123,
    "Specialists in finance, accounting, administrative organization, public and commercial relations": 124,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Information and communication technology technicians": 135,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "personal service workers": 151,
    "sellers": 152,
    "Personal care workers and the like": 153,
    "Protection and security services personnel": 154,
    "Market-oriented farmers and skilled agricultural and animal production workers": 161,
    "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence": 163,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in metallurgy, metalworking and similar": 172,
    "Skilled workers in electricity and electronics": 174,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "Fixed plant and machine operators": 181,
    "assembly workers": 182,
    "Vehicle drivers and mobile equipment operators": 183,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194,
    "Street vendors (except food) and street service providers": 195
}

# Mapping untuk kolom biner (0/1)
binary_map = {
    "Yes": 1,
    "No": 0
}
gender_map = {
    "Male": 1,
    "Female": 0
}


# AKHIR DEFINISI MAPPING

# Muat data asli untuk mendapatkan nilai default (mode/mean)
try:
    df = pd.read_csv('data.csv', sep=';')
except FileNotFoundError:
    st.error("File 'data.csv' tidak ditemukan. Pastikan ada di direktori /content/.")
    st.stop()


st.set_page_config(page_title="Prediksi Status Siswa", layout="wide")
st.title("Prediksi Status Akademik Siswa Jaya Institut")
st.markdown("Aplikasi ini memprediksi apakah seorang siswa akan Dropout, Enrolled, atau Graduate berdasarkan karakteristiknya.")

st.subheader("Input Data Siswa")

# Fungsi untuk mendapatkan input pengguna
def get_user_input(data_frame):
    input_data = {}

    with st.sidebar:
        st.header("Input Data Siswa")

        # Helper function untuk menentukan nilai tampilan default fitur kategorikal.
        def get_default_display(df_col, mapping):
            default_value = int(df_col.mode()[0])
            for display, value in mapping.items():
                if value == default_value:
                    return display
            return None # Jika mapping benar tidak akan terjadi

        # Input untuk fitur numerik
        input_data['Application_order'] = st.number_input(
            'Urutan Aplikasi (0-9)',
            min_value=0, max_value=9,
            value=int(data_frame['Application_order'].mean()),
            step=1
        )
        input_data['Previous_qualification_grade'] = st.number_input(
            'Nilai Kualifikasi Sebelumnya (0-200)',
            min_value=0, max_value=200,
            value=int(data_frame['Previous_qualification_grade'].mean()),
            step=1
        )
        input_data['Admission_grade'] = st.number_input(
            'Nilai Penerimaan (0-200)',
            min_value=0, max_value=200,
            value=int(data_frame['Admission_grade'].mean()),
            step=1
        )
        input_data['Age_at_enrollment'] = st.number_input(
            'Usia Saat Pendaftaran',
            min_value=17, max_value=80,
            value=int(data_frame['Age_at_enrollment'].mean()),
            step=1
        )
        input_data['Curricular_units_1st_sem_credited'] = st.number_input(
            'Unit Kurikuler Semester 1 (Dikreditkan)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_1st_sem_credited'].mean()),
            step=1
        )
        input_data['Curricular_units_1st_sem_enrolled'] = st.number_input(
            'Unit Kurikuler Semester 1 (Terdaftar)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_1st_sem_enrolled'].mean()),
            step=1
        )
        input_data['Curricular_units_1st_sem_evaluations'] = st.number_input(
            'Unit Kurikuler Semester 1 (Evaluasi)',
            min_value=0, max_value=45,
            value=int(data_frame['Curricular_units_1st_sem_evaluations'].mean()),
            step=1
        )
        input_data['Curricular_units_1st_sem_approved'] = st.number_input(
            'Unit Kurikuler Semester 1 (Lulus)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_1st_sem_approved'].mean()),
            step=1
        )
        input_data['Curricular_units_1st_sem_grade'] = st.number_input(
            'Nilai Unit Kurikuler Semester 1 (0-20)',
            min_value=0.0, max_value=20.0,
            value=data_frame['Curricular_units_1st_sem_grade'].mean(),
            step=0.1, format="%.1f"
        )
        input_data['Curricular_units_1st_sem_without_evaluations'] = st.number_input(
            'Unit Kurikuler Semester 1 (Tanpa Evaluasi)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_1st_sem_without_evaluations'].mean()),
            step=1
        )
        input_data['Curricular_units_2nd_sem_credited'] = st.number_input(
            'Unit Kurikuler Semester 2 (Dikreditkan)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_2nd_sem_credited'].mean()),
            step=1
        )
        input_data['Curricular_units_2nd_sem_enrolled'] = st.number_input(
            'Unit Kurikuler Semester 2 (Terdaftar)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_2nd_sem_enrolled'].mean()),
            step=1
        )
        input_data['Curricular_units_2nd_sem_evaluations'] = st.number_input(
            'Unit Kurikuler Semester 2 (Evaluasi)',
            min_value=0, max_value=45,
            value=int(data_frame['Curricular_units_2nd_sem_evaluations'].mean()),
            step=1
        )
        input_data['Curricular_units_2nd_sem_approved'] = st.number_input(
            'Unit Kurikuler Semester 2 (Lulus)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_2nd_sem_approved'].mean()),
            step=1
        )
        input_data['Curricular_units_2nd_sem_grade'] = st.number_input(
            'Nilai Unit Kurikuler Semester 2 (0-20)',
            min_value=0.0, max_value=20.0,
            value=data_frame['Curricular_units_2nd_sem_grade'].mean(),
            step=0.1, format="%.1f"
        )
        input_data['Curricular_units_2nd_sem_without_evaluations'] = st.number_input(
            'Unit Kurikuler Semester 2 (Tanpa Evaluasi)',
            min_value=0, max_value=30,
            value=int(data_frame['Curricular_units_2nd_sem_without_evaluations'].mean()),
            step=1
        )
        input_data['Unemployment_rate'] = st.number_input(
            'Tingkat Pengangguran (%)',
            min_value=0.0, max_value=20.0,
            value=data_frame['Unemployment_rate'].mean(),
            step=0.1, format="%.1f"
        )
        input_data['Inflation_rate'] = st.number_input(
            'Tingkat Inflasi (%)',
            min_value=0.0, max_value=10.0,
            value=data_frame['Inflation_rate'].mean(),
            step=0.1, format="%.1f"
        )
        input_data['GDP'] = st.number_input(
            'PDB (Gross Domestic Product)',
            min_value=0.0, max_value=25000.0,
            value=data_frame['GDP'].mean(),
            step=0.1, format="%.1f"
        )

        # Input untuk fitur kategorikal
        # Marital_status
        input_data['Marital_status'] = marital_status_map[st.selectbox(
            'Status Perkawinan',
            options=list(marital_status_map.keys()),
            index=list(marital_status_map.keys()).index(get_default_display(data_frame['Marital_status'], marital_status_map))
        )]

        # Application_mode
        input_data['Application_mode'] = application_mode_map[st.selectbox(
            'Mode Aplikasi',
            options=list(application_mode_map.keys()),
            index=list(application_mode_map.keys()).index(get_default_display(data_frame['Application_mode'], application_mode_map))
        )]
        
        # Course
        input_data['Course'] = course_map[st.selectbox(
            'Program Studi',
            options=list(course_map.keys()),
            index=list(course_map.keys()).index(get_default_display(data_frame['Course'], course_map))
        )]

        # Daytime_evening_attendance
        input_data['Daytime_evening_attendance'] = daytime_evening_map[st.selectbox(
            'Waktu Kuliah (Siang/Malam)',
            options=list(daytime_evening_map.keys()),
            index=list(daytime_evening_map.keys()).index(get_default_display(data_frame['Daytime_evening_attendance'], daytime_evening_map))
        )]

        # Previous_qualification
        input_data['Previous_qualification'] = previous_qualification_map[st.selectbox(
            'Kualifikasi Sebelumnya',
            options=list(previous_qualification_map.keys()),
            index=list(previous_qualification_map.keys()).index(get_default_display(data_frame['Previous_qualification'], previous_qualification_map))
        )]

        # Nationality
        input_data['Nationality'] = nationality_map[st.selectbox(
            'Kewarganegaraan',
            options=list(nationality_map.keys()),
            index=list(nationality_map.keys()).index(get_default_display(data_frame['Nacionality'], nationality_map))
        )]

        # Mothers_qualification
        input_data["Mothers_qualification"] = mother_qualification_map[st.selectbox(
            "Kualifikasi Pendidikan Ibu",
            options=list(mother_qualification_map.keys()),
            index=list(mother_qualification_map.keys()).index(get_default_display(data_frame["Mothers_qualification"], mother_qualification_map))
        )]

        # Fathers_qualification
        input_data["Fathers_qualification"] = father_qualification_map[st.selectbox(
            "Kualifikasi Pendidikan Ayah",
            options=list(father_qualification_map.keys()),
            index=list(father_qualification_map.keys()).index(get_default_display(data_frame["Fathers_qualification"], father_qualification_map))
        )]

        # Mothers_occupation
        input_data["Mothers_occupation"] = mother_occupation_map[st.selectbox(
            "Pekerjaan Ibu",
            options=list(mother_occupation_map.keys()),
            index=list(mother_occupation_map.keys()).index(get_default_display(data_frame["Mothers_occupation"], mother_occupation_map))
        )]

        # Fathers_occupation
        input_data["Fathers_occupation"] = father_occupation_map[st.selectbox(
            "Pekerjaan Ayah",
            options=list(father_occupation_map.keys()),
            index=list(father_occupation_map.keys()).index(get_default_display(data_frame["Fathers_occupation"], father_occupation_map))
        )]
        
        # Binary options (Yes/No)
        input_data['Displaced'] = binary_map[st.selectbox('Mahasiswa Pindahan?', options=list(binary_map.keys()), index=list(binary_map.keys()).index(get_default_display(data_frame['Displaced'], binary_map)))]
        input_data['Educational_special_needs'] = binary_map[st.selectbox('Berkebutuhan Khusus?', options=list(binary_map.keys()), index=list(binary_map.keys()).index(get_default_display(data_frame['Educational_special_needs'], binary_map)))]
        input_data['Debtor'] = binary_map[st.selectbox('Memiliki Tunggakan (Debitur)?', options=list(binary_map.keys()), index=list(binary_map.keys()).index(get_default_display(data_frame['Debtor'], binary_map)))]
        input_data['Tuition_fees_up_to_date'] = binary_map[st.selectbox('Pembayaran SPP Lancar?', options=list(binary_map.keys()), index=list(binary_map.keys()).index(get_default_display(data_frame['Tuition_fees_up_to_date'], binary_map)))]
        input_data['Scholarship_holder'] = binary_map[st.selectbox('Penerima Beasiswa?', options=list(binary_map.keys()), index=list(binary_map.keys()).index(get_default_display(data_frame['Scholarship_holder'], binary_map)))]
        input_data['International'] = binary_map[st.selectbox('Mahasiswa Internasional?', options=list(binary_map.keys()), index=list(binary_map.keys()).index(get_default_display(data_frame['International'], binary_map)))]
        
        # Gender - menggunakan gender_map
        input_data['Gender'] = gender_map[st.selectbox(
            'Jenis Kelamin',
            options=list(gender_map.keys()),
            index=list(gender_map.keys()).index(get_default_display(data_frame['Gender'], gender_map))
        )]


    return pd.DataFrame([input_data])

# Mendapatkan input pengguna
user_input_df = get_user_input(df)

# Menampilkan input pengguna (opsional, bisa dihapus nanti)
st.subheader("Data Input Anda")
st.write(user_input_df)

# Tombol Prediksi
if st.button("Prediksi Status"):
    # Lakukan prediksi
    prediction_proba = full_pipeline.predict_proba(user_input_df)
    prediction = full_pipeline.predict(user_input_df)

    # Decode hasil prediksi
    predicted_status = label_encoder.inverse_transform(prediction)[0]
    
    st.subheader("Hasil Prediksi")

    # Tampilkan hasil prediksi dengan warna dan ikon yang sesuai
    if predicted_status == 'Dropout':
        st.error(f"Prediksi Status: **{predicted_status}** ❌")
        st.warning(f"Probabilitas Dropout: **{prediction_proba[0][prediction[0]]*100:.2f}%**")
    elif predicted_status == 'Enrolled':
        st.info(f"Prediksi Status: **{predicted_status}** 💡")
        st.success(f"Probabilitas Enrolled: **{prediction_proba[0][prediction[0]]*100:.2f}%**")
    else: # Graduate
        st.success(f"Prediksi Status: **{predicted_status}** ✅")
        st.success(f"Probabilitas Graduate: **{prediction_proba[0][prediction[0]]*100:.2f}%**")

    st.info("Catatan: Ini adalah prediksi berdasarkan model machine learning. Akurasi model bergantung pada kualitas dan representasi data pelatihan.")