intro = "\nWelcome to Piece of Cake. We present you a wide assortment of \ndeliciously rich cakes that are infused with deep flavors. \n"
from tkinter import *
from tkinter import ttk
import random
import mysql.connector as mc
from PIL import ImageTk, Image 
screen = Tk()
screen.configure(bg = "LightPink1")
screen.wm_title("Piece of Cake")
w = str(screen.winfo_screenwidth())
w2 = screen.winfo_screenwidth()-25
h = str(screen.winfo_screenheight()+3000)
h2 = screen.winfo_screenheight()-10
screen.geometry(w+"x"+h)
screen.iconbitmap(r"cakeicon1.ico")

main_frame = Frame(screen)
main_frame.pack(fill = BOTH, expand = 1)

my_canvas = Canvas(main_frame)
my_canvas.configure(bg = "LightPink1")
my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

scroll = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
scroll.pack(side = RIGHT, fill = Y)

my_canvas.configure(yscrollcommand = scroll.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
my_canvas.configure(bg = "LightPink1")

def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

frame2 = Frame(my_canvas) 
frame2.configure(bg = "LightPink1")
my_canvas.create_window((0,0), window = frame2, height = h, width = w, anchor = "center")

valLst = ["","","","","","","","","","","","","","",""]

mycon=mc.connect(host="localhost", user="root",passwd="")
cursor=mycon.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS INVOICE")
cursor.execute("USE INVOICE")
mycon.commit()

try:
    cursor.execute("SELECT * FROM CUSTOMER")
except:
    cursor.execute('''CREATE TABLE CUSTOMER(
        OID INT(5) NOT NULL PRIMARY KEY,
        NAME VARCHAR(50),
        PHNO VARCHAR(11),
        EMAIL VARCHAR(50),
        ADDR VARCHAR(100),
        BASE VARCHAR(10),
        ICING VARCHAR(10),
        WEIGHT VARCHAR(5),
        TOPPING VARCHAR(20),
        OCCASION VARCHAR(20),
        SPECIALTY VARCHAR(20),
        QTY VARCHAR(3),
        PRICE INT(4),
        MOP VARCHAR(15),
        REQUIREMENTS VARCHAR(15)
        )''')
    mycon.commit()
    print("Table created.")
  
#functions
#Custom specific functions
def Custom():
    make = Label(frame2, text = "\nMake your Cake!", fg='#4a2512', bg='LightPink1')
    make.config(font = ("Lato",20))

    Base()
    Icing()
    WeightCustom()
    Topping()
    Occasion1()
    switch(spects)
    
    finCake = Button(frame2,text = "Finish Cake", fg = "black",bg = "#7BC1C3", command = getweightC)
    finCake.config(font = ("Lato",17))
    finCake.grid(row = 11, column = 1)
    make.grid(row = 5, column = 1, sticky = W)

def Base():
    base = Label(frame2, text = "Base Cake Flavour:", fg='#7e4816', bg='LightPink1')
    base.config(font = ("Lato",17))
    bFlavors = ["Chocolate", "Vanilla","Coffee","Red Velvet","Lemon","Marble"]
    global n
    n = StringVar()
    baseCake = OptionMenu(frame2,n,*bFlavors)
    baseCake.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    base.grid(row = 6, column = 1, sticky = W)
    baseCake.grid(row = 6, column = 1, sticky = E)

def Icing():
    icing = Label(frame2, text = "Icing Flavour:", fg='#7e4816', bg='LightPink1')
    icing.config(font = ("Lato",17))
    iFlavors = ["Chocolate","Vanilla","Mocha","Black Forest","Butter Cream","Strawberry Glaze"]
    global i
    i = StringVar()
    icingCake = OptionMenu(frame2,i,*iFlavors)
    icingCake.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    icing.grid(row = 7, column = 1, sticky = W)
    icingCake.grid(row = 7, column = 1, sticky = E)  

def WeightCustom():
    weight = Label(frame2, text = "Weight:", fg='#7e4816', bg='LightPink1')
    weight.config(font = ("Lato",17))
    weightLst = ["500 g","1 kg","2 kg","3 kg"]
    global w 
    w = StringVar(frame2)
    weightBox = OptionMenu(frame2,w,*weightLst)
    weightBox.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    weight.grid(row = 8, column = 1, sticky = W)
    weightBox.grid(row = 8, column = 1, sticky = E)

def Topping():
    top = Label(frame2, text = "Toppings:", fg='#7e4816', bg='LightPink1')
    top.config(font = ("Lato",17))

    topFlavors = ["None","Chocolate Shards","Sprinkles","Coffee","Powdered Sugar","Cocoa Powder","Cookies","Rock Candy","Fresh Fruit"]
    global t 
    t = StringVar()
    toppings = OptionMenu(frame2,t,*topFlavors)
    toppings.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    top.grid(row = 9, column = 1, sticky = W)
    toppings.grid(row = 9, column = 1, sticky = E)

def Occasion1():
    occ = Label(frame2, text = "Occasion:", fg='#7e4816', bg='LightPink1')
    occ.config(font = ("Lato",17))                         
    occLst = ["Birthday","Wedding","Party","Anniversary","Company Party","Christmas"]
    global j
    j = StringVar(frame2)   
    occmenu = OptionMenu(frame2,j,*occLst)
    occmenu.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    occ.grid(row = 10,column = 1,sticky = W)
    occmenu.grid(row = 10,column=1,sticky = E)

def getweightC():
    price = Label(frame2, text = "Price: ",fg = "#7e4816", bg = "LightPink1")
    price.configure(font = ("Lato",17))
    global wCho
    wCho = w.get()
    global top
    top = t.get()
    global pr
    pr = 0
    if wCho == "500 g":
        pr = 1000
    elif wCho == "1 kg":
        pr = 1300
    elif wCho == "2 kg":
        pr = 1700
    elif wCho == "3 kg":
        pr = 2000 
    else:
        pr = pr
    
    if top != "None":
        pr+=20
   
    req = Label(frame2, text = "Requirements:", fg = "#7e4816", bg = "LightPink1")
    req.configure(font = ("Lato",17)) 
    requirements = ["None","Vegan","Gluten Free","Sugar Free"]
    global z
    z = StringVar()
    require = OptionMenu(frame2, z, *requirements )
    require.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)

    sid7=IntVar()
    sid8 = IntVar()
    sid9 = IntVar()
    sid10 = IntVar()
    sid11 = IntVar()
    sid12 = IntVar()
    sides=Label(frame2, text='Party Equipment:',fg = "#7e4816", bg = "LightPink1")
    sides.configure(font = ("Lato",17))

    c0=Checkbutton(frame2,text="N/A",variable=sid7,onvalue = 1,offvalue = 0)
    c0.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c1=Checkbutton(frame2,text='Party hats',variable=sid8)
    c1.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c2=Checkbutton(frame2,text='Cake-cutting knives',variable=sid9)
    c2.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c3=Checkbutton(frame2,text='Banners',variable=sid10)
    c3.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c4=Checkbutton(frame2,text='Spoons',variable=sid11)
    c4.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c5=Checkbutton(frame2,text='Candles',variable=sid12)
    c5.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    
    sides.grid(row = 17, column = 1 , sticky = W)
    c0.grid(row = 18, column = 1, sticky = W)
    c1.grid(row = 19, column = 1, sticky = W)
    c2.grid(row = 20, column = 1, sticky = W)
    c3.grid(row = 21, column = 1, sticky = W)
    c4.grid(row = 22, column = 1, sticky = W)
    c5.grid(row = 23, column = 1, sticky = W)
    priceLab = Label(frame2,text = pr, fg = 'black', bg='LightPink1') 
    priceLab.config(font = ("Lato",17))
    price.grid(row = 15, column = 1, sticky = W)
    priceLab.grid(row = 15, column = 1,sticky = E) 
    req.grid(row = 16,column = 1,sticky = W)
    require.grid(row = 16,column = 1, sticky = E)
    global proceed
    proceed = Button(frame2,text = "Proceed", fg = "black",bg = "#7BC1C3", command = deliveryOptions)
    proceed.config(font = ("Lato",17))
    proceed.grid(row = 24, column = 1)
    changes = Label(frame2,text="*Disclaimer: You cannot make changes after this step.", fg = "red", bg = "LightPink1")
    changes.config(font = ("Lato",10))
    changes.grid(row = 25, column = 1)

#Specialties specific functions
def Specialties():
    intro_for_specialties = Label(frame2, text = "\nChoose your Cake!", fg='#4a2512', bg='LightPink1')
    intro_for_specialties.config(font = ("Lato",20))
    stype()
    WeightSpects()
    Quantity()
    Occasion2()
    switch(custom)
    Complete = Button(frame2,text = "Complete", fg = "black",bg = "#7BC1C3", command = getweightS)
    Complete.config(font = ("Lato",17))
    Complete.grid(row = 15, column = 1)

def stype():
    stypelab = Label(frame2, text='Specialty Type: ', fg = "#7e4816", bg = "LightPink1")
    stypelab.configure(font = ("Lato",17))  
    global var
    var = StringVar()
    
    cheesecake = Radiobutton(frame2, text="Cheesecake", variable = var, value=1, bg = "LightPink1") 
    cheesecake.configure(font = ("Lato",12)) 
    
    icecream = Radiobutton(frame2, text="Ice Cream Cake", variable = var, value=2, bg = "LightPink1")
    icecream.configure(font = ("Lato",12))  
    
    sponge = Radiobutton(frame2, text="Spongecake", variable = var,value=3, bg = "LightPink1")
    sponge.configure(font = ("Lato",12))
    gingerbread = Radiobutton(frame2, text="Gingerbread House", variable = var,value=4, bg = "LightPink1")
    gingerbread.configure(font = ("Lato",12)) 
    
    brownie = Radiobutton(frame2, text="Brownies", variable = var,value=5, bg = "LightPink1")
    brownie.configure(font = ("Lato",12)) 
    
    rainbow = Radiobutton(frame2, text="Rainbow Cake", variable = var,value=6, bg = "LightPink1")
    rainbow.configure(font = ("Lato",12))     
    
    stypelab.grid(row = 5, column = 1)
    cheesecake.grid(row = 6, column = 1)
    icecream.grid(row = 7, column = 1)
    sponge.grid(row = 8, column = 1)
    gingerbread.grid(row = 9, column = 1)
    brownie.grid(row = 10, column = 1)
    rainbow.grid(row = 11, column = 1)

def WeightSpects():
    global w2
    w2 = StringVar(frame2)

    weightLst2 = ["500 g","1 kg","2 kg","3 kg"]
    weightS = Label(frame2, text = "Weight:", fg='#7e4816', bg='LightPink1')
    weightS.config(font = ("Lato",17))
    
    weightBox2 = OptionMenu(frame2,w2,*weightLst2)
    weightBox2.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    
    weightS.grid(row = 12, column = 1, sticky = W)
    weightBox2.grid(row = 12, column = 1, sticky = E)

def Quantity():
    quantity = Label(frame2, text='Quantity:', fg = "#7e4816", bg = "LightPink1")
    quantity.configure(font = ("Lato",17))  
    quantitylist = [1,2,3,4,5]
    global n
    n = IntVar()
    quantitydrop = OptionMenu(frame2,n,*quantitylist)
    n.set(1)
    quantitydrop.configure(font = ("Lato",17), fg = 'black', bg = 'white', height = 1, width = 13, relief = FLAT)
    quantity.grid(row = 13, column = 1, sticky = W)
    quantitydrop.grid(row = 13, column = 1, sticky = E)  
 
def Occasion2():
    occ2 = Label(frame2, text = "Occasion:", fg='#7e4816', bg='LightPink1')
    occ2.config(font = ("Lato",17))                         
    occLst2 = ["Birthday","Wedding","Party","Anniversary","Company Party","Christmas"]
    global j2
    j2 = StringVar(frame2)   
    occmenu2 = OptionMenu(frame2,j2,*occLst2)
    occmenu2.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)
    occ2.grid(row = 14,column = 1,sticky = W)
    occmenu2.grid(row = 14,column = 1, sticky = E)
    
def getweightS():
    price = Label(frame2, text = "Price: ",fg = "#7e4816", bg = "LightPink1")
    price.configure(font = ("Lato",17))
    global wCho2
    wCho2 = w2.get()
    global quan
    quan = n.get()
    global pr2
    pr2 = 0
    if wCho2 == "500 g":
        pr2 = 1000
    elif wCho2 == "1 kg":
        pr2 = 1300
    elif wCho2 == "2 kg":
        pr2 = 1700
    elif wCho2 == "3 kg":
        pr2 = 2000 

    if quan == 1:
        pr2= pr2
    elif quan == 2:
        pr2=pr2*2
    elif quan == 3:
        pr2*=3
    elif quan == 4:
        pr2*=4
    elif quan == 5:
        pr2*=5    
    
    req = Label(frame2, text = "Requirements:", fg = "#7e4816", bg = "LightPink1")
    req.configure(font = ("Lato",17)) 
    requirements = ["None","Vegan","Gluten Free","Sugar Free"]
    global z
    z = StringVar()
    require = OptionMenu(frame2, z, *requirements )
    require.config(font = ("Lato",17), bg = "white",fg = "black", height = 1, width = 13, relief = FLAT)    
    
    priceLab = Label(frame2,text = pr2, fg = 'black', bg='LightPink1') 
    priceLab.config(font = ("Lato",17))
    price.grid(row = 16, column = 1, sticky = W)
    priceLab.grid(row = 16, column = 1, sticky = E) 
    req.grid(row = 17, column = 1, sticky = W)
    require.grid(row = 17, column = 1, sticky = E)

    sid1=IntVar()
    sid2 = IntVar()
    sid3 = IntVar()
    sid4 = IntVar()
    sid5 = IntVar()
    sid6 = IntVar()
    sides=Label(frame2, text='Party Equipment:',fg = "#7e4816", bg = "LightPink1")
    sides.grid(row = 18, column = 1 , sticky = W)
    sides.configure(font = ("Lato",17))

    c0=Checkbutton(frame2,text='None',variable=sid1)
    c0.grid(row = 19, column = 1, sticky = W)
    c0.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c1=Checkbutton(frame2,text='Party hats',variable=sid2)
    c1.grid(row = 20, column = 1, sticky = W)
    c1.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c2=Checkbutton(frame2,text='Cake-cutting knives',variable=sid3)
    c2.grid(row = 21, column = 1, sticky = W)
    c2.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c3=Checkbutton(frame2,text='Banners',variable=sid4)
    c3.grid(row = 22, column = 1, sticky = W)
    c3.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c4=Checkbutton(frame2,text='Spoons',variable=sid5)
    c4.grid(row = 23, column = 1, sticky = W)
    c4.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    c5=Checkbutton(frame2,text='Candles',variable=sid6)
    c5.grid(row = 24, column = 1, sticky = W)
    c5.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",14))
    global proceed
    proceed = Button(frame2,text = "Proceed", fg = "black",bg = "#7BC1C3", command = deliveryOptions)
    proceed.config(font = ("Lato",17))
    proceed.grid(row = 25, column = 1)
    changes = Label(frame2,text="*Disclaimer: You cannot make changes after this step.", fg = "red", bg = "LightPink1")
    changes.config(font = ("Lato",10))
    changes.grid(row = 26, column = 1)

#Common functions
def switch(a):
    a["state"] = DISABLED 


def callbackName(input1):
    if input1.isalpha():
        return True
    elif input1 is ' ':
        return True
    else:
        return False

def callbackNum(input2):
    if input2.isdigit():
        return True
    elif input2 is '':
        return True
    else:
        return False

def deliveryOptions():
    switch(proceed)
    global pickup
    pickup = Button(frame2, text = "I will Pick Up", fg='black',bg = "#7BC1C3", command = switch2)
    pickup.config(font = ("Lato", 13), height = 1, width = 10)
    global deliver
    deliver = Button(frame2, text = "Deliver to me",command=Delivery, fg='black',bg = "#7BC1C3")
    deliver.config(font = ("Lato", 13), height = 1, width = 10)
    
    info_label=Label(frame2, text='\nPlease enter your personal details:\n',fg='#7e4816', bg='LightPink1',width=30, height= 2)
    info_label.configure(font = ("Lato", 15, "underline"))


    cliName = Label(frame2, text='Name: ',fg='#7e4816', bg='LightPink1')
    cliName.configure(font = ("Lato",15))

    global name
    reg = frame2.register(callbackName)
    name = Entry(frame2, fg='gray9', bg='white')
    name.configure(font = ("Lato",15),validate = 'key',validatecommand = (reg,'%P'))

    cliNum = Label(frame2, text='Phone Number: ',fg='#7e4816', bg='LightPink1',)
    cliNum.configure(font = ("Lato",15))

    global phNo
    reg2 = frame2.register(callbackNum)
    phNo = Entry(frame2, fg='gray9', bg='white')
    phNo.configure(font = ("Lato",15),validate = 'key',validatecommand = (reg2,'%P'))

    cliEmail= Label(frame2, text='Email: ',fg='#7e4816', bg='LightPink1')
    cliEmail.configure(font = ("Lato",15))

    global email
    email = Entry(frame2, fg='gray9', bg='white')
    email.configure(font = ("Lato",15))
    emailadd = email.get()
    
    try:
        base = n.get()
        icing = i.get()
        valLst[5] = base
        valLst[6] = icing
        valLst[7] = wCho
        valLst[8] = top
        valLst[9] = j.get()
        valLst[10] = "N/A"
        valLst[11] = "N/A"
        valLst[12] = pr
        valLst[14] = z.get()
    except:
        specType = ""
        if var.get() == "1":
            specType = "Cheesecake"
        elif var.get() == "2":
            specType = "Ice Cream Cake"
        elif var.get() == "3":
            specType = "Spongecake"
        elif var.get() == "4":
            specType = "Gingerbread House"
        elif var.get() == "5":
            specType = "Brownies"
        elif var.get() == "6":
            specType = "Rainbow Cake"
            
        valLst[5] = "N/A"
        valLst[6] = "N/A"
        valLst[7] = wCho2
        valLst[8] = "N/A"
        valLst[9] = j2.get()
        valLst[10] = specType
        valLst[11] = quan
        valLst[12] = pr2  
        valLst[14] = z.get()
    
    pickup.grid(row = 27, column = 1)
    deliver.grid(row = 28, column = 1)
    info_label.grid(row = 29, column = 1)
    cliName.grid(row = 30, column = 1, sticky = W)
    name.grid(row = 30, column = 1, sticky = E)
    cliNum.grid(row = 31, column = 1, sticky = W)
    phNo.grid(row = 31, column = 1, sticky = E)
    cliEmail.grid(row = 32, column = 1, sticky = W)
    email.grid(row = 32, column = 1, sticky = E)

def switch2():
    switch(deliver)  
    propayment()  

def Delivery():
    cliAdd = Label(frame2, text='Delivery Address: ',fg='#7e4816', bg='LightPink1')
    cliAdd.configure(font = ("Lato",15))
        
    global add
    add = Text(frame2, fg='gray9', bg='white', height = 10, width = 20)
    add.configure(font = ("Lato",15))

    cliAdd.grid(row = 33, column = 1, sticky = NW)
    add.grid(row = 33, column = 1, sticky = E)
    propayment()
    switch(pickup)  

def propayment():
    global propayment1
    propayment1 = Button(frame2, text = "Proceed to Payment", fg='black',bg = "#7BC1C3", command = payment)
    propayment1.config(font = ("Lato", 13), height = 1, width = 20)
    propayment1.grid(row = 34, column = 1)

def payment():
    switch(propayment1)
    pay=Label(frame2, text='\n\nHow would you prefer to pay?\n\n',fg='#7e4816', bg='LightPink1',width=30, height= 2)
    pay.configure(font = ("Lato", 15))
    pay.grid(row = 35, column = 1)
    
    valLst[1] = name.get()
    valLst[2] = phNo.get()
    valLst[3] = email.get()
    
    try:
        valLst[4] = add.get("1.0",END)
    except: 
        valLst[4] = "N/A"
    
    global r
    r=IntVar()
    debitcard = Radiobutton(frame2, text ='Debit Card', variable=r, value=1,bg = "LightPink1",fg='#7e4816')
    debitcard.configure(font = ("Lato",12))
    
    global e1
    e1=Entry(frame2, width=30)
    e1.configure(font = ("Lato",12))

    creditcard = Radiobutton(frame2, text ='Credit Card', variable=r, value=2,bg = "LightPink1",fg='#7e4816')
    creditcard.configure(font = ("Lato",12))
    
    global e2
    e2=Entry(frame2, width=30)
    e2.configure(font = ("Lato",12))

    upi = Radiobutton(frame2, text ='UPI', variable=r, value=3,bg = "LightPink1",fg='#7e4816')
    upi.configure(font = ("Lato",12))
    
    global e3
    e3=Entry(frame2, width=30)
    e3.configure(font = ("Lato",12))

    cod = Radiobutton(frame2, text ='Cash', variable=r, value=4,bg = "LightPink1",fg='#7e4816')
    cod.configure(font = ("Lato",12))
    
    global finish
    finish = Button(frame2, text = "Finish", fg='black',bg = "#7BC1C3", command = end)
    finish.config(font = ("Lato", 13), height = 1, width = 10)
    finish["state"] = DISABLED
    
    checkbutton1 = IntVar()
    global TC
    TC = Checkbutton(frame2, text = "I agree to the Terms & Conditions", 
                      variable = checkbutton1, onvalue = 1, 
                      offvalue = 0,height = 2,width = 30,command = able) 
    TC.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",13))
    
    debitcard.grid(row = 36, column = 1)
    e1.grid(row = 37, column = 1)
    creditcard.grid(row = 38, column = 1)
    e2.grid(row = 39, column = 1)
    upi.grid(row = 40, column = 1)
    e3.grid(row = 41, column = 1)
    cod.grid(row = 42, column = 1)
    finish.grid(row = 44, column = 1)
    TC.grid(row=43,column=1)

def able():
    finish["state"] = NORMAL
    TC["state"] = DISABLED

def end():
    switch(finish)
    mylabel=Label(frame2, text='Thank you for shopping with us!!',fg='#7e4816', bg='LightPink1')
    mylabel.configure(font = ("Lato", 15))
    mylabel.grid(row = 45, column = 1)
    
    mylabel2 = Label(frame2,text = "You will receive you order in 5 days",fg='#7e4816', bg='LightPink1')
    mylabel2.configure(font = ("Lato", 15))
    mylabel2.grid(row = 46, column = 1)
    
    mop = r.get()
    Mop = ""
    if mop == 1:
        Mop = "Debit Card"
    elif mop == 2:
        Mop = "Credit Card"
    elif mop == 3:
        Mop = "UPI"
    elif mop == 4:
        Mop = "Cash"
    
    valLst[13] = Mop
    sValLst = str(valLst)
        
    button = Button(frame2, text = "Exit", fg='black',bg = "#7BC1C3",command = close_window)
    button.config(font = ("Lato", 13), height = 1, width = 10)
    button.grid(row = 48, column = 1 )
      
    intext = open("Invoice.txt","w")
    invLst = ["INVOICE \n","Order ID: "+str(valLst[0])+" \n",
              "Name: "+valLst[1]+" \n", "Phone Number: "+str(valLst[2])+" \n",
              "Email: "+valLst[3]+" \n","Address: "+valLst[4]+" \n",
              "Base: "+valLst[5]+" \n","Icing: "+valLst[6]+" \n",
              "Weight: "+valLst[7]+" \n","Toppings: "+valLst[8]+" \n",
              "Occasion: "+valLst[9]+" \n", "Specialty Type: "+valLst[10]+" \n", 
              "Quantity: "+str(valLst[11])+" \n","Price: "+str(valLst[12])+" \n",
              "Mode of Payment: "+valLst[13]+" \n","Requirements: "+valLst[14]]        
    intext.writelines(invLst)
    intext.close()
    
    intext = open("Invoice.txt","r")
    invoiceText = intext.read()
    invoiceLab = Label(frame2,text = invoiceText+"\n",fg='black', bg='white', relief = "groove")
    invoiceLab.configure(font = ("Arial", 10))
    invoiceLab.grid(row = 47,column = 1)
        
    fields = ["OID","NAME","PHNO","EMAIL","ADDR","BASE","ICING","WEIGHT",
          "TOPPING","OCCASION","SPECIALTY","QTY","PRICE",
          "MOP","REQUIREMENTS"]
    
    cursor.execute("INSERT INTO CUSTOMER(OID) VALUES("+str(valLst[0])+")")
    mycon.commit()
    for i in range(1,len(fields)):
        if type(valLst[i]) is str:
            cursor.execute("UPDATE CUSTOMER SET "+fields[i]+" = '"+valLst[i]+"' WHERE OID = "+str(valLst[0]))
            mycon.commit()
        elif type(valLst[i]) is int:
            cursor.execute("UPDATE CUSTOMER SET "+fields[i]+" = "+ str(valLst[i])+" WHERE OID = "+str(valLst[0]))    
            mycon.commit()
    
    admin = Button(frame2,text = "Admin",fg='black',bg = "#7BC1C3",command = new_window)
    admin.config(font = ("Lato", 13), height = 1, width = 10)
    admin.grid(row = 49, column = 1 )

def close_window (): 
    screen.destroy()

def new_window():
    close_window()
    
    global screen2
    screen2 = Tk()
    screen2.configure(bg = "LightPink1")
    screen2.wm_title("Piece of Cake Administrator")
    w = str(screen2.winfo_screenwidth())
    w2 = screen2.winfo_screenwidth()-25
    h = str(screen2.winfo_screenheight()+1000)
    h2 = screen2.winfo_screenheight()-10
    screen2.geometry(w+"x"+h)
    screen2.iconbitmap(r"cakeicon1.ico")

    main_frame2 = Frame(screen2)
    main_frame2.pack(fill = BOTH, expand = 1)
    
    global my_canvas2
    my_canvas2 = Canvas(main_frame2)
    my_canvas2.pack(side = LEFT,fill = BOTH, expand = 1)
    
    scroll2 = ttk.Scrollbar(main_frame2, orient = VERTICAL, command = my_canvas2.yview)
    scroll2.pack(side = RIGHT, fill = Y)
    
    my_canvas2.configure(yscrollcommand = scroll2.set)
    my_canvas2.bind("<Configure>", lambda e: my_canvas2.configure(scrollregion = my_canvas2.bbox("all")))
    my_canvas2.configure(bg = "LightPink1")

    my_canvas2.bind_all("<MouseWheel>", _on_mouse_wheel2)
    
    global frame3
    frame3 = Frame(my_canvas2) 
    frame3.configure(bg = "LightPink1")
    my_canvas2.create_window((0,0), window = frame3, height = h, width = w, anchor = "center")
    
    spaceBut2 = Button(frame3, text = "",fg = "LightPink1",bg = "LightPink1",relief = FLAT)
    spaceBut2.config(height = 1, width = 25)
    spaceBut2.grid(row = 0, column = 0)
    
    head1 = Label(frame3, text = "Piece of Cake", bg = "LightPink1", fg = "#4a2512")
    head1.configure(anchor = CENTER,font = ("Lato",25,"underline"))
    head1.grid(row = 0, column = 1)
    global pwdLab
    pwdLab = Label(frame3,text= "Password: ",fg='#7e4816', bg='LightPink1')
    pwdLab.configure(font = ("Lato", 15))
    pwdLab.grid(row = 1, column = 1, sticky = W)
    global pwdEnt
    pwdEnt = Entry(frame3,show = "*", fg='gray9', bg='white',width = 6)
    pwdEnt.configure(font = ("Lato",15))
    pwdEnt.grid(row = 1, column = 1, sticky = E)
    global pwdGet
    pwdGet = Button(frame3,text = "Submit",fg='black',bg = "#7BC1C3",command = password)
    pwdGet.config(font = ("Lato", 13), height = 1, width = 10)
    pwdGet.grid(row = 2, column = 1)
        
def exitBut():
    screen2.destroy()

def display1():
    confo.destroy()
    cursor.execute("SELECT * FROM CUSTOMER")
    global i
    i=10
    global totOrd 
    totOrd = []
    for student in cursor: 
        for j in range(len(student)):
            if j == 0:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i, column=j+1) 
                e.insert(END, student[j])
                totOrd.append(e)
            elif j == 1:
                e = Entry(frame3, width=18, fg='black',bg = "LightPink1") 
                e.grid(row=i, column=j+1) 
                e.insert(END, student[j])
                totOrd.append(e)
            elif j == 7:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i, column=j+1) 
                e.insert(END, student[j]) 
                totOrd.append(e)
            elif j == 11:
                e = Entry(frame3, width=5, fg='black',bg = "LightPink1") 
                e.grid(row=i, column=j+1) 
                e.insert(END, student[j]) 
                totOrd.append(e)
            elif j == 12:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i, column=j+1) 
                e.insert(END, student[j])
                totOrd.append(e)
            else:
                e = Entry(frame3, width=10, fg='black',bg = "LightPink1") 
                e.grid(row=i, column=j+1) 
                e.insert(END, student[j])
                totOrd.append(e)                   
        i=i+1

def getID():
    for b in serOrd:
        b.destroy()
        
    global oidLab
    oidLab = Label(frame3, text = "Order ID: ",fg='#7e4816', bg='LightPink1')
    oidLab.config(font = ("Lato",15))
    global oid
    oid = Entry(frame3, fg='gray9', bg='white',width = 6)
    oid.configure(font = ("Lato",15))    
    global pro
    pro = Button(frame3, text = "Show Order",fg='black',bg = "#7BC1C3",command = showOrd)
    pro.config(font = ("Lato", 13), height = 1, width = 13)
    
    oidLab.grid(row = i+1, column = 1, sticky = W)
    oid.grid(row = i+1, column = 1, sticky = E)
    pro.grid(row = i+2, column = 1)

def showOrd():
    global ID
    ID = oid.get()
    cursor.execute("SELECT * FROM CUSTOMER WHERE OID = "+ID)
    global selOrd
    selOrd = []
    for val in cursor:
        for j in range(len(val)):
            if j == 0:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i+3, column=j+1) 
                e.insert(END, val[j])
                selOrd.append(e)
            elif j == 1:
                e = Entry(frame3, width=18, fg='black',bg = "LightPink1") 
                e.grid(row=i+3, column=j+1) 
                e.insert(END, val[j]) 
                selOrd.append(e)
            elif j == 7:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i+3, column=j+1) 
                e.insert(END, val[j]) 
                selOrd.append(e)
            elif j == 11:
                e = Entry(frame3, width=5, fg='black',bg = "LightPink1") 
                e.grid(row=i+3, column=j+1) 
                e.insert(END, val[j]) 
                selOrd.append(e)
            elif j == 12:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i+3, column=j+1) 
                e.insert(END, val[j]) 
                selOrd.append(e)
            else:
                e = Entry(frame3, width=10, fg='black',bg = "LightPink1") 
                e.grid(row=i+3, column=j+1) 
                e.insert(END, val[j])  
                selOrd.append(e)
    global deleteBut
    deleteBut = Button(frame3, text = "Cancel",fg='black',bg = "#7BC1C3",command = delOrd)
    deleteBut.config(font = ("Lato", 13), height = 1, width = 13)
    deleteBut.grid(row = i+4, column = 1)

def search():
    confo.destroy()
    global oidLab2
    oidLab2 = Label(frame3, text = "Order ID: ",fg='#7e4816', bg='LightPink1')
    oidLab2.config(font = ("Lato",15))
    global oid2
    oid2 = Entry(frame3, fg='gray9', bg='white',width = 6)
    oid2.configure(font = ("Lato",15)) 
    global pro2
    pro2 = Button(frame3, text = "Show Order",fg='black',bg = "#7BC1C3",command = dispOrder)
    pro2.config(font = ("Lato", 13), height = 1, width = 13)
    
    oidLab2.grid(row = i+6 ,column = 1, sticky = W)
    oid2.grid(row = i+6, column = 1,sticky = E)
    pro2.grid(row = i+7, column = 1)
    
def dispOrder():
    global ID
    ID = oid2.get()
    cursor.execute("SELECT * FROM CUSTOMER WHERE OID = "+ID)
    global serOrd
    serOrd = []
    for val in cursor:
        for j in range(len(val)):
            if j == 0:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i+8, column=j+1) 
                e.insert(END, val[j])
                serOrd.append(e)
            elif j == 1:
                e = Entry(frame3, width=18, fg='black',bg = "LightPink1") 
                e.grid(row=i+8, column=j+1) 
                e.insert(END, val[j])
                serOrd.append(e)
            elif j == 7:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i+8, column=j+1) 
                e.insert(END, val[j]) 
                serOrd.append(e)
            elif j == 11:
                e = Entry(frame3, width=5, fg='black',bg = "LightPink1") 
                e.grid(row=i+8, column=j+1) 
                e.insert(END, val[j])
                serOrd.append(e)
            elif j == 12:
                e = Entry(frame3, width=6, fg='black',bg = "LightPink1") 
                e.grid(row=i+8, column=j+1) 
                e.insert(END, val[j]) 
                serOrd.append(e)
            else:
                e = Entry(frame3, width=10, fg='black',bg = "LightPink1") 
                e.grid(row=i+8, column=j+1) 
                e.insert(END, val[j]) 
                serOrd.append(e)

def destroy():
    for i in totOrd:
        i.destroy()
    oidLab.destroy()
    oid.destroy()
    pro.destroy()
    for a in selOrd:
        a.destroy()
    deleteBut.destroy()
    oidLab2.destroy()
    oid2.destroy()
    pro2.destroy()
    for b in serOrd:
        b.destroy()
   
def delOrd():
    cursor.execute("DELETE FROM CUSTOMER WHERE OID = "+ID)
    mycon.commit()     
    destroy()
    global confo
    confo = Label(frame3,text = "Your order has been canceled.")
    confo.config(fg='#7e4816', bg='LightPink1',font = ("Lato",15))
    confo.grid(row = 10, column = 1) 

def password():
    pwd = pwdEnt.get()
    if pwd == "quartz":
        mycon=mc.connect(host="localhost", user="root",passwd="")
        cursor=mycon.cursor(buffered=True)
        cursor.execute("USE INVOICE")
        pwdLab.destroy()
        pwdEnt.destroy()
        pwdGet.destroy() 
        
        global confo
        confo = Label(frame3,text = "  ")
        confo.config(fg='#7e4816', bg='LightPink1',font = ("Lato",15))
        confo.grid(row = 10, column = 1) 
        
        global disp
        disp = Button(frame3, text = "Display all Orders",fg='black',bg = "#7BC1C3",command=display1)
        disp.config(font = ("Lato", 13), height = 1, width = 13)
        
        global delete1
        delete1 = Button(frame3, text = "Cancel an Order",fg='black',bg = "#7BC1C3", command = getID)
        delete1.config(font = ("Lato", 13), height = 1, width = 13)
        
        searOrd = Button(frame3, text = "Search",fg='black',bg = "#7BC1C3",command = search)
        searOrd.config(font = ("Lato", 13), height = 1, width = 13)
        
        spaceBut = Button(frame3, text = "",fg = "LightPink1",bg = "LightPink1",relief = FLAT)
        spaceBut.config(height = 1, width = 25)
        
        spaceBut2 = Button(frame3, text = "",fg = "LightPink1",bg = "LightPink1",relief = FLAT)
        spaceBut2.config(height = 1, width = 25)
        
        exBut = Button(frame3, text = "Exit",fg='black',bg = "#7BC1C3", command = exitBut)
        exBut.config(font = ("Lato", 13), height = 1, width = 13)
        
        spaceBut2.grid(row = 4, column = 1)
        disp.grid(row = 5, column = 1)
        delete1.grid(row = 6, column = 1)
        searOrd.grid(row = 7, column = 1)
        exBut.grid(row = 8, column = 1)
        screen2.mainloop()
    else:
        errMess = Label(frame3,text = "Incorrect Password",bg = "LightPink1", fg = "#4a2512")
        errMess.configure(anchor = CENTER,font = ("Lato",15))
        errMess.grid(row = 4, column = 1)

def _on_mouse_wheel2(event):
    my_canvas2.yview_scroll(-1 * int((event.delta / 120)), "units")                

head = Label(frame2, text = "Piece of Cake", bg = "LightPink1", fg = "#4a2512")
head.configure(anchor = CENTER,font = ("Lato",35,"underline"))

introd = Label(frame2, text = intro, fg = "#7e4816", bg = "LightPink1")
introd.configure(anchor = CENTER,font = ("Lato",15))

space = Label(frame2, text = "sdgdfjgfhgfjhjgjgfugfwaugfsagsfjwagfjwgffjh",fg = "LightPink1", bg = "LightPink1")
space.configure(anchor = CENTER,font = ("Lato",15))

valLst[0] = random.randint(50000,99999)

img = Image.open("Choco.png") 
image = img.resize((280, 230), Image.ANTIALIAS) 
pic = ImageTk.PhotoImage(image)
panel = Label(frame2, image = pic)
panel.grid(row = 1,column = 0)

img2 = Image.open("Mango.png") 
image2 = img2.resize((280, 230), Image.ANTIALIAS) 
pic2 = ImageTk.PhotoImage(image2)
panel2 = Label(frame2, image = pic2)
panel2.grid(row = 3,column = 2)

img3 = Image.open("Valentine.png") 
image3 = img3.resize((280, 230), Image.ANTIALIAS) 
pic3 = ImageTk.PhotoImage(image3)
panel3 = Label(frame2, image = pic3)
panel3.grid(row = 4,column = 0)

img4 = Image.open("Harry.png") 
image4 = img4.resize((280, 230), Image.ANTIALIAS) 
pic4 = ImageTk.PhotoImage(image4)
panel4 = Label(frame2, image = pic4)
panel4.grid(row = 26,column = 2)

img5 = Image.open("Fruit.png") 
image5 = img5.resize((280, 230), Image.ANTIALIAS) 
pic5 = ImageTk.PhotoImage(image5)
panel5 = Label(frame2, image = pic5)
panel5.grid(row = 34,column = 0)

img6 = Image.open("Orange Donut.png") 
image6 = img6.resize((280, 230), Image.ANTIALIAS) 
pic6 = ImageTk.PhotoImage(image6)
panel6 = Label(frame2, image = pic6)
panel6.grid(row = 44,column = 2)

img7 = Image.open("Cat.png") 
image7 = img7.resize((280, 230), Image.ANTIALIAS) 
pic7 = ImageTk.PhotoImage(image7)
panel7 = Label(frame2, image = pic7)
panel7.grid(row = 47,column = 0)

Eoptions1=Label(frame2, text='Would you like to try one of our specialities?\nOr do you want to customize the cake?')
Eoptions1.config(fg = "#7e4816", bg = "LightPink1",anchor = CENTER,font = ("Lato",15))
custom=Button(frame2, text='Customize', command = Custom)
custom.config(fg = "black",bg = "#7BC1C3",font = ("Lato",14), width = 10)
spects=Button(frame2, text='Specialties', command = Specialties)
spects.config(fg = "black",bg = "#7BC1C3",font = ("Lato",14), width = 10)
contactInfo = Label(frame2,text = "Phone: +91 9876543210\tE-mail: contact@pieceofcake.com\nAddress: 11A/B Kumud Nagar, Pune")
contactInfo.config(fg = "#7e4816", bg = "LightPink1",font = ("Lato",10))
head.grid(row = 0, column = 1)
introd.grid(row = 1,column = 1)
space.grid(row = 1, column = 0)
Eoptions1.grid(row = 2, column = 1)
custom.grid(row = 3, column = 1)
spects.grid(row = 4, column = 1)

screen.mainloop()