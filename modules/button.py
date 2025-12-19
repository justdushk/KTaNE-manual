def button_module():
    """Модуль кнопки"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: КНОПКА")
    print("=" * 50)
    
    # Ввод данных
    print("\nДоступные цвета: синий(с), белый(б), желтый(ж), красный(кр)")
    while True:
        color = input("Цвет кнопки: ").strip().lower()
        if color in ['с', 'б', 'ж', 'кр']:
            break
        print("Неверный цвет!")
    
    print("\nДоступные надписи: прервать(п), взорвать(в), держать(д)")
    while True:
        label = input("Надпись на кнопке: ").strip().lower()
        if label in ['п', 'в', 'д']:
            break
        print("Неверная надпись!")
    
    hold = False  # Нужно ли удерживать
    
    # Правило 1
    if color == 'с' and label == 'п':
        hold = True
    # Правило 2
    elif label == 'в':
        batteries = int(input("\nКоличество элементов питания на бомбе: "))
        if batteries > 1:
            print("\n" + "=" * 50)
            print("НАЖМИТЕ И РЕЗКО ОТПУСТИТЕ КНОПКУ")
            print("=" * 50)
            input("\nНажмите Enter для возврата в меню...")
            return
    # Правило 3
    elif color == 'б':
        car = input("\nЕсть ли горящий индикатор CAR? (да/нет): ").strip().lower()
        if car == 'да':
            hold = True
    # Правило 4
    if not hold and label != 'в':
        batteries = int(input("\nКоличество элементов питания на бомбе: "))
        frk = input("Есть ли горящий индикатор FRK? (да/нет): ").strip().lower()
        if batteries > 2 and frk == 'да':
            print("\n" + "=" * 50)
            print("НАЖМИТЕ И РЕЗКО ОТПУСТИТЕ КНОПКУ")
            print("=" * 50)
            input("\nНажмите Enter для возврата в меню...")
            return
    # Правило 5
    if not hold and color == 'ж':
        hold = True
    # Правило 6
    elif not hold and color == 'кр' and label == 'д':
        print("\n" + "=" * 50)
        print("НАЖМИТЕ И РЕЗКО ОТПУСТИТЕ КНОПКУ")
        print("=" * 50)
        input("\nНажмите Enter для возврата в меню...")
        return
    # Правило 7
    elif not hold:
        hold = True
    
    # Если дошли сюда - удерживаем
    if hold:
        print("\n" + "=" * 50)
        print("УДЕРЖИТЕ КНОПКУ")
        print("=" * 50)
        print("\nПРИ УДЕРЖАНИИ КНОПКИ:")
        print("С  - 4")
        print("Б  - 1")
        print("Ж - 5")
        print("Другое - 1")
        print("\n(Отпустите, когда любая цифра таймера равна указанной)")
        print("=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")