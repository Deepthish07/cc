def calculate_cgpa(grades, credits):
    total_points = 0
    total_credits = 0

    for i in range(len(grades)):
        total_points += grades[i] * credits[i]
        total_credits += credits[i]

    cgpa = total_points / total_credits
    return cgpa

def cgpa_calculator():
    print("Welcome to the CGPA Calculator!")
    
    num_subjects = int(input("Enter the number of subjects: "))

    grades = []
    credits = []

    for i in range(num_subjects):
        grade = float(input(f"Enter your grade for subject {i+1} (0.0 - 10.0): "))
        credit = float(input(f"Enter the credits for subject {i+1}: "))
        
        grades.append(grade)
        credits.append(credit)

    cgpa = calculate_cgpa(grades, credits)
    print(f"\nYour CGPA is: {cgpa:.2f}")

# Run the CGPA calculator
cgpa_calculator()
