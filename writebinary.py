import pickle

with open("writebinary.TXT","wb") as file:

    pickle.dump({"HELLO PYTHON"},file)
