def complicated_wires_module():
    """Модуль усложненных проводов"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: УСЛОЖНЕННЫЕ ПРОВОДА")
    print("=" * 50)
    
    # Спрашиваем серийный номер и порт заранее
    serial_even = input("\nПоследняя цифра серийного номера четная? (да/нет): ").strip().lower() == 'да'
    batteries = int(input("Количество элементов питания: "))
    has_parallel = input("Есть ли параллельный порт? (да/нет): ").strip().lower() == 'да'
    
    while True:
        try:
            count = int(input("\nСколько проводов в модуле? "))
            if count > 0:
                break
            print("Должно быть больше 0!")
        except ValueError:
            print("Введите число!")
    
    print("\n" + "=" * 50)
    print("АНАЛИЗ ПРОВОДОВ")
    print("=" * 50)
    print("\nДля каждого провода укажите его характеристики:")
    print("С - синий, К - красный, З - звёздочка, Л - светодиод")
    print("Порядок ввода: СКЗЛ (например: СЗЛ для синего со звёздочкой и светодиодом)")
    print("Для белого провода просто нажмите Enter")
    print("\nДля выхода на любом этапе введите 'выход'")
    print()
    
    # Правила по упрощённому руководству
    rules = {
        '': 'РЕЖЬТЕ',  # Белый провод
        'С': ('РЕЖЬТЕ', 'serial_even'),
        'К': ('РЕЖЬТЕ', 'serial_even'),
        'З': 'РЕЖЬТЕ',
        'Л': 'НЕ РЕЖЬТЕ',
        'СК': ('РЕЖЬТЕ', 'serial_even'),
        'СЗ': 'НЕ РЕЖЬТЕ',
        'СЛ': ('РЕЖЬТЕ', 'parallel'),
        'КЗ': 'РЕЖЬТЕ',
        'КЛ': ('РЕЖЬТЕ', 'batteries'),
        'ЗЛ': ('РЕЖЬТЕ', 'batteries'),
        'СКЗ': ('РЕЖЬТЕ', 'parallel'),
        'СКЛ': ('РЕЖЬТЕ', 'serial_even'),
        'СЗЛ': ('РЕЖЬТЕ', 'parallel'),
        'КЗЛ': ('РЕЖЬТЕ', 'batteries'),
        'СКЗЛ': 'НЕ РЕЖЬТЕ'
    }
    
    for i in range(count):
        print(f"\nПРОВОД {i+1}:")
        
        wire_code = input("  Введите код провода (СКЗЛ): ").strip().upper()
        
        if wire_code.lower() == 'выход':
            break
        
        # Проверяем корректность ввода
        valid_chars = set('СКЗЛ')
        if not all(c in valid_chars for c in wire_code):
            print("  ⚠ Неверный ввод! Используйте только С, К, З, Л")
            continue
        
        # Нормализуем порядок: СКЗЛ
        normalized = ''
        if 'С' in wire_code:
            normalized += 'С'
        if 'К' in wire_code:
            normalized += 'К'
        if 'З' in wire_code:
            normalized += 'З'
        if 'Л' in wire_code:
            normalized += 'Л'
        
        # Определяем действие
        if normalized in rules:
            rule = rules[normalized]
            
            if isinstance(rule, tuple):
                action, condition = rule
                if condition == 'serial_even':
                    result = action if serial_even else 'НЕ РЕЖЬТЕ'
                    condition_text = f" (последняя цифра серийного номера {'чётная' if serial_even else 'нечётная'})"
                elif condition == 'parallel':
                    result = action if has_parallel else 'НЕ РЕЖЬТЕ'
                    condition_text = f" (параллельный порт {'есть' if has_parallel else 'отсутствует'})"
                elif condition == 'batteries':
                    result = action if batteries >= 2 else 'НЕ РЕЖЬТЕ'
                    condition_text = f" (батареек: {batteries})"
                print(f"  → {result}{condition_text}")
            else:
                print(f"  → {rule}")
        else:
            print(f"  ⚠ Неизвестная комбинация: {normalized}")
    
    print("\n" + "=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")