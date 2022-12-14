import sys

expenses = []

def expense_show(month):
    for expense_amounth, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amounth} - {expense_type}')
def add_expense(month):
    print()
    expense_amounth = input("Podaj kwotę:")
    if expense_amounth.isalpha():
        expense_amounth = input("Trzeba podać kwotę, a nie słowo.")

    expense_type = input("Podaj typ wydatku (rozrywka, dom, zakupy i inne): ")
    if expense_type.isdigit():
        expense_type = input("Trzeba podać typ wydatków w postaci słowa.")
    expense = (expense_amounth, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amounth_of_month = sum(int(expense_amounth) for expense_amounth, _, expense_month in expenses if expense_month == month)
    number_of_expesnses_of_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expense_of_month = total_amounth_of_month / number_of_expesnses_of_month
    total_amounth_all = sum(int(expense_amounth) for expense_amounth, _, _ in expenses)
    average_expense_all = total_amounth_all / len(expenses)
 
    print()
    print("Statystyki:")
    print("Wszystkie wydatki w tym miasiącu:", total_amounth_of_month)
    print("Średnia kwota wydatków: ", average_expense_of_month)
    print("Wszystkie wydatki: ", total_amounth_all)
    print("Średnia kwota za wszystkie miesiąca: ", average_expense_all)
    print(int("Statystyki:", dom, rozrywka, inne, zakupy ))
    

while True:
    print()
    month = (int(input("Wybierz miesiąc od 1 do 12: ")))
    if  month == 0 or month >= 13 or month <= 0:
        print(input("Musisz podać cyfre od 1 do 12."))
    
    while True:
            print()
            print("0 - powrót do wyboru miesiąca.")
            print("1 - wyświetl wszystkie wydatki.")
            print("2 - dodaj wydatek.")
            print("3 - Statystyki.")
            choice = int(input("Wybierz opcję: "))
                
            if choice == 0:
                break
            if choice == 1:
                expense_show(month)
            if choice == 2:
                add_expense(month)
            if choice == 3:
                show_stats(month)
            if choice <0 or choice >=4:
                print("Podaj zakres od 0 do 3.")