from doctest import testmod

class OutOffPowerError(Exception):
    def __str__(self):
        return "Out off power"


class Robot:
    '''
    Obiekt ruszającego się Robota.

    robot może poruszac się w 2 wymiarach po planszy.
    Nalezy uważać aby robot posiadał moc. Aby ją uzupełnić
    należy wstąpić na pole pierwszego wiersza.

    :param str name: nazwa
    :param tuple start: pozycja startowa
    :param list place: obecna pozycja
    :param int power: moc potrzebna do wykonywania ruchów
    :param int board_dim: długość boku planszy

    :Example:
    >>> r = Robot("robot1")
    >>> r
    robot1, [0, 0], 9
    >>> r.up(-1)
    >>> r
    robot1, [1, 0], 8
    >>> r.up(1)
    >>> r
    robot1, [0, 0], 12
    >>> r.up(13)
    >>> r
    robot1, [3, 0], -1
    >>> r.up(2)
    Out off power
    >>> r
    robot1, [3, 0], -1
    '''

    def __init__(self, name, start=(0, 0), power=9, board_dim=8):
        self.name = name
        self.start = start
        self.board_dim = board_dim
        self.power = power
        self.place = list(start)

    @property
    def name(self):
        return self.__dict__['name']

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError("Name must be string type.")
        self.__dict__['name'] = value

    @property
    def start(self):
        return self.__dict__['start']

    @start.setter
    def start(self, value):
        if type(value) not in (list, tuple) or len(value) != 2:
            raise TypeError("Place must be 2 elements list.")
        self.__dict__['start'] = value

    @property
    def board_dim(self):
        return self.__dict__['board_dim']

    @board_dim.setter
    def board_dim(self, value):
        if type(value) != int or value <= 0:
            raise TypeError("Board dimention must be positive integer type.")
        self.__dict__['board_dim'] = value

    @property
    def place(self):
        return self.__dict__['place']

    @place.setter
    def place(self, value):
        if type(value) not in (list, tuple) or len(value) != 2:
            raise TypeError("Place must be 2 elements list.")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("Place values should be int")
        self.__dict__['place'] = value
        self.__dict__['place'][0] = self.__dict__['place'][0] % self.board_dim
        self.__dict__['place'][1] = self.__dict__['place'][1] % self.board_dim

    @property
    def power(self):
        return self.__dict__['power']

    @power.setter
    def power(self, value):
        if type(value) != int:
            raise TypeError("Power must be integer type.")
        self.__dict__['power'] = value

    def __move(self, vector, value):
        if type(value) != int:
            raise TypeError("You can only move with integer intervals.")
        try:
            self.check_power()
            new_position = [self.place[0] +
                            vector[0], self.place[1] + vector[1]]
            self.place = new_position
            self.power = self.power - abs(value)

            if self.place[0] == 0:  # jeśli pierwszy wiersz
                self.power = self.power + 5
        except OutOffPowerError as e:
            print(e)

    def up(self, value):
        self.__move([-value, 0], value)

    def left(self, value):
        self.__move([0, -value], value)

    def __str__(self):
        return f"Name:{self.name},\nPlace: {self.place},\nPower: {self.power}"

    def __repr__(self):
        return f"{self.name}, {self.place}, {self.power}"

    def check_power(self):
        if self.power <= 0:
            raise OutOffPowerError

testmod()
