

from cgitb import text
import code
from ctypes.wintypes import SIZE
from distutils import command
from fileinput import filename
from importlib.metadata import files
from importlib.resources import path
from math import prod
from optparse import Values
from queue import Empty
from re import search
from tabnanny import check
import tkinter as tk
from tkinter import*
import json
from tkinter.filedialog import asksaveasfile
from tkinter.font import BOLD
from webbrowser import get
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from turtle import color, left, onclick, position, width



window = Tk()
window.geometry('2000x2000')
window.title("GES-STOCK")
window.configure(bg='white',background="gainsboro")

Frame_window1 = LabelFrame(window,width=2000,height=70,padx=100)
Frame_window1.configure(bg="white")
Frame_window1.place(x=153,y=0)

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
img_label = Label(Frame_img,image=img,width=1500,height=1000).place(x=5,y=10)



#titre = Label(Frame_img,width=45, text= "BIENVENUE A LA PHARMACIE SANTE DU BIEN-ETRE:",background="lavender",font=('Arial',45,"bold"))
#titre.place(x=130,y=15)


barre_rech = Label(Frame_window1,text="Rech/Email:",borderwidth=5,border=1,fg="black",bg="white")
barre_rech.configure(bg='lavender')
barre_rech.place(x=1300,y=17)
Barre =Entry(Frame_window1)
Barre.place(x=1400,y=15)

btn = Button(Frame_window1,width=5,height=1,bg="teal",text="Valider",highlightbackground="blue",borderwidth=2)
btn.place(x=1600,y=18)


Produit = Label(img_label,text= "Stock:")
Produit.place(x=1700,y=200)
produit = Entry(img_label,border=2)
produit.place(x=1780,y=200)

def open_appr():
   win = Toplevel(Frame_window1)
   win.geometry('1000x1000')
   win.title("Approvisionnement")
   win.configure(bg="white")
   

   Frame_1 = LabelFrame(win,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="lavender")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   barre_rech = Label(Frame_1,text="Rech/Email:",borderwidth=5,border=1,fg="black",bg="white")
   barre_rech.configure(bg='lavender')
   barre_rech.place(x=580,y=18)
   Barre =Entry(Frame_1)
   Barre.place(x=678,y=15)
   
   Frame2 = LabelFrame(win,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=0, ipadx=30)

   Produit = Label(Frame2,text= "Nom produit:")
   Produit.grid(row=1,column=1)
   produit = Entry(Frame2,border=2)
   produit.grid(row=1,column=2)

   Code = Label(Frame2,text= "Code:")
   Code.grid(row=2,column=1)
   code =Entry(Frame2,border=2)
   code.grid(row=2,column=2)

   Qte_livree = Label(Frame2,text= "Qte livree:")
   Qte_livree.grid(row=3,column=1)
   qte_livree = Entry(Frame2,border=2)
   qte_livree.grid(row=3,column=2)

   Prix_unitairée = Label(Frame2,text= "PA unitaire:")
   Prix_unitairée.grid(row=4,column=1)
   prix_unitairée = Entry(Frame2,border=2)
   prix_unitairée.grid(row=4,column=2)

   Prix_global = Label(Frame2,text= "PA global:")
   Prix_global.grid(row=5,column=1)
   prix_global = Entry(Frame2,border=2)
   prix_global.grid(row=5,column=2)

   Fournisseur = Label(Frame2,text= "Fournisseur:")
   Fournisseur.grid(row=6,column=1)
   fournisseur = Entry(Frame2,border=2)
   fournisseur.grid(row=6,column=2)

   
   
   def check():
       
      dictionnary ={
         "Produit": produit.get(),
         "Code": code.get(),
         "Qte livree": qte_livree.get(),
         "PA unitaire": prix_unitairée.get(),
         "PA global": prix_global.get(),
         "Fournisseur": fournisseur.get()
      }

      json_object = json.dumps(dictionnary,indent=4)
      with open("Approv.json","a") as f:
         f.write(json_object)

      produit.delete(0,END)
      code.delete(0,END)
      qte_livree.delete(0,END)
      prix_unitairée.delete(0,END)
      prix_global.delete(0,END)
      fournisseur.delete(0,END)

   treeframe = LabelFrame(win,width=1200,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Produit","Code","Qte_livrée","PA unitaire","PA global","Fournisseur"]
   
   
   myTree = ttk.Treeview(treeframe,height=200,column=column)
   myTree.pack(fill="both")
   myTree['show']='headings'
   for each in column:
      myTree.column(each,width=90)
      myTree.heading(each,text=each.capitalize())
   

   btn = Button(Frame2,width=10,height=2,bg="teal",text="Valider",highlightbackground="blue",borderwidth=0,command=check)
   btn.grid(row=10, columnspan=4,pady=30,padx=10)

   def imprime():
      win_imprime = Toplevel(Frame_window1)
      win_imprime.geometry('600x600')
      win_imprime.title("Impression")
      win_imprime.configure(bg="white")
          
   btn2 = Button(win,width=10,height=2,bg="teal",text="Imprimer",command=imprime ,highlightbackground="red",borderwidth=10)
   btn2.place(x=900,y=100)

   
def open_vente():
       
   win = Toplevel(Frame_window1)
   win.geometry('1000x1000')
   win.title("Vente")
   win.configure(bg="white")

   Frame_1 = LabelFrame(win,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="white")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   Frame2 = LabelFrame(win,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=10, ipadx=30)

   treeframe = LabelFrame(win,width=1200,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Nom produit","Qte","PA unitaire","PA global"]

   data =[
      ('f65','pomme','500','500',),
      ('f65','miment','1000','500',),
      ('f65','oignon','400','500',),
      ('f65','pomme','2460','500',),
      ('f65','gombo','5620','500',),
         
   ]
   myTree = ttk.Treeview(treeframe,height=200,column=column)
   myTree.pack(fill="both")
   myTree['show']='headings'
   for each in column:
      myTree.column(each,width=90)
      myTree.heading(each,text=each.capitalize())
   for each in data:
      myTree.insert("",END,values=each)


   Produit = Label(Frame2,text= "Produit:")
   Produit.grid(row=1,column=1)
   produit = Entry(Frame2,border=2)
   produit.grid(row=1,column=2)

   Code = Label(Frame2,text= "Qte:")
   Code.grid(row=2,column=1)
   code =Entry(Frame2,border=2)
   code.grid(row=2,column=2)

   Qte_livree = Label(Frame2,text= "PA unitaire:")
   Qte_livree.grid(row=3,column=1)
   qte_livree = Entry(Frame2,border=2)
   qte_livree.grid(row=3,column=2)

   Prix_unitaire = Label(Frame2,text= "PA global:")
   Prix_unitaire.grid(row=4,column=1)
   prix_unitaire = Entry(Frame2,border=2)
   prix_unitaire.grid(row=4,column=2)

   def check():
       
      dictionnary ={
         "Produit": produit.get(),
         "Code": code.get(),
         "Qte livree": qte_livree.get(),
         "PA unitaire": prix_unitaire.get(),
         
      }

      json_object = json.dumps(dictionnary,indent=4)
      with open("Vente.json","a") as f:
         f.write(json_object)

      produit.delete(0,END)
      code.delete(0,END)
      qte_livree.delete(0,END)
      prix_unitaire.delete(0,END)
      
   btn = Button(Frame2,width=10,height=2,command=check , bg="teal",text="Valider",highlightbackground="blue",borderwidth=0)
   btn.grid(row=10, columnspan=4,pady=20,padx=10)

   btn2 = Button(win,width=10,height=2,bg="teal",text="Imprimer",highlightbackground="red",borderwidth=10)
   btn2.place(x=900,y=100)


   
def open_stock():
       
   win_stock = Toplevel(Frame_window1)
   win_stock.geometry('1000x1000')
   win_stock.title("Stock")
   win_stock.configure(bg="white")

   Frame_1 = LabelFrame(win_stock,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="white")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   Frame2 = LabelFrame(win_stock,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=50, ipadx=30)

   treeframe = LabelFrame(win_stock,width=1200,height=1000)
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


def open_fournisseur():
       
   win_fournisseur = Toplevel(Frame_window1)
   win_fournisseur.geometry('1000x1000')
   win_fournisseur.title("Ajout de fournisseur")
   win_fournisseur.configure(bg="white")

   Frame_1 = LabelFrame(win_fournisseur,width=1500,height=80,bg="lavender")
   Frame_1.configure(bg="white")
   Frame_1.pack(side=tkinter.TOP,pady=5,padx=0)

   Frame2 = LabelFrame(win_fournisseur,text="Formulaire de saisie")
   Frame2.configure(bg="white")
   Frame2.pack(side=tkinter.TOP, padx=5,pady=5, ipady=30, ipadx=30)
   
   treeframe = LabelFrame(win_fournisseur,width=1200,height=1000)
   treeframe.configure(bg="white")
   treeframe.pack(pady=10,padx=10)

   column = ["Nom","Code","Contact","Adresse","Ville","Pays","Telephone"]

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


   Nom = Label(Frame2,text= "Nom:")
   Nom.grid(row=1,column=1)
   nom = Entry(Frame2,border=2)
   nom.grid(row=1,column=2)

   Code = Label(Frame2,text= "Code:")
   Code.grid(row=2,column=1)
   code =Entry(Frame2,border=2)
   code.grid(row=2,column=2)

   Contact = Label(Frame2,text= "Contact:")
   Contact.grid(row=3,column=1)
   contact = Entry(Frame2,border=2)
   contact.grid(row=3,column=2)

   Adresse = Label(Frame2,text= "Adresse:")
   Adresse.grid(row=4,column=1)
   adresse = Entry(Frame2,border=2)
   adresse.grid(row=4,column=2)

   Ville = Label(Frame2,text= "Ville:")
   Ville.grid(row=5,column=1)
   ville = Entry(Frame2,border=2)
   ville.grid(row=5,column=2)

   Pays = Label(Frame2,text= "Pays:")
   Pays.grid(row=6,column=1)
   pays = Entry(Frame2,border=2)
   pays.grid(row=6,column=2)

   Telephone = Label(Frame2,text= "Telephone:")
   Telephone.grid(row=7,column=1)
   telephone = Entry(Frame2,border=2)
   telephone.grid(row=7,column=2)

   def check():
       
      dictionnary ={
         "Produit": produit.get(),
         "Code": code.get(),
         "Qte livree": contact.get(),
         "PA unitaire": adresse.get(),
         "PA global": ville.get(),
         "Fournisseur": pays.get(),
         "Telephone": telephone.get(),
      }

      json_object = json.dumps(dictionnary,indent=4)
      with open("fournisseur.json","a") as f:
         f.write(json_object)

      produit.delete(0,END)
      code.delete(0,END)
      contact.delete(0,END)
      adresse.delete(0,END)
      ville.delete(0,END)
      pays.delete(0,END)
      telephone.delete(0,END)

   btn = Button(Frame2,width=10,height=2,bg="teal",text="Valider",command=check, highlightbackground="blue",borderwidth=0)
   btn.grid(row=10, columnspan=4,pady=20,padx=10)

   
       
       
        
photo1 = PhotoImage(file="add.png")
photoimage1 = photo1.subsample(10,10)
Button(Frame_window2,text="Approv",image=photoimage1,compound=BOTTOM,command=open_appr).place(x=15,y=30)

photo2 = PhotoImage(file="add.png")
photoimage2 = photo2.subsample(10,10)
Button(Frame_window2,text="Ventes",image=photoimage2,compound=BOTTOM,command=open_vente,borderwidth=2).place(x=15,y=90)

photo3 = PhotoImage(file="add.png")
photoimage3 = photo3.subsample(10,10)
Button(Frame_window2,text="Stocks",image=photoimage3,compound=BOTTOM,command=open_stock).place(x=15,y=150)

photo4 = PhotoImage(file="add.png")
photoimage4 = photo4.subsample(8,10)
Button(Frame_window2,text="Fournis",image=photoimage4,compound=BOTTOM,command=open_fournisseur).place(x=15,y=210)

photo5 = PhotoImage(file="stock.png")
photoimage5 = photo5.subsample(10,10)
Button(Frame_window1,text="Fourni",image=photoimage5,compound=TOP).place(x=15,y=270)





window.mainloop()