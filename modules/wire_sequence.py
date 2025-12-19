def wire_sequence_module():
    """Модуль последовательностей проводов"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: ПОСЛЕДОВАТЕЛЬНОСТИ ПРОВОДОВ")
    print("=" * 50)
    
    # Таблицы решений
    red_table = {
        1: ['В'], 2: ['Б'], 3: ['А'], 4: ['А', 'В'],
        5: ['Б'], 6: ['А', 'В'], 7: ['А', 'Б', 'В'],
        8: ['А', 'Б'], 9: ['Б']
    }
    
    blue_table = {
        1: ['Б'], 2: ['А', 'В'], 3: ['Б'], 4: ['А'],
        5: ['Б'], 6: ['Б', 'В'], 7: ['В'],
        8: ['А', 'В'], 9: ['А']
    }
    
    black_table = {
        1: ['А', 'Б', 'В'], 2: ['А', 'В'], 3: ['Б'], 4: ['А', 'В'],
        5: ['Б'], 6: ['Б', 'В'], 7: ['А', 'Б'],
        8: ['В'], 9: ['В']
    }
    
    # Счетчики проводов каждого цвета
    counters = {'красный': 0, 'синий': 0, 'черный': 0}
    history = []  # История проводов для отмены
    
    print("\nВводите провода по порядку.")
    print("Формат: 'цвет буква' (например, 'красный А')")
    print("Доступные цвета: красный(кр), синий(с), черный(ч)")
    print("Доступные буквы: А, Б, В")
    print("\nКоманды:")
    print("  'панель' - следующая панель")
    print("  'назад' - отменить последний провод")
    print("  'выход' - вернуться в меню\n")
    
    panel_num = 1
    print(f"ПАНЕЛЬ {panel_num}")
    print("-" * 50)
    
    while True:
        wire_input = input("\nПровод: ").strip().lower()
        
        if wire_input == 'выход':
            break
        elif wire_input == 'назад':
            if history:
                last = history.pop()
                counters[last['color']] -= 1
                print(f"✓ Отменен: {last['color']} #{last['occurrence']} → {last['letter']}")
            else:
                print("История пуста, нечего отменять!")
            continue
        elif wire_input == 'панель':
            panel_num += 1
            print(f"\n{'=' * 50}")
            print(f"ПАНЕЛЬ {panel_num}")
            print("-" * 50)
            continue
        
        # Парсим ввод
        parts = wire_input.split()
        if len(parts) != 2:
            print("Неверный формат! Используйте: 'цвет буква'")
            continue
        
        color, letter = parts[0], parts[1].upper()
        
        if color not in ['кр', 'с', 'ч']:
            print("Неверный цвет! Используйте: красный(кр), синий(с), черный(ч)")
            continue
        
        if letter not in ['А', 'Б', 'В']:
            print("Неверная буква! Используйте: А, Б, В")
            continue
        
        # Увеличиваем счетчик этого цвета
        counters[color] += 1
        occurrence = counters[color]
        
        # Определяем, резать ли
        cut = False
        if color == 'красный':
            cut = letter in red_table.get(occurrence, [])
        elif color == 'синий':
            cut = letter in blue_table.get(occurrence, [])
        elif color == 'черный':
            cut = letter in black_table.get(occurrence, [])
        
        result = "РЕЖЬТЕ" if cut else "НЕ РЕЖЬТЕ"
        print(f"  {color.capitalize()} #{occurrence} → {letter} → {result}")
        
        # Сохраняем в историю
        history.append({
            'color': color,
            'letter': letter,
            'occurrence': occurrence,
            'cut': cut
        })
    
    print("\n" + "=" * 50)
    print(f"Всего проводов обработано:")
    print(f"  Красных: {counters['красный']}")
    print(f"  Синих: {counters['синий']}")
    print(f"  Черных: {counters['черный']}")
    print("=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")