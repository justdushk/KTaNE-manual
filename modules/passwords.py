def passwords_module():
    """Модуль паролей (пошаговый ввод)"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: ПАРОЛИ")
    print("=" * 50)
    
    # Список всех возможных паролей
    all_passwords = [
        'аллея', 'бомба', 'вверх', 'взрыв', 'внизу',
        'вьюга', 'горох', 'готов', 'густо', 'давай',
        'давно', 'книга', 'конец', 'лилия', 'линия',
        'можно', 'назад', 'нравы', 'песец', 'песня',
        'порох', 'порыв', 'потом', 'право', 'пусто',
        'румба', 'скоро', 'супер', 'травы', 'тумба',
        'тунец', 'фугас', 'шприц', 'щипок', 'щипцы'
    ]
    
    possible = all_passwords.copy()
    position = 0
    entered_letters = []
    
    while position < 5:
        print("\n" + "=" * 50)
        print(f"ПОЗИЦИЯ {position + 1} из 5")
        print("=" * 50)
        
        if entered_letters:
            print(f"Введено: {' '.join(entered_letters)}_____"[:5])
        
        print(f"\nТекущих вариантов: {len(possible)}")
        
        letter = input(f"\nВведите букву {position + 1} (или 'назад'/'выход'): ").strip().lower()
        
        if letter == 'выход':
            return
        
        if letter == 'назад':
            if position > 0:
                position -= 1
                entered_letters.pop()
                # Восстанавливаем список паролей для предыдущей позиции
                possible = all_passwords.copy()
                for i, let in enumerate(entered_letters):
                    possible = [pwd for pwd in possible if pwd[i] == let]
            else:
                print("⚠ Уже первая позиция!")
            continue
        
        if len(letter) != 1 or not letter.isalpha():
            print("⚠ Введите одну букву!")
            continue
        
        # Фильтруем пароли
        filtered = [pwd for pwd in possible if pwd[position] == letter]
        
        if not filtered:
            print(f"\n⚠ Нет паролей с буквой '{letter}' на позиции {position + 1}")
            print("\nДоступные буквы на этой позиции:")
            available = sorted(set(pwd[position] for pwd in possible))
            print("  " + ", ".join(available))
            continue
        
        # Обновляем список
        possible = filtered
        entered_letters.append(letter)
        
        print(f"\n✓ Осталось вариантов: {len(possible)}")
        
        if len(possible) <= 5:
            print("\nПодходящие пароли:")
            for pwd in possible:
                highlight = ''.join(
                    f"[{c}]" if i <= position else c
                    for i, c in enumerate(pwd)
                )
                print(f"  • {highlight}")
        
        if len(possible) == 1:
            print("\n" + "=" * 50)
            print(f"🎯 ПАРОЛЬ НАЙДЕН: {possible[0].upper()}")
            print("=" * 50)
            input("\nНажмите Enter для возврата в меню...")
            return
        
        position += 1
    
    # Если дошли до конца
    print("\n" + "=" * 50)
    if len(possible) == 1:
        print(f"🎯 ПАРОЛЬ: {possible[0].upper()}")
    elif possible:
        print("ВОЗМОЖНЫЕ ПАРОЛИ:")
        for pwd in possible:
            print(f"  • {pwd.upper()}")
    else:
        print("⚠ Что-то пошло не так!")
    print("=" * 50)
    
    input("\nНажмите Enter для возврата в меню...")