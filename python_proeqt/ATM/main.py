import json
file_path = "bancomat.json"

bank =[
  {
    "pin": 1111,
    "name": "john",
    "balance": 2486.45
  },
  {
    "pin": 2222,
    "name": "Adam",
    "balance": 24.5
  },
  {
    "pin": 3333,
    "name": "Nia",
    "balance": 4586.25
  },
  {
    "pin": 4444,
    "name": "Selen",
    "balance": 486.55
  },
  {
    "pin": 5555,
    "name": "Nik",
    "balance": 565
  }
]


with open(file_path, mode="r", encoding="utf-8") as file:
    file_reader = json.load(file)

write_pin = int(input("enter your pin "))
write_money = 0

for data in  file_reader:
    if  data["pin"] == write_pin:
      #  write_money = 0
       balance = data["balance"]
       name = data["name"]

class Bancomat:
    def __init__(self, money):
       self.money = money
       self.balance = balance

    def  take_out(self):
       
           
        if self.money < self.balance:
            take_out_balance = self.balance - self.money
            return take_out_balance
           
        else:
            print("your balance is not enought..")
       
    def filing(self):
        filing_balance = self.balance + self.money
        return filing_balance
    
    def your_balance(self):
        see_balance = self.balance
        return see_balance

print("1 for balance")
print("2 for take out")
print("3 for filing")
print("4 for exit")






bank = Bancomat(write_money)
take_out_or_filing = 0

def banko():
  take_out_or_filing = 0

  while take_out_or_filing != 4:

    take_out_or_filing = int(input("... "))
    if take_out_or_filing == 1:
        bank = Bancomat(0)
        print(bank.your_balance())

    elif take_out_or_filing == 2:
        write_money = eval(input("enter money "))
        bank = Bancomat(write_money)
        
        for data in file_reader:
            if  data["pin"] == write_pin:
                data["balance"]  = bank.take_out()
        print(bank.take_out())
        
 
    elif take_out_or_filing == 3:
        write_money = eval(input("enter money "))
        bank = Bancomat(write_money)

        for data in file_reader:
            if  data["pin"] == write_pin:
                data["balance"]  = bank.filing()
        print(bank.filing())
    elif take_out_or_filing == 4:
      print("Good bye...")
      break
    else:
      print("Error...")

banko()

# for data in file_reader:
#     if  data["pin"] == write_pin:
#         data["balance"]  = bank.take_out()
#     else:
#         data["balance"]  = bank.filing()


def writer():
    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(file_reader, file, ensure_ascii=False, indent=2)

writer()
         



    