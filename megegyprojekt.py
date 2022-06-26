from numpy import diag


class Racs:

    def __init__(self, pygame, egyik_jatekos, masik_jatekos):
        self.racs= [[0 for x in range(3)] for y in range(3)]
        print(self.racs)

        self.racsvonalak= [((0,200),(600,200)), 
                            ((0, 400), (600,400)), 
                            ((200,0), (200,600)),
                            ((400,0), (400,600))]
        self.pygame= pygame

        self.bolha= egyik_jatekos
        self.nyuszi= masik_jatekos
        #self.csacsi= pygame.image.load("csacsi.png")
    

        self.switch_letter= True

    def draw(self, win):
        for line in self.racsvonalak:
            self.pygame.draw.line(win, (255,255,255), line[0], line[1], 2)
        
        for y in range(len(self.racs)):
            for x in range(len(self.racs[y])):
                if self.get_cell(x, y)== "X":
                    win.blit(self.bolha, (x*200,y*200))
                elif self.get_cell(x, y)== "O":
                    win.blit(self.nyuszi, (x*200,y*200))


    def get_cell(self, x, y):
        return self.racs[y][x]

    def set_cell(self, x, y, value):
        self.racs[y][x] = value

    def mouse_click(self, x, y, letter):
        if self.get_cell(x,y)== 0:
            self.switch_letter= True
            self.set_cell(x,y, letter)

        else:
            self.switch_letter= False

    def win(self, letter):
        for sor in self.racs:
            sor_win=True
            for elem in sor:
                if elem == letter:
                    continue
                sor_win=False
                break
            if sor_win:
                break
       
        print('sor_win', sor_win)
        for i in range(3):
            oszlop_win= True
            for j in range(3):
                if self.racs[j][i] == letter:
                    continue
                oszlop_win= False
                break
            if oszlop_win:
                break
        print('oszlop_win', oszlop_win)

        diag_win=False
        if (self.racs[0][0] == self.racs[1][1] == self.racs[2][2]==letter) and (self.racs[0][0] != 0 and self.racs[1][1] !=0 and self.racs[2][2]!=0):
            diag_win=True

        if (self.racs[0][2]== self.racs[1][1] == self.racs[2][0] == letter) and (self.racs[0][2]!=0 and  self.racs[1][1] != 0 and self.racs[2][0] != 0):
            diag_win=True
        print('diag_win', diag_win)
        return sor_win or oszlop_win or diag_win






    def sorok_kiiarasa(self):
        for sor in self.racs:
            print(sor)

if __name__== "__main__":
    r=Racs()
    r.sorok_kiiratasa()

