from tkinter import *
import random
import time
import datetime
import tkinter.messagebox
import tempfile
import subprocess, sys
from tkinter import ttk
import os

class Coaching:
    def __init__(self, t):
        self.t = t
        self.t.title("Coaching Management System")
        self.t.geometry("1350x750+0+0")


        date = StringVar()
        date.set(time.strftime("%d/%m/%Y"))

        x1 = StringVar()
        x2 = StringVar()
        x3 = StringVar()
        x4 = IntVar()
        x5 = IntVar()
        x6 = StringVar()
        x7 = IntVar()

        Firstname = StringVar() #
        Surname = StringVar() #
        Address = StringVar() #
        PostCode = StringVar() #
        Telephone = StringVar() #
        Fees = IntVar() #
        AccomodationFees = StringVar() #
        RegNumber = StringVar() #
        StudentID = StringVar() #
        College = StringVar() #
        Nationality = StringVar() #
        ExtraCourses = StringVar() #
        FinalFees = StringVar() #
        ExtraCourses.set('0')
        AccomodationFees.set('0')
        FinalFees.set('0')

        #***************************************************************************Functions*********************************************************************************************#       
        def sysexit():
            sysexit = tkinter.messagebox.askyesno("Coaching Management System", "Confirm if you want to exit?")
            if sysexit > 0:
                t.destroy()
                return

        def sysprint():
            sysprint = self.txtreceipt.get("1.0", "end-1c")
            filename = tempfile.mktemp(".txt")
            open(filename, 'w').write(sysprint)
            os.startfile(filename, "Print")
            
        def sysreset():
            Firstname.set('')
            Surname.set('')
            Address.set('')
            PostCode.set('')
            Telephone.set('')
            StudentID.set('')
            Fees.set('')
            Nationality.set('')
            College.set('')

            RegNumber.set('')

            x1.set('')
            x2.set('')
            x3.set('')
            x4.set(0)
            x5.set(0)
            x6.set('')
            x7.set(0)

            ExtraCourses.set("0")
            AccomodationFees.set("0")
            FinalFees.set("0")
            
            self.textExtraCourses.configure(state = DISABLED)
            self.textaccomodation.configure(state = DISABLED)
            self.textfinalfees.configure(state = DISABLED)

            self.cboxverificationid.current(0)
            self.degree.current(0)
            self.pmode.current(0)
            self.courses.current(0)
            sysgen()

        def sysreset2():
            sysreset2 = tkinter.messagebox.askyesno("Coaching Management System", "Confirm if you want to reset?")
            if sysreset2 > 0:
                sysreset()
            elif sysreset2 <= 0:
                sysreset()
                self.txtreceipt.delete("1.0", END)
                self.txtreceipt.insert(END, "Student ID\t\t First Name\t\t Lastname\t\t Address\t\t Extra Course  \t\t Telephone\t\t Date\t\t Degree\t\t College\t\t Course\t\t Final Fees\t\n")                

        def sysgen():
            membername = StringVar()
            x = random.randint(10908, 500786)
            randomRef = str(x)
            membername.set(randomRef)
            RegNumber.set(randomRef)

        def sysreceipt():
            sysgen()
            self.txtreceipt.insert(END, StudentID.get() + "\t\t" + Firstname.get() + "\t\t" + Surname.get() + "\t\t" + Address.get() + "\t\t" + ExtraCourses.get() + "\t\t" + Telephone.get() + "\t\t" + date.get() + "\t\t" + x2.get() + "\t\t" + College.get() + "\t\t" + x6.get() + "\t\t" + FinalFees.get() + "\n")

        def accomodation():
            global paid1
            if x5.get() == 1:
                self.textaccomodation.configure(state = NORMAL)
                item1 = float(9450)
                AccomodationFees.set("Rs." + str(item1))
                paid1 = AccomodationFees.get()
                AccomodationFees.set("Rs." + str(item1))
            elif x5.get() == 0:
                self.textaccomodation.configure(state = NORMAL)
                AccomodationFees.set("0")

        def finalfees():
            global paid1
            if x7.get() == 1:
                self.textfinalfees.configure(state = NORMAL)
                item1 = float(9450)
                item1 = Fees.get() - item1
                FinalFees.set("Rs." + str(item1))
            elif x7.get() == 0:
                self.textfinalfees.configure(state = NORMAL)
                item = Fees.get()
                FinalFees.set("Rs." + str(item))

        def extracourse():
            if x4.get() == 1:
                self.textExtraCourses.configure(state = NORMAL)
                ExtraCourses.set("Yes")
            elif x4.get() == 0:
                self.textExtraCourses.configure(state = NORMAL)
                ExtraCourses.set("No")
                
        #***************************************************************************MainFrames*********************************************************************************************#       
        mainframe = Frame(self.t)
        mainframe.grid()

        tops = Frame(mainframe, bd = 10, relief = GROOVE)
        tops.pack(side = TOP)

        self.labeltitle = Label(tops, width = 30, font = ('arial', 39, 'bold'), text = 'Coaching Management System', justify = CENTER)
        self.labeltitle.grid(padx = 150)

        membername = LabelFrame(mainframe, bd = 10, width = 1300, height = 400, font = ('arial', 12, 'bold'), text = 'Student Credentials', relief = GROOVE)
        membername.pack(padx = 38, side = TOP)

        receipt = LabelFrame(mainframe, bd = 10, width = 1300, height = 200, font = ('arial', 12, 'bold'), text = 'Details', relief = GROOVE)
        receipt.pack(padx = 38, side = TOP)

 #***************************************************************************Widgets******************************************************************************************************************#       
        self.labelstdid = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Student ID')
        self.labelstdid.grid(row = 0, column = 0, sticky = W)
        self.textstdid = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = StudentID, insertwidth = 2)
        self.textstdid.grid(row = 0, column = 1)

        self.labelfname = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'First Name')
        self.labelfname.grid(row = 1, column = 0, sticky = W)
        self.textfname = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = Firstname, insertwidth = 2)
        self.textfname.grid(row = 1, column = 1)
        
        self.labelsname = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Last Name')
        self.labelsname.grid(row = 2, column = 0, sticky = W)
        self.textsname = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = Surname, insertwidth = 2)
        self.textsname.grid(row = 2, column = 1)

        self.labeladdress = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Address')
        self.labeladdress.grid(row = 3, column = 0, sticky = W)
        self.textaddress = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = Address, insertwidth = 2)
        self.textaddress.grid(row = 3, column = 1)

        self.labelpcode = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Post Code')
        self.labelpcode.grid(row = 4, column = 0, sticky = W)
        self.textpcode = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = PostCode, insertwidth = 2)
        self.textpcode.grid(row = 4, column = 1)

        self.cboxExtraCourses = Checkbutton(membername, text = 'Extra Courses', variable = x4, onvalue = 1, offvalue = 0, font = ('arial', 16, 'bold'), command = extracourse)
        self.cboxExtraCourses.grid(row = 5, column = 0, sticky = W)
        self.textExtraCourses = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = ExtraCourses, insertwidth = 2, state = DISABLED, justify = RIGHT)
        self.textExtraCourses.grid(row = 5, column = 1)
        
#***************************************************************************Widgets*********************************************************************************************#       
        self.labeltele = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Telephone')
        self.labeltele.grid(row = 0, column = 2, sticky = W)
        self.texttele = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = Telephone, insertwidth = 2)
        self.texttele.grid(row = 0, column = 3)

        self.labeldate = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Date')
        self.labeldate.grid(row = 1, column = 2, sticky = W)
        self.textdate = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = date, insertwidth = 2)
        self.textdate.grid(row = 1, column = 3)
        
        self.labelverificationid = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Verification ID')
        self.labelverificationid.grid(row = 2, column = 2, sticky = W)
        self.cboxverificationid = ttk.Combobox(membername, textvariable = x1, state = 'readonly', font = ('arial', 13, 'bold'), width = 19)
        self.cboxverificationid['value'] = (' ', 'Aadhar Card', 'Pan Card', 'Student ID', 'Voting Card', 'Driving License')
        self.cboxverificationid.current(0)
        self.cboxverificationid.grid(row = 2, column = 3)

        self.degree = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Degree')
        self.degree.grid(row = 3, column = 2, sticky = W)
        self.degree = ttk.Combobox(membername, textvariable = x2, state = 'readonly', font = ('arial', 13, 'bold'), width = 19)
        self.degree['value'] = (' ', 'Matriculation(10th)', 'Intermediate(12th)', 'Graduation', 'Post Graduation')
        self.degree.current(0)
        self.degree.grid(row = 3, column = 3)

        self.pmode = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Payment Mode')
        self.pmode.grid(row = 4, column = 2, sticky = W)
        self.pmode = ttk.Combobox(membername, textvariable = x3, state = 'readonly', font = ('arial', 13, 'bold'), width = 19)
        self.pmode['value'] = (' ', 'Cash', 'Cheque', 'Card', 'Demand Draft', 'PhonePe', 'Paytm', 'Google Pay')
        self.pmode.current(0)
        self.pmode.grid(row = 4, column = 3)
        
        self.chkaccomodation = Checkbutton(membername, text = 'Accomodation', variable = x5, onvalue = 1, offvalue = 0, font = ('arial', 16, 'bold'), command = accomodation)
        self.chkaccomodation.grid(row = 5, column = 2, sticky = W)
        self.textaccomodation = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = AccomodationFees, insertwidth = 2, state = DISABLED, justify = RIGHT)
        self.textaccomodation.grid(row = 5, column = 3)

   #***************************************************************************Widgets*********************************************************************************************#       
        self.labelregno = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Reg. Number')
        self.labelregno.grid(row = 0, column = 4, sticky = W)
        self.textregno = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = RegNumber, insertwidth = 2, state = DISABLED)
        self.textregno.grid(row = 0, column = 5)

        self.labelcollege = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'College')
        self.labelcollege.grid(row = 1, column = 4, sticky = W)
        self.textcollege = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = College, insertwidth = 2)
        self.textcollege.grid(row = 1, column = 5)
        
        self.labelfees = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Fees')
        self.labelfees.grid(row = 2, column = 4, sticky = W)
        self.textfees = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = Fees, insertwidth = 2)
        self.textfees.grid(row = 2, column = 5)

        self.courses = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Course')
        self.courses.grid(row = 3, column = 4, sticky = W)
        self.courses = ttk.Combobox(membername, textvariable = x6, state = 'readonly', font = ('arial', 13, 'bold'), width = 19)
        self.courses['value'] = (' ', 'Java(Core + Advance)', 'Python(Core + Advance)', 'Hibernate', 'Android', 'Spring', 'C & C++', 'PHP + MySQL', 'Big Data & Hadoop', 'Angular JS', 'Embedded System', 'Cloud Computing')
        self.courses.current(0)
        self.courses.grid(row = 3, column = 5)

        self.labelnationality = Label(membername, bd = 7, font = ('arial', 16, 'bold'), text = 'Nationality')
        self.labelnationality.grid(row = 4, column = 4, sticky = W)
        self.textnationality = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = Nationality, insertwidth = 2)
        self.textnationality.grid(row = 4, column = 5)

        self.cboxfinalfees = Checkbutton(membername, text = 'Final Fees', variable = x7, onvalue = 1, offvalue = 0, font = ('arial', 16, 'bold'), command = finalfees)
        self.cboxfinalfees.grid(row = 5, column = 4, sticky = W)
        self.textfinalfees = Entry(membername, bd = 7, font = ('arial', 13, 'bold'), textvariable = FinalFees, insertwidth = 2, state = DISABLED, justify = RIGHT)
        self.textfinalfees.grid(row = 5, column = 5)

        #***************************************************************************Receipts*********************************************************************************************#       
        self.txtreceipt = Text(receipt, width = 181, height = 10, font = ('arial', 10, 'bold'))
        self.txtreceipt.grid(row = 0, column = 0, columnspan = 4)

        self.txtreceipt.insert(END, "Student ID\t\t First Name\t\t Lastname\t\t Address\t\t Extra Course  \t\t Telephone\t\t Date\t\t Degree\t\t College\t\t Course\t\t Final Fees\t\n")

        self.btnreceipt = Button(receipt, bd = 7, font = ('arial', 16, 'bold'), width = 13, text = 'Receipt', command = sysreceipt)
        self.btnreceipt.grid(row = 1, column = 0, pady = 10)

        self.btnreset = Button(receipt, bd = 7, font = ('arial', 16, 'bold'), width = 13, text = 'Reset', command = sysreset2)
        self.btnreset.grid(row = 1, column = 1, pady = 10)

        self.btnprint = Button(receipt, bd = 7, font = ('arial', 16, 'bold'), width = 13, text = 'Print', command = sysprint)
        self.btnprint.grid(row = 1, column = 2, pady = 10)

        self.btnexit = Button(receipt, bd = 7, font = ('arial', 16, 'bold'), width = 13, text = 'Exit', command = sysexit)
        self.btnexit.grid(row = 1, column = 3, pady = 10)

        
if __name__ == '__main__':
    t = Tk()
    t.wm_iconbitmap('logo.ico')
    app = Coaching(t)
    t.mainloop()
