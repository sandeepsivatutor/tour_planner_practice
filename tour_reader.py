import csv
with open("tour_places.csv", newline="") as file:
    for row in csv.DictReader(file):
        print(row)