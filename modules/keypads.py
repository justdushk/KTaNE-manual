def keypads_module():
    """Модуль клавиатур"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: КЛАВИАТУРЫ")
    print("=" * 50)
    
    # Столбцы символов по твоим названиям (по порядку сверху вниз)
    columns = [
        ['зеркало', 'ат', 'лямбда', 'вишенки', 'ю', 'гроб', 'обратка'],
        ['дрон', 'зеркало', 'обратка', 'хвостик', 'нзвезда', 'гроб', 'вопрос'],
        ['копирайт', 'запятая', 'хвостик', 'птицы', 'руз', 'лямбда', 'нзвезда'],
        ['анз', 'р', 'лайк', 'ю', 'птицы', 'вопрос', 'смайл'],
        ['трезубец', 'смайл', 'лайк', 'сточка', 'р', 'зхвост', 'ззвезда'],
        ['анз', 'дрон', 'пазл', 'ае', 'трезубец', 'краб', 'омега']
    ]
    
    # Показываем все доступные символы для справки
    all_symbols = set()
    for col in columns:
        all_symbols.update(col)
    
    print("\nДоступные названия символов:")
    symbols_list = sorted(list(all_symbols))
    for i in range(0, len(symbols_list), 6):
        print("  " + ", ".join(symbols_list[i:i+6]))
    
    print("\nВведите названия 4 символов (по одному или через пробел):")
    
    symbols = []
    
    # Можно ввести все сразу или по одному
    input_str = input("\nСимволы: ").strip().lower()
    
    if ' ' in input_str:
        # Ввели все сразу через пробел
        symbols = input_str.split()[:4]
    else:
        # Ввели первый, запрашиваем остальные
        symbols.append(input_str)
        for i in range(2, 5):
            sym = input(f"Символ {i}: ").strip().lower()
            symbols.append(sym)
    
    # Ищем подходящий столбец
    found_column = None
    for col in columns:
        # Проверяем, все ли символы есть в этом столбце
        if all(sym in col for sym in symbols):
            found_column = col
            break
    
    if found_column:
        # Сортируем символы по порядку в столбце
        sorted_symbols = [sym for sym in found_column if sym in symbols]
        
        print("\n" + "=" * 50)
        print("НАЖИМАЙТЕ В ТАКОМ ПОРЯДКЕ:")
        print("=" * 50)
        for i, sym in enumerate(sorted_symbols, 1):
            print(f"{i}. {sym}")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("ОШИБКА: Не найден столбец с этими символами!")
        print("Проверьте правильность ввода.")
        print("=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")