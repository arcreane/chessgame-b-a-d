


class Player:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        if self.color== 0:
            self.color =(255,255,255)
    def askMove(self):
        self.ask_user=input("Votre prochain mouvement ?")

        if self.ask_user == 0:
            print("1")
        else:
            return self.ask_user,player_one.askMove()


coo=[]
#Génère une liste de A1 à H8
for i in range(1,9):
    coo.append(f'A{i}'),coo.append(f'B{i}'),coo.append(f'C{i}'),coo.append(f'D{i}'),coo.append(f'E{i}'),coo.append(f'F{i}'),coo.append(f'G{i}'),coo.append(f'H{i}')
print(coo)
print(len(coo))
player_one=Player('Simon',0)
print(player_one.askMove())
