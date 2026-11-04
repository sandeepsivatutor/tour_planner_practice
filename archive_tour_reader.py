import csv
with open("archive_tour.csv", newline="") as file:
    for row in csv.DictReader(file):
        print(row)