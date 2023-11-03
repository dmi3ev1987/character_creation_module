from random import randint

"""
Хорошим тоном считается давать числовым значениям имена, если это возможно.
Число 5 — это значение стандартной атаки, и в рамках вашего кода оно
неизменяемо. Вынесите это значение в глобальную константу
и назовите её DEFAULT_ATTACK:
"""
# Вот она — новая глобальная константа.
DEFAULT_ATTACK = 5
# Новая константа — стандартное значение защиты.
DEFAULT_DEFENCE = 10
# Стандартное значение выносливости.
DEFAULT_STAMINA = 80


class Character:
    # Новая константа.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Новая переменная класса — диапазон значения защиты.
    RANGE_VALUE_DEFENCE = (1, 5)
    # Вот они — две новые константы.
    SPECIAL_BUFF = 15  # значение очков урона, для базового класса
    SPECIAL_SKILL = 'Удача'  # название умения

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки
    def attack(self):
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        # Вместо числа 5 теперь используется константа DEFAULT_ATTACK.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    # Объявляем метод защиты.
    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Объявляем метод специального умения.
    def special(self):
        # Здесь описано тело метода special().
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    # Новый метод базового класса.
    def __str__(self):
        # Чтобы вывести имя у объекта класса есть специальный атрибут
        # __class__.__name__
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


# Далее описываем классы-наследники.
class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
