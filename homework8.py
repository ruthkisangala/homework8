# Task 1

def task_one_dict():
    print("")
    n = int(input("Enter \"n\": "))
    keys = list(range(1,(n+1)))
    values = []
    for i in range(1, n+1):
        value = i**2
        values.append(value)
    combined_dict = {keys[i]: values[i] for i in range(0, n)}
    print(combined_dict)
    return combined_dict
    
combined_dict = task_one_dict()

# Task 2
def adding(dict_input):
   
    sum_keys = 0
    sum_values = 0

    for key, value in dict_input.items():
        sum_keys += int(key)
        sum_values += int(value)
    
    print("\nThe sum of all keys is: " + str(sum_keys))
    print("The sum of all values is: " + str(sum_values))
    #return sum_keys, sum_values

adding(combined_dict)

# Task 3

# Taks 4
#dict_to_print = input("Enter a dictionary")

def dict_print(dict_to_print):
    print("\nThe keys and values of the dictionary are:")
    for key, value in dict_to_print.items():
        print("{}:{}".format(key,value))
    print("")
dict_print(combined_dict)