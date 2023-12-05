# Task 1

def task_one_dict():
    n = int(input("Enter \"n\":"))
    keys = list(range(1,(n+1)))
    values = []
    for i in range(1, n+1):
        value = i**2
        values.append(value)
    combined_list = {keys[i]: values[i] for i in range(0, n)}
    print(combined_list)
    
task_one_dict()


# Task 2


