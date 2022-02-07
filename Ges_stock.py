

from cgi import test
import code
from ctypes.wintypes import SIZE
from distutils import command
from optparse import Values
from os import path
from re import search
import tkinter as tk
from tkinter import*
from subprocess import call
from tkinter import messagebox
import json
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from turtle import color, left, position, width


windowc = Tk()
windowc.geometry('600x300+380+200')
windowc.title("CONNEXION UTILISATEUR")
windowc.configure(bg='lavender')

uti = Label(windowc,text= "Utilisateur:")
uti.place(x=5, y= 10,)
utientry =Entry(windowc,border=3)
utientry.place(x =100, y=10)
utientry.config(relief=SUNKEN)

mdp = Label(windowc,text= "Mot de passe:")
mdp.place(x=5, y= 50,)
mdpentry =Entry(windowc,border=3)
mdpentry.place(x =100, y=50)
mdpentry.config(relief=SUNKEN)

def connection():
    
   nom= utientry.get()
   mdps= mdpentry.get()

   if (nom =="" or mdps==""):
      messagebox.showerror( "Error" ,"veuillez renseigner tout les shamps")

   elif (nom !="gnaore" or mdps!="1993"):
      messagebox.showinfo("shamps incorrect")

   elif (nom =="gnaore" and mdps=="1993"):

      windowc.destroy()
        
      window = Tk()
      window.geometry('2000x2000')
      window.title("GES-STOCK")
      window.configure(bg='white',background="gainsboro")




      Frame_window1 = LabelFrame(window,width=1500,height=70)
      Frame_window1.configure(bg="white")
      Frame_window1.place(x=20,y=0)

      Frame_window2 = LabelFrame(window,width=150,height=1200,)
      Frame_window2.configure(bg="lavender")
      Frame_window2.pack(side=tkinter.LEFT,pady=0,padx=5)



      Frame_window3 = LabelFrame(window,width=6000,height=1200)
      Frame_window3.configure(bg="white",background="teal")
      Frame_window3.place(x=178,y=110)


      Frame_img = LabelFrame(window,width=5000,height=5000)
      Frame_img.configure(bg="teal")
      Frame_img.pack(side=tkinter.BOTTOM,pady=110,padx=17)

      #img = ImageTk.PhotoImage(Image.open("image_window2.jpeg"))
      #imglabel = Label(Frame_img,image=img,width=1500,height=1000).place(x=5,y=10)



      def open_appr():
         win = Toplevel(window)
         win.geometry("800x800")
         win.title("CLIENT")
         win.configure(bg="white")
         
         
         
         
      photo1 = PhotoImage("add.png")
      photoimage1 = photo1.subsample(10,10)
      Button(Frame_window2,text="Approv",image=photoimage1,compound=BOTTOM,command=open_appr,border=3).place(x=15,y=30)

      photo2 = PhotoImage("1485712554058.jpg")
      photoimage2 = photo2.subsample(10,10)
      Button(Frame_window2,text="Ventes",image=photoimage2,compound=BOTTOM,borderwidth=2).place(x=15,y=100)

      photo3 = PhotoImage("")
      photoimage3 = photo3.subsample(8,10)
      Button(Frame_window2,text="Stock",image=photoimage3,compound=BOTTOM).place(x=15,y=170)





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

         btn = Button(new_windown,width=5,height=1,bg="teal",text="Valider",border=3)
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
         qte_stock = Entry(Frame2,border=2)
         qte_stock.grid(row=5,column=3)

         
         

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

      call(window)

btnenregister = Button(windowc,text="Connextion",font=("Arial",16),fg="red",command=connection)    
btnenregister.place(x=150,y=200,width=200)

mainloop()