from math import gamma
from pickle import TRUE
#from numpy import _FlatIterSelf
import pygame 
import megegyprojekt 
from megegyprojekt import Racs
import time


def jatek() -> bool:
    window= pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Prog1 projekt, Berenyi Flora')

    #ezek a saját háziállataim, a magam szórakoztatására használom őket a játékban
    nyuszi= pygame.image.load('nyuszi.png')
    bolha= pygame.image.load('bolha.png')
    csacsi= pygame.image.load('csacsi.png')
    kalitka= Racs(pygame, bolha, nyuszi)

    elorunning= True
    running= False


    letter= "X"
    egyik_jatekos=bolha
    masik_jatekos= nyuszi
    nyer=nyuszi

    pygame.font.init()
    #elofutashoz kiiratando szovegek
    font= pygame.font.SysFont("", 40)
    font2= pygame.font.SysFont("", 30)
    font3= pygame.font.SysFont("", 30)
    bolha_str= pygame.font.SysFont("", 33)
    nyuszi_str= pygame.font.SysFont("", 33)

    udvozlet= font.render("Üdvözlet!", False, (255, 255, 255))
    ezegy= font2.render("Ez egy tic-tac toe játék.", False, (255, 255, 255))
    valaszd= font3.render("Válaszd ki a spirituális állatod! (Kattints a képre!)", False, (255, 255, 255))
    bolha_szoveg= bolha_str.render("Bolha", False, (255,255,255))
    nyuszi_szoveg= nyuszi_str.render("Nyuszi", False, (255,255,255))

    #veg_kepernyohoz kiiratando szöveg
    nyertel_str=pygame.font.SysFont("", 33)


    dontetlen_kep= pygame.image.load('dontetlen.png')

    nyertel= nyertel_str.render("Nyertél!", False, (255,255,255))
    ujrakep= pygame.image.load('ujra.png')
    kilepeskep= pygame.image.load('kilepes.png')

    def valasztas():
        elorunning=True
        while elorunning==True:
            egyik_jatekos=bolha
            masik_jatekos= nyuszi
            running=False

            window.fill((0,0,0))
            window.blit(udvozlet, (0,0))
            window.blit(ezegy, (0,50))
            window.blit(valaszd, (0,80))
            window.blit(bolha, (0,200))
            window.blit(nyuszi, (0, 400))
            window.blit(bolha_szoveg, (200,200))
            window.blit(nyuszi_szoveg, (200, 400))
            pygame.display.flip()
            for event in pygame.event.get():#ez a struktúra használata átvétel
                    #kilépési módok(space vagy a piros x-re kattintasz az ablak jobb felső sarkában)
                    if event.type== pygame.QUIT:
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            
                            mouse_pos= pygame.mouse.get_pos()
                            
                            x= mouse_pos[0] //200
                            y= mouse_pos[1] //200
                            print(x,y)
                            if x==0 and y ==1:
                                print("Bolha")
                                egyik_jatekos= kalitka.bolha
                                masik_jatekos=kalitka.nyuszi
                                elorunning=False

                            elif x == 0 and y==2:
                                print("Nyuszi")
                                egyik_jatekos= kalitka.nyuszi
                                masik_jatekos= kalitka.bolha
                                elorunning=False
        return egyik_jatekos, masik_jatekos

    egyik_jatekos, masik_jatekos = valasztas()
    print(egyik_jatekos)
    window.fill((0,0,0))
    pygame.display.flip()
    running=True    

    kalitka=Racs(pygame, egyik_jatekos, masik_jatekos)
    lepesek=0
    dontetlen=False
    while running:
            nyer=egyik_jatekos
            window.fill((0,0,0))

            kalitka.draw(window)
            pygame.display.flip()
            for event in pygame.event.get():
                #kilépési módok(space vagy a piros x-re kattintasz az ablak jobb felső sarkában)
                if event.type== pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        mouse_pos= pygame.mouse.get_pos()
                        x= mouse_pos[0] //200
                        y= mouse_pos[1] //200
                        pozi= (x, y)
                        kalitka.mouse_click(x, y, letter)
                        if kalitka.switch_letter:
                            eppen_betu= letter
                            lepesek+=1
                            kalitka.draw(window)
                            pygame.display.flip()
                            if kalitka.win(letter):
                                if letter== "X":
                                    nyer=egyik_jatekos
                                else:
                                    nyer= masik_jatekos
                                time.sleep(1)
                                running=False
                                break
                                
                            else:
                                if letter== "X":
                                    letter= "O"
                                
                                else:
                                    letter= "X"

                            if lepesek==9:
                                time.sleep(1)
                                dontetlen=True
                                running=False
                

    vege=True                    
                
    #veg_kepernyo


        
    while vege:
        if dontetlen:
            window.fill((0,0,0))
            window.blit(dontetlen_kep,(200, 150))
            window.blit(ujrakep, (0,400))
            window.blit(kilepeskep, (400,400))
            pygame.display.flip()
            for event in pygame.event.get():
                        #kilépési módok(space vagy a piros x-re kattintasz az ablak jobb felső sarkában)
                        if event.type== pygame.QUIT:
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:
                                
                                mouse_pos= pygame.mouse.get_pos()
                                
                                x= mouse_pos[0] //200
                                y= mouse_pos[1] //200
                                if x==0 and y ==2:
                                    print('Zárd be és indíts újra kérlek!')
                                    return True

                                elif x == 2 and y==2:
                                    quit()
        else:

            window.fill((0,0,0))
            window.blit(nyer, (200,150))  
            window.blit(nyertel, (200, 360)) 
            window.blit(ujrakep, (0,400))
            window.blit(kilepeskep, (400,400))
            pygame.display.flip()

            for event in pygame.event.get():
                        #kilépési módok(space vagy a piros x-re kattintasz az ablak jobb felső sarkában)
                        if event.type== pygame.QUIT:
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:
                                
                                mouse_pos= pygame.mouse.get_pos()
                                
                                x= mouse_pos[0] //200
                                y= mouse_pos[1] //200
                                if x==0 and y ==2:
                                    print('Zárd be és indíts újra kérlek!')
                                    return True

                                elif x == 2 and y==2:
                                    quit()
                                
if __name__ == "__main__":
    while jatek():
        pass



 