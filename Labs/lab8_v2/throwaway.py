import json

ex_dict: {str, str} = {"fuck": "you",
                       "bitch": "ass"}
with open("file.txt", 'w') as file:
    file.write(json.dumps(ex_dict))
