def wires_module():
    """Модуль проводов"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: ПРОВОДА")
    print("=" * 50)
    
    # Количество проводов
    while True:
        try:
            count = int(input("\nСколько проводов (3-6)? "))
            if 3 <= count <= 6:
                break
            print("Неверное количество! Должно быть от 3 до 6.")
        except ValueError:
            print("Введите число!")
    
    # Ввод цветов проводов
    colors = []
    print(f"\nВведите цвет каждого провода (сверху вниз):")
    print("Доступные цвета: красный, синий, желтый, белый, черный")
    
    for i in range(count):
        while True:
            color = input(f"Провод {i+1}: ").strip().lower()
            if color in ['красный', 'синий', 'желтый', 'белый', 'черный']:
                colors.append(color)
                break
            print("Неверный цвет! Используйте: красный, синий, желтый, белый, черный")
    
    # Подсчет цветов
    red_count = colors.count('красный')
    blue_count = colors.count('синий')
    yellow_count = colors.count('желтый')
    white_count = colors.count('белый')
    black_count = colors.count('черный')
    
    result = None
    
    # Логика для 3 проводов
    if count == 3:
        if red_count == 0:
            result = 2
        elif colors[-1] == 'белый':
            result = count
        elif blue_count > 1:
            # Последний синий
            for i in range(len(colors) - 1, -1, -1):
                if colors[i] == 'синий':
                    result = i + 1
                    break
        else:
            result = count
    
    # Логика для 4 проводов
    elif count == 4:
        serial_needed = False
        if red_count > 1:
            serial = input("\nПоследняя цифра серийного номера нечетная? (да/нет): ").strip().lower()
            if serial == 'да':
                # Последний красный
                for i in range(len(colors) - 1, -1, -1):
                    if colors[i] == 'красный':
                        result = i + 1
                        break
            else:
                serial_needed = True
        
        if result is None:
            if colors[-1] == 'желтый' and red_count == 0:
                result = 1
            elif blue_count == 1:
                result = 1
            elif yellow_count > 1:
                result = count
            else:
                result = 2
    
    # Логика для 5 проводов
    elif count == 5:
        if colors[-1] == 'черный':
            serial = input("\nПоследняя цифра серийного номера нечетная? (да/нет): ").strip().lower()
            if serial == 'да':
                result = 4
        
        if result is None:
            if red_count == 1 and yellow_count > 1:
                result = 1
            elif black_count == 0:
                result = 2
            else:
                result = 1
    
    # Логика для 6 проводов
    elif count == 6:
        if yellow_count == 0:
            serial = input("\nПоследняя цифра серийного номера нечетная? (да/нет): ").strip().lower()
            if serial == 'да':
                result = 3
        
        if result is None:
            if yellow_count == 1 and white_count > 1:
                result = 4
            elif red_count == 0:
                result = count
            else:
                result = 4
    
    print(f"\n{'=' * 50}")
    print(f"РЕЖЬТЕ ПРОВОД № {result}")
    print(f"{'=' * 50}")
    
    input("\nНажмите Enter для возврата в меню...")