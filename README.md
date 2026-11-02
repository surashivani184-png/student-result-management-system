# Student Performance & Result Management System
**MCA General — Semester 1 | Python Programming Lab Mini Project**

- **Student Name:** Shivani
- **University Roll / UID:** 26MCA20231
- **Section:** 4-A
- **Course:** Master of Computer Applications (MCA General)
- **Semester:** 1st Semester
- **Subject:** Python Programming Lab

---

## 📌 Project Overview
The **Student Performance & Result Management System** is a professional desktop GUI application developed in Python (using standard `tkinter` and `ttk`). It automates the evaluation, storage, retrieval, and reporting of student examination marks across five core MCA Semester 1 subjects.

The system incorporates all fundamental and intermediate Python syllabus concepts—including modern structural pattern matching (`match-case`), nested loops, custom functions with default arguments, dictionary/list data structures, robust input validation, and persistent file storage via JSON.

---

## 🚀 Key Features
1. **Interactive Modern GUI**: Clean Navy & Slate styled dual-pane interface built using Tkinter and `ttk.Treeview`.
2. **Student & Subject Records**: Tracks UID, Student Name, Section, Semester, and 5 Core Subject Marks:
   - Python Programming
   - Data Structures & Algorithms
   - Computer Architecture
   - Discrete Mathematics
   - Operating Systems
3. **Automated Calculations**:
   - Total Marks out of 500
   - Percentage Calculation
   - Academic Letter Grade (`A+`, `A`, `B+`, `B`, `C`, `D`, `F`) using Python's `match-case`
   - Subject-wise & Overall Pass/Fail Evaluation (Minimum 40% required per subject)
4. **Complete Record Operations (CRUD)**:
   - Add new student with duplicate UID detection
   - Update existing records directly from the interactive table
   - Delete records with confirmation dialog
   - Search/Filter by UID or Name in real-time
5. **Real-time Class Analytics (KPI Cards)**:
   - Total Enrolled Students
   - Count of Passed and Failed Students
   - Class Average Percentage
6. **Academic Marksheet & Batch Report Generation**:
   - Generates official ASCII-formatted Marksheet with verification seals
   - Export individual marksheet to formatted `.txt` files
   - Export full class summary report with subject-wise class averages to `.txt` files
7. **Zero External Dependencies**: Built entirely with Python Standard Library (`tkinter`, `json`, `os`).

---

## 📂 Project Directory Structure
```text
mini project/
├── student_management_system.py   # Complete application source code
├── students_data.json             # Persistent JSON database (pre-seeded with 10 records)
├── test_system.py                 # Automated unit test suite (all syllabus logic)
├── PROJECT_REPORT.md              # Complete 17-part academic project report
├── PRESENTATION_AND_VIVA.md       # 10-slide PPT outline, speech & 15 viva Q&As
└── README.md                      # Quick-start documentation
```

---

## 🛠️ How to Run the Application

### Prerequisites
- Python 3.10 or higher installed (Tested on Python 3.13)
- Windows / macOS / Linux with Tkinter support (standard with official Python installers)

### Step 1: Open Terminal / Command Prompt
Open PowerShell or Command Prompt and navigate to the project directory:
```powershell
cd "c:\Users\dell\Desktop\python programming lab\mini project"
```

### Step 2: Run Automated Tests (Optional but Recommended)
Verify the core business logic and syllabus constructs:
```powershell
python test_system.py
```
*Expected Output:* `ALL 8 VERIFICATION TESTS PASSED SUCCESSFULLY! [OK]`

### Step 3: Launch the GUI Application
```powershell
python student_management_system.py
```

---

## 🎯 Syllabus Concepts Demonstrated
| Syllabus Topic | Project Implementation Location & Demonstration |
| :--- | :--- |
| **Python Features** | Interpreted execution, platform independence, standard library |
| **Program Structure** | Global configuration, business logic functions, GUI class, `if __name__ == "__main__":` |
| **Keywords & Identifiers**| `def`, `return`, `if`, `elif`, `else`, `match`, `case`, `for`, `while`, `break`, `continue`, `global`, `True`, `False`, `try`, `except`, `with`, `class` |
| **Data Types** | `int` (counters), `float` (percentages, marks), `str` (UID, names), `list` (subjects, records), `dict` (student data), `bool` (pass/fail status) |
| **Operators** | Arithmetic (`+`, `-`, `*`, `/`, `//`), Comparison (`==`, `<`, `>=`), Logical (`and`, `or`, `not`), Membership (`in`, `not in`) |
| **Indentation & Scope** | Standard 4-space blocks, global configurations vs local function scopes |
| **Conditionals** | Range validation (`0 <= mark <= 100`), `if-elif-else`, and `match-case` tier evaluation |
| **Loops & Control** | `for` loop (marks summation, table loading), `while` loop with `break` (linear search), `continue` (record filtering) |
| **Nested Loops** | Subject-wise class averages calculation across all student records |
| **Functions** | Modularity, docstrings, type conversions, default parameters (`max_marks=500.0`), tuple returns |
| **File I/O** | Safe file reading and writing using `with open(...)` and `json` serialization |

---

## 👤 Author Credentials
- **Student Name:** Shivani
- **UID:** 26MCA20231
- **Section:** 4-A
- **Course:** MCA General
- **Semester:** 1
- **Subject:** Python Programming Lab
