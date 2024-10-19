
class MoneyManage :
    def __init__(self):
        self.getmoneylist = []
        self.givemoneylist = []
    def add_getmoney( self, makeob ):
        self.getmoneylist.append(makeob)
    def add_givemoney( self, makeob ):
        self.givemoneylist.append(makeob)
    def show_getmoneylist( self ):
        print("-------------------------------------------")
        print("*********** Show Get Money Lists **********")
        tot = 0
        for i in self.getmoneylist:
            print(f"{i.name}\t\t{i.amount}")
            tot += int(i.amount)
        print(f"---- Total : {tot} \t\t ")
        print("-------------------------------------------")
    def show_givemoneylist( self ):
        print("-------------------------------------------")
        print("*********** Show Give Money Lists **********")
        tot = 0
        for i in self.givemoneylist:
            print(f"{i.name}\t\t{i.amount}")
            tot += int(i.amount)
        print(f"---- Total : { tot } \t\t ")
        print("-------------------------------------------")
    def edit_get_money( self, name, amount ):
        print("-------------------------------------------")
        for i in self.getmoneylist :
            if i.name == name :
                i.amount = amount
                print("New Amount Added")
        print("-------------------------------------------")
    def edit_give_money( self, name, amount ):
        print("-------------------------------------------")
        for i in self.givemoneylist :
            if i.name == name :
                i.amount = amount
                print("New Amount Added")
        print("-------------------------------------------")
        