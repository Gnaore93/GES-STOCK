

from ctypes.wintypes import SIZE
from optparse import Values
from re import search
import tkinter as tk
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import color, left, width



window = Tk()
window.geometry('1200x1200')
window.title("GES-STOCK")
window.configure(bg='white')


#window.iconbitmap("H:\pdf python\image\Caddie_AdobeStock_7200604-scaled.jpeg",)



def open_menu_prodt():
   new_windown = Toplevel(window)
   new_windown.geometry('1000x600')
   new_windown.title("PRODUIT")
   new_windown.configure(bg= "white")
   

   Frame1 = LabelFrame(new_windown,width=1500,height=80)
   Frame1.configure(bg="lavender")
   Frame1.pack(side=tkinter.TOP,pady=5,padx=5)

   
   Frame2 = LabelFrame(new_windown,width=500,height=150,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP,pady=10,padx=10,)

   treeframe = LabelFrame(new_windown,width=1000,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Code","Produit","Qte_entrant","Stock_actuel"]

   data =[
      ('f65','pomme','500','500'),
      ('f65','miment','1000','500'),
      ('f65','oignon','400','500'),
      ('f65','pomme','2460','500'),
      ('f65','gombo','5620','500'),
         
   ]
   myTree = ttk.Treeview(treeframe,height=200,column=column)
   myTree.pack(fill="both")
   myTree['show']='headings'
   for each in column:
      myTree.column(each,width=100)
      myTree.heading(each,text=each.capitalize())
   for each in data:
      myTree.insert("",END,values=each)

   def filterTreeview(*args):
      ItemsOnTreeview = myTree.get_children()
      search = rechvar.get().capitalize 

      for eachItem in ItemsOnTreeview:
         if search in myTree.item(eachItem)['Values'][2]:
            search_var = myTree.item(eachItem)['values']
            myTree.delete(eachItem)
            myTree.insert("",0,values=search_var)



   barre_rech = Label(Frame1,text="Rech/Email:",borderwidth=5,border=1,fg="black",bg="white")
   barre_rech.configure(bg='lavender')
   barre_rech.place(x=580,y=10)

   
   rechvar = StringVar()
   Barre =Entry(Frame1,textvariable=rechvar)
   Barre.place(x=650,y=10)
   rechvar.trace("w",filterTreeview)

   Code = Label(Frame2,text= "Code:")
   Code.grid(row=2,column=2)
   code = Entry(Frame2,border=2)
   code.grid(row=2,column=3)

   Produit = Label(Frame2,text= "Produit:")
   Produit.grid(row=2,column=4)
   Prodt = Entry(Frame2,border=2)
   Prodt.grid(row=2,column=5)

   Qte_entrant = Label(Frame2,text= "Qte_entrant:")
   Qte_entrant.grid(row=2,column=6)
   qte = Entry(Frame2,border=2)
   qte.grid(row=2,column=7)

   Stock_actuel = Label(Frame2,text= "Stock_actuel:")
   Stock_actuel.grid(row=2,column=9)
   qte = Entry(Frame2,border=2)
   qte.grid(row=2,column=10)

   
   
   
   

def open_menu_clt():
   new_windown_clt = Toplevel(window)
   new_windown_clt.geometry('1000x600')
   new_windown_clt.title("CLIENT")
   new_windown_clt.configure(bg= "white")
   Frame_head = LabelFrame(new_windown_clt,width=1500,height=80)
   Frame_head.configure(bg="lavender")
   Frame_head.pack(side=tkinter.TOP,pady=5,padx=5)

   Frame_clt = LabelFrame( new_windown_clt ,width=1500,height=80,text= "formulaire")
   Frame_clt.configure(bg="white")
   Frame_clt.pack(pady=15,padx=15)

   Nom = Label(Frame_clt,text= "Nom:")
   Nom.grid(row=2,column=2)
   nom = Entry(Frame_clt,border=2)
   nom.grid(row=2,column=3)

   Habitation = Label(Frame_clt,text= "Habitation:")
   Habitation.grid(row=2,column=4)
   habitation = Entry(Frame_clt,border=2)
   habitation.grid(row=2,column=5)

   Profession = Label(Frame_clt,text= "Profession:")
   Profession.grid(row=2,column=6)
   profession = Entry(Frame_clt,border=2)
   profession.grid(row=2,column=7)

   Email = Label(Frame_clt,text= "Email:")
   Email.grid(row=2,column=8)
   email = Entry(Frame_clt,border=2)
   email.grid(row=2,column=9)
   



def open_menu_livsn():
   new_windown_livsn = Toplevel(window)
   new_windown_livsn.geometry('1000x600')
   new_windown_livsn.configure(bg= "white")
   
   Frame_livsn = LabelFrame( new_windown_livsn,width=1500,height=80,text= "formulaire")
   Frame_livsn.configure(bg="navy")
   Frame_livsn.pack(pady=10,padx=10)
   


def open_menu_hist():
   new_windown_hist = Toplevel(window)
   new_windown_hist.geometry('1000x600')
   new_windown_hist.configure(bg= "white")
   lbl= menubar3(new_windown_hist,text ="ok")
   lbl.pack()


def open_menu_stock():
   new_windown_stock = Toplevel(window)
   new_windown_stock.geometry('1000x600')
   new_windown_stock.configure(bg= "white")
   lbl= menubar4(new_windown_stock,text ="ok")
   lbl.pack()

def open_edit_clt():
   new_windown_edit_clt = Toplevel(window)
   new_windown_edit_clt.geometry('1000x600')
   new_windown_edit_clt.configure(bg= "white")
   lbl= menubar5(new_windown_edit_clt,text ="ok")
   lbl.pack()

def open_edit_prd():
   new_windown_edit_prd = Toplevel(window)
   new_windown_edit_prd.geometry('1000x600')
   new_windown_edit_prd.configure(bg= "white")
   lbl= menubar5(new_windown_edit_prd,text ="ok")
   lbl.pack()





dropdown = tk.Menu(window)
menubar=tk.Menu(dropdown,tearoff=0)
menubar.add_command(label="Ajout produit",command=open_menu_prodt)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar1=tk.Menu(dropdown,tearoff=0)
menubar1.add_command(label="Ajout client",command=open_menu_clt)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar2=tk.Menu(dropdown,tearoff=0)
menubar2.add_command(label="Effectuer livraison",command=open_menu_livsn)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar3=tk.Menu(dropdown,tearoff=0)
menubar3.add_command(label="Historique livraison",command=open_menu_hist)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar4=tk.Menu(dropdown,tearoff=0)
menubar4.add_command(label="Voir mes stock",command=open_menu_stock)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar5=tk.Menu(dropdown,tearoff=0)
menubar5.add_command(label="Editer client",command=open_edit_clt)
menubar5.add_command(label="Editer produit",command=open_edit_prd)
window.config(menu=dropdown)


dropdown.add_cascade(label="PRODUIT",menu= menubar)
dropdown.add_cascade(label="CLIENT",menu= menubar1)
dropdown.add_cascade(label="LIVRAISON",menu= menubar2)
dropdown.add_cascade(label="HISTORIQUE",menu= menubar3)
dropdown.add_cascade(label="GESTION DES STOCK",menu= menubar4)
dropdown.add_cascade(label="EDITER",menu= menubar5)








window.mainloop()