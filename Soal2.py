def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        laragest = num2
    else:
        largest = num3
    return largest 

number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))
number3 = int(input("Masukkan angka ketiga: "))
largest = find_largest(number1, number2, number3)
print("Angka terbesar adalah:", largest)