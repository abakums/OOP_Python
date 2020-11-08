class FoodMixin:
    def eat_meat(self, count):
        print("Вы съели {0} кусков мяса".format(count))

    def eat_fish(self, count):
        print("Вы съели {0} рыб".format(count))

    def drink_milk(self, count):
        print("Вы выпили {0} литров молока".format(count))


class WeightMixin:
    def weight_on_the_scales(self, weight):
        return "Вы взвесились! Ваш вес составляет: {0} кг".format(weight)
