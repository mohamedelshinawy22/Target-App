from tkinter import *
from datetime import date
from PIL import Image,ImageTk #PIP install pillow
from tkinter import ttk, messagebox
import sqlite3

class supplier2Class:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x500+220+130')
        self.root.resizable(False,False)
        self.root.config(bg="#06283D")
        self.root.title('Al-Rashwan Application || Developed By Mohamed Elshinawy')
        self.root.focus_force()
        #======================================
        #===ALL variables==
        self.var_searchtype=StringVar()
        self.var_searchtext=StringVar()
        self.var_supplier2_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()

        
        #=====image banner====
        self.about_btn_img1 = PhotoImage(file='assed\\about2.png')
        self.about_btn = Label(
        self.root,image=self.about_btn_img1, borderwidth=0 , highlightthickness=0,relief="flat")
        self.about_btn.place(x=20, y=15, width=160, height=79)
        
        #========searchFrame===========
        SearchFrame=Label(self.root,relief="ridge",bd=2,bg="#57a1f8",fg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        search_frame_text=Label(self.root,text="البحث عن مقاول",font=("Arial",15,"bold"),bg="#57a1f8",fg="white")
        search_frame_text.place(x=250,y=10,height=20)
        
        #====options======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchtype,values=("اختر","الكود","الاسم","رقم الهاتف"),state="readonly",justify=CENTER,font=("microsoft YaHei UI Light",15,"bold"))
        cmb_search.place(x=10,y=10,width=180,height=40)
        cmb_search.current(0)
        text_search=Entry(SearchFrame,justify="right",textvariable=self.var_searchtext,bg="lightyellow",font=("Arial",18)).place(x=200,y=10,width=210,height=40)
        btn_search=Button(SearchFrame,command=self.search,bg="#4caf50",bd=7,fg="white",text="بحث",font=("Arial",15),cursor="hand2").place(x=430,y=10,width=150,height=40)
        #,command=self.search
        #=======title=========
        title=Label(self.root,text="بيانات المقاول",font=("Arial",20,"bold"),relief="ridge",bd=2,bg="#57a1f8",fg="white").place(x=50,y=100,width=1000,height=50)

        #=========content======
        lbl_supplier2_invoice=Label(self.root,text=":  كود المقاول",font=("Arial",22,"bold"),bg="#06283D",fg="white").place(x=950,y=170)
        txt_supplier2_invoice=Entry(self.root,justify="right",textvariable=self.var_supplier2_invoice,font=("Arial",15,"bold"),bg="white").place(x=750,y=180,width=180)
        
        supplier2_name=Label(self.root,text=": اسم المقاول",font=("Arial",22,"bold"),bg="#06283D",fg="white").place(x=580,y=170)
        txt_name=Entry(self.root,justify="right",textvariable=self.var_name,font=("Arial",15,"bold"),bg="white").place(x=380,y=180,width=200)#x=420,y=180
        
        supplier2_contact=Label(self.root,text=": رقم الهاتف",font=("Arial",22,"bold"),bg="#06283D",fg="white").place(x=200,y=170)#x=180,y=185
        txt_name=Entry(self.root,justify="right",textvariable=self.var_contact,font=("Arial",15,"bold"),bg="white").place(x=20,y=180,width=180)#x=20,y=180
        
        supplier2_note=Label(self.root,text=": وصف المقاول",font=("Arial",22,"bold"),bg="#06283D",fg="white").place(x=280,y=250)
        self.txt_note=Text(self.root ,font=("Arial",15,"bold"),bg="lightyellow")
        self.txt_note.place(x=20,y=250,width=250,height=100)#x=20,y=250
        
        #====Buttons====
        btn_add=Button(self.root,command=self.add,bg="#4caf50",bd=5,fg="white",text="حفظ",font=("Arial",20),cursor="hand2").place(x=850,y=230,width=200,height=50)
        #,command=self.add
        btn_update=Button(self.root,command=self.update,bg="#57a1f8",bd=5,fg="white",text="تعديل",font=("Arial",20),cursor="hand2").place(x=600,y=230,width=200,height=50)
        #,command=self.update
        btn_delete=Button(self.root,command=self.delete,bg="red",bd=5,fg="white",text="حذف",font=("Arial",20),cursor="hand2").place(x=850,y=300,width=200,height=50)
        #,command=self.delete
        btn_clear=Button(self.root,command=self.clear,bg="#607d8b",bd=5,fg="white",text="مسح الخانات",font=("Arial",20),cursor="hand2").place(x=600,y=300,width=200,height=50)
        #,command=self.clear
        #=====supplier2 Ditales======
        supplier2_frame=Frame(self.root,bd=3,relief=RIDGE)
        supplier2_frame.place(x=0,y=365,relwidth=1,height=135)
        
        scrolly=Scrollbar(supplier2_frame,orient=VERTICAL)
        scrollX=Scrollbar(supplier2_frame,orient=HORIZONTAL)
        #======header====
        self.supplier2Table=ttk.Treeview(supplier2_frame,columns=("Invoice","Name","Contact","Note"),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.supplier2Table.xview)
        scrolly.config(command=self.supplier2Table.yview)
        self.supplier2Table.heading("Invoice",text="الكود")
        self.supplier2Table.heading("Name",text="اسم المقاول")
        self.supplier2Table.heading("Contact",text="رقم الهاتف")
        self.supplier2Table.heading("Note",text="الوصف")
        self.supplier2Table["show"]="headings"
        self.supplier2Table.column("Invoice",width=100)
        self.supplier2Table.column("Name",width=100)
        self.supplier2Table.column("Contact",width=100)
        self.supplier2Table.column("Note",width=100)
        self.supplier2Table.pack(fill=BOTH,expand=1)
        self.supplier2Table.bind("<ButtonRelease-1>",self.get_data)
        #,self.get_data
        self.show()
        

#===================================================
    def add(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_supplier2_invoice.get()=="":
                messagebox.showerror("Error","Your Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier2 where Invoice=?",(self.var_supplier2_invoice.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Error This Invoice Is Already Token With Another User , Try Diffrent Id Please!!",parent=self.root)
                else:
                    cur.execute("Insert into supplier2(Invoice,Name,Contact,Note) values(?,?,?,?)",(
                        self.var_supplier2_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_note.get('1.0',END),
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("Success","supplier2 Ditales Are Added Successfully..!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    #=====show data base on frame =======    
    def show(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier2")
            rows=cur.fetchall()
            self.supplier2Table.delete(*self.supplier2Table.get_children())
            for row in rows:
                self.supplier2Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    #======get data =========
    def get_data(self,ev):
        f=self.supplier2Table.focus()
        content=(self.supplier2Table.item(f))
        row=content['values']
        #print(row)
        self.var_supplier2_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_note.delete('1.0',END)
        self.txt_note.insert(END,row[3])    
    #===== update data ========
    def update(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_supplier2_invoice.get()=="":
                messagebox.showerror("Error","Your Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier2 where Invoice=?",(self.var_supplier2_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid User Invoice Please Set Your Invoice in His Place..!",parent=self.root)
                else:
                    cur.execute("Update supplier2 set Name=?,Contact=?,Note=? where Invoice=?",(
                        
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_note.get('1.0',END),
                        self.var_supplier2_invoice.get(),
                    ))
                    con.commit()
                    self.show()
                    
                    messagebox.showinfo("Success","supplier2 Ditales Is Updated Successfully..!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    #=======delete=======
    def delete(self):
        con=sqlite3.connect(database=r'data base\\mis.db')
        cur=con.cursor()
        try:
            if self.var_supplier2_invoice.get()=="":
                messagebox.showerror("Error","Your Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier2 where Invoice=?",(self.var_supplier2_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid User Invoice Please Set Your Invoice in His Place..!",parent=self.root)
                else:
                    op=messagebox.askyesno("Delete","Do you Really want to Delete?? ",parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier2 where Invoice=?",(self.var_supplier2_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","supplier2 Ditales Is Deleted Successfully..!!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    #====== clear data======
    def clear(self):
        self.var_supplier2_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_searchtype.set("Select")
        self.var_searchtext.set("")
        self.txt_note.delete('1.0',END)
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
                cur.execute("Select * from supplier2 where "+self.var_searchtype.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.supplier2Table.delete(*self.supplier2Table.get_children())
                    for row in rows:
                        
                        self.supplier2Table.insert('',END,values=row)
                        
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
#    "Arial"="Arial"
#    "times new roman"="times new roman"
#    "microsoft YaHei UI Light"="microsoft YaHei UI Light"
    root=Tk()
    obj=supplier2Class(root)
    root.mainloop()
                        