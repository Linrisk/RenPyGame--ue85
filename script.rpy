define e = Character("Accueil Perso", color="#42aaff")
define p = Character("Professeur", color="#ff8c00")
define c_proviseur = Character("Proviseur", color="#800000")
define d = Character("Directeur", color="#008000")
define el = Character("Élève", color="#ff1493")
#Lola est la technicienne du club - Quête 3 - Analyse des témoignages sur le Forum
define l = Character("Lola", color="#4b01c2")
define alexis = Character("Alexis (Rédacteur)", color="#00bfff")
define technicienne = Character("Technicienne", color="#ff69b4")
#Responsable graphisme et photographie - Quête 2 - Analyse la vidéo deepfake
define alice = Character("Alice", color="#32cd32")
define lucas = Character("Lucas", color="#fff200")
define ethan = Character("Ethan", color="#a068ff")

# Images des lieux
image map_overlay = "images/decor_8_hover.png"  # Image avec surbrillance des zones
image salle_profs = "images/decor_3.png"
image cdi_bg = "images/decor_4.png"
image b_salle_info = "images/backgrounds/b_salle_info.png"
image b_couloirs = "images/backgrounds/b_couloirs.png"
image b_couloirs_2 = "images/backgrounds/b_couloirs_2.png"
image b_club = "images/b_club.png"
image b_salle_technicien = "images/backgrounds/b_salle_technicien.png"  # Image de la salle de la technicienne

# Images des personnages
image bureau_proviseur = "images/backgrounds/b_bureau_proviseur.png"  # Image du bureau du proviseur
image c_lola = "images/characters/c_lola.png"
image c_lola_p = "images/characters/c_lola_pensive.png"
image c_ethan = "images/characters/c_ethan.png"
image c_ethan_2 = "images/characters/c_ethan_2.png"
image c_lucas_enerve = "images/characters/c_lucas_enerve.png"
image c_lucas_normal = "images/characters/c_lucas_enerve.png"
image c_alice_sourit = "images/characters/c_alice_sourit.png"
image c_alice_triste = "images/characters/c_alice_triste.png"
image character_enzo_ = "images/characters/c_enzo.png"
image character_alexis_sourit = "images/characters/c_alexis_sourit.png"
image character_alexis_sourit_pas = "images/characters/c_alexis_sourit.png"
image technicienne = "images/characters/c_alice_sourit.png"
image c_proviseur = "images/characters/c_proviseur.png"

#images GUI
image telephone = "images/gui/telephone.png"  # Image du téléphone
image forum = "images/gui/bg_forum.png"
image ordi_forum = "images/gui/bg_ordi_tech.png"

#images Items
image temoi1 = "images/items/T1.png"
image temoi2 = "images/items/T2.png"
image temoi3 = "images/items/T3.png"
image temoi4 = "images/items/T4.png"

#Images quête_2 

image bg_video_analysis = "images/backgrounds/b_zoom_ordi_technicien.png"
image oeil = "images/icons/eye.png"
image account = "images/icons/account.png"
image zoom_visage = "images/zoom_visage.png"
image zoom_main = "images/zoom_main.png"
image fake_account_profile = "images/fake_account_profile.png"
image fake_account_videos = "images/fake_account_videos.png"
image legit_account = "images/legit_account.png"
image fake_account_video_1 = Movie(play="videos/video_fake_account_1.webm", size=(640,360), loop=False)
image fake_account_video_2 = Movie(play="videos/video_fake_account_2.webm", size=(640,360), loop=False)




# Initialisation des variables de score par quête
default quete1_score = 0
default quete2_score = 0
default quete3_score = 0
# Initialise la variable des quêtes complétées
default quetes_complete = 0
# Initialisation des variables d'opportunités de score par quête
default quete1_opportunity = 4
default quete2_opportunity = 4
default quete3_opportunity = 4 # 4 possibilités de bien répondre et donc 4 points de score possibles pour cette quête

# Variable pour les témoignages récupérés par le joueur dans la quête 3
default témoignages_récupérés = []  # Initialise une liste vide pour stocker les témoignages récupérés par le joueur

#Variable quête 1, pour que le jeu vérifie quand le joueur a parlé à lucas et ethan et ne pas répéter les dialogues
default a_parle_a_lucas = False
default a_parle_a_ethan = False

#scene de fin 
default article_incomplet= False #si le joueur n'a pas récupéré tous les témoignages, il ne peut pas publier l'article
default nombre_preuves_fiables = 0
default total_preuves = 0
default selected_items = []
default score_items = "0%"

#Zoom personnage dialogues 
init: 
    transform zoom_perso:
        zoom 1.2   # 1.0 = taille normale, 1.3 = 30% plus grand quand le personnage parle alors qu'ils sont plusieurs.    
# Transform pour les autres personnages
    transform taille_normale:
        zoom 1.0

# Initialisation des variables
init:

    default quests = {
    "alexis": False,
    "technicienne": False,
    "respo_interview": False
    }
    default current_quest = None

    default mousepos = "(0, 0)"
    # Système d'inventaire
    default inventory = []
    default inventory_visible = False
    default max_items = 10

    # Définition des objets récupérables
    default items = {
    "article_ethan": {
        "name": "Article Ethan", 
        "image": "gui/icons/files.png", 
        "description": "Article d'Ethan sur les jeux vidéo.",
        "fiable": False
    },
    "article_lucas": {
        "name": "Article Lucas", 
        "image": "gui/icons/files.png", 
        "description": "Article de Lucas sur les jeux vidéo.",
        "fiable": True
    },
    "temoignage1": {
        "name": "Témoignage Élève A", 
        "image": "gui/icons/files.png",
        "description": "Témoignage non vérifié sur l'incident",
        "fiable": False
    },
    "temoignage2": {
        "name": "Témoignage Youtubeur", 
        "image": "gui/icons/files.png",
        "description": "Déclaration non sourcée",
        "fiable": False
    },
    "temoignage3": {
        "name": "Témoignage Journal", 
        "image": "gui/icons/files.png",
        "description": "Témoignage vérifié avec source",
        "fiable": True
    },
    "temoignage4": {
        "name": "Témoignage TikTok", 
        "image": "gui/icons/files.png",
        "description": "Témoignage viral non corroboré",
        "fiable": False
    },
    "fiche_biais": {
        "name": "Fiche Biais Cognitifs", 
        "image": "gui/icons/files.png",
        "description": "Mémo sur les biais courants",
        "fiable": True
    },
    "fiche_conclusion_video": {
    "name": "Rapport d'analyse vidéo", 
    "image": "gui/icons/files.png",
    "description": "Conclusion technique sur l'authenticité",
    "fiable": True  # À adapter selon le choix
    }


}


init python:
    def toggle_selection(item):
        if item in selected_items:
            selected_items.remove(item)
        else:
            selected_items.append(item)

    def update_score():
        if not selected_items:
            return "0%"
        fiables = sum(1 for i in selected_items if i.get("fiable", False))
        return f"{(fiables * 100) // len(selected_items)}%"

    quests = {
        "alexis": False,
        "technicienne": False,
        "respo_interview": False
    }
    ##Je mets l'affichage inventaire en haut à gauche - fin le boutton
    config.overlay_screens.append("hud")


    def add_to_inventory(item_id, fiable=False):
        if item_id in items and len(inventory) < max_items:
            inventory.append({
                "id": item_id,
                "fiable": items[item_id].get("fiable", fiable)
            })
            renpy.notify(f"{items[item_id]['name']} ajouté à l'inventaire")
            return True
        return False



    def calculer_pourcentage(): # pour calculer le total du score = % de fiabilité de l'article final
        total_score = quete1_score + quete2_score + quete3_score
        total_opportunity = quete1_opportunity + quete2_opportunity + quete3_opportunity
        pourcentage = (float(total_score) / total_opportunity) * 100
        return pourcentage

    def pause_music_with_fade():
        renpy.music.set_volume(0.0, delay=1.5, channel="music")
        renpy.pause(1.0)
        renpy.music.set_pause(True, channel="music")

    def resume_music_with_fade():
        renpy.music.set_pause(False, channel="music")
        renpy.music.set_volume(1.0, delay=0.5, channel="music")

# Faites pas gaffe, c'est juste pour caler les zones de la map cliquable avec l'image
screen debug_mouse_position():
    textbutton "Afficher Coordonnées" action Show("mouse_position") xpos 20 ypos 20

screen mouse_position():
    text "[mousepos]" xalign 0.5 yalign 0.95
    timer 0.1 action [SetVariable("mousepos", str(renpy.get_mouse_pos())), Show("mouse_position")]

# Détail des objets
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

# Écran de tutoriel pour l'inventaire
screen tutoriel_inventaire():
    modal True
    add "gui/g_inventory.png" xalign 0.5 yalign 0.2
    frame:
        background None
        xalign 0.5
        yalign 0.8
        xsize 800
        ysize 600

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.1
            text "Votre Inventaire" size 40 xalign 0.5

            text "Fonctionnalités:" size 30 xalign 0.5
            text "• Voir les objets récoltés" xalign 0.5
            text "• Gérer les objets importants" xalign 0.5

        textbutton "J'ai compris" action [Hide("tutoriel_inventaire"), Return()] xalign 0.5 yalign 0.95

# Inventaire
screen inventory_screen():
    modal True
    add "gui/g_inventory.png" xalign 0.5 yalign 0.5

    frame:
        background None
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
                    use inventory_slot(item_id)
                for i in range(max_items - len(inventory)):
                    frame:
                        xsize 150
                        ysize 150
                        text "Vide" xalign 0.5 yalign 0.5

        textbutton "Fermer" action Hide("inventory_screen") xalign 0.5 yalign 0.95


##Screen pour les objets et pour l'affichage les objets dans l'inventaire et les objets dans les étiquettes  

screen inventory_slot(item_id):
    default show_tooltip = False

    frame:
        xsize 150
        ysize 150
        imagebutton:
            idle items[item_id]["image"]
            action Show("item_description", item_id=item_id)
            hovered SetScreenVariable("show_tooltip", True)
            unhovered SetScreenVariable("show_tooltip", False)
            xalign 0.5
            yalign 0.5

        if show_tooltip:
            frame:
                background "#333c"
                xsize 140
                ysize 40
                xpos 10
                ypos 110
                text items[item_id]["name"] size 18 xalign 0.5
                text items[item_id]["description"] size 14 xalign 0.5

screen hud():
    textbutton "Inventaire" action ToggleScreen("inventory_screen") xpos 20 ypos 20



# Destinations
label start:
    play music "intro_jeu.ogg"volume 0.3
    scene bureau_proviseur
    with fade
    "Bienvenu au collège Beausoleil"
    "Vous êtes le.la responsable journalisme d'investigation du club de journalisme de l'établissement"
    "Vous et vos amis membres du club êtes convoqués dans le bureau du proviseur."
    "Un grave problème secoue le collège en ce moment, mais le proviseur va vous expliquer la situation en détail"

    show c_proviseur at center

    c_proviseur "Bonjour à tous !"
    c_proviseur "Merci d'être venus si rapidement."
    c_proviseur "Nous avons une situation délicate entre les mains."

    pause(0.5)

    c_proviseur "Une vague de désinformation secoue l'établissement..."

    c_proviseur "C'est cette vidéo qui a tout déclenché, elle montre Paul un élève de 5ème dans une situation plus que délicate, je vous laisse juger par vous même de la situation"

    $ pause_music_with_fade()

    hide c_proviseur

    scene black

    show screen video_popup("videos/v_deepfake.webm")
    $ renpy.pause(0.1, hard=True)  # pour laisser le temps à la vidéo de démarrer

      

    "La vidéo est terminée."

    $ resume_music_with_fade()

    show c_proviseur
    c_proviseur "La vidéo montre donc Paul, un élève de 5ème, après qu'il ait fais un trou dans un mur du collège avec une pioche."

    c_proviseur "Les commentaires sous la vidéo s'enflamment, certains affirment qu'il se serait cru dans le jeu vidéo Minecraft et qu'il aura détruit le mur pour récolter du diamant, exactement comme dans le jeu !"
    c_proviseur "Le vrai problème, la majorité des commentaires accusent les jeux vidéo de pousser les adolescents à des comportements violents, sans aucune nuance et surtout sans preuve ou source fiable."

    hide video_tiktok
    show c_proviseur at center
    with dissolve

    c_proviseur "Cette vidéo est devenue virale. Les parents s'inquiètent, les médias locaux commencent à s'intéresser à l'affaire."

    c_proviseur "Mais je soupçonne que la situation est plus complexe qu'elle n'y paraît."

    c_proviseur "J'ai besoin que votre club de journalisme mène l'enquête pour démêler le vrai du faux."

    c_proviseur "Vous devrez recueillir des témoignages, analyser les sources d'information que vous pourrez trouver, analyser la vidéo de Paul et finalement publier un article fiable qui rétablira la vérité et apaisera tout le monde."

    c_proviseur "Pour mener cette mission à bien, vous aurez accès à un inventaire."
   
    

    c_proviseur "Il vous permettra de voir les objets récoltés, et de les utiliser pour progresser dans votre enquête."

    c_proviseur "Je vous ai débloqué tous les accès, vous devriez y jeter un œil."

    c_proviseur "Pour afficher l'inventaire appuyez sur la touche E du clavier. Cliquez ensuite sur Fermer pour le faire disparaitre."
    hide c_proviseur
    

    # Lancement du tutoriel de l'inventaire
    call screen tutoriel_inventaire

    hide inventory

    show c_proviseur

    c_proviseur "Bonne chance dans votre enquête. La réputation de Paul est en jeu, et la sauvegarde de l'esprit critique de nos élèves est entre vos mains."

    hide c_proviseur
    with dissolve

    "Maintenant que vous connaissez les détails de votre mission, vous devez organniser votre enquête. Rendez-vous dans la salle du club journalisme!"

    jump club_journalisme_intro

# Scène 2 : Début de l’enquête
# Lieu : Club Journalisme
label club_journalisme_intro:
    scene club_journalisme
    with fade

    play music "presentation_club.mp3" fadeout 1.0 fadein 1.0
    "Vous voici dans la salle du club de journalisme, prêt à organiser votre enquête avec les autres membres du club."

    show character_alexis_sourit at left, zoom_perso
    show technicienne at center
    show c_lola at right

    alexis "Vu que tu es le.la responsable de l’investigation, le mieux, c’est que tu partes sur le terrain pour récolter un maximum d’informations."

    alexis "On doit rédiger un article fiable, basé sur des faits vérifiés pour rétablir le calme dans le collège, on est tous là en soutien mais tu es l'expert.e en investigation donc on te fait confiance."

    alexis "Bien sûr, on est tous spécialisés dans un domaine donc on pourra te donner des conseils dans tes recherches, mais fais attention : ramène des informations pertinentes, et surtout fais preuve d'esprit critique."

    # Dialogue avec Alexis (Rédacteur)
    alexis "De mon côté, j'ai entendu parler d'une source qui pourrait être intéressante. Enzo répète a qui veut bien l'entendre que les jeux vidéos rendent violents et qu'il a des preuves, tu pourrai peut-être aller lui parler ?"

    alexis "Mais méfie-toi, il faut toujours vérifier la fiabilité des sources. Ne prends pas tout pour argent comptant."

    show character_alexis_sourit at left, taille_normale
    show technicienne at center, zoom_perso
    show c_lola at right

    # Dialogue avec la Technicienne
    alice "De mon côté, je peux t'aider à analyser la vidéo dont parlait le proviseur, je suis spécialiste en images et vidéo comme tu le sais, ça peut-être un intéressant de regarder ça ensemble."

    alice "Les influenceurs et les vidéos virales peuvent facilement manipuler l'opinion publique. Je vais déjà commencer à analyser la vidéo de Paul pour voir si elle a été modifiée."

    show character_alexis_sourit at left, taille_normale
    show technicienne at center, taille_normale
    show c_lola at right, zoom_perso

    # Dialogue avec la technicienne - Lola analyse forum - Quête 3
    l "Quant à moi, je peux essayer de commencer à récolter des témoignages en ligne, je suis plutôt à l'aise avec les outils de communication sur Internet donc on peut voir ensemble ce que je trouve."

    l "Après si je trouve des témoignages, je compte sur toi pour m'aider à trouver les plus fiables et les plus intéressants. Certains témoignages pourraient être biaisés, et on ne peut pas se permettre de publier des informations non vérifiées."

    hide character_alexis_sourit 
    hide technicienne 
    hide c_lola
    with fade

    # Objectifs
    "Votre objectif est de recueillir et croiser les informations fournies par chaque membre du club Journalisme."
    "En tant que Journalistes en herbe, le proviseur compte sur vous pour écrire un article sérieux, donc analysez bien les informations que vous trouverez, car elles seront la base de votre artcile final !"
    "Si les informations que vous collectez ne sont pas fiables, c'est l'article que vous allez rédiger qui manquera aussi de fiabilité, ça serait une catastrophe pour les élèves du collège."

    "Pour pouvoir écrire l'article, vous devrez :"
    "1. Vérifier la fiabilité des sources mentionnées par Alexis."
    "2. Analyser la vidéo de Paul avec l'aide d'Alice pour détecter d'éventuelles manipulations."
    "3. Analyser et récupérer les bons témoignages que Lola aura pu récolter en ligne."

    jump choix_quete


# Scène 2 bis : Choix de la quête (Menu) - Boucle à chaque fois

label choix_quete:
    scene club_journalisme
    with fade
    play music "choix_quete.ogg" fadeout 0.5 fadein 1

    if current_quest:
        if current_quest == "alexis":
            alexis "Tu n’as pas encore fini de récupérer ce que je t’ai demandé. Reviens quand ce sera fait."
        elif current_quest == "technicienne":
            technicienne "Tu dois encore travailler sur l’analyse de la vidéo. On se retrouve une fois que tu as terminé."
        elif current_quest == "respo_interview":
            respo_interview "Tu dois encore interroger quelques témoins. Reviens après."
        jump retour_avant_quete

    "Alors maintenant, quelle piste décidez vous de suivre ?"

    if all(quests.values()):
        "Félicitations, toutes les enquêtes sont terminées !"
        return

    menu:
        "Sélectionnez une des pistes d’enquête présentée par chaque membre du club :"
        "Suivre Alexis - Le Rédacteur" if not quests["alexis"]:
            $ current_quest = "alexis"
            jump quete_1

        "Suivre Alice - La Reponsable Images et Vidéo" if not quests["technicienne"]:
            $ current_quest = "technicienne"
            jump quete_2

        "Suivre Lola - La Responsable informatique et communication" if not quests["respo_interview"]:
            $ current_quest = "respo_interview"
            jump quete_3


#Quête 1 - Témoignages
#Etape 1 discussion avec le rédacteur, Alexis, début de la quête

label quete_1:
    scene b_couloirs
    with fade #permet une transition visuelle progressive
    play music "quete_1.wav" loop fadeout 0.5 fadein 1.0

    show c_alexis_sourit #affiche le personnage avec une expression choisi

    alexis "Parfait, allons-y. Je pense que pour commencer il faudrait que tu ailles chercher des témoignages."

    alexis "Et si tu allais parler à Ethan et Lucas, j'ai entendu dire qu'ils ont des opinions très différents sur les jeux vidéo !"

    alexis "Tu pourras sûrement les trouver dans les couloirs et le hall car ils n'ont pas cours actuellement."


#j'ai rajouté une option pour choisir à qui parler en premier, après peut-être que le joueur pourra s'y rendre lui-même en utilisant la map ?

label choix_destination:
    "C'est parti, est-ce que je commence par le hall ou les couloirs ?"

    menu:
        "Aller aux couloirs" if not a_parle_a_lucas:
            jump scene_couloirs  # emmène le joueur pour parler à Lucas

        "Aller au hall" if not a_parle_a_ethan:
            jump scene_hall  # emmène le joueur pour parler à Ethan

    # Si le joueur a parlé aux deux personnages, passer à la réflexion
    if a_parle_a_lucas and a_parle_a_ethan:
        jump reflexion_apres_discussions
    else:
        jump choix_destination  # Représente le menu si un personnage n'a pas encore été rencontré

#Etape 2, récupération de témoignages oraux

#scène du témoignage de Lucas

label scene_couloirs:

    scene b_couloirs_2

    with fade

    show c_lucas_normal

    lucas "Ce que je pense des jeux vidéo ? Déjà, pas pareil qu'Ethan qui dit n’importe quoi." 

    lucas "Il a lu un article et maintenant il croit qu’il a tout compris." 

    lucas "Franchement, dire que les jeux vidéo rendent violent, c’est juste un truc que les adultes répètent pour nous faire peur."

    show c_lucas_enerve

    lucas "Moi, je joue tout le temps, et j’suis pas devenu une brute, hein !"

    lucas "Il raconte que son pote s’énerve plus qu’avant parce qu’il joue à des jeux de baston… Mais ça veut rien dire !"

    lucas "Peut-être que ce mec a juste des soucis, ou qu’il est fatigué, ou j’sais pas…"

    lucas "Mais c’est pas un jeu qui va le transformer en bagarreur ! Sinon, tous ceux qui jouent à Mario, ils passeraient leur temps à sauter sur les gens, non ?"

    lucas "En plus, moi aussi, j’ai lu un article là-dessus, et il disait que les jeux vidéo, ça aide justement à gérer ses émotions."

    show c_lucas_normal

    lucas "Les chercheurs ont fait des tests, et ils ont vu que ça peut même réduire le stress."

    lucas "Alors peut-être que certains s’énervent plus en jouant, mais d’autres, au contraire, ça les calme !" 

    lucas "Et puis, y’a aussi des études qui prouvent que les jeux vidéo, ça aide à se concentrer, à être plus stratège, et même à mieux travailler en équipe."

    show c_lucas_enerve 

    lucas "Mais Ethan, il veut pas entendre ça, il préfère croire que dès qu’on touche une manette, on devient un monstre."

    menu:    #permet au joeur de choisir entre deux options
        "Si des scientifiques le disent, alors ça doit être vrai.":
            "Tu acceptes l'information sans poser de question."
            $ quete1_score -= 1  # mauvais choix, ne gagne pas de points

        "Est-ce que tu as une source pour ce que tu dis ?":
            lucas "Oui, je l'ai lu dans un article récemment. Attends, voici le lien."
            $ quete1_score += 1  # bon choix, gagne 1 point
            $ add_to_inventory("article_lucas", fiable=True) # ajoute l'article de Lucas à l'inventaire
            "Tu as obtenu l'article de Lucas. Tu pourras aller en vérifier la fiabilité !"
        
    $ a_parle_a_lucas = True # variable avec dollar qu'on peut utiliser au cours du jeu, ici elle sert à vérifier que le joueur a bien parlé avec Lucas (variable originelle avant start du jeu)
   
    if a_parle_a_lucas and a_parle_a_ethan: #variable qui permet que si le joueur a déjà parlé avec ethan et lucas, alors il peut aller au club de journalisme, mais si non il est mené à la conversation qui lui manque
        jump reflexion_apres_discussions
    else:
        jump choix_destination #si le joeur n'a pas encore parlé à l'un des deux personnages, il est renvoyé au choix de destination


# Scène témoignage d'Ethan

label scene_hall:

    scene b_hall

    with fade

    show c_ethan

    ethan "Mon avis sur les jeux vidéo ? Bah moi, j’suis sûr que ça rend violent." 

    ethan "J’ai lu un article là-dessus, et franchement, ça fait flipper. Ils disent que quand tu joues trop à des jeux où tu tapes ou tu tires sur des gens, ben ton cerveau, il s’habitue à la violence. Du coup, après, t’es plus agressif sans t’en rendre compte."

    ethan "Et là, y’a Lucas qui me sort que c’est n’importe quoi, que lui, il joue tout le temps et qu’il est pas violent du tout."

    ethan "Mais j’suis désolé, c’est pas parce que LUI il se contrôle que c’est pareil pour tout le monde !"

    show c_ethan_2

    ethan "Genre, j’connais un pote, il joue que à des jeux où faut se battre, et ben il s’énerve super vite maintenant."

    ethan "Avant, il était grave cool, mais là, il part au quart de tour pour rien."

    ethan "Même les scientifiques l’ont prouvé, y’a des études qui montrent que ça change notre façon de réagir."

    ethan "Mais Lucas, il veut rien entendre ! Il dit que c’est juste un truc que les adultes répètent pour faire peur."

    ethan "Franchement, il abuse. Après, j’dis pas que tous ceux qui jouent deviennent des criminels, hein, mais bon…"

    ethan "À force, ça doit bien avoir un effet. Et puis, si ça rendait pas violent, pourquoi yaurait autant de bagarres à l’école, hein ? J’suis sûr que y’a un lien !"

    menu: #ouvre des choix après le dialogue
        "Si des scientifiques le disent, alors ça doit être vrai.":
            "Tu acceptes l'information sans poser de question."
            $ quete1_score -= 1  # Mauvais choix

        "Est-ce que tu as une source pour ce que tu dis ?":
            show c_ethan
            ethan "Oui, je l'ai lu dans un article récemment. Attends, voici le lien."
            $ quete1_score += 1  # Bon choix
            $ add_to_inventory("article_ethan", fiable=False)# Ajoute l'article d'Ethan à l'inventaire
            "Tu as obtenu l'article d'Ethan. Tu pourras aller en vérifier la fiabilité !"

    $ a_parle_a_ethan = True #valide auprès du jeu que le joueur a parlé à Ethan
    #variable qui ramène le joueur au choix de destination s'il doit encore parler à un personnage
    if a_parle_a_lucas and a_parle_a_ethan:
        jump reflexion_apres_discussions
    else:
        jump choix_destination


#Etape 3 la vérification de l'obtention des sources

#Scène intermédiaire
label reflexion_apres_discussions:
    scene b_couloirs
    with fade

    
    "Maintenant que j'ai parlé à Lucas et Ethan, peut-être devrais-je retourner parler à Alexis?"
    "Il doit m'attendre au club de journalisme."


    jump club_journalisme #le joueur est amené au label suivant



label club_journalisme:
    scene b_club
    with fade

    show c_alexis_sourit

    alexis "Ah, te voilà! Alors, as-tu trouvé des informations intéressantes ?"

    # Vérification des articles dans l'inventaire
    if "article_lucas" in inventory and "article_ethan" in inventory:
        alexis "Super ! Je vois que tu as collecté les deux articles dont nous avions besoin."
        jump scene_lecture_articles

    elif "article_lucas" not in inventory:
        show c_alexis_sourit_pas
        alexis "Hmm, il te manque quelque chose. Il faudrait peut-être retourner voir Lucas dans les couloirs ?"
        $ a_parle_a_lucas = False
        jump scene_couloirs_retour

    elif "article_ethan" not in inventory:
        show c_alexis_sourit_pas
        alexis "Hmm, il te manque quelque chose. Tu devrais peut-être retourner parler à Ethan dans le hall ?"
        $ a_parle_a_ethan = False
        jump scene_hall_retour



#scène vers laquelle le joueur est amené s'il n'a pas obtenu l'article de Lucas
label scene_couloirs_retour:
    scene b_couloirs_2
    show  c_lucas_normal
    
    lucas "Tiens, tu reviens ? Tu veux qu'on reparle des jeux vidéo ?"
    lucas "Franchement, je comprends pas pourquoi certains pensent encore que c'est dangereux..."
    lucas "Mais si tu veux, je peux te renvoyer l'article dont je parlais."

    menu:
        "Oui, je veux bien le lien vers ton article.":
            lucas "Pas de souci. Voilà !"
            $ add_to_inventory("article_lucas") #obtiens l'article de Lucas
            $ a_parle_a_lucas = True #confirme à nouveau que le joueur a parlé à Lucas, il peut à nouveau être renvoyé vers le club et montrer sa source à Alexis
            "Tu as obtenu l'article de Lucas. Tu pourras aller en vérifier la fiabilité !"
            jump retour_au_club

        "Non, c'est bon, je voulais juste repasser.":
            lucas "Okay, comme tu veux !"
            jump retour_au_club

#scène où le joueur est amené s'il n'a pas obtenu l'article d'Ethan
label scene_hall_retour:
    scene b_hall
    show c_ethan
    
    ethan "Ah, tu veux encore parler des jeux vidéo ? Lucas t’a encore embrouillé, c’est ça ?"

    show c_ethan_2

    ethan "Mais je maintiens ce que j’ai dit. Et puis j’avais un article très sérieux, c’est pas moi qui invente !"

    menu:
        "Tu peux me donner le lien de ton article ?":
            ethan "Bien sûr. Tiens, le voilà."
            $ add_to_inventory("article_ethan") #ajoute l'article d'Ethan à l'inventaire
            $ a_parle_a_ethan = True #reconfirme que le joueur a parlé à Ethan
            "Tu as obtenu l'article d'Ethan. Tu pourras aller en vérifier la fiabilité !"
            jump retour_au_club

        "Non merci, je repasserai peut-être plus tard.": #si le joueur choisi cette option, il est amené au club où il sera encouragé à parler encore à Ethan
            ethan "Pas de souci."
            jump retour_au_club

#scène intermédiaire que le joueur obtient quand il a bien demandé leurs sources à Ethan et Lucas
label retour_au_club:
    "Bon, je crois que j'ai ce qu'il faut maintenant. Retournons voir Alexis."
    jump club_journalisme


#Le joueur lit les 2 articles qu'il a récupérés 
label scene_lecture_articles:

    scene b_zoom_ordi_club
    with fade

    show c_alexis_sourit
    alexis "Parfait. Lis-les attentivement, puis dis-moi lequel te semble le plus fiable."

    label lecture_articles_menu: #choix des articles à lire, menu de retour au choix quand le joueur a fini de lire l'un d'entre eux.

        menu:
            "Choisis un article à lire :"
            "Lire l'article de Lucas":
                jump lire_article_lucas
            "Lire l'article d'Ethan":
                jump lire_article_ethan
            "J'ai lu les deux articles":
                jump choix_article_fiable

    return

#lecture de l'article de lucas

label lire_article_lucas:

    scene b_zoom_ordi_club
    show article_lucas_general at truecenter
    with dissolve

    "Voici l'article de Lucas affiché en grand. Clique quand tu as fini de le lire."
    window hide #cache le ruban de dialogue (il cachait une partie de l'article)


    pause #permet de mettre le script sur pause jusqu'à que le joueur clique (ici ça lui laisse le temps de lire)

    hide article_lucas_general
    with fade
    window show

    jump lecture_articles_menu

label lire_article_ethan:

    scene b_zoom_ordi_club
    show article_ecran_general1 at truecenter
    with dissolve

    "Voici la première page de l'article d'Ethan affichée en grand. Il vient du site www.alnas.fr et a été écrit par Antar Belkhefa. Clique pour voir la suite."
    window hide

    pause

    hide article_ecran_general1
    with fade

    show article_ecran_general2 at truecenter
    with dissolve

    "Voici la deuxième page de l'article d'Ethan."

    pause

    hide article_ecran_general2
    with fade

    window show
    jump lecture_articles_menu

#le joueur choisit l'article qui lui paraît le plus pertinent
label choix_article_fiable:

    menu:
        "Quel article est le plus fiable selon toi ?"
        "Celui de Lucas":
            $ choix_article = "lucas" #permet de se souvenir qu'il a choisit l'article de lucas et de le mener au feedback approprié
        "Celui d'Ethan":
            $ choix_article = "ethan" #idem mais pour l'article d'ethan

    if choix_article == "lucas":  #variable qui guide le joueur en fonction de l'article choisi
        jump feedback_lucas
    else:
        jump feedback_ethan



#Dernière étape : feedback d'Alexis
#Partie 1 = analyse de l'article d'Ethan 
label feedback_ethan:

    scene b_zoom_ordi_club

    alexis "Alors, regardons article d'Ethan. Regarde bien le titre :"

    #montre les deux pages à la fois positionnées côte à côte

    show article_ecran_general1 at Position(xalign=0.25, yalign=0.5)
    show article_ecran_general2 at Position(xalign=0.75, yalign=0.5)


    with fade

    alexis "« Santé : 10 raisons pour lesquelles les appareils électroniques devraient être interdits aux enfants ! »"
    alexis "Oula… Ça annonce direct la couleur, non ? On dirait presque une alerte rouge !"

    #cache les deux articles
    hide article_ecran_general1
    
    hide article_ecran_general2

    #montre spécifiquement le titre pour l'analyser de plus près

    show article_ecran_titre at truecenter

    with fade

    alexis "Déjà, ce titre est super alarmiste. Il dit qu’on devrait interdire les écrans aux enfants… mais sans expliquer à partir de quel âge, dans quel contexte, ou même de quels écrans on parle."
    alexis "C’est ce qu’on appelle du *sensationnalisme*. Ça fait peur, ça attire l’œil, mais ce n’est pas très sérieux."

    hide article_ecran_titre

    #montre spécifiquement un paragraphe pour l'analyser de plus près

    show article_ecran_paragraphe at truecenter
    with fade

    alexis "Regarde maintenant ce paragraphe : il parle de plein de dangers des écrans, comme des maladies mentales ou des retards de développement."
    alexis "Mais il ne donne pas de sources précises. Et certaines infos sont exagérées, voire fausses !"
    alexis "Par exemple, il dit qu’un enfant sur trois a un retard de développement en entrant au lycée… mais aucune étude sérieuse ne dit ça."

    hide article_ecran_paragraphe

    #montre spécifiquement le dernier paragraphe pour l'analyser de plus près

    show article_ecran_conclusion at truecenter
    with fade

    alexis "Et le pire, c’est qu’il n’y a aucun contrepoint. Aucune info sur les bons côtés des écrans : apprendre, communiquer, s’amuser…"
    alexis "Un article fiable, lui, aurait donné plusieurs points de vue, des chiffres vérifiables, et des conseils d’experts."

    hide article_ecran_conclusion

    alexis "Alors, est-ce que les écrans sont dangereux ? Pas forcément. Ce qui compte, c’est comment on les utilise."
    alexis "Les spécialistes recommandent de ne pas les interdire, mais de les utiliser intelligemment, avec l’aide des parents."
    alexis "Bref, avant de croire un article comme celui-là, pose-toi toujours des questions. C’est comme ça qu’on devient un lecteur malin !"

    jump feedback_lucas #transporte le joueur à la lecture du prochain article

#Partie 2 = analyse de l'article de Lucas (à améliorer graphiquement aussi)

label feedback_lucas:

    scene b_zoom_ordi_club
 

    alexis "Bon, maintenant regardons l'article de Lucas."
    alexis "C’est une bonne occasion de voir comment on peut bien informer."

    show article_lucas_general at truecenter #truecenter permet de montrer une image au centre parfait de l'écran de jeu
    with dissolve

    alexis "Voici un article qui parle d’un sujet sensible : le lien entre jeux vidéo et violence."
    alexis "Mais tu vas voir, il est bien plus rigoureux et nuancé que le précédent."

    hide article_lucas_general
    with fade

    #titre séparé qui apparaît en plus gros
    show article_lucas_titre at truecenter
    with dissolve #type de transition visuelle

    alexis "Déjà, regarde le titre. Il n’exagère rien, ne fait pas de raccourci, et ne cherche pas à faire peur."
    alexis "C’est un bon point de départ : un article fiable pose les choses calmement."

    hide article_lucas_titre
    with fade
    #paragraphe séparé qui apparaît en plus gros

    show article_lucas_paragraphe1 at truecenter
    with dissolve

    alexis "Ici, on voit que l’article s’appuie sur des études scientifiques sérieuses."
    alexis "Il cite des chercheurs connus, comme Christopher Ferguson ou Karen Sternheimer. C’est important, parce qu’ils travaillent vraiment sur le sujet."

    hide article_lucas_paragraphe1
    with fade
    
    #paragraphe 2 séparé qui apparaît en plus gros

    show article_lucas_paragraphe2 at truecenter
    with dissolve

    alexis "L’article explique aussi que les jeux vidéo ne rendent pas violents. Il nuance, il ne nie pas tout, mais il met les choses en perspective."
    alexis "Il parle de frustration, de stress temporaire… mais il montre que ce n’est pas pareil que de devenir violent."

    hide article_lucas_paragraphe2
    with fade
    
    #conclusion séparée qui apparaît en plus gros

    show article_lucas_conclusion at truecenter
    with dissolve

    alexis "Enfin, il conclut en rappelant que le consensus scientifique est clair : il n’y a pas de lien direct entre jeux vidéo et violence."
    alexis "Et surtout, il parle aussi des autres facteurs : l’environnement, la santé mentale, la famille… bref, il donne du contexte."

    hide article_lucas_conclusion
    with fade

    alexis "Cet article est un bon exemple. Il est calme, nuancé, cite ses sources, et ne cherche pas à manipuler les émotions."
    alexis "C’est ça, un article fiable !"

    jump conclusion_quete1 #amène à la fin de la quête

#Fin de la quête 1
label conclusion_quete1:

    $ score = quete1_score  # enregistre score quête 1
    $ quetes_complete += 1  # informe le jeu qu'une quête a été complétée

    scene b_club
    with fade

    show c_alexis_sourit
    alexis "Bravo, tu as demandé les sources des informations que tu entendais quand c'était nécessaire et à présent tu sais à quels signes de fiabilité faire attention quand tu lis des articles de presse!"
    

    "Quête d'Alexis terminée."
    $ quests["alexis"] = True
    $ current_quest = None
    jump choix_quete




## OCE LOG - QUETE OCE A INTEGRER

#Quête 2 - Analyse vidéo
label quete_2:
    scene b_salle_info
    with fade
    play music "quete_2.wav" loop fadeout 0.5 fadein 1.0

    show c_alice_sourit at left
    alice "On va analyser la vidéo de Paul ensemble."
    alice "Pour rappel, un deepfake, c'est une vidéo créée ou modifiée grâce à l'intelligence artificielle pour faire croire à quelque chose de faux. Il faut donc être très attentif aux détails !"
    alice "Regarde, voici la vidéo qui a circulé partout :"

    $ renpy.movie_cutscene("videos/v_deepfake.webm")

    "Tu observes attentivement la vidéo."

    alice "Tu vas pouvoir utiliser plusieurs outils pour vérifier si la vidéo est authentique ou truquée."

    
    $ indices_video = []
    $ outils_utilises = []

    call quete2_analysis

# Ecran accueil choix menu outils
label quete2_analysis:
    scene b_zoom_ordi_technicien  # Image de fond de l'ordinateur
    with fade

    menu:
        "Choisis un outil d'analyse :"
        
        "Examiner les détails visuels" if "visuel" not in outils_utilises:
            jump quete2_visuel
            
        "Vérifier le compte source" if "compte" not in outils_utilises:
            jump quete2_compte
            
        "Interroger un témoin" if "temoin" not in outils_utilises:
            jump quete2_temoin
            
        "Passer à la synthèse" if len(outils_utilises) >= 2:
            jump quete2_synthese


# Analyse image pure
label quete2_visuel:
    show c_alice_sourit at left
    alice "On commence par l'image. Je zoome sur le visage de Paul."
    show expression "zoom_video" at truecenter with dissolve

    alice "Tu remarques quelque chose de bizarre ?"
    menu:
        "Les ombres ne collent pas et il ne cligne jamais des yeux.":
            alice "Bien vu ! Les deepfakes oublient souvent ces détails."
            $ indices_video.append("Ombres incohérentes et absence de clignement")
            $ quete2_score += 1
            $ outils_utilises.append("visuel")
            hide expression "zoom_video" with dissolve
            call quete2_analysis
            
        "Non, tout a l'air normal.":
            alice "Regarde mieux, fais attention aux mains..."
            
            alice "Les mains bougent de façon étrange, ce qui est peut-être un autre indice de manipulation."
            menu:
                "Oui, les mains sont bizarres aussi.":
                    alice "Exact ! Les deepfakes ont souvent du mal à générer des mains réalistes."
                    $ indices_video.append("Mains étranges (signalé par Alice)")
                    $ outils_utilises.append("visuel")
                    $ quete2_score += 1
                    hide expression "zoom_main" with dissolve
                    call quete2_analysis

                "Non, je trouve les mains normales.":
                    alice "Pourtant, regarde bien : certains doigts sont déformés ou il y a des mouvements impossibles. Les IA ont souvent du mal avec les mains et cree des mains à 6 doigts, c'est un signe de manipulation."
                    $ indices_video.append("Mains suspectes (signalé par Alice)")
                    $ outils_utilises.append("visuel")
                    hide expression "zoom_main" with dissolve
                    call quete2_analysis



# Analyse du superbe beau compte du turfu qui a fait la vidéo 
label quete2_compte:
    show c_alice_sourit at left
    alice "Examinons le compte qui a posté la vidéo."
    
    show fake_account_profile at truecenter with dissolve
    alice "Regarde son profil : le nom, le compte n'est abonné à personne, la photo est issu d'un film, la bio est très étrange et incite à donner de l'argent sur un lien ... Déjà très suspect."
    hide fake_account_profile with dissolve

    show fake_account_videos at truecenter with dissolve
    alice "Ses autres vidéos sont tout aussi étranges :"
    hide fake_account_videos with dissolve

    menu:
        "Examiner la vidéo 'Anniversaire avec les dinosaures'":
            show fake_account_video_1 at truecenter
            "Tu lances la vidéo 'Anniversaire avec les dinosaures'."
            pause 3
            hide fake_account_video_1
            alice "Cette vidéo montre un anniversaire avec des dinosaures, mais en y regardant de plus près, on remarque que le montage est grossier et que les dinosaures n'existent plus... Le titre est typique de l'envie d'attirer l'attention."
            $ indices_video.append("Vidéo 'Anniversaire avec les dinosaures' : montage douteux et contenu trompeur.")

        "Regarder 'Otarie qui jongle OMG'":
            show fake_account_video_2 at truecenter
            "Tu lances la vidéo 'Otarie qui jongle OMG'."
            pause 3
            hide fake_account_video_2
            alice "Cette vidéo montre une otarie qui jongle, mais en y regardant de plus près, on remarque que le montage est grossier (depuis quand les otaries ont de reels bras?). Le titre est typique de l'envie d'attirer l'attention."
            $ indices_video.append("Vidéo 'Otarie qui jongle' : titre exagéré, contenu sans intérêt.")


    
    show legit_account at truecenter with dissolve
    alice "À l'inverse, un compte sérieux a : historique, bio détaillée, publications régulières et variées."
    hide legit_account with dissolve

    menu:
        "Ces incohérences prouvent que le compte est fake":
            alice "Exact ! Aucun compte sérieux n'aurait ce genre de contenu incohérent."
            $ quete2_score += 1
        
        "Peut-être qu'il débute juste...":
            alice "Même un nouveau compte aurait un minimum de cohérence. Là l'objectif est simplement d'avoir le plus d'abonnés."
           

    $ outils_utilises.append("compte")
    jump quete2_continue



# Témoin externe ?
label quete2_temoin:
    show c_alice_sourit at left
    alice "On peut aussi interroger un témoin. J'ai retrouvé un élève qui était présent ce jour-là."
    show el at right
    el "Je l’ai vu passer près des casiers, mais il n’avait pas de pioche et n’a rien cassé."
    
    menu:
        "Merci pour ton témoignage !":
            alice "Ce témoignage va à l'encontre de la vidéo, c'est un indice important."
            $ indices_video.append("Témoin : Paul n’a rien cassé ce jour-là")
            $ quete2_score += 1
            
        "Ce témoignage n'est pas convaincant":
            alice "Vraiment ? Pourtant il contredit directement la vidéo..."
            $ indices_video.append("Témoignage douteux (signalé par Alice)")

    $ outils_utilises.append("temoin")
    call quete2_analysis


label quete2_continue:
    if len(outils_utilises) < 3:  # Si moins de 2 outils utilisés
        call quete2_analysis  # Retour à l'écran dde base
    else:
        jump quete2_synthese  # Passe à la conclusion

# Bilan de la quête tmtc
label quete2_synthese:
    scene b_salle_info with fade
    show c_alice_sourit at left
    
    # Calcul du score sur 4
    
    alice "Tu as terminé l’analyse. Voici les indices que tu as collectés :"
    "[', '.join(indices_video)]"
    
    
    alice "Avec tous ces éléments, quelle est ta conclusion ?"
    
    menu:
        "La vidéo est authentique":
           
            alice "Tu ignores tous les indices que nous avons pourtant trouvés ensemble..."
            $ quests["technicienne"] = True
            $ current_quest = None
            $ add_to_inventory("fiche_conclusion_video", fiable=True)
            jump choix_quete

        "La vidéo est un deepfake":
            $ quete2_score += 1
            alice "Bravo ! Ta conclusion s'appuie sur une analyse solide."
            $ quests["technicienne"] = True
            $ current_quest = None
            $ add_to_inventory("fiche_conclusion_video", fiable=False)
            jump choix_quete

        "Manque de preuves":
            alice "La prudence est une qualité, mais il faut parfois trancher."
            $ quests["technicienne"] = True
            $ current_quest = None
            $ add_to_inventory("fiche_conclusion_video", fiable=False)
            jump choix_quete




## OCE LOG - A PARTIR DE LA TOUT EST BON 
# Quête 3 - point d'entrée
label quete_3:
    play music "quete_3.wav" loop fadeout 0.5 fadein 1.0
    scene club_journalisme with fade
    $ quests["respo_interview"] = True
    $ current_quest = None
    show c_lola with dissolve 

    l "Salut ! Du coup, pour récolter des témoignages pour qu'on puisse écrire notre article j’ai mis un message sur le Forum de l’ENT du collège pour voir si des élèves et des profs avaient envie de témoigner et de nous donner des informations."
    l "Je ne m’attendais pas à ça, mais le forum déborde. J’ai fait un premier tri mais là {b}j’ai vraiment besoin de toi pour trier les derniers messages.{/b}"
    l "Le problème c’est que certains témoignages ont l’air un peu bizarres. Je pense qu’il y en a quelques-uns qui ne sont pas fiables et que mon cerveau me joue des tours."
    l "Tu sais en classe on nous a parlé des {b}biais cognitifs{/b} et que ça pouvait nous empêcher d’y voir clair face à des informations ou des témoignages, mais viens on va regarder tout ça sur mon ordinateur."

    jump ordinateur_lola

# Scène 2 - Explication des biais
label ordinateur_lola:  
    scene ordi_forum with dissolve
    show c_lola at left
    with dissolve

    l "Pour t'aider, voici ce que j’ai noté en cours sur trois biais cognitifs courants dans la diffusion de fausses informations :"
    l "{b}Corrélation illusoire :{/b} c'est quand on voit un lien qui n'existe pas réélement, entre deux événements."
    l "{b}Autorité :{/b} croire qu'une information est vraie simplement parce qu'elle provient d'une figure réputée, sans vérifier les faits."
    l "{b}Confirmation (cherry picking):{/b} ce biais nous pousse à ne retenir que les infos qui confirment nos croyances et à ignorer celles qui pourraient les contredire."
    l "J'ai ajouté une fiche récap sur les  biais cognitifs à ton inventaire si jamais tu as besoin de te rappeler de chaque définition pendant qu'on analysera les témoignages !"
    $ add_to_inventory("fiche_biais")

    l "Donc là il faut vraiment que tu check chaque témoignage du forum. Pour chaque message, tu as deux options : Le Récupérer si tu sens qu’il est fiable ou l’Analyser si tu sens qu’il l’est pas. Et si en plus tu trouves quel biais entre en jeu, alors t’es un boss."
    l "Après si t’analyses un témoignage qui au final est fiable c’est pas grave hein, vaut mieux être trop prudent que pas assez, tu pourras toujours le récupérer. Mais si tu dis qu’il est biaisé alors que non, c’est dommage on le mettra de côté pour rien, et là c'est l'article qu'on va écrire qui sera bancal."
    l "Si t’as tout compris et que t’es Prêt(e), allons voir le forum !"

    jump témoignage_1

label témoignage_1:
    scene forum with fade
    show temoi1 at Position(ypos=1200)
    with dissolve
   

    # Texte du témoignage
    "Voici le premier témoignage, qu'en penses-tu ?"

    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            $ pause_music_with_fade()
            play sound "faux.mp3" loop fadein 0.2
            scene forum with dissolve
            show c_lola_p at left 
            with dissolve
            l "Hmm... Ok, moi je trouve que le lien qu'il fait est bizarre..."  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
            $ quete3_score -= 1  # Score = -1
            $ témoignages_récupérés.append("Témoignage 1 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
            jump témoignage_2  # Saute vers le témoignage suivant

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            scene forum with dissolve 
            with dissolve
            jump analyse_biais_1  # Saute vers l'analyse du témoignage

    return

# Analyse du premier témoignage
label analyse_biais_1:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            scene forum with dissolve
            show c_lola_p at left 
            l "Je crois que c'est plutôt un biais de corrélation illusoire. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump témoignage_2
        "Confirmation":
            scene forum with dissolve
            show c_lola_p at left 
            l "Je crois que c'est plutôt un biais de corrélation illusoire. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump témoignage_2
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            scene forum with dissolve
            show c_lola at left
            l "Trop fort ! T'as identifié le biais de corrélation illusoire. Le témoignage n'était pas fiable."  # Lola félicite le joueur
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1  # Augmente le score du joueur de 1
            jump témoignage_2  # Saute vers le témoignage suivant
        "fiable":
            $ pause_music_with_fade()
            play sound "faux.mp3" loop fadein 0.2
            scene forum with dissolve
            show c_lola_p at left 
            l "Hmm... Ok, moi je trouve que le lien qu'il fait est bizarre..."  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
    $ quete3_score -= 1  # Score = -1
    $ témoignages_récupérés.append("Témoignage 1 (Biaisé)") 
    $ add_to_inventory("temoignage1", fiable=False) # Ajoute le témoignage à la liste des témoignages récupérés
    jump témoignage_2  # Saute vers le témoignage suivant

label témoignage_2:
    scene forum with fade
    show temoi2 at Position(ypos=1200)
    with dissolve

    # Texte du témoignage
    "Voici le second témoignage, qu'en penses-tu ?"

    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            $ pause_music_with_fade()
            play sound "faux.mp3" loop fadein 0.2
            scene forum with dissolve
            show c_lola_p at left
            l "Hmm… Ok, moi je trouve qu’il fait confiance un peu vite à ce Youtubeur, en plus il dit même pas qui c’est … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
            $ quete3_score -= 1  # Score = -1
            $ témoignages_récupérés.append("Témoignage 2 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
            $ add_to_inventory("temoignage2", fiable=False)

            jump témoignage_3  # Saute vers le témoignage suivant

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            scene forum with dissolve 
            jump analyse_biais_2  # Saute vers l'analyse du témoignage

    return

# Analyse du deuxième témoignage
label analyse_biais_2:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            scene forum with dissolve
            show c_lola at left 
            l "T’es le boss ! T’as identifié le biais d’autorité. Le témoignage n'était pas fiable."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump témoignage_3
        "Confirmation":
            scene forum with dissolve
            show c_lola_p at left
            l "Je crois que c’est plutôt un biais d’autorité. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump témoignage_3
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            scene forum with dissolve
            show c_lola_p at left
            l "Je crois que c’est plutôt un biais d’autorité. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Lola félicite le joueur
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score += 1  # Augmente le score du joueur de 1
            jump témoignage_3  # Saute vers le témoignage suivant
        "fiable":
            scene forum with dissolve
            show c_lola_p at left
            $ pause_music_with_fade()
            play sound "faux.mp3" loop fadein 0.2
            l "Hmm… Ok, moi je trouve qu’il fait confiance un peu vite à ce Youtubeur, en plus il dit même pas qui c’est … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
    $ quete3_score -= 1  # Score = -1
    $ témoignages_récupérés.append("Témoignage 2 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
    $ add_to_inventory("temoignage3", fiable=True)
    jump témoignage_3  # Saute vers le témoignage suivant

label témoignage_3:
    scene forum with fade
    show temoi3 at Position(ypos=1200)
    with dissolve

    # Texte du témoignage
    "Voici le troisième témoignage, qu'en penses-tu ?"

    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            $ pause_music_with_fade()
            play sound "bien_joue.mp3" loop fadein 0.2
            scene forum with dissolve
            show c_lola at left  
            l "Parfait ! Ce témoignage est fiable et précieux pour notre article. En plus il a même mis le lien vers l'enquête, c'est top !" # Feedback bonne réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
            $ quete3_score += 1
            $ témoignages_récupérés.append("Témoignage 3 (Fiable)")
            $ add_to_inventory("temoignage4", fiable=False)
            jump témoignage_4

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            scene forum with dissolve
            jump analyse_biais_3  # Saute vers l'analyse du témoignage

    return

# Analyse du troisième témoignage
label analyse_biais_3:
    play music "quete_3.wav" loop fadeout 0.5 fadein 1.0
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
        
            scene forum with dissolve
            show c_lola_p at left
            l "T’es sûr ? Pourtant il parle de journaliste indépendant, met sa source et tout, j’ai vraiment cru que c’était fiable. Mais bon c’est toi le spécialiste hein !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            jump témoignage_4
        "Confirmation":
            scene forum with dissolve
            show c_lola_p at left
            l "T’es sûr ? Pourtant il parle de journaliste indépendant, met sa source et tout, j’ai vraiment cru que c’était fiable. Mais bon c’est toi le spécialiste hein !"  # Feedback mauvaise réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            $ quete3_score -= 1  # Score = -1
            jump témoignage_4
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            scene forum with dissolve
            show c_lola_p at left
            l "T’es sûr ? Pourtant il parle de journaliste indépendant, met sa source et tout, j’ai vraiment cru que c’était fiable. Mais bon c’est toi le spécialiste hein !"  # Feedback mauvaise réponse
            $ quete3_score -= 1  # Score = -1  # Augmente le score du joueur de 1
            jump témoignage_4  # Saute vers le témoignage suivant
        "fiable":
            scene forum with dissolve
            show c_lola at left  
            $ pause_music_with_fade()
            play sound "bien_joue.mp3" loop fadein 0.2
            l "Parfait ! Ce témoignage est fiable et précieux pour notre article. En plus il a même mis le lien vers l'enquête, c'est top !" # Feedback bonne réponse
            l "Allez, témoignage suivant !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
            $ quete3_score += 1
    $ témoignages_récupérés.append("Témoignage 2 (Fiable)")  # Ajoute le témoignage à la liste des témoignages récupérés
    jump témoignage_4  # Saute vers le témoignage suivant

label témoignage_4:
    scene forum with fade
    show temoi4 at Position(ypos=1200)
    with dissolve

    # Texte du témoignage
    "Voici le quatrième témoignage, qu'en penses-tu ?"
    menu:  # Crée un menu avec les options de choix pour le joueur
        "Récupérer ce témoignage":  # Option pour récupérer le témoignage
            $ pause_music_with_fade()
            play sound "faux.mp3" loop fadein 0.2
            scene forum with dissolve
            show c_lola_p at left
            l "Ah ouais … Ok. Moi je trouve pas que ce qu’il dit soit basé sur des infos vraiment fondées son témoignage, puis bon il cite même pas les articles, et alors TikTok moi j’suis pas sûre de valider … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
            $ quete3_score -= 1  # Score = -1
            $ témoignages_récupérés.append("Témoignage 2 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
            jump conclusion_quete3  # Saute vers le témoignage suivant

        "Analyser ce témoignage":  # Option pour analyser le témoignage
            scene forum with dissolve
            jump analyse_biais_4  # Saute vers l'analyse du témoignage

    return

# Analyse du premier témoignage
label analyse_biais_4:
    menu:  # Crée un menu avec des options pour le joueur
        "Quel biais cognitif identifiez-vous ?"  # Question posée au joueur
        "Autorité":  # Option pour choisir le biais d'autorité
            scene forum with dissolve
            show c_lola_p at left
            l "Je crois que c’est plutôt un biais de confirmation. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump conclusion_quete3
        "Confirmation":
            scene forum with dissolve
            show c_lola at left 
            l "T’es le boss ! T’as identifié le biais de confirmation. Le témoignage n'était pas fiable." # Feedback bonne réponse
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score += 1
            jump conclusion_quete3
        "Corrélation illusoire":  # Option pour choisir le biais de corrélation illusoire
            scene forum with dissolve
            show c_lola_p at left
            l "Je crois que c’est plutôt un biais de confirmation. Mais déjà bravo d’avoir capté que le témoignage était biaisé."  # Feedback mauvais biais
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            $ quete3_score += 1  # Augmente le score du joueur de 1
            jump conclusion_quete3  # Saute vers le témoignage suivant
        "fiable":
            scene forum with dissolve
            show c_lola_p at left
            $ pause_music_with_fade()
            play sound "faux.mp3" loop fadein 0.2
            l "Ah ouais … Ok. Moi je trouve pas que ce qu’il dit soit basé sur des infos vraiment fondées son témoignage, puis bon il cite même pas les articles, et alors TikTok moi j’suis pas sûre de valider … mais bon c’est toi le spécialiste !"  # Feedback mauvaise réponse
            l "C'était le dernier, merci pour ton aide !" # Transition vers le prochain témoignage
            stop sound fadeout 0.5
            $ resume_music_with_fade()
    $ quete3_score -= 1  # Score = -1
    $ témoignages_récupérés.append("Témoignage 4 (Biaisé)")  # Ajoute le témoignage à la liste des témoignages récupérés
    jump conclusion_quete3  # Saute vers le témoignage suivant

label conclusion_quete3:
    scene ordi_forum with dissolve
    

    $ score = quete3_score  # Enregistre le score de la quête 3
    $ quetes_complete += 1  # Incrémente le nombre de quêtes complétées

    if quete3_score >= 3:
        show c_lola at center
        with dissolve
        l "Bravo, grâce à toi on a des témoignages vraiment fiables pour l’article, je pense que ca va vraiment avoir un impact positifs sur tout le collège..."
    elif quete3_score >= 2:
        show c_lola at center
        with dissolve
        l "Je pense que tu as peut-être fait quelques erreurs, mais l'important est que tu as su repérer des messages douteux... Ca nous évitera de raconter n'importequoi dans notre article"
    else:
        show c_lola_p at center
        with dissolve
        l "Avec un peu de recul, je ne suis pas trop sûre de tes choix... J'ai peur de ce qu'on va raconter dans l'article, mais je te fais confiance c'est toi le spécialiste."


    $ quests["respo_interview"] = True
    $ current_quest = None
    jump choix_quete


#AJout derniere scene oce

label scene6_feedback:
    scene bg_club_journalisme
    with fade

    show alexis neutre at left
    show alice neutre at center
    show lola neutre at right

    "Vous regroupez toutes les preuves collectées autour de la table du club."

    # Feedback Alexis (Quête 1)
    if quete1_score >= 2:
        alexis ""
        alexis ""
    else:
        alexis ""
        alexis ""

    # Feedback Alice (Quête 2)
    if quete2_score >= 2:
        alice "Analyse vidéo terminée : ombres incohérentes, absence de clignements et artefacts de deepfake confirmés."
        alice "Preuves techniques solides pour démontrer la manipulation."
    else:
        alice "L'analyse reste incomplète... Difficile d'être catégorique sur l'authenticité de la vidéo."

    # Feedback Lola (Quête 3)
    if quete3_score >= 2:
        lola ""
    else:
        lola ""

    jump scene6_article

label scene6_article:
    scene bg_club_table
    with dissolve

    show alexis serieux at center

    alexis "Maintenant, sélectionne les éléments les plus pertinents pour l'article final :"
    
    # Vérification inventaire minimum
    if len(inventaire) < 3:
        alexis "Attends... Tu as loupe des éléments crutiaux, la prochaine fois tu devras faire plus gaffe aux  !"
        $ article_incomplet = True
        jump scene7_evaluation


    # Screen de sélection des éléments
    call screen selection_article(inventaire)

    # Calcul score final
    $ score_quetes = ( (quete1_score + quete2_score + quete3_score) / 10 ) * 100  # 12 = 3 quêtes × 4 pts max
    $ score_items = sum(1 for item in selected_items if item["fiable"]) / len(selected_items)
    $ score_final = (score_quetes + score_items) / 2

    if score_final < 0.5:
        alexis "L'article manque de preuves tangibles... Le proviseur risque d'être sceptique."
    else:
        alexis "Avec ces éléments, notre enquête tiendra la route !"

    jump scene7_evaluation

screen selection_article(items):

    frame:
        xalign 0.5
        yalign 0.1
        vbox:
            text "Éléments disponibles :" bold True
            for item in items:
                textbutton item["nom"]:
                    action Function(toggle_selection, item), SetVariable("score_items", update_score())
                    tooltip item["description"]

    frame:
        xalign 0.5
        yalign 0.9
        vbox:
            text "Sélection actuelle :"
            for item in selected_items:
                text item["nom"] + (" (fiable)" if item.get("fiable", False) else " (douteux)")
            
            text "Crédibilité : [score_items]"
            
            if len(selected_items) >= 5:
                textbutton "Valider la sélection" action Return()
            else:
                text "Minimum 5 éléments requis" color "#ff0000"



label scene7_evaluation:
    scene bg_proviseur
    show c_proviseur at center
    with fade

    # Calcul du score des items
    $ nb_fiables = sum(1 for item in selected_items if item["fiable"])
    $ total_items = len(selected_items)
    $ score_items = (nb_fiables / total_items * 100) if total_items > 0 else 0
    
    # Calcul du score final
    $ score_quetes = (quete1_score + quete2_score + quete3_score) * 10
    $ score_final = (score_quetes + score_items) / 2

    
    "[DEBUG] Score quêtes : [quete1_score]/4 [quete2_score]/4 [quete3_score]/4"
    "[DEBUG] Items fiables : [nombre_preuves_fiables]/[total_preuves]"

 
    # Affichage du rapport d'enquête
    call screen score_report(score_final)

    proviseur "Voyons voir... Vous avez recoupé les témoignages, analysé la vidéo, vérifié les sources..."
    proviseur "Je vais maintenant évaluer la fiabilité de votre article."

    # Évaluation finale
    if score_final < 50:
        show proviseur severe
        proviseur "Hélas, votre article manque de preuves solides. Les élèves et les parents restent dans le doute."
        proviseur "La désinformation continue de se propager. Il faudra redoubler d'efforts la prochaine fois."
        play sound "sfx/failure.wav"
        show red_cross at truecenter with dissolve

    elif 50 <= score_final < 70:
        show proviseur neutre
        proviseur "Votre article a permis de calmer le jeu. Ce n'est pas parfait, mais vous avez su apporter des éléments de réponse."
        proviseur "Vous avez rétabli la vérité sur plusieurs points essentiels."
        play sound "sfx/neutral.wav"
        show yellow_check at truecenter with dissolve

    else:
        show proviseur souriant
        proviseur "Félicitations ! Votre enquête est exemplaire. Grâce à vous, le collège retrouve son calme."
        proviseur "Tout le monde a pu apprendre à mieux décrypter les informations. Vous avez sauvé le collège !"
        play sound "sfx/success.wav"
        show green_check at truecenter with dissolve

    # Option de rejeu
    menu:
        "Recommencer l'aventure ?":
            jump start_game
        "Quitter":
            jump credits

label credits:
    scene bg_club_journalisme
    with fade

    show c_alexis at left
    show c_alice at center
    show c_lola at right

    alexis "Merci d'avoir joué !"
    alice "On espère que vous avez appris plein de choses sur la désinformation."
    lola "Et que vous serez plus vigilant face aux fake news !"
    
screen score_report(score):
    frame:
        xalign 0.5
        yalign 0.2
        vbox:
            label "Rapport de fiabilité" xalign 0.5
            null height 20
            
            hbox:
                vbox:
                    text "Score des quêtes: [score_quetes]%"
                    text "Preuves sélectionnées: [score_items]%"
                    null height 10
                    text "Score final: [score_final]%" bold True
                
                add "ui/progress_bar.png" at progress_animation(score/100.0)

            key "dismiss" action Return()

transform progress_animation(value):
    subpixel True
    xysize (300, 30)
    crop (0, 0, 0, 0)
    easein 1.5 crop (0, 0, value, 1.0)
