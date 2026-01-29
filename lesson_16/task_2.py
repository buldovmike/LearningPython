class Turtle:
    #Инициализирует черепашку с начальными координатами и шагом
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
    #Увеличивает y на s
    def go_up(self):
        self.y += self.s
    #Уменьшает y на s
    def go_down(self):
        self.y -= self.s
    #Уменьшает x на s
    def go_left(self):
        self.x -= self.s
    #Увеличивает x на s
    def go_right(self):
        self.x += self.s
    #Увеличивает s на 1
    def evolve(self):
        self.s += 1
    #Уменьшает s на 1.
    #Если s станет ≤ 0, выводит сообщение об ошибке и не изменяет значение
    def degrade(self):
        if self.s <= 1:
            print("Ошибка: параметр s не может стать ≤ 0.")
        else:
            self.s -= 1

    #Возвращает минимальное количество действий для достижения точки (x2, y2)
    def count_moves(self, x2, y2):
        # Вычисляем расстояния по осям
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        # Количество ходов по каждой оси (целочисленное деление с округлением вверх)
        moves_x = dx // self.s
        if dx % self.s != 0:
            moves_x += 1

        moves_y = dy // self.s
        if dy % self.s != 0:
            moves_y += 1

        return moves_x + moves_y

# Пример использования:
if __name__ == "__main__":
    # Создаем черепашку в точке (0, 0) с шагом 1
    turtle = Turtle(0, 0, 1)

    print(f"Начальная позиция: ({turtle.x}, {turtle.y}), шаг: {turtle.s}")

    # Двигаемся вверх
    turtle.go_up()
    print(f"После go_up(): ({turtle.x}, {turtle.y})")

    # Двигаемся вправо
    turtle.go_right()
    print(f"После go_right(): ({turtle.x}, {turtle.y})")

    # Увеличиваем шаг
    turtle.evolve()
    print(f"После evolve(): шаг = {turtle.s}")

    # Считаем ходы до точки (5, 3)
    moves = turtle.count_moves(5, 3)
    print(f"Минимальное количество ходов до (5, 3): {moves}")

    # Пытаемся уменьшить шаг (должно пройти успешно)
    turtle.degrade()
    print(f"После degrade(): шаг = {turtle.s}")

    # Пытаемся уменьшить шаг еще раз (должно вывести сообщение об ошибке)
    turtle.degrade()