import json

# Load json file
def load_json():
    with open('grades.json', 'r') as file:
        data = json.load(file)
    return data

# Calculate GPA
def gpa_calculate(data):
    grade_sum = 0
    ects_sum = 0
    for course_semester in data:
        for course in course_semester['courses']:
            grade = course['grade']
            ect = course['ects']
            grade_sum += grade * ect
            ects_sum += course['ects']
    return grade_sum / ects_sum

# gpa for each semester in list
def gpa_for_each_semester(data):
    semesters = []
    for course_semester in data:        
        semester_gpa = {}
        grade_ect_mult = 0
        ects_sum = 0
        semester_gpa['semester'] = course_semester['semester']
        for course in course_semester['courses']:
            grade = course['grade']
            ect = course['ects']
            grade_ect_mult += grade * ect
            ects_sum += course['ects']
        gpa_semester = grade_ect_mult / ects_sum
        semester_gpa['GPA'] = round(gpa_semester, 3)
        semesters.append(semester_gpa)
    return semesters

def main():
    # Load json file
    data = load_json()
    
    # Total GPA result
    total_gpa = gpa_calculate(data)
    print(f"Final GPA: {total_gpa}")

    # gpa for each semester
    each_semester_gpa = gpa_for_each_semester(data)
    for semester in each_semester_gpa:
        print(f"Semester: {semester['semester']}   GPA: {semester['GPA']}")


if __name__=="__main__":
    main()



"""
Here are some feature ideas you can add to your GPA calculator:

Per-Semester GPA Calculation:
Show GPA for each semester, not just the overall GPA.

Course Filtering:
Allow users to filter courses by semester, grade, or ECTS.

Grade Distribution:
Display statistics or charts showing grade distribution.

Best/Worst Course Finder:
Highlight courses with the highest and lowest grades.

Course Addition/Editing:
Let users add, edit, or remove courses directly from the program.

Support for Different Grading Scales:
Allow conversion between different grading systems (e.g., 1-5, A-F).

Export Results:
Export GPA and course data to a CSV or PDF file.

User Interface:
Add a simple GUI using Tkinter or a web interface with Flask.

Pass/Fail Summary:
Show how many courses were passed or failed.

What-If Analysis:
Let users simulate how future grades would affect their GPA.

Let me know if you want details on how to implement any of these!
"""