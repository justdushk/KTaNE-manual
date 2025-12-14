def memory_module():
    """Модуль памяти"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: ПАМЯТЬ")
    print("=" * 50)
    print("\nЭтот модуль запоминает ваши действия на каждом этапе.")
    print("Позиции кнопок: 1 (левая) - 2 - 3 - 4 (правая)")
    print("\nВведите 'выход' на любом этапе для возврата в меню")
    
    # Хранилище данных о нажатиях
    history = {}  # {stage: {'position': X, 'value': Y}}
    
    for stage in range(1, 6):
        print(f"\n{'=' * 50}")
        print(f"ЭТАП {stage}")
        print("=" * 50)
        
        # Читаем значение на экране
        while True:
            try:
                display_input = input(f"\nЦифра на экране: ").strip()
                if display_input.lower() == 'выход':
                    input("\nНажмите Enter для возврата в меню...")
                    return
                display = int(display_input)
                if 1 <= display <= 4:
                    break
                print("Должно быть от 1 до 4!")
            except ValueError:
                print("Введите число!")
        
        position = None
        value = None
        
        # Логика для каждого этапа
        if stage == 1:
            if display == 1:
                position = 2
            elif display == 2:
                position = 2
            elif display == 3:
                position = 3
            elif display == 4:
                position = 4
            
            print(f"\n→ Нажмите кнопку на позиции {position}")
            
            while True:
                try:
                    value = int(input(f"Какая цифра на кнопке {position}? "))
                    if 1 <= value <= 4:
                        break
                    print("Должно быть от 1 до 4!")
                except ValueError:
                    print("Введите число!")
        
        elif stage == 2:
            if display == 1:
                print("\n→ Нажмите кнопку со значением 4")
                while True:
                    try:
                        position = int(input("На какой позиции кнопка со значением 4? "))
                        if 1 <= position <= 4:
                            value = 4
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 2 or display == 4:
                position = history[1]['position']
                print(f"\n→ Нажмите кнопку на позиции {position} (как на этапе 1)")
                while True:
                    try:
                        value = int(input(f"Какая цифра на кнопке {position}? "))
                        if 1 <= value <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 3:
                position = 1
                print(f"\n→ Нажмите кнопку на позиции {position}")
                while True:
                    try:
                        value = int(input(f"Какая цифра на кнопке {position}? "))
                        if 1 <= value <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
        
        elif stage == 3:
            if display == 1:
                value = history[2]['value']
                print(f"\n→ Нажмите кнопку со значением {value} (как на этапе 2)")
                while True:
                    try:
                        position = int(input(f"На какой позиции кнопка со значением {value}? "))
                        if 1 <= position <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 2:
                value = history[1]['value']
                print(f"\n→ Нажмите кнопку со значением {value} (как на этапе 1)")
                while True:
                    try:
                        position = int(input(f"На какой позиции кнопка со значением {value}? "))
                        if 1 <= position <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 3:
                position = 3
                print(f"\n→ Нажмите кнопку на позиции {position}")
                while True:
                    try:
                        value = int(input(f"Какая цифра на кнопке {position}? "))
                        if 1 <= value <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 4:
                print("\n→ Нажмите кнопку со значением 4")
                while True:
                    try:
                        position = int(input("На какой позиции кнопка со значением 4? "))
                        if 1 <= position <= 4:
                            value = 4
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
        
        elif stage == 4:
            if display == 1:
                position = history[1]['position']
                print(f"\n→ Нажмите кнопку на позиции {position} (как на этапе 1)")
                while True:
                    try:
                        value = int(input(f"Какая цифра на кнопке {position}? "))
                        if 1 <= value <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 2:
                position = 1
                print(f"\n→ Нажмите кнопку на позиции {position}")
                while True:
                    try:
                        value = int(input(f"Какая цифра на кнопке {position}? "))
                        if 1 <= value <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
            elif display == 3 or display == 4:
                position = history[2]['position']
                print(f"\n→ Нажмите кнопку на позиции {position} (как на этапе 2)")
                while True:
                    try:
                        value = int(input(f"Какая цифра на кнопке {position}? "))
                        if 1 <= value <= 4:
                            break
                        print("Должно быть от 1 до 4!")
                    except ValueError:
                        print("Введите число!")
        
        elif stage == 5:
            if display == 1:
                value = history[1]['value']
                print(f"\n→ Нажмите кнопку со значением {value} (как на этапе 1)")
            elif display == 2:
                value = history[2]['value']
                print(f"\n→ Нажмите кнопку со значением {value} (как на этапе 2)")
            elif display == 3:
                value = history[4]['value']
                print(f"\n→ Нажмите кнопку со значением {value} (как на этапе 4)")
            elif display == 4:
                value = history[3]['value']
                print(f"\n→ Нажмите кнопку со значением {value} (как на этапе 3)")
            
            while True:
                try:
                    position = int(input(f"На какой позиции кнопка со значением {value}? "))
                    if 1 <= position <= 4:
                        break
                    print("Должно быть от 1 до 4!")
                except ValueError:
                    print("Введите число!")
        
        # Сохраняем данные этапа
        history[stage] = {'position': position, 'value': value}
        print(f"\n✓ Этап {stage} завершен: позиция {position}, значение {value}")
    
    print("\n" + "=" * 50)
    print("МОДУЛЬ ОБЕЗВРЕЖЕН!")
    print("=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")