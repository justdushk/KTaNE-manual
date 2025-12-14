def knobs_module():
    """Модуль поворотных ручек (метод Daido)"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: ПОВОРОТНЫЕ РУЧКИ")
    print("=" * 50)
    
    print("\nМетод быстрой идентификации:")
    print("Введите только номера колонок (1-6), где светодиоды горят В ОБОИХ рядах")
    print("(игнорируйте светодиоды, которые горят только в одном ряду)")
    print("\nПример: если светодиоды горят в обоих рядах в колонках 2, 3 и 5,")
    print("введите: 2 3 5\n")
    
    both_input = input("Введите номера колонок (через пробел): ").strip()
    
    # Парсим ввод
    both_leds = []
    for part in both_input.split():
        try:
            col = int(part)
            if 1 <= col <= 6:
                both_leds.append(col)
        except ValueError:
            continue
    
    both_leds = sorted(set(both_leds))  # Убираем дубликаты и сортируем
    
    print("\n" + "=" * 50)
    print("АНАЛИЗ:")
    print("=" * 50)
    print(f"Светодиоды горят в обоих рядах в колонках: {both_leds if both_leds else 'нет таких'}")
    
    # Правила быстрой идентификации
    result = None
    
    if not both_leds:
        # DOWN: 0 (нет двойных светодиодов)
        result = "ВНИЗ"
    elif both_leds == [5]:
        # LEFT: 5
        result = "ВЛЕВО"
    elif set(both_leds) == {1, 3, 5} or set(both_leds) == {1, 3}:
        # RIGHT: 1-3-5 или 1-3
        result = "ВПРАВО"
    elif set(both_leds) == {3, 6} or set(both_leds) == {3, 5}:
        # UP: 3-6 или 3-5
        result = "ВВЕРХ"
    elif set(both_leds) == {2, 3, 6}:
        # DOWN: 2-3-6
        result = "ВНИЗ"
    else:
        # Дополнительная проверка для других вариантов
        if 2 in both_leds and 3 in both_leds and 6 in both_leds:
            result = "ВНИЗ"
        elif (3 in both_leds and 6 in both_leds) or (3 in both_leds and 5 in both_leds):
            result = "ВВЕРХ"
        elif 5 in both_leds and len(both_leds) == 1:
            result = "ВЛЕВО"
        elif 1 in both_leds and 3 in both_leds:
            result = "ВПРАВО"
        else:
            result = "НЕИЗВЕСТНО"
    
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТ:")
    print("=" * 50)
    
    if result != "НЕИЗВЕСТНО":
        print(f"\n>>> УСТАНОВИТЕ РУЧКУ В ПОЛОЖЕНИЕ: {result} <<<\n")
    else:
        print("\n⚠ Паттерн не распознан!")
        print("Проверьте правильность ввода данных")
        print("\nПодсказка - возможные комбинации:")
        print("  ВВЕРХ:  колонки 3-6 или 3-5")
        print("  ВНИЗ:   колонки 2-3-6 или нет двойных светодиодов (0)")
        print("  ВЛЕВО:  колонка 5")
        print("  ВПРАВО: колонки 1-3-5 или 1-3\n")
    
    print("=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")