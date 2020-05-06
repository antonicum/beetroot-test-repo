import random
import datetime
from datetime import timedelta

name = (input("Привет! Давай познакомимся. Как тебя зовут? \nВведи, пожалуйста, своё имя сюда: ").capitalize())
print('\nОчень приятно, ', name, '. Меня зовут Калькулятор. Давай посчитаем что-то.')
print("""
      Для начала тебе следует выбрать одну из следующих операций:
      Сложение
      Вычитание
      Умножение
      Деление
      Целочисленное деление
      Степень числа
      Остаток от деления
      Факториал
      Революционер
      Сколько дней прожито
      Дата и время смерти""")
print("Выбрал?")
while True:
    operation = (input("Напиши 0, чтобы завершить работу Калькулятора или напиши операцию, которую будем производить, сюда: ").lower().strip())
    if operation == "0": 
        print(f'Рад был тебя видеть, {name}!') 
        break 
    if operation in ("сложение", "вычитание", "умножение", "деление", "целочисленное деление", "остаток от деления"):
        result = None
        while result == None:
            num1 = (input("Введи первое число: ")) 
            num1_bez_tochki = num1.replace(".", "", 1)
            if num1_bez_tochki.isdigit() == False:
                print("Пожалуйста, я же калькулятор и воспринимаю только цифры: ")
            else:
                num1_part = num1.split('.')
                if len(num1_part) == 2 and num1_part[0].isdigit() and num1_part[1].isdigit():
                    num1 = float(num1)
                else:                     
                    num1 = float(num1)    
                while result == None:
                    num2 = (input("Введи второе число: "))
                    num2_bez_tochki = num2.replace(".", "", 1)
                    if num2_bez_tochki.isdigit() == False:
                        print("Пожалуйста, я же калькулятор, напиши цифрами: ") 
                    else:
                        num2_part = num2.split('.')
                        if len(num2_part) == 2 and num2_part[0].isdigit() and num2_part[1].isdigit():
                            num2 = float(num2)      
                        else:                       
                            num2 = float(num2)      
                        
                        if operation == "сложение":
                            print((f'{num1}').rstrip('0').rstrip('.'),(f'+ {num2}').rstrip('0').rstrip('.'),(f'= {num1 + num2}').rstrip('0').rstrip('.'))
                            result = (f'{num1 + num2}') 
                        
                        elif operation == "вычитание":
                            print((f'{num1}').rstrip('0').rstrip('.'),(f'- {num2}').rstrip('0').rstrip('.'),(f'= {num1 - num2}').rstrip('0').rstrip('.'))
                            result = (f'{num1 - num2}')
                            
                        elif operation == "умножение":
                            print((f'{num1}').rstrip('0').rstrip('.'),(f'* {num2}').rstrip('0').rstrip('.'),(f'= {num1 * num2}').rstrip('0').rstrip('.'))
                            result = (f'{num1 * num2}')
                            
                        elif operation == "деление":
                            if num2 != 0:
                                print((f'{num1}').rstrip('0').rstrip('.'),(f'/ {num2}').rstrip('0').rstrip('.'),(f'= {num1 / num2}').rstrip('0').rstrip('.'))
                                result = (f'{num1 / num2}') 
                            else:
                                print("На ноль не делим!")
                                
                        elif operation == "целочисленное деление":
                            print((f'{num1}').rstrip('0').rstrip('.'),(f'// {num2}').rstrip('0').rstrip('.'),(f'= {num1 // num2}').rstrip('0').rstrip('.'))
                            result = (f'{num1 // num2}')
    
                        elif operation == "остаток от деления":
                            print((f'{num1}').rstrip('0').rstrip('.'),(f'% {num2}').rstrip('0').rstrip('.'),(f'= {num1 % num2}').rstrip('0').rstrip('.'))
                            result = (f'{num1 % num2}')
                           
    elif operation == ("степень числа").lower().strip():
        result = None
        while result == None:
            num1 = input("Введи число, которое будем возводить в степень: ")
            num1_bez_tochki = num1.replace(".", "", 1)
            if num1_bez_tochki.isdigit() == False:
                print("Пожалуйста, я же калькулятор, напиши цифрами: ")
            else:
                num1_part = num1.split(".")
                if len(num1_part) == 2 and num1_part[0].isdigit() and num1_part[1].isdigit():
                    num1 = float(num1)
                else:
                    num1 = float(num1)
                result = None
                while result == None:         
                    num2 = input("Введи число, собственно, степени:")
                    num2_bez_tochki = num2.replace(".", "", 1)
                    if num2_bez_tochki.isdigit() == False:
                        print("Пожалуйста, я же калькулятор, напиши цифрами: ")
                    else:
                        num2_part = num2.split(".")
                        if len(num2_part) == 2 and num2_part[0].isdigit() and num2_part[1].isdigit():
                            num2 = float(num2)
                        else:
                            num2 = float(num2)
                        print((f'{num1}').rstrip('0').rstrip('.'),(f'** {num2}').rstrip('0').rstrip('.'),(f'= {num1 ** num2}').rstrip('0').rstrip('.'))
                        result = (f'{num1 ** num2}')
                    
    elif operation == ("революционер").lower().strip():
            print(f'{name},ты революционер на ', random.randrange(0, 100),"%.")
            
    elif operation == ("факториал").lower().strip():
        result = None
        while result == None:
            num = input(f'Здесь уже всё проще, {name}. Введи число, факториал которого хочешь увидеть: ')
            num_bez_tochki = num.replace(".", "", 1)
            if num_bez_tochki.isdigit() == False:
                print("Не забывай, что я калькулятор и могу считать только числа: ")
            else:
                num_part = num.split(".")
                if len(num_part) == 2 and num_part[0].isdigit() and num[1].isdigit():
                    num1 = float(num)
                else:
                    num1 = float(num)
                factorial = 1
                while num1 > 1:
                    factorial *= num1
                    num1 -= 1
                print((f'\nФакториал числа {num}').rstrip('0').rstrip('.'),(f' =  {factorial}').rstrip('0').rstrip('.'))
                result = factorial
                
    elif operation == ("дата и время смерти").lower().strip():
        
        min_year=datetime.now().year
        max_year=(min_year + 111)
        
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year+1
        end = start + timedelta(days=365 * years)
        for i in range(1):
            random_date = start + (end - start) * random.random()
            print(random_date)
            left = (f'В таком случае тебе осталось {(random_date - start)/365} years').replace("days", "лет/года").replace(",",".")
            print(left[:-22])
            
    elif operation == ("сколько дней прожито").lower().strip():
        a = input('Дата рождения(гггг-мм-дд): ')
        a = a.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        bb = datetime.date.today()
        cc = aa-bb
        dd = str(cc)
        print("Ты прожил",(dd.split()[0]).replace("-", ""),"дней.")
        
    elif operation not in ("Дата и время смерти","случайное число", "степень числа", "сложение", "вычитание", "умножение", "деление", "целочисленное деление", "остаток от деления"):
        print("\nТаких операций я не знаю :(")
        
    