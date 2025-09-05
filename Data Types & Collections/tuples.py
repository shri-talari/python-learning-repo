'''Q1. Student Records Manager 

Input: Names and marks of 5 students (marks entered as comma-separated string, cast to integers).

Store each student’s data as a tuple (name, [marks]) in a list.

Task:

Compute each student’s total & average marks.

Print: "Name | Total | Average | Pass/Fail" (Pass if avg ≥ 40).

Identify the topper (highest average).'''

records = []
for i in range(5):
    student_name = input(f"Please enter the name of student {i+1}: ")
    student_marks = input("Enter marks for all subjects separated by comma : ")
    student_marks = [int(x) for x in student_marks.split(",")]
    records.append((student_name, student_marks))

print("")
print("Name | Total | Average | Pass/Fail")

topper_name = ""
topper_avg = 0

for name, marks in records:
    student_total = 0
    for m in marks:
        student_total += m
    avg = student_total / len(marks) 
    if avg >= 40:
        result = "Pass"
    else:
        result = "Fail"      
    print(name, "|", student_total, "|", avg, "|", result)
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
print("")
print("The topper is", topper_name, "with highest average marks of", topper_avg)

        
'''Q2. Movie Ratings Tracker

You have a tuple of movies:
("Inception", "Interstellar", "Memento", "Tenet")

User enters ratings (1–10) for each movie as space-separated input (cast to integers).

Task:

Store movie and rating pairs as tuples inside a list.

Print all movies with ratings.

Identify the highest & lowest rated movies.

Print only movies with rating ≥ 8.'''

movies = ("Inception", "Interstellar", "Memento", "Tenet")

ratings_input = input("Enter ratings (1-10) for each movie in order, separated by spaces: ")
ratings = [int(x) for x in ratings_input.split()]

records = []
for i in range(len(movies)):
    records.append((movies[i], ratings[i]))

print("\nMovie | Rating")
for name, rating in records:
    print(name, "|", rating)
highest_rating = -1
lowest_rating = 11
highest_movie = ""
lowest_movie = ""
for name, rating in records:
    if rating > highest_rating:
        highest_rating = rating
        highest_movie = name
    if rating < lowest_rating:
        lowest_rating = rating
        lowest_movie = name
print("\nHighest rated movie:", highest_movie, "with rating", highest_rating)
print("Lowest rated movie:", lowest_movie, "with rating", lowest_rating)

print("\nMovies with rating >= 8:")
for name, rating in records:
    if rating >= 8:
        print(name, "|", rating)


'''Q3. Tuple-based Data Cleaner

Input: Tuple of mixed values: ("45", 23, "0", 0, "18", 9, "hello", "7")

Task:

Extract only numeric values (cast them all to integers).

Store them in a list and remove zeros.

Print:

Cleaned list

Sum and average of values

Maximum and minimum'''

data = ("45", 23, "0", 0, "18", 9, "hello", "7")
cleaned = [] 

for item in data:
    if type(item) == int:
        value = item
    elif type(item) == str and item.isdigit():
        value = int(item)
    else:
        continue  
    if value != 0:
        cleaned.append(value)

print("Cleaned list:", cleaned)

total = 0
for x in cleaned:
    total += x
average = total / len(cleaned)
maximum = cleaned[0]
minimum = cleaned[0]
for x in cleaned:
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)

