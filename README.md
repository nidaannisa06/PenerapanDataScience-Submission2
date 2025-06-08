# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama perjalanannya, institusi ini telah berhasil mencetak banyak lulusan berkualitas dengan reputasi yang sangat baik. Namun, di balik keberhasilan tersebut, Jaya Jaya Institut menghadapi tantangan serius: tingginya angka dropout siswa. Fenomena ini menjadi perhatian utama karena berdampak pada reputasi, efisiensi operasional, dan keberlangsungan institusi.

### Permasalahan Bisnis
1. **Tingginya Angka Dropout Siswa** : Banyak siswa yang tidak menyelesaikan pendidikan mereka, yang menyebabkan kerugian sumber daya dan potensi.
2. **Keterlambatan Deteksi Dropout** : Institusi kesulitan mengidentifikasi siswa yang berpotensi dropout sejak dini, sehingga upaya bimbingan atau intervensi terlambat dilakukan.
3. **Kurangnya Pemahaman Data** : Jaya Jaya Institut membutuhkan cara yang lebih mudah untuk memahami data siswa dan memonitor performa mereka secara berkelanjutan.

### Cakupan Proyek
1. Analisis Data Siswa: Melakukan eksplorasi dan analisis mendalam terhadap data siswa untuk mengidentifikasi faktor-faktor yang berkorelasi dengan dropout dan performa siswa.
2. Pengembangan Model Machine Learning: Membangun model Machine Learning yang mampu memprediksi siswa yang berpotensi dropout berdasarkan data yang tersedia.
3. Pembuatan Dashboard Bisnis: Mengembangkan dashboard interaktif yang memvisualisasikan data performa siswa dan insight dari analisis, memudahkan Jaya Jaya Institut dalam memantau dan mengambil keputusan.
4. Deployment Prototype ML: Membuat prototype sistem Machine Learning dalam bentuk aplikasi web (Streamlit) yang dapat diakses oleh user untuk memprediksi potensi dropout.
5. Pemberian Rekomendasi: Memberikan rekomendasi action items berdasarkan temuan dari analisis data dan model Machine Learning untuk membantu Jaya Jaya Institut mengurangi angka dropout dan meningkatkan performa siswa.

### Persiapan

Sumber data: [Student's Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
- Proyek ini dapat dijalankan dengan mudah menggunakan Google Colabolatory (Colab), yang menyediakan *environment* siap pakai dengan sebagian besar dependensi yang sudah **terinstal**.
- Namun jika ingin menjalankan proyek ini secara local di komputer pribadi, disarankan untuk menggunakan virtual environment untuk mengelola dependensi proyek:

**1. Membuat Virtual Environment (opsional, untuk lokal)**:
Buka terminal atau command prompt, lalu navigasikan ke direktori proyek Anda. Jalankan perintah berikut:

```Bash
python -m venv venv
```

**2. Mengaktifkan Virtual Environment (opsional, untuk lokal)** :
- Windows:
```Bash
.\venv\Scripts\activate
```

- macOS / Linux:
```Bash
    source venv/bin/activate
```

**3. Instalasi Dependensi** :
- Baik di Google Colab maupun di environment lokal (setelah mengaktifkan virtual environment), Anda mungkin perlu menginstal beberapa library tambahan yang tidak tersedia secara default. Pastikan Anda berada di direktori proyek dan jalankan perintah berikut:
```Bash
    pip install -r requirements.txt
```
- Catatan: Jika ada library yang perlu diinstal di Colab, Anda bisa menambahkannya di sel kode awal notebook Colab Anda dengan:
```Bash
!pip install nama_library
```
- Catatan: Untuk menjalankan prediction notebook dibutuhkan file yang ada di folder model.

## **Cara Menjalankan Proyek**
**Menggunakan Google Colaboratory (Direkomendasikan)**
1. **Buka Notebook** : Unggah atau buka file notebook .ipynb proyek ini di Google Colab.
2. **Jalankan Semua Sel** : Pastikan Anda menjalankan semua sel kode secara berurutan, dari atas ke bawah. Ini akan memproses data, melatih model (jika ada), dan menyiapkan dashboard.
3. **Akses Dashboard** : Untuk mengakses dashboard di Looker Studio, gunakan tautan yang disediakan di bagian "Business Dashboard" di bawah ini.

## **Menjalankan Secara Lokal (Opsional)**
Jika telah melakukan langkah-langkah Setup Environment di atas untuk menjalankan proyek secara lokal:
1. Pastikan Virtual Environment Aktif: Di terminal atau command prompt, pastikan Anda telah mengaktifkan virtual environment.
2. Jalankan Skrip Utama: Navigasikan ke direktori utama proyek Anda. Kemudian, jalankan file Python utama proyek Anda. Jika file utama Anda adalah main.py, app.py, atau dashboard.py (sesuaikan dengan nama file Anda):

```Bash
    python nama_file_utama_anda.py
```

3. Akses Dashboard: Setelah skrip berhasil dijalankan, jika dashboard Anda di-hosting secara lokal, alamat akses biasanya akan ditampilkan di terminal (misalnya, http://127.0.0.1:8050/ atau http://localhost:5000/). Namun, untuk dashboard Looker Studio, Anda cukup mengakses tautan [Student's Performance Dasboard Jaya Jaya Institut](https://lookerstudio.google.com/reporting/9467bde1-b17d-404e-8656-25e4eac16513).

## Business Dashboard
Saya telah membuat business dashboard yang bertujuan untuk membantu Jaya Jaya Institut dalam memahami data siswa dan memonitor performa mereka. Dashboard ini berisi visualisasi kunci yang menampilkan distribusi nilai siswa, faktor-faktor demografis yang mungkin memengaruhi performa, serta tren performa dari waktu ke waktu (jika data memungkinkan).

[Student's Performance Dasboard Jaya Jaya Institut](https://lookerstudio.google.com/reporting/9467bde1-b17d-404e-8656-25e4eac16513)

## Menjalankan Sistem Machine Learning
Saya telah mengembangkan prototype sistem Machine Learning menggunakan Streamlit yang siap digunakan untuk memprediksi potensi dropout siswa.
Anda dapat mengakses prototype sistem Machine Learning ini secara langsung melalui deployment di Streamlit Community Cloud:
[Link Deployment Streamlit](https://penerapandatascience-submission2-ip6c28uldcf8pn3kbqf4zk.streamlit.app/)

### Cara Menjalankan Proyek
1. Menggunakan Google Colaboratory (Direkomendasikan)
- Buka Notebook: Unggah atau buka file notebook .ipynb proyek ini di Google Colab.
- Jalankan Semua Sel: Pastikan Anda menjalankan semua sel kode secara berurutan, dari atas ke bawah. Ini akan memproses data, melatih model (jika ada), dan menyiapkan dashboard.
- Akses Dashboard: Untuk mengakses dashboard di Looker Studio (atau tool lain), gunakan tautan yang disediakan di bagian "Business Dashboard" di atas.

2. Menjalankan Secara Lokal (Opsional)
- Jika telah melakukan langkah-langkah Setup Environment di atas untuk menjalankan proyek secara lokal:
- Pastikan Virtual Environment Aktif: Di terminal atau command prompt, pastikan Anda telah mengaktifkan virtual environment.
- Jalankan Skrip Utama: Navigasikan ke direktori utama proyek Anda. Kemudian, jalankan file Python utama proyek Anda. Jika file utama Anda adalah main.py, app.py, atau dashboard.py (sesuaikan dengan nama file Anda, dalam kasus ini adalah app.py untuk Streamlit):
```Bash
streamlit run app.py
```
- Akses Dashboard: Setelah skrip Streamlit berhasil dijalankan, aplikasi akan terbuka otomatis di browser Anda (biasanya di http://localhost:8501). Namun, untuk dashboard eksternal seperti Looker Studio, Anda cukup mengakses tautan yang diberikan di bagian "Business Dashboard".


## Conclusion
Berdasarkan analisis data dan pengembangan model Machine Learning, proyek ini berhasil mengidentifikasi faktor-faktor kunci yang berkontribusi terhadap potensi dropout siswa di Jaya Jaya Institut. Model Machine Learning yang telah dibangun dapat memprediksi risiko dropout dengan tingkat akurasi tertentu, memungkinkan institusi untuk mengidentifikasi siswa berisiko lebih awal. Dashboard yang telah dibuat juga memberikan gambaran visual yang jelas mengenai performa siswa dan distribusi faktor-faktor terkait, mempermudah pemantauan dan pengambilan keputusan berbasis data. Dengan demikian, Jaya Jaya Institut kini memiliki alat yang lebih baik untuk proaktif dalam menangani masalah dropout dan meningkatkan keberhasilan siswa.

### Rekomendasi Action Items
Berikut adalah beberapa rekomendasi action items yang dapat dilakukan Jaya Jaya Institut berdasarkan temuan proyek ini untuk mengurangi angka dropout dan mencapai target mereka:
- Menerapkan Sistem Deteksi Dini: Gunakan prototype Machine Learning yang telah dibuat untuk secara rutin memprediksi siswa yang berisiko dropout. Identifikasi siswa dengan skor risiko tinggi dan segera lakukan intervensi.
- Program Bimbingan Intensif: Bagi siswa yang teridentifikasi berisiko tinggi dropout, institusi dapat merancang dan mengimplementasikan program bimbingan atau mentoring khusus. Ini bisa melibatkan konseling akademik, dukungan psikologis, atau bantuan finansial jika relevan.
- Peningkatan Komunikasi dan Keterlibatan: Tingkatkan komunikasi dengan siswa dan orang tua, terutama bagi mereka yang menunjukkan penurunan performa atau indikasi dropout. Dorong partisipasi siswa dalam kegiatan kampus atau kelompok studi untuk meningkatkan rasa memiliki dan keterlibatan.
- Peninjauan Kurikulum dan Metode Pengajaran: Berdasarkan insight dari dashboard (misalnya, mata pelajaran tertentu yang seringkali menjadi pemicu penurunan performa), institusi dapat meninjau dan menyesuaikan kurikulum atau metode pengajaran untuk area-area tersebut guna membuatnya lebih menarik dan efektif.
- Monitoring Berkelanjutan: Manfaatkan business dashboard untuk memantau performa siswa secara berkelanjutan. Identifikasi tren, anomali, dan faktor-faktor baru yang mungkin memengaruhi dropout untuk penyesuaian strategi di masa mendatang.
