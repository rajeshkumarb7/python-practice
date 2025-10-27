import pickle

def save_dict(d,file_path):
    with open(file_path,'wb') as file:
        pickle.dump(d,file)

def load_dict(file_path):
    with open(file_path,'rb') as file:
        return pickle.load(file)

dic={1:"apple",2:"ball",3:"cat"}
#dic=[1,3,5,7,5,3,2,0] any python object like int,string,list,set, tuple,dict....
f_path="./file_save_dictionary_using _pickel.pickle"
save_dict(dic,f_path)
recovered=load_dict(f_path)
print(recovered)

"""
Key Points:

Pickling = Convert a Python object → byte stream (for saving).

Unpickling = Convert byte stream → original object (for loading).

pickle.dump(obj, file) → Save object to file.

pickle.load(file) → Read object back from file.

Use 'wb' (write binary) for saving and 'rb' (read binary) for loading.

Useful for saving data, models, or sending Python objects over a network.
"""