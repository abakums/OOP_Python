class Battle:
    """Создание класса с содержанием всех составляющих битвы"""
    @staticmethod
    def battle(u1, u2):
        """Метод для воспроизведения битвы"""
        while u1.health > 0 and u2.health > 0:
            print(u1.universal_hit(u2), "\n")
            if u2.health > 0:
                print(u2.universal_hit(u1), "\n")

    @staticmethod
    def end_of_battle(u1, u2):
        """Вывод окончани битвы"""
        print("\n\n Битва между {0} и {1} одошла к концу!".format(u1, u2))

    def detail_battle(self, u1, u2):
        """Метод битвы с подробностями"""
        print(u1.who_am_i())
        print(u2.who_am_i())
        self.battle(u1, u2)
        self.end_of_battle(u1, u2)
