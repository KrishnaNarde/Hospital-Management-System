#this is for making window 
from tkinter import*
from tkinter import ttk  # used to make scroll bar in prescription data wala block
from tkinter import messagebox
import mysql.connector
win =Tk()  # making window
win.state('zoomed') # for making our small window large

#heading
Label(win,text='HOSPITAL MANAGEMENT SYSTEM',font='impack 31 bold', bg='black',fg='white').pack(fill=X) 
 # in the above line we are creating heading line giving it all attribute like text,font,bg etc
 # --fill=X used to fill it to total window size
 
 
 # for making frames(2 square where info of patient is given that boxes)
frame1=Frame(win,bd=12,relief=RIDGE)
frame1.place(x=0,y=50,width=1535,height=400)

#  lable frame making in frame1 for paitent information
lf1=LabelFrame(frame1,text='Patient Information',font='arial 20 bold',bd=10, bg='SeaGreen1',fg='white')
lf1.place(x=0,y=0,width=900,height=380)
# Lables for patient information 50 ka gap hai between 2
Label(lf1,text='Name of Tablet',bg='seagreen1').place(x=5,y=10)
Label(lf1,text='reference id',bg='seagreen1').place(x=5,y=60)
Label(lf1,text='Daily Dose',bg='seagreen1').place(x=5,y=110)
Label(lf1,text='Side Effect of tablet',bg='seagreen1').place(x=5,y=160)
Label(lf1,text='Blood Pressure',bg='seagreen1').place(x=5,y=210)
Label(lf1,text='Medication',bg='seagreen1').place(x=5,y=260)
Label(lf1,text='Patient Id',bg='seagreen1').place(x=420,y=10)
Label(lf1,text='Name of Patient',bg='seagreen1').place(x=420,y=60)
Label(lf1,text='Date of Birth',bg='seagreen1').place(x=420,y=110)
Label(lf1,text='Patient Address',bg='seagreen1').place(x=420,y=160)

#--------------------------------------------------------------------------------------------------
# textVariable for every entry field
nameoftablet=StringVar()
ref=StringVar()
dailydoses=StringVar()
sidotab=StringVar()
bp=StringVar()
madi=StringVar()
patid=StringVar()
nameofpatient=StringVar()
dob=StringVar()
padd=StringVar()

#for entry field
e1=Entry(lf1,bd=5,textvariable=nameoftablet)
e1.place(x=110,y=10,width=300)

e2=Entry(lf1,bd=5,textvariable=ref)
e2.place(x=110,y=60,width=300)

e3=Entry(lf1,bd=5,textvariable=dailydoses)
e3.place(x=110,y=110,width=300)

e4=Entry(lf1,bd=5,textvariable=sidotab)
e4.place(x=110,y=160,width=300)

e5=Entry(lf1,bd=5,textvariable=bp)
e5.place(x=110,y=210,width=300)

e6=Entry(lf1,bd=5,textvariable=madi)
e6.place(x=110,y=260,width=300)

e7=Entry(lf1,bd=5,textvariable=patid)
e7.place(x=530,y=10,width=300)

e8=Entry(lf1,bd=5,textvariable=nameofpatient)
e8.place(x=530,y=60,width=300)

e9=Entry(lf1,bd=5,textvariable=dob)
e9.place(x=530,y=110,width=300)

e10=Entry(lf1,bd=5,textvariable=padd)
e10.place(x=530,y=160,width=300)




# lable frame for priscription

lf2=LabelFrame(frame1,text='Prescription',font='arial 20 bold',bd=10,bg='SeaGreen1',fg='white')
lf2.place(x=920,y=0,width=590,height=380)

#textbox for prescriptionbox
txt_frame=Text(lf2,font='inpack 10 bold',width=40,height=30,bg='Grey')
txt_frame.pack(fill=BOTH)


#frame2 (info wala part)
frame2=Frame(win,bd=12,relief=RIDGE)
frame2.place(x=0,y=450,width=1535,height=300)

#################################BUTTON FUNCTIONS###############################3
def predata():   # this function is for prescription data
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror('Error','All fields are required') #message will be shown for msg we have to import message box from tkinder
    else:
        conn=mysql.connector.connect(host='localhost',username='root',password='Krishna@11',database='hospital_data')
        my_cursor=conn.cursor()
        my_cursor.execute('insert into hospital_infodata values(%s,%s,%s,%s,%s,%s,%s,%s)',(
            nameoftablet.get(),
            ref.get(),
            dailydoses.get(),
            sidotab.get(),
            bp.get(),
            nameofpatient.get(),
            dob.get(),
            padd.get()
        ))
        conn.commit()
        fetch_data()
        conn.close()
        messagebox.showinfo('Success',' Record has been Successfully inserted ')
def fetch_data():
    conn=mysql.connector.connect(host='localhost',username='root',password='Krishna@11',database='hospital_data')
    my_cursor=conn.cursor()
    my_cursor.execute('select * from hospital_infodata')
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        conn.commit()
    conn.close()
    
def get_data(event=''):                   #this function is for get info in upper window when we click on that data in frame 2
    cursor_row=table.focus()
    data=table.item(cursor_row)
    row=data['values']
    nameoftablet.set(row[0])
    ref.set(row[1])
    dailydoses.set(row[2])
    sidotab.set(row[3])
    bp.set(row[4])
    nameofpatient.set(row[5])
    dob.set(row[6])
    padd.set(row[7])
    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
# button function for prescription
def pre():
    txt_frame.insert(END,'Name of Tablet :\t\t\t'+nameoftablet.get()+'\n\n')
    txt_frame.insert(END,'reference id :\t\t\t'+ref.get()+'\n\n')
    txt_frame.insert(END,'Daily doses :\t\t\t'+dailydoses.get()+'\n\n')
    txt_frame.insert(END,'side effect of tablet :\t\t\t'+sidotab.get()+'\n\n')
    txt_frame.insert(END,'Blood pressure :\t\t\t'+bp.get()+'\n\n')
    txt_frame.insert(END,'Medication : \t\t\t'+madi.get()+'\n\n')
    txt_frame.insert(END,'Patient id :\t\t\t'+patid.get()+'\n\n')
    txt_frame.insert(END,'Name of Patient :\t\t\t'+nameofpatient.get()+'\n\n')
    txt_frame.insert(END,'Date of birth :\t\t\t'+dob.get()+'\n\n')
    txt_frame.insert(END,'Patient Address :\t\t\t'+padd.get()+'\n\n')
    


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^delete button function^^^^^^^^^^^^^^^^^^^^
def delete():
    conn=mysql.connector.connect(host='localhost',username='root',password='Krishna@11',database='hospital_data')
    my_cursor=conn.cursor()
    query=('delete from hospital_infodata where Reference no = %s')
    value=(ref.get(),)
    my_cursor.execute(query,value)
    conn.commit()
    conn.close()
    fetch_data()
    messagebox.showinfo('Deleted','Patient data has been successfully deleted')
    
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Clear button function^^^^^^^^^^^^^^^^^^^^^^
    
def clear():   #all textvariable set to empty string
    nameoftablet.set('')
    ref.set('')
    dailydoses.set('')
    sidotab.set('')
    bp.set('')
    madi.set('')
    patid.set('')
    nameofpatient.set('')
    dob.set('')
    padd.set('')
    
    txt_frame,delete(1.0,END)
    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Exit button function^^^^^^^^^^^^^^^^^^^^^6
def Exit():
    confirm=messagebox.askyesno('Conformation','Are you sure you want to Exit')
    if confirm>0:
        win.destroy()
        return
    
    
    


           


# BUTTON making
# delete B
dl_btn=Button(win,text='Delete',font='arial 15 bold',bg='brown',fg='white',bd=5,cursor='hand2',command=delete)
dl_btn.place(x=0,y=750,width=270)

#precption B
prep_btn=Button(win,text='Prescription',font='arial 15 bold',bg='brown',fg='white',bd=5,cursor='hand2',command=pre)
prep_btn.place(x=271,y=750,width=300)


#save prescription data
presd_btn=Button(win,text='Save Prescription Data',font='arial 15 bold',bg='brown',fg='white',bd=5,cursor='hand2',command=predata)
presd_btn.place(x=570,y=750,width=350)

#clear B
cl_btn=Button(win,text='Clear Information',font='arial 15 bold',bg='brown',fg='white',bd=5,cursor='hand2',command=clear)
cl_btn.place(x=920,y=750,width='330')

 # exit B
ex_btn=Button(win,text='Exit',font='arial 15 bold',bg='brown',fg='white',bd=5,cursor='hand2',command=Exit)
ex_btn.place(x=1250,y=750,width=300)

# scroll bar prescriptation info store
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

#table view for frame2
table=ttk.Treeview(frame2,columns=('not','refn','dd','sidotab','bp','pname','dob','padd'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)

#heading for prescription data wala frame
table.heading('not',text='Name of tables')
table.heading('refn',text='reference id')
table.heading('dd',text='daily doses')
table.heading('sidotab',text='side effect of tablet')
table.heading('bp',text='blood pressure')
table.heading('pname',text='patient Name')
table.heading('dob',text='date of birth')
table.heading('padd',text='patient address')
table['show']='headings'
table.pack(fill=BOTH,expand=1)
#----------------------------------(for reducing the size of each col of table so that it will be shown)------

table.column('not',width=120) # here we r not doing for all columb because of not requirement


win.config(bg='grey') # in this line giving colour to window background
table.bind('<ButtonRelease-1>',get_data) 
fetch_data()
mainloop()