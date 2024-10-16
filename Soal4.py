#Menerima input n yang menentukan batas atas bilangan ganjil yang akan dicetak
def print_odd_number(n):
    """Mencetak bilangan ganjil dari 1 hingga n."""
    for i in range(1, n+1, 2): #melakukan perulangan dengan langkah 2
        print(i, end=" ") #mencetak setiap bilangan ganjil 

n = int(input("Masukkan nilai n untuk bilangan ganjil: ")) #meminta input, mengubah tipe data, dan menyimpan nilai
print_odd_number(n) #mencetak bilangan ganjil dari 1 hingga n
