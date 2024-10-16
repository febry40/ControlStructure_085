#pendefinisian fungsi
def fibonacci_series(n):
    fib_sequence = []  
    a, b = 0, 1  
    while a <= n:  
        fib_sequence.append(a)  
        a, b = b, a + b
    return fib_sequence  

#pengambilan input dari pengguna serta konversi tipe data
n = int(input("Masukkan nilai n untuk deret Fibonacci: "))

#pemanggilan fungsi dan penyimpanan hasil
fibonacci_result = fibonacci_series(n)

#output dari program
print(f"Deret Fibonacci hingga {n}: {fibonacci_result}")

#output untuk mencetak jumlah elemen dalam deret Fibonacci
print(f"Total angka dalam deret Fibonacci hingga {n}: {len(fibonacci_result)}")