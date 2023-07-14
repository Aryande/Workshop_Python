from flask import Flask, render_template
app = Flask(__name__)

konten = [
    {
        'penulis': 'Ariyanto Dendo',
        'judul': 'Postingan Pertama',
        'sinopsis': 'Ini adalah postingan pertama',
        'isi': 'Ini adalah Responsi Python',
        'tanggal': '14 juli 2023',
        'jam': '16.00'
    },
    {
        'penulis': 'Aryan',
        'judul': ' Flask',
        'sinopsis': 'Ini adalah Responsi flask',
        'isi': 'Ini adalah isi dari Responsi flask',
        'tanggal': '14 juli 2023',
        'jam': '18.00'
    }
]

@app.route('/')
def home():
    return render_template('home.html', konten=konten, judul='Beranda')

@app.route('/tentang/')
def tentang():
    return render_template('tentang.html', judul='Tentang')


if __name__ == '__main__':
    app.run(debug=True)
