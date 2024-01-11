class Produits:
    def __init__(self, nom, prix_achat, prix_vente, description="Pas de description"):
        self.nom = nom
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.stock = 0
        self.description = description

    def afficher_description(self):
        print(f"Description du produit {self.nom}: {self.description}")

    def modifier_description(self, nouvelle_description):
        self.description = nouvelle_description

    def augmenter_stock(self, quantite):
        self.stock += quantite

    def diminuer_stock(self, quantite):
        if self.stock >= quantite:
            self.stock -= quantite
        else:
            print("Stock insuffisant.")

    def obtenir_valeurs(self):
        return {
            'Nom': self.nom,
            'Prix Achat': self.prix_achat,
            'Prix Vente': self.prix_vente,
            'Stock': self.stock,
            'Description': self.description
        }


class Livres(Produits):
    def __init__(self, nom, prix_achat, prix_vente, auteur, editeur, description="Pas de description"):
        super().__init__(nom, prix_achat, prix_vente, description)
        self.auteur = auteur
        self.editeur = editeur


class Cds(Produits):
    def __init__(self, nom, prix_achat, prix_vente, auteur, interprete, titres, description="Pas de description"):
        super().__init__(nom, prix_achat, prix_vente, description)
        self.auteur = auteur
        self.interprete = interprete
        self.titres = titres


class Magasins:
    def __init__(self, adresse):
        self.adresse = adresse
        self.stock = []

    def ajouter_produit(self, produit):
        self.stock.append(produit)

    def ajouter_livre(self, livre):
        self.stock.append(livre)

    def ajouter_cd(self, cd):
        self.stock.append(cd)

    def acheter_produit(self, reference_produit, nombre_exemplaires):
        self.stock[reference_produit].augmenter_stock(nombre_exemplaires)

    def vendre_produit(self, reference_produit, nombre_exemplaires):
        self.stock[reference_produit].diminuer_stock(nombre_exemplaires)

    def bilan(self):
        for produit in self.stock:
            print(produit.obtenir_valeurs())


def interaction(magasin):
    while True:
        print("1. Ajouter produit")
        print("2. Ajouter livre")
        print("3. Ajouter CD")
        print("4. Acheter produit")
        print("5. Vendre produit")
        print("6. Afficher bilan")
        print("0. Quitter")

        choix = int(input("Choisissez une option : "))

        if choix == 1:
            nom = input("Nom du produit : ")
            prix_achat = float(input("Prix d'achat : "))
            prix_vente = float(input("Prix de vente : "))
            description = input("Description : ")
            produit = Produits(nom, prix_achat, prix_vente, description)
            magasin.ajouter_produit(produit)

        elif choix == 2:
            nom = input("Nom du livre : ")
            prix_achat = float(input("Prix d'achat : "))
            prix_vente = float(input("Prix de vente : "))
            auteur = input("Auteur : ")
            editeur = input("Editeur : ")
            description = input("Description : ")
            livre = Livres(nom, prix_achat, prix_vente, auteur, editeur, description)
            magasin.ajouter_livre(livre)

        elif choix == 3:
            nom = input("Nom du CD : ")
            prix_achat = float(input("Prix d'achat : "))
            prix_vente = float(input("Prix de vente : "))
            auteur = input("Auteur : ")
            interprete = input("Interprete : ")
            titres = input("Titres (séparés par des virgules) : ").split(',')
            description = input("Description : ")
            cd = Cds(nom, prix_achat, prix_vente, auteur, interprete, titres, description)
            magasin.ajouter_cd(cd)

        elif choix == 4:
            reference = int(input("Référence du produit : "))
            quantite = int(input("Quantité à acheter : "))
            magasin.acheter_produit(reference, quantite)

        elif choix == 5:
            reference = int(input("Référence du produit : "))
            quantite = int(input("Quantité à vendre : "))
            magasin.vendre_produit(reference, quantite)

        elif choix == 6:
            magasin.bilan()

        elif choix == 0:
            break

        else:
            print("Option invalide. Veuillez réessayer.")

# Test de l'application
magasin_test = Magasins("123 Rue du Commerce")
interaction(magasin_test)
