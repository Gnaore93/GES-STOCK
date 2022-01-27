print("GES-SOFT APPLICATION")

print("Bienvenue dans le menu de GES_SOFT")
nom_produit = {}
list_produit = {"pomme": 500, "mangue": 500}
list_client = {"richard": "r@", "gnaore": "g@"}
commande = {}
qte_livraison = {}
email_client = {}
nom_client = {}
historique = {}


suggestion = "oui"


def rvtment():
    print("SE RAVITAILLER")
    suggestion = "-"
    while suggestion != "non":
        nom_produit = input("Veuillez ajouter un produit:\t")
        qte_produit = int(input("Veuillez renseigner la quntite du produit:\t"))
        if nom_produit not in list_produit:
            list_produit[nom_produit] = nom_produit
            list_produit[nom_produit] = qte_produit
            print(list_produit)
        else:
            list_produit[nom_produit] += qte_produit
            print(list_produit)
        suggestion = input("Vouler vous ajouter un vouveau produit:\t?")


def ajout_client():
    print("AJOUTER UN CLIENT")
    suggestion = "oui"
    while suggestion == "oui":
        nom_client = input("Veuillez ajouter un CLIENT")
        email_client = input("Veuillez renseigner L'email du client:\t")
        if email_client not in list_client.values():
            list_client[nom_client] = nom_client
            list_client[nom_client] = email_client
            print(list_client)
        else:
            print("ce client exist deja")
        suggestion = input("voulez vous ajouter un neauveau client?:\t")


def eff_livr():
    print("EFFECTUER UNE LIVRAISON")
    suggestion = "oui"
    while suggestion == "oui":
        global commande
       
        email_client = input("Veuillez enter l'email du client:\t")
        if email_client in list_client.values():
            nom_produit = input("Veuillez entrer le nom du produit a livrer:\t")
            if nom_produit  in list_produit.keys():
                qte_livraison = int(input("Veuillez renseigner La quantite du produit:\t"))
                if qte_livraison <= list_produit[nom_produit]:
                    list_produit[nom_produit] -= qte_livraison
                    #print(list_produit)
                    #print(historique)
                    commande[nom_produit] = qte_livraison
                    historique[email_client] = commande
                    print(commande)
                else:
                    print("quantite insuffisante; la livraison ne peut etre effectuee")
            else:
                print(" le produit n'existe pas, veuillez l'ajouter a la liste de produit")
        else:
            print("client inexistant, veuillez choisir un client valide")
        suggestion = input("voulez vous effectuer une nouvelle livraison?:\t")


def histo():
    
    print("VOIR L'HISTORIQUE DES LIVRAISONS")
    contener = []
    for cle, valeur in historique.items():
        print("client :",  cle)
        for cle1, valeur1 in valeur.items():
            if cle in historique:
                contener.append(f"{cle1}:\t{valeur1}")
            #print(contener)
            print(f"{cle1}:\t{valeur1}")
        print("---------------------\n")


def stock():
    print("VOIR MON STOCK")
    for prodt, qtte in list_produit.items():
        print(f"Produit:\t{prodt}\nDisponibilités:\t {qtte}")
        print("-------------------------\n")



def edit_clt():
    print("EDITER UN CLIENT")
    rpnse = "oui"
    while rpnse != "non":
        clt_edit = input("Veuillez ecrire le nom du client a editer \t")
        if clt_edit in list_client:
            new_clt = input("Veuillez saisir le nouveau nom \t")
            list_client[new_clt] = list_client.pop(clt_edit)
            print(list_client)
            rpnse = input("Voulez vous editer un autre client? \t")
        else:
            print("ce client n'existe pas")


def edit_prodt():
    print("EDITER UN PRODUIT")
    rpse = "oui"
    while rpse != "non":
        prodt_edit = input("Veuillez ecrire le nom du produit a editer \t")
        if prodt_edit in list_produit:
            new_prodt = input("Veuillez saisir le nouveau produit \t")
            list_produit[new_prodt] = list_produit.pop(prodt_edit)
            print(list_produit)
            rpse = input("voulez vous editer un nouveau produit?  \t")
        else:
            print("ce produit nexiste pas!")



def error():
    print("cette option n'existe pas!")

option_menu = {
    "1": rvtment,
    "2": ajout_client,
    "3": eff_livr,
    "4": histo,
    "5": stock,
    "6": edit_clt,
    "7": edit_prodt,
 }







option = "-"
while option != "q":
    option = input("Choisissez une option:")
    option_menu.get(option, error)()






