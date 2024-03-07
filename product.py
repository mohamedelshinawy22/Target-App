from tkinter import *
from datetime import date
from PIL import Image,ImageTk #PIP install pillow
from tkinter import ttk,messagebox
import sqlite3


class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x500+150+130')
        self.root.resizable(False,False)
        self.root.config(bg="#06283D")
        self.root.title('قائمة توريدات الشركات')
        self.root.focus_force()
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#57a1f8")
        product_frame.place(x=10,y=10,width=450,height=480) #==Hight=700 **
        #===ALL variables==
        self.var_searchtype=StringVar()
        self.var_searchtext=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=IntVar()
        self.var_qty=IntVar()
        self.var_madfo3=IntVar()
        self.bill_amnt=IntVar()
        self.var_serial=StringVar()
        self.var_pid=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.cart_list=[]
        self.var_status= self.bill_amnt
        self.fatch_cat_sup() 
       
        #=====Title=======
        self.icon_title=PhotoImage(file="assed\\dev_logo1.png")
        lbl_title=Label(product_frame,text="  تسجيل التوريدات للشركات",image=self.icon_title,compound=LEFT,font=("times new roman",20,"bold"),bg="#3D3C42",fg="white",anchor='w').pack(side=TOP,fill=X,pady=5,padx=5)
        #===== Content on left frame=================
        lbl_category=Label(product_frame,text="الصنف المورد",font=("times new roman",20,"bold"),bg="#57a1f8").place(x=20,y=90)
        cmb_category=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_category.place(x=165,y=100)
        if cmb_category['values']:  # Check if there are any values in the Combobox
            cmb_category.current(0)  # Set the current selection to the first item

        
        lbl_supplier=Label(product_frame,text="الشركة",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=140)
        cmb_suplier=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_suplier.place(x=165,y=140)
        if cmb_suplier['values']:  # Check if there are any values in the Combobox
            cmb_suplier.current(0)  # Set the current selection to the first item

        
        lbl_product_name=Label(product_frame,text="التاريخ",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=180)
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("times new roman",20),bg="white").place(x=165,y=180,width=245)
        
        lbl_madfo3=Label(product_frame,text="المدفوعات",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=220)
        txt_madfo3=Entry(product_frame,textvariable=self.var_madfo3,font=("times new roman",20),bg="white").place(x=165,y=220,width=245)
        
        lbl_price=Label(product_frame,text="السعر",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=300)#300
        self.txt_price=Entry(product_frame,textvariable=self.var_price,font=("times new roman",20),bg="white")
        self.txt_price.place(x=165,y=300,width=245)

        lbl_quantity=Label(product_frame,text="الكمية",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=260)#260
        self.txt_quantity=Entry(product_frame,textvariable=self.var_qty,font=("times new roman",20),bg="white")
        self.txt_quantity.place(x=165,y=260,width=245)

        lbl_status=Label(product_frame,text="الاجمالي",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=340)
        #cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Select","Active","Inactive"),state="readonly",justify=CENTER,font=("time new roman",15))
        self.var_status=self.bill_amnt
        self.lbl_amount=Label(product_frame,text="الاجمالي\n[0]",font=("times new roman",18,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amount.place(x=165,y=340,width=245)
        #cmb_status.current(0)
        
        lbl_serial=Label(product_frame,text="ملاحظة",font=("times new roman",25,"bold"),bg="#57a1f8").place(x=20,y=390)
        txt_serial=Entry(product_frame,textvariable=self.var_serial,font=("times new roman",20),bg="white").place(x=165,y=390,width=245)
        
        self.lbl_egmaly=Label(product_frame,text="اجمالي المبلغ [0]",font=("times new roman",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_egmaly.place(x=20,y=430,width=200,height=40)
        
        self.lbl_egmaly_madfo3=Label(product_frame,text="اجمالي المدفوع [0]",font=("times new roman",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_egmaly_madfo3.place(x=230,y=430,width=200,height=40)
        #====Buttons====
        btn_add=Button(self.root,command=self.add,bg="#4caf50",bd=7,fg="white",text="حفظ",font=("times new roman",15),cursor="hand2").place(x=950,y=440,width=120,height=50)
        btn_update=Button(self.root,command=self.update,bg="#57a1f8",bd=7,fg="white",text="تعديل",font=("times new roman",15),cursor="hand2").place(x=800,y=440,width=120,height=50)
        btn_delete=Button(self.root,command=self.delete,bg="red",bd=7,fg="white",text="حذف",font=("times new roman",15),cursor="hand2").place(x=650,y=440,width=120,height=50)
        btn_clear=Button(self.root,command=self.clear,bg="#607d8b",bd=7,fg="white",text="مسح الخانات",font=("times new roman",15),cursor="hand2").place(x=500,y=440,width=120,height=50)
        #command=self.add,
        #command=self.update,
        #command=self.delete,
        #command=self.clear,
        
        #========searchFrame===========
        SearchFrame=Label(self.root,relief="ridge",bd=2,bg="#607d8b",fg="white")
        SearchFrame.place(x=500,y=20,width=570,height=50)
        search_frame_text=Label(self.root,text="البحث حسب",font=("times new roman",15,"bold"),bg="#607d8b",fg="white")
        search_frame_text.place(x=520,y=10,height=20)
        #====options======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchtype,values=("اختر","الصنف","اسم الشركة","التاريخ","ملاحظة"),state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_search.place(x=10,y=10,width=150,height=35)
        cmb_search.current(0)
        text_search=Entry(SearchFrame,textvariable=self.var_searchtext,bg="lightyellow",font=("times new roman",18)).place(x=190,y=10,width=180,height=33)
        btn_search=Button(SearchFrame,command=self.search,bg="#4caf50",bd=7,fg="white",text="Search",font=("times new roman",15),cursor="hand2").place(x=390,y=10,width=140,height=35)
        #,command=self.search
        #=====customer Ditales======
        product_frame=Frame(self.root,bd=3,relief=RIDGE)
        product_frame.place(x=480,y=80,width=600,height=350)
        
        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollX=Scrollbar(product_frame,orient=HORIZONTAL)
        #======header====
        self.ProductTable=ttk.Treeview(product_frame,columns=("Id","Date","Category","Supplier","Price","Quantity","Total","Note","Madfo3"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("Id",text="كود")
        self.ProductTable.heading("Date",text="التاريخ")
        self.ProductTable.heading("Category",text="الصنف المورد")
        self.ProductTable.heading("Supplier",text="اسم الشركة")
        self.ProductTable.heading("Price",text="السعر")
        self.ProductTable.heading("Quantity",text="الكمية")
        self.ProductTable.heading("Total",text="الاجمالي")
        self.ProductTable.heading("Note",text="ملاحظة")
        self.ProductTable.heading("Madfo3",text="المدفوعات")
        self.ProductTable["show"]="headings"
        self.ProductTable.column("Id",width=100)
        self.ProductTable.column("Date",width=100)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("Price",width=100)
        self.ProductTable.column("Quantity",width=100)
        self.ProductTable.column("Total",width=100)
        self.ProductTable.column("Note",width=100)
        self.ProductTable.column("Madfo3",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        #,self.get_data
        self.show()
        #self.txt_price2=float(self.txt_price.get())
        #self.txt_quantity2=float(self.txt_quantity.get())
        #cart_data=[self.txt_price2,self.txt_quantity2]
        #self.cart_list.append(cart_data)
        
        self.bill_updates()
        
#===================================================

    
    def bill_updates(self):
        try:
            price = int(self.var_price.get())
        except (ValueError, TclError):
            price = 0
        
        try:
            quantity = int(self.var_qty.get())
        except (ValueError, TclError):
            quantity = 0
        def sum_column_values(database_name, table_name, column_name):
            # اتصال بقاعدة البيانات
            conn = sqlite3.connect(database_name)
            cursor = conn.cursor()

            # استعلام SQL لاسترداد قيم العمود المراد جمعها
            query = f"SELECT SUM({column_name}) FROM {table_name}"

            # تنفيذ الاستعلام
            cursor.execute(query)

            # الحصول على القيمة المجمعة
            total_sum = cursor.fetchone()[0]

            # إغلاق الاتصال بقاعدة البيانات
            conn.close()

            return total_sum

        def sum_column_values(database_name, table_name, column_name2):
            # اتصال بقاعدة البيانات
            conn = sqlite3.connect(database_name)
            cursor = conn.cursor()

            # استعلام SQL لاسترداد قيم العمود المراد جمعها
            query = f"SELECT SUM({column_name2}) FROM {table_name}"

            # تنفيذ الاستعلام
            cursor.execute(query)

            # الحصول على القيمة المجمعة
            total_sum = cursor.fetchone()[0]

            # إغلاق الاتصال بقاعدة البيانات
            conn.close()

            return total_sum

        column_name2 = "Madfo3"
        database_name = "data base\\mis.db"
        table_name = "product"
        total2 = sum_column_values(database_name, table_name, column_name2)
        # مثال على استخدام الدالة
        database_name = "data base\\mis.db"
        table_name = "product"
        column_name = "Total"

        total = sum_column_values(database_name, table_name, column_name)
        #print("Total sum:", total)
        self.bill_amnt = price * quantity
        self.lbl_amount.config(text=f'الاجمالي\n[{str(self.bill_amnt)}]')
        self.lbl_egmaly.config(text=f'اجمالي المبلغ [{str(total)}]')#"اجمالي المدفوع [0]"
        self.lbl_egmaly_madfo3.config(text=f'اجمالي الدفعات [{str(total2)}]')
        self.lbl_amount.after(200, self.bill_updates)


    
    def fatch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")        
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        
        try:
            cur.execute("Select Name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Scelect")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("Select Name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Scelect")
                for i in sup:
                    self.sup_list.append(i[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def add(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_sup.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","All Fieled must be required",parent=self.root)
            else:
#--------------------------------------------------                cur.execute("Select * from product where Date=? and Category=? and Supplier=? and Price=? and Quantity=? and Total=?",(self.var_name.get(),self.var_cat.get(),self.var_sup.get(),self.var_price.get(),self.var_qty.get(),self.var_status.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Product Alreagy Present, Try Another Name !!!",parent=self.root)
                else:
                    cur.execute("Insert into product(Date,Category,Supplier,Price,Quantity,Total,Note,Madfo3) values(?,?,?,?,?,?,?,?)",(
                        
                        self.var_name.get(),
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.bill_amnt,
                        self.var_serial.get(),
                        self.var_madfo3.get(),
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("Success","Product Added Successfully..!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    #=====show data base on frame =======    
    def show(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    #======get data =========
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_name.set(row[1])
        self.var_cat.set(row[2])
        self.var_sup.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        self.var_serial.set(row[7])
        self.var_madfo3.set(row[8])

    #===== update data ========
    def update(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product From The List",parent=self.root)
            else:
                cur.execute("Select * from product where Id=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("Update product set Date=?,Category=?,Supplier=?,Price=?,Quantity=?,Total=?,Note=?,Madfo3=? where Id=?",(
                        
                        self.var_name.get(),
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_serial.get(),
                        self.var_madfo3.get(),
                        self.var_pid.get(),
                    ))
                    con.commit()
                    self.show()
                    
                    messagebox.showinfo("Success","Product Ditales Is Updated Successfully..!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    #=======delete=======
    def delete(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product From The List",parent=self.root)
            else:
                cur.execute("Select * from product where Id=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Delete","Do you Really want to Delete?? ",parent=self.root)
                    if op == True:
                        cur.execute("delete from product where Id=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Ditales Is Deleted Successfully..!!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    #====== clear data======
    def clear(self):
        self.var_cat.set("")
        self.var_name.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("")
        self.var_serial.set("")
        self.var_pid.set("")
        self.var_searchtype.set("Select")
        self.var_searchtext.set("")
        self.show()
    #=======search======
    def search(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_searchtype.get()=="Select":
                messagebox.showerror("Error","Select Search By Options..!",parent=self.root)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search Input Should Be Required..!",parent=self.root)
            else:
                cur.execute("Select * from product where "+self.var_searchtype.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        
                        self.ProductTable.insert('',END,values=row)
                        
                else:
                    messagebox.showerror("Error","No Record Found..!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)





if __name__=="__main__":        
#    "#57a1f8"="#57a1f8"
#    "#100c08"="#100c08"
#    "#184a45"="#184a45"
#    "#06283D"="#06283D"
#    "#4caf50"="#4caf50"
#    "#607d8b"="#607d8b"
#    times new roman"="times new roman"
#    "times new roman"="times new roman"
#    "times new roman"="times new roman"
    root=Tk()
    obj=productClass(root)
    root.mainloop()
