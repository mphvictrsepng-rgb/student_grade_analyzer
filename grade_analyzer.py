students = [
    {"name": "Amara",  "marks": [78, 85, 90, 72]},
    {"name": "Lerato", "marks": [55, 60, 48, 70]},
    {"name": "Sipho",  "marks": [92, 88, 95, 91]},
    {"name": "Fatima", "marks": [65, 70, 68, 75]},
    {"name": "Kagiso", "marks": [40, 35, 50, 45]},
]
"""TODO 1 — Write a function calculate_average(marks) that takes a list of marks and returns the average as a float"""

def calculate_average(marks):
    if not marks:                     #i did this just in case there are no marks for a student or an empty list
        return 0.0
    return sum(float(m) for m in marks) / len(marks)      #the float(m) for m (a generator expression) will turn string values into floats, e.g., for future work when i start working w/ CSV files
print(calculate_average(students[0]["marks"]))
print(calculate_average(students[1]["marks"]))   
