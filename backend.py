import sqlite3

def VisitorData():
        con=sqlite3.connect("visitorinfo.db")
        cur=con.cursor()
        cur.execute("create table if not exists visitor(ids integer PRIMARY KEY,VisitID text ,Firstname text,Surname text,Age text,contact text,Vehicleno text,EntryTime text,ExitTime text)")
        con.commit()
        con.close()
        
def Addrec(VisitID, Firstname ,Surname ,Age ,contact ,Vehicleno,EntryTime ,ExitTime ):
        con=sqlite3.connect("visitorinfo.db")
        cur=con.cursor()
        cur.execute("Insert into visitor values(NULL,?,?,?,?,?,?,?,?)",(VisitID, Firstname ,Surname ,Age ,contact ,Vehicleno,EntryTime ,ExitTime))
        con.commit()
        con.close()
        
def ViewData():
        con=sqlite3.connect("visitorinfo.db")
        cur=con.cursor()
        cur.execute("select * from visitor ")
        row=cur.fetchall()
        con.close()
        return row
         
def deleteRec(ids):
        con=sqlite3.connect("visitorinfo.db")
        cur=con.cursor()
        cur.execute("delete  from  visitor where ids=?",(ids,))
        con.commit()
        con.close()
        
def searchData(VisitID="", Firstname="" ,Surname="" ,Age="" ,contact="" ,Vehicleno="",EntryTime="" ,ExitTime="" ):
        con=sqlite3.connect("visitorinfo.db")
        cur=con.cursor()
        cur.execute("select * from visitor where VisitID=? or Firstname=? or Surname=? or Age=? or contact=? or Vehicleno=? or EntryTime=?  or ExitTime=?",(VisitID, Firstname ,Surname ,Age ,contact ,Vehicleno,EntryTime ,ExitTime))
        rows=cur.fetchall()
        con.close()
        return rows
        
def dataUpdate(ids,VisitID="", Firstname="" ,Surname="" ,Age="" ,contact="" ,Vehicleno="",EntryTime="" ,ExitTime=""):
        con=sqlite3.connect("visitorinfo.db")
        cur=con.cursor()
        cur.execute("update visitor set VisitID=? or Firstname=? or Surname=? or Age=? or contact=? or Vehicleno=? or EntryTime=?  or ExitTime=?,where ids=?",(VisitID, Firstname ,Surname ,Age ,contact ,Vehicleno,EntryTime ,ExitTime,ids))
        con.commit()
        con.close()
VisitorData()