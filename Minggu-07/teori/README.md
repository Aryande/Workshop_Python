Kelas menyediakan sarana bundling data dan fungsionalitas bersama. Membuat kelas baru akan membuat tipe objek baru, yang memungkinkan instance baru dari tipe tersebut dibuat. Setiap instance kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi statusnya.

Objek memiliki individualitas, dan banyak nama (dalam berbagai cakupan) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama di Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel).

Namespace adalah pemetaan dari nama ke objek . Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang.

Perhatikan bagaimana penugasan lokal (yang merupakan default) tidak mengubah pengikatan spam scope_test . Penugasan mengubah pengikatan spam scope_test , dan penugasan mengubah pengikatan tingkat modul.nonlocalglobal

definisi fungsi ( defpernyataan) harus dieksekusi sebelum memiliki efek apa pun. (Anda dapat menempatkan definisi kelas di cabang pernyataan if, atau di dalam fungsi.)

nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat.Operasi instantiasi ("memanggil" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu kelas dapat mendefinisikan metode khusus bernama __init__()

Objek kelas mendukung dua jenis operasi: referensi atribut dan instansiasi. Attribute references menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat. Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data, dan metode.

Python memiliki dua fungsi bawaan yang bekerja dengan warisan: 1.Gunakan isinstance() untuk memeriksa jenis instance: isinstance(obj, int) akan menjadi True hanya jika obj.class adalah int atau beberapa kelas yang diturunkan dari int. 2. Gunakan issubclass() untuk memeriksa warisan kelas: issubclass(bool, int)adalah True karena bool adalah subkelas dari int. Namun, issubclass(float, int) adalah False karena float bukan subkelas dari int.
