import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar

class HotelReservationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Luxury Hotels and Resorts | Anantara Hotels, Resorts")
        self.root.configure(bg="#F0F0FF")
        
        self.create_main_window()
        self.root.mainloop()
        
#For creating main window
#Creating the image background
        
    def create_main_window(self):
        self.frame = Frame(self.root, width=700, height=500)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)
        self.img = ImageTk.PhotoImage(Image.open("anantaraJPG.jpg"))
        self.label = Label(self.frame, image=self.img)
        self.label.pack()
        
# Labelling and packing

        i1 = Label(self.root, text="ANANTARA", bg="#83838B", fg="white", font=('Dotum', 25))
        i2 = Label(self.root, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i1.pack(fill="x")
        i2.pack(fill="x")
        
#Creating Frames for login and Signup
        
        self.frame = Frame(self.root)
        self.frame.pack(side="right", anchor="ne")
        bf = Frame(self.root)
        bf2 = Frame(self.root)
        bf2.pack(side="bottom", anchor="sw")
        bf3 = Frame(self.root)
        bf3.pack(side="bottom", anchor="sw")
        bf.pack(side="bottom")
        bf1 = Frame(self.root)
        bf1.pack(side="bottom", anchor="sw")
        bottomframe = Frame(self.root)
        bottomframe.pack(side="bottom", anchor="se")
        
#Creating frames button for bottom
        
        i5 = Label(bf, text="© 2023 Anantara Hotels, Resorts & Spas", bg="white")
        i5.pack(side="left")
        i6 = Button(bottomframe, text="Privacy Statement", bg="white")
        i6.pack(side=RIGHT)
        i7 = Button(bottomframe, text="Cookie Policy", bg="white")
        i7.pack(side=RIGHT)
        i8 = Button(bottomframe, text="Terms and Conditions ", bg="white")
        i8.pack(side=RIGHT)
        i9 = Label(bf1, text="ANY QUESTIONS?", bg="white")
        i9.pack(side="left")
        i12 = Label(bf2, text="Contact Number: +66 2 365 9110", bg="white")
        i12.pack(side="left")
        i12 = Label(bf3, text="Email us: reserveanantara@anantara.com", bg="white")
        i12.pack(side="left")

        
        
# # Creating Signup page

        # Declaration of input values
        Firstname = StringVar()
        LastName = StringVar()
        phoneNumber = IntVar()
        Email = StringVar()
        createpassword = StringVar()
        confirmpassword = StringVar()

        def database():
            Fname = Firstname.get()
            Lname = LastName.get()
            number = phoneNumber.get()
            email = Email.get()
            createpass = createpassword.get()
            confirmpass = confirmpassword.get()
            if not Fname or not Lname or not number or not email or not createpass or not confirmpass:
                messagebox.showerror('Error', 'All fields are required.')
                return
            if createpass != confirmpass:
                messagebox.showerror('Error', 'Passwords do not match.')
                return

            conn = sqlite3.connect('SELF.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS SIGNUP(Firstname text,LastName text,phoneNumber INTEGER,Email text,createpassword text,confirmpassword text)")
                cursor.execute('INSERT INTO SIGNUP(Firstname,LastName,phoneNumber,Email,createpassword,confirmpassword)values(?,?,?,?,?,?)',(Fname,Lname,number,email,createpass,confirmpass))
                cursor.execute('SELECT * FROM SIGNUP')
                # Fetch and print all rows
                rows = cursor.fetchall()

                # Print results
                for row in rows:
                    print(row)

            conn.commit()
            messagebox.showinfo('Information','Sign-in successfully')

        c1 = Label(self.root, text="First Name*").place(x=120, y=300)
        c2 = Label(self.root, text="Last Name*").place(x=120, y=350)
        c3 = Label(self.root, text="Phone Number*").place(x=120, y=400)
        c4 = Label(self.root, text="Email*").place(x=120, y=450)
        c5 = Label(self.root, text="Create Password*").place(x=120, y=500)
        c6 = Label(self.root, text="Confirm Password*").place(x=120, y=550)
        
        ce1 = Entry(self.root, textvar=Firstname, bd=3)
        ce1.place(x=280, y=300)
        ce2 = Entry(self.root, textvar=LastName, bd=3)
        ce2.place(x=280, y=350)
        ce3 = Entry(self.root, textvar=phoneNumber, bd=3)
        ce3.place(x=280, y=400)
        ce4 = Entry(self.root, textvar=Email, bd=3)
        ce4.place(x=280, y=450)
        ce5 = Entry(self.root, textvar=createpassword, bd=3,show='*')
        ce5.place(x=280, y=500)
        ce6 = Entry(self.root, textvar=confirmpassword, bd=3,show='*')
        ce6.place(x=280, y=550)
        
    #SignIn Submit Button
        ce3 = Button(self.root, text="SUBMIT", command=database, font=('Dotum', 10))
        ce3.place(x=280, y=600)
        
#login
        def LOGin():
            x = e1.get()
            y = e2.get()

            if x == "" or y == "":
                messagebox.showinfo('message', "Fill the Email and Password")
                return

            # Connect to SQLite database
            conn = sqlite3.connect("SELF.db")  # Ensure your DB file is named correctly
            cursor = conn.cursor()

            # Fetch user from database
            cursor.execute("SELECT * FROM SIGNUP WHERE Email=? AND createpassword=?", (x, y))
            user = cursor.fetchone()

            conn.close()  # Close connection

            if user:
                messagebox.showinfo('message', "Login Successful")
                self.current_user = user  # Store logged-in user
                self.hotel_log()  # Call the hotel_log function

            else:
                messagebox.showerror('error', "Invalid Email or Password")

        L1 = Label(self.root, text="Email").place(x=1320, y=380)
        L2 = Label(self.root, text="Password").place(x=1320, y=440)
        e1 = Entry(self.root, bd=3)
        e1.place(x=1420, y=380)
        e2 = Entry(self.root, bd=3, show='*')
        e2.place(x=1420, y=440)

        # Login page submit button
        ce20 = Button(self.root, text="SUBMIT", command=LOGin)
        ce20.place(x=1450, y=500)

    def logout(self) :
        for widgets in self.root.winfo_children():
            widgets.destroy()
        self.create_main_window()

    def hotel_log(self, previous_window=1):
        # Clear existing widgets from main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Reuse main window
        d = self.root
        d.geometry("1600x800")
        d.title("Anantara Fares Maldives Resort")
        d.configure(bg="#F0F0FF")


# Label Widget
        b = Label(d, bg="#F0F0FF", bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)
# Label Widget
        a = Label(d, bg="#F0F0FF", bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)
# Labelling and packing Room 1
        i10 = Label(d, text="ANANTARA", bg="#83838B", fg="white", font=('Dotum', 25))
        i11 = Label(d, text="Maldives Resort", fg="white", bg="#83838B", font=('Dotum', 12))
        welcome_label = Label(d, text=f"Hello {self.current_user[0]} {self.current_user[1]}", 
                                bg="#83838B", fg="white", font=('Dotum', 14))
        i10.pack(fill="x")
        i11.pack(fill="x")
        welcome_label.pack(fill="x")
        
        # Add logout and order list buttons
        logout_btn = Button(d, text="Logout", command=self.logout, bg="white")
        logout_btn.place(x=1500, y=20)
        order_list_btn = Button(d, text="Order List", command=self.show_orders, bg="white")
        order_list_btn.place(x=1400, y=20)



        i30 = Label(d, text="BEACH POOL VILLA", font=('Dotum', 22, 'bold'))
        i30.place(x=430, y=120)

        image = Image.open("pool.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(d, image=test)
        labell.image = test
        labell.place(x=70, y=120)

        i31 = Label(d, text="*Best Flexible with Breakfast and Dinner", font=('Dotum', 10, 'bold'), bg="#F0F0FF")
        i31.place(x=430, y=170)

        i32=Label(d,text="*Two meals included",font=('Dotum',10),bg="#F0F0FF")
        i32.place(x=430,y=210)

        i33=Label(d,text="*Non-refundable",font=('Dotum',10,'bold'),bg="#F0F0FF")
        i33.place(x=430,y=250)

        i34=Label(d,text="*Children stay for free",font=('Dotum',10),bg="#F0F0FF")
        i34.place(x=430,y=290)

        i35=Label(d,text="- FREE WIFI",font=('Dotum',10),bg="#F0F0FF")
        i35.place(x=70,y=380)

        i36=Label(d,text="- ROOM SIZE 258 M.sq / 2,776 FT.sq",font=('Dotum',10),bg="#F0F0FF")
        i36.place(x=70,y=410)

        i37=Label(d,text="- MAXIMUM 3 ADULTS",font=('Dotum',10),bg="#F0F0FF")
        i37.place(x=70,y=440)



        i38 = Label(d, text="- IN-VILLA BUTLER SERVICE", font=('Dotum', 10), bg="#F0F0FF")
        i38.place(x=70, y=470)

        image = Image.open("Rate-1.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(d, image=test)
        labell.image = test
        labell.place(x=450, y=380)

# Labelling and packing "Room 2"

        i30=Label(d,text="SEA VIEW VILLA",font=('Dotum',22,'bold'))
        i30.place(x=1180,y=120)
    
        image = Image.open("sv_room.jpg")
        test=ImageTk.PhotoImage(image)
        labell=Label(d,image=test)
        labell.image=test
        labell.place(x=820,y=120)

        i31=Label(d,text="*Best Flexible with Breakfast and Dinner",font=('Dotum',10,'bold'),bg="#F0F0FF")
        i31.place(x=1180,y=170)

        i32=Label(d,text="*Two meals included",font=('Dotum',10),bg="#F0F0FF")
        i32.place(x=1180,y=210)

        i33=Label(d,text="*Non-refundable",font=('Dotum',10,'bold'),bg="#F0F0FF")
        i33.place(x=1180,y=250)

        i34=Label(d,text="*Children stay for free",font=('Dotum',10),bg="#F0F0FF")
        i34.place(x=1180,y=290)

        i35=Label(d,text="- FREE WIFI",font=('Dotum',10),bg="#F0F0FF")
        i35.place(x=820,y=380)

        i36=Label(d,text="- ROOM SIZE 258 M.sq / 2,776 FT.sq",font=('Dotum',10),bg="#F0F0FF")
        i36.place(x=820,y=410)

        i37=Label(d,text="- MAXIMUM 3 ADULTS",font=('Dotum',10),bg="#F0F0FF")
        i37.place(x=820,y=440)

        i38=Label(d,text="- IN-VILLA BUTLER SERVICE",font=('Dotum',10),bg="#F0F0FF")
        i38.place(x=820,y=470)

        


        image = Image.open("Rate-2.jpg")
        test=ImageTk.PhotoImage(image)
        labell=Label(d,image=test)
        labell.image=test
        labell.place(x=1200,y=380)

                



        def hotel_log_A():
            f = Toplevel()
            f.geometry("1600x800")
            f.title("Anantara Fares Maldives Resort")
            f.configure(bg="#F0F0FF")
# Label Widget
            b = Label(f, bg="#F0F0FF", bd=2, relief=RIDGE)
            b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)
# Label Widget
            a = Label(f, bg="#F0F0FF", bd=2, relief=RIDGE)
            a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)
# Labelling and packing Room 1
            i101 = Label(f, text="ANANTARA", bg="#83838B", fg="white", font=('Dotum', 25))
            i111 = Label(f, text="Maldives Resort", fg="white", bg="#83838B", font=('Dotum', 12))
            i101.pack(fill="x")
            i111.pack(fill="x")

            i301 = Label(f, text="Over Water Pool Villa", font=('Dotum', 22, 'bold'))
            i301.place(x=430, y=120)

            image = Image.open("Pool_Villa.jpg")
            test = ImageTk.PhotoImage(image)
            labell1 = Label(f, image=test)
            labell1.image = test
            labell1.place(x=70, y=120)

            i311 = Label(f, text="*Best Flexible with Breakfast and Dinner", font=('Dotum', 10, 'bold'), bg="#F0F0FF")
            i311.place(x=430, y=170)

            i321=Label(f,text="*Two meals included",font=('Dotum',10),bg="#F0F0FF")
            i321.place(x=430,y=210)

            i331=Label(f,text="*Non-refundable",font=('Dotum',10,'bold'),bg="#F0F0FF")
            i331.place(x=430,y=250)

            i341=Label(f,text="*Children stay for free",font=('Dotum',10),bg="#F0F0FF")
            i341.place(x=430,y=290)

            i351=Label(f,text="- FREE WIFI",font=('Dotum',10),bg="#F0F0FF")
            i351.place(x=70,y=380)

            i361=Label(f,text="- ROOM SIZE 267 M.sq / 2,873 FT.sq",font=('Dotum',10),bg="#F0F0FF")
            i361.place(x=70,y=410)

            i371=Label(f,text="- MAXIMUM 3 ADULTS",font=('Dotum',10),bg="#F0F0FF")
            i371.place(x=70,y=440)



            i381 = Label(f, text="- IN-VILLA BUTLER SERVICE", font=('Dotum', 10), bg="#F0F0FF")
            i381.place(x=70, y=470)

            image = Image.open("Rate-3.jpg")
            test = ImageTk.PhotoImage(image)
            labell1 = Label(f, image=test)
            labell1.image = test
            labell1.place(x=450, y=380)

# Labelling and packing "Room 2"

            i301=Label(f,text="Two Bedroom HOUSE",font=('Dotum',22,'bold'))
            i301.place(x=1180,y=120)
    
            image = Image.open("bedroom.jpg")
            test=ImageTk.PhotoImage(image)
            labell1=Label(f,image=test)
            labell1.image=test
            labell1.place(x=820,y=120)

            i311=Label(f,text="*Best Flexible with Breakfast and Dinner",font=('Dotum',10,'bold'),bg="#F0F0FF")
            i311.place(x=1180,y=170)

            i321=Label(f,text="*Two meals included",font=('Dotum',10),bg="#F0F0FF")
            i321.place(x=1180,y=210)

            i331=Label(f,text="*Non-refundable",font=('Dotum',10,'bold'),bg="#F0F0FF")
            i331.place(x=1180,y=250)
    
            i341=Label(f,text="*Children stay for free",font=('Dotum',10),bg="#F0F0FF")
            i341.place(x=1180,y=290)

            i351=Label(f,text="- FREE WIFI",font=('Dotum',10),bg="#F0F0FF")
            i351.place(x=820,y=380)

            i361=Label(f,text="- ROOM SIZE 1500 M.sq / 16,140 FT.sq",font=('Dotum',10),bg="#F0F0FF")
            i361.place(x=820,y=410)

            i371=Label(f,text="- MAXIMUM 6 ADULTS",font=('Dotum',10),bg="#F0F0FF")
            i371.place(x=820,y=440)

            i381=Label(f,text="- IN-VILLA BUTLER SERVICE",font=('Dotum',10),bg="#F0F0FF")
            i381.place(x=820,y=470)

        


            image = Image.open("Rate-4.jpg")
            test=ImageTk.PhotoImage(image)
            label1l=Label(f,image=test)
            label1l.image=test
            label1l.place(x=1200,y=380)

            ce30 = Button(f, text="BOOK NOW", command=book, font=('Dotum', 14, 'bold'))
            ce30.place(x=500, y=550)

# Book now button for Room 2
            ce30 = Button(f, text="BOOK NOW", command=book, font=('Dotum', 14, 'bold'))
            ce30.place(x=1250, y=550)

            ce600 = Button(f, text="<<", command=lambda: self.hotel_log(f), font=('Dotum', 10))
            ce600.pack(side="left")

            def go_back(self):
                # Clear current view and recreate login screen
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.create_main_window()

        


        def book():
            # Clear existing widgets
            for widget in self.root.winfo_children():
                widget.destroy()
            
            # Reuse main window for booking
            e = self.root
            e.geometry("1600x800")
            e.title("BOOKING PAGE")
            e.configure(bg="#F0F0FF")


            
            # Labelling and packing
            i51 = Label(e, text="ANANTARA", bg="#83838B", fg="white", font=('Dotum', 25))
            i52 = Label(e, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
            i51.pack(fill="x")
            i52.pack(fill="x")

            i39 = Label(e, text="Your Booking Details", font=('Dotum', 22))
            i39.place(x=620, y=120)

            NIGHTS = IntVar()
            ADULTS = IntVar()
            ROOMS = IntVar()
            CHECK_IN = StringVar()
            CHECK_OUT = StringVar()

            def database(nights, adults, rooms, check_in_date, check_out_date):
                nights = NIGHTS.get()
                adults = ADULTS.get()
                rooms = ROOMS.get()
                check_in_date = CHECK_IN.get()
                check_out_date = CHECK_OUT.get()

                if not nights or not adults or not rooms or not check_in_date or not check_out_date:
                    messagebox.showerror('Error', 'All fields are required.')
                    return

               
                conn = sqlite3.connect("SELF.db")
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('CREATE TABLE IF NOT EXISTS Company1(NIGHTS INTEGER,ADULTS INTEGER,ROOMS INTEGER,CHECK_IN text,CHECK_OUT text,ROOM_TYPE text)')

                    room_type = "Beach Pool Villa"  # This should be dynamic based on selection
                    cursor.execute('INSERT INTO Company1(NIGHTS,ADULTS,ROOMS,CHECK_IN,CHECK_OUT,ROOM_TYPE)values(?,?,?,?,?,?)', 
                                (nights, adults, rooms,check_in_date,check_out_date,room_type))

                conn.commit()
                messagebox.showinfo('Information', 'BOOKED SUCCESSFULLY')
                self.hotel_log()
              

            L51 = Label(e, text="NIGHT(S)").place(x=620, y=200)
            L52 = Label(e, text="ADULTS:").place(x=620, y=250)
            L53 = Label(e, text="ROOMS:").place(x=620, y=300)

            e51 = Entry(e, bd=3, textvariable=NIGHTS)
            e51.place(x=720, y=200)

            e52 = Entry(e, bd=3, textvariable=ADULTS)
            e52.place(x=720, y=250)

            e53 = Entry(e, bd=3, textvariable=ROOMS)
            e53.place(x=720, y=300)
         

           

        
            

            def get_selected_date():
                selected_date = cal.get_date()
                date_var.set(selected_date)
                 # Calendar Widget
            cal = Calendar(e, selectmode="day", year=2023, month=8, day=3)
            cal.place(x=300,y=200)

            select_date_button = Button(e, text="SELECT DATE", command=get_selected_date)
            select_date_button.place(x=470,y=400)
    
    # Selected Date Display
            date_var = tk.StringVar()
            selected_date_label = Label(e, textvariable=date_var)
            selected_date_label.place(x=400,y=400)

    # Update entry fields with selected dates
            def update_checkin_date():
                checkin_entry.delete(0, tk.END)
                checkin_entry.insert(0, date_var.get())
                CHECK_IN.set(date_var.get())
        
            def update_checkout_date():
                checkout_entry.delete(0, tk.END)
                checkout_entry.insert(0, date_var.get())
                CHECK_OUT.set(date_var.get()) 
                

    # Check-In Date
            checkin_label = Label(e, text="CHECK-IN:")
            checkin_label.place(x=620,y=350)
            
            checkin_entry = tk.Entry(e)
            checkin_entry.place(x=720,y=350)
            
            update_checkin_button = Button(e, text="CONFIRM CHECK-IN", command=update_checkin_date)
            update_checkin_button.place(x=720,y=385)

    # Check-Out Date
            checkout_label = Label(e, text="CHECK-OUT:")
            checkout_label.place(x=620,y=435)
            
            checkout_entry = tk.Entry(e)
            checkout_entry.place(x=720,y=435)
            
            update_checkout_button = Button(e, text="CONFIRM CHECK-OUT", command=update_checkout_date)
            update_checkout_button.place(x=720,y=470)

               # Confirm Booking Button
            # Add order list button
            order_list_btn = Button(e, text="View Orders", command=self.show_orders, font=('Dotum', 14, 'bold'))
            order_list_btn.place(x=900, y=600)
            
            insert_button = Button(e, text="CONFIRM", command=lambda:database(NIGHTS.get(), ADULTS.get(), ROOMS.get(), checkin_entry.get(), checkout_entry.get()), font=('Dotum', 14, 'bold')) 

            insert_button.place(x=700, y=600)

        ce30 = Button(d, text="BOOK NOW", command=book, font=('Dotum', 14, 'bold'))
        ce30.place(x=500, y=550)

# Book now button for Room 2
        ce30 = Button(d, text="BOOK NOW", command=book, font=('Dotum', 14, 'bold'))
        ce30.place(x=1250, y=550)

        ce60 = Button(d, text=">>",command=hotel_log_A,font=('Dotum', 10))
        ce60.pack(side="right")
    def show_orders(self):
        order_window = Toplevel()
        order_window.title("Order List")
        order_window.geometry("800x600")
        
        conn = sqlite3.connect("SELF.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Company1")
        orders = cursor.fetchall()
        
        columns = ("Nights", "Adults", "Rooms", "Check-in", "Check-out", "Room Type")
        tree = ttk.Treeview(order_window, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            
        for order in orders:
            tree.insert("", "end", values=order)
            
        tree.pack(expand=True, fill="both")
        conn.close()

if __name__ == "__main__":
    app = HotelReservationApp()
