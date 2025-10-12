print("          ПОБЕГ ИЗ ТЮРЬМЫ")
print()

print("Вы - известный археолог, отправившийся в горы")
print("Там вы нашли стремный амулет валяющийся на дороге.")
print()

print("Сегодня к вам в лабораторию приходит подозрительный незнакомец.")
print("Он предлагает вам продать амулет за огромную сумму денеги.")

choice1 = input("Что вы сделаете? (1 - продать амулет, 2 - отказаться, 3 - спросить подробности): ")

if choice1 == "1":
    print("Вы соглашаетесь на сделку. Незнакомец улыбается и достает пистолет.")
    print("'Жаль, что вы выбрали этот путь', - говорит он и стреляет в вас.")
elif choice1 == "2":
    print("Вы отказываетесь продавать амулет. Незнакомец злобно смеется.")
    print("'Тогда вы мне не нужны', - говорит он и нажимает кнопку на пульте.")
    print("Комната наполняется газом, и вы теряете сознание.")
else:
    print("Вы пытаетесь выяснить, зачем ему амулет.")
    print("Незнакомец нервничает и неожиданно нападает на вас.")
    print("В борьбе вы падаете и ударяетесь головой о стол.")

print()
print("...")
print("Вы приходите в сознание в холодной каменной камере.")
print("На вас надеты наручники, амулет пропал.")
print()
print("   ТЮРЕМНАЯ КАМЕРА")
print()
print("Вы осматриваете камеру. Она небольшая, с каменными стенами.")
print("В углу стоит кровать, рядом - стол и стул.")
print("На столе вы замечаете странные символы.")
print()


print("На столе вырезана числовая последовательность:")
print("2, 4, 8, 16, ?")
print("Какое число должно быть следующим?")

puzzle1 = False
attempts1 = 0

while not puzzle1 and attempts1 < 3:
    answer1 = input("Ваш ответ: ")
    
    if answer1 == "32":
        print("Правильно! Последовательность удваивается каждый раз.")
        print("Из-под стола выпадает маленький ключ.")
        puzzle1 = True
    else:
        attempts1 += 1
        if attempts1 < 3:
            print("Неправильно. Попробуйте еще раз.")
        else:
            print("Вы исчерпали все попытки. К счастью, ключ все равно выпадает, но вы поранились.")

print()
print("Вы подбираете ключ. Он подходит к наручникам!")
print("Теперь вы свободны и можете исследовать камеру дальше.")
print()


print("Осмотрев камеру, вы находите скрытую дверь за кроватью.")
print("На двери висит замок с кодовой панелью.")
print("Рядом на стене висит табличка с загадкой:")
print()

print("Какая птица из яйца родится, а яйца не несет?")
print("'что это?'")

puzzle2 = False
attempts2 = 0

while not puzzle2 and attempts2 < 3:
    answer2 = input("Ваш ответ: ").lower()
    
    if answer2 == "Петух" or answer2 == "petux":
        print("Правильно! Замок открывается с щелчком.")
        puzzle2 = True
    else:
        attempts2 += 1
        if attempts2 < 3:
            print("Неправильно. Подумайте еще.")
        else:
            print("Вы не смогли разгадать загадку, но замок старый и поддается силовому воздействию.")
            print("С большим усилием вы ломаете замок.")
            puzzle2 = True

print()
print("Дверь открывается, и вы попадаете в темный коридор.")
print()

print("   ТЕМНЫЙ КОРИДОР")
print()

print("Перед вами развилка. Коридор разветвляется на три направления.")
print("Справа доносится шум воды, слева - тишина, прямо - слабый свет.")

direction_choice = input("Куда пойдете? (1 - направо, 2 - налево, 3 - прямо): ")

if direction_choice == "1":
    print("Вы идете направо и находите комнату с водопроводом.")
    print("К сожалению, комната заканчивается тупиком. Приходится вернуться.")
    print()
    direction_choice = input("Теперь куда? (2 - налево, 3 - прямо): ")
    
if direction_choice == "2":
    print("Вы идете налево и попадаете в склад.")
    print("Здесь полно старых вещей, но выхода нет.")
    print("Находя металлический прут, вы берете его с собой.")
    has_weapon = True
    print()
    direction_choice = "3"  

if direction_choice == "3":
    print("Вы идете прямо на свет и попадаете в большое помещение.")
    print("Это похоже на главный зал тюрьмы.")
else:
    print("Вы блуждаете по коридорам и в итоге находите главный зал.")

print()
print("В зале вас ждет стражник - финальный босс.")
print()
print("   ФИНАЛЬНАЯ БИТВА")
print()

print("Страшный стражник с мечом стоит между вами и выходом.")
print("'Никто не уходит отсюда живым!' - кричит он.")

player_health = 100
boss_health = 100
round_count = 0

print(f"Ваше здоровье: {player_health}")
print(f"Здоровье стража: {boss_health}")
print()

while player_health > 0 and boss_health > 0:
    round_count += 1
    print(f"--- Раунд {round_count} ---")
    
    print("Ваши действия:")
    print("1 - Атаковать")
    print("2 - Защищаться")
    print("3 - Использовать предмет (если есть)")
    
    action = input("Выберите действие (1-3): ")
    
    import random
    boss_action = random.randint(1, 3)
    
    if action == "1":  
        if boss_action == 1:  
            damage_to_boss = random.randint(15, 25)
            damage_to_player = random.randint(10, 20)
            boss_health -= damage_to_boss
            player_health -= damage_to_player
            print(f"Вы атакуете и наносите {damage_to_boss} урона!")
            print(f"Стражник атакует одновременно и наносит {damage_to_player} урона!")
        elif boss_action == 2:  
            damage_to_boss = random.randint(5, 15)
            boss_health -= damage_to_boss
            print(f"Вы атакуете, но стражник защищается. Вы наносите {damage_to_boss} урона!")
        else:  
            damage_to_boss = random.randint(20, 30)
            boss_health -= damage_to_boss
            print(f"Вы атакуете, пока стражник готовит заклинание! Вы наносите {damage_to_boss} урона!")
    
    elif action == "2":  
        if boss_action == 1:  
            damage_to_player = random.randint(5, 10)
            player_health -= damage_to_player
            print(f"Вы защищаетесь! Стражник атакует и наносит всего {damage_to_player} урона!")
        elif boss_action == 2:  
            print("Оба защищаются. Ничего не происходит.")
        else:  
            print("Вы защищаетесь, но стражник использует магию и обходит вашу защиту!")
            damage_to_player = random.randint(15, 25)
            player_health -= damage_to_player
            print(f"Вы получаете {damage_to_player} урона!")
    
    elif action == "3":  
        if 'weapon' in locals() and weapon: 
            damage_to_boss = random.randint(25, 40)
            boss_health -= damage_to_boss
            print(f"Вы используете металлический прут и наносите сокрушительный {damage_to_boss} урон!")
            weapon = False  
        else:
            print("У вас нет полезных предметов! Вы теряете ход.")
            if boss_action == 1:
                damage_to_player = random.randint(10, 20)
                player_health -= damage_to_player
                print(f"Стражник атакует и наносит {damage_to_player} урона!")
    
    else:  
        print("Неверная команда! Вы теряете ход.")
        if boss_action == 1:
            damage_to_player = random.randint(10, 20)
            player_health -= damage_to_player
            print(f"Стражник атакует и наносит {damage_to_player} урона!")
    if boss_health <= 0:
        boss_health = 0
        print("Вы победили стража!")
        break
    if player_health <= 0:
        player_health = 0
        print("Вы проиграли...")
        break
    
    print(f"Ваше здоровье: {player_health}")
    print(f"Здоровье стража: {boss_health}")
    print()

print()
print("             ФИНАЛ")
print()

if player_health > 0:
    print("Поздравляем! Вы победили стража и смогли выбраться из тюрьмы!")
    print("Перед вами открывается выход на свободу.")
    print("Солнце слепит глаза после долгого пребывания в темнице.")
    print()
    print("Но вы скорее всего задаетесь вопросом о том")
    print("Что это был за незнакомец и что за амулет...")
    interec = input("Так ведь? ").lower()
    if interec == "да":
            print("Извините автор не придумал, но на самом деле то...")
            print()
            print("Зачем оно тебе надо?")
            print()
            print("Ты только выбрался из темницы из-за какого-то подозрительного типа...")
            print()
            print("Рисковал своей жизнью и так далее, а теперь тебе интересно кто он ?")
            print("Иди домой")
    elif interec == "нет":
            print("Вот и правильно :D")
            print()
            print()
            print("Иди домой")
    else:
        print("Оно тебе не надо все...")
        print()
        print("Иди домой")
else:
    print("К сожалению, вы не смогли победить стража - вы неудачник или идиот...")
    print("Вас возвращают в камеру, и надежда на побег тает...")
    print()
    print("Но может быть, в следующий раз вам повезет больше?")

print()
print("Спасибо за игру!")