from doctest import testmod


class GearBox:
    """
    Obiekt GearBox - skrzynia biegów

    :param int gear: obecny bieg
    :param float v: obecna prędkość
    :param float[] T: tabela progów automatycznej zmiany biegu
    :param float acceleration_limit: limit zmiany prędkość na pojedynczą zmianę

    :Example:
    >>> g1 = GearBox()
    >>> g1
    0, 1
    >>> g1.change_speed(10)
    >>> g1
    10, 1
    """

    def __init__(self, gear=1, v=0,  T=[0, 30, 60, 90, 120, 150], acceleration_limit=30):
        self.v = v
        self.gear = gear
        self.T = T
        self.acceleration_limit = acceleration_limit

    def change_speed(self, by_what):
        """
        Zmiana prędkości. Wymaga numerycznego wejścia,
        oraz możliwego do wykonania przez skrzynię.
        Automatycznie zmieniany jest bieg po zmianie prędkości.
        """
        assert type(by_what) in (float, int)
        assert abs(by_what) <= self.acceleration_limit
        self.v = self.v + by_what
        self.check_gear()

    def change_gear(self, by_what):
        """ Zmiana biegu o wartość. Zakładamy skończoną liczbę biegów """
        assert by_what + self.gear in range(0, 7)
        self.gear += by_what

    def get_gear(self):
        return self.gear

    def check_gear(self):
        """ Sprawdzenie o ile należy zmienić bieg zgodnie z listą progów T """
        if self.gear != 0 and self.v < self.T[self.gear-1]:
            self.change_gear(-1)
            self.check_gear()
        elif self.gear != 6 and self.v > self.T[self.gear]:
            self.change_gear(1)
            self.check_gear()

    def __str__(self):
        return f"Prędkość: {self.v}, Bieg: {self.gear}"

    def __repr__(self):
        return f"{self.v}, {self.gear}"


class EmptyTank(Exception):
    """ Wyjątek wywoływany kiedy zbiornik nie ma paliwa """

    def __str__(self):
        return "Tank is Empty."


class Vehicle:
    """
    Obiekt Vehicle - posiada obiekt, skrzynia biegów,
    dodaje funkcjonalność w postaci zbiornika paliwa.

    :param float gas_level: obecny poziom paliwa
    :param GearBox gear_box: obiekt skrzynia biegów
    :param float v_speed_to_gas: współczynnik spalania na zmianę prędkości


    :Example:
    >>> v = Vehicle()
    >>> v
    100.0, 0, 1
    >>> v.change_speed(10)
    >>> v
    95.0, 10, 1
    """

    def __init__(self):
        self.gas_level = 100.0
        self.gear_box = GearBox()
        self.v_speed_to_gas = 2

    def change_speed(self, value):
        """
        Zwiększenie możliwe tylko jeśli stan paliwa na to pozwala.
        Po sprawdzeniu kożystamy z metody gear_box'a
        """
        if value > 0:
            if value/self.v_speed_to_gas >= self.gas_level:
                raise EmptyTank()
            self.gas_level -= value/self.v_speed_to_gas
        self.gear_box.change_speed(value)

    def get_gas_level(self):
        return self.gas_level

    def fill_tank(self):
        self.gas_level = 100

    def __repr__(self):
        return f"{self.gas_level:.1f}, {self.gear_box.__repr__()}"

    def __str__(self):
        return f"Pojazd: poziom paliwa:{self.gas_level:.1f}\nJego skrzynia biegów:{self.gear_box}"


class Boat:
    """
    Obiekt Boat - posiada obiekt, skrzynia biegów,
    dodaje funkcjonalność w postaci zbiornika paliwa.

    :param float gas_level: obecny poziom paliwa
    :param GearBox gear_box: obiekt skrzynia biegów
    :param float b_speed_to_gas: współczynnik spalania na zmianę prędkości


    :Example:
    >>> b = Boat()
    >>> b
    100.0, 0, 1
    >>> b.change_speed(10)
    >>> b
    96.7, 10, 1
    """

    def __init__(self):
        self.gas_level = 100
        self.gear_box = GearBox()
        self.b_speed_to_gas = 3

    def change_speed(self, value):
        """
        Zwiększenie możliwe tylko jeśli stan paliwa na to pozwala.
        Po sprawdzeniu kożystamy z metody gear_box'a
        """
        if value > 0:
            if value/self.b_speed_to_gas >= self.gas_level:
                raise EmptyTank()
            self.gas_level -= value/self.b_speed_to_gas
        self.gear_box.change_speed(value)

    def get_gas_level(self):
        return self.gas_level

    def fill_tank(self):
        self.gas_level = 100

    def __repr__(self):
        return f"{self.gas_level:.1f}, {self.gear_box.__repr__()}"

    def __str__(self):
        return f"Łódź: poziom paliwa:{self.gas_level:.1f}\nJego skrzynia biegów:{self.gear_box}"


class Amphibian(Boat, Vehicle):
    """
    Obiekt Amphibian - klasa dziedziczy po Boat i Vehicle
    posiada parametr czy znajduje się na wodzie,
    zależnie od tego używa funkcji jednej lub drugiej klasy.
    Różnice tutaj widać w ilości spalanego paliwa.

    :param bool on_water: czy znajduje się na wodzie

    :Example:
    >>> a = Amphibian()
    >>> a.change_speed(10)
    >>> print(a.get_gas_level())
    95.0
    >>> a.change_speed(10)
    >>> print(a.get_gas_level())
    90.0
    >>> a.on_water = True
    >>> a.change_speed(10)
    >>> print(a.get_gas_level())
    86.66666666666667
    """

    def __init__(self, on_water=False):
        self.on_water = on_water
        Boat.__init__(self)
        Vehicle.__init__(self)

    def change_speed(self, value):
        if self.on_water:
            Boat.change_speed(self, value)
        else:
            Vehicle.change_speed(self, value)


testmod()
