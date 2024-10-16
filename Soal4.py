def print_odd_number(n):
    """Mencetak bilangan ganjil dari 1 hingga n."""
    for i in range(1, n+1, 2):
        print(i, end=" ")

n = int(input("Masukkan nilai n untuk bilangan ganjil: "))
print_odd_number(n)
