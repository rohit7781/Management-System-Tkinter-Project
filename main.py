from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time
import webbrowser
from PIL import ImageTk, Image

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


    class LoginPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg='white')

            def check(username, password):
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Sahil@123", database="studentrecord")
                c = conn.cursor()
                c.execute(f"SELECT username,password FROM adminrecord where username = '{username}' and password='{password}'")
                result = c.fetchall()
                if result:
                    label1.place_forget()
                    label2.place_forget()
                    controller.show_frame(HomePage)
                else:
                    messagebox.showerror("Error", "No Data Found")
                conn.commit()

            def register():
                label1.place_forget()
                label2.place_forget()
                controller.show_frame(RegisterPage)

            def showimage():
                label1.place(x=0, y=0)
                label2.place(relx=0.8, rely=0.02)

                # Main Big
            image1 = Image.open("images/img6.jpg")
            resize = image1.resize((800, 595), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize)
            label1 = Label(image=test)
            label1.image = test
            label1.place(x=0, y=0)

                # Small Icon
            image2 = Image.open("images/login.png")
            resize = image2.resize((100, 100), Image.ANTIALIAS)
            test2 = ImageTk.PhotoImage(resize)
            label2 = Label(image=test2, bg="white")
            label2.image = test2
            label2.place(relx=0.8, rely=0.02)

            intro = Label(self, bg="white", text="School\nManagement\nSystem", font=("arial", 70)).place(relx=0.10, rely=0.15)
            intro = Label(self, bg="white", fg="tomato", text="Created by Sahil Sharma", font=("arial", 30)).place(relx=0.16, rely=0.8)

            Label(self, text="Sign In: ", fg="white", font=("Arial", 15, "underline"), bg="blue").place(relx=0.8, rely=0.20)
            Label(self, text="Username:", font=("Arial", 15), bg="white").place(relx=0.7, rely=0.25)
            username = Entry(self, font=("arial", 15), width=29)
            username.place(relx=0.7, rely=0.32)
            Label(self, text="Password:", font=("arial", 15), bg="white").place(relx=0.7, rely=0.43)
            password = Entry(self, font=("arial", 15), width=29)
            password.place(relx=0.7, rely=0.5)
            Button(self, text="Login", cursor="hand2", borderwidth=0, width=29, bg="blue", fg="white", font=("Arial", 15), command=lambda: check(username.get(), password.get())).place(relx=0.7, rely=0.6)
            Button(self, text="Register", cursor="hand2", borderwidth=0, width=29, bg="red", fg="white", font=("Arial", 15), command=register).place(relx=0.7, rely=0.68)
            Button(self, text="Show Image", cursor="hand2", borderwidth=0, width=29, bg="skyblue", fg="black", font=("Arial", 15), command=showimage).place(relx=0.7, rely=0.76)


    class RegisterPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)

            self.configure(bg='white')
            def insert(username, password, email, mobile):
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Sahil@123", database="studentrecord")
                c = conn.cursor()
                c.execute(f"INSERT INTO adminrecord VALUES('{username}', '{password}', '{email}', {mobile})")
                conn.commit()
                controller.show_frame(LoginPage)

            Label(self, text="Register new User", bg="#a5b0f2", width=109, height=2, font=('Arial')).pack()
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
            Button(self, bg="red", cursor="hand2", borderwidth=0, fg="white", text="Register", font=("arial", 15), width=31, command=lambda: insert(username.get(), password.get(), email.get(), mobile.get())).place(relx=0.2, rely=0.6)

            Label(self, text="", height=36, bg="#a5b0f2").place(relx=0.6, rely=0.088)

            Label(self, bg="white", text="Already have an Account:", font=("arial", 15, "underline")).place(relx=0.7, rely=0.3)
            Button(self, cursor="hand2", borderwidth=0, bg="blue", fg="white", text="Login", width=30, font=("arial", 15), command=lambda: controller.show_frame(LoginPage)).place(relx=0.66, rely=0.4)

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

            Label(self, text="Student Management System", bg="#a5b0f2", width=109, height=2, font=('Arial')).pack()
            Label(self, text="Welcome Sahil", bg="white", fg="black", font=("Arial",)).place(y=55, x=10)
            time_string = time.strftime('%H:%M')
            Label(self, text=f"Time : {time_string}", fg="black", bg="white", font=("Arial",)).place(relx=0.88, y=55)

            Button(self, text="Insert Data", bg="#612cc9", borderwidth=0, fg="white", width=20, height=5, font=("arial",), cursor="hand2", command=lambda: controller.show_frame(InsertPage)).place(relx=0.1, y=125)
            Button(self, text="Update Data", bg="yellow", borderwidth=0, fg="black", width=20, height=5, font=("Arial",), cursor="hand2", command=lambda: controller.show_frame(UpdatePage)).place(relx=0.4, y=125)
            Button(self, text="Delete Data", bg="red", borderwidth=0, fg="white", width=20, height=5, font=("Arial",), cursor="hand2", command=lambda: controller.show_frame(DeletePage)).place(relx=0.7, y=125)
            Button(self, text="GitHub", bg="#24292e", borderwidth=0, fg="white", width=20, height=5, font=("Arial",), cursor="hand2", command=git).place(relx=0.1, y=325)
            Button(self, text="Facebook", bg="#3b5998", borderwidth=0, fg="white", width=20, height=5, font=("Arial",), cursor="hand2", command=face).place(relx=0.4, y=325)
            Button(self, text=" Instagram", bg="#d113ae", borderwidth=0, fg="white", width=20, height=5, font=("Arial",), cursor="hand2", command=insta).place(relx=0.7, y=325)

            btn = Button(self, text="Logout", bg="white",  fg="red", font=("Arial", 15), command=logout, width=20, height=3, cursor="hand2")
            btn.place(relx=0.4, y=500)

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

    class InsertPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg="white")

            Label(self, text="Insert Data", bg="#a5b0f2", width=109, height=2, font=('Arial')).pack()

            Label(self, text="Personal Information:", bg="white", font=('arial 15 underline')).place(x=100, y=80)

            Label(self, text="First name : ", bg="white", font=("Arial 15")).place(x=30, y=130)
            firstname = Entry(self, font=("Arial 15"))
            firstname.place(x=250, y=130)
            Label(self, text="Last name : ", bg="white", font=("Arial 15")).place(x=30, y=180)
            lastname = Entry(self, font=("Arial 15"))
            lastname.place(x=250, y=180)
            Label(self, text="Father's name : ", bg="white", font=("Arial 15")).place(x=30, y=230)
            fname = Entry(self, font=("Arial 15"))
            fname.place(x=250, y=230)
            Label(self, text="Mobile number : ", bg="white", font=("Arial 15")).place(x=30, y=280)
            mnumber = Entry(self, font=("Arial 15"))
            mnumber.place(x=250, y=280)
            Label(self, text="Email : ", bg="white", font=("Arial 15")).place(x=30, y=330)
            email = Entry(self, font=("Arial 15"))
            email.place(x=250, y=330)
            Label(self, text="Gender : ", bg="white", font=("Arial 15")).place(x=30, y=380)
            gender = Entry(self, font=("Arial 15"))
            gender.place(x=250, y=380)
            Label(self, text="Date of Birth : ", bg="white", font=("Arial 15")).place(x=30, y=430)
            dob = Entry(self, font=("Arial 15"))
            dob.place(x=250, y=430)


            # Line

            Label(self, text="", height="27", bg="black").place(y=52, x=600)

            # Academic Information

            Label(self, text="Academic Information:", bg="white", font=("Arial 15 underline")).place(x=800, y=80)
            Label(self, text="Roll No : ", bg="white", font=("Arial 15")).place(x=710, y=160)
            rollno = Entry(self, font=("Arial 15"))
            rollno.place(x=930, y=160)
            Label(self, text="Branch : ", bg="white", font=("Arial 15")).place(x=710, y=210)
            branch = Entry(self, font=("Arial 15"))
            branch.place(x=930, y=210)
            Label(self, text="Batch : ", bg="white", font=("Arial 15")).place(x=710, y=260)
            batch = Entry(self, font=("Arial 15"))
            batch.place(x=930, y=260)
            Label(self, text="Semester : ", bg="white", font=("Arial 15")).place(x=710, y=310)
            semester = Entry(self, font=("Arial 15"))
            semester.place(x=930, y=310)
            Label(self, text="College name : ", bg="white", font=("Arial 15")).place(x=710, y=360)
            cname = Entry(self, font=("Arial 15"))
            cname.place(x=930, y=360)

            Button(self, text="Insert", command=lambda: controller.show_frame(HomePage), bg="green", fg="white", width="50", font=("Arial"), cursor="hand2").place(x=325, y=500)
            Button(self, text="Home", command=lambda: controller.show_frame(HomePage), bg="red", fg="white", width="50", font=("Arial"), cursor="hand2").place(x=325, y=550)

    class UpdatePage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg="brown")

            Label(self, text="Update Data", bg="#a5b0f2", width=109, height=2, font=('Arial')).pack()
            Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).pack()

    class DeletePage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.configure(bg="purple")

            Label(self, text="Delete Data", bg="#a5b0f2", width=109, height=2, font=('Arial')).pack()
            Button(self, text="Home", command=lambda: controller.show_frame(HomePage)).pack()

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
            # self.show_frame(HomePage)
            # self.show_frame(InsertPage)

        def show_frame(self, page):
            frame = self.frames[page]
            frame.tkraise()
            self.title("School Management System")

    app = Application()
    app.resizable(0, 0)
    app.geometry("1200x600+170+100")
    app.mainloop()


progress = ttk.Progressbar(splash_root, length=700)
progress.place(rely=0.985, relx=0)
progress.step(20)
progress.start()
splash_root.after(5000, main)
# splash_root.after(5, main)
splash_root.mainloop()
