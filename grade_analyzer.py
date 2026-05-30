students = [
    {"name": "Amara",  "marks": [78, 85, 90, 72]},
    {"name": "Lerato", "marks": [55, 60, 48, 70]},
    {"name": "Sipho",  "marks": [92, 88, 95, 91]},
    {"name": "Fatima", "marks": [65, 70, 68, 75]},
    {"name": "Kagiso", "marks": [40, 35, 50, 45]},
]

def calculate_average(marks):
    if not marks:                                     #i did this just in case there are no marks for a student or an empty list
        return 0.0
    return sum(float(m) for m in marks) / len(marks)    #the float(m) for m (a generator expression) will turn string values into floats, e.g., for future work when i start working w/ CSV files

def get_status(average):
    return "PASS" if average >= 60 else "FAIL"            

results = []                                     #this empty list will store all the results

for student in students:
    avg = calculate_average(student["marks"])
    status = get_status(avg)

    results.append({                             #i'm gonna add this to the empty list
        "name":   student["name"],
        "avg":    avg,
        "status": status
    })

print('=============Student Report===============')         # I'm going to loop through the results to avoid printing a block of dictionries. this will make my report look clean and neat.
print()                                                 # just to make some space between the report header print() output and the columns output
print(f'{'Name':<10} | {'Average':<10} | {'Status':<10}')
print('-' * 42)
for student in results:
    print(f'{student['name']:<10} | {student['avg']:<10.2f} | {student['status']:<10}')
print('=' * 42)