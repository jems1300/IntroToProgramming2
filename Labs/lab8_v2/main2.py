import json

dict_keys: [str, str] = {}
# Create an empty dictionary list

user = input("Please enter the name of the file: ")

while True:
    # I put a try block to prevent invalid inputs like letters so i can avoid a value error
    try:
        user2 = int(input("Please select from our four options: \n"
                          "1. Add a task to the list\n"
                          "2. Display all tasks\n"
                          "3. Look up task\n"
                          "4. Exit \n"))
        if user2 == 1:
            key = input("Name the task: ")
            value = input("Name the description: ")
            dict_keys[key] = value
            # i did some googling and found a way to to input the key and value respectively

        elif user2 == 2:
            print(dict(sorted(dict_keys.items(), key=lambda x: x[0])))
            # This will sort the items through the index of the key value

        elif user2 == 3:
            user3 = input("Enter the name of the task: ")
            if user3 in dict_keys:
                print(dict_keys[user3])
                # If the key is indeed in the dictionary list, it will only print the value of that key
            else:
                print("Task not found")

        elif user2 == 4:
            # made sure to overwrite whatever is in the text with w
            with open(user, 'w') as txt:
                txt.write(json.dumps(dict_keys))
            break
    except ValueError:
        print("Please enter the correct value")

