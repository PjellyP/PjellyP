
class mouse:
 

    mouse1="bloody"
    mouse2="razzer"
    mouse3="logitech"
    mouse4="tesco"
 
    def __init__(self,name,colour,country,typer):
     self.name = name
     self.colour = colour
     self.country = country
     self.typer = typer

A61_by = mouse("A61_by","black","argentina","gaming")
viper_mini = mouse("viper_mini","green","America","gaming")
signature_M650 = mouse("signature_M650","white","switzerland","office")
Gm_2025= mouse("Gm_2025","RGB","iran","gaming")

print("company of A61 is {}".format(A61_by.__class__.mouse1))
print("company of viper is {}".format(viper_mini.__class__.mouse2))
print("company of signature is {}".format(signature_M650.__class__.mouse3))
print("company of Gm is {}".format(Gm_2025.__class__.mouse4))

print("the color of {} is {} and from {} and this mouse is {}".format(A61_by.name,A61_by.colour,A61_by.country,A61_by.typer))
print("the color of {} is {} and from {} and this mouse is {}".format(viper_mini.name,viper_mini.colour,viper_mini.country,viper_mini.typer))
print("the color of {} is {} and from {} and this mouse is {}".format(signature_M650.name,signature_M650.colour,signature_M650.country,signature_M650.typer))
print("the color of {} is {} and from {} and this mouse is {}".format(Gm_2025.name,Gm_2025.colour,Gm_2025.country,Gm_2025.typer))


class price:
    
    def __init__(self):
        self.__price= 50

    def sell(self):
        print("selling price is:{}$".format(self.__price))
    def setprice(self,price):
        self.__price=price
c = price()
c.sell()
c.setprice(20.75)
c.sell()
c.setprice(35.94)
c.sell()    
c.setprice(18.51)
c.sell()


class Gm_2025:


    def dpi(self):
        print("Gm_2025's max dpi in this mouse has 3200dpi")

    def number_of_clicks(self):
        print("Gm_2025's number of clicks in this mouse  has 8 number clicks")

    def scroll(self):
        print("tesco has bad scroll")

class A61:

    def dpi(self):
        print("A61's max dpi in this mouse has over than 3200dpi")

    def number_of_clicks(self):
        print("A61's number of clicks in this mouse has 8 number clicks")

    def scroll(self):
        print("bloody has great scroll")

def dpi_test(mouse):
    mouse.dpi()
def number_of_clicks_test(mouse):
    mouse.number_of_clicks()
def scroll_test(mouse):
    mouse.scroll()

A = A61()
G = Gm_2025()

dpi_test(A)
dpi_test(G)
number_of_clicks_test(A)
number_of_clicks_test(G)
scroll_test(A)
scroll_test(G)