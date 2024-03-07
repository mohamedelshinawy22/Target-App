from tkinter import *
from datetime import date
from PIL import Image,ImageTk #PIP install pillow
import webbrowser
import os
import tempfile
from tkinter import ttk,messagebox
import sqlite3
import time
from business_name import business_name
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1250x700+70+20')
        self.root.resizable(False,False)
        self.root.config(bg="#06283D")
        self.root.title('Bill UI || Developed By Mohamed Elshinawy')
        
        
        #============
        self.cart_list=[]
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.chk_print=0
        
        conn = sqlite3.connect('data base/mis.db')
        cur = conn.cursor()
        cur.execute("SELECT Name, phone FROM business_name ORDER BY business_id DESC LIMIT 1")
        row = cur.fetchone()
        if row is None:
            self.nam_defult = "Robo Code System"
            self.phone_defult = "+201006682928"
        else:
            self.nam_defult = row[0]
            self.phone_defult = row[1]
        conn.close()
        #=====Title=======
        self.icon_title=PhotoImage(file="assed\\dev_logo1.png")
        title=Label(self.root,text="Bill User Interface",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#3D3C42",fg="white",anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=70)
        #=====Button_Log out=======
        btn_logout=Button(self.root,text="Log out",font=("times new roman",15,"bold"),bg="#57a1f8",fg="white",cursor="hand2").place(x=1100,y=15,height=40,width=100)    
        #=====Clock========
        self.lbl_clock=Label(self.root,text="Welcome To Bill User Interface \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="#7F5283",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #=========Product Frame=======
        productframe1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        productframe1.place(x=6,y=110,width=410,height=550)
        ptitle=Label(productframe1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #=====Product Search Frame===
        self.var_search=StringVar()
        productframe2=Frame(productframe1,bd=2,relief=RIDGE,bg="white")
        productframe2.place(x=2,y=42,width=398,height=90)
        lbl_search=Label(productframe2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(productframe2,text="Product Name ",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(productframe2,textvariable=self.var_search,font=("goudy old style",15),bg="white").place(x=128,y=47,width=150,height=22)
        btn_search=Button(productframe2,command=self.search,bg="#4caf50",bd=3,fg="white",text="Search",font=("goudy old style",15),cursor="hand2").place(x=284,y=45,width=105,height=25)
        btn_showall=Button(productframe2,command=self.show,bg="#2196f9",bd=3,fg="white",text="Show All",font=("goudy old style",15),cursor="hand2").place(x=284,y=10,width=105,height=25)
        #=====Product Ditales Frame======
        productframe3=Frame(productframe1,bd=3,relief=RIDGE)
        productframe3.place(x=2,y=140,width=398,height=385)
        
        scrolly=Scrollbar(productframe3,orient=VERTICAL)
        scrollX=Scrollbar(productframe3,orient=HORIZONTAL)
        #======header====
        self.productTable=ttk.Treeview(productframe3,columns=("Id","Name","Price","Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("Id",text="Id")
        self.productTable.heading("Name",text="Name")
        self.productTable.heading("Price",text="Price")
        self.productTable.heading("Quantity",text="Quantity")
        self.productTable.heading("Status",text="Status")
        self.productTable["show"]="headings"
        self.productTable.column("Id",width=40)
        self.productTable.column("Name",width=100)
        self.productTable.column("Price",width=100)
        self.productTable.column("Quantity",width=40)
        self.productTable.column("Status",width=100)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(productframe1,text="Note : 'Enter 0 Quantity to remove product from a Cart'",font=("goudy old style",12,"bold"),bg="white",anchor='w',fg="red").pack(side=BOTTOM,fill=X)
        #==========Customer Frame======
        customerframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customerframe.place(x=420,y=110,width=530,height=70)
        ctitle=Label(customerframe,text="Customer Details",font=("goudy old style",15,"bold"),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(customerframe,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(customerframe,textvariable=self.var_cname,font=("goudy old style",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(customerframe,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(customerframe,textvariable=self.var_contact,font=("goudy old style",13),bg="lightyellow").place(x=380,y=35,width=140)
        #=====Cal Cart Frame=== 
        cal_cart_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_cart_frame.place(x=420,y=185,width=530,height=360)
        #=====Calulator Frame===
        self.var_cal_input=StringVar()
        cal_frame=Frame(cal_cart_frame,bd=9,relief=RIDGE,bg="white")
        cal_frame.place(x=5,y=10,width=268,height=340)
        txt_cal_input=Entry(cal_frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(cal_frame,text='7',command=lambda:self.get_input(7),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(cal_frame,text='8',command=lambda:self.get_input(8),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(cal_frame,text='9',command=lambda:self.get_input(9),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(cal_frame,text='+',command=lambda:self.get_input('+'),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=1,column=3)
        btn_4=Button(cal_frame,text='4',command=lambda:self.get_input(4),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(cal_frame,text='5',command=lambda:self.get_input(5),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(cal_frame,text='6',command=lambda:self.get_input(6),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(cal_frame,text='-',command=lambda:self.get_input('-'),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=2,column=3)
        btn_1=Button(cal_frame,text='1',command=lambda:self.get_input(1),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(cal_frame,text='2',command=lambda:self.get_input(2),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(cal_frame,text='3',command=lambda:self.get_input(3),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(cal_frame,text='*',command=lambda:self.get_input('*'),font=("arial",15,"bold"),width=4,bd=5,pady=10,cursor="hand2").grid(row=3,column=3)
        btn_0=Button(cal_frame,text='0',command=lambda:self.get_input(0),font=("arial",15,"bold"),width=4,bd=5,pady=16,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(cal_frame,text='Ac',command=self.clear_cal,font=("arial",15,"bold"),width=4,bd=5,pady=16,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(cal_frame,text='=',command=self.perform_cal,font=("arial",15,"bold"),width=4,bd=5,pady=16,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(cal_frame,text='/',command=lambda:self.get_input('/'),font=("arial",15,"bold"),width=4,bd=5,pady=16,cursor="hand2").grid(row=4,column=3)

        #=====Cart Frame===        
        cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        self.cart_title=Label(cart_frame,text="Cart \t Total Product : [0]",font=("goudy old style",15,"bold"),bg="lightgray")
        self.cart_title.pack(side=TOP,fill=X)
               
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollX=Scrollbar(cart_frame,orient=HORIZONTAL)
        #======header====
        self.cartTable=ttk.Treeview(cart_frame,columns=("Id","Name","Price","Quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
        self.cartTable.heading("Id",text="Id")
        self.cartTable.heading("Name",text="Name")
        self.cartTable.heading("Price",text="Price")
        self.cartTable.heading("Quantity",text="Quantity")
        self.cartTable["show"]="headings"
        self.cartTable.column("Id",width=40)
        self.cartTable.column("Name",width=100)
        self.cartTable.column("Price",width=100)
        self.cartTable.column("Quantity",width=100)
        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
        #=====Add Cart Widgets Frame===
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        AddCartWidgetFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        AddCartWidgetFrame.place(x=420,y=550,width=530,height=110)
        lbl_p_name=Label(AddCartWidgetFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(AddCartWidgetFrame,textvariable=self.var_pname,font=("goudy old style",13),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(AddCartWidgetFrame,text="Price Per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(AddCartWidgetFrame,textvariable=self.var_price,font=("goudy old style",13),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_QTY=Label(AddCartWidgetFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_QTY=Entry(AddCartWidgetFrame,textvariable=self.var_qty,font=("goudy old style",13),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_p_inStock=Label(AddCartWidgetFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_p_inStock.place(x=5,y=70)

        btn_clear_cart=Button(AddCartWidgetFrame,command=self.clear_cart,bg="lightgray",bd=3,text="Clear",font=("goudy old style",15,"bold"),cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(AddCartWidgetFrame,command=self.add_update_cart,bg="#57a1f8",bd=3,text="Add | Update Cart",font=("goudy old style",15,"bold"),fg="white",cursor="hand2").place(x=340,y=70,width=180,height=30)


        #==============Bill Frame ============
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=953,y=110,width=295,height=410)
        bill_title=Label(bill_frame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=("goudy old style",15),bg="#AEE2FF",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        #========Bill Buttons=========
        bill_menue_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menue_frame.place(x=953,y=520,width=295,height=140)
        self.lbl_amount=Label(bill_menue_frame,text="Bill Amount\n[0]",font=("times new roman",12,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amount.place(x=2,y=5,width=90,height=50)
        self.lbl_discount=Label(bill_menue_frame,text="Discount\n[5%]",font=("times new roman",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=100,y=5,width=90,height=50)
        self.lbl_net_pay=Label(bill_menue_frame,text="Net Pay\n[0]",font=("times new roman",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=200,y=5,width=90,height=50)

        btn_print=Button(bill_menue_frame,command=self.bill_print,text="Print\nBill",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
        btn_print.place(x=2,y=60,width=90,height=70)
        btn_clear_all=Button(bill_menue_frame,command=self.clear_all,text="Clear All",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=100,y=60,width=90,height=70)
        btn_generate=Button(bill_menue_frame,command=self.generate_bill,text="Generate\nSave Bill",cursor="hand2",font=("times new roman",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=200,y=60,width=90,height=70)
        #=====Footer========
        lbl_footer=Label(self.root,text="Sales User Interface System || is developed By Mohamed Elshinawy",font=("times new roman",20,"bold"),bg="#7F5283",fg="white").pack(side=BOTTOM,fill=X)
        
        self.show()
        #self.bill_top()
        self.update_date_time()
#=========================All Functions ===========================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    #=====show data base on frame =======    
    def show(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            #self.productTable=ttk.Treeview(productframe3,columns=("Id","Name","Price","Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
            cur.execute("Select Id,Name,Price,Quantity,Status from product where Status ='Active'")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #=======search======
    def search(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search Input Should Be Required..!",parent=self.root)
            else:
                cur.execute("Select Id,Name,Price,Quantity,Status from product where Name LIKE '%"+self.var_search.get()+"%' and Status ='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        
                        self.productTable.insert('',END,values=row)
                        
                else:
                    messagebox.showerror("Error","No Record Found..!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #======get data =========
    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_p_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        
    #======get data_cart =========
    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']
        #Id,Name,Price,Quantity,Stock
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_p_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        
        
        
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","Please Select Product From The List",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Quantity Should Be Required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        
        else:
            # price_cal=int(self.var_qty.get())*float(self.var_price.get())
            # price_cal=float(price_cal)
            price_cal=self.var_price.get()
            #Id,Name,Price,Quantity,Stock
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]

            #======Update Cart =========
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product Already Present \nDo You Want To Update | Remove From The Cart List?",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #Id,Name,Price,Quantity,Status
                        #self.cart_list[index_][2]=price_cal #Price
                        self.cart_list[index_][3]=self.var_qty.get() #Quantity
            else:
                self.cart_list.append(cart_data)
            self.show_cart()   
            self.bill_updates()
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amount.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cart_title.config(text=f"Cart \t Total Product : [{str(len(self.cart_list))}]")
             
    def show_cart(self):
        try:
            #if len(self.cart_list)
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","Customer Details (Name - Contact) Should Be Required..??!",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Please Add Some Products To The Cart..!",parent=self.root)            
        else:
            #=======Bill Top=======
            self.bill_top()
            #=======Bill Middle=======
            self.bill_middle()
            #=======Bill Bottom=======
            self.bill_bottom()
            
            fp=open(f'bill\\{str(self.invoice)}.txt','w')
            fp.write(self.bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Your Bill Has Been Saved Successfully..!!",parent=self.root)
            self.chk_print=1
            
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
         {str(self.nam_defult)}
  Phone No. {str(self.phone_defult)} 
{str("="*27)}
 Cutomer Name: {self.var_cname.get()}
 Phone No: {self.var_contact.get()}
 Bill No: {str(self.invoice)}\n Date: {str(time.strftime("%d/%m/%Y"))}
{str("="*27)}
 P.Name\t     Quantity\t  Price
{str("="*27)}          
        '''
        self.bill_area.delete('1.0',END)
        self.bill_area.insert('1.0',bill_top_temp)                   

    def bill_bottom(self):
        op=messagebox.askyesno('Confirm',"Your System Have a discount \nDo You Want To Discount it (YES) \nTo Remove The Discount (NO) !!",parent=self.root)
        if op==True:
            bill_bottom_temp=f'''
{str("="*27)}
Total Bill Amount : {self.bill_amnt}
Discount : {self.discount}
Net Pay : {self.net_pay}      
{str("="*27)}        
        '''
            self.bill_area.insert(END,bill_bottom_temp)   
        else:
            bill_bottom_temp=f'''
{str("="*27)}
Total Bill Amount : {self.bill_amnt}
{str("="*27)}        
        '''
            self.bill_area.insert(END,bill_bottom_temp) 
    def bill_middle(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            
            for row in self.cart_list:
                #Id,Name,Price,Quantity,Status
                
                Id=row[0]
                Name=row[1]
                Quantity=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    Status='Inactive'
                if int(row[3])!=int(row[4]):
                    Status='Active'
                Price=float(row[2])*int(row[3])
                Price=str(Price)
                self.bill_area.insert(END,"\n "+Name+"\t   "+row[3]+"\t  "+Price)
                #=======Update Quantity In Product Table=====
                cur.execute('Update product set Quantity=?,Status=? where Id=?',(
                    Quantity,
                    Status,
                    Id    
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_p_inStock.config(text=f"In Stock ")
        self.var_stock.set('')
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.bill_area.delete('1.0',END)
        self.cart_title.config(text=f"Cart \t Total Product : [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d\%m\%Y")
        self.lbl_clock.config(text=f"Welcome To Bill User Interface \t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
        
    def bill_print(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please Wait While Printing..",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print","Please Genrate Bill First..,To Print the receipt",parent=self.root)
            
                
if __name__=="__main__":        
    root=Tk()
    obj=BillClass(root)
    root.mainloop()