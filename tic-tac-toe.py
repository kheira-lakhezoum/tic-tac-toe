import pygame
import sys

pygame.init()

pygame.display.set_caption('CuPython')

largeur, hauteur = 600, 600
ecran = pygame.display.set_mode((largeur, hauteur))
blanc = (255, 255, 255)
noir = (0, 0, 0)
red = (255, 51, 221)

taille_box = 200
nombre_lignes = 3
nombre_colonnes = 3

grille = [['', '', ''],
          ['', '', ''],
          ['', '', '']]

coeur = pygame.image.load("coeur.png")
coeur = pygame.transform.scale(coeur, (100,100))
fleche = pygame.image.load("fleche.png")
fleche = pygame.transform.scale(fleche, (100,100))


def draw_grille():
    ecran.fill(noir)
    for ligne in range(1, nombre_lignes):
        pygame.draw.line(ecran, blanc, (0, ligne * taille_box), (largeur, ligne * taille_box), 3)
    for colonne in range(1, nombre_colonnes):
        pygame.draw.line(ecran, blanc, (taille_box * colonne, 0), (taille_box * colonne, hauteur), 3)


def draw_symbole(symbole, ligne, colonne):
    for ligne in range(3):
        for colonne in range(3):
            symbole = grille[ligne][colonne]
            if symbole == 'coeur':
                x = colonne * taille_box + taille_box // 2 - coeur.get_width() // 2
                y = ligne * taille_box + taille_box // 2 - coeur.get_height() // 2
                ecran.blit(coeur, (x, y))

            elif symbole == 'fleche':
                x = colonne * taille_box + taille_box // 2 - fleche.get_width() // 2
                y = ligne * taille_box + taille_box // 2 - fleche.get_height() // 2
                ecran.blit(fleche, (x, y))


def victoire():
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != '':
            return grille[i][0]  # Ligne gagnante
        
        if grille[0][i] == grille[1][i] == grille[2][i] != '':
            return grille[0][i]  # Colonne gagnante

        if grille[0][0] == grille[1][1] == grille[2][2] != '':
            return grille[0][0]  # Diagonale gagnante
        
        if grille[0][2] == grille[1][1] == grille[2][0] != '':
            return grille[0][2]  # Diagonale gagnante

    return None


def afficher_message(message):
    font = pygame.font.Font(None, 70)
    text = font.render(message, True, red)
    ecran.blit(text, (largeur // 2 - text.get_width() // 2, hauteur // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(4000)


def win():
    gagnant = victoire()
    if gagnant or all(all(cell != '' for cell in row) for row in grille):
        afficher_message(f"Le joueur {gagnant} a gagné!" if gagnant else "Aucun gagnant !")
        pygame.quit()
        sys.exit()


def play():
    tour = 'coeur' 

    run = True
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                colonne, ligne = event.pos[0] // taille_box, event.pos[1] // taille_box
                if grille[ligne][colonne] == '':
                    grille[ligne][colonne] = tour
                tour = 'coeur' if tour == 'fleche' else 'fleche' 

            draw_grille()
            draw_symbole(coeur, 0, 0)
            draw_symbole(fleche, 2, 1)
            win()

        pygame.display.flip()
        pygame.time.delay(100)

play()

