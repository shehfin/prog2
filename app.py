course_name = "Software Engineering"
student_count = 60

with open("build_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Course Name: {course_name}\n")
    file.write(f"Number of Students: {student_count}\n")

print("Report generated successfully.")
print(f"Course Name: {course_name}")
print(f"Number of Students: {student_count}")