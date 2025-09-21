print("Привет! Я калькулятор")
print("Можно использовать: + - * / // % **")
print("== != > < >= <=")
print("and or not")
print("& | ^ ~ << >>")
print("Напиши 'стоп' чтобы выйти")

while True:
    vvod = input("Введи пример: ")
    
    if vvod == "стоп":
        print("Пока!")
        break
    
    chasti = vvod.split()
    
    if len(chasti) == 2:
        deistvie = chasti[0]
        chislo = int(chasti[1])
        
        if deistvie == "~":
            otvet = ~chislo
            print("Ответ:", otvet)
        elif deistvie == "not":
            otvet = not chislo
            print("Ответ:", otvet)
        else:
            print("Не понимаю такой пример")
        continue
    
    if len(chasti) != 3:
        print("Пиши так: число действие число")
        continue
    
    try:
        chislo1 = float(chasti[0])
        deistvie = chasti[1]
        chislo2 = float(chasti[2])
    except:
        print("Используй только цифры!")
        continue
    
    otvet = None
    
    if deistvie == "+":
        otvet = chislo1 + chislo2
    elif deistvie == "-":
        otvet = chislo1 - chislo2
    elif deistvie == "*":
        otvet = chislo1 * chislo2
    elif deistvie == "/":
        if chislo2 == 0:
            print("На ноль делить нельзя!")
            continue
        otvet = chislo1 / chislo2
    elif deistvie == "//":
        if chislo2 == 0:
            print("На ноль делить нельзя!")
            continue
        otvet = chislo1 // chislo2
    elif deistvie == "%":
        if chislo2 == 0:
            print("На ноль делить нельзя!")
            continue
        otvet = chislo1 % chislo2
    elif deistvie == "**":
        otvet = chislo1 ** chislo2
    
    elif deistvie == "==":
        otvet = chislo1 == chislo2
    elif deistvie == "!=":
        otvet = chislo1 != chislo2
    elif deistvie == ">":
        otvet = chislo1 > chislo2
    elif deistvie == "<":
        otvet = chislo1 < chislo2
    elif deistvie == ">=":
        otvet = chislo1 >= chislo2
    elif deistvie == "<=":
        otvet = chislo1 <= chislo2
    
    elif deistvie == "and":
        otvet = bool(chislo1) and bool(chislo2)
    elif deistvie == "or":
        otvet = bool(chislo1) or bool(chislo2)
    
    elif deistvie == "&":
        otvet = int(chislo1) & int(chislo2)
    elif deistvie == "|":
        otvet = int(chislo1) | int(chislo2)
    elif deistvie == "^":
        otvet = int(chislo1) ^ int(chislo2)
    elif deistvie == "<<":
        otvet = int(chislo1) << int(chislo2)
    elif deistvie == ">>":
        otvet = int(chislo1) >> int(chislo2)
    
    else:
        print("Не знаю такое действие")
        continue
    
    print("Ответ:", otvet)