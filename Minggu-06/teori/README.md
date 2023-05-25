8. Errors and Exceptions
Sampai saat ini pesan kesalahan belum banyak disebutkan,Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaks dan pengecualian .
8.1. Syntax Errors
Kesalahan sintaksis, juga dikenal sebagai kesalahan parsing, mungkin merupakan jenis keluhan paling umum. Parser mengulangi baris yang menyinggung dan menampilkan 'panah' kecil yang menunjuk ke titik paling awal di baris tempat kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token yang mendahului tanda panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua ( ':') tidak ada sebelumnya. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari jika input berasal dari skrip.
8.2. Exceptions
ekspresi benar secara sintaksis, itu dapat menyebabkan kesalahan ketika upaya dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera belajar cara menanganinya dalam program Python.
Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam berbagai jenis, dan jenisnya dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameErrordan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama dari pengecualian bawaan yang terjadi.
