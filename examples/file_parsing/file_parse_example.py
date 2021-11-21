f = open("examples/file_parsing/sample_text.txt", "r")
file_content = f.readlines()
some_dict = {}
for line in file_content:
    l = line.split() # separate each line by the parameter. space by default
    some_dict[l[0]] = l[1:]
f.close()
print(some_dict)
