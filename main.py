from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageFilter
import mysql.connector 
import re

root =Tk()
root.title("Login")
root.geometry('1920x1080')
root.resizable(True,True)

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'ayush2120', database = 'project')
cur = conn.cursor()

img1=PhotoImage(file=r"E:\\project\\project_image\\loginass.png")
Label(root,image=img1,bg='white').place(x=0,y=0)

def admin():
    top0 =Toplevel()
    top0.title("Login")
    top0.geometry('1920x1080')
    top0.resizable(True,True)

    img2=PhotoImage(file=r"E:\\project\\project_image\\loginnn.png")
    imgl=Label(top0,image=img2,bg='white')
    imgl.place(x=0,y=0)

    def signin():
        username=user.get()
        password=code.get()

        if username=='jahnavi62442' and password=='2707':
            topp = Toplevel()
            topp.title('Agent List')
            topp.geometry('1920x1080')

            conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'ayush2120', database = 'project')
            cur = conn.cursor()




            def show():
                top1=Toplevel()
                top1.title("Login")
                top1.geometry('1920x1080')
                top1.resizable(True,True)

                img1=PhotoImage(file=r"E:\\project\\project_image\\handle.png")
                Label(top1,image=img1,bg='white').place(x=0,y=0) 


                s=ttk.Style()
                s.configure('Treeview', rowheight=30)

                tree_scroll=Scrollbar(top1)
                tree_scroll.place(x=1370,y=250,height=327)

                mytree=ttk.Treeview(top1,yscrollcommand=tree_scroll.set)
                mytree.pack()

                tree_scroll.config(command=mytree.yview)


                mytree['columns']=("pid","price","area","bhk","yoc","type","status","doa","dos","comm")

                mytree.column("#0",width=0, minwidth='0')
                mytree.column("pid", anchor=W, width=120)
                mytree.column("price",anchor=W, width=120)
                mytree.column("area",anchor=W, width=120)
                mytree.column("bhk",anchor=W, width=120)
                mytree.column("yoc",anchor=W, width=120)
                mytree.column("type",anchor=W, width=120)
                mytree.column("status",anchor=W, width=120)
                mytree.column("doa",anchor=W, width=120)
                mytree.column("dos",anchor=W, width=120)
                mytree.column("comm",anchor=W, width=120)

                mytree.heading("#0",text="Label",anchor=W)
                mytree.heading("pid",text="Property id",anchor=W)
                mytree.heading("price",text="Price",anchor=W)
                mytree.heading("area",text="Area",anchor=W)
                mytree.heading("bhk",text="Bedrooms",anchor=W)
                mytree.heading("yoc",text="Year of construction",anchor=W)
                mytree.heading("type",text="Type",anchor=W)
                mytree.heading("status",text="Status",anchor=W)
                mytree.heading("doa",text="Date of Approach",anchor=W)
                mytree.heading("dos",text="Date of Selling",anchor=W)
                mytree.heading("comm",text="Commission earned",anchor=W)

                t=stype.get()
                s=sstatus.get()
                aid=agentid.get()

                conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'ayush2120', database = 'project')
                cur = conn.cursor()

                sql=("select pid,sid,price,area,bhk,yoc,type,status,doa from property where aid=%s and type=%s and status=%s")
                val=(aid,t,s)
                cur.execute(sql,val)
                records=cur.fetchall()

                sql1=("select aname, aphone, amail from agent where aid=%s")
                val1=[agentid.get()]
                cur.execute(sql1,val1)
                details=cur.fetchall()
                agent_name=details[0][0]
                agent_phone=details[0][1]
                agent_mail=details[0][2]
                Label(top1,text=agent_name,fg='black',border=0,bg='#E7E8F8',font=('Microsoft YaHei UI Light',11)).place(x=320,y=165)
                Label(top1,text=agent_phone,fg='black',border=0,bg='#F0E6EF',font=('Microsoft YaHei UI Light',11)).place(x=690,y=167)
                Label(top1,text=agent_mail,fg='black',border=0,bg='#F8E3E5',font=('Microsoft YaHei UI Light',11)).place(x=1055,y=165)


                tv=[]
                for i in records:
                    if(s=="unsold"):
                        i=i+("---",)
                        i=i+("---",)
                        tv.append(i)
                    elif(t=="sale" and s=="sold"):
                        sql1=("select dos,commm from sales where pid=%s and sid=%s")
                        val1=(i[0],i[1])
                        cur.execute(sql1,val1)
                        rec=cur.fetchall()
                        i=i+(rec[0][0],)
                        i=i+(rec[0][1],)
                        tv.append(i)
                    elif(t=="rent" and s=="sold"):
                        sql1=("select dos,comm from rentals where pid=%s and sid=%s")
                        val1=(i[0],i[1])
                        cur.execute(sql1,val1)
                        rec=cur.fetchall()
                        i=i+(rec[0][0],)
                        i=i+(rec[0][1],)
                        tv.append(i)

                mytree.pack(pady=250)
                mytree.tag_configure('evenrow',background='white')
                mytree.tag_configure('oddrow',background='#D1D9EF')

                final=[]
                for i in tv:
                    i=i[:1]+i[2:]
                    final.append(i)
              
                count=0
                for i in final:
                    if count%2!=0:
                        mytree.insert(parent='',index='end',text="",values=i,tags='evenrow')
                    else:
                        mytree.insert(parent='',index='end',text="",values=i,tags='oddrow')
                    count+=1

                top1.mainloop()



            img1=PhotoImage(file=r"E:\\project\\project_image\\agenttree.png")
            Label(topp,image=img1,bg="white").place(x=0,y=0)


            my_tree = ttk.Treeview(topp,columns = ("column1", "column2"),show='headings')



            my_tree.column("column1",anchor=W, width=164, minwidth=25)
            my_tree.column("column2", anchor=W, width=164)
            my_tree.pack(padx = 10,pady = 10)

            my_tree.heading("column1", text="ID", anchor=W)
            my_tree.heading("column2", text="Name", anchor=W)

            s=ttk.Style()
            s.configure('Treeview', rowheight=29)

            my_tree.place(x = 940, y = 210)

            sql=("select aid,aname from agent")
            cur.execute(sql)
            detail=cur.fetchall()


            my_tree.tag_configure('evenrow',background='white')
            my_tree.tag_configure('oddrow',background='#D1D9EF')
                            
            count=0
            for rec in detail:
                if count%2!=0:
                    my_tree.insert(parent='',index='end',text="",values=rec,tags='evenrow')
                else:
                    my_tree.insert(parent='',index='end',text="",values=rec,tags='oddrow')

                count+=1

            def select(a):
                agentid.delete(0,END)
                selected=my_tree.focus()
                value=my_tree.item(selected,'values')
                agentid.insert(0,value[0])

            my_tree.bind("<<TreeviewSelect>>",select)

            agentid=Entry(topp,width=7,fg="black",border=0,bg="white",font=("Times",12))
            agentid.place(x=965,y=612)

            type=['sale','rent']
            stype=ttk.Combobox(topp,value=type,width=5) 
            stype.current(0)
            stype.place(x=1130,y=615)

            status=['sold','unsold']
            sstatus=ttk.Combobox(topp,value=status,width=5) 
            sstatus.current(0)
            sstatus.place(x=1307,y=615)

            button=Button(topp,width=26,height=1,text='Show Details',bg='#8093B8',fg='white',border=0,activebackground='#8093B8',command=show)
            button.place(x=1012,y=677)

            topp.mainloop()


        elif user.get()=='Username':
            messagebox.showinfo("Username","Enter Username",parent=top0)

        elif code.get()=='Password':
            messagebox.showinfo("Password","Enter the Password",parent=top0)



        

    #-----------------------------------------------

    def on_enter(e):
        user.delete(0,END)
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
   
    user=Entry(top0,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=1020,y=346)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

#-----------------------------------------------

    def on_enter(e):
        code.delete(0,END)
        code.config(show='*')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
   
    code=Entry(top0,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=1020,y=446)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    # def showpass():
    #     code.config(show='')

    # showp=Button(top0,text='show',bg='white',fg='black',border=0,activebackground="white",command=showpass)
    # showp.place(x=1270,y=448)

    but=Button(top0,width=20,pady=7,text='Login',bg='#889DC6',fg='white',border=0,activebackground="#8093B8",command=signin)
    but.place(x=1060,y=565)
    top0.mainloop() 


def agent():
    top1 =Toplevel(root)
    #top1=Tk()
    top1.title("Agent-Login")
    top1.geometry('1920x1080')
    top1.configure(bg="#fff")
    top1.resizable(True,True)
    global img2
    img2=PhotoImage(file=r"E:\\project\\project_image\\loginnn.png")
    imgl=Label(top1,image=img2,bg='white') 
    imgl.place(x=0,y=0)

    def signin():
        username=user.get()
        password=code.get()

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ayush2120",
            database="project"
            )
        cur = conn.cursor()

        cur.execute("select uname,pwd,aid from agent")
        records=cur.fetchall()

        flag=0
        for rec in records:
            if rec[0]== username and int(rec[1])==int(password):
                global aid
                aid=rec[2]
                top2=Toplevel(top1)
                top2.title("welcome Agent")
                top2.geometry('1920x1080')
                top2.configure(bg="#fff")
                top2.resizable(True,True)
                global img3
                img3=PhotoImage(file=r"E:\\project\\project_image\welbf.png")
                Label(top2,image=img3,bg='white').place(x=0,y=0)

                def buy():
                    conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="ayush2120",
                    database="project"
                    )
                    buytop1=Toplevel()
                    buytop1.title("form")
                    buytop1.geometry('1920x1080')
                    buytop1.configure(bg="white")
                    buytop1.resizable(True,True)

                    img4=PhotoImage(file=r"E:\\project\\project_image\Buyer Details.png")
                    Label(buytop1,image=img4,bg="white").place(x=0,y=0)  

                    name=Entry(buytop1,width=70,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    name.place(x=210,y=211)

                    aadhar=Entry(buytop1,width=60,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    aadhar.place(x=300,y=267)

                    phone=Entry(buytop1,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    phone.place(x=212,y=323)

                    mail=Entry(buytop1,width=23,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    mail.place(x=530,y=323)

                    #-------------------------------------------------

                    ptype=['sale','rent']

                    def loc(l):
                        loc=[]
                        loc.append("Any")
                        protype=type.get()
                        cur = conn.cursor()
                        sql=("select pid from property where aid=%s and status='unsold' and type=%s")
                        val=[aid,protype]
                        cur.execute(sql,val)

                        rec=cur.fetchall()
                        for i in rec:
                            newStr=re.sub("[^A-Z]","",i[0],0,re.IGNORECASE)
                            if newStr not in loc:
                                loc.append(newStr)

                            locl.config(value=loc)
                            locl.current(0)

                    type=ttk.Combobox(buytop1,value=ptype,width=5)
                    type.current(0)
                    type.place(x=200,y=450)

                    type.bind("<<ComboboxSelected>>",loc)
                    locl=ttk.Combobox(buytop1,value=loc,width=30)
                    locl.current()

                    locl.place(x=495,y=450)

                    minp=[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000,15000000,20000000,25000000,30000000]
                    
                    def maxp(p):
                        maxp=[]
                        minprice= minl.get()
                        for price in minp:
                            if( int(price)>=int(minprice)):
                                maxp.append(price)

                            maxl.config(value=maxp)
                            maxl.current()
                    minl=ttk.Combobox(buytop1,value=minp)
                    minl.current()
                    minl.pack(pady=20)

                    minl.bind("<<ComboboxSelected>>",maxp)

                    maxl=ttk.Combobox(buytop1)
                    maxl.current()

                    minl.place(x=295,y=512)
                    maxl.place(x=645,y=512)

                    area=Entry(buytop1,width=5,fg='black',border=0,bg='white',font=('Times',11))
                    area.place(x=290,y=573)
                    Frame(buytop1,width=70,height=1,bg='black').place(x=290,y=590)
                    Label(buytop1,text="sq ft",bg='white').place(x=330,y=567)

                    bhk=Entry(buytop1,width=5,fg='black',border=0,bg='white',font=('Times',11))
                    bhk.place(x=650,y=573)
                    Frame(buytop1,width=70,height=1,bg='black').place(x=650,y=590)



                    def submit():
                        conn = mysql.connector.connect(
                            host="127.0.0.1",
                            user="root",
                            password="ayush2120",
                            database="project"
                        )
                        # if name.get()=='':
                        #     messagebox.showinfo("Name","Enter the Name")
         
                        # if phone.get()=='':
                        #     messagebox.showinfo("Phone","Enter the Phone Number")
         
                        # if len(phone.get())!=10:
                        #     messagebox.showwarning("Invalid","Invalid phone number")
         
      
                        # if mail.get()=='':
                        #     messagebox.showinfo("Email","Enter the Email")
         
                        # elif "@gmail.com" not in mail.get():
                        #     messagebox.showinfo("Email","Invalid Email")

                        if name.get()!=''and phone.get()!=''and len(phone.get())==10 and mail.get()!=''and ".com" in mail.get() and aadhar.get()!='' and len(aadhar.get())==12:

    
                            cur = conn.cursor()
                            sql=("select pid, price, area, bhk, yoc,type from property where aid=%s and status='unsold'")
                            val=[aid]
                            cur.execute(sql,val)
                            records=cur.fetchall()

                            minP=minl.get()
                            maxP=maxl.get()                     
                            local=locl.get()
                            areaa=area.get()
                            beehk=bhk.get()
                            tipe=type.get()
                            prop=[]

                            for rec in records:
                                if local=="Any":
                                    if int(rec[1])>=int(minP) and int(rec[1])<=int(maxP) and int(rec[2])>int(areaa) and int(rec[3])>=int(beehk) and rec[5]==tipe:
                                        prop.append(rec)
            
                                word=rec[0].split("-")
                                if int(rec[1])>=int(minP) and int(rec[1])<=int(maxP) and word[2]==local and int(rec[2])>int(areaa) and int(rec[3])>=int(beehk) and rec[5]==tipe:
                                    prop.append(rec)
         
                            global buytop2
                            buytop2=Toplevel()
                            buytop2.title("Property Details")
                            buytop2.geometry('1920x1080')
                            buytop2.configure(bg="white")
                            buytop2.resizable(True,True)


                            global imgj
                            imgj=PhotoImage(file=r"E:\\project\\project_image\\tv.png")
                            Label(buytop2,image=imgj,bg='white').place(x=0,y=0)
                            mytree=ttk.Treeview(buytop2)


                            s=ttk.Style()
                            s.configure('Treeview', rowheight=27)

                            tree_scroll=Scrollbar(buytop2)
                            tree_scroll.place(x=1137,y=196,height=296)

                            mytree=ttk.Treeview(buytop2,yscrollcommand=tree_scroll.set)
                            mytree.pack()

                            tree_scroll.config(command=mytree.yview)

                            #define columns
                            mytree['columns']=("pid","price","area","bhk","yoc")

                            #formate columns
                            mytree.column("#0",width=0, minwidth='0')
                            mytree.column("pid", anchor=W, width=147)
                            mytree.column("price",anchor=W, width=147)
                            mytree.column("area",anchor=W, width=147)
                            mytree.column("bhk",anchor=W, width=147)
                            mytree.column("yoc",anchor=W, width=147)

                            #create headings
                            mytree.heading("#0",text="Label",anchor=W)
                            mytree.heading("pid",text="Property id",anchor=W)
                            mytree.heading("price",text="Price",anchor=W)
                            mytree.heading("area",text="Area",anchor=W)
                            mytree.heading("bhk",text="Bedrooms",anchor=W)
                            mytree.heading("yoc",text="Year of construction",anchor=W)

                            #add data
                            mytree.pack(pady=196,padx=380)
    
                            mytree.tag_configure('evenrow',background='white')
                            mytree.tag_configure('oddrow',background='#D1D9EF')
                            
                            count=0
                            for i in prop:
                                if count%2!=0:
                                    mytree.insert(parent='',index='end',text="",values=i,tags='evenrow')
                                else:
                                    mytree.insert(parent='',index='end',text="",values=i,tags='oddrow')
                                count+=1
                            
                                def buyprop():
                                    if proid.get()!='' and dos.get()!='':
                                        global buytop3
                                        buytop3=Toplevel()
                                        buytop3.title("Thank you")
                                        buytop3.geometry('1920x1080')
                                        buytop3.configure(bg="white")
                                        buytop3.resizable(True,True)

                                        global imgty
                                        imgty=PhotoImage(file=r"E:\\project\\project_image\\tyb.png")
                                        Label(buytop3,image=imgty,bg='white').place(x=0,y=0)


                                        conn = mysql.connector.connect(
                                        host="127.0.0.1",
                                        user="root",
                                        password="ayush2120",
                                        database="project"
                                        )
                                        cur=conn.cursor()
                                        sql="insert into buyer(bid,aid,bname,bmail,bphone,pid) values(%s,%s,%s,%s,%s,%s)"
                                        val=(int(aadhar.get()),aid,name.get(),mail.get(),int(phone.get()),proid.get())
                                        cur.execute(sql,val)
                                        conn.commit()

                                        sql1="select sid from seller where pid=%s"
                                        val1=[proid.get()]
                                        cur.execute(sql1,val1)
                                        seller_id=cur.fetchall()
                                        print(seller_id[0][0])

                                        sql2="select doa,price from property where pid=%s and sid=%s"
                                        val2=(proid.get(),seller_id[0][0])
                                        cur.execute(sql2,val2)
                                        rec=cur.fetchall()
                                        print(rec)
                                        dateOfApp=rec[0][0]
                                        proPrice=int(rec[0][1])

                                        sql3="select comm from agent where aid=%s"
                                        val3=[aid]
                                        cur.execute(sql3,val3)
                                        commPer=cur.fetchall()
                                        comm=(float(commPer[0][0])*int(proPrice))/100

                                        if tipe=='sale':
                                            sql4="insert into sales(pid,aid,sid,bid,doa,dos,commm) values(%s,%s,%s,%s,%s,%s,%s)"
                                            val4=(proid.get(),aid,seller_id[0][0],int(aadhar.get()),dateOfApp,dos.get(),comm)
                                            cur.execute(sql4,val4)
                                            conn.commit()
                                        elif tipe=='rent':
                                            sql5="insert into rentals(pid,aid,sid,bid,doa,dos,timepd,comm) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                            val5=(proid.get(),aid,seller_id[0][0],int(aadhar.get()),dateOfApp,dos.get(),float(tpd.get()),comm)
                                            cur.execute(sql5,val5)
                                            conn.commit()

                                        sql6="update property set status='sold' where pid=%s and sid=%s and doa=%s"
                                        val6=(proid.get(),seller_id[0][0],dateOfApp)
                                        cur.execute(sql6,val6)

                                        Label(buytop3,text=comm,fg='black',border=0,bg='#E7E8F8',font=('Times',15)).place(x=500,y=499)



                                        conn.commit()
                                        conn.close()
                                    else:
                                       messagebox.showerror("Error","Enter all fields",parent=buytop2) 

                        elif name.get()=='':
                            messagebox.showinfo("Name","Enter the Name",parent=buytop1) 
                        elif phone.get()=='':
                            messagebox.showinfo("Phone","Enter the Phone Number",parent=buytop1)
         
                        elif len(phone.get())!=10:
                            messagebox.showwarning("Invalid","Invalid phone number",parent=buytop1)
         
      
                        elif mail.get()=='':
                            messagebox.showinfo("Email","Enter the Email",parent=buytop1)
         
                        elif "@gmail.com" not in mail.get():
                            messagebox.showinfo("Email","Invalid Email",parent=buytop1)

                        def select(a):
                            proid.delete(0,END)
                            selected=mytree.focus()
                            value=mytree.item(selected,'values')
                            proid.insert(0,value[0])

                        mytree.bind("<<TreeviewSelect>>",select)

                        #Label(buytop2,text="Enter id of the property buyer is interested in: ",fg="black",bg="white",font=("Times",12)).place(x=115,y=580)
                        proid=Entry(buytop2,width=17,fg="black",border=0,bg="#E9E7F5",font=("Times",12))
                        proid.place(x=375,y=577)
                        #Frame(buytop2,width=95,height=1,bg="black").place(x=400,y=600)
                        
                        

                        #Label(buytop2,text="Time period(if rental):  ",fg="black",bg="white",font=("Times",12)).place(x=115,y=630)
                        dos=Entry(buytop2,width=15,fg="black",border=0,bg="#F3E4EB",font=("Times",12))
                        dos.place(x=815,y=577)
                        # Label(buytop2,text="Date of Buying :  ",fg="black",bg="white",font=("Times",12)).place(x=530,y=450)
                        # dob = DateEntry(buytop2, width= 16, background= "#D1D9EF", foreground= "black",bd=2).place(x=635,y=452)
                        #Label(buytop2,text="Date of Buying :  ",fg="black",bg="white",font=("Times",12)).place(x=545,y=580)
                        tpd=Entry(buytop2,width=10,fg="black",border=0,bg="#FEE2E0",font=("Times",12))
                        tpd.place(x=1280,y=577)
                        #Frame(buytop2,width=95,height=1,bg="black").place(x=220,y=650)

                        Button(buytop2,width=20,text='Buy',bg='#8093B8',fg='black',border=0,activebackground='#8093B8',command=buyprop).place(x=705,y=680)
                        #Button(buytop2,width=25,pady=7,text='select',bg='#D1D9EF',fg='black',border=1,command=select).place(x=600,y=680)

                    Button(buytop1,width=20,height=1,text='Submit',bg='#91B3FA',fg='white',border=0,activebackground="#91B3FA",command=submit).place(x=380,y=657)
                    buytop1.mainloop()

 #-------------------------------------------------------------------------------------------------------------------------------------------------                    
                def sell():
                    conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="ayush2120",
                    database="project"
                    )
                    selltop1=Toplevel()
                    selltop1.title("form")
                    selltop1.geometry('1920x1080')
                    selltop1.configure(bg="white")
                    selltop1.resizable(True,True)
                

                    def submit():   
                        sname.get()
                        saadhar.get()
                        sphone.get()
                        smail.get()
                        slocl.get()
                        sprice.get()
                        hno.get()
                        sno.get()
                        city.get()
                        pincode.get()
                        sarea.get()
                        sbhk.get()
                        cur = conn.cursor()

                        if(sname.get()!=''and saadhar.get()!='' and len(saadhar.get())==12 and sphone.get()!='' and len(sphone.get())==10 and smail.get()!='' and ("@gmail.com" in smail.get()) and slocl.get()!='' and sprice.get()!=''and hno.get()!='' and sno.get()!='' and city.get()!='' and pincode.get()!='' and sarea.get()!='' and sbhk.get()!=''):
                            global selltop2
                            selltop2=Toplevel()
                            selltop2.title("Thank You")
                            selltop2.geometry('1920x1080')
                            selltop2.configure(bg='white')
                            selltop2.resizable(True,True)  
                            global imgtys
                            imgtys=PhotoImage(file=r"E:\\project\\project_image\\tys.png")
                            Label(selltop2,image=imgtys).place(x=0,y=0)
                            
                            sql1="insert into seller(sid,sname,smail,sphone,pid,aid) values(%s,%s,%s,%s,%s,%s)"
                            address=str(hno.get())+"-"+str(sno.get())+"-"+slocl.get()
                            val1=(saadhar.get(),sname.get(),smail.get(),sphone.get(),address,aid)
                            cur.execute(sql1,val1)
                            conn.commit()

                            sql2="insert into property(pid,sid,aid,price,area,bhk,yoc,doa,type,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val2=(address,saadhar.get(),aid,sprice.get(),sarea.get(),sbhk.get(),syoc.get(),doa.get(),stype.get(),'unsold')
                            cur.execute(sql2,val2)
                            conn.commit()


                        elif sname.get()=='':
                            messagebox.showinfo("Name","Enter the Name",parent=selltop1) 
                        elif sphone.get()=='':
                            messagebox.showinfo("Phone","Enter the Phone Number",parent=selltop1)
         
                        elif len(sphone.get())!=10:
                            messagebox.showwarning("Invalid","Invalid phone number",parent=selltop1)
         
                        elif smail.get()=='':
                            messagebox.showinfo("Email","Enter the Email",parent=selltop1)
         
                        elif "@gmail.com" not in smail.get():
                            messagebox.showinfo("Email","Invalid Email",parent=selltop1)

                        elif slocl.get()=='':
                            messagebox.showinfo("Locality","Enter locality")
    
                        elif sprice.get()=='':
                            messagebox.showinfo("Price","Enter price")

                        elif hno.get()=='':
                            messagebox.showinfo("House Number","Enter House number")

                        elif sno.get()=='':
                            messagebox.showinfo("Street number","Enter street number")

                        elif city.get()=='':
                            messagebox.showinfo("City","Enter city")

                        elif pincode.get()=='':
                            messagebox.showinfo("Pincode","Enter pincode")

                        elif sarea.get()=='':
                            messagebox.showinfo("Area","Enter area")

                        elif sbhk.get()=='':
                            messagebox.showinfo("BHK","Enter BHK")



                    img1=PhotoImage(file=r"E:\\project\\project_image\sd.png")
                    Label(selltop1,image=img1,bg="white").place(x=0,y=0)
                            
                    sname=Entry(selltop1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    sname.place(x=225,y=228)

                    saadhar=Entry(selltop1,width=60,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    saadhar.place(x=317,y=283)

                    sphone=Entry(selltop1,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    sphone.place(x=230,y=337)

                    smail=Entry(selltop1,width=23,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    smail.place(x=540,y=337)

                    #-------------------------------------------------

                    ptype=['sale','rent']
                    stype=ttk.Combobox(selltop1,value=ptype,width=5)
                    stype.current(0)
                    stype.place(x=210,y=456)

                    #entry for locality
                    slocl=Entry(selltop1,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    slocl.place(x=660,y=501)

                    #entry for price
                    sprice=Entry(selltop1,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    sprice.place(x=483,y=455)

                    #entry for hno
                    hno=Entry(selltop1,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    hno.place(x=215,y=501)

                    #entry for streetno
                    sno=Entry(selltop1,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    sno.place(x=440,y=501)

                    #entry for city
                    Frame(selltop1,width=170,height=1,bg='black').place(x=210,y=575)
                    city=Entry(selltop1,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    city.place(x=210,y=551)
           
                    #entry for pincode
                    pincode=Entry(selltop1,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    pincode.place(x=530,y=551)

                    #entry for area
                    sarea=Entry(selltop1,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    sarea.place(x=210,y=600)
                    Label(selltop1,text="sq ft",bg='white').place(x=280,y=600)

                    #entry for bedrooms
                    sbhk=Entry(selltop1,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    sbhk.place(x=440,y=600)

                    syoc=Entry(selltop1,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    syoc.place(x=738,y=602)
                    Frame(selltop1,width=70,height=1,bg='black').place(x=733,y=625)

                    doa=Entry(selltop1,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
                    doa.place(x=328,y=657)
                    Frame(selltop1,width=100,height=1,bg='black').place(x=323,y=680)

                    Button(selltop1,width=20,height=1,text='Submit',bg='#5A90FF',fg='white',border=0,activebackground="#5A90FF",command=submit).place(x=410,y=706)

                    selltop1.mainloop()




                buyb=Button(top2,width=17,text="BUY",bg='#8093B8',fg='white',border=0,font=("bold"),activebackground='#8093B8',command=buy)
                buyb.place(x=999,y=297)
                sellb=Button(top2,width=17,text="SELL",bg='#8093B8',fg='white',border=0,font=("bold"),activebackground='#8093B8',command=sell)
                sellb.place(x=999,y=474)


                flag=1
                break
        if(flag==0):
            messagebox.showerror("Invalid","Invalid Username or Password",parent=top1)

        conn.commit()
        conn.close()

    def on_enter(e):
        user.delete(0,END)
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
   
    user=Entry(top1,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    user.place(x=1020,y=346)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
#Frame(frame,width=295,height=2,bg='black').place(x=75,y=105)
#-----------------------------------------------
    def on_enter(e):
        code.delete(0,END)
        code.config(show='*')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
   
    code=Entry(top1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    code.place(x=1020,y=446)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    def showpass():
        code.config(show='')

    showp=Button(top1,text='show',bg='white',fg='black',border=0,activebackground="white",command=showpass)
    showp.place(x=1270,y=448)

    but=Button(top1,width=20,pady=7,text='Login',bg='#889DC6',fg='white',border=0,activebackground="#889DC6",command=signin)
    but.place(x=1060,y=565)

adb=Button(root,width=10,pady=2,text='Admin',bg='#8093B8',fg='white',border=0,font=("bold"),activebackground='#8093B8',command=admin)
adb.place(x=1067,y=367)
agb=Button(root,width=10,pady=2,text='Agent',bg='#8093B8',fg='white',border=0,font=("bold"),activebackground='#8093B8',command=agent)
agb.place(x=1067,y=475)

root.mainloop()