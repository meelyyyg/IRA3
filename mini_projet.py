# Mini projet Python
# Benjamin Krauss et Mélissande Garçonnet
# Gestion de trains 

trains = {
    
    'ANG-PAR': {'places_total': 500, 'places_restantes': 500, 'passagers': set()},
    'ANG-TRS': {'places_total': 300, 'places_restantes': 300, 'passagers': set()},
    'ANG-NTS': {'places_total': 400, 'places_restantes': 400, 'passagers': set()},
}

def afficher(trains):
        
    print("Voici la liste des trains partant de la gare d'Angers :")
        
    for trajet, infos in trains.items():
        
        if(trajet == 'ANG-PAR'):
            print(f"Pour le trajet entre Angers et Paris, il reste {infos['places_restantes']} places disponibles sur {infos['places_total']} places au total.")
            
        if(trajet == 'ANG-TRS'):
            print(f"Pour le trajet entre Angers et Tours, il reste {infos['places_restantes']} places disponibles sur {infos['places_total']} places au total.")
            
        if(trajet == 'ANG-NTS'):
            print(f"Pour le trajet entre Angers et Nantes, il reste {infos['places_restantes']} places disponibles sur {infos['places_total']} places au total.")
            
    


def reserver(trains):
    
    nom = input("Veuillez entrer votre nom. ")
    prenom = input("Veuillez insérer votre prénom. ")
    passager = (nom.upper(), prenom.capitalize())
    choix = input("Où souhaitez-vous vous rendre ? (Paris, Tours ou Nantes)")
    
    while (choix != "Nantes" and choix != "Tours" and choix != "Paris"):
        
        print("La destination choisie n'existe pas. Veuillez choisir entre Tours, Nantes et Paris.")
        choix = input("Où souhaitez-vous vous rendre ? (Paris, Tours ou Nantes) ")
    
    if (choix == "Nantes") :
        
        train = trains['ANG-NTS']
        
        if (passager in train['passagers']):
            print(f"Le passager {prenom} {nom} est déjà inscrit sur le trajet entre Angers et Nantes.")
            return
        
        if (train['places_restantes'] <= 0):
            print(f"Plus de places disponibles pour le trajet à destination de Nantes.")
            return
        
        train['passagers'].add(passager)
        train['places_restantes'] -= 1
        print(f"{prenom} {nom} ajouté au train pour Nantes. Il reste {train['places_restantes']} places.")
        numero = (train['places_total']) - (train['places_restantes'])
        ticket(nom,prenom,numero,choix)
    
    if (choix == "Tours") :
        
        train = trains['ANG-TRS']
        
        if (passager in train['passagers']):
            print(f"Le passager {prenom} {nom} est déjà inscrit sur le trajet entre Angers et Tours.")
            return
        
        if (train['places_restantes'] <= 0):
            print(f"Plus de places disponibles pour le trajet à destination de Tours.")
            return
        
        train['passagers'].add(passager)
        train['places_restantes'] -= 1
        print(f"{prenom} {nom} ajouté au train pour Tours. Il reste {train['places_restantes']} places.")
        numero = (train['places_total']) - (train['places_restantes'])
        ticket(nom,prenom,numero,choix)
        
    if (choix == "Paris") :
        
        train = trains['ANG-PAR']
        
        if (passager in train['passagers']):
            print(f"Le passager {prenom} {nom} est déjà inscrit sur le trajet entre Angers et Paris.")
            return
        
        if (train['places_restantes'] <= 0):
            print(f"Plus de places disponibles pour le trajet à destination de Paris.")
            return
        
        train['passagers'].add(passager)
        train['places_restantes'] -= 1
        print(f"{prenom} {nom} ajouté au train pour Paris. Il reste {train['places_restantes']} places.")
        numero = (train['places_total']) - (train['places_restantes'])
        ticket(nom,prenom,numero,choix)
        
    
    


def annuler(trains):
    
    nom = input("Veuillez entrer le nom utilisé pour la réservation. ")
    prenom = input("Veuillez insérer le prénom utilisé pour la réservation. ")
    passager = (nom.upper(), prenom.capitalize())
    choix = input("Quel trajet souhaitez-vous annuler ? (Paris, Tours ou Nantes)")
    
    while (choix != "Nantes" and choix != "Tours" and choix != "Paris"):
        
        print("La destination choisie n'existe pas. Veuillez choisir entre Tours, Nantes et Paris.")
        choix = input("Quel trajet souhaitez vous annuler ? (Paris, Tours ou Nantes) ")
    
    if (choix == "Nantes") :
        
        train = trains['ANG-NTS']
        
        if (passager not in train['passagers']):
            print(f"Le passager {prenom} {nom} n'existe pas sur le trajet entre Angers et Nantes.")
            return
        
        train['passagers'].remove(passager)
        train['places_restantes'] += 1
        print(f"{prenom} {nom} supprimé train pour Nantes. Il reste {train['places_restantes']} places.")
    
    if (choix == "Tours") :
        
        train = trains['ANG-TRS']
        
        if (passager not in train['passagers']):
            print(f"Le passager {prenom} {nom} n'existe pas sur le trajet entre Angers et Tours.")
            return
        
        
        train['passagers'].remove(passager)
        train['places_restantes'] += 1
        print(f"{prenom} {nom} a été supprimé du train pour Tours. Il reste {train['places_restantes']} places.")
        
    if (choix == "Paris") :
        
        train = trains['ANG-PAR']
        
        if (passager not in train['passagers']):
            print(f"Le passager {prenom} {nom} n'existe pas sur le trajet entre Angers et Paris.")
            return
        
        train['passagers'].remove(passager)
        train['places_restantes'] += 1
        print(f"{prenom} {nom} a été supprimé du train pour Paris. Il reste {train['places_restantes']} places.")
    


def passagers(trains):
    
    print("Choisissez le train que vous souhaitez consulter.")
    choix = input (" 1️⃣ - Nantes \n 2️⃣ - Tours \n 3️⃣ - Paris \n")
        
    if(choix == '1'):
        
        print(f"Pour le trajet entre Angers et Nantes, voici la liste des passagers \n {trains['ANG-NTS']['passagers']}.")
        
    if(choix == '2'):
        
        print(f"Pour le trajet entre Angers et Tours, voici la liste des passagers \n {trains['ANG-TRS']['passagers']}.")
        
    if(choix == '3'):
        
        print(f"Pour le trajet entre Angers et Paris, voici la liste des passagers \n {trains['ANG-PAR']['passagers']}.")
        



def complet(trains):
    
    print("Voici la liste des trains complets :")
        
    for trajet, infos in trains.items():
        
        if(infos['places_restantes'] == 0):
            
            if(trajet == 'ANG-NTS'):
            
                print ("Le train à destination de Nantes est complet.")
            
            if(trajet == 'ANG-TRS'):
            
                print ("Le train à destination de Tours est complet.")
                
            if(trajet == 'ANG-PAR'):
            
                print ("Le train à destination de Paris est complet.")




def ticket(nom, prenom, numero, destination):
    
    numero = str(numero)
    
    print("============= Billet de votre trajet =============")
    print("  ")
    print("  ")
    print("  ")
    print("Nom du voyageur : " + nom)
    print("Prénom du voyageur : " + prenom)
    print("  ")
    print("Destination : " + destination)
    print("Numéro de siège : " + numero)
    

print("=== MENU RÉSERVATION TRAIN ===\n1️⃣  Afficher les trains\n2️⃣  Réserver une place\n3️⃣  Annuler une réservation\n4️⃣  Afficher les passagers d’un train\n5️⃣  Voir les trains complets\n0️⃣  Quitter")

choix = input("Que souhaitez-vous faire ? ")

while(choix != '0'):

    if(choix == '1'):
        
        afficher(trains)
        
    if(choix == '2'):
        
        reserver(trains)
        
    if(choix == '3'):
        
        annuler(trains)
        
    if(choix == '4'):
        
        passagers(trains)
        
    if(choix == '5'):
        
        complet(trains)
    
    print("=== MENU RÉSERVATION TRAIN ===\n1️⃣  Afficher les trains\n2️⃣  Réserver une place\n3️⃣  Annuler une réservation\n4️⃣  Afficher les passagers d’un train\n5️⃣  Voir les trains complets\n0️⃣  Quitter")
    choix = input("Que souhaitez-vous faire ? ")
    













