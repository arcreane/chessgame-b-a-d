coo=[]
#Génère une liste de A1 à H8
for i in range(1,9):
    coo.append(f'A{i}'),coo.append(f'B{i}'),coo.append(f'C{i}'),coo.append(f'D{i}'),coo.append(f'E{i}'),coo.append(f'F{i}'),coo.append(f'G{i}'),coo.append(f'H{i}')
# Pos_numb est un dict où la ligne et colonne = coordonnées ,cad
Pos_numb={}
for i in range(0,64):
    Pos_numb[coo[i]]=(0,0)
# Numb_pos inverse de Pos_numb
Numb_pos = {}
for i in range(0,64):
    Numb_pos[(50*i,50*i)]=coo[i]
print(Pos_numb)
print(Numb_pos)
if __name__ == "__main__":
    class Player:
        def __init__(self, name, color):
            self.name = name
            self.color = color
            if self.color == 0:
                self.color = (255, 255, 255)

        if __name__ == "__main__":
            def askMove(self):
                ask_user = input("Votre prochain mouvement ?")


                if ask_user in Pos_numb:
                    print("1")
                else:
                    return ask_user, player_one.askMove()



print(coo)
print(len(coo))
player_one=Player('Simon',0)
print(player_one.askMove())

