from pymysql import *
from tkinter import *
from tkinter import messagebox


class StudentGui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x400+350+150")

        self.row1 = Frame(self.root)
        self.lblrno = Label(self.row1, text="Rno:", width=15, font=("Times", 15, "bold"))
        self.enrno = Entry(self.row1, width=50, font=("Times", 15, "bold"))
        self.row1.pack(side=TOP, padx=5, pady=5, fill=X)
        self.lblrno.pack(side="left")
        self.enrno.pack(side="left")

        self.row2 = Frame(self.root)
        self.lblname = Label(self.row2, text="Name:", width=15, font=("Times", 15, "bold"))
        self.enname = Entry(self.row2, width=50, font=("Times", 15, "bold"))
        self.row2.pack(side=TOP, padx=5, pady=5, fill=X)
        self.lblname.pack(side="left")
        self.enname.pack(side="left")

        self.row3 = Frame(self.root)
        self.lblcourse = Label(self.row3, text="Course:", width=15, font=("Times", 15, "bold"))
        self.encourse = Entry(self.row3, width=50, font=("Times", 15, "bold"))
        self.row3.pack(side=TOP, padx=5, pady=5, fill=X)
        self.lblcourse.pack(side="left")
        self.encourse.pack(side="left")

        self.row4 = Frame(self.root)
        self.lblfees = Label(self.row4, text="Fees:", width=15, font=("Times", 15, "bold"))
        self.enfees = Entry(self.row4, width=50, font=("Times", 15, "bold"))
        self.row4.pack(side=TOP, padx=5, pady=5, fill=X)
        self.lblfees.pack(side="left")
        self.enfees.pack(side="left")

        self.row5 = Frame(self.root)
        self.btnfirst = Button(self.row5, width=15, font=("Times", 15, "bold"), text="First",command = self.first)
        self.btnprev = Button(self.row5, width=15, font=("Times", 15, "bold"), text="Prev",command = self.prev)
        self.btnnext = Button(self.row5, width=15, font=("Times", 15, "bold"), text="Next",command = self.next)
        self.btnlast = Button(self.row5, width=15, font=("Times", 15, "bold"), text="Last",command = self.last)
        self.row5.pack(side=TOP, fill=X, padx=5, pady=5)
        self.btnfirst.pack(side="left")
        self.btnprev.pack(side="left")
        self.btnnext.pack(side="left")
        self.btnlast.pack(side="left")

        self.row6 = Frame(self.root)
        self.btnclear = Button(self.row6, width=15, font=("Times", 15, "bold"), text="Clear",command = self.clearall)
        self.btninsert = Button(self.row6, width=15, font=("Times", 15, "bold"), text="Insert",command = self.insert)

        self.row6.pack(side=TOP, fill=X, padx=5, pady=5)
        self.btnclear.pack(side="left")
        self.btninsert.pack(side="left")


        self.connecttoDB()

        self.root.mainloop()

       
    def connecttoDB(self):

        try:
            # providing connection string
            self.conn = connect(host="localhost", user="root", password="", db="pythondb")

            # connecting to db
            self.cur = self.conn.cursor()

            self.getdata()
        except:
            messagebox.showerror("Error in ConnecttoDB")


    def getdata(self):

        try:
            # executing the query
            self.cur.execute("select * from student")

            # empty 2D list
            self.data = [[]]

            # storing data into local variable data
            self.data = self.cur.fetchall()

            self.rowno = 0

            self.showdata()
        except:
            messagebox.showerror("Error in getdata")


    def showdata(self):
        try:
            self.clearall()
            
            self.enrno.configure(state='normal')
            self.enname.configure(state='normal')
            self.encourse.configure(state='normal')
            self.enfees.configure(state='normal')


            self.enrno.insert(0, self.data[self.rowno][0])
            self.enname.insert(0, self.data[self.rowno][1])
            self.encourse.insert(0, self.data[self.rowno][2])
            self.enfees.insert(0, self.data[self.rowno][3])

            
            self.enrno.configure(state='disabled')
            self.enname.configure(state='disabled')
            self.encourse.configure(state='disabled')
            self.enfees.configure(state='disabled')
        except:
             messagebox.showerror("Error in showdata")

    def next(self):
        try:
            self.enrno.configure(state='normal')
            self.enname.configure(state='normal')
            self.encourse.configure(state='normal')
            self.enfees.configure(state='normal')


            lastrow = len(self.data) - 1
            if(self.rowno <lastrow):
                self.rowno += 1
                self.showdata()


                self.enrno.configure(state='disabled')
                self.enname.configure(state='disabled')
                self.encourse.configure(state='disabled')
                self.enfees.configure(state='disabled')
            else:
                messagebox.showerror(title = "StudentDB",message="last Record")
        except:
            messagebox.showerror("Error in next")


    def prev(self):
        try:
            self.enrno.configure(state='normal')
            self.enname.configure(state='normal')
            self.encourse.configure(state='normal')
            self.enfees.configure(state='normal')


            if(self.rowno == 0):
                messagebox.showerror(title = "StudentDB",message="First Record")
            else:
                self.rowno -=1
                self.showdata()


                self.enrno.configure(state='disabled')
                self.enname.configure(state='disabled')
                self.encourse.configure(state='disabled')
                self.enfees.configure(state='disabled')
        except:
             messagebox.showerror("Error in prev")

    def first(self):
        try:
            self.enrno.configure(state='normal')
            self.enname.configure(state='normal')
            self.encourse.configure(state='normal')
            self.enfees.configure(state='normal')


            self.rowno = 0
            self.showdata()


            self.enrno.configure(state='disabled')
            self.enname.configure(state='disabled')
            self.encourse.configure(state='disabled')
            self.enfees.configure(state='disabled')
        except:
             messagebox.showerror("Error in first")

    def last(self):
        try:
            self.enrno.configure(state='normal')
            self.enname.configure(state='normal')
            self.encourse.configure(state='normal')
            self.enfees.configure(state='normal')


            self.rowno = len(self.data) - 1
            self.showdata()


            self.enrno.configure(state='disabled')
            self.enname.configure(state='disabled')
            self.encourse.configure(state='disabled')
            self.enfees.configure(state='disabled')
        except:
             messagebox.showerror("Error in last")

    def insert(self):
        try:
            rno = self.enrno.get()
            name = self.enname.get()
            course = self.encourse.get()
            fees = self.enfees.get()

            insqry = "insert into student values(" + rno + ",'" + name + "','" + course + "'," + fees + ")"

            n = self.cur.execute(insqry)
            self.conn.commit()

            if(n > 0):
                messagebox.showinfo(title = "StudentDB",message="Data Inserted SuccessFully")
                self.getdata()
            else:
                 messagebox.showerror(title = "StudentDB",message="Data Insertion Error")       

        except:
              messagebox.showerror("Error in insert")





    def clearall(self):
        try:
            self.enrno.configure(state='normal')
            self.enname.configure(state='normal')
            self.encourse.configure(state='normal')
            self.enfees.configure(state='normal')

            
            self.enrno.delete(0,END)
            self.enname.delete(0,END)
            self.encourse.delete(0,END)
            self.enfees.delete(0,END)
        except:
            messagebox.showerror("Error in clearall")

if __name__ == "__main__":
    obj = StudentGui()