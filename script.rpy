# Définition des personnages
define e = Character("Accueil Perso", color="#42aaff")
define p = Character("Professeur", color="#ff8c00")
define c_proviseur = Character("Proviseur", color="#800000")  
define d = Character("Directeur", color="#008000")
define el = Character("Élève", color="#ff1493")
define l = Character("Lola", color="#4b01c2")

# Images des lieux
image map_overlay = "images/decor_8_hover.png"  # Image avec surbrillance des zones
image salle_profs = "images/decor_3.png"
image cdi_bg = "images/decor_4.png"
image salle_info = "images/decor_6.png"
image terrain_sport = "images/decor_7.png"
image club_journalisme = "images/club_journalisme.jpg"

# Images des lieux
image bureau_proviseur = "images/backgrounds/b_bureau_proviseur.png"  # Image du bureau du proviseur
image character_proviseur = "images/characters/c_proviseur.png"
image telephone = "images/gui/telephone.png"  # Image du téléphone

#Initialisation des variables de score par quête
#default quete1_score = 0
#default quete2_score = 0
default quete3_score = 0
#Initialise la variable des quêtes complétées
default quetes_complete = 0
# Initialisation des variables d'opportunités de score par quête
#default quete1_opportunity = ?
#default quete2_opportunity = ?
default quete3_opportunity = 4 #4 possibilités de bien répondre et donc 4 points de score possibles pour cette quête
    
#Variable pour les témoignages récupérés par le joueur dans la quête 3
default témoignages_récupérés = []  # Initialise une liste vide pour stocker les témoignages récupérés par le joueur

# Initialisation des variables
init :
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
    
    def calculer_pourcentage(): #pour calculer le total du score = % de fiabilité de l'article final
        total_score = quete1_score + quete2_score + quete3_score
        total_opportunity = quete1_opportunity + quete2_opportunity + quete3_opportunity
        pourcentage = (float(total_score) / total_opportunity) * 100
        return pourcentage

# Faites pas gaffe, c'est juste pour caler les zones de la map cliquable avec l'image
screen debug_mouse_position():
    textbutton "Afficher Coordonnées" action Show("mouse_position") xpos 20 ypos 20

screen mouse_position():
    text "[mousepos]" xalign 0.5 yalign 0.95
    timer 0.1 action [SetVariable("mousepos", str(renpy.get_mouse_pos())), Show("mouse_position")]


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


##océ#





# Écran de tutoriel pour l'inventaire
screen tutoriel_inventaire():
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
            yalign 0.1
            text "Votre Inventaire" size 40 xalign 0.5

            text "Fonctionnalités:" size 30 xalign 0.5Z
            text "• Voir les objets récoltés" xalign 0.5
            text "• Utiliser les objets pour progresser" xalign 0.5
            text "• Gérer les objets importants" xalign 0.5

      
        textbutton "J'ai compris" action [Hide("tutoriel_inventaire"), Return()] xalign 0.5 yalign 0.95


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

# Destinations
label start:
    # Configuration des touches et écrans
    $ config.keymap['inventory'] = ['e', 'E']
    $ config.underlay.append(renpy.Keymap(inventory=lambda: renpy.show_screen('inventory_screen')))
    show screen debug_mouse_position

    scene bureau_proviseur
    with fade

    "Vous êtes convoqués dans le bureau du proviseur avec les autres membres du club journalisme."

    show c_proviseur at center

    c_proviseur "Merci d'être venus si rapidement. Nous avons une situation délicate entre les mains."

    c_proviseur "Il y a des rumeurs qui circulent dans tout le collège. Une vague de désinformation secoue l'établissement, et tout le monde semble se laisser emporter."

    c_proviseur "C'est cette vidéo qui a tout déclenché..."

    hide c_proviseur

    scene black

    play movie "videos/v_deepfake.mp4"
    show movie

    "Voici une vidéo à propos des deepfakes."

    stop movie
    hide movie

    "La vidéo est terminée."

    "La vidéo montre Paul, un élève de 5ème, en train de frapper un mur du collège avec ce qui ressemble à une pioche."

    "On l'entend dire : « Je vais trouver du diamant comme dans Minecraft ! »"

    "Les commentaires sous la vidéo s'enflamment, accusant les jeux vidéo de pousser les adolescents à des comportements violents."

    hide video_tiktok
    show c_proviseur at center
    with dissolve

    c_proviseur "Cette vidéo est devenue virale. Les parents s'inquiètent, les médias locaux commencent à s'intéresser à l'affaire."

    c_proviseur "Mais je soupçonne que la situation est plus complexe qu'elle n'y paraît."

    c_proviseur "J'ai besoin que votre club journalisme mène l'enquête pour démêler le vrai du faux."

    c_proviseur "Vous devrez recueillir des témoignages, analyser les sources d'information et publier un article qui rétablira la vérité."

    c_proviseur "Pour mener cette mission à bien, vous aurez accès à un inventaire pour gérer les objets que vous récolterez."

    show inventory at right
    with moveinright

    c_proviseur "Il vous permettra de voir les objets récoltés, de les utiliser pour progresser dans votre enquête, et de gérer les objets importants."

    c_proviseur "Je vous ai débloqué tous les accès, vous devriez y jeter un œil."

    # Lancement du tutoriel de l'inventaire
    call screen tutoriel_inventaire

    hide inventory

    c_proviseur "Bonne chance dans votre enquête. La réputation de Paul et la perception des jeux vidéo au sein de notre établissement sont entre vos mains."

    hide c_proviseur
    with dissolve

    e "Maintenant que nous avons notre mission, nous devons organiser notre enquête. Retournons au club journalisme!"

    jump map_screen



























































##

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


        # Club journalisme
        hotspot (290, 250, 200, 150) action Jump("professeur")
        
        # CDI 
        hotspot (1400, 300, 230, 180) action Jump("cdi")
        
        # Salle info
        hotspot (800, 400, 220, 150) action Jump("eleve_concerne")
        
        # Terrain sport
        hotspot (600, 650, 250, 200) action Jump("prof_sport")
        
        # Bouton
        textbutton "Retour" action Return() xpos 20 ypos 1000


# Quête 3 - point d'entrée
label quete_3:
    scene club_journalisme
    #show lola (manque image)

    l "Salut ! Du coup, pour écrire notre article j’ai mis un message sur le Forum de l’ENT du collège pour voir si des élèves et des profs avaient envie de témoigner et de nous donner des informations."
    l "Je ne m’attendais pas à ça, mais le forum déborde. J’ai fais un premier tri mais là {b}j’ai vraiment besoin de toi pour trier les derniers messages.{/b}"
    l "Le problème c’est que certains ont l’air un peu bizarres. Je pense qu’il y en a quelques un qui ne sont pas fiables et que mon cerveau me joue des tours."
    l "Tu sais en classe on nous a parlé des {b}biais cognitifs{/b} et que ça pouvait nous empêcher d’y voir claire face à des informations ou des témoignages, mais viens on va regarder tout ça sur mon ordinateur."

#jump ordinateur_lola (manque image)

# Scène 2 - Explication des biais
label ordinateur_lola:
    #scene ordinateur
    #show lola sérieux (manque image)

    l "Pour t'aider, voici ce que j’ai noté en cours sur trois biais cognitifs courants dans la diffusion de fausses informations :"
    l "{b}Corrélation illusoire :{/b} c'est quand on voit un lien entre deux événements qui n'existent pas réellement."
    l "{b}Autorité :{/b} croire qu'une information est vraie simplement parce qu'elle provient d'une figure réputée, sans vérifier les faits."
    l "{b}Confirmation{/b} (cherry picking) {b}:{/b} ce biais nous pousse à ne retenir que les infos qui confirment nos croyances et à ignorer celles qui pourraient les contredire."
    l "Donc là il faut vraiment que tu check chaque témoignage du forum. Pour chaque message, tu as deux options : Le Récupérer si tu sens qu’il est fiable ou l’Analyser si tu sens qu’il l’est pas. Et si en plus tu trouve quel biais entre en jeu, alors t’es un boss."
    l "Après si t’analyse un témoignage qui au final est fiable c’est pas grave hein, vaut mieux être trop prudent que pas assez, tu pourra toujours le récupérer. Mais si tu dis qu’il est biaisé alors que non, c’est dommage on le mettra de côté pour rien."
    l "Si t’as tout compris et que t’es Prêt(e), allons voir le forum !"

    #jump forum
    jump témoignage_1

#label forum:
    #scene forum (manque image)
    #show écran_ordinateur (manque visuel forum)

    #jump téémoignage_1 # est-ce qu'on met un visuel du témoignage sur un forum où on laisse l'image d'un écran d'ordi ?

label témoignage_1:
    #scene forum (manque image)
    #show avatar_témoin_1 (manque visuel avatar) 
    #On peut peut-être mettre une pastille comme une photo d'avatar/de profil d'un forum pour illustrer ?

    # Texte du témoignage
    "« Depuis que mon petit frère joue aux jeux de tir, il semble de plus en plus agressif. Ça doit être dû aux jeux vidéo. »"

    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            l "Hmm... Ok, moi je trouve que le lien qu'il fait est bizarre..."  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            $ témoignages_récupérés.append("Témoignage 1 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
            jump témoignage_2  # Saute vers le témoignage suivant

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            jump analyse_biais_1  # Saute vers l'analyse du témoignage

    return  

# Analyse du premier témoignage
label analyse_biais_1:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            l "Je crois que c'est plutôt un biais de corrélation illusoire. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump témoignage_2
        "Confirmation":
            l "Je crois que c'est plutôt un biais de corrélation illusoire. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump témoignage_2
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            l "Trop fort ! T'as identifié le biais de corrélation illusoire. Le témoignage n'était pas fiable."  # Lola félicite le joueur
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1  # Augmente le score du joueur de 1
            jump témoignage_2  # Saute vers le témoignage suivant
        "fiable":
            l "Hmm... Ok, moi je trouve que le lien qu'il fait est bizarre..."  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
    $ quete3_score -= 1  # Score = -1
    $ témoignages_récupérés.append("Témoignage 1 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
    jump témoignage_2  # Saute vers le témoignage suivant

label témoignage_2:
    #scene forum (manque image)
    #show avatar_témoin_2 (manque visuel avatar) 
    #On peut peut-être mettre une pastille comme une photo d'avatar/de profil d'un forum pour illustrer ?

    # Texte du témoignage
    "« Un célèbre youtubeur a affirmé que les jeux vidéo rendent violent. Il ne se trompe jamais, donc ça doit être vrai. »"

    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            l "Hmm… Ok, moi je trouve qu’il fait confiance un peu vite à ce Youtubeur, en plus il dit même pas qui c’est … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            $ témoignages_récupérés.append("Témoignage 2 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
            jump temoignage_3  # Saute vers le témoignage suivant

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            jump analyse_biais_2  # Saute vers l'analyse du témoignage

    return  

# Analyse du deuxième témoignage
label analyse_biais_2:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            l "T’es le boss ! T’as identifié le biais d’autorité. Le témoignage n'était pas fiable."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump temoignage_3
        "Confirmation":
            l "Je crois que c’est plutôt un biais d’autorité. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump temoignage_3
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            l "Je crois que c’est plutôt un biais d’autorité. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Lola félicite le joueur
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1  # Augmente le score du joueur de 1
            jump temoignage_3  # Saute vers le témoignage suivant
        "fiable":
            l "Hmm… Ok, moi je trouve qu’il fait confiance un peu vite à ce Youtubeur, en plus il dit même pas qui c’est … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
    $ quete3_score -= 1  # Score = -1
    $ témoignages_récupérés.append("Témoignage 2 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
    jump temoignage_3  # Saute vers le témoignage suivant
    
label temoignage_3:
    #scene forum (manque image)
    #show avatar_témoin_2 (manque visuel avatar) 
    #On peut peut-être mettre une pastille comme une photo d'avatar/de profil d'un forum pour illustrer ?

    # Texte du témoignage
    "« Une récente enquête menée par un collectif de journalistes indépendants montre que la violence dans les collèges reste stable malgré la popularité des jeux vidéo. J’ai même le liens de l’enquête si vous voulez. »"

    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            l "Parfait ! Ce témoignage est fiable et précieux pour notre article. En plus il a même mis le lien vers l'enquête, c'est top !" # Feedback bonne réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            $ témoignages_récupérés.append("Témoignage 3 (Fiable)")
            jump témoignage_4

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            jump analyse_biais_3  # Saute vers l'analyse du témoignage

    return  

# Analyse du troisième témoignage
label analyse_biais_3:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            l "T’es sur ? Pourtant il parle de journaliste indépendant, met sa source et tout, j’ai vraiment cru que c’était fiable. Mais bon c’est toi le spécialiste hein !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            jump témoignage_4
        "Confirmation":
            l "T’es sur ? Pourtant il parle de journaliste indépendant, met sa source et tout, j’ai vraiment cru que c’était fiable. Mais bon c’est toi le spécialiste hein !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            jump témoignage_4
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            l "T’es sur ? Pourtant il parle de journaliste indépendant, met sa source et tout, j’ai vraiment cru que c’était fiable. Mais bon c’est toi le spécialiste hein !"  # Feedback mauvaise réponse
            $ quete3_score -= 1  # Score = -1  # Augmente le score du joueur de 1
            jump témoignage_4  # Saute vers le témoignage suivant
        "fiable":
            l "Parfait ! Ce témoignage est fiable et précieux pour notre article. En plus il a même mis le lien vers l'enquête, c'est top !" # Feedback bonne réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
    $ témoignages_récupérés.append("Témoignage 2 (Fiable)")  # Ajoute le témoignage à la liste des témoignages récupérés
    jump témoignage_4  # Saute vers le témoignage suivant

    label témoignage_4:
    #scene forum (manque image)
    #show avatar_témoin_2 (manque visuel avatar) 
    #On peut peut-être mettre une pastille comme une photo d'avatar/de profil d'un forum pour illustrer ?

    # Texte du témoignage
    "« J’ai lu plein d’articles expliquant que les jeux vidéo augmentent l’agressivité, ils en parlent tout le temps sur TikTok et tous mes amis pensent la même chose. Ça ne peut pas être une coïncidence.»"
    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            l "Ah ouais … Ok. Moi je trouve pas que ce qu’il dit soit basé sur des infos vraiment fondées son témoignage, puis bon il cite même pas les articles, et alors TikTok moi j’suis pas sûre de valider … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            $ témoignages_récupérés.append("Témoignage 2 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
            jump conclusion_quete3  # Saute vers le témoignage suivant

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            jump analyse_biais_4  # Saute vers l'analyse du témoignage

    return  

# Analyse du premier témoignage
label analyse_biais_4:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            l "Je crois que c’est plutôt un biais de confirmation. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump conclusion_quete3
        "Confirmation":
            l "T’es le boss ! T’as identifié le biais de confirmation. Le témoignage n'était pas fiable." # Feedback bonne réponse
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump conclusion_quete3
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            l "Je crois que c’est plutôt un biais de confirmation. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score += 1  # Augmente le score du joueur de 1
            jump conclusion_quete3  # Saute vers le témoignage suivant
        "fiable":
            l "Ah ouais … Ok. Moi je trouve pas que ce qu’il dit soit basé sur des infos vraiment fondées son témoignage, puis bon il cite même pas les articles, et alors TikTok moi j’suis pas sûre de valider … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
    $ quete3_score -= 1  # Score = -1
    $ témoignages_récupérés.append("Témoignage 4 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
    jump conclusion_quete3  # Saute vers le témoignage suivant


label conclusion_quete3:
    scene club_journalisme

    $ score = quete3_score  # Enregistre le score de la quête 3
    $ quetes_complete += 1  # Incrémente le nombre de quêtes complétées

    if quete3_score >= 3:
        l "Bravo, grâce à toi on a des témoignages vraiment fiables pour l’article..."
    elif quete3_score >= 2:
        l "Je pense que tu as peut-être fait quelques erreurs, mais l'important est que tu as su repérer des messages douteux..."
    else:
        l "Avec un peu de recul, je ne suis pas trop sûre de tes choix..."
        
    return