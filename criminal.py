# from time import clock_getres
from ast import Delete
from cgitb import text
from dataclasses import dataclass
import imp
from logging.config import valid_ident
from msilib.schema import Verb
from signal import getsignal
from tkinter import*
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import left, right, st, update, width
from winsound import MessageBeep
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        root.state("zoomed")
        self.root.title("Criminal Management System")


        #variables
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_crime=StringVar()
        self.var_year=StringVar()
        self.var_country=StringVar()
        self.var_gender=StringVar()
        self.var_marks=StringVar()
        self.var_other_details=StringVar()
        self.var_address=StringVar()
        self.var_city=StringVar()
        self.var_state=StringVar()


        #1
        img1=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\label1.jpg")
        img1=img1.resize((425,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=0,y=0,width=425,height=200)


        #2
        img2=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\label2.jpg")
        img2=img2.resize((425,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=425,y=0,width=425,height=200)

        #3
        img3=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\label3.jpg")
        img3=img3.resize((430,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        first_label=Label(self.root,image=self.photoimg3)
        first_label.place(x=850,y=0,width=430,height=200)


        #bg
        bgimg=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\bg.jpg")
        bgimg=bgimg.resize((1300,450),Image.ANTIALIAS)
        self.photoimgbg=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=200,width=1300,height=450)

        title_label=Label(bg_img,text="CRIMINAL MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="#F3E1FF",fg="#5F00A0")
        title_label.place(x=0,y=0,width=1300,height=35)


        #frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=12,y=42,width=1250,height=398)


        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=550,height=385)


        img_left=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\sample.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=535,height=85) 


        #criminal frame
        crime_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Crime Details",font=("times new roman",12,"bold"))
        crime_frame.place(x=5,y=50,width=535,height=92)


        #name
        name_label=Label(crime_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=0,padx=10,pady=5)

        name_textbox=ttk.Entry(crime_frame,textvariable=self.var_name)
        name_textbox.grid(row=0,column=1,padx=2,pady=5,sticky=W)


        #crime
        crime_label=Label(crime_frame,text="Crime",font=("times new roman",12,"bold"),bg="white")
        crime_label.grid(row=0,column=2,padx=10,sticky=W)

        crime_combo=ttk.Combobox(crime_frame,textvariable=self.var_crime,font=("times new roman",12,"bold"),state="readonly")
        crime_combo["values"]=("Select Crime","Assault","Domestic Violence","Murder","Robbery","Theft")
        crime_combo.current(0)
        crime_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)


        #year
        year_label=Label(crime_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_textbox=ttk.Entry(crime_frame,textvariable=self.var_year)
        year_textbox.grid(row=1,column=1,padx=2,pady=5,sticky=W)


        #nationality
        nationality_label=Label(crime_frame,text="Country",font=("times new roman",12,"bold"),bg="white")
        nationality_label.grid(row=1,column=2,padx=10,sticky=W)

        nationality_textbox=ttk.Entry(crime_frame,textvariable=self.var_country,width=29)
        nationality_textbox.grid(row=1,column=3,padx=2,pady=5,sticky=W)


        #criminal info
        criminal_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Information",font=("times new roman",12,"bold"))
        criminal_frame.place(x=5,y=147,width=535,height=211)


        #criminal id
        criminalId_label=Label(criminal_frame,text="Criminal Id",font=("times new roman",12,"bold"),bg="white")
        criminalId_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)

        criminalId_textbox=ttk.Entry(criminal_frame,textvariable=self.var_id,width=15,font=("times new roman",12,"bold"))
        criminalId_textbox.grid(row=0,column=1,padx=5,pady=2,sticky=W)


        #gender id
        gender_label=Label(criminal_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=0,column=2,padx=5,pady=2,sticky=W)

        gender_combo=ttk.Combobox(criminal_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)


        #marks id
        marks_label=Label(criminal_frame,text="Marks",font=("times new roman",12,"bold"),bg="white")
        marks_label.grid(row=1,column=0,padx=5,pady=2,sticky=W)

        marks_textbox=ttk.Entry(criminal_frame,textvariable=self.var_marks,width=15,font=("times new roman",12,"bold"))
        marks_textbox.grid(row=1,column=1,padx=5,pady=2,sticky=W)


        #others id
        marks_label=Label(criminal_frame,text="Other Details",font=("times new roman",12,"bold"),bg="white")
        marks_label.grid(row=1,column=2,padx=5,pady=2,sticky=W)

        marks_textbox=ttk.Entry(criminal_frame,textvariable=self.var_other_details,width=15,font=("times new roman",12,"bold"))
        marks_textbox.grid(row=1,column=3,padx=5,pady=2,sticky=W)


        #address id
        address_label=Label(criminal_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=2,column=0,padx=5,pady=2,sticky=W)

        address_textbox=ttk.Entry(criminal_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        address_textbox.grid(row=2,column=1,padx=5,pady=2,sticky=W)


        #city id
        city_label=Label(criminal_frame,text="City",font=("times new roman",12,"bold"),bg="white")
        city_label.grid(row=3,column=0,padx=5,pady=2,sticky=W)

        city_textbox=ttk.Entry(criminal_frame,textvariable=self.var_city,width=15,font=("times new roman",12,"bold"))
        city_textbox.grid(row=3,column=1,padx=5,pady=2,sticky=W)


        #state id
        state_label=Label(criminal_frame,text="State",font=("times new roman",12,"bold"),bg="white")
        state_label.grid(row=3,column=2,padx=5,pady=2,sticky=W)

        state_textbox=ttk.Entry(criminal_frame,textvariable=self.var_state,width=15,font=("times new roman",12,"bold"))
        state_textbox.grid(row=3,column=3,padx=5,pady=2,sticky=W)


        #button frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=12,y=292,width=512,height=32)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=13,font=("times new roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #button frame 1
        btn_frame1=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=12,y=325,width=512,height=29)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=27,font=("times new roman",11,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=1)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=28,font=("times new roman",11,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=2)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Records",font=("times new roman",12,"bold"))
        right_frame.place(x=685,y=5,width=550,height=385)


        img_right=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\sample.jpeg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=535,height=85)


        #system search
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=50,width=535,height=70)


        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select","Criminal Id","Crime")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showAll_btn=Button(search_frame,text="Show All",width=11,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)


        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=125,width=535,height=220)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=("name","crime","year","country","criminalId","gender","marks","other_details","address","city","state"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("name",text="NAME")
        self.criminal_table.heading("crime",text="CRIME")
        self.criminal_table.heading("year",text="YEAR")
        self.criminal_table.heading("country",text="COUNTRY")
        self.criminal_table.heading("criminalId",text="CRIMINAL Id")
        self.criminal_table.heading("gender",text="GENDER")
        self.criminal_table.heading("marks",text="MARKS")
        self.criminal_table.heading("other_details",text="OTHER")
        self.criminal_table.heading("address",text="ADDRESS")
        self.criminal_table.heading("city",text="CITY")
        self.criminal_table.heading("state",text="STATE")
        self.criminal_table["show"]="headings"

        self.criminal_table.column("name",width=80)
        self.criminal_table.column("crime",width=100)
        self.criminal_table.column("year",width=100)
        self.criminal_table.column("country",width=100)
        self.criminal_table.column("criminalId",width=100)
        self.criminal_table.column("gender",width=60)
        self.criminal_table.column("marks",width=100)
        self.criminal_table.column("other_details",width=100)
        self.criminal_table.column("address",width=180)
        self.criminal_table.column("city",width=60)
        self.criminal_table.column("state",width=80)


        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #function
    def add_data(self):
        if self.var_name.get()=="Enter Name" or self.var_crime.get()=="" or self.var_year.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="criminal@2022",database="criminal")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into crime_record values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                            self.var_name.get(),
                                            self.var_crime.get(),
                                            self.var_year.get(),
                                            self.var_country.get(),
                                            self.var_id.get(),
                                            self.var_gender.get(),
                                            self.var_marks.get(),
                                            self.var_other_details.get(),
                                            self.var_address.get(),
                                            self.var_city.get(),
                                            self.var_state.get()
                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Criminal details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        

    # fetch data 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="criminal@2022",database="criminal")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from crime_record")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_focus)
        data=content["values"]

        self.var_name.set(data[0])
        self.var_crime.set(data[1])
        self.var_year.set(data[2])
        self.var_country.set(data[3])
        self.var_id.set(data[4])
        self.var_gender.set(data[5])
        self.var_marks.set(data[6])
        self.var_other_details.set(data[7])
        self.var_address.set(data[8])
        self.var_city.set(data[9])
        self.var_state.set(data[10])

    #update function
    def update_data(self):
        if self.var_name.get()=="Enter Name" or self.var_crime.get()=="" or self.var_year.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update criminal details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="criminal@2022",database="criminal")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update criminal set Name=%s,Crime=%s,Year=%s,Country=%s,Gender=%s,Marks=%s,Other_Details=%s,Address=%s,City=%s,State=%s where Id=%s",(
                                        self.var_name.get,
                                        self.var_crime.get(),
                                        self.var_year.get(),
                                        self.var_country.get(),
                                        self.var_gender.get(),
                                        self.var_marks.get(),
                                        self.var_other_details.get(),
                                        self.var_address.get(),
                                        self.var_city.get(),
                                        self.var_state.get(),
                                        self.var_id.get()
                                    ))    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Criminal details successfully updated",parent=self.root)  
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     


    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Criminal id reequired",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Criminal Page Delete","Do yo want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="criminal@2022",database="criminal")
                    my_cursor=conn.cursor()
                    sql="delete from crime_record where CRIMINAL Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted criminal details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()