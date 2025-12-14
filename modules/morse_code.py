def morse_code_module():
    """Модуль азбуки Морзе"""
    print("\n" + "=" * 50)
    print("МОДУЛЬ: АЗБУКА МОРЗЕ")
    print("=" * 50)
    
    # Таблица морзе (русская азбука)
    morse_table = {
        'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 
        'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---',
        'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
        'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
        'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
        'щ': '--.-', 'ъ': '--.--', 'ь': '-..-', 'ы': '-.--', 'э': '..-..',
        'ю': '..--', 'я': '.-.-'
    }
    
    # Таблица слов и частот
    words_freq = {
        'токарь': '3.505',
        'мостик': '3.515',
        'венок': '3.522',
        'брать': '3.532',
        'клара': '3.535',
        'попей': '3.542',
        'виток': '3.545',
        'восток': '3.552',
        'вилка': '3.555',
        'порок': '3.565',
        'койка': '3.572',
        'рокер': '3.575',
        'помой': '3.582',
        'покой': '3.592',
        'борис': '3.595',
        'порог': '3.600'
    }
    
    print("\nВводите буквы в морзе (. и -).")
    print("После ввода каждой буквы будет показан список возможных слов.")
    print("\nКоманды:")
    print("  'назад' - отменить последнюю букву")
    print("  'выход' - вернуться в меню\n")
    
    current_letters = []
    letter_num = 1
    
    while True:
        morse_input = input(f"\nБуква {letter_num}: ").strip().lower()
        
        if morse_input == 'выход':
            break
        elif morse_input == 'назад':
            if current_letters:
                removed = current_letters.pop()
                print(f"✓ Отменена буква: {removed.upper()}")
                print(f"Текущее слово: {''.join(current_letters).upper() if current_letters else '(пусто)'}\n")
                letter_num -= 1
            else:
                print("Слово пусто, нечего отменять!\n")
            continue
        
        # Проверяем корректность ввода
        if not all(c in '.-' for c in morse_input):
            print("Используйте только точки (.) и тире (-)!")
            continue
        
        # Ищем букву по морзе
        found_letter = None
        for letter, code in morse_table.items():
            if code == morse_input:
                found_letter = letter
                break
        
        if found_letter:
            current_letters.append(found_letter)
            print(f"→ Буква: {found_letter.upper()}")
            print(f"Текущее слово: {''.join(current_letters).upper()}")
            
            # Автоматически ищем возможные слова
            current_word = ''.join(current_letters)
            possible_words = []
            
            for word, freq in words_freq.items():
                if word.startswith(current_word):
                    possible_words.append((word, freq))
            
            if possible_words:
                print("\n" + "-" * 50)
                print("ВОЗМОЖНЫЕ СЛОВА:")
                for word, freq in possible_words:
                    print(f"  {word.upper():8} → {freq} МГц")
                print("-" * 50)
                
                # Проверяем точное совпадение
                if current_word in words_freq:
                    freq = words_freq[current_word]
                    print("\n" + "=" * 50)
                    print(f"✓ СЛОВО НАЙДЕНО: {current_word.upper()}")
                    print(f"✓ УСТАНОВИТЕ ЧАСТОТУ: {freq} МГц")
                    print("=" * 50)
                    
                    cont = input("\nНачать заново? (да/нет): ").strip().lower()
                    if cont == 'да':
                        current_letters = []
                        letter_num = 0
                    else:
                        break
            else:
                print("\n⚠ Нет слов с таким началом! Проверьте ввод.")
                print("Начинаем заново...")
                current_letters = []
                letter_num = 0
            
            letter_num += 1
        else:
            print("Не найдено буквы с таким кодом! Проверьте ввод.")
    
    input("\nНажмите Enter для возврата в меню...")