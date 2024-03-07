from tkinter import *
from datetime import date
from PIL import Image,ImageTk #PIP install pillow
from tkinter import ttk,messagebox
import sqlite3


class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x500+150+130')
        self.root.resizable(False,False)
        self.root.config(bg="#06283D")
        self.root.title('قائمة التوريدات')
        self.root.focus_force()
        #======Variables====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        #=====Title=======
        self.icon_title=PhotoImage(file="assed\\dev_logo1.png")
        lbl_title=Label(self.root,text="شركة ال رشوان للتوريدات والمعدات الثقيلة لصاحبها م: رامي رشوان - م: محمد رشوان",image=self.icon_title,compound=LEFT,font=("times new roman",25,"bold"),bg="#3D3C42",fg="white",anchor='w').pack(side=TOP,fill=X,pady=20,padx=20)
        lbl_name=Label(self.root,text="ادخل اسم الصنف",font=("times new roman",30,"bold"),bg="#06283D",fg="white",anchor='w').place(x=50,y=100)
        txt_name=Entry(self.root,justify="right",textvariable=self.var_name,font=("times new roman",25,"bold"),bg="white").place(x=50,y=170,width=400)
        #======buttons=============
        btn_add=Button(self.root,command=self.add,bg="#4caf50",bd=7,fg="white",text="حفظ",font=("goudy old style",15,"bold"),cursor="hand2").place(x=470,y=170,width=150,height=45)
        #,command=self.add
        btn_delete=Button(self.root,command=self.delete,bg="red",bd=7,fg="white",text="حذف",font=("goudy old style",15,"bold"),cursor="hand2").place(x=630,y=170,width=150,height=45)
        #,command=self.delete
        #=====Category Ditales======
        Category_frame=Frame(self.root,bd=3,relief=RIDGE)
        Category_frame.place(x=800,y=120,width=300,height=375)
        
        scrolly=Scrollbar(Category_frame,orient=VERTICAL)
        scrollX=Scrollbar(Category_frame,orient=HORIZONTAL)
        #======header====
        self.category_table=ttk.Treeview(Category_frame,columns=("Category_Id","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        self.category_table.heading("Category_Id",text="كود الصنف")
        self.category_table.heading("Name",text="اسم الصنف")
        self.category_table["show"]="headings"
        self.category_table.column("Category_Id",width=100)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        #,self.get_data
        #===== image ====
        self.img=Image.open("assed\\category.png")
        self.img=ImageTk.PhotoImage(self.img)
        self.lbl_image=Label(self.root,image=self.img)
        self.lbl_image.place(x=130,y=225,width=468,height=250)
    
        self.show()
    #====== add category Detiales======    
    def add(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Your Category name must be required",parent=self.root)
            else:
                cur.execute("Select * from category where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Category Alreagy Present, Try Another Name !!!",parent=self.root)
                else:
                    cur.execute("Insert into category(Name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Name is Added Successfully..!!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #=====show data base on frame =======    
    def show(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #======get data =========
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
    #=======delete=======
    def delete(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Your Category name must be required",parent=self.root)
            else:
                cur.execute("Select * from category where Category_Id=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Name Please Set Avilable Name..!",parent=self.root)
                else:
                    op=messagebox.askyesno("Delete","Do you Really want to Delete?? ",parent=self.root)
                    if op == True:
                        cur.execute("delete from category where Category_Id=?",(self.var_cat_id.get(),))
                        con.commit()
                        
                        messagebox.showinfo("Delete","Category Is Deleted Successfully..!!",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
        
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
    obj=categoryClass(root)
    root.mainloop()
