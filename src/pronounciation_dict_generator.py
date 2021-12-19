import pickle
# Creates the pronounciation_dict.pkl which is basically cmudict.0.7a_SPHINX_40.txt
# in python dictionary form
input_file = open("cmudict.0.7a_SPHINX_40.txt", "r")
file_content = input_file.readlines()
word_dict = {}
count = 0
for line in file_content:
    l = line.split() # separate each line by the parameter. space by default
    word_dict[l[0]] = l[1:]
input_file.close()

pickle_file = open("pronounciation_dict.pkl", "wb")
pickle.dump(word_dict, pickle_file)
pickle_file.close()
