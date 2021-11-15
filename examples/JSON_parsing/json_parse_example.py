import json

# Python file paths are relative. If you are getting file not found try to run
# this from the EZ-YTP directory
with open('examples/JSON_parsing/example.json') as f:
    json_data = json.load(f)

    # get specific value
    print("name:", json_data['name'])

    # get nested value
    print("num wheels on car:", json_data["car"]["wheels"])

    # iterate values in list
    i = 0
    for stick in json_data["sticks"]:
        print("stick", i, ":", stick)
        i += 1
    
    # make python dict object to store name and age in format {<name>: <age>}
    person_dict = {}
    person_dict[json_data["name"]] = json_data["age"]

    print ("dict contains: ", person_dict)
