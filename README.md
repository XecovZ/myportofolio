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

### AI Disclosure

Saya menggunakan Gemini 3.1 untuk membantu pengerjaan tugas PBP. Strategi yang saya gunakan adalah: Untuk HTML, saya minta untuk diberikan best practice dalam HTML, kemudian saya implementasikan itu sendiri dan meminta feedback apakah sudah sesuai atau belum. Untuk CSS, saya menggunakan Gemini untuk men-generate kode untuk styling, kemudian saya minta penjelasan untuk setiap baris kode yang dibuat agar saya paham apa yang dilakukan kode tersebut.

Selain itu, saya juga menggunakan Gemini untuk bertanya pertanyaan-pertanyaan yang lebih spesifik tentang kegunaan suatu kode (misal: "Apa bedanya `<section>` dan `<article>`?")

Link chat history: https://share.gemini.google/eCaB7DvXX1I6