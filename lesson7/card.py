import random

class players_card():
    def __init__(self, lst):
        self._lst = lst

    @property
    def lst(self):
        return self._lst


    def fillcard(self, lst):

            self.colomn1 = [lst[itm] for itm in range(0, 5)]
            self.colomn2 = [lst[itm] for itm in range(5, 10)]
            self.colomn3 = [lst[itm] for itm in range(10, 15)]

            return [self.colomn1 , self.colomn2, self.colomn3] 

            
    
    def step(self,  numb):

        self.numb = numb
        
        for i in range(0, 15):
            if self.lst[i] == numb:
               self.lst[i] = ''
               
            else:
                pass

        return self.lst


            

            
            