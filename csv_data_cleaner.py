import csv

# function 
def is_valid_row(row):                             
    if row["name"] == "":
        return False
    try:
        float(row["mark"])
        return True
    except ValueError:
        return False

# the reading and cleaning section
cleaned = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if not is_valid_row(row):
            continue
        cleaned.append({
            "name": row["name"].strip(),
            "age":  row["age"] if row["age"] != "" else "0",
            "mark": float(row["mark"]),
            "city": row["city"] if row["city"] != "" else "Unknown"
        })

# the output 
fieldnames = ["name", "age", "mark", "city"]

with open("students_clean.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned)

print("Done! students_clean.csv has been created.")
print(cleaned)
