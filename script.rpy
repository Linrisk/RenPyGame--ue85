# Définition des personnages
define e = Character("Accueil Perso", color="#42aaff")
define p = Character("Professeur", color="#ff8c00")
define d = Character("Directeur", color="#008000")
define el = Character("Élève", color="#ff1493")

# Images des lieux
image map_overlay = "images/decor_8_hover.png"  # Image avec surbrillance des zones
image salle_profs = "images/decor_3.png"
image cdi_bg = "images/decor_4.png"
image salle_info = "images/decor_6.png"
image terrain_sport = "images/decor_7.png"

# Initialisation des variables
init:
    default mousepos = "(0, 0)"
    # Système d'inventaire
    default inventory = []
    default inventory_visible = False
    default max_items = 10
    
    # Définition des objets récupérables (Lorempsum non fonctionnel// C'était pour test la mécanique)
    default items = {
        "carnet": {"name": "Carnet de notes", "image": "images/item_carnet.png", "description": "Notes du professeur avec des marques de connexion."},
        "cle_usb": {"name": "Clé USB", "image": "images/item_cle_usb.png", "description": "Contient des fichiers suspects datés du jour de l'incident."},
        "emploi_temps": {"name": "Emploi du temps", "image": "images/item_emploi.png", "description": "L'emploi du temps de l'élève accusé. Il était en sport lors de l'envoi."},
        "journal_cdi": {"name": "Registre du CDI", "image": "images/item_registre.png", "description": "Liste des élèves présents au CDI ce jour-là."},
        "capture_ecran": {"name": "Capture d'écran", "image": "images/item_capture.png", "description": "Preuve de connexion à l'ENT à une heure suspecte."}
    }

init python:
    def afficher_coord(x, y):
        renpy.notify(f"Position : ({x}, {y})")
        
    def add_to_inventory(item_id):
        if item_id in items and len(inventory) < max_items and item_id not in inventory:
            inventory.append(item_id)
            renpy.notify(f"{items[item_id]['name']} ajouté à l'inventaire")
            return True
        elif item_id in inventory:
            renpy.notify("Vous avez déjà cet objet")
        else:
            renpy.notify("Inventaire plein")
            return False

# Faites pas gaffe, c'est juste pour caler les zones de la map cliquable avec l'image
screen debug_mouse_position():
    textbutton "Afficher Coordonnées" action Show("mouse_position") xpos 20 ypos 20

screen mouse_position():
    text "[mousepos]" xalign 0.5 yalign 0.95
    timer 0.1 action [SetVariable("mousepos", str(renpy.get_mouse_pos())), Show("mouse_position")]

# Inventaire
screen inventory_screen():
    modal True
    
    frame:
        background "gui/frame.png"
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.0
            text "Inventaire" size 40 xalign 0.5
            
            grid 5 2:
                spacing 10
                xalign 0.5
                for item_id in inventory:
                    frame:
                        xsize 150
                        ysize 150
                        imagebutton:
                            idle items[item_id]["image"]
                            action Show("item_description", item_id=item_id)
                            xalign 0.5
                            yalign 0.5
                # Remplir avec des slots vides
                for i in range(max_items - len(inventory)):
                    frame:
                        xsize 150
                        ysize 150
                        text "Vide" xalign 0.5 yalign 0.5
        
        textbutton "Fermer" action Hide("inventory_screen") xalign 0.5 yalign 0.95

# Detail des objets maggle
screen item_description(item_id):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 300
        
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            
            text items[item_id]["name"] size 30 xalign 0.5
            null height 20
            image items[item_id]["image"] xalign 0.5
            null height 20
            text items[item_id]["description"] xalign 0.5
            
        textbutton "Fermer" action Hide("item_description") xalign 0.5 yalign 0.95

# Destinations
label start:
    show screen debug_mouse_position
    scene black
    with fade
    e "Bienvenue, enquêteur en herbe ! Il faut innocenter l'élève et trouver le véritable coupable."
    e "Nous avons plusieurs lieux à explorer. Choisis où commencer."
    e "Appuie sur la touche E à tout moment pour accéder à ton inventaire."
    
    # Initialisation des touches pour l'inventaire
    $ config.keymap['inventory'] = ['e', 'E']
    $ config.underlay.append(renpy.Keymap(inventory=lambda: renpy.show_screen('inventory_screen')))
    
    jump map_screen

# Carte
label map_screen:
    with fade
    show screen mouse_position  # Affiche les coordonnées de la souris
    call screen map_interactive
    return

screen map_interactive():
    imagemap:
        ground "images/decor_8.png"
        hover "images/decor_8_hover.png"  # Affiche la version surbrillante au survol
        
        #Memento, image en 1920x1080 importantes!


        # Salle des profs 
        hotspot (290, 250, 200, 150) action Jump("professeur")
        
        # CDI 
        hotspot (1400, 300, 230, 180) action Jump("cdi")
        
        # Salle info
        hotspot (800, 400, 220, 150) action Jump("eleve_concerne")
        
        # Terrain sport
        hotspot (600, 650, 250, 200) action Jump("prof_sport")
        
        # Bouton
        textbutton "Retour" action Return() xpos 20 ypos 1000


label professeur:
    scene salle_profs
    with fade
    p "Ce n'est pas moi qui ai envoyé ce mail ! Mon mot de passe était trop simple..."
    p "Regardez, ces captures de mon ENT sont bizarres..."
    
    menu:
        "Que faire ?"
        
        "Examiner l'ordinateur":
            p "Vous pouvez voir ici les traces de connexion suspectes."
            "Vous remarquez une capture d'écran montrant une connexion à l'heure de l'incident."
            $ add_to_inventory("capture_ecran")
        
        "Demander plus d'informations":
            p "J'ai noté quelques observations dans mon carnet. Prenez-le, ça pourrait vous aider."
            $ add_to_inventory("carnet")
    
    jump map_screen

label cdi:
    scene cdi_bg
    with fade
    d "Nous avons noté qui était présent dans le CDI ce jour-là."
    
    menu:
        "Que faire ?"
        
        "Consulter le registre":
            d "Voici le registre des présences. Certains élèves ont utilisé les ordinateurs du CDI."
            $ add_to_inventory("journal_cdi")
        
        "Observer les ordinateurs":
            "Vous remarquez qu'un des ordinateurs du CDI a encore l'historique de navigation ouvert."
            "Une clé USB a été oubliée dans l'un des ports."
            $ add_to_inventory("cle_usb")
    
    jump map_screen

label eleve_concerne:
    scene salle_info
    with fade
    el "Je ne sais pas qui m'en voulait... Peut-être mes adversaires de la dernière compétition ?"
    el "Mais comment prouver que ce n'est pas moi ?"
    
    menu:
        "Que faire ?"
        
        "Demander son emploi du temps":
            el "J'étais en cours de sport au moment où le mail a été envoyé. Voici mon emploi du temps."
            $ add_to_inventory("emploi_temps")
        
        "Examiner son ordinateur":
            "L'ordinateur n'a pas de traces de connexion à l'ENT au moment des faits."
            "Cela renforce l'alibi de l'élève."
    
    jump map_screen

label prof_sport:
    scene terrain_sport
    with fade
    p "Voici le plan du circuit. Les premiers élèves de la course peuvent témoigner."
    p "L'élève accusé a participé à la course et a terminé deuxième. Impossible qu'il ait envoyé ce mail en même temps."
    
    "Les témoignages des autres élèves confirment que l'élève accusé était bien présent pendant toute la durée du cours de sport."
    
    jump map_screen

    #ti kokiyol#