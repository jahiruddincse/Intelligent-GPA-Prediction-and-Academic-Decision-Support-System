# Intelligent GPA Prediction and Academic Decision Agent



grade_points = {
    "S": 10, "A": 9, "B": 8, "C": 7,
    "D": 6, "E": 5, "F": 0
}

print("===== GPA Prediction and Decision Agent =====\n")

subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    print("\nSubject", i + 1)

    name = input("Subject name: ")
    credits = float(input("Credits: "))
    grade = input("Expected Grade (S,A,B,C,D,E,F): ").upper()
    difficulty = int(input("Difficulty (1-5): "))
    prep = int(input("Preparation Level (1-5): "))

    subjects.append({
        "name": name,
        "credits": credits,
        "grade": grade,
        "difficulty": difficulty,
        "prep": prep
    })

total_points = 0
total_credits = 0

for s in subjects:
    total_points += grade_points[s["grade"]] * s["credits"]
    total_credits += s["credits"]

current_gpa = total_points / total_credits

print("\nPredicted Current GPA:", round(current_gpa, 2))

print("\n===== SUBJECT PRIORITY =====")

priority = []

for s in subjects:
    impact = s["credits"] * (10 - grade_points[s["grade"]])
    effort = s["difficulty"] + (5 - s["prep"])

    score = impact / (effort + 1)
    priority.append((score, s))

priority.sort(key=lambda x: x[0], reverse=True)

for score, s in priority:
    print("-", s["name"], "| Score:", round(score, 2))

target = float(input("\nEnter target GPA: "))
print("\nTarget GPA:", target)

best_subject = None
best_gpa = current_gpa
best_effort = 0

for s in subjects:
    original = s["grade"]

    s["grade"] = "S"

    total_points = 0
    total_credits = 0

    for x in subjects:
        total_points += grade_points[x["grade"]] * x["credits"]
        total_credits += x["credits"]

    new_gpa = total_points / total_credits

    if new_gpa > best_gpa:
        best_gpa = new_gpa
        best_subject = s
        best_effort = s["difficulty"] + (5 - s["prep"])

    s["grade"] = original

print("\n===== RECOMMENDATION =====")

if best_subject:
    print("\nBest way to reach your target GPA (" + str(target) + "):\n")

    print("Focus on:", best_subject["name"])

    if best_subject["difficulty"] >= 4:
        print("Suggestion: Practice concepts regularly")
    elif best_subject["prep"] <= 2:
        print("Suggestion: Start from basics")
    else:
        print("Suggestion: Revise and solve papers")

    print("\nPredicted GPA:", round(best_gpa, 2))
    print("Effort score:", best_effort)

else:
    print("Improve multiple subjects to reach target GPA")

print("\n===== GPA PREDICTION ANALYSIS =====")

for s in subjects:
    original = s["grade"]

    s["grade"] = "S"

    total_points = 0
    total_credits = 0

    for x in subjects:
        total_points += grade_points[x["grade"]] * x["credits"]
        total_credits += x["credits"]

    new_gpa = total_points / total_credits

    print("If", s["name"], "gets S → GPA:", round(new_gpa, 2))

    s["grade"] = original

print("\n===== PERFORMANCE =====")

if current_gpa >= 9:
    print("Excellent")
elif current_gpa >= 8:
    print("Very Good")
elif current_gpa >= 7:
    print("Good")
else:
    print("Needs Improvement")

print("\nNote: Predictions are based on input and may vary in real exams.")
