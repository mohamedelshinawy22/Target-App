from tkinter import *
from datetime import date
import time
from PIL import Image,ImageTk #PIP install pillow
import webbrowser
import tkinter.font as tkFont
import os



#from employee import employeeClass

#from business_name import business_name

import sqlite3
from tkinter import messagebox
from cryptography.fernet import Fernet
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1250x700+50+5')
        self.root.resizable(False,False)
        self.root.config(bg="#06283D")
        self.root.title('AL Rashwan System || Developed By Mohamed Elshinawy')
        u1='https://www.facebook.com/mohamed.elshinawy.3158'
        def open1():
            webbrowser.open_new(u1)
        u2='https://www.instagram.com/mohamed_elshinawy1/'
        def open2():
            webbrowser.open_new(u2)
        u3='https://api.whatsapp.com/send?phone=+201006682928'
        def open3():
            webbrowser.open_new(u3)
        u4='https://www.linkedin.com/in/mohamed-elshinawy-1b2582259'
        def open4():
            webbrowser.open_new(u4)
        
        #=====Title=======
        self.icon_title=PhotoImage(file="assed\\about2.png")
        title=Label(self.root,text="شركة ال رشوان للمقاولات العامة والتوريدات   \t",image=self.icon_title,compound=RIGHT,font=("times new roman",30,"bold"),bg="#06283D",fg="white",anchor='w',padx=20).place(x=350,y=0,relwidth=1,height=70)
        #=====Button_Log out=======
        btn_logout=Button(self.root,text="Log out",font=("times new roman",15,"bold"),bg="#57a1f8",fg="white",cursor="hand2").place(x=30,y=15,height=40,width=100)    
        #=====Clock========
        arabic_font = tkFont.Font(family="Helvetica", size=18,weight='bold') 
        self.lbl_clock=Label(self.root,text="HH:MM:SS : الوقت\t\tDD-MM-YYYY : التاريخ\t\t م/ محمد رشوان \t&&\t م/ رامي رشوان",font=("times new roman",18,"bold"),bg="#7F5283",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #======Left menue===
        self.menue_logo=Image.open("assed\\menue_ph1.png")
        self.menue_logo=self.menue_logo.resize((200,140),Image.Resampling.LANCZOS)
        self.menue_logo=ImageTk.PhotoImage(self.menue_logo)
        left_menue=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        left_menue.place(x=1050,y=100,width=200,height=700) #==Hight=700 **
        
        
        lbl_menue_logo=Label(left_menue,image=self.menue_logo)
        lbl_menue_logo.pack(side=TOP,fill=X)
        self.icon_sharecat=PhotoImage(file="assed\\sharecat.png")
        self.icon_supplier=PhotoImage(file="assed\\supplier.png")
        self.icon_category=PhotoImage(file="assed\\catogory.png")

        lbl_menue=Label(left_menue,text="القائمة",font=("times new roman",20),bg="#009688",fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_sharecat=Button(left_menue,command=self.sharecat,image=self.icon_sharecat,compound=LEFT,padx=5,anchor="w",text="الشركات",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(left_menue,command=self.supplier,image=self.icon_supplier,compound=LEFT,padx=5,anchor="w",text="المقاولين",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(left_menue,command=self.category,image=self.icon_category,compound=LEFT,padx=5,anchor="w",text="الاصناف",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_sharekat_moamlat=Button(left_menue,command=self.sharekat_moamlat,image=self.icon_sharecat,compound=LEFT,padx=5,anchor="w",text="معاملات \nوحسابات الشركات",font=("times new roman",15,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_m2wleen_moamlat=Button(left_menue,command=self.m2wleen_moamlat,image=self.icon_supplier,compound=LEFT,padx=5,anchor="w",text="معاملات \nوحسابات المقاولين",font=("times new roman",15,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        
#======================= Content ===================================
        self.mohamed_logo=Image.open("assed\\WhatsApp_Image_2024-02-12_at_13.52.31_4793e57a-removebg-preview.png")
        #self.mohamed_logo=self.mohamed_logo.resize((200,140),Image.Resampling.LANCZOS)
        self.mohamed_logo=ImageTk.PhotoImage(self.mohamed_logo)
        lbl_mohamed_logo=Label(self.root,image=self.mohamed_logo).place(x=5,y=100,width=352,height=708)
        
        self.ramy_logo=Image.open("assed\\WhatsApp_Image_2024-02-12_at_14.10.30_11e10d87-removebg-preview.png")
        #self.mohamed_logo=self.mohamed_logo.resize((200,140),Image.Resampling.LANCZOS)
        self.ramy_logo=ImageTk.PhotoImage(self.ramy_logo)
        lbl_ramy_logo=Label(self.root,image=self.ramy_logo).place(x=660,y=100,width=398,height=627)
        #WhatsApp Image 2024-02-11 at 20.58.25_d96dd386
        self.logo=Image.open("assed\\WhatsApp Image 2024-02-11 at 20.58.25_d96dd386.png")
        #self.mohamed_logo=self.mohamed_logo.resize((200,140),Image.Resampling.LANCZOS)
        self.logo=ImageTk.PhotoImage(self.logo)
        lbl_logo=Label(self.root,image=self.logo).place(x=400,y=250,width=250,height=250)
        #==========================================================
        self.update_date_time()
    def sharecat(self):
        os.system("python supplier.py")
        #os.system('python de_code2.py')
    def supplier(self):
        os.system("python supplier2.py")
    def category(self):
        os.system("python category.py")
    def sharekat_moamlat(self):
        os.system("python product.py")
    def m2wleen_moamlat(self):
        os.system("python product2.py")
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d/%m/%Y")
        #Welcome To Saller User Interface System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS"
        self.lbl_clock.config(text=f"{str(time_)} : الوقت\t\t{str(date_)} : التاريخ\t\t م/ محمد رشوان \t&&\t م/ رامي رشوان")
        self.lbl_clock.after(200,self.update_date_time)
    
"""        self.icon_employee=PhotoImage(file="assed\\employee.png")
        self.icon_supplier=PhotoImage(file="assed\\supplier.png")
        self.icon_category=PhotoImage(file="assed\\catogory.png")
        self.icon_salles=PhotoImage(file="assed\\salles.png")
        self.icon_exite=PhotoImage(file="assed\\exite.png")
        lbl_menue=Label(left_menue,text="Menue",font=("times new roman",20),bg="#009688",fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_employee=Button(left_menue,command=self.employee,image=self.icon_employee,compound=LEFT,padx=5,anchor="w",text="Customer",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(left_menue,command=self.supplier,image=self.icon_supplier,compound=LEFT,padx=5,anchor="w",text="Supplier",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(left_menue,command=self.category,image=self.icon_category,compound=LEFT,padx=5,anchor="w",text="Category",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(left_menue,image=self.icon_salles,command=self.product,compound=LEFT,padx=5,anchor="w",text="Product",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_salles=Button(left_menue,command=self.sales,image=self.icon_salles,compound=LEFT,padx=5,anchor="w",text="Sales",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(left_menue,image=self.icon_exite,compound=LEFT,padx=5,anchor="w",text="Exit",font=("times new roman",20,"bold"),bg="#009688",bd=7,fg="white",cursor="hand2").pack(side=TOP,fill=X)
        self.bills_btn=Button(self.root,command=self.bills,pady=5,padx=5,text="Create Bill",fg="white",border=2,font=("times new roman",20,"bold"),bg="#009688",bd=7,cursor="hand2")
        self.bills_btn.place(x=210 , y=470,width=150,height=50)

        self.business_name_btn=Button(self.root,command=self.business_name,pady=5,padx=5,text="Business Name",fg="white",border=2,font=("times new roman",15,"bold"),bg="#009688",bd=7,cursor="hand2")
        self.business_name_btn.place(x=210 , y=530,width=150,height=50)
        
        self.returns_btn=Button(self.root,command=self.returns,pady=5,padx=5,text="Returns",fg="white",border=2,font=("times new roman",20,"bold"),bg="#009688",bd=7,cursor="hand2")
        self.returns_btn.place(x=210 , y=590,width=150,height=50)

        #=====Content=======
        self.lbl_employee=Label(self.root,text="Total Customer\n [ 0 ]",bd=5,relief=RIDGE,font=("goudy old style",20,"bold"),bg="#57a1f8",fg="white",cursor="hand2")
        self.lbl_employee.place(x=300,y=120,width=300,height=150)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n [ 0 ]",bd=5,relief=RIDGE,font=("goudy old style",20,"bold"),bg="#57a1f8",fg="white",cursor="hand2")
        self.lbl_supplier.place(x=920,y=120,width=300,height=150)
        
        self.lbl_category=Label(self.root,text="Total Category\n [ 0 ]",bd=5,relief=RIDGE,font=("goudy old style",20,"bold"),bg="#57a1f8",fg="white",cursor="hand2")
        self.lbl_category.place(x=300,y=300,width=300,height=150)
        
        self.lbl_salles=Label(self.root,text="Total Sales\n [ 0 ]",bd=5,relief=RIDGE,font=("goudy old style",20,"bold"),bg="#57a1f8",fg="white",cursor="hand2")
        self.lbl_salles.place(x=920,y=300,width=300,height=150)
        
        self.lbl_product=Label(self.root,text="Total Product\n [ 0 ]",bd=5,relief=RIDGE,font=("goudy old style",20,"bold"),bg="#57a1f8",fg="white",cursor="hand2")
        self.lbl_product.place(x=380,y=480,width=300,height=150)

        self.lbl_returns=Label(self.root,text="Total Returns\n [ 0 ]",bd=5,relief=RIDGE,font=("goudy old style",20,"bold"),bg="#57a1f8",fg="white",cursor="hand2")
        self.lbl_returns.place(x=700,y=480,width=300,height=150)
        
        
        #====cotact us===
        self.facebook_byn=Button(self.root,command=open1,pady=7,width=39,text="Facebook",fg="white",border=0,bg="#100c08",cursor="hand2")
        self.facebook_byn.place(x=620 , y=204)
        
        self.instagram_byn=Button(self.root,command=open2,pady=7,width=39,text="Instagram",fg="white",border=0,bg="#100c08",cursor="hand2")
        self.instagram_byn.place(x=620 , y=264)
        
        self.whatsapp_byn=Button(self.root,command=open3,pady=7,width=39,text="Whats App",fg="white",border=0,bg="#100c08",cursor="hand2")
        self.whatsapp_byn.place(x=620 , y=328)
        
        self.linkedin_byn=Button(self.root,command=open4,pady=7,width=39,text="Linked In",fg="white",border=0,bg="#100c08",cursor="hand2")
        self.linkedin_byn.place(x=620 , y=392)
        #=====Footer========
        lbl_footer=Label(self.root,text="Saller User Interface System || is developed By Mohamed Elshinawy",font=("times new roman",20,"bold"),bg="#7F5283",fg="white").pack(side=BOTTOM,fill=X)
        self.update_date_time()
        #self.update_content()-----------------------------
        #os.system('python de_code2.py')
#=====================================================================   


    def employee(self):
        # استرجاع المفتاح من الملف
        with open('key9.key', 'rb') as key9_file:
            key9 = key9_file.read()

        # فتح الملف المشفّر وفك تشفيره
        with open('employee.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key9)
        decrypted = fernet.decrypt(encrypted)

        # إنشاء ملف جديد للملف الأصلي
        with open('employee.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        
        os.system("python employee.py")
        os.remove('employee.py')
        #os.system('python de_code2.py')
        
#    def supplier(self):
        # استرجاع المفتاح من الملف
        with open('key2.key', 'rb') as key_file:
            key2 = key_file.read()

        # فتح الملف المشفّر وفك تشفيره
        with open('supplier.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key2)
        decrypted = fernet.decrypt(encrypted)

        # إنشاء ملف جديد للملف الأصلي
        with open('supplier.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        
        # from supplier import supplierClass
        # self.new_win=Toplevel(self.root)
        # self.new_obj=supplierClass(self.new_win)
        #os.system('python de_code.py')
        os.system("python supplier.py")
        os.remove('supplier.py')
        #os.system('python de_code2.py')

#    def category(self):
        # استرجاع المفتاح من الملف
        with open('key3.key', 'rb') as key3_file:
            key3 = key3_file.read()

        # فتح الملف المشفّر وفك تشفيره
        with open('category.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key3)
        decrypted = fernet.decrypt(encrypted)

        # إنشاء ملف جديد للملف الأصلي
        with open('category.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        # from category import categoryClass
        # self.new_win=Toplevel(self.root)
        # self.new_obj=categoryClass(self.new_win) 
        #os.system('python de_code.py')
        os.system("python category.py")
        os.remove('category.py')
        #os.system('python de_code2.py')

#    def product(self):
        # استرجاع المفتاح من الملف
        with open('key4.key', 'rb') as key4_file:
            key4 = key4_file.read()

        # فتح الملف المشفّر وفك تشفيره
        with open('product.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key4)
        decrypted = fernet.decrypt(encrypted)

        # إنشاء ملف جديد للملف الأصلي
        with open('product.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted) 
        # from product import productClass
        # self.new_win=Toplevel(self.root)
        # self.new_obj=productClass(self.new_win)       
        #os.system('python de_code.py')
        os.system("python product.py")
        os.remove('product.py')
        #os.system('python de_code2.py')

    def sales(self):
        # استرجاع المفتاح من الملف
        with open('key6.key', 'rb') as key6_file:
            key6 = key6_file.read()
        
        # فتح الملف المشفّر وفك تشفيره
        with open('bills.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key6)
        decrypted = fernet.decrypt(encrypted)

        # إنشاء ملف جديد للملف الأصلي
        with open('bills.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted) 
        
        os.system("python bills.py")
        os.remove('bills.py')
        #os.system('python de_code2.py')

    def bills(self):
        # استرجاع المفتاح من الملف
        with open('key5.key', 'rb') as key5_file:
            key5 = key5_file.read()

        # فتح الملف المشفّر وفك تشفيره
        with open('billing.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key5)
        decrypted = fernet.decrypt(encrypted)
        
        # إنشاء ملف جديد للملف الأصلي
        with open('billing.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)        
        
        #=================================
        os.system("python billing.py")
        os.remove('billing.py')
        #os.system('python de_code2.py')
    
    def business_name(self):
        # self.new_win=Toplevel(self.root)
        # self.new_obj=business_name(self.new_win)
        os.system("python business_name.py")
        #os.system('python de_code2.py')

    
    def returns(self):
        # استرجاع المفتاح من الملف
        with open('key7.key', 'rb') as key7_file:
            key7 = key7_file.read()

        # فتح الملف المشفّر وفك تشفيره
        with open('returns.py.encrypted', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        fernet = Fernet(key7)
        decrypted = fernet.decrypt(encrypted)

        # إنشاء ملف جديد للملف الأصلي
        with open('returns.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)        
        # from returns import returnsClass
        # self.new_win=Toplevel(self.root)
        # self.new_obj=returnsClass(self.new_win)
        #os.system('python de_code.py')
        os.system("python returns.py")
        os.remove('returns.py')
        #os.system('python de_code2.py')

    #def update_content(self):
        try:
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d%m%Y")
            #Welcome To Saller User Interface System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS"
            self.lbl_clock.config(text=f"Welcome To Saller User Interface System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

            
"""    

    
        
if __name__=="__main__":        
#    "#57a1f8"="#57a1f8"
#    "#100c08"="#100c08"
#    "#184a45"="#184a45"
#    "#06283D"="#06283D"
#    "#4caf50"="#4caf50"
#    "#607d8b"="#607d8b"
#    "goudy old style"="goudy old style"
#    "times new roman"="times new roman"
#    "microsoft YaHei UI Light"="microsoft YaHei UI Light"
    root=Tk()
    obj=IMS(root)
    root.mainloop()
