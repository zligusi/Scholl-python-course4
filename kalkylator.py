# The cod is a mini kalkylator 

want = input("Что делаем ? (+ , - ,  * ,  : )")

while True :
    try :
        a = int(input("Введите первое число : "))
        b = int(input("Введите второе число : "))
        
        if want == "+" :
            c = a + b 
        elif want == "-" :
            c = a - b 
        elif want == "*" :
            c = a * b
        elif want == ":" :
            c = a / b
        else :
            print("Вы ввели не правильный знак операции ")
        break
    except ValueError :
        print("Вы ввели не число ")
print(f"Результат : {c}")