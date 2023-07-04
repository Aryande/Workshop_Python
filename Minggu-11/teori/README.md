Flask (Labu) Dalam membuat environment maka langkah yang harus di lakukan : - conda create -n workshopy python=22.9.0- aktifkan dengan : conda active workshopy - selanjutnya baru install flask dengan : pip install flask

kemudia membuat sebuah tampilan dengan memberikan ucapan hello word 

untuk menjalankan Flask_APP yang telah di buat Server Terlihat Secara Eksternal Akan melihat bahwa server hanya dapat diakses dari komputer sendiri, bukan dari komputer lain dalam jaringan. Ini adalah default karena dalam mode debugging, pengguna aplikasi dapat mengeksekusi kode Python sewenang-wenang di komputer

Variabel lingkungan FLASK_APP adalah nama modul yang akan diimport saat labu dijalankan. Jika modul tersebut salah diberi nama, Anda akan mendapatkan kesalahan import saat memulai (atau jika debug diaktifkan saat menavigasi ke aplikasi)

Perintah flask run dapat melakukan lebih dari sekadar memulai server pengembangan. Dengan mengaktifkan mode debug, server akan secara otomatis memuat ulang jika kode berubah, dan akan menampilkan debugger interaktif di browser jika terjadi kesalahan selama permintaan.

Saat mengembalikan HTML (tipe respons default di Flask), setiap nilai yang diberikan pengguna yang dirender dalam output harus diloloskan untuk melindungi dari serangan injeksi. HTML Template yang di gunakan from markupsafe import escape

@app.route("/") def hello(name): return f"Hello, {escape(name)}!"
