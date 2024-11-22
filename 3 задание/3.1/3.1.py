class GeometricFigure:
    def area(self):
        raise NotImplementedError()
    
class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return pi * (self.radius ** 2)

class Rhombus(GeometricFigure):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

def main():
    continue_program = True
    
    while continue_program:
        print("\nВыберите фигуру для расчета площади:")
        print("1. Прямоугольник")
        print("2. Круг")
        print("3. Ромб")
        print("4. Выход")
        
        choice = input("Введите номер фигуры (1-4): ")
        
        if choice == '1':
            width = float(input("Ширина прямоугольника = "))
            height = float(input("Высота прямоугольника = "))
            rectangle = Rectangle(width, height)
            print("Площадь прямоугольника =", rectangle.area())
        
        elif choice == '2':
            radius = float(input("Радиус круга = "))
            circle = Circle(radius)
            print("Площадь круга =", circle.area())
        
        elif choice == '3':
            diagonal1 = float(input("1 диагональ ромба  = "))
            diagonal2 = float(input("2 диагональ ромба 2 = "))
            rhombus = Rhombus(diagonal1, diagonal2)
            print("Площадь ромба =", rhombus.area())
        
        elif choice == '4':
            print("Выход из программы.")
            continue_program = False
        
        else:
            print("Неверный выбор. Пожалуйста, выберите номер от 1 до 4.")

if __name__ == "__main__":
    main()
