
import pickle
with open("writebinary.TXT", 'rb') as file:
    a=pickle.load(file)
    print(a)