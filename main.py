import os
import sys

# Импорты модулей
from modules.wires import wires_module
from modules.button import button_module
from modules.keypads import keypads_module
from modules.simon_says import simon_says_module
from modules.avas import avas_module
from modules.memory import memory_module
from modules.morse_code import morse_code_module
from modules.complicated_wires import complicated_wires_module
from modules.wire_sequence import wire_sequence_module
from modules.maze import maze_module
from modules.passwords import passwords_module
from modules.knobs import knobs_module

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """Главное меню выбора модуля"""
    while True:
        clear_screen()
        print("=" * 50)
        print("KEEP TALKING AND NOBODY EXPLODES - МАНУАЛ")
        print("=" * 50)
        print("\nВыберите модуль:\n")
        print("1.  Провода")
        print("2.  Кнопка")
        print("3.  Клавиатуры")
        print("4.  Делай как я (Simon Says)")
        print("5.  Меня зовут Авас, а вас?")
        print("6.  Память")
        print("7.  Азбука Морзе")
        print("8.  Усложненные провода")
        print("9.  Последовательности проводов")
        print("10. Лабиринты")
        print("11. Пароли")
        print("12. О поворотных ручках (нестабильный)")
        print("\n0.  Выход")
        print("=" * 17 + ' made by justduhsik ' + "=" * 17)
        
        choice = input("\nВведите номер модуля: ").strip()
        
        if choice == "0":
            print("\nДо встречи!")
            sys.exit()
        elif choice == "1":
            wires_module()
        elif choice == "2":
            button_module()
        elif choice == "3":
            keypads_module()
        elif choice == "4":
            simon_says_module()
        elif choice == "5":
            avas_module()
        elif choice == "6":
            memory_module()
        elif choice == "7":
            morse_code_module()
        elif choice == "8":
            complicated_wires_module()
        elif choice == "9":
            wire_sequence_module()
        elif choice == "10":
            maze_module()
        elif choice == "11":
            passwords_module()
        elif choice == "12":
            knobs_module()
        else:
            print("\nНеверный выбор!")
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main_menu()