Mylist = ['Lakers','Bucks','Celtics','Suns']
print(*Mylist[0:4],sep=', ')


Mylist = ['Lakers','Bucks','Celtics','Suns']
Future_Champ = input('Predict who’s going to be the next champion: ')
Mylist.append(Future_Champ)
Mylist.sort()
print(*Mylist,sep=',')
