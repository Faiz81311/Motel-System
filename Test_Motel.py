import pandas as pd
import mysql.connector as sql

conn = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
    database = 'motel'
)

if conn.is_connected():
    print('successfully connected')



p = True
while p is True:
    
    
    
    def menu():
        print("1.  About The Project")
        print("2.  Create table Customer")
        print("3.  Show all customers details")
        print("4.  Add new customer detail")
        print("5.  Create table roomtype")
        print("6.  Add roomtype")
        print("7.  Show roomtypes")
        print("8.  Ask customers choice of room and calculate charge according to stay ")
        print("9.  Create table laundry")
        print("10. Add details of items and charge in laundry")
        print("11. Show laundry menu")
        print("12. Laundry bill")
        print("13. Create table game")
        print("14. Add details of games and the charges")
        print("15. Show all game list")
        print("16. Game bill")
        print("17. Create table restaurant")
        print("18. Add details of food items available in restaurant")
        print("19. Show menu of restaurant")
        print("20. Restaurant bill")
        print("21. Search details of a customer by customer mobile number")
        print("22. Remove a customer")
        print("23. Exit program")


    menu()


    #1
    def about():
        print("Motel Management Programe")

    #2
    def create_customer():
        c1 = conn.cursor()
        c1.execute("create table customer(name varchar(25),address varchar(25),mobile int(50),checkin date,checkout date)")
        print('Table customer created')
 
    #3
    def show_customer():
        print("All records of customers")
        df = pd.read_sql("select * from customer",conn)
        print(df)

    #4
    def add_customer():
        c1 = conn.cursor()
        L = []
        name = input("enter name :")
        L.append(name)
        address = input("enter address :")
        L.append(address)
        mobile = input('enter mobile :')
        L.append(mobile)
        checkin = input('enter check-in date : ')
        L.append(checkin)
        checkout = input('enter check-out date :')
        L.append(checkout)
        cust = (L)
        sql = "insert into customer(name,address,mobile,checkin,checkout)values(%s,%s,%s,%s,%s)"
        c1.execute(sql,cust)
        conn.commit()
        print('Record of customer inserted')

    #5
    def create_roomtype():
        c1 = conn.cursor()
        c1.execute("create table roomtype(sno int(5),type varchar(25),rent int(11))")
        print('Table roomtype created')

    #6
    def add_roomtype():
        c1 = conn.cursor()
        df = pd.read_sql("select * from roomtype",conn)
        print(df)
        L = []
        sno = input("enter roomtype no. :")
        L.append(sno)
        type = input("enter roomtype :")
        L.append(type)
        rent = input('enter rent :')
        L.append(rent)
        rt = (L)
        sql = "insert into roomtype(sno,type,rent)values(%s,%s,%s)"
        c1.execute(sql,rt)
        conn.commit()
        print("roomtype inserted")

    #7
    def show_roomtype():
        print("All records of type rooms available")
        df = pd.read_sql("select * from roomtype",conn)
        print(df)
    
    #8
    def roomrent():
        df = pd.read_sql("select * from roomtype",conn)
        print(df)
        x = int(input("Enter your choice :"))
        n = int(input("How many nights will you be satying"))
        if x == 1:
            print("You have chosen Single room ")
            s = 2000*n
        elif x == 2:
            print("You have chosen Double room ")
            s = 3000*n
        elif x == 3:
            print("You have chosen Triple room ")
            s = 4000*n
        elif x == 4:
            print("You have chosen King room ")
            s = 6000*n
        else:
            print("Please choose a room")
        print("Your rent is ",s)

    #9
    def create_laundry():
        c1 = conn.cursor()
        c1.execute("create table laundry(sno int(5),itemname varchar(25),rate int(11))")
        print("table laundry created")

    #10
    def add_laundry():
        c1 = conn.cursor()
        df = pd.read_sql("select * from laundry",conn)
        print(df)
        L = []
        sno = input("enter dress item serial no. :")
        L.append(sno)
        itemname = input("enter itemname to be washed :")
        L.append(itemname)
        rate = input('enter rate per piece :')
        L.append(rate)
        laun = (L)
        sql = "insert into laundry(sno,itemname,rate)values(%s,%s,%s)"
        c1.execute(sql,laun)
        conn.commit()
        print("Record inserted")

    #11
    def laundrymenu():
        print("All records of laundry")
        df = pd.read_sql("select * from laundry",conn)
        print(df)

    #12
    def lbill():
        global s
        df = pd.read_sql("select * from laundry",conn)
        print(df)
        x = int(input("Enter your choice :"))
        n = int(input("How many shits you want to get washed"))
        if x == 1:
            print("you want to get")
            s = 75*n
        elif x == 2:
            print("you want to get")
            s = 100*n
        elif x == 3:
            print("you want to get")
            s = 150*n
        elif x == 4:
            print("you want to get")
            s = 170*n
        elif x == 5:
            print("you want to get")
            s = 200*n
        else:
            print("Invalid option")
        print("your laundry charge is Rs ",s)
        return s

    #13
    def create_game():
        c1 = conn.cursor()
        c1.execute("create table game(sno int(11),gamename varchar(25),charges int(11))")
        print("table game created")

    #14
    def add_game():
        c1 = conn.cursor()
        df = pd.read_sql("select * from game",conn)
        print(df)
        L = []
        sno = input("enter game no. :")
        L.append(sno)
        gamename = input("enter game name :")
        L.append(gamename)
        charges = input('enter charges :')
        L.append(charges)
        game = (L)
        sql = "insert into game(sno,gamename,charges)values(%s,%s,%s)"
        c1.execute(sql,game)
        conn.commit()
        print("Game inserted")

    #15
    def show_game():
        print("All games available")
        df = pd.read_sql("select * from game",conn)
        print(df)

    #16
    def gamebill():
        df = pd.read_sql("select * from game",conn)
        print(df)
        g = int(input("enter choice for game : "))
        if g == 1:
            h = int(input("no. of hrs :"))
            s = 600*h
        elif g == 2:
            h = int(input("no. of hrs :"))
            s = 800*h
        elif g == 3:
            h = int(input("no. of hrs :"))
            s = 700*h
        elif g == 4:
            h = int(input("no. of hrs :"))
            s = 500*h
        else:
            print("Invalid option")
        print("Total game bill ",s)

    #17
    def create_restaurant():
        c1 = conn.cursor()
        c1.execute("create table restaurant(sno int(5),itemname varchar(25),rate int(11))")
        print("Restaurant table created")

    #18
    def add_restaurant():
        c1 = conn.cursor()
        df = pd.read_sql("select * from restaurant",conn)
        print(df)
        L = []
        sno = input("enter food item no. :")
        L.append(sno)
        itemname = input("enter itemname name :")
        L.append(itemname)
        charges = input('enter charges :')
        L.append(charges)
        f = (L)
        sql = "insert into restaurant(sno,itemname,rate)values(%s,%s,%s)"
        c1.execute(sql,f)
        conn.commit()
        print("Food item insert")

    #19
    def show_restaurant():
        df = pd.read_sql('select * from restaurant',conn)
        print(df)

    #20
    def restaurantbill():
        print("All food available")
        df = pd.read_sql("select * from restaurant",conn)
        print(df)
        c = int(input("Order your item no. :"))
        d = int(input("enter the quantity :"))
        if  c == 1:
            s = 200*d
        elif c == 2:
            s = 250*d
        elif c == 3:
            s = 60*d
        elif c == 4:
            s = 80*d
        elif c == 5:
            s = 90*d
        else:
            print("Inalid option")
        print("total food bill = Rs %s"%s)

    #21
    def search_bycustmob():
        print('All the customers are :-')
        df = pd.read_sql("select * from customer",conn)
        print(df)
        print('search details of a customer by customer mobile number ')
        a = input('Enter customer mobile number :')
        qry = 'select * from customer where mobile=%s;'%(a,)
        df = pd.read_sql(qry,conn)
        print(df)

    #22
    def del_cust():
        print('All the customers are :-')
        df = pd.read_sql("select * from customer",conn)
        print(df)
        c1 = conn.cursor()
        h = input("Enter customer name to be removed :")
        c1.execute("delete from customer where name='%s'"%h)
        df = pd.read_sql("select * from customer",conn)
        print(df)
        conn.commit()


    opt= int(input('enter your choice :'))
    if opt == 1:
        about()
    elif opt == 2:
        create_customer()
    elif opt == 3:
        show_customer()
    elif opt == 4:
        add_customer()
    elif opt == 5:
        create_roomtype()
    elif opt == 6:
        add_roomtype()
    elif opt == 7:
        show_roomtype()
    elif opt == 8:
        roomrent()
    elif opt == 9:
        create_laundry()
    elif opt == 10:
        add_laundry()
    elif opt == 11:
        laundrymenu()
    elif opt == 12:
        lbill()
    elif opt == 13:
        create_game()  
    elif opt == 14:
        add_game()
    elif opt == 15:
        show_game()
    elif opt == 16:
        gamebill()
    elif opt == 17:
        create_restaurant()
    elif opt == 18:
        add_restaurant()
    elif opt == 19:
        show_restaurant()
    elif opt == 20:
        restaurantbill()
    elif opt == 21:
        search_bycustmob()
    elif opt == 22:
        del_cust()
    elif opt == 23:
        p = False
    else:
        print('Invalid option')


