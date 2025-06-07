# GPA Calculator

This Python project calculates your total GPA (Grade Point Average) and per-semester GPA from a JSON file of grades. It also generates a PDF summarizing your results.

---

## Features

- **Load grades from a JSON file**
- **Compute overall GPA**
- **Compute GPA for each semester**
- **Generate a results summary as a PDF**

---

## How to Use

### 1. Requirements

- Python 3.x
- [FPDF](https://pypi.org/project/fpdf/) library

Install FPDF via pip:

```bash
pip install fpdf
```

### 2. Prepare the Grades JSON File

Create a file named `grades.json` in the same directory. Use this format:

```json
[
  {
    "semester": "Winter 2024/25",
    "courses": [
      {
        "code": "W08IST-SI4002W",
        "name": "Basics of Entrepreneurship",
        "type_hours": "w 30",
        "grade": 5.5,
        "ects": 2
      }
      // ... more courses
    ]
  }
  // ... more semesters
]
```

(See the provided `grades.json` for a complete example.)

### 3. Run the Program

```bash
python main.py
```

### 4. Output

- The program prints the overall GPA and GPAs for each semester in your terminal.
- It also creates a `gpa.pdf` file with a summary table.

---

## Files

- `main.py` — The main Python script.
- `grades.json` — Your input data.
- `gpa.pdf` — Output PDF (created by the program).
- `README.md` — This file.

---

## Customizing

- You can update `grades.json` with your own course/semester data as needed.
- The script ignores courses with 0 ECTS (like "Futsal").

---

## Example Output

```
Final GPA: 4.47
Semester: Winter 2024/25   GPA: 4.42
Semester: Summer 2023/24   GPA: 4.55
Semester: Winter 2023/24   GPA: 4.35
```

And see `gpa.pdf` for a summary table.

---

## License

Feel free to use and adapt for learning or personal use!
