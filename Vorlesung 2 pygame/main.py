#########################################################################
# Import:     Alle Abhängigkeiten werden am Anfang eingebunden
#########################################################################

import pygame   # die Spiele-Engine
import random   # Zufallszahlen brauchen wir immer...
import os       # Das Dateisystem
from settings import *
from sprites import *

#########################################################################
# Initialisierung:    pygame wird gestartet
#                     und eine Bildschirm-Ausgabe wird generiert
#########################################################################

pygame.init()           # pygame Initialisierung
pygame.mixer.init()     # Die Sound-Ausgabe wird initialisiert
pygame.display.set_caption("My Game")   # Überschrift des Fensters

#########################################################################
# Das Clock-Objekt:    Damit lassen sich Frames und Zeiten messen
#                      Sehr wichtig für Animationen etc.
#########################################################################

clock = pygame.time.Clock()

#########################################################################
# Das screen-Objekt:    Auf dem screen werden alle Grafiken gerendert
# Cooles Feature: pygame.SCALED(verdoppelte Auflösung für einen Retro-Effekt)
#########################################################################

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)

#########################################################################
# Grafiken:    Das Einbinden von Grafiken kann auch ausgelagert werden
#########################################################################

# Das Dateisystem ermittelt das aktuelle Verzeichnis
game_folder = os.path.dirname(__file__)

# Wir binden eine Grafik (Ball) ein
# convert_alpha lässt eine PNG-Datei transparent erscheinen
image_dict = {}

for nr in range(1, 9):
    image_dict["coin"+str(nr)] = pygame.image.load(os.path.join(
        game_folder, '_images/coin'+str(nr)+'.png')).convert_alpha()

image_dict["ball"] = pygame.image.load(os.path.join(
    game_folder, '_images/ball.png')).convert_alpha()
sprites = []

# Sprite Factory
for _ in range(10):
    sprites.append(Ball(random.randint(64, WIDTH - 64),
                        random.randint(64, HEIGHT - 64),
                        random.choice([-3, -2, -1, 1, 2, 3]),
                        random.choice([-3, -2, -1, 1, 2, 3]), image_dict))

for _ in range(10):
    sprites.append(Coin(random.randint(64, WIDTH - 64),
                        random.randint(64, HEIGHT - 64),
                        random.choice([-3, -2, -1, 1, 2, 3]),
                        random.choice([-3, -2, -1, 1, 2, 3]), image_dict))

running = True

#########################################################################
# Game Loop:  Hier ist das Herzstück des Templates
# Im Game Loop laufen immer 5 Phasen ab:
# 1. Wait: Die Zeit zwischen 2 Frames wird mit Wartezeit gefüllt
# 2. Input: Alle (Input-)Events werden verarbeitet (Maus, Tastatur, etc.)
# 3. Update: Alle Sprites werden aktualisert inkl. Spiellogik
# 4. Render: Alle Sprites werden auf den Bildschirm gezeichnet
# 5. Double Buffering: Der Screen wird geswitcht und angezeigt
#########################################################################

while running:
    #########################################################################
    # 1. Wait-Phase:
    # Die pygame-interne Funktion clock.tick(FPS) berechnet die
    # tatsächliche Zeit zwischen zwei Frames und limitiert diese
    # auf einen Wert(z. B. 1/60). Diese tatsächliche verbrauchte
    # Zeit wird dann bei der Aktualisierung des Spiels benötigt,
    # um dieGeschwindigkeit der Objekte anzupassen.

    dt = clock.tick(FPS) / 1000

    #########################################################################
    # 2. Input-Phase:
    # Mit pygame.event.get() leeren wir den Event-Speicher.
    # Das ist wichtig, sonst läuft dieser voll und das Spiel stürzt ab.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Windows Close Button?
            running = False             # dann raus aus dem Game Loop

    #########################################################################
    # 3. Update-Phase: Hier ist die komplette Game Logik untergebracht.

    for sprite in sprites:
        sprite.update()

    #########################################################################
    # 4. Render-Phase: Zeichne alles auf den Bildschirm

    # Hintergrund
    screen.fill((255, 255, 255))    # RGB Weiß

    # Zeichne Objekte an Position auf den Screen
    for sprite in sprites:
        screen.blit(sprite.image, sprite.imageRect)

    #########################################################################
    # 5. Double Buffering

    pygame.display.flip()

###########################
# Spiel verlassen: quit

pygame.quit()
