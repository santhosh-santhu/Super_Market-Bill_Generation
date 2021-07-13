from datetime import datetime

name = input("Enter customer name:")

#Here iam listing some  items
lists =''' 
Rice    Rs 55/kg
Sugar   Rs 30/kg
salt    Rs 10/kg
oil     Rs 110/ per liter
panner  Rs 210/kg
Maggi   Rs 50/kg
Boost   Rs 100/each
colgate Rs 25/each
'''

#declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist=[]#itemlist
qlist=[]#quantity list
plist=[]#pricelist

#rates for items
items={'Rice':55,'Sugar':30,'Salt':10,'oil':80,'panner':210,'maggi':50,'Boost':100,'colgate':25}

option = int(input("For list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity = int(input("Enter quanity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            #if we want to cut gst
            gst=(totalprice*5)/100
            finalamount = gst+totalprice
        else:
            print("Sorry,you entered item is not available ")
    else:
        print("Please enter the valid number")
    #To geneate the bill
    inp=input("can i bill the items y/n:")
    if inp=='y':
        pass
        if finalamount!=0:
            print(25*"=","World Supermarket",25*"=")
            print(28*" ","Ramanthapur")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",6*" ",'items',8*" ",'Quantity',8*" ","Price")
            for i in range(len(pricelist)):
                print(i,1*' ',8*' ',ilist[i],8*' ',qlist[i],8*"  ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:",'Rs',totalprice)
            print("Gst amount",30*" ",'Rs',totalprice)
            print(75*"-")
            print(50*" ",'finalamount','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting!Have a good day")
            print(75*"-")






            


    

