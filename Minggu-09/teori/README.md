Aplikasi Python akan sering menggunakan paket dan modul yang tidak disertakan sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi perpustakaan tertentu, karena aplikasi mungkin memerlukan bug tertentu yang telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi lama dari antarmuka perpustakaan.

Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venvbiasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3atau versi apa pun yang Anda inginkan.

Lokasi direktori umum untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian menyingkir sambil memberinya nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrok dengan .envfile definisi variabel lingkungan yang didukung beberapa perkakas.

(Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau fish shell, ada alternatif activate.cshdan activate.fishskrip yang sebaiknya Anda gunakan.)

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankannya pythonakan memberi Anda versi tertentu dan pemasangan Python.python -m pip freezeakan menghasilkan daftar serupa dari paket-paket yang diinstal, tetapi hasilnya menggunakan format yang diharapkan.

Anda dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama pip . Secara default pipakan menginstal paket dari Python Package Index . Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.pip memiliki sejumlah subperintah: "install", "uninstall", "freeze", dll. (Lihat panduan Memasang Modul Python untuk dokumentasi lengkap untuk pip.). 

