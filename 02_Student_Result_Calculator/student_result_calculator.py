sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))
sub5 = int(input("Enter marks for Subject 5: "))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100
print("\n----- Student Result -----")
print("Total Marks :", total_marks)
print("Percentage  :", percentage, "%")
if percentage >= 90:
    print("Grade : S")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade : B")
elif percentage >= 60:
    print("Grade : C")
elif percentage >= 50:
    print("Grade : D")
else:
    print("Grade : F")