from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time
import webbrowser
from PIL import ImageTk, Image
from tkcalendar import DateEntry

splash_root = Tk()
splash_root.overrideredirect(True)
splash_root.geometry("700x430+450+200")
splash_root.resizable(0, 0)
splash_root.config(bg="white")

logo = Image.open("images/mainlogo.png")
resize = logo.resize((600, 430), Image.ANTIALIAS)
mainlogo = ImageTk.PhotoImage(resize)
label2 = Label(image=mainlogo, bg="white")
label2.image = mainlogo
label2.place(x=55, rely=0)


def main():
    progress.stop()
    splash_root.destroy()
    conn = mysql.connector.connect(host="localhost", user="root", passwd="Sahil@123", database="studentrecord")
    c = conn.cursor()

    class LoginPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg='white')

            def check(username, password):
                c.execute(f"SELECT username,password FROM adminrecord where username = '{username}' and "
                          f"password='{password}'")
                result = c.fetchall()
                if result:
                    label1.place_forget()
                    label2.place_forget()
                    username2.delete(0, END)
                    password2.delete(0, END)
                    controller.show_frame(HomePage)
                else:
                    messagebox.showerror("Error", "No Data Found")
                conn.commit()

            def register():
                label1.place_forget()
                label2.place_forget()
                controller.show_frame(RegisterPage)

            def showimage():
                label1.place(x=10, y=10)
                label2.place(relx=0.77, rely=0.02)

                # Main Big
            image1 = Image.open("images/logo.png")
            resize1 = image1.resize((800, 595), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize1)
            label1 = Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            # Small Icon
            image2 = Image.open("images/login.png")
            resize2 = image2.resize((130, 100), Image.ANTIALIAS)
            test2 = ImageTk.PhotoImage(resize2)
            label2 = Label(image=test2, bg="white")
            label2.image = test2
            label2.place(relx=0.77, rely=0.02)

            intro = Label(self, bg="white", text="School\nManagement\nSystem", font=("arial", 70))
            intro.place(relx=0.10, rely=0.15)
            intro2 = Label(self, bg="white", fg="tomato", text="Created by Sahil Sharma", font=("arial", 30))
            intro2.place(relx=0.16, rely=0.8)

            Label(self, text="Sign In: ", font=("Arial", 15, "underline"), bg="white", fg="#536DFE").\
                place(relx=0.8, rely=0.20)
            Label(self, text="Username:", font=("Arial", 15), bg="white").place(relx=0.7, rely=0.25)
            username2 = Entry(self, font=("arial", 15), width=29)
            username2.place(relx=0.7, rely=0.32)
            Label(self, text="Password:", font=("arial", 15), bg="white").place(relx=0.7, rely=0.43)
            password2 = Entry(self, font=("arial", 15), width=29, show="*")
            password2.place(relx=0.7, rely=0.5)
            Button(self, text="Login", cursor="hand2", borderwidth=0, width=29, bg="#536DFE", fg="white",
                   font=("Arial", 15), command=lambda: check(username2.get(), password2.get())).place(relx=0.7,
                                                                                                      rely=0.6)
            Button(self, text="Register", cursor="hand2", borderwidth=0, width=29, bg="tomato", fg="white",
                   font=("Arial", 15), command=register).place(relx=0.7, rely=0.68)
            Button(self, text="Show Image", cursor="hand2", borderwidth=0, width=29, bg="skyblue", fg="black",
                   font=("Arial", 15), command=showimage).place(relx=0.7, rely=0.76)

    class RegisterPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)

            self.configure(bg='white')

            def insert(username, password, email, mobile):
                c.execute(f"INSERT INTO adminrecord VALUES('{username}', '{password}', '{email}', {mobile})")
                conn.commit()
                messagebox.showinfo("Register", "Admin Registered.")
                controller.show_frame(LoginPage)

            Label(self, text="Register new User", bg="#a5b0f2", width=109, height=2, font='Arial').pack()
            Label(self, bg="white", text="Username:", font=("arial", 15)).place(relx=0.2, rely=0.2)
            username = Entry(self, font=("arial", 15))
            username.place(relx=0.3, rely=0.2)
            Label(self, bg="white", text="Password:", font=("arial", 15)).place(relx=0.2, rely=0.3)
            password = Entry(self, font=("arial", 15))
            password.place(relx=0.3, rely=0.3)
            Label(self, bg="white", text="Email:", font=("arial", 15)).place(relx=0.2, rely=0.4)
            email = Entry(self, font=("arial", 15))
            email.place(relx=0.3, rely=0.4)
            Label(self, bg="white", text="Mobile:", font=("arial", 15)).place(relx=0.2, rely=0.5)
            mobile = Entry(self, font=("arial", 15))
            mobile.place(relx=0.3, rely=0.5)
            Button(self, bg="red", cursor="hand2", borderwidth=0, fg="white", text="Register", font=("arial", 15),
                   width=31, command=lambda: insert(username.get(), password.get(), email.get(), mobile.get())).\
                place(relx=0.2, rely=0.6)

            Label(self, text="", height=36, bg="#a5b0f2").place(relx=0.6, rely=0.088)

            Label(self, bg="white", text="Already have an Account:", font=("arial", 15, "underline")).\
                place(relx=0.7, rely=0.3)
            Button(self, cursor="hand2", borderwidth=0, bg="blue", fg="white", text="Login", width=30,
                   font=("arial", 15), command=lambda: controller.show_frame(LoginPage)).place(relx=0.66, rely=0.4)

    class HomePage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg='white')

            def logout():
                out = messagebox.askyesno("Logout", "Are you Sure?")
                if out:
                    controller.show_frame(LoginPage)
                else:
                    pass

            def on_enter(e):
                btn['background'] = 'red'
                btn.config(fg="white")

            def on_leave(e):
                btn['background'] = '#d6d4d4'
                btn.config(fg="red")

            def insta():
                webbrowser.open("https://www.instagram.com/sahil_sharma_50", new=True)

            def face():
                webbrowser.open("https://www.facebook.com/sahilsharma50s/", new=True)

            def git():
                webbrowser.open("https://github.com/sahil-sharma-50", new=True)

            Label(self, text="Student Management System", bg="#a5b0f2", width=109, height=2, font=('Arial', 15)).pack()
            Label(self, text="Welcome User", bg="white", fg="black", font=("Arial",)).place(y=55, x=10)
            time_string = time.strftime('%H:%M')
            Label(self, text=f"Time : {time_string}", fg="black", bg="white", font=("Arial",)).place(relx=0.88, y=55)

            Button(self, text="Insert Data", bg="#612cc9", borderwidth=0, fg="white", width=20, height=5,
                   font=("arial",), cursor="hand2", command=lambda: controller.show_frame(InsertPage)).\
                place(relx=0.1, y=125)
            Button(self, text="Update Data", bg="yellow", borderwidth=0, fg="black", width=20, height=5,
                   font=("Arial",), cursor="hand2", command=lambda: controller.show_frame(UpdatePage)).\
                place(relx=0.4, y=125)
            Button(self, text="Delete Data", bg="red", borderwidth=0, fg="white", width=20, height=5,
                   font=("Arial",), cursor="hand2", command=lambda: controller.show_frame(DeletePage)).\
                place(relx=0.7, y=125)
            Button(self, text="GitHub", bg="#24292e", borderwidth=0, fg="white", width=20, height=5,
                   font=("Arial",), cursor="hand2", command=git).place(relx=0.1, y=325)
            Button(self, text="Facebook", bg="#3b5998", borderwidth=0, fg="white", width=20,
                   height=5, font=("Arial",), cursor="hand2", command=face).place(relx=0.4, y=325)
            Button(self, text=" Instagram", bg="#d113ae", borderwidth=0, fg="white", width=20, height=5,
                   font=("Arial",), cursor="hand2", command=insta).place(relx=0.7, y=325)

            btn = Button(self, text="Logout", bg="white",  fg="red", font=("Arial", 15), command=logout,
                         width=20, height=3, cursor="hand2")
            btn.place(relx=0.4, y=500)

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

    class InsertPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg="white")


            def insertdata(firstname2, lastname2, fathername2, mobile2, email2, gender2, dateofbirth2, rollno2, branch2, batch2, sem2, cname2):
                c.execute(f"INSERT INTO studentinfo values('{firstname2}', '{lastname2}',"
                          f" '{fathername2}', {mobile2}, '{email2}', '{gender2}', '{dateofbirth2}', '{rollno2}',"
                          f" '{branch2}', {batch2}, {sem2}, '{cname2}')")
                conn.commit()
                messagebox.showinfo("Data Inserted", "1 Record Added.")
                firstname.delete(0, END)
                lastname.delete(0, END)
                fname.delete(0, END)
                mnumber.delete(0, END)
                email.delete(0, END)
                dob.delete(0, END)
                rollno.delete(0, END)
                branch.set("Select Branch")
                batch.set("Select Batch")
                sem.set("Select Semester")
                cname.delete(0, END)

                controller.show_frame(HomePage)

            Label(self, text="Insert Data", bg="#a5b0f2", width=109, height=2, font=('Arial', 15)).pack()

            Label(self, text="Personal Information:", bg="white", font=("arial", 15, "underline")).place(x=100, y=80)

            Label(self, text="First name : ", bg="white", font=("Arial", 15)).place(x=30, y=130)
            firstname = Entry(self, font=("Arial", 15))
            firstname.place(x=250, y=130)
            Label(self, text="Last name : ", bg="white", font=("Arial", 15)).place(x=30, y=180)
            lastname = Entry(self, font=("Arial", 15))
            lastname.place(x=250, y=180)
            Label(self, text="Father's name : ", bg="white", font=("Arial", 15)).place(x=30, y=230)
            fname = Entry(self, font=("Arial", 15))
            fname.place(x=250, y=230)
            Label(self, text="Mobile number : ", bg="white", font=("Arial", 15)).place(x=30, y=280)
            mnumber = Entry(self, font=("Arial", 15))
            mnumber.place(x=250, y=280)
            Label(self, text="Email : ", bg="white", font=("Arial", 15)).place(x=30, y=330)
            email = Entry(self, font=("Arial", 15))
            email.place(x=250, y=330)
            Label(self, text="Gender : ", bg="white", font=("Arial", 15)).place(x=30, y=380)
            gender = StringVar()
            option = ['Male', 'Female']
            gender.set("Select Gender")
            OptionMenu(self, gender, *option).place(x=250, y=380)
            Label(self, text="Date of Birth : ", bg="white", font=("Arial", 15)).place(x=30, y=430)
            dob = DateEntry(self, font=("Arial", 15), date_pattern='dd/mm/yyyy')
            dob.place(x=250, y=430)


            # Line

            Label(self, text="", height="27", bg="#a5b0f2").place(y=52, x=600)

            # Academic Information

            Label(self, text="Academic Information:", bg="white", font=("Arial", 15, "underline")).place(x=800, y=80)
            Label(self, text="Roll No : ", bg="white", font=("Arial", 15)).place(x=710, y=160)
            rollno = Entry(self, font=("Arial", 15))
            rollno.place(x=930, y=160)
            branch = StringVar()
            options = ['Betch', 'BCA', 'Bsc.IT', 'BBA', 'BA']
            branch.set("Select a Branch")
            Label(self, text="Branch : ", bg="white", font=("Arial", 15)).place(x=710, y=210)
            OptionMenu(self, branch, *options).place(x=930, y=210)
            batch = IntVar()
            options2 = [2017, 2018, 2019, 2020, 2021]
            batch.set("Select Batch")
            Label(self, text="Batch : ", bg="white", font=("Arial", 15)).place(x=710, y=260)
            OptionMenu(self, batch, *options2).place(x=930, y=260)
            sem = StringVar()
            sem.set("Select Semester")
            options3 = [1, 2, 3, 4, 5, 6, 7, 8]
            Label(self, text="Semester : ", bg="white", font=("Arial", 15)).place(x=710, y=310)
            OptionMenu(self, sem, *options3).place(x=930, y=310)
            Label(self, text="College name : ", bg="white", font=("Arial", 15)).place(x=710, y=360)
            cname = Entry(self, font=("Arial", 15))
            cname.place(x=930, y=360)

            Button(self, text="Insert", command=lambda: insertdata(firstname.get(), lastname.get(), fname.get(), mnumber.get(), email.get(), gender.get(), dob.get(), rollno.get(), branch.get(), batch.get(), sem.get(), cname.get()), bg="green", fg="white", width="50", font=("Arial"), cursor="hand2").place(x=325, y=500)
            Button(self, text="Home", command=lambda: controller.show_frame(HomePage), bg="red", fg="white", width="50", font=("arial"), cursor="hand2").place(x=325, y=550)

    class UpdatePage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg="white")

            def mydata(search):
                try:
                    c.execute(f"Select * from studentinfo WHERE rollno = '{search}'")
                    rs = c.fetchall()
                    for row in rs:
                        firstname.insert(0, row[0])
                        lastname.insert(0, row[1])
                        fname.insert(0, row[2])
                        mnumber.insert(0, row[3])
                        email.insert(0, row[4])
                        gender.set(row[5])
                        dob.insert(0, row[6])
                        rollno.insert(0, row[7])
                        branch.set(row[8])
                        batch.set(row[9])
                        sem.set(row[10])
                        cname.insert(0, row[11])

                except Exception as e:
                    print(e)

            def updatedata(firstname2, lastname2, fname2, mnumber2, email2, gender2, dob2, rollno2, branch2, batch2, sem2, cname2):
                try:
                    c.execute(f"UPDATE studentinfo SET firstname = '{firstname2}', lastname = '{lastname2}',"
                              f" fathername = '{fname2}', mobile = '{mnumber2}', email = '{email2}',"
                              f" gender = '{gender2}', dateofbirth = '{dob2}', rollno = '{rollno2}',"
                              f" branch = '{branch2}', batch = '{batch2}', semester = '{sem2}',"
                              f" clgname = '{cname2}' WHERE rollno = '{rollno.get()}'")
                    conn.commit()
                except Exception as e:
                    print(e)
                messagebox.showinfo("Update", "Record Updated Successfully.")
                controller.show_frame(HomePage)

            Label(self, text="Update Data", bg="#a5b0f2", width=109, height=2, font=('Arial', 15)).pack()
            Label(self, text="Enter Rollno: ", font=('arial', 15)).place(relx=0.3, y=75)
            search = Entry(self, fon=("arial", 15))
            search.place(relx=0.42, y=75)
            Button(self, text="Search", font=('arial', 11), cursor="hand2",
                   command=lambda : mydata(search.get())).place(relx=0.62, y=75)

            Label(self, text="First name : ", bg="white", font=("Arial", 15)).place(x=30, y=130)
            firstname = Entry(self, font=("Arial", 15))
            firstname.place(x=250, y=130)
            Label(self, text="Last name : ", bg="white", font=("Arial", 15)).place(x=30, y=180)
            lastname = Entry(self, font=("Arial", 15))
            lastname.place(x=250, y=180)
            Label(self, text="Father's name : ", bg="white", font=("Arial", 15)).place(x=30, y=230)
            fname = Entry(self, font=("Arial", 15))
            fname.place(x=250, y=230)
            Label(self, text="Mobile number : ", bg="white", font=("Arial", 15)).place(x=30, y=280)
            mnumber = Entry(self, font=("Arial", 15))
            mnumber.place(x=250, y=280)
            Label(self, text="Email : ", bg="white", font=("Arial", 15)).place(x=30, y=330)
            email = Entry(self, font=("Arial", 15))
            email.place(x=250, y=330)
            Label(self, text="Gender : ", bg="white", font=("Arial", 15)).place(x=30, y=380)
            gender = StringVar()
            option = ['Male', 'Female']
            OptionMenu(self, gender, *option).place(x=250, y=380)

            Label(self, text="Date of Birth : ", bg="white", font=("Arial", 15)).place(x=30, y=430)
            dob = Entry(self, font=("Arial", 15))
            dob.place(x=250, y=430)

            # Line

            Label(self, text="", height="27", bg="#a5b0f2").place(y=130, x=600)

            # Academic Information

            Label(self, text="Roll No : ", bg="white", font=("Arial", 15)).place(x=710, y=160)
            rollno = Entry(self, font=("Arial", 15))
            rollno.place(x=930, y=160)
            branch = StringVar()
            options = ['Betch', 'BCA', 'Bsc.IT', 'BBA', 'BA']
            branch.set("Select a Branch")
            Label(self, text="Branch : ", bg="white", font=("Arial", 15)).place(x=710, y=210)
            OptionMenu(self, branch, *options).place(x=930, y=210)
            batch = IntVar()
            options2 = [2017, 2018, 2019, 2020, 2021]
            batch.set("Select Batch")
            Label(self, text="Batch : ", bg="white", font=("Arial", 15)).place(x=710, y=260)
            OptionMenu(self, batch, *options2).place(x=930, y=260)
            sem = StringVar()
            sem.set("Select Semester")
            options3 = [1, 2, 3, 4, 5, 6, 7, 8]
            Label(self, text="Semester : ", bg="white", font=("Arial", 15)).place(x=710, y=310)
            OptionMenu(self, sem, *options3).place(x=930, y=310)
            Label(self, text="College name : ", bg="white", font=("Arial", 15)).place(x=710, y=360)
            cname = Entry(self, font=("Arial", 15))
            cname.place(x=930, y=360)

            Button(self, text="Update", command=lambda : updatedata(firstname.get(), lastname.get(), fname.get(),
                                                                    mnumber.get(), email.get(), gender.get(),
                                                                    dob.get(), rollno.get(), branch.get(),
                                                                    batch.get(), sem.get(),
                                                                    cname.get()), bg="yellow", fg="black",
                                                        width="50", font=("Arial"), cursor="hand2").place(x=325, y=500)
            Button(self, text="Home", command=lambda : controller.show_frame(HomePage), bg="red", fg="white",
                                                        width="50", font=("Arial"), cursor="hand2").place(x=325, y=550)


    class DeletePage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg="white")

            def deleteme(roll):
                # messagebox.askyesno("Delete Record", "Are You Sure.")
                c.execute(f"SELECT * from studentinfo WHERE rollno = '{roll.get()}'")
                rs = c.fetchall()
                if rs:
                    a = messagebox.askyesno("Delete Record", "Are You Sure.")
                    if a:
                        c.execute(f"DELETE FROM studentinfo WHERE rollno = '{roll.get()}'")
                        conn.commit()
                        messagebox.showinfo("Deleted", "Record Delete Successfully.")
                        controller.show_frame(DeletePage)
                else:
                    messagebox.showerror("No Data", "No Record Found")

            def showdata2():
                i = 4
                c.execute(f"SELECT * from studentinfo")
                Label(self, text="").grid(row=2)
                Label(self, text="First Name", font=("arial", 12), width=10).grid(row=3, column=3)
                Label(self, text="Last Name", font=("arial", 12), width=10).grid(row=3, column=4)
                Label(self, text="Father Name", font=("arial", 12), width=10).grid(row=3, column=5)
                Label(self, text="Mobile", font=("arial", 13), width=10).grid(row=3, column=6)
                Label(self, text="Email", font=("arial", 13), width=10).grid(row=3, column=7)
                Label(self, text="Gender", font=("arial", 13), width=10).grid(row=3, column=8)
                Label(self, text="Date of Birth", font=("arial", 12), width=10).grid(row=3, column=9)
                Label(self, text="Roll No", font=("arial", 13), width=10).grid(row=3, column=10)
                Label(self, text="Branch", font=("arial", 13), width=10).grid(row=3, column=11)
                Label(self, text="Batch", font=("arial", 13), width=10).grid(row=3, column=12)
                Label(self, text="Semester", font=("arial", 13), width=10).grid(row=3, column=13)
                Label(self, text="College", font=("arial", 13), width=10).grid(row=3, column=14)


                for student in c:
                    for j in range(len(student)):
                        e = Label(self, font=("arial", 10), fg='blue', bg="white")
                        e.grid(row=i, column=j + 3)
                        e.config(text=student[j])
                    Label(self, text="", width=169, height=0, borderwidth=0, bg="pink", fg="white"). \
                        grid(row=i + 1, columnspan=15, column=2)
                    i = i + 2

            Label(self, text="Delete Data", bg="#a5b0f2", width=109, height=2, font=('Arial', 15)).\
                grid(row=0, column=0, columnspan=19)
            Label(self, text="Enter Rollno: ", font=("arial", 12)).grid(row=1, column=4, columnspan=3)
            dele = Entry(self, font=("arial", 12))
            dele.grid(row=1, column=6, columnspan=2)
            Button(self, text="Delete", font=("arial", 11), cursor="hand2", command=lambda : deleteme(dele)).\
                grid(row=1, column=2, columnspan=12)
            Button(self, text="Show Data", font=("arial", 11), cursor="hand2", command=showdata2). \
                grid(row=1, column=4, columnspan=12)
            Button(self, text="Home", font=("arial", 11), bg="red", fg="white", borderwidth=0, cursor="hand2",
                   command=lambda : controller.show_frame(HomePage)).grid(row=1, column=7, columnspan=12)

    class Application(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            # creating a window/Frame
            window = Frame(self)
            window.pack()

            window.grid_rowconfigure(0, minsize=600)
            window.grid_columnconfigure(0, minsize=1200)

            self.frames = {}
            for F in (LoginPage, RegisterPage, HomePage, InsertPage, UpdatePage, DeletePage):
                frame = F(window, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(LoginPage)

        def show_frame(self, page):
            frame = self.frames[page]
            frame.tkraise()
            self.title("School Management System")

    app = Application()
    app.resizable(0, 0)
    app.iconbitmap('images/favicon.ico')
    app.geometry("1200x600+170+100")
    app.mainloop()


progress = ttk.Progressbar(splash_root, length=700)
progress.place(rely=0.985, relx=0)
progress.step(20)
progress.start()
splash_root.after(5000, main)
splash_root.mainloop()
