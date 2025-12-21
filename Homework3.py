import random

print('Игра - Soul_night_2.0')
print(
    'Правила игры:\nИгрок заходит на игровое поле на позицию (1;1). У него есть выбор: пойти налево, направо, вверх, вниз.\n Есть несколько видов комнат, в которые игрок может попасть.\nВиды комнат: пустая комната, комната с сундуком, логово монстра, комната с ключом, комната ловушка, портал')
print('Чтобы победить в игре игроки необходимо найти ключ в специальной комнате, а потом пройти к порталу')
print(
    'По ходу игры Вы можете находить различные предметы для игры, которые помогут Вам пройти сквозь монстров, а также не умереть в других опасных комнатах')
print("Инвентарь ограничен 5 слотами, выбирайте предметы, которые хотите взять, с умом")
print("\n")
print('Какой уровень сложности хотите выбрать? (напишите цифру)')
print('1 уровень: поле 4х4')
print('2 уровень: поле 8х8')
print('3 уровень: поле 12х12')

player_choice = int(input())

rooms = ["пусто", "сундук", "монстр", "ключ", "ловушка", "портал"]
items_pool = ["зелье здоровья", "меч", "щит", "АК-74", "патроны", "броня"]


class Game():
    def __init__(self, hero, lvl, position):
        self.hero = hero
        self.hp = 100
        self.hp_max = 100
        self.lvl = lvl
        self.position = position
        self.inventory = []
        self.max_inventory_size = 5
        self.has_key = False
        self.game_over = False
        self.win = False

        if lvl == 1:
            self.field_size = 4
        elif lvl == 2:
            self.field_size = 8
        else:
            self.field_size = 12

        self.field = [[random.choice(["пусто", "сундук", "монстр", "ловушка"]) for i in range(self.field_size)] for j in range(self.field_size)]  # создается игровое поле со случайнвми комнатами

        key_x, key_y = random.randint(0, self.field_size - 1), random.randint(0, self.field_size - 1)  # вставляем ключ на какую то позициб
        portal_x, portal_y = random.randint(0, self.field_size - 1), random.randint(0, self.field_size - 1)  # и портал

        while portal_x == key_x and portal_y == key_y:  # убираем случай, когда портал и ключ вместе
            portal_x, portal_y = random.randint(0, self.field_size - 1), random.randint(0, self.field_size - 1)

        self.field[key_x][key_y] = "ключ"
        self.field[portal_x][portal_y] = "портал"

        self.position = [0, 0]  # начало игры
        self.field[0][0] = "пусто"  # начальная комната пустая

    # смотрим на карту с предметами, затем удалим после тестирования
    def show_dev_map(self):
        print("\nРЕЖИМ РАЗРАБОТЧИКА")
        print("К - ключ, П - портал, М - монстр, С - сундук, Л - ловушка, _ - пусто")
        print("Игрок находится на позиции:", (self.position[0] + 1, self.position[1] + 1)) #расположение игрока, смотрим на массив
        #создаем двумерный массив и обозначаем расположение
        for i in range(self.field_size):
            row = []
            for j in range(self.field_size):
                room = self.field[i][j]
                if room == "ключ":
                    row.append("К")
                elif room == "портал":
                    row.append("П")
                elif room == "монстр":
                    row.append("М")
                elif room == "сундук":
                    row.append("С")
                elif room == "ловушка":
                    row.append("Л")
                elif room == "пусто":
                    row.append("_")
                else:
                    row.append("?")
            print(" ".join(row))
        print("\n")

    def show_status(self):
        print(f'\n СТАТУС ')
        print(f'Имя Героя: {self.hero}')
        print(f'Здоровье: {self.hp}/{self.hp_max}')
        print(f'Уровень: {self.lvl} (поле {self.field_size}x{self.field_size})')
        print(f'Позиция: ({self.position[0] + 1}, {self.position[1] + 1})')
        print(f'Ключ: {"найден" if self.has_key else "не найден"}')
        print(f'Инвентарь ({len(self.inventory)}/{self.max_inventory_size}): {self.inventory}')
        print('\n')

    def show_inventory(self):
        print(f'\n ИНВЕНТАРЬ ')
        if not self.inventory:
            print("Инвентарь пуст")
        else:
            # генератор списка для отображения пронумерованного инвентаря
            inventory_list = [f"{i + 1}. {item}" for i, item in enumerate(self.inventory)]
            print("\n".join(inventory_list))
        print('\n')

    def move_player(self, direction):  # функция для движения
        x, y = self.position

        if direction == "вверх" and x > 0:
            x -= 1
        elif direction == "вниз" and x < self.field_size - 1:
            x += 1
        elif direction == "влево" and y > 0:
            y -= 1
        elif direction == "вправо" and y < self.field_size - 1:
            y += 1
        else:
            print("Вы улетели за границу вселенной... Удачного полета!")
            self.game_over = True
            return

        self.position = [x, y]
        self.enter_room(x, y)

    def enter_room(self, x, y):
        room_type = self.field[x][y]
        print(f"\nВы вошли в комнату ({x + 1}, {y + 1}): {room_type}")

        if room_type == "пусто":
            print("Комната пуста. Ничего интересного.")

        elif room_type == "сундук":
            found_items = [random.choice(items_pool) for _ in range(random.randint(1, 2))]  # находим случайный предмте
            print(f"Вы нашли сундук! Внутри: {', '.join(found_items)}")

            for item in found_items:
                if len(self.inventory) < self.max_inventory_size:
                    self.inventory.append(item)  # добавляем предмет в инвентарб
                    print(f"Вы взяли: {item}")
                else:
                    print(f"Инвентарь полон! Успокойся. Нельзя взять: {item}")

        elif room_type == "монстр":
            damage = random.randint(10, 30)
            if 'меч' in self.inventory:
                print("Вы грохнули монстра мечом и не получили урона!")
                self.inventory.remove('меч')

            elif 'АК-74' in self.inventory and 'патроны' in self.inventory:
                print("Вы  расстреляли монстра и не получили урона! Горжусь!")
                self.inventory.remove('АК-74')
                self.inventory.remove('патроны')

            elif 'щит' in self.inventory:
                reduce_damage = damage // 2
                self.hp -= reduce_damage
                print(f"Вы заблокировали атаку щитом! Получили {reduce_damage} урона вместо {damage}.")
                self.inventory.remove('щит')

            elif 'броня' in self.inventory:
                reduce_damage = damage // 2
                self.hp -= reduce_damage
                print(f"Броня поглотила часть удара! Получили {reduce_damage} урона вместо {damage}.")
                self.inventory.remove('броня')

            else:
                self.hp -= damage
                print(f"На вас напал монстр! Вы беззащитны и потеряли {damage} здоровья. Акуратнее")



        elif room_type == "ключ":
            if not self.has_key:
                self.has_key = True
                self.field[x][y] = "пусто"  # убираем ключ с карты
                print("Вы нашли ключ! Теперь вы можете активировать портал!")

                if len(self.inventory) < self.max_inventory_size:  # +ключ в инвентарь, если есть место
                    self.inventory.append("ключ")
                else:
                    print("Инвентарь полон, но ключ активирован")
            else:
                print("Вы уже нашли ключ ранее.")

        elif room_type == "ловушка":
            damage = random.randint(5, 20)
            self.hp -= damage
            print(f"Вы попали в ловушку! Вы потеряли {damage} здоровья.")
            if "щит" in self.inventory or "броня" in self.inventory:
                print("Ваша защита смягчила удар!")
                self.hp += damage // 2  # срезаем урон (те добавляем)
                self.inventory.remove('щит')
                self.inventory.remove('броня')

        elif room_type == "портал":
            if self.has_key:
                print("ПОЗДРАВЛЯЕМ! Вы активировали портал с помощью ключа и победили в игре!")
                self.win = True
                self.game_over = True
            else:
                print("Это портал, но для его активации нужен ключ. Найдите его...")

        # проверка здоровья
        if self.hp <= 0:
            print("Ваше здоровье на нуле. Игра окончена... Попробуй еще раз")
            self.game_over = True

    def do_smthg_with_inventory(self):  # функция для упр инвентом
        while True:
            print("\n УПРАВЛЕНИЕ ИНВЕНТАРЕМ ")
            self.show_inventory()

            print("1. Выбросить предмет")
            print("2. Отсортировать инвентарь")
            print("3. Перевернуть порядок предметов")
            print("4. Найти предмет")
            print("5. Выйти из управления инвентарем")
            print("6. Похилиться")
            choice = input("Выберите действие: ")

            if choice == "1":
                if not self.inventory:
                    print("Инвентарь пуст!")
                    continue

                item_name = input("Введите название предмета для выбрасывания: ")
                if item_name in self.inventory:  # проверяем есть ли предмет вообще
                    self.inventory.remove(item_name)  # удаляем
                    print(f"Вы выбросили: {item_name}")
                else:
                    print("Такого предмета нет в инвентаре!")

            elif choice == "2":
                if not self.inventory:
                    print("Инвентарь пуст!")
                    continue

                self.inventory.sort()  # сорт
                print("Инвентарь отсортирован!")

            elif choice == "3":
                if not self.inventory:
                    print("Инвентарь пуст!")
                    continue

                self.inventory.reverse()  # реверсируем список
                print("Порядок предметов изменен!")

            elif choice == "4":
                if not self.inventory:
                    print("Инвентарь пуст!")
                    continue

                item_name = input("Введите название предмета для поиска: ")
                if item_name in self.inventory:  # есть ли вообще предмет
                    index = self.inventory.index(item_name)  # ищем индекс
                    print(f"Предмет '{item_name}' найден в позиции {index + 1}")
                else:
                    print(f"Предмет '{item_name}' не найден в инвентаре!")
            elif choice == '6':
                if "зелье здоровья" not in self.inventory:
                    print("У вас нет зелья здоровья!")
                    continue
                else:
                    if self.hp + 20 >= 100:
                        self.hp = 100
                        self.inventory.remove('зелье здоровья')
                    else:
                        self.hp += 20
                        self.inventory.remove('зелье здоровья')



            elif choice == "5":
                break
            else:
                print("Неверный выбор!")

    def play(self):
        print(f"\nДобро пожаловать в подземелье, {self.hero}!")
        print("Цель: найти ключ и активировать портал для победы.")

        while not self.game_over:
            self.show_status()

            # показать карту (удалим после тестирования)
            self.show_dev_map()

            print("Доступные действия:")
            print("1. Двигаться (вверх, вниз, влево, вправо)")
            print("2. Просмотреть инвентарь")
            print("3. Управление инвентарем")
            print("4. Сдаться")

            action = input("Выберите действие: ")

            if action == "1":
                direction = input("Куда двигаться? (вверх/вниз/влево/вправо): ").lower()
                if direction in ["вверх", "вниз", "влево", "вправо"]:
                    self.move_player(direction)
                else:
                    print("Неверное направление!")

            elif action == "2":
                self.show_inventory()

            elif action == "3":
                self.do_smthg_with_inventory()

            elif action == "4":
                print("Вы сдались. Игра окончена!")
                self.game_over = True

            else:
                print("Неверный выбор!")

        if self.win:
            print("\n ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ! ")
        else:
            print("\nИГРА ОКОНЧЕНА. ВЫ ПРОИГРАЛИ.")


# Запуск игры
hero_name = input("Введите имя вашего героя: ")
game = Game(hero_name, player_choice, [0, 0])
game.play()
