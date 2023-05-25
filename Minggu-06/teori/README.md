8. Errors and Exceptions
Sampai saat ini pesan kesalahan belum banyak disebutkan,Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaks dan pengecualian .
8.1. Syntax Errors
Kesalahan sintaksis, juga dikenal sebagai kesalahan parsing, mungkin merupakan jenis keluhan paling umum. Parser mengulangi baris yang menyinggung dan menampilkan 'panah' kecil yang menunjuk ke titik paling awal di baris tempat kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token yang mendahului tanda panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua ( ':') tidak ada sebelumnya. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari jika input berasal dari skrip.
8.2. Exceptions
ekspresi benar secara sintaksis, itu dapat menyebabkan kesalahan ketika upaya dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera belajar cara menanganinya dalam program Python.
Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam berbagai jenis, dan jenisnya dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameErrordan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama dari pengecualian bawaan yang terjadi.
8.3. Handling Exceptions
Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih.
Pernyataan tersebut tryberfungsi sebagai berikut.
•	Jika tidak ada pengecualian yang terjadi, kecuali klausa dilewati dan eksekusi pernyataan tryselesai.
•	Jika pengecualian terjadi selama eksekusi klausa try, klausa lainnya akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai menurut exceptkata kunci, klausa kecuali dieksekusi, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali.
•	Jika pengecualian terjadi yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali , itu diteruskan ke trypernyataan luar; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.
Kelas dalam exceptklausa kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar daripadanya (tetapi bukan sebaliknya — klausa pengecualian yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar).
BaseExceptionadalah kelas dasar umum dari semua pengecualian. Salah satu subkelasnya, Exception, adalah kelas dasar dari semua pengecualian non-fatal.
8.4. Raising Exceptions
Pernyataan itu raisememungkinkan pemrogram untuk memaksa pengecualian tertentu terjadi.
Satu-satunya argumen untuk raisemenunjukkan pengecualian yang akan diajukan. Ini harus berupa instance pengecualian atau kelas pengecualian (kelas yang berasal dari BaseException, seperti Exceptionatau salah satu subkelasnya).
8.5. Exception Chaining
Jika pengecualian yang tidak tertangani terjadi di dalam suatu exceptbagian, pengecualian yang ditangani akan dilampirkan padanya dan disertakan dalam pesan kesalahan.
8.6. User-defined Exceptions
Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian.
8.7. Defining Clean-up Actions
Poin-poin berikut membahas kasus yang lebih kompleks ketika pengecualian terjadi:
•	Jika pengecualian terjadi selama eksekusi klausa try , pengecualian dapat ditangani oleh except klausa. Jika pengecualian tidak ditangani oleh except klausa, pengecualian akan dimunculkan kembali setelah finally klausa dieksekusi.
•	Pengecualian bisa terjadi selama eksekusi except atau elseklausa. Sekali lagi, pengecualian dimunculkan kembali setelah finallyklausa dieksekusi.
•	Jika finallyklausa mengeksekusi break, continueatau returnpernyataan, pengecualian tidak dimunculkan kembali.
•	Jika trypernyataan mencapai break, continueatau returnpernyataan, finallyklausa akan dieksekusi tepat sebelum break, continueatau return eksekusi pernyataan.
•	Jika finallyklausa menyertakan return pernyataan, nilai yang dikembalikan akan menjadi nilai dari pernyataan finallyklausa return, bukan nilai dari pernyataan tryklausa return .

8.8. Predefined Clean-up Actions
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan saat objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. 
8.9. Raising and Handling Multiple Unrelated Exceptions
Builtin ExceptionGroupmembungkus daftar instance pengecualian sehingga dapat dimunculkan bersama. 
Dengan menggunakan except*alih-alih except, kita hanya dapat menangani pengecualian dalam grup yang cocok dengan tipe tertentu secara selektif.
8.10. Enriching Exceptions with Notes
Saat pengecualian dibuat untuk dimunculkan, biasanya diinisialisasi dengan informasi yang menjelaskan kesalahan yang terjadi. Ada kasus di mana berguna untuk menambahkan informasi setelah pengecualian tertangkap. Untuk tujuan ini, pengecualian memiliki metode add_note(note)yang menerima string dan menambahkannya ke daftar catatan pengecualian. Render traceback standar menyertakan semua catatan, sesuai urutan penambahannya, setelah pengecualian.
