#menerima nilai persentase sebagai input dan mengembalikan string yang sesuai dengan kategori kinerja
def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Below average performance"
#if-elif-else digunakan untuk memeriksa rentang nilai persentase dan menentukan kategori

percentage = float(input("Masukkan nilai n untuk melihat performa dari siswa tersebut: "))
#percentage menyimpan nilai hasil konversi input pengguna dari string ke float
#float digunakan untuk mengonversi nilai yang dimasukkan pengguna dari tipe string menjadi float

print(evaluate_performance(percentage))
#menampilkan hasil performa siswa berdasarkan nilai yang diberikan

