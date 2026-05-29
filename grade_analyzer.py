students = [
    {"name": "Amara",  "marks": [78, 85, 90, 72]},
    {"name": "Lerato", "marks": [55, 60, 48, 70]},
    {"name": "Sipho",  "marks": [92, 88, 95, 91]},
    {"name": "Fatima", "marks": [65, 70, 68, 75]},
    {"name": "Kagiso", "marks": [40, 35, 50, 45]},
]
"""TODO 1 - Write a function calculate_average(marks) that takes a list of marks and returns the average as a float"""

def calculate_average(marks):
    if not marks:                     #i did this just in case there are no marks for a student or an empty list
        return 0.0
    return sum(float(m) for m in marks) / len(marks)      #the float(m) for m (a generator expression) will turn string values into floats, e.g., for future work when i start working w/ CSV files
print(calculate_average(students[0]["marks"]))
print(calculate_average(students[1]["marks"]))

"""Write a function get_status(average) that returns "PASS" if the average is 60 or above, otherwise "FAIL"."""

def get_status(average):
     return "PASS" if average >= 60 else "FAIL"
student_avg_0 = calculate_average(students[0]["marks"])           # to make things easy for myself, i chose to name my variables here according to the location of the item on the list. 0 for Amara, 1 for Lerator and so forth
student_status_0 = get_status(student_avg_0)

student_avg_1 = calculate_average(students[1]["marks"])
student_status_1 = get_status(student_avg_1)


print(f'Amara | Average: {student_avg_0} | Status: {student_status_0}')        # I need to figure aout hou to make the headings, e.g., all items under thir respective headings 
print(f'Lerato | Average: {student_avg_1} | Status: {student_status_1}')
