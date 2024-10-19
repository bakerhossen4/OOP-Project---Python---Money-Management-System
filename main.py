from moneymanage import MoneyManage
from make import Make

manob = MoneyManage()
makeob1 = Make( "baker", 200 )
makeob2 = Make( "faker", 1200 )
makeob3= Make( "zaker", 2200 )

makeob4 = Make( "rahim", 100 )
makeob5 = Make( "karim", 1100 )
makeob6 = Make( "fahim", 2100 )

manob.add_getmoney( makeob1 )
manob.add_getmoney( makeob2 )
manob.add_getmoney( makeob3)

manob.add_givemoney( makeob4 )
manob.add_givemoney( makeob5 )
manob.add_givemoney( makeob6 )

while True :
    print("............................................................................")
    print("------------------------ Personal Money Management System ------------------")
    print("1: Show All Money I get from people")
    print("2: Show all money I have to give people")
    print("3: Edit a getting money entry")
    print("4: Edit a given money entry")
    print("5: Exit")
    print("............................................................................")
    inputVal = int(input("Enter your Input : "))
    if inputVal == 1 :
        manob.show_getmoneylist()
    elif inputVal == 2:
        manob.show_givemoneylist()
    elif inputVal == 3:
        data = input("Enter Name of person I get Money :")
        amount = input("New Amount : ")
        manob.edit_get_money( data, amount)
    elif inputVal == 4:
        data = input("Enter Name of person I have to give Money :")
        amount = input("New Amount : ")
        manob.edit_give_money( data, amount)

