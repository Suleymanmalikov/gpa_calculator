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



def main():
    data = load_json()
    gpa_result = gpa_calculate(data)
    print(type(gpa_result))
    print(gpa_result)


if __name__=="__main__":
    main()