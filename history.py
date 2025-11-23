import csv
import os.path

FILE = "history.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Cost Price", "Selling Price", "Type", "Amount", "Percentage"])

def save_record(cp, sp, type_, amount, percent):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([cp, sp, type_, amount, percent])

def show_history():
    print("\nHISTORY OF THE RECORDED AMOUNTS\n")

    if not os.path.exists(FILE):
        print("No history found!")
        return

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        rows=list(reader)
        if len(rows) == 0:
            print("No records found.")
            
        count=0
        for row in rows:
            count+=1
            print(count,". CP:",row[0],"| SP:", row[1],"| Type:", row[2],"| Amount:",row[3],"| Percent:",row[4])
    
def clear_history():
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Cost Price", "Selling Price", "Type", "Amount", "Percentage"])
        print("History cleared successfully...")
