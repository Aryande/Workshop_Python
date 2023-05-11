Input and Output : Ada beberapa cara untuk mempresentasikan output dari suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang.
Fancier Output Formatting : Sejauh ini kita menemukan dua cara penulisan nilai: pernyataan ekspresi dan print()fungsi. (Cara ketiga menggunakan write()metode objek file; file keluaran standar dapat dirujuk sebagai sys.stdout.

Untuk menggunakan string literal yang diformat, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, dapat menulis ekspresi Python antara karakter { dan } yang dapat merujuk ke variabel atau nilai literal.

Metode string str.format(). Menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arah pemformatan secara terperinci, tetapi juga harus memberikan informasi yang akan diformat.

Dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan untuk membuat tata letak. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu.

Fungsi str() digunakan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr() digunakan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str() akan mengembalikan nilai yang sama dengan repr().

Literal string yang diformat (f-string) memungkinkan untuk memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {expression}. Penggunaan dasar metode str.format() Tanda kurung dan karakter di dalamnya (sebut format bidang) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang diteruskan ke metode str.format().

