Nama : M. Fatih Danika

NPM : 2506532100

Kelas : PBP B

## Local Setup Guide
1. Clone repository
```bash
   git clone https://github.com/XecovZ/myportofolio.git
```
2. Go to the project's directory
```bash
   cd myportofolio
```
3. Run the project
```bash
   python manage.py runserver
```
4. Open the local website on this link:
```bash
   http://127.0.0.1:8000/
```


### Tugas 1

1. Saya menggunakan `<section>` dan `<article>`. Walau keduanya memiliki fungsi yang sama sebagai container di HTML, saya merasa makna semantiknya membantu saya dalam aspek kerapihan kode dan membuat kode jadi lebih enak dibaca. Seperti pada kasus saya, `<section>` bermakna suatu bagian di web portofolio yang mengcontain pengalaman saya. Sementara `<article>` bermakna rincian dari pengalaman tersebut.


2. Setiap tipografi (terutama untuk judul section) harus besar di monitor laptop. Tapi jika dilihat dari handphone, teks tersebut hanya akan memakan banyak ruang di layar. Untuk itu, saya harus membuat setiap teks dapat beradaptasi di layar laptop dan handphone. Solusinya saya menggunakan clamp() pada font-size di css yang berfungsi untuk membuat minimum dan maximum size dari suatu teks. 


3. Pada saat mengimplementasi website portofolio impian, saya terpikirkan untuk menambah background "Particle Network Pattern" (referensi website: https://williamlin.io/). Namun, Gemini bilang bahwa implementasinya di CSS murni sangatlah kompleks karena titik-titiknya tersebar secara random. Setelah saya cari tahu lebih lanjut, ternyata orang-orang menggunakan JavaScript untuk membuatnya. Di situ saya sadar bahwa static web murni memiliki keterbatasan. Pada iterasi proyek selanjutnya (setelah belajar javascript), saya ingin menambahkan background tersebut di web portofolio saya. 


Link chat history tugas 1: https://share.gemini.google/eCaB7DvXX1I6


### Tugas 2

1. Project urls.py memeriksa awalan URL saat request masuk, kemudian mengarahkan ke urls.py punya aplikasi yang ingin dituju. App urls.py menerima arahan dari Project urls.py dan memanggil fungsi View yang menangani page tersebut. View menerima request, lalu meminta data yang dibutuhkan kepada Model. Model mengambil data dari database dan memberikannya ke View. View memberikan data yang diterima ke Template. Kemudian data-data tersebut dirender sebagai tampilan yang ditampilkan ke user.


2. Kalau kita punya sangat banyak data yang ingin ditampilkan, approach hard-coding akan membuat kode template menjadi tidak enak dilihat. Dengan menyimpan data pada model, kita bisa bebas mengupdate (add/edit/delete) data tanpa mengubah kode program. Selain itu, ada banyak manfaat apabila kita menyimpan data pada model, salah satunya adalah penambahan fitur pencarian dan filter.


3. `makemigrations` mengecek apakah ada perubahan pada models.py. Jika ada, secara otomatis membuat file baru di folder migrations sebagai blueprint migrasi. `migrate` membaca blueprint yang sudah dibuat `makemigrations` dan menjalankannya agar skema database terupdate dengan perubahan terbaru. Saya melakukan 2 kali remigration pada model Achievement ketika saya memutuskan untuk menghapus field "description" dan menghapus `auto_now_add=True` pada `achieved_at = models.DateTimeField()`


Link chat history tugas 2: https://share.gemini.google/xs8GHTYL9LQR


### Tugas 3

1. Penggunaan ModelForm membuat implementasi input data kita menjadi lebih modular. Manfaatnya kita tidak perlu membuat `<input>` secara manual di file htmlnya. Selain itu `ModelForm` juga sudah secara otomatis membuat form HTML berdasarkan arsitektur Model yang sudah didefinisikan di `models.py`. `{% csrf_token %}` digunakan sebagai aspek security yang melindungi website dari tindakan tak terautorisasi oleh orang asing (atau disebut serangan Cross-Site Request Forgery)


2. Karena JSON lebih ringan dan syntaxnya lebih simple. Selain itu JSON (JavaScript Object Notation) juga native untuk JavaScript yang merupakan bahasa yang populer dalam web development. 


3. Setelah client mengirim request ke URL di website portofolio, URL tersebut dikirim ke fungsi `show_model` di `views.py`. Fungsi tersebut memanggil fungsi `get_model_json` yang kemudian membuat perintah ORM secara otomatis untuk mengambil data dari database berupa QuerySet object. Setelah itu, object tersebut akan diberikan ke Serializer untuk diterjemahkan menjadi string JSON. Data JSON tersebut akhirnya dikembalikan pada client dalam bentuk HTTP Response yang dirender. Serialization berfungsi untuk menerjemahkan QuerySet object menjadi format JSON yang lebih mudah dibaca.


Link chat history tugas 3: https://share.gemini.google/azgSPG49PL6J


### AI Disclosure

Saya menggunakan Gemini 3.1 untuk membantu pengerjaan tugas PBP. Strategi yang saya gunakan adalah: Untuk HTML, saya minta untuk diberikan best practice dalam HTML, kemudian saya implementasikan itu sendiri dan meminta feedback apakah sudah sesuai atau belum. Untuk CSS, saya menggunakan Gemini untuk men-generate kode untuk styling, kemudian saya minta penjelasan untuk setiap baris kode yang dibuat agar saya paham apa yang dilakukan kode tersebut. Untuk komponen selain HTML dan CSS, saya mengerjakannya berdasarkan tutorial secara manual, kemudian meminta feedback apakah sudah benar atau belum.

Ketika terdapat erorr/bug, saya meminta Gemini untuk menjelaskan apa bug yang terjadi dan bagaimana caranya untuk memperbaiki hal tersebut. Selain itu, saya juga menggunakan Gemini untuk bertanya pertanyaan-pertanyaan yang lebih spesifik tentang kegunaan suatu kode (misal: "Apa bedanya `<section>` dan `<article>`?")