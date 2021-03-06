import random
from pip import main

class Domino:
     def __init__(self):
         self.dominoes=[]
     def init_game(self):
         self.population()
         self.Computer=self.radgen()
         self.Player=self.radgen()
         self.gjej_max()
         self.count=0
         self.dic={}
         self.score={}
         self.depozita=[]
         self.Mbylle=False
         self.numri=0
     def population(self):
         for i in range(7):
            for j in range(7):
             if [j,i] in self.dominoes:
               pass
             else:
               self.dominoes.append([i,j])
     def radgen(self):
         n=0
         list_random_from_stack=[]
         while n<7:
          x=random.randint(0,len(self.dominoes)-1)
          list_random_from_stack+=[self.dominoes.pop(x)]
          n+=1
         return list_random_from_stack
     def gjej_max(self):
         self.max=[]
         for i in self.Player:
          if i>self.max:
            self.max=i
         for j in self.Computer:
          if j>self.max:
            self.max=j
         if self.max in self.Computer:
           self.Computer.remove(self.max)
           self.rradha=False
         else:
           self.Player.remove(self.max)
           self.rradha=True
     def printimi(self):
       print(70 * "=")
       print("Stock pieces: ",len(self.dominoes))
       print("Computer pieces: ",len(self.Computer),"\n")
       if len(self.vlera)>6:
           print(self.vlera[0],self.vlera[1],self.vlera[2],"...",self.vlera[-3],self.vlera[-2],self.vlera[-1])
       else:
        for q in self.vlera:
           print(q,end="")
       print("\n\nYour pieces:")
       for g in range(1,len(self.Player)+1):
         print("{}:{}".format(g,self.Player[g-1]))
       print()
     def populate_dictionary(self):
              for i in range(0,7):
                  self.dic[i]=0
                  #print(dic[i])
     def calculate_stone(self):
              self.populate_dictionary()
              for i,j in self.Computer:
                  if i and j in self.dic.keys():
                    self.dic[i]=self.dic[i]+1
                    self.dic[j]=self.dic[j]+1
     def database_score(self):
              self.calculate_stone()
              for i,j in self.Computer:
                if i==j:
                    self.score[i,j]=self.dic[i]
                else:
                    self.score[i,j]=self.dic[i]+self.dic[j]
                
     def print_score(self):# Print the score
              self.database_score()
              # for self.k,self.v in self.score.items():
              #     print(self.k,": ",self.v)
              # print("score eshte: ",self.score)
     def renditja_gureve_comp(self):
              self.print_score()
              for elementi in range(0,len(self.Computer)-1):
                for elementi_krahasues in range(elementi+1,len(self.Computer)-1):
                    vlera_depozites_string_elementi=tuple(self.Computer[elementi])
                    vlera_depozites_string_elementi_krahasues=tuple(self.Computer[elementi_krahasues])
                    kthejme_intiger_elementi=int(self.score[vlera_depozites_string_elementi])
                    kthejme_intiger_elementi_krahasues=int(self.score[vlera_depozites_string_elementi_krahasues])
                    if kthejme_intiger_elementi_krahasues>kthejme_intiger_elementi:
                        maxi=self.Computer[elementi_krahasues]
                        self.Computer[elementi_krahasues]=self.Computer[elementi]
                        self.Computer[elementi]=maxi
     def futet_elementi_ne_fushe(self):
              self.renditja_gureve_comp()
              for elem in self.Computer:
                      if elem[0]==self.vlera[0][0]:
                          self.vlera.insert(0,elem[::-1])
                          index_computer=self.Computer.index(elem)
                          pop_computer=self.Computer.pop(index_computer)
                          self.score.pop(tuple(elem))
                          self.numri=1
                          break
                      if elem[1]==self.vlera[0][0]:
                          self.vlera.insert(0,elem)
                          index_computer=self.Computer.index(elem)
                          pop_computer=self.Computer.pop(index_computer)
                          self.score.pop(tuple(elem))
                          self.numri=1
                          break
                      if (elem[0]==self.vlera[-1][1]):
                          self.vlera.append(elem)
                          index_computer=self.Computer.index(elem)
                          pop_computer=self.Computer.pop(index_computer)
                          self.score.pop(tuple(elem))
                          self.numri=1
                          break
                      if elem[1]==self.vlera[-1][1]:
                          self.vlera.append(elem[::-1])
                          index_computer=self.Computer.index(elem)
                          pop_computer=self.Computer.pop(index_computer)
                          self.score.pop(tuple(elem))
                          self.numri=1
                          break
              if self.numri==0:
                      self.merr_stock(0)
                      self.rradha=False
              self.numri=0
     def kontrolli_Lojtar(self):
                while abs(self.user)>len(self.Player)+1:
                  print("Invalid input. Please try again.")
                  self.user_input()
                old_list=self.Player[:]
                guri_lojtar=[self.Player.pop(abs(self.user)-1)]#hoqem -1
                guri_lojtar_invertum=guri_lojtar[0][::-1]
                if self.user>0:
                    if self.fut_djathtas(guri_lojtar,guri_lojtar_invertum) == False:
                        self.Player=old_list
                        return False      
                if self.user<0:
                    if self.fut_majtas(guri_lojtar,guri_lojtar_invertum) == False:
                        self.Player=old_list
                        return False      
                return True  
     def fut_majtas(self,piece,piece_inver):
            if self.vlera[0][0] == piece[0][1]:

                  self.vlera.insert(0,piece[0])
                  return True
            elif self.vlera[0][0] == piece_inver[1]:
                  self.vlera.insert(0,piece_inver)
                  return True
            else:
                  return False
     def fut_djathtas(self,piece,piece_inver):
            if self.vlera[-1][1] == piece[0][0]:
                  self.vlera.append(piece[0])
                  return True
            elif self.vlera[-1][1] == piece_inver[0]:
                  self.vlera.append(piece_inver)
                  return True
            else:
                  return False      
     def user_input(self):
          self.user=input("Status: It's your turn to make a move. Enter your command.\n")
          it_is = False
          while it_is==False:
           try:
            int(self.user)
            it_is = True
           except ValueError:
            it_is = False
            print("Invalid input. Please try again.")
            self.user = input("Status: It's your turn to make a move. Enter your command.\n")
          self.user=int(self.user)
     def check_if_draw_true(self):
                funksioni=self.Computer+self.Player+self.dominoes
                count=0
                for el1 in funksioni:
                      for kursori in range(2):
                          if (el1[kursori] == self.vlera[0][0]) or (el1[kursori] == self.vlera[-1][1]):
                              count+=1
                if count==0:
                              return True
     def check_if_draw(self):
                if self.check_if_draw_true():
                            self.printimi()
                            self.Mbylle=True
                            print("Game Over, Draw!")
                            return self.fillon_loja()
                else:
                      pass
     def merr_stock(self,funk):
          if len(self.dominoes)>0 and funk==1:
                self.Player.append(self.dominoes.pop())
                self.rradha=True
          if len(self.dominoes)>0 and funk==0:
                self.Computer.append(self.dominoes.pop())
                self.rradha=False
          if len(self.dominoes)==0 and funk==1:
                print("Illegal move. Stock empty.")
                self.check_if_draw()

     def fillon_loja(self):
      if self.Mbylle==False:
        self.vlera=[self.max]
      while (len(self.Player)!=0 or len(self.Computer)!=0) and self.Mbylle == False:
       self.printimi()
       if self.rradha:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        computer_value_input=input() 
        while computer_value_input!='':
           print("Press enter and not another character for the computer to make a move")
           computer_value_input=input()
        if self.Computer!=[]:
          self.futet_elementi_ne_fushe()
        self.rradha=False
        if self.Computer==[]:
          self.printimi()
          print("Status: The game is over. The computer won!")
          break
       else:
          self.user_input()
          if len(self.Player)>0:
           if self.user==0:
                      self.merr_stock(1)
           else:
            while self.kontrolli_Lojtar()==False:
                  if self.user==0:
                            self.merr_stock(1)
                            break
                  else:     
                            print("Illegal move. Please try again.")
                            self.user_input()
          self.rradha=True
          if self.Player==[]:
            self.printimi()
            print("Status: The game is over. You won!")  
            break
       self.check_if_draw()
if __name__ == "__main__":
    game = Domino()
    game.init_game()
    game.fillon_loja()