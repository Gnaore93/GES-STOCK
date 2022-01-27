

from ctypes.wintypes import SIZE
from distutils import command
from math import prod
from optparse import Values
from queue import Empty
from re import search
import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from turtle import color, left, position, width



window = Tk()
window.geometry('2000x2000')
window.title("GES-STOCK")
window.configure(bg='white',background="gainsboro")


Frame_window1 = LabelFrame(window,width=2000,height=70,padx=100)
Frame_window1.configure(bg="white")
Frame_window1.place(x=153,y=0)

# barre_rech = Label(Frame_window1,text="Rech/Email:",borderwidth=5,border=1,fg="red",bg="white")
# barre_rech.configure(bg='lavender')
# barre_rech.pack(side=tkinter.RIGHT,pady=5,padx=5)
# Barre =Entry(Frame_window1,)
# Barre.pack(side=tkinter.RIGHT,pady=5,padx=10)

Frame_window2 = LabelFrame(window,width=150,height=1200,)
Frame_window2.configure(bg="lavender")
Frame_window2.pack(side=tkinter.LEFT,pady=5,padx=5)



Frame_window3 = LabelFrame(window,width=6000,height=1200)
Frame_window3.configure(bg="white",background="teal")
Frame_window3.place(x=178,y=110)


Frame_img = LabelFrame(window,width=5000,height=5000)
Frame_img.configure(bg="teal")
Frame_img.pack(side=tkinter.BOTTOM,pady=110,padx=17)

img = ImageTk.PhotoImage(Image.open("image_window2.jpeg"))
imglabel = Label(Frame_img,image=img,width=1500,height=1000).place(x=5,y=10)



def open_appr():
   win = Toplevel(Frame_window1)
   win.geometry('1000x1000')
   win.title("CLIENT")
   win.configure(bg="white")

   Frame_1 = LabelFrame(win,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="lavender")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   Frame2 = LabelFrame(win,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=50, ipadx=30)

   treeframe = LabelFrame(win,width=1200,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Nom produit","Code","Qte_livrée","PA unitaire","Prix unitaire","PA global","Fournisseur"]

   data =[
      ('f65','pomme','500','500','fj','gnjg','hgjg'),
      ('f65','miment','1000','500','fj','gnjg','hgjg'),
      ('f65','oignon','400','500','fj','gnjg','hgjg'),
      ('f65','pomme','2460','500','fj','gnjg','hgjg'),
      ('f65','gombo','5620','500','fj','gnjg','hgjg'),
         
   ]
   myTree = ttk.Treeview(treeframe,height=200,column=column)
   myTree.pack(fill="both")
   myTree['show']='headings'
   for each in column:
      myTree.column(each,width=90)
      myTree.heading(each,text=each.capitalize())
   for each in data:
      myTree.insert("",END,values=each)



   Produit = Label(Frame2,text= "Nom produit:")
   Produit.grid(row=1,column=1)
   Produit = Entry(Frame2,border=2)
   Produit.grid(row=1,column=2)

   Code = Label(Frame2,text= "Code:")
   Code.grid(row=2,column=1)
   Code =Entry(Frame2,border=2)
   Code.grid(row=2,column=2)

   Qte_livree = Label(Frame2,text= "Qte_livrée:")
   Qte_livree.grid(row=3,column=1)
   Qte_livree = Entry(Frame2,border=2)
   Qte_livree.grid(row=3,column=2)

   Prix_unitaire = Label(Frame2,text= "PA unitaire:")
   Prix_unitaire.grid(row=4,column=1)
   Prix_unitaire = Entry(Frame2,border=2)
   Prix_unitaire.grid(row=4,column=2)

   Prix_global = Label(Frame2,text= "PA global:")
   Prix_global.grid(row=5,column=1)
   Prix_global = Entry(Frame2,border=2)
   Prix_global.grid(row=5,column=2)

   Fournisseur = Label(Frame2,text= "Fournisseur:")
   Fournisseur.grid(row=6,column=1)
   Fournisseur = Entry(Frame2,border=2)
   Fournisseur.grid(row=6,column=2)

def open_vente():
       
   win = Toplevel(Frame_window1)
   win.geometry('1000x1000')
   win.title("CLIENT")
   win.configure(bg="white")

   Frame_1 = LabelFrame(win,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="white")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   Frame2 = LabelFrame(win,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=50, ipadx=30)

   treeframe = LabelFrame(win,width=1200,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Nom produit","Code","Qte_livrée","PA unitaire","Prix unitaire","PA global","Fournisseur"]

   data =[
      ('f65','pomme','500','500','fj','gnjg','hgjg'),
      ('f65','miment','1000','500','fj','gnjg','hgjg'),
      ('f65','oignon','400','500','fj','gnjg','hgjg'),
      ('f65','pomme','2460','500','fj','gnjg','hgjg'),
      ('f65','gombo','5620','500','fj','gnjg','hgjg'),
         
   ]
   myTree = ttk.Treeview(treeframe,height=200,column=column)
   myTree.pack(fill="both")
   myTree['show']='headings'
   for each in column:
      myTree.column(each,width=90)
      myTree.heading(each,text=each.capitalize())
   for each in data:
      myTree.insert("",END,values=each)


   Produit = Label(Frame2,text= "Nom produit:")
   Produit.grid(row=1,column=1)
   Produit = Entry(Frame2,border=2)
   Produit.grid(row=1,column=2)

   Code = Label(Frame2,text= "Qte:")
   Code.grid(row=2,column=1)
   Code =Entry(Frame2,border=2)
   Code.grid(row=2,column=2)

   Qte_livree = Label(Frame2,text= "Montant:")
   Qte_livree.grid(row=3,column=1)
   Qte_livree = Entry(Frame2,border=2)
   Qte_livree.grid(row=3,column=2)

   Prix_unitaire = Label(Frame2,text= "PA unitaire:")
   Prix_unitaire.grid(row=4,column=1)
   Prix_unitaire = Entry(Frame2,border=2)
   Prix_unitaire.grid(row=4,column=2)

   Prix_global = Label(Frame2,text= "PA global:")
   Prix_global.grid(row=5,column=1)
   Prix_global = Entry(Frame2,border=2)
   Prix_global.grid(row=5,column=2)

   Fournisseur = Label(Frame2,text= "Fournisseur:")
   Fournisseur.grid(row=6,column=1)
   Fournisseur = Entry(Frame2,border=2)
   Fournisseur.grid(row=6,column=2)


def open_stock():
       
   win = Toplevel(Frame_window1)
   win.geometry('1000x1000')
   win.title("CLIENT")
   win.configure(bg="white")

   Frame_1 = LabelFrame(win,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="white")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   Frame2 = LabelFrame(win,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=50, ipadx=30)

   treeframe = LabelFrame(win,width=1200,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Nom produit","Code","Qte_livrée","PA unitaire","Prix unitaire","PA global","Fournisseur"]

   data =[
      ('f65','pomme','500','500','fj','gnjg','hgjg'),
      ('f65','miment','1000','500','fj','gnjg','hgjg'),
      ('f65','oignon','400','500','fj','gnjg','hgjg'),
      ('f65','pomme','2460','500','fj','gnjg','hgjg'),
      ('f65','gombo','5620','500','fj','gnjg','hgjg'),
         
   ]
   myTree = ttk.Treeview(treeframe,height=200,column=column)
   myTree.pack(fill="both")
   myTree['show']='headings'
   for each in column:
      myTree.column(each,width=90)
      myTree.heading(each,text=each.capitalize())
   for each in data:
      myTree.insert("",END,values=each)


   Produit = Label(Frame2,text= "Nom produit:")
   Produit.grid(row=1,column=1)
   Produit = Entry(Frame2,border=2)
   Produit.grid(row=1,column=2)

   Code = Label(Frame2,text= "Code:")
   Code.grid(row=2,column=1)
   Code =Entry(Frame2,border=2)
   Code.grid(row=2,column=2)

   Qte_livree = Label(Frame2,text= "Qte_livrée:")
   Qte_livree.grid(row=3,column=1)
   Qte_livree = Entry(Frame2,border=2)
   Qte_livree.grid(row=3,column=2)

   Prix_unitaire = Label(Frame2,text= "PA unitaire:")
   Prix_unitaire.grid(row=4,column=1)
   Prix_unitaire = Entry(Frame2,border=2)
   Prix_unitaire.grid(row=4,column=2)

   Prix_global = Label(Frame2,text= "PA global:")
   Prix_global.grid(row=5,column=1)
   Prix_global = Entry(Frame2,border=2)
   Prix_global.grid(row=5,column=2)

   Fournisseur = Label(Frame2,text= "Fournisseur:")
   Fournisseur.grid(row=6,column=1)
   Fournisseur = Entry(Frame2,border=2)
   Fournisseur.grid(row=6,column=2)
       
       
        
photo1 = PhotoImage(file="add.png")
photoimage1 = photo1.subsample(10,10)
Button(Frame_window2,text="Approv",image=photoimage1,compound=BOTTOM,command=open_appr).place(x=15,y=30)

photo2 = PhotoImage(file="add.png")
photoimage2 = photo2.subsample(10,10)
Button(Frame_window2,text="Ventes",image=photoimage2,compound=BOTTOM,command=open_vente,borderwidth=2).place(x=15,y=100)

photo3 = PhotoImage(file="stock.png")
photoimage3 = photo3.subsample(8,10)
Button(Frame_window2,text="Stock",image=photoimage3,compound=BOTTOM).place(x=15,y=170)

photo4 = PhotoImage(file="stock.png")
photoimage4 = photo4.subsample(8,10)
Button(Frame_window2,text="F/ss",image=photoimage4,compound=BOTTOM).place(x=15,y=240)

photo5 = PhotoImage(file="stock.png")
photoimage5 = photo5.subsample(8,10)
Button(Frame_window1,text="F/ss",image=photoimage5,compound=TOP).place(x=15,y=240)






def open_menu_prodt():
   new_windown = Toplevel(window)
   new_windown.geometry('1000x600')
   new_windown.title("PRODUIT")
   new_windown.configure(bg= "white")
   
 

   Frame1 = LabelFrame(new_windown,width=1500,height=80)
   Frame1.configure(bg="lavender")
   Frame1.pack(side=tkinter.TOP,pady=5,padx=0)

   
   Frame2 = LabelFrame(new_windown,width=800,height=500,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5)

   btn = Button(new_windown,width=5,height=1,bg="teal",text="Valider")
   btn.pack(side=tkinter.LEFT,padx=5,pady=5)
   
   

   treeframe = LabelFrame(new_windown,width=1200,height=1000)
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
   Produit.grid(row=3,column=2)
   Prodt = Entry(Frame2,border=2)
   Prodt.grid(row=3,column=3)

   Qte_entrant = Label(Frame2,text= "Qte_entrant:")
   Qte_entrant.grid(row=4,column=2)
   qte = Entry(Frame2,border=2)
   qte.grid(row=4,column=3)

   Stock_actuel = Label(Frame2,text= "Fournisseur:")
   Stock_actuel.grid(row=5,column=2)
   qte = Entry(Frame2,border=2)
   qte.grid(row=5,column=3)

   
   
   
   

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
   


def open_menu_stock():
   new_windown_stock = Toplevel(window)
   new_windown_stock.geometry('1000x600')
   new_windown_stock.configure(bg= "white")
   

def open_edit_clt():
   new_windown_edit_clt = Toplevel(window)
   new_windown_edit_clt.geometry('1000x600')
   new_windown_edit_clt.configure(bg= "white")
   

def open_edit_prd():
   new_windown_edit_prd = Toplevel(window)
   new_windown_edit_prd.geometry('1000x600')
   new_windown_edit_prd.configure(bg= "white")
   

"""def  toggle_win():
   toogle = Frame(window,width=1000,height=100,bg="#12c4c0")
   toogle.place(x=2,y=2,)

   def dele():
      toogle.destroy()

   Button(toogle,text="close",command=dele).place(x=5,y=10)
Button(window,command=toggle_win,text="Menu").place(x=5,y=10)"""



dropdown = tk.Menu(Frame_window2)
menubar=tk.Menu(dropdown,tearoff=0)
menubar.add_command(label="Ajout produit",command=open_menu_prodt)
window.config(menu=dropdown)

dropdown = tk.Menu(Frame_window2)
menubar1=tk.Menu(dropdown,tearoff=0)
menubar1.add_command(label="Ajout client",command=open_menu_clt)
window.config(menu=dropdown)

dropdown = tk.Menu(Frame_window2)
menubar2=tk.Menu(dropdown,tearoff=0)
menubar2.add_command(label="Effectuer livraison",command=open_menu_livsn)
window.config(menu=dropdown)

dropdown = tk.Menu(Frame_window2)
menubar3=tk.Menu(dropdown,tearoff=0)
menubar3.add_command(label="Historique livraison",command=open_menu_hist)
window.config(menu=dropdown)

dropdown = tk.Menu(Frame_window2)
menubar4=tk.Menu(dropdown,tearoff=0)
menubar4.add_command(label="Voir mes stock",command=open_menu_stock)
window.config(menu=dropdown)

dropdown = tk.Menu(Frame_window2)
menubar5=tk.Menu(dropdown,tearoff=0)
menubar5.add_command(label="Editer client",command=open_edit_clt)
menubar5.add_command(label="Editer produit",command=open_edit_prd)
window.config(menu=dropdown)


dropdown.add_cascade(label="PRODUIT",menu= menubar)
dropdown.add_cascade(label="CLIENT",menu= menubar1)
dropdown.add_cascade(label="LIVRAISON",menu= menubar2)
dropdown.add_cascade(label="VENTE",menu= menubar3)
dropdown.add_cascade(label="GESTION DES STOCK",menu= menubar4)
dropdown.add_cascade(label="EDITER",menu= menubar5)



window.mainloop()