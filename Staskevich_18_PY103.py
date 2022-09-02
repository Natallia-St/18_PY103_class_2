class Tomato: # Объявление класса
    states = [1, 2, 3] # Создание статической переменной в виде списка с этапами роста

    def __init__(self, index): # Инициал. динамической переменной класса
        self._index = index
        self._state = 0

    def grow(self): # Метод для перехода на следующий уровень роста
        if self._state < 3:
            self._state += 1
            print("Уровень роста", self._state)

    def is_ripe(self): # Метод для определения спелости, если объект достиг последнего уровня
        if self._state == 3:
            # print("Спелый")
            return True

        else:
            # print("НЕ спелый")
            return False


class TomatoBush: # Объявление класса
    def __init__(self, count_tomato): # Инициал. динамической переменной класса
        self.count_tomato = count_tomato
        # Создание пуcтого списка и наполнение его объектами класса Tomato
        self.list_ = []
        for i in range(0, count_tomato):
            self.list_.append(Tomato(index=i))
        # for i in self.list_:
        # print(self._state)

    def grow_all(self): # Метод для перехода всех томатов из списка на следующий уровень роста
        for i in self.list_: # Для каждого томата из списка вызываем метод grow из класса Tomato
            i.grow()
            # print(i._state)

    def all_are_ripe(self): # Метод класса для определения зрелости всех томатов
        all_ripe_list_ = [] # Список, в который будем для каждого томата записывать зрелый/не зрелый
        for i in self.list_:
            if i.is_ripe():
                all_ripe_list_.append(True)
            else:
                all_ripe_list_.append(False)
        # print(all_ripe_list_)
        return all(all_ripe_list_) # Возврат списка, если для всех томатов в списке True

    def give_away_all(self): # Очистка списка с томатами
        self.list_.clear()


class Gardener: # Объявление класса
    def __init__(self, name, plant): # Инициал. динамической переменной класса
        self.name = name
        self._plant = plant # Plant будет передоваться в качестве параметра для Gardener, как объект класса Томат

    def work(self): # Метод, при вызове которого растения переходят на следующий уровень
        print("Садовник поработал и tomato на растении достигли следующего этапа")
        self._plant.grow_all()

    def harvest(self):# Метод, который будет проверять, созрели ли все томаты
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Томаты созрели и садовник собрал весь урожай")
        else:
            print("Не весь урожай еще созрел")

    @staticmethod # Статический метод
    def info():
        print("Справка по садоводству")


Gardener.info()
object_bush = TomatoBush(2)
# object_bush.grow_all()
# object_bush.all_are_ripe()
object_gardener = Gardener("Sam", object_bush)
object_gardener.work()
object_gardener.harvest()
object_gardener.work()
object_gardener.harvest()
object_gardener.work()
object_gardener.harvest()
# object_gardener.work()
# object_gardener.harvest()
