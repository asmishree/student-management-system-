from tkinter import *
from tkinter import ttk   #used for combo box jo gender ke liye laga rhe
import pymysql
import re
from tkinter import messagebox, END
from datetime import datetime

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        root.configure(bg="black")
        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman",45,"bold"), bg="BLACK", fg="WHITE")
        title.pack(side=TOP, fill=X)

        # Variables
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.dob_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.email_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="dim grey")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_Frame, text="Manage Students", bg="grey", fg="white", font=("times new roman",30,"bold"))
        m_title.grid(row=0, columnspan=3, pady=20)

        # Roll No
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman",15,"bold"), bd=5, relief="groove")
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Name
        lbl_name = Label(Manage_Frame, text="Name", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman",15,"bold"), bd=5, relief="groove")
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # DOB
        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_dob.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman",15,"bold"), bd=5, relief="groove")
        txt_dob.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Gender
        lbl_gender = Label(Manage_Frame, text="Gender", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=15, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman",13,"bold"), state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        # Contact
        lbl_Contact = Label(Manage_Frame, text="Contact", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman",15,"bold"), bd=5, relief="groove")
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Email
        lbl_email = Label(Manage_Frame, text="Email", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_email.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman",15,"bold"), bd=5, relief="groove")
        txt_email.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Address
        lbl_address = Label(Manage_Frame, text="Address", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(Manage_Frame, width=30, height=4, font=("",10), relief="groove")
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Buttons Frame
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="grey")
        btn_Frame.place(x=17, y=500, width=420)
        addbutton = Button(btn_Frame, text="ADD", width=10, command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updatebutton = Button(btn_Frame, text="UPDATE", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebutton = Button(btn_Frame, text="DELETE", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbutton = Button(btn_Frame, text="CLEAR", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # Detail Frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="grey", fg="white", font=("times new roman",15,"bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=15, font=("times new roman",13,"bold"), state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)
        txt_search = Entry(Detail_Frame, textvariable=self.search_text, width=20, font=("times new roman",15,"bold"), bd=5, relief="groove")
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        searchbutton = Button(Detail_Frame, text="SEARCH", command=self.search_data, width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbutton = Button(Detail_Frame, text="SHOW ALL", command=self.fetch_data, width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        # Table Frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="grey")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "dob", "gender", "email", "contact", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        # Table Heading
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        self.Student_table.pack(fill=BOTH, expand=1)

    def add_students(self):
    # collect values
        roll = self.Roll_No_var.get().strip()
        name = self.name_var.get().strip()
        dob = self.dob_var.get().strip()
        gender = self.gender_var.get().strip()
        email = self.email_var.get().strip()
        address = self.txt_address.get("1.0", "end-1c").strip()
        contact = self.contact_var.get().strip()

    # Mandatory fields check
        if not (roll and name and dob and gender and email and address and contact):
            messagebox.showerror("Error", "All fields are required.")
            return

    # Roll number validation
        if not roll.isdigit():
            messagebox.showerror("Error", "Roll number should contain digits only.")
            return

    # Contact number validation
        if not (contact.isdigit() and len(contact) == 10):
            messagebox.showerror("Error", "Contact number must be exactly 10 digits.")
            return
        #contact duplicate::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("SELECT * FROM students WHERE contact = %s", (contact,))
            result = cur.fetchone()
            if result:
                messagebox.showerror("Error", "This contact number already exists.")
                con.close()
                return
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")
            return

    # Date of Birth validation (format + logical range)
        try:
            parts = re.split(r"[-/]", dob)

            if not (1 <= int (parts[0]) <= 31):
                messagebox.showerror("Error", "Day should be between 1 and 31.")
                return
            if not (1 <= int(parts[1]) <= 12):
                messagebox.showerror("Error", "Month should be between 1 and 12.")
                return
            if not (1950 <= int(parts[2]) <= 2025):
                messagebox.showerror("Error", "Year should be between 1950 and 2025.")
                return
            try:
                entered_date = datetime.strptime(dob, "%d-%m-%Y") 
            except ValueError:
                try:
                    entered_date = datetime.strptime(dob, "%d/%m/%Y") 
                except ValueError:
                    messagebox.showerror("Error", "Invalid date format! Use DD-MM-YYYY or DD/MM/YYYY.")
                    return
           #current date:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            limit_date = datetime(2025, 11, 12)
            if entered_date >= limit_date:
                messagebox.showerror("Error", "Date should be less than 12-11-2025.")
                return

        except ValueError:
            messagebox.showerror("Error", f"Invalid Date! Use DD-MM-YYYY format:{ValueError}")
            return

    # Email validation
        email_pattern = r"^[A-Za-z0-9._\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$"
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid email address format.")
            return

    # Database operations
    
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()

            # Duplicate Roll Number check
            cur.execute(f"SELECT * FROM students WHERE roll_no = {roll}")
            existing = cur.fetchone()
            if existing:
                messagebox.showerror("Error", f"Roll Number {roll} already exists!")
                return

            # Insert record
            sql = """
                INSERT INTO students (roll_no, name, dob, gender, email, contact, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (roll, name, dob, gender, email, contact, address))
            con.commit()

            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record has been inserted successfully!")

        except Exception as e:
            print(f"Error in addimg data: {e}")
            messagebox.showerror("Database Error", f"Failed to insert record:\n{str(e)}")

        finally:
            if 'con' in locals() and con.open:
                con.close()
            


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select* from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
        con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.dob_var.set(row[2])
        self.gender_var.set(row[3])
        self.email_var.set(row[4])
        self.contact_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s, dob=%s, gender=%s, email=%s, contact=%s, address=%s where roll_no=%s",
            (self.name_var.get(), self.dob_var.get(), self.gender_var.get(), self.email_var.get(),
             self.contact_var.get(), self.txt_address.get('1.0',END), self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        self.fetch_data()
        con.close()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        query = "SELECT * FROM students WHERE " + self.search_by.get() + " LIKE %s"
        value = ("%" + self.search_text.get() + "%",)
        cur.execute(query, value)
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
        else:
            print("No records found!")  # optional for debugging
        con.close()

# root initialize krke object banaya hai
root = Tk()
ob = Student(root)
root.mainloop()
