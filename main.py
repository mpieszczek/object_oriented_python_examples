from bank_account import Adres, Client, Account, WrongPinException, DebtNotAllowed


new_adres = Adres("Poniatowskiego", 10, "Katowice", "40-666")
new_client = Client('1' * 11, "Pieszczek", "Mateusz", "2021-11-10", "M", "2021-11-10",
                    "ul. Poniatowskiego 10, Katowice 40-666")
# TEST klasy
# klient i adres nie są tematem zadania więc są stałe
new_account = None
print("Podaj pin do swojego nowego konta.")
while new_account == None:
    try:
        pin = str(input())
        new_account = Account(new_client, new_adres, pin)
    except (WrongPinException):
        print("Nie poprawny format pin-u, spróbuj ponownie.")


while True:
    try:
        print("Wybierz opcję w - wyciąg, d - depozyt, s - status:")
        option = input()
        if option == "d":
            print('Wybrałeś depozyt pieniędzy.\nPodaj kwotę:')
            amount = float(input())
            print('Podaj PIN:')
            pin = input()
            new_account.deposit(amount, pin)
        elif option == "w":
            print('Wybrałeś wyciąg pieniędzy.\nPodaj kwotę:')
            amount = float(input())
            print('Podaj PIN:')
            pin = input()
            new_account.withdrawal(amount, pin)
        elif option == "s":
            print('Wybrałeś status.\nPodaj PIN:')
            pin = input()
            new_account.accountStatus(pin)
        else:
            print("Nie ma takiej operacji.")
    except (WrongPinException):
        print("Zły PIN")
    except (DebtNotAllowed):
        print("Nie posiadasz tyle pieniędzy")
