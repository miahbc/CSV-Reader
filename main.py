# cats = open("cats.csv", "r")
# dogs = open("dogs.csv", "r")
# print(cats.read())
# print(dogs.read())

import csv

# with open('cats.csv') as cats_file:
#     csv_reader = csv.reader(cats_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f"Column names are {', '.join(row)}")
#             line_count += 1
#         else:
#             print(f'\t{row[0]} is a {row[1]}-year-old {row[2]}.')
#             line_count += 1


# with open('dogs.csv') as dogs_file:
#     csv_reader = csv.reader(dogs_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f"Column names are {', '.join(row)}")
#             line_count += 1
#         else:
#             print(f'\t{row[0]} is a {row[1]}-year-old {row[2]}.')
#             line_count += 1

with open('cats.csv') as cats_file:
    csv_reader = csv.reader(cats_file, delimiter=',')
    catList = []
    for row in csv_reader:
        catList.append(row)
    print(catList)