#frontend 
from tkinter import *
import tkinter.messagebox
from django.conf.locale import bg
import backend 
from distutils.command.sdist import sdist
#-----------------------------------Window------------------------------------------------------------
class building:
       
    def __init__(self,root):
        self.root=root
        self.root.title("Housing Society Manaagement")
        self.root.geometry('1920x1080')
        self.root.config(bg="cyan")
        
        VisitID =StringVar()
        Firstname=StringVar()
        Surname =StringVar()
        Date =StringVar()
        contact =StringVar()
        Vehicleno =StringVar()
        EntryTime =StringVar()
        ExitTime =StringVar()
        
#------------------------------------------Functions--------------------------------------------------------------------

        def Exit1():
            Exit1=tkinter.messagebox.askyesno("Housing Society Manaagement", "Confirm if you want to exit")
            if Exit1 > 0 :
                root.destroy()
            return
        
        def clearData():
            self.txt_ID.delete(0, END)
            self.txt_first.delete(0, END)
            self.txt_surname.delete(0, END)
            self.txt_date.delete(0, END)
            self.txt_cntc.delete(0, END)
            self.txt_vehno.delete(0, END)
            self.txt_entry.delete(0, END)
            self.txt_exit.delete(0, END)
            
        def addData():
                if(len(VisitID.get())!=0):
                    
                    backend.Addrec(VisitID.get(),Firstname.get() ,Surname.get() ,Date.get() ,contact.get() ,Vehicleno.get(),EntryTime.get() ,ExitTime.get() )
                    Visitorlist.delete(0, END)
                    Visitorlist.insert(END,(VisitID.get(),Firstname.get() ,Surname.get() ,Date.get() ,contact.get() ,Vehicleno.get(),EntryTime.get() ,ExitTime.get()))
        
        def DisplayData():
            Visitorlist.delete(0, END)
            for row in backend.ViewData():
                Visitorlist.insert(END,row,str(""))    
                
        def VisitorRecords (event):
                global sd
                searchVis=Visitorlist.curselection()[0]
                sd=Visitorlist.get(searchVis)
            
                self.txt_ID.delete(0, END)
                self.txt_ID.insert(END, sd[1])
                self.txt_first.delete(0, END)
                self.txt_first.insert(END, sd[2])
                self.txt_surname.delete(0, END)
                self.txt_surname.insert(END, sd[3])
                self.txt_date.delete(0, END)
                self.txt_date.insert(END, sd[4])
                self.txt_cntc.delete(0, END)
                self.txt_cntc.insert(END, sd[5])
                self.txt_vehno.delete(0, END)
                self.txt_vehno.insert(END, sd[6])
                self.txt_entry.delete(0, END)
                self.txt_entry.insert(END, sd[7])
                self.txt_exit.delete(0, END)
                self.txt_exit.insert(END, sd[8])
                
        def DeleteData():
            if(len(VisitID.get())!=0):
                backend.deleteRec(sd[0])
                clearData()
                DisplayData()      
                
        def searchDatabase():
            Visitorlist.delete(0,END)
            for row in backend.searchData(VisitID.get(),Firstname.get() ,Surname.get() ,Date.get() ,contact.get() ,Vehicleno.get(),EntryTime.get() ,ExitTime.get()):
                Visitorlist.insert(END,row,str(""))
                
        def updateData():
            if(len(VisitID.get())!=0):
                backend.deleteRec(sd[0])
            if(len(VisitID.get())!=0):
                backend.Addrec(VisitID.get(),Firstname.get() ,Surname.get() ,Date.get() ,contact.get() ,Vehicleno.get(),EntryTime.get() ,ExitTime.get())
                Visitorlist.delete(0, END)
                Visitorlist.insert(END,(VisitID.get(),Firstname.get() ,Surname.get() ,Date.get() ,contact.get() ,Vehicleno.get(),EntryTime.get() ,ExitTime.get()))
                
                                                                                                                                              
#-----------------------------------------Frames------------------------------------------------------------------------
       
        MainFrame = Frame(self.root,bg="cyan")
        MainFrame.grid()
        
        TitleFrame = Frame(MainFrame,bd=8,padx=10,pady=10,bg="white",relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.leb_title =Label(TitleFrame,font=('arial',47,'bold'),text="HOUSING SOCIETY MANAGEMENT",bg="white",width=39)
        self.leb_title.grid()
#----------------------------------------Button Frame----------------------------------------------------------------------        
       
        Buttonframe=Frame(MainFrame,bd=2,width=1920,height=70,padx=18,pady=10,bg="yellow",relief=RIDGE)
        Buttonframe.pack(side=BOTTOM)

#---------------------------------------Data Frame-------------------------------------------------------------------------
        Dataframe=Frame(MainFrame,bd=1,width=1920,height=500,padx=18,pady=10,bg="cyan",relief=RIDGE)
        Dataframe.pack(side=BOTTOM)
        
        Dataframe_left=LabelFrame(Dataframe,bd=2,font=('arial',20,'bold'),width=1200,height=700,padx=18,pady=0,bg="white",relief=RIDGE,text=" Visitor Information \n")
        Dataframe_left.pack(side=LEFT)
        
        Dataframe_right=LabelFrame(Dataframe,bd=2,font=('arial',18,'bold'),width=720,height=500,padx=18,pady=10,bg="white",relief=RIDGE,text=" Visitor Details :- \n")
        Dataframe_right.pack(side=RIGHT)
        
#-------------------------------------------Textboxes and labels--------------------------------------------------------------------------
       
        self.leb_ID =Label(Dataframe_left,font=('arial',15,'bold'),text="Visitor's ID - ",bg="white",padx=2,pady=2)
        self.leb_ID.grid(row=0 ,column=0,sticky=W)
        self.txt_ID =Entry(Dataframe_left,font=('arial',15),textvariable=VisitID,width=45,bd=2,selectborderwidth=3)
        self.txt_ID.grid(row=0 ,column=1)
        
        
        self.leb_first =Label(Dataframe_left,font=('arial',15,'bold'),text="First Name - ",bg="white",padx=2,pady=2)
        self.leb_first.grid(row=1 ,column=0,sticky=W)
        self.txt_first =Entry(Dataframe_left,font=('arial',15),textvariable=Firstname,width=45,bd=2,selectborderwidth=3)
        self.txt_first.grid(row=1 ,column=1)
        
        self.leb_surname =Label(Dataframe_left,font=('arial',15,'bold'),text="Surname - ",bg="white",padx=2,pady=2)
        self.leb_surname.grid(row=2 ,column=0,sticky=W)
        self.txt_surname =Entry(Dataframe_left,font=('arial',15),textvariable=Surname,width=45,bd=2,selectborderwidth=3)
        self.txt_surname.grid(row=2 ,column=1)
        
        self.leb_date =Label(Dataframe_left,font=('arial',15,'bold'),text="Date - ",bg="white",padx=2,pady=2)
        self.leb_date.grid(row=3 ,column=0,sticky=W)
        self.txt_date =Entry(Dataframe_left,font=('arial',15),textvariable=Date,width=45,bd=2,selectborderwidth=3)
# self.txt_date.insert(0,"Date Format -25oct2019")
        self.txt_date.grid(row=3 ,column=1)
        
        
        self.leb_cntc =Label(Dataframe_left,font=('arial',15,'bold'),text="Contact Number - ",bg="white",padx=2,pady=2)
        self.leb_cntc.grid(row=4 ,column=0,sticky=W)
        self.txt_cntc =Entry(Dataframe_left,font=('arial',15),textvariable=contact,width=45,bd=2,selectborderwidth=3)
        self.txt_cntc.grid(row=4 ,column=1)
        
        
        self.leb_vehno =Label(Dataframe_left,font=('arial',15,'bold'),text="Vehicle Number - ",bg="white",padx=2,pady=2)
        self.leb_vehno.grid(row=5 ,column=0,sticky=W)
        self.txt_vehno =Entry(Dataframe_left,font=('arial',15),textvariable=Vehicleno,width=45,bd=2,selectborderwidth=3)
        self.txt_vehno.grid(row=5 ,column=1)
        
        
        self.leb_entry =Label(Dataframe_left,font=('arial',15,'bold'),text="Entry Time - ",bg="white",padx=2,pady=2)
        self.leb_entry.grid(row=6 ,column=0,sticky=W)
        self.txt_entry =Entry(Dataframe_left,font=('arial',15),textvariable=EntryTime,width=45,bd=2,selectborderwidth=3)
        self.txt_entry.grid(row=6 ,column=1)
        
        
        self.leb_exit =Label(Dataframe_left,font=('arial',15,'bold'),text="Exit Time - ",bg="white",padx=2,pady=2)
        self.leb_exit.grid(row=7 ,column=0,sticky=W)
        self.txt_exit =Entry(Dataframe_left,font=('arial',15),textvariable=ExitTime,width=45,bd=2,selectborderwidth=3)
        self.txt_exit.grid(row=7 ,column=1)
#---------------------------------------------------------ListBox and ScrollBar for Right Frame-----------------------------------------------------
        scrollbar = Scrollbar(Dataframe_right)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        Visitorlist=Listbox(Dataframe_right,width=60,height=24,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        Visitorlist.bind("<<ListboxSelect>>",VisitorRecords)
        Visitorlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=Visitorlist.yview())
        
#---------------------------------------------------------All Buttons---------------------------------------------------------------------------
        self.btn_new=Button(Buttonframe,text="Add New",font=('arial',15,'bold'),height=1,width=15,bd=4,command=addData)
        self.btn_new.grid(row=0,column=0)
        
        self.btn_dis=Button(Buttonframe,text="Display",font=('arial',15,'bold'),height=1,width=15,bd=4,command=DisplayData)
        self.btn_dis.grid(row=0,column=1)
        
        self.btn_clr=Button(Buttonframe,text="Clear",font=('arial',15,'bold'),height=1,width=15,bd=4,command=clearData)
        self.btn_clr.grid(row=0,column=2)
        
        self.btn_update=Button(Buttonframe,text="Update",font=('arial',15,'bold'),height=1,width=15,bd=4,command=updateData)
        self.btn_update.grid(row=0,column=3)
        
        self.btn_search=Button(Buttonframe,text="Search",font=('arial',15,'bold'),height=1,width=15,bd=4,command=searchDatabase)
        self.btn_search.grid(row=0,column=4)
        
        self.btn_Delete=Button(Buttonframe,text="Delete",font=('arial',15,'bold'),height=1,width=15,bd=4,command=DeleteData)
        self.btn_Delete.grid(row=0,column=5)
        
        self.btn_exit=Button(Buttonframe,text="Exit",font=('arial',15,'bold'),height=1,width=15,bd=4,command=Exit1)
        self.btn_exit.grid(row=0,column=6)
        
        
if __name__=='__main__':
        root=Tk()
        application=building(root)
        root.mainloop()
        