#menerima input n yang menentukan jumlah baris pada pola
def print_pattern(n):
    """Mencetak pola angka seperti yang diminta."""
    for i in range(1, n+1): #membuat sebuah perulangan
        print(str(i)*i) #mengkonversi angka i menjadi string dan mengulanginya sebanyak i kali

n = int(input("Masukkan nilai: ")) #memasukkan nilai
print_pattern(n) #Memanggil fungsi print_pattern dengan nilai n yang telah diperoleh dari input 

