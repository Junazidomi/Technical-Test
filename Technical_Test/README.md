# Technical Test Bit Health


### Cara menjalankan

1. Buat envirotment Anaconda dengan cara
   
   ```
     conda create Technical Test
   ```
2. Jalankan aplikasi dengan cara
   
   ```
    python -m uvicorn app.main:app --reload
   ```
3. Silahkan akses link tersebut dan lakukan 

     ```
      http://127.0.0.1:8000/docs
     ```
### Explanation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan hasil analisis dan refaktor program, refaktor dilakukan dengan memisahkan proses ke dalam beberapa modul dan class yang memiliki tanggung jawab yang jelas agar lebih mudah dalam pemeliharaan. Selain itu, logika HTTP dipisahkan dari logika bisnis, penyimpanan data, dan proses embedding. Pendekatan enkapsulasi juga diterapkan dengan membagi tanggung jawab ke dalam beberapa komponen, seperti EmbeddingService untuk menangani embedding, DocumentStore untuk pengelolaan penyimpanan data (Qdrant dan in-memory), serta RagWorkflow untuk mengatur alur retrieval dan answering. Pendekatan ini bertujuan untuk menghindari penggunaan global state, mengurangi coupling antar komponen, serta mempermudah proses pengujian (testing) dan pemeliharaan kode di masa depan.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Salah satu pertimbangan yang diambil adalah tidak menyertakan kerangka kerja injeksi dependensi atau sistem konfigurasi yang lebih kompleks.
Metode ini membatasi fleksibilitas konfigurasi yang luas yang diperlukan pada skala produksi yang lebih besar, tetapi membuat kode menjadi sederhana dan mudah dipahami. Kompromi ini dibuat untuk menjaga fokus refactoring pada kualitas struktur kode daripada menambah kompleksitas.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Setelah dilakukan refaktor, versi ini mampu meningkatkan maintainability karena proses pemeliharaan maupun pengembangan dapat dilakukan secara terisolasi pada masing-masing komponen. Refaktor dilakukan dengan tujuan mempermudah pengguna (developer) dalam melakukan pengembangan, pemeliharaan, serta memahami alur kerja aplikasi. Hal ini dicapai dengan memisahkan proses-proses yang sebelumnya berada dalam satu program menjadi beberapa modul atau komponen yang memiliki tanggung jawab yang jelas. Selain itu, struktur folder yang tertata dengan baik serta penamaan modul dan class yang eksplisit membantu pengguna dalam memahami fungsi dan peran setiap bagian dari program secara lebih cepat dan intuitif.




