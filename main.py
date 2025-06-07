import json
from fpdf import FPDF

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

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "GPA CALCULATOR", align="C", ln=True)
    pdf.ln(10)

    pdf.cell(40, 10, f"Total GPA: {total_gpa}", ln=True)

    pdf.cell(40, 10, "Semester", 1)
    pdf.cell(40, 10, "GPA", 1)
    pdf.ln(10)

    for semester in each_semester_gpa:
        pdf.cell(40, 10, str(semester['semester']), 1)
        pdf.cell(40, 10, str(semester['GPA']), 1)
        pdf.ln(10)
    
    pdf.output("gpa.pdf")

    


if __name__=="__main__":
    main()