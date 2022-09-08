from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from criminal import Criminal

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        root.state("zoomed")
        self.root.title("Face Recognition System")

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

        title_label=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="#F3E1FF",fg="#5F00A0")
        title_label.place(x=0,y=0,width=1300,height=35)


        #criminal button
        criminal=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\criminal.jpg")
        criminal=criminal.resize((120,120),Image.ANTIALIAS)
        self.photoimgcriminal=ImageTk.PhotoImage(criminal)

        b1=Button(bg_img,image=self.photoimgcriminal,command=self.criminal_details,cursor="hand2")
        b1.place(x=90,y=70,width=120,height=120)

        b1_1=Button(bg_img,text="Criminal Details",command=self.criminal_details,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=90,y=180,width=120,height=20)


        #face detector button
        face_detector=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\face_detector.jpg")
        face_detector=face_detector.resize((120,120),Image.ANTIALIAS)
        self.photoimgdetector=ImageTk.PhotoImage(face_detector)

        b2=Button(bg_img,image=self.photoimgdetector,cursor="hand2")
        b2.place(x=390,y=70,width=120,height=120)

        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=390,y=180,width=120,height=20)


        #criminal record button
        criminal_record=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\record.jpeg")
        criminal_record=criminal_record.resize((120,120),Image.ANTIALIAS)
        self.photoimgrecord=ImageTk.PhotoImage(criminal_record)

        b3=Button(bg_img,image=self.photoimgrecord,cursor="hand2")
        b3.place(x=690,y=70,width=120,height=120)

        b3_3=Button(bg_img,text="Criminal Details",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=690,y=180,width=120,height=20)


        #train data button
        train_data=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\train.jpeg")
        train_data=train_data.resize((120,120),Image.ANTIALIAS)
        self.photoimgtrain=ImageTk.PhotoImage(train_data)

        b4=Button(bg_img,image=self.photoimgtrain,cursor="hand2")
        b4.place(x=990,y=70,width=120,height=120)

        b4_4=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=990,y=180,width=120,height=20)


        #photos button
        photos=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\photos.jpeg")
        photos=photos.resize((120,120),Image.ANTIALIAS)
        self.photoimgphotos=ImageTk.PhotoImage(photos)

        b5=Button(bg_img,image=self.photoimgphotos,cursor="hand2")
        b5.place(x=90,y=270,width=120,height=120)

        b5_5=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=90,y=380,width=120,height=20)


        #developer button
        developer=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\developer.jpeg")
        developer=developer.resize((120,120),Image.ANTIALIAS)
        self.photoimgdeveloper=ImageTk.PhotoImage(developer)

        b6=Button(bg_img,image=self.photoimgdeveloper,cursor="hand2")
        b6.place(x=390,y=270,width=120,height=120)

        b6_6=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=390,y=380,width=120,height=20)


        #help button
        help=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\help.jpeg")
        help=help.resize((120,120),Image.ANTIALIAS)
        self.photoimghelp=ImageTk.PhotoImage(help)

        b7=Button(bg_img,image=self.photoimghelp,cursor="hand2")
        b7.place(x=690,y=270,width=120,height=120)

        b7_7=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=690,y=380,width=120,height=20)


        #exit button
        exit=Image.open(r"C:\Users\priya\OneDrive\Desktop\FACE_RECOGNITION+ATTENDANCE\images\exit.jpeg")
        exit=exit.resize((120,120),Image.ANTIALIAS)
        self.photoimgexit=ImageTk.PhotoImage(exit)

        b8=Button(bg_img,image=self.photoimgexit,cursor="hand2")
        b8.place(x=990,y=270,width=120,height=120)

        b8_8=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=990,y=380,width=120,height=20)


        #function button
    def criminal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Criminal(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()