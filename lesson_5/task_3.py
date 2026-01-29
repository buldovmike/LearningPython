min_sum_invest=int(input("Введите минимальную сумму инвестиций "))
mike_cash=int(input("Введите кол-во доларов у Майкла "))
ivan_cash=int(input("Ввидите кол-во долларов у Ивана "))

if (mike_cash >= min_sum_invest) and (ivan_cash >= min_sum_invest):
    print("2")
elif (mike_cash >= min_sum_invest) and not((ivan_cash >= min_sum_invest)):
    print("Mike")
elif not((mike_cash >= min_sum_invest)) and (ivan_cash >= min_sum_invest):
    print("Ivan")
elif (mike_cash + ivan_cash) >= min_sum_invest:
    print("1")
else:
    print("0")
