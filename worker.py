from doctest import testmod

class Worker:
    """
    Obiekt Worker - kontener na informacje pracownika

    :param str first_name: imie
    :param str surname: nazwisko
    :param int max_id: statyczny, ostatnio nadany id(nadajemy unikalne)
    :param int id_num: id pracownika

    :Example:
    >>> Worker.max_id = 0
    >>> w1 = Worker("Jan","Kowalski")
    >>> w2 = Worker("Krzysztof","Nowak")
    >>> print(w1)
    1, Jan Kowalski
    >>> print(w2)
    2, Krzysztof Nowak
    """
    max_id = 0

    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname
        Worker.max_id += 1
        self.id_num = Worker.max_id

    def __str__(self):
        return f"{self.id_num}, {self.first_name} {self.surname}"


class Menager(Worker):
    """
    Obiekt Menager - klasa dziedzicąca po Worker
    dodana modyfikowalna lista pracowników podlegających menadżerowi

    :params list workers: lista pracowników podlegających pod menagerem

    :Example:
    >>> Worker.max_id = 0
    >>> w1 = Worker("Jan","Kowalski")
    >>> w2 = Worker("Krzysztof","Nowak")
    >>> m = Menager("Zygmunt", "Tyl", [w1,w2])
    >>> m
    3, Zygmunt Tyl ['1, Jan Kowalski', '2, Krzysztof Nowak']

    """

    def __init__(self, first_name, surname, workers=[]):
        self.workers = workers
        super().__init__(first_name, surname)

    def __str__(self):
        temp = "\n\t".join([str(w) for w in self.workers])
        return super().__str__() + f"\nList of subordinates:\n\t{temp}"

    def __repr__(self):
        return super().__str__() + " " + str([str(w) for w in self.workers])

    def add_worker(self, worker):
        self.workers.append(worker)

    def remove_worker(self, worker):
        self.workers.pop(worker)


testmod()
