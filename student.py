from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Student:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("STUDENT ATTENDANCE MONITORING SYSTEM")

        #==============variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        
        
       

        #First Image
        img=Image.open(r"C:\Users\Rai\Desktop\Raj\face_recognition\images\mct.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=130)

        #second Image
        img1=Image.open(r"C:\Users\Rai\Desktop\Raj\face_recognition\images\mct.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=430,y=0,width=430,height=130)

        #third image
        img2=Image.open(r"C:\Users\Rai\Desktop\Raj\face_recognition\images\mct.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=860,y=0,width=430,height=130)

        
        #bgimage
        img3=Image.open(r"C:\Users\Rai\Desktop\Raj\face_recognition\images\bg.jpg")
        img3=img3.resize((1300,700),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)
        
        #title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width="1300",height="40")

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=45,width=1250,height=500)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=450)

        img_left=Image.open(r"C:\Users\Rai\Desktop\Raj\face_recognition\images\mct.jpeg")
        img_left=img_left.resize((595,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=595,height=100)

        #Current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=105,width=595,height=90)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,sticky="W")

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","COMPUTER","IT","AIDS","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=8,sticky="W")

        
        #Course
        dep_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,sticky="W")

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Course","FE","SE","TE","BE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=8,sticky="W")

        #Year
        dep_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,sticky="W")

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Year","2021-2022","2022-2023","2023-2024","2024-2025")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=8,pady=10,sticky="W")

        
        #Semester
        dep_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,sticky="W")

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Semester","First Half","Second Half")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=8,pady=10,sticky="W")
        
        #Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=195,width=595,height=230)  
        
        #StudentID
        StudentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",11,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,sticky="W")

        StudentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",11,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky="W")
        
        #Student Name
        StudentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,sticky="W")

        StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",11,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,sticky="W")

         #ClassDivision
        ClassDIV_label=Label(class_student_frame,text="Division:",font=("times new roman",11,"bold"),bg="white")
        ClassDIV_label.grid(row=1,column=0,padx=10,pady=5,sticky="W")

        #ClassDIV_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",11,"bold"))
        #ClassDIV_entry.grid(row=1,column=1,padx=10,pady=5,sticky="W")

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky="W")

         #Roll No
        Rollno_label=Label(class_student_frame,text="Roll No:",font=("times new roman",11,"bold"),bg="white")
        Rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky="W")

        Rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times new roman",11,"bold"))
        Rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky="W")

        #Gender
        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",11,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky="W")

       # Gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman",11,"bold"))
       # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky="W")

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky="W")

        #DOB
        DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",11,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky="W")

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",11,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky="W")

        #Email
        Email_label=Label(class_student_frame,text="Email:",font=("times new roman",11,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky="W")

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",11,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky="W")

        #PhoneNO
        PhoneNo_label=Label(class_student_frame,text="Phone No:",font=("times new roman",11,"bold"),bg="white")
        PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky="W")

        PhoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",11,"bold"))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky="W")

        #radiobuttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0) 
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=1)

        #buttonframe
        btn_frame=Frame(class_student_frame,bd=1.5,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=140,width=590,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data_fn,width=15,font=("times new roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=1.5,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=175,width=590,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=31,font=("times new roman",11,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)










        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=600,height=450)

        img_right=Image.open(r"C:\Users\Rai\Desktop\Raj\face_recognition\images\mct.jpeg")
        img_right=img_right.resize((595,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=580,height=100)


        #-------------Search System---------------

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=105,width=580,height=60)  
        
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_label.grid(row=0,column=0,padx=8,pady=5,sticky="W")

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",10,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=6,pady=10,sticky="W")

        search_entry=ttk.Entry(Search_frame,width=13,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky="W")
        
        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=2)

        showall_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2)

        #----------Table frame-----------
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=580,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       
  #==========function==========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='ahppr2367f',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                           self.var_dep.get(),
                                                                                           self.var_course.get(),
                                                                                           self.var_year.get(),
                                                                                           self.var_semester.get(),
                                                                                           self.var_std_id.get(),
                                                                                           self.var_std_name.get(),
                                                                                           self.var_div.get(),
                                                                                           self.var_roll.get(),
                                                                                           self.var_dob.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_gender.get(),
                                                                                           self.var_phone.get(),
                                                                                           self.var_radio1.get(),              
                                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


#===========fetch data=============

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='ahppr2367f',database='face_recognition')
        my_cursor=conn.cursor()   
        my_cursor.execute("select * from student")  
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

#===========get cursor=====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])      
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_radio1.set(data[12])
  
#========updata function========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update data?",parent=self.root)  
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='ahppr2367f',database='face_recognition')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Dob=%s,Email=%s,gender=%s,phone=%s,photosample=%s where Student_id=%s",(

                                                                                           self.var_dep.get(),
                                                                                           self.var_course.get(),
                                                                                           self.var_year.get(),
                                                                                           self.var_semester.get(),
                                                                                           self.var_std_name.get(),
                                                                                           self.var_div.get(),
                                                                                           self.var_roll.get(),
                                                                                           self.var_dob.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_gender.get(),
                                                                                           self.var_phone.get(),
                                                                                           self.var_radio1.get(),
                                                                                           self.var_std_id.get(),              
                                                                                                   ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated!",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root)

#=========delete function=============

    def delete_data_fn(self):
        if self.var_std_id.get()=="":
           messagebox.showerror("Error","Student id is required!",parent=self.root)      
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this data?",parent=self.root) 
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='ahppr2367f',database='face_recognition')
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Data deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root)     

#========reset function=========

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),  
        self.var_dob.set(""),                                                         
        self.var_email.set(""),   
        self.var_gender.set("Male"),
        self.var_phone.set(""),
        self.var_radio1.set(""),                    






                    



              



   







if __name__ == "__main__":

    root=Tk()
    obj=Student(root)
    root.mainloop()     
