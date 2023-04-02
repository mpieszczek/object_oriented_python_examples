from datetime import date

class WrongPinException(Exception):
    pass
class DebtNotAllowed(Exception):
    pass


class Client:
    def __init__(self, pesel, surname, firstName, expiryDate, plec, birthDate, adres):
        if len(pesel)==11:
            self.pesel = pesel
            self.surname = surname
            self.plec = plec
            self.firstName = firstName
            self.expiryDate = expiryDate
            self.birthDate = birthDate
            self.adres = adres
        else:
            print("Nie poprawny pesel")
            print("\n")


    def surname_change(self, new_surname):
        self.surname = new_surname
    def print_data(self):
        print("Imie: "+self.firstName)
        print("Nazwisko: " + self.surname)
        print("PESEL: " + self.pesel)
        print("Data waznosci: " + self.expiryDate)
        print("Plec: " + self.plec)
        print("Data urodzenia: " + self.birthDate)
        print("Adres: " + self.adres)
    def expiry_check(self):
        print("Dzisiaj jest " + str(date.today()) +", a dowód wygasa "+self.expiryDate)



class Adres:
    def __init__(self,street,houseNumber,city,postalCode):
        self.__street = street
        self.__houseNumber = houseNumber
        self.__city = city
        self.__postalCode = postalCode
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,value):
        self.__street = value
    @property
    def houseNumber(self):
        return self.__houseNumber
    @houseNumber.setter
    def houseNumber(self,value):
        self.__houseNumber = value
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,value):
        self.__city = value
        print("Value has been set")
    @property
    def postalCode(self):
        return self.__postalCode
    @postalCode.setter
    def postalCode(self,value):
        self.__postalCode = value



class Account:
    def __init__(self,client,adres,pin):
        if len(pin) == 4 and pin.isnumeric():
            self.client = client
            self.adres = adres
            self.pin = pin
            self.saldo = 0
        else:
            raise WrongPinException
    def CheckPin(self,pin):
        if pin != self.pin:
            raise WrongPinException
    def CheckIfWithdrawalPossible(self,amount):
        if amount > self.saldo:
            raise DebtNotAllowed
    def deposit(self, amount, pin):
        self.CheckPin(pin)
        self.saldo += amount

    def withdrawal(self, amount, pin):
        self.CheckPin(pin)
        self.CheckIfWithdrawalPossible(amount)
        self.saldo -= amount
    def accountStatus(self,pin):
        self.CheckPin(pin)
        print(self.saldo)
        print(self.client.print_data())


