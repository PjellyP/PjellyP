import customtkinter as ct
import mysql.connector as mc
ct.set_appearance_mode("system")
ct.set_default_color_theme("dark-blue")

#please follow the instruction in the comments all over the code.
# attention : please run the code below that is commented, in another file then back to this file and run the actual code.

# import mysql.connector as mc
# yourdb = mc.connect(
#     host = "localhost",
#     user = " ",#ENTER your username of mysql in this line
#     password = " ",#ENTER your password of mysql in this line
# )
# cursor = yourdb.cursor()
# cursor.execute("CREATE DATABASE ") #ENTER your desired database name after DATABASE in quotations
#
# yourdb = mc.connect(
#     host = "localhost",
#     user = " ",#ENTER your username of mysql in this line
#     password = " ",#ENTER your password of mysql in this line
#     database = " ",# ENTER the name of database that you entered  to create it
# )
#
# cursor = yourdb.cursor()
# cursor.execute("CREATE TABLE formd(id INT(200) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(225),lastname VARCHAR(225),experties VARCHAR(225),syscode INT(225))")
#
# yourdb = mc.connect(
#     host = "localhost",
#     user = " ",#ENTER your username of mysql in this line
#     password = " ",#ENTER your password of mysql in this line
#     database = " ",# ENTER the name of database that you entered to create it
# )
#
# cursor = yourdb.cursor()
# cursor.execute("CREATE TABLE formss(id INT(200) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(225),lastname VARCHAR(225),IDD INT(225),ILLINSURC VARCHAR(225))")
#
#
# yourdb = mc.connect(
#     host = "localhost",
#     user = " ",#ENTER your username of mysql in this line
#     password = " ",#ENTER your password of mysql in this line
#     database = " ",# ENTER the name of database that you entered to create it
# )
#
# cursor = yourdb.cursor()
# cursor.execute("CREATE TABLE form_n(id INT(200) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(225),lastname VARCHAR(225),ID_n INT(225),syscode INT(225))")
#
#
# yourdb = mc.connect(
#     host = "localhost",
#     user = " ",#ENTER your username of mysql in this line
#     password = " ",#ENTER your password of mysql in this line
#     database = " ",# ENTER the name of database that you entered to create it
# )
#
# cursor = yourdb.cursor()
# cursor.execute("CREATE TABLE form_ops(id INT(200) NOT NULL AUTO_INCREMENT PRIMARY KEY,ops_type VARCHAR(225),docname VARCHAR(225),roomnum INT(225),nursename VARCHAR(225))")
##############


class GUI:

# window of login
    def __init__(self):
        self.root = ct.CTk()
        self.root.geometry("500x200")
        self.root.title("LOGIN")
        self.root.resizable(False, False)

        self.lb = ct.CTkLabel(master=self.root, text="LOGIN PLEASE")
        self.lb.place(x=225, y=10)

        self.ey = ct.CTkEntry(master=self.root, placeholder_text="enter your username ")
        self.ey.place(x=200, y=40)

        self.label_login = ct.CTkLabel(master=self.root, text=" use n,m,r,t,d,w to create username")
        self.label_login.place(x=1, y=40)

        self.ey2 = ct.CTkEntry(master=self.root, placeholder_text="enter your password ")
        self.ey2.place(x=200, y=70)

        self.label_login2 = ct.CTkLabel(master=self.root, text=" use e,o,p,l,k to create password")
        self.label_login2.place(x=15, y=70)

        self.bt = ct.CTkButton(master=self.root, text="LOGIN", command=self.dd)
        self.bt.place(x=200, y=100)
        self.root.mainloop()

# func of login with user and pass
    def dd(self):
        for g in str(self.ey.get()):
            for g_ in str(self.ey2.get()):
                if g in ["n", "m", "r", "t", "d", "w"] and g_ in ["e", "o", "p", "l", "k"]:
                    return self.close(), self.form_choose()
                else:
                    self.write_invalid()

# write that user or pass invalid
    def write_invalid(self):
        self.write = ct.CTk()
        self.write.geometry("300x100")
        self.write.title("invalid🔔❌❕")
        self.write.resizable(False, False)
        self.label_write = ct.CTkLabel(master=self.write, text="THE PASSWORD OR USERNAME IS INVALID")
        self.label_write.place(x=30, y=30)
        self.write.mainloop()

# close method choose form
    def close(self):
        self.root.destroy()

# window of choose form
    def form_choose(self):
        self.win = ct.CTk()
        self.win.geometry("513x513")
        self.win.title("FORM")
        self.win.resizable(False, False)

        self.but = ct.CTkButton(master=self.win, width=100, height=100, text="FORM OF DOCTORS", command=self.formd)
        self.but.place(x=50, y=80)
        
        self.but2 = ct.CTkButton(master=self.win, width=100, height=100, text="FORM OF PATIENTS",
                                 command=self.form_patients)
        self.but2.place(x=185, y=80)
        
        self.but3 = ct.CTkButton(master=self.win, width=100, height=100, text="FORM OF NURSES", command=self.form_nurses
                                 )
        self.but3.place(x=320, y=80)
        
        self.but4 = ct.CTkButton(master=self.win, width=120, height=120, text="FORM OF OPs", command=self.form_OPs)
        self.but4.place(x=190, y=190)

        self.win.mainloop()

# window of doctors
    def formd(self):
        self.win_doctors = ct.CTk()
        self.win_doctors.geometry("500x500")
        self.win_doctors.title("FORM OF DOCTORS")
        self.win.resizable(False, False)

        self.lable_docN = ct.CTkLabel(master=self.win_doctors, text="PLEASE ENTER YOUR NAME :")
        self.lable_docN.place(x=20, y=50)
        self.label_docNE = ct.CTkEntry(master=self.win_doctors)
        self.label_docNE.place(x=300, y=50)
        
        self.label_docL = ct.CTkLabel(master=self.win_doctors, text="PLEASE ENTER YOUR LAST NAME :")
        self.label_docL.place(x=20, y=100)
        self.label_docLE = ct.CTkEntry(master=self.win_doctors)
        self.label_docLE.place(x=300, y=100)
        
        self.label_docEX = ct.CTkLabel(master=self.win_doctors, text="PLEASE ENTER YOUR EXPERTISE :")
        self.label_docEX.place(x=20, y=150)
        self.label_docEXE = ct.CTkEntry(master=self.win_doctors)
        self.label_docEXE.place(x=300, y=150)
        
        self.label_docsyscode = ct.CTkLabel(master=self.win_doctors, text="PLEASE ENTER YOUR MEDICAL SYSTEM CODE  :")
        self.label_docsyscode.place(x=20, y=200)
        self.label_docsyscodeE = ct.CTkEntry(master=self.win_doctors)
        self.label_docsyscodeE.place(x=300, y=200)
        
        self.button_doctors_store = ct.CTkButton(master=self.win_doctors, text="DOCTOR CLICK TO STORE",
                                                 command=lambda: [self.store_d(), self.close_d()])
        self.button_doctors_store.place(x=200, y=400)
        
        self.win_doctors.mainloop()

# func of closing the open window for doctor window
    def close_d(self):
        self.win_doctors.destroy()

# func of storing data in mysql
    def store_d(self):
        doctorsn = self.label_docNE.get()
        doctorsl = self.label_docLE.get()
        doctorse = self.label_docEXE.get()
        doctorss = self.label_docsyscodeE.get()

        mydb = mc.connect(
            host="localhost",
            user=" ", # ENTER the username of your mysql workbench
            password=" ", # ENTER the password of your mysql workbench
            database=" ", # ENTER the database name that you created
        )

        mycursor = mydb.cursor()
        sqlformula_d = "INSERT INTO formd(name,lastname,expertise,syscode) VALUES (%s,%s,%s,%s)"
        infos_doctors = ([doctorsn, doctorsl, doctorse, doctorss])
        mycursor.execute(sqlformula_d, infos_doctors)

        mydb.commit()

# window of patients
    def form_patients(self):
        self.win_patients = ct.CTk()
        self.win_patients.geometry('500x500')
        self.win_patients.title('FORM OF PATIENTS')
        self.win_patients.resizable(False, False)

        self.label_PatientsN = ct.CTkLabel(master=self.win_patients, text="PLEASE ENTER YOUR NAME :")
        self.label_PatientsN.place(x=20, y=50)
        self.label_PatientsNE = ct.CTkEntry(master=self.win_patients)
        self.label_PatientsNE.place(x=300, y=50)
        
        self.label_PatientsL = ct.CTkLabel(master=self.win_patients, text="PLEASE ENTER YOUR LAST NAME :")
        self.label_PatientsL.place(x=20, y=100)
        self.label_PatientsLE = ct.CTkEntry(master=self.win_patients)
        self.label_PatientsLE.place(x=300, y=100)
        
        self.label_PatientsID = ct.CTkLabel(master=self.win_patients, text="PLEASE ENTER YOUR ID :")
        self.label_PatientsID.place(x=20, y=150)
        self.label_PatientsIDE = ct.CTkEntry(master=self.win_patients)
        self.label_PatientsIDE.place(x=300, y=150)
        
        self.label_PatientsINS_ILL = ct.CTkLabel(master=self.win_patients,
                                                 text="PLEASE ENTER YOUR ILLNESS AND INSURANCE :")
        self.label_PatientsINS_ILL.place(x=20, y=200)
        self.label_PatientsINS_ILLE = ct.CTkEntry(master=self.win_patients)
        self.label_PatientsINS_ILLE.place(x=340, y=200)

        self.button_patients_store = ct.CTkButton(master=self.win_patients, text="PAITENT CLICK TO STORE",
                                                  command=lambda: [self.store_p(), self.close_p()])
        self.button_patients_store.place(x=200, y=400)
        
        self.win_patients.mainloop()

# func of closing the patients open window
    def close_p(self):
        self.win_patients.destroy()

# func of storing the patients data
    def store_p(self):
        patientn = self.label_PatientsNE.get()
        patientln = self.label_PatientsLE.get()
        patientid = self.label_PatientsIDE.get()
        patientillinsurc = self.label_PatientsINS_ILLE.get()

        mydb = mc.connect(
            host = "localhost",
            user = " ", # ENTER the username of your mysql workbench
            password = " ", # ENTER the password of your mysql workbench
            database = " ", # ENTER the name of database that you created
        )

        mycursor = mydb.cursor()
        sqlformula = "INSERT INTO formss(name,lastname,IDD,ILLINSURC) VALUES (%s,%s,%s,%s)"
        infos = ([patientn,patientln,patientid,patientillinsurc])
        mycursor.execute(sqlformula,infos)

        mydb.commit()

# window of nurses
    def form_nurses(self):
        self.win_nurses = ct.CTk()
        self.win_nurses.geometry('500x500')
        self.win_nurses.title('FORM OF NURSES')
        self.win_nurses.resizable(False, False)

        self.label_nursesN = ct.CTkLabel(master=self.win_nurses, text="PLEASE ENTER YOUR NAME :")
        self.label_nursesN.place(x=20, y=50)
        self.label_nursesNE = ct.CTkEntry(master=self.win_nurses)
        self.label_nursesNE.place(x=300, y=50)
        
        self.label_nursesL = ct.CTkLabel(master=self.win_nurses, text="PLEASE ENTER YOUR LAST NAME :")
        self.label_nursesL.place(x=20, y=100)
        self.label_nursesLE = ct.CTkEntry(master=self.win_nurses)
        self.label_nursesLE.place(x=300, y=100)
        
        self.label_nursesID = ct.CTkLabel(master=self.win_nurses, text="PLEASE ENTER YOUR ID :")
        self.label_nursesID.place(x=20, y=150)
        self.label_nursesIDE = ct.CTkEntry(master=self.win_nurses)
        self.label_nursesIDE.place(x=300, y=150)
        
        self.label_nursesSYSCODE = ct.CTkLabel(master=self.win_nurses, text="PLEASE ENTER YOUR SYSTEM CODE OF NURSES :")
        self.label_nursesSYSCODE.place(x=20, y=200)
        self.label_nursesSYSCODEE = ct.CTkEntry(master=self.win_nurses)
        self.label_nursesSYSCODEE.place(x=340, y=200)

        self.BUTTON_NURSE = ct.CTkButton(master=self.win_nurses, text="NURSE CLICK TO STORE",
                                         command=lambda: [self.store_n(), self.close_n()])
        self.BUTTON_NURSE.place(x=200, y=400)
        self.win_nurses.mainloop()

# func of closing the nurses open window
    def close_n(self):
        self.win_nurses.destroy()

# func of storing the nurses data
    def store_n(self):
        namen = self.label_nursesNE.get()
        lastnamen = self.label_nursesLE.get()
        Idn = self.label_nursesIDE.get()
        syscoden = self.label_nursesSYSCODEE.get()

        mydb = mc.connect(
            host="localhost",
            user=" ", # ENTER the username of your mysql workbench
            password=" ", # ENTER the password of your mysql workbench
            database=" ", # ENTER the name of database that you created
        )

        mycursor = mydb.cursor()
        sqlformula_n = "INSERT INTO form_n(name,lastname,ID_n,syscode) VALUES (%s,%s,%s,%s)"
        infos_n = ([namen, lastnamen, Idn, syscoden])
        mycursor.execute(sqlformula_n, infos_n)

        mydb.commit()

# window of operations
    def form_OPs(self):
        self.winops=ct.CTk()
        self.winops.geometry("500x500")
        self.winops.title("FORM OF OPs")
        self.winops.resizable(False, False)

        self.labops= ct.CTkLabel(master=self.winops, text="PLEASE ENTER OPERATION TYPE :")
        self.labops.place(x=20, y=50)
        self.labopsE= ct.CTkEntry(master=self.winops)
        self.labopsE.place(x=300, y=50)

        self.labops1 = ct.CTkLabel(master=self.winops, text="PLEASE ENTER YOUR DOCTOR's NAME :")
        self.labops1.place(x=20, y=100)
        self.labops1E = ct.CTkEntry(master=self.winops)
        self.labops1E.place(x=300, y=100)

        self.labops2 = ct.CTkLabel(master=self.winops, text="PLEASE ENTER YOUR ROOM NUMBER :")
        self.labops2.place(x=20, y=150)
        self.labops2E = ct.CTkEntry(master=self.winops)
        self.labops2E.place(x=300, y=150)

        self.labops3 = ct.CTkLabel(master=self.winops, text="PLEASE ENTER your NURSE's NAME :")
        self.labops3.place(x=20, y=200)
        self.labops3E = ct.CTkEntry(master=self.winops)
        self.labops3E.place(x=340, y=200)

        self.BUTTON_Ops = ct.CTkButton(master=self.winops, text="CLICK TO STORE!", command=lambda: [self.store_ops(),
                                                                                                    self.close_ops()])
        self.BUTTON_Ops.place(x=200, y=400)
        self.winops.mainloop()

# func of closing the open ops window
    def close_ops(self):
        self.winops.destroy()

# func of storing the data in the mysql
    def store_ops(self):
        optype = self.labopsE.get()
        docname = self.labops1E.get()
        roomnum = self.labops2E.get()
        nursename = self.labops3E.get()

        mydb = mc.connect(
            host="localhost",
            user=" ", # ENTER the username of your mysql workbench
            password=" ", # ENTER the password of your mysql workbench
            database=" ", # ENTER the name of database that you created
        )

        mycursor = mydb.cursor()
        sqlformula_ops = "INSERT INTO form_ops(ops_type, docname, roomnum, nursename) VALUES (%s,%s,%s,%s)"
        infos_ops = ([optype, docname, roomnum, nursename])
        mycursor.execute(sqlformula_ops, infos_ops)

        mydb.commit()

GUI()


