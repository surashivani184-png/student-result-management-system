"""
========================================================================================
PROJECT TITLE: Student Performance & Result Management System
ACADEMIC SUBMISSION DETAILS:
  - Student Name : Shivani
  - UID          : 26MCA20231
  - Section      : 4-A
  - Course       : Master of Computer Applications (MCA General)
  - Semester     : Semester 1
  - Subject      : Python Programming Lab (Mini Project)
========================================================================================
PURPOSE & SYLLABUS CONCEPTS DEMONSTRATED:
  1. Program Structure: Imports, global configuration, business logic functions, GUI class.
  2. Keywords & Identifiers: def, return, if, elif, else, match, case, for, while, break,
     continue, global, True, False, None, try, except, with, as, class.
  3. Variables & Data Types: int, float, str, bool, list, dict, tuple.
  4. Operators: Arithmetic (+, -, *, /, //, %), Comparison (==, !=, <, <=, >, >=),
     Logical (and, or, not), Membership (in, not in), Assignment (=, +=).
  5. Scope and Lifetime: Global data constants vs local function parameters/variables.
  6. Indentation: Strict standard 4-space block hierarchy.
  7. Conditional Logic: if-elif-else ladders and Python 3.10+ match-case statement.
  8. Loops & Control: for loops, while loops, nested loops, break, and continue.
  9. Functions: Modular programming, default parameters, multi-value returns, docstrings.
  10. File Handling & Storage: JSON persistence for robust data management.
  11. GUI: Tkinter & ttk with Treeview, modern responsive layout, dialogs, marksheets.
========================================================================================
"""

# ======================================================================================
# MODULE 1: IMPORTS & GLOBAL CONFIGURATION (Syllabus: Program Structure & Global Scope)
# ======================================================================================
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Global Constants (Syllabus: Identifiers & Scope)
DATA_FILE = "students_data.json"
MAX_MARKS_PER_SUBJECT = 100.0
PASSING_MARKS = 40.0

# 5 Core MCA Semester 1 Subjects (Syllabus: List data type)
SUBJECTS = [
    "Python Programming",
    "Data Structures & Algorithms",
    "Computer Architecture",
    "Discrete Mathematics",
    "Operating Systems"
]

TOTAL_MAX_MARKS = float(len(SUBJECTS) * MAX_MARKS_PER_SUBJECT)  # 500.0


# ======================================================================================
# MODULE 2: CORE BUSINESS LOGIC & ALGORITHMS (Syllabus: Functions, Loops, Conditionals)
# ======================================================================================

def calculate_total_marks(marks_list):
    """
    Calculates the total marks from a list of numerical marks.
    Demonstrates:
      - Function definition (def) and docstrings
      - Variables (total, mark)
      - Arithmetic operator (+) and assignment operator (+=)
      - 'for' loop for collection traversal
    """
    total = 0.0
    for mark in marks_list:  # Syllabus: 'for' loop
        total += float(mark)  # Syllabus: Arithmetic += operator and float casting
    return round(total, 2)


def calculate_percentage(total_marks, max_marks=TOTAL_MAX_MARKS):
    """
    Calculates percentage obtained based on total and max marks.
    Demonstrates:
      - Default parameter (max_marks=TOTAL_MAX_MARKS)
      - Arithmetic division (/) and multiplication (*) operators
      - Return statement returning a float
    """
    if max_marks <= 0:  # Syllabus: if conditional & comparison operator
        return 0.0
    percentage = (total_marks / max_marks) * 100.0
    return round(percentage, 2)


def evaluate_pass_fail(marks_dict, pass_mark=PASSING_MARKS):
    """
    Checks if student has passed all subjects or failed in one or more.
    Demonstrates:
      - Dictionary iteration (.items())
      - 'for' loop with early termination ('break' statement)
      - Conditional comparison (<) and boolean flag
      - Tuple return: (is_passed: bool, failed_subjects: list)
    """
    passed = True
    failed_subjects = []
    
    # Check each individual subject marks against the pass mark
    for subject, mark in marks_dict.items():
        if float(mark) < pass_mark:  # Syllabus: Comparison operator
            passed = False
            failed_subjects.append(subject)
            # We record all failed subjects to inform the student
    
    return passed, failed_subjects


def determine_grade(percentage, is_passed):
    """
    Assigns academic letter grade based on percentage using match-case.
    Demonstrates:
      - 'if-else' conditional statement
      - Integer floor division operator (//)
      - Python 3.10+ 'match-case' pattern matching with compound patterns (|)
    """
    # If the student failed in any subject, grade is strictly 'F' (Fail)
    if not is_passed:  # Syllabus: Logical 'not' operator
        return "F"
    
    # Integer division by 10 to obtain tier bracket (e.g., 95 // 10 = 9)
    tier = int(percentage // 10)  # Syllabus: Arithmetic '//' operator
    
    # Syllabus: Modern Python match-case construct
    match tier:
        case 10 | 9:
            return "A+"   # 90% - 100% (Outstanding)
        case 8:
            return "A"    # 80% - 89.99% (Excellent)
        case 7:
            return "B+"   # 70% - 79.99% (Very Good)
        case 6:
            return "B"    # 60% - 69.99% (Good)
        case 5:
            return "C"    # 50% - 59.99% (Average)
        case 4:
            return "D"    # 40% - 49.99% (Pass Class)
        case _:
            return "F"    # Below 40% (Fail)


def linear_search_student(records, target_uid):
    """
    Searches for a student by UID using a 'while' loop with index and 'break'.
    Demonstrates:
      - 'while' loop construct
      - Indexing and comparison
      - 'break' statement on condition match
      - Return record and index, or (None, -1) if not found
    """
    index = 0
    total_records = len(records)
    found_student = None
    found_index = -1
    
    # Syllabus: 'while' loop
    while index < total_records:
        current_record = records[index]
        # Comparison operator (case-insensitive UID check)
        if current_record["uid"].strip().upper() == target_uid.strip().upper():
            found_student = current_record
            found_index = index
            break  # Syllabus: 'break' loop control statement
        index += 1  # Syllabus: Increment counter
        
    return found_student, found_index


def filter_students_by_query(records, query_text):
    """
    Filters student records by query (matches UID or Name).
    Demonstrates:
      - 'for' loop
      - 'continue' statement to skip non-matching elements
      - Membership operator 'in'
      - List accumulation
    """
    filtered = []
    clean_query = query_text.strip().lower()
    
    for student in records:
        uid_match = clean_query in student["uid"].lower()
        name_match = clean_query in student["name"].lower()
        
        # If neither matches, skip to the next iteration using 'continue'
        if not (uid_match or name_match):  # Syllabus: Logical 'or', 'not'
            continue  # Syllabus: 'continue' loop control statement
            
        filtered.append(student)
        
    return filtered


def compute_class_statistics(records):
    """
    Computes overall summary statistics for the entire batch.
    Demonstrates:
      - Nested loops (calculating average score per subject across all students)
      - Built-in functions: min(), max(), len()
      - Dictionary aggregation
    """
    if not records:
        return {
            "total_students": 0,
            "pass_count": 0,
            "fail_count": 0,
            "pass_percentage": 0.0,
            "class_average": 0.0,
            "highest_percentage": 0.0,
            "lowest_percentage": 0.0,
            "subject_averages": {sub: 0.0 for sub in SUBJECTS}
        }
    
    total_students = len(records)
    pass_count = 0
    fail_count = 0
    total_percentage_sum = 0.0
    percentages = []
    
    # Subject-wise marks accumulator
    subject_sums = {sub: 0.0 for sub in SUBJECTS}
    
    # Outer loop through all students (Syllabus: for loop)
    for student in records:
        pct = student["percentage"]
        percentages.append(pct)
        total_percentage_sum += pct
        
        if student["result"] == "PASS":
            pass_count += 1
        else:
            fail_count += 1
            
        # Inner loop through each subject (Syllabus: Nested loop demonstration)
        for sub_name in SUBJECTS:
            subject_sums[sub_name] += float(student["marks"].get(sub_name, 0.0))
            
    # Calculate averages
    class_avg = round(total_percentage_sum / total_students, 2)
    pass_pct = round((pass_count / total_students) * 100.0, 2)
    highest_pct = max(percentages)
    lowest_pct = min(percentages)
    
    subject_averages = {
        sub: round(subject_sums[sub] / total_students, 2)
        for sub in SUBJECTS
    }
    
    return {
        "total_students": total_students,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_percentage": pass_pct,
        "class_average": class_avg,
        "highest_percentage": highest_pct,
        "lowest_percentage": lowest_pct,
        "subject_averages": subject_averages
    }


# ======================================================================================
# MODULE 3: DATA PERSISTENCE LAYER (Syllabus: File Handling & JSON Storage)
# ======================================================================================

def load_student_records(file_path=DATA_FILE):
    """
    Loads student records from a JSON file.
    Demonstrates:
      - 'try-except' exception handling
      - 'with' context manager for safe file I/O
      - json.load() deserialization
    """
    if not os.path.exists(file_path):
        # Create initial seed sample data if file does not exist
        return create_initial_sample_records(file_path)
    
    try:
        with open(file_path, "r", encoding="utf-8") as file_handler:
            data = json.load(file_handler)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError) as error:
        print(f"[Warning] Failed to load {file_path}: {error}. Starting with empty records.")
        return []


def save_student_records(records, file_path=DATA_FILE):
    """
    Saves student records to a JSON file with pretty formatting.
    Demonstrates:
      - 'with open' context manager
      - json.dump() with indent=4 for human readability
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file_handler:
            json.dump(records, file_handler, indent=4)
        return True
    except IOError as error:
        print(f"[Error] Failed to save {file_path}: {error}")
        return False


def create_initial_sample_records(file_path):
    """
    Generates realistic, representative sample data for Section 4-A.
    Includes the project author (Shivani, UID: 26MCA20231) and classmates.
    """
    sample_records = [
        {
            "uid": "26MCA20231",
            "name": "Shivani",
            "section": "4-A",
            "semester": "1",
            "marks": {
                "Python Programming": 94.0,
                "Data Structures & Algorithms": 89.0,
                "Computer Architecture": 86.0,
                "Discrete Mathematics": 92.0,
                "Operating Systems": 90.0
            },
            "total": 451.0,
            "percentage": 90.2,
            "grade": "A+",
            "result": "PASS"
        },
        {
            "uid": "26MCA20202",
            "name": "Aman Sharma",
            "section": "4-A",
            "semester": "1",
            "marks": {
                "Python Programming": 78.0,
                "Data Structures & Algorithms": 72.0,
                "Computer Architecture": 68.0,
                "Discrete Mathematics": 74.0,
                "Operating Systems": 70.0
            },
            "total": 362.0,
            "percentage": 72.4,
            "grade": "B+",
            "result": "PASS"
        },
        {
            "uid": "26MCA20205",
            "name": "Priya Verma",
            "section": "4-A",
            "semester": "1",
            "marks": {
                "Python Programming": 85.0,
                "Data Structures & Algorithms": 82.0,
                "Computer Architecture": 80.0,
                "Discrete Mathematics": 79.0,
                "Operating Systems": 84.0
            },
            "total": 410.0,
            "percentage": 82.0,
            "grade": "A",
            "result": "PASS"
        },
        {
            "uid": "26MCA20211",
            "name": "Rahul Kumar",
            "section": "4-A",
            "semester": "1",
            "marks": {
                "Python Programming": 52.0,
                "Data Structures & Algorithms": 48.0,
                "Computer Architecture": 55.0,
                "Discrete Mathematics": 45.0,
                "Operating Systems": 50.0
            },
            "total": 250.0,
            "percentage": 50.0,
            "grade": "C",
            "result": "PASS"
        },
        {
            "uid": "26MCA20219",
            "name": "Sneha Gupta",
            "section": "4-A",
            "semester": "1",
            "marks": {
                "Python Programming": 65.0,
                "Data Structures & Algorithms": 34.0,  # Below 40: Failed in DSA
                "Computer Architecture": 58.0,
                "Discrete Mathematics": 62.0,
                "Operating Systems": 60.0
            },
            "total": 279.0,
            "percentage": 55.8,
            "grade": "F",
            "result": "FAIL"
        }
    ]
    save_student_records(sample_records, file_path)
    return sample_records


# ======================================================================================
# MODULE 4: TKINTER GUI APPLICATION INTERFACE (Syllabus: OOP & Event-Driven Programming)
# ======================================================================================

class StudentPerformanceApp:
    """
    Main Application GUI Class for Student Performance & Result Management System.
    Provides complete record management, calculation, search, and reporting.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance & Result Management System - MCA General")
        self.root.geometry("1280x750")
        self.root.minsize(1050, 680)
        
        # Set modern application theme styling
        self.apply_theme_styles()
        
        # In-memory record storage (Syllabus: List of Dictionaries)
        self.records = load_student_records(DATA_FILE)
        
        # State tracking variable for update operations
        self.selected_uid = None
        
        # Build UI layout
        self.create_header()
        self.create_main_content()
        self.create_status_bar()
        
        # Populate table on startup
        self.refresh_table(self.records)
        self.update_statistics_display()

    def apply_theme_styles(self):
        """Configures clean, professional TTK styles and color palette."""
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Color definitions
        self.NAVY_DARK = "#0f172a"
        self.NAVY_BLUE = "#1e3a8a"
        self.PRIMARY_BLUE = "#2563eb"
        self.ACCENT_CYAN = "#0284c7"
        self.LIGHT_BG = "#f8fafc"
        self.CARD_BG = "#ffffff"
        self.SUCCESS_GREEN = "#16a34a"
        self.DANGER_RED = "#dc2626"
        self.TEXT_MAIN = "#1e293b"
        self.BORDER_COLOR = "#cbd5e1"
        
        self.root.configure(bg=self.LIGHT_BG)
        
        # Treeview styling
        self.style.configure("Treeview.Heading",
                             font=("Segoe UI", 10, "bold"),
                             background="#e2e8f0",
                             foreground=self.NAVY_DARK,
                             relief="flat",
                             padding=5)
        self.style.configure("Treeview",
                             font=("Segoe UI", 9),
                             rowheight=26,
                             background="#ffffff",
                             fieldbackground="#ffffff")
        self.style.map("Treeview",
                       background=[("selected", "#dbeafe")],
                       foreground=[("selected", "#1e3a8a")])

    def create_header(self):
        """Builds top banner containing project, student, and course credentials."""
        header_frame = tk.Frame(self.root, bg=self.NAVY_DARK, padx=20, pady=12)
        header_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Left side: Title and subtitle
        title_box = tk.Frame(header_frame, bg=self.NAVY_DARK)
        title_box.pack(side=tk.LEFT)
        
        title_label = tk.Label(
            title_box,
            text="🎓 Student Performance & Result Management System",
            font=("Segoe UI", 16, "bold"),
            fg="#ffffff",
            bg=self.NAVY_DARK
        )
        title_label.pack(anchor="w")
        
        subtitle_label = tk.Label(
            title_box,
            text="MCA General | Semester 1 | Python Programming Lab Project",
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg=self.NAVY_DARK
        )
        subtitle_label.pack(anchor="w")
        
        # Right side: Student credentials badge
        student_badge = tk.Frame(header_frame, bg="#1e293b", padx=12, pady=6,
                                 highlightbackground="#334155", highlightthickness=1)
        student_badge.pack(side=tk.RIGHT)
        
        badge_name = tk.Label(
            student_badge,
            text="Developer: Shivani",
            font=("Segoe UI", 10, "bold"),
            fg="#38bdf8",
            bg="#1e293b"
        )
        badge_name.pack(anchor="e")
        
        badge_details = tk.Label(
            student_badge,
            text="UID: 26MCA20231  |  Section: 4-A",
            font=("Segoe UI", 8),
            fg="#cbd5e1",
            bg="#1e293b"
        )
        badge_details.pack(anchor="e")

    def create_main_content(self):
        """Constructs dual-pane layout: Data Entry (Left) & Records/Analytics (Right)."""
        main_container = tk.Frame(self.root, bg=self.LIGHT_BG, padx=12, pady=10)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left Pane: Input Form
        self.left_pane = tk.LabelFrame(
            main_container,
            text=" Student Details & Subject Marks ",
            font=("Segoe UI", 11, "bold"),
            bg=self.CARD_BG,
            fg=self.NAVY_DARK,
            padx=14,
            pady=10,
            relief=tk.GROOVE,
            bd=1
        )
        self.left_pane.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        self.build_form_inputs()
        self.build_form_buttons()
        
        # Right Pane: Search, Table, Statistics, and Report Actions
        self.right_pane = tk.Frame(main_container, bg=self.LIGHT_BG)
        self.right_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.build_search_bar()
        self.build_table_view()
        self.build_analytics_cards()

    def build_form_inputs(self):
        """Creates labelled entry fields for demographic data and 5 subjects."""
        # Section A: Student Metadata
        meta_frame = tk.Frame(self.left_pane, bg=self.CARD_BG)
        meta_frame.pack(fill=tk.X, pady=(0, 8))
        
        # UID
        tk.Label(meta_frame, text="Student UID *", font=("Segoe UI", 9, "bold"),
                 bg=self.CARD_BG, fg=self.TEXT_MAIN).grid(row=0, column=0, sticky="w", pady=3)
        self.entry_uid = ttk.Entry(meta_frame, width=24, font=("Segoe UI", 9))
        self.entry_uid.grid(row=0, column=1, sticky="w", padx=6, pady=3)
        
        # Name
        tk.Label(meta_frame, text="Full Name *", font=("Segoe UI", 9, "bold"),
                 bg=self.CARD_BG, fg=self.TEXT_MAIN).grid(row=1, column=0, sticky="w", pady=3)
        self.entry_name = ttk.Entry(meta_frame, width=24, font=("Segoe UI", 9))
        self.entry_name.grid(row=1, column=1, sticky="w", padx=6, pady=3)
        
        # Section & Semester (Side by Side)
        tk.Label(meta_frame, text="Section", font=("Segoe UI", 9, "bold"),
                 bg=self.CARD_BG, fg=self.TEXT_MAIN).grid(row=2, column=0, sticky="w", pady=3)
        self.entry_section = ttk.Entry(meta_frame, width=24, font=("Segoe UI", 9))
        self.entry_section.grid(row=2, column=1, sticky="w", padx=6, pady=3)
        self.entry_section.insert(0, "4-A")
        
        tk.Label(meta_frame, text="Semester", font=("Segoe UI", 9, "bold"),
                 bg=self.CARD_BG, fg=self.TEXT_MAIN).grid(row=3, column=0, sticky="w", pady=3)
        self.entry_semester = ttk.Entry(meta_frame, width=24, font=("Segoe UI", 9))
        self.entry_semester.grid(row=3, column=1, sticky="w", padx=6, pady=3)
        self.entry_semester.insert(0, "1")
        
        # Separator line
        ttk.Separator(self.left_pane, orient="horizontal").pack(fill=tk.X, pady=8)
        
        # Section B: Subject Marks (5 Subjects out of 100)
        marks_title = tk.Label(
            self.left_pane,
            text="Subject Marks (Out of 100 Each, Pass ≥ 40):",
            font=("Segoe UI", 9, "bold"),
            bg=self.CARD_BG,
            fg=self.PRIMARY_BLUE
        )
        marks_title.pack(anchor="w", pady=(0, 6))
        
        marks_frame = tk.Frame(self.left_pane, bg=self.CARD_BG)
        marks_frame.pack(fill=tk.X)
        
        self.subject_entries = {}
        for idx, subject in enumerate(SUBJECTS):
            lbl = tk.Label(marks_frame, text=f"{subject}:", font=("Segoe UI", 8),
                           bg=self.CARD_BG, fg=self.TEXT_MAIN)
            lbl.grid(row=idx, column=0, sticky="w", pady=2)
            
            ent = ttk.Entry(marks_frame, width=10, font=("Segoe UI", 9))
            ent.grid(row=idx, column=1, sticky="e", padx=(10, 0), pady=2)
            self.subject_entries[subject] = ent
            
        # Separator line
        ttk.Separator(self.left_pane, orient="horizontal").pack(fill=tk.X, pady=8)
        
        # Section C: Calculated Readout Preview
        calc_box = tk.LabelFrame(self.left_pane, text=" Quick Calculation Preview ",
                                 font=("Segoe UI", 8, "bold"), bg="#f1f5f9", fg="#475569")
        calc_box.pack(fill=tk.X, pady=(0, 8), padx=2)
        
        self.lbl_preview_total = tk.Label(calc_box, text="Total: -- / 500",
                                          font=("Segoe UI", 9), bg="#f1f5f9", fg=self.TEXT_MAIN)
        self.lbl_preview_total.grid(row=0, column=0, sticky="w", padx=6, pady=2)
        
        self.lbl_preview_pct = tk.Label(calc_box, text="Percentage: -- %",
                                        font=("Segoe UI", 9), bg="#f1f5f9", fg=self.TEXT_MAIN)
        self.lbl_preview_pct.grid(row=0, column=1, sticky="w", padx=6, pady=2)
        
        self.lbl_preview_grade = tk.Label(calc_box, text="Grade: --",
                                          font=("Segoe UI", 9, "bold"), bg="#f1f5f9", fg=self.PRIMARY_BLUE)
        self.lbl_preview_grade.grid(row=1, column=0, sticky="w", padx=6, pady=2)
        
        self.lbl_preview_result = tk.Label(calc_box, text="Result: --",
                                           font=("Segoe UI", 9, "bold"), bg="#f1f5f9", fg="#64748b")
        self.lbl_preview_result.grid(row=1, column=1, sticky="w", padx=6, pady=2)

    def build_form_buttons(self):
        """Creates CRUD operational buttons with clear color coding."""
        btn_frame = tk.Frame(self.left_pane, bg=self.CARD_BG)
        btn_frame.pack(fill=tk.X, pady=4)
        
        # Row 1: Calculate & Add
        btn_calc = tk.Button(
            btn_frame, text="⚡ Calculate", font=("Segoe UI", 9, "bold"),
            bg="#f8fafc", fg=self.PRIMARY_BLUE, relief=tk.RAISED, bd=1,
            cursor="hand2", padx=8, pady=4, command=self.on_calculate_preview
        )
        btn_calc.grid(row=0, column=0, padx=2, pady=3, sticky="ew")
        
        btn_add = tk.Button(
            btn_frame, text="➕ Add Student", font=("Segoe UI", 9, "bold"),
            bg=self.SUCCESS_GREEN, fg="#ffffff", relief=tk.RAISED, bd=1,
            cursor="hand2", padx=8, pady=4, command=self.on_add_student
        )
        btn_add.grid(row=0, column=1, padx=2, pady=3, sticky="ew")
        
        # Row 2: Update & Delete
        btn_update = tk.Button(
            btn_frame, text="✏️ Update", font=("Segoe UI", 9, "bold"),
            bg=self.ACCENT_CYAN, fg="#ffffff", relief=tk.RAISED, bd=1,
            cursor="hand2", padx=8, pady=4, command=self.on_update_student
        )
        btn_update.grid(row=1, column=0, padx=2, pady=3, sticky="ew")
        
        btn_delete = tk.Button(
            btn_frame, text="🗑️ Delete", font=("Segoe UI", 9, "bold"),
            bg=self.DANGER_RED, fg="#ffffff", relief=tk.RAISED, bd=1,
            cursor="hand2", padx=8, pady=4, command=self.on_delete_student
        )
        btn_delete.grid(row=1, column=1, padx=2, pady=3, sticky="ew")
        
        # Row 3: Clear Form & Generate Marksheet
        btn_clear = tk.Button(
            btn_frame, text="🧹 Clear Fields", font=("Segoe UI", 9),
            bg="#e2e8f0", fg=self.TEXT_MAIN, relief=tk.RAISED, bd=1,
            cursor="hand2", padx=8, pady=4, command=self.clear_form
        )
        btn_clear.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        
        btn_report = tk.Button(
            btn_frame, text="📄 View Marksheet", font=("Segoe UI", 9, "bold"),
            bg=self.NAVY_BLUE, fg="#ffffff", relief=tk.RAISED, bd=1,
            cursor="hand2", padx=8, pady=4, command=self.on_view_marksheet
        )
        btn_report.grid(row=2, column=1, padx=2, pady=3, sticky="ew")
        
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)

    def build_search_bar(self):
        """Builds top search/filter controls in the right pane."""
        search_card = tk.Frame(self.right_pane, bg=self.CARD_BG, padx=10, pady=8,
                               highlightbackground=self.BORDER_COLOR, highlightthickness=1)
        search_card.pack(fill=tk.X, pady=(0, 8))
        
        tk.Label(search_card, text="🔍 Search Student:", font=("Segoe UI", 9, "bold"),
                 bg=self.CARD_BG, fg=self.TEXT_MAIN).pack(side=tk.LEFT, padx=(0, 6))
        
        self.entry_search = ttk.Entry(search_card, width=28, font=("Segoe UI", 9))
        self.entry_search.pack(side=tk.LEFT, padx=(0, 8))
        self.entry_search.bind("<Return>", lambda event: self.on_search_student())
        
        btn_search = tk.Button(
            search_card, text="Search (UID/Name)", font=("Segoe UI", 8, "bold"),
            bg="#e0f2fe", fg=self.PRIMARY_BLUE, relief=tk.GROOVE, padx=8, pady=2,
            cursor="hand2", command=self.on_search_student
        )
        btn_search.pack(side=tk.LEFT, padx=3)
        
        btn_reset = tk.Button(
            search_card, text="Show All", font=("Segoe UI", 8),
            bg="#f1f5f9", fg=self.TEXT_MAIN, relief=tk.GROOVE, padx=8, pady=2,
            cursor="hand2", command=self.on_show_all
        )
        btn_reset.pack(side=tk.LEFT, padx=3)
        
        # Batch actions on right
        btn_export = tk.Button(
            search_card, text="💾 Export Report (.txt)", font=("Segoe UI", 8, "bold"),
            bg="#dcfce7", fg=self.SUCCESS_GREEN, relief=tk.GROOVE, padx=8, pady=2,
            cursor="hand2", command=self.on_export_class_report
        )
        btn_export.pack(side=tk.RIGHT, padx=3)

    def build_table_view(self):
        """Constructs modern Treeview table displaying records with scrollbars."""
        table_container = tk.Frame(self.right_pane, bg=self.CARD_BG,
                                   highlightbackground=self.BORDER_COLOR, highlightthickness=1)
        table_container.pack(fill=tk.BOTH, expand=True)
        
        # Table Columns
        columns = ("uid", "name", "section", "semester", "total", "percentage", "grade", "result")
        self.tree = ttk.Treeview(table_container, columns=columns, show="headings", selectmode="browse")
        
        # Heading titles & column alignments
        headers = [
            ("uid", "UID", 110, "center"),
            ("name", "Student Name", 160, "w"),
            ("section", "Sec", 60, "center"),
            ("semester", "Sem", 55, "center"),
            ("total", "Total (/500)", 95, "center"),
            ("percentage", "Percentage", 95, "center"),
            ("grade", "Grade", 70, "center"),
            ("result", "Result", 80, "center")
        ]
        
        for col_id, title, width, align in headers:
            self.tree.heading(col_id, text=title)
            self.tree.column(col_id, width=width, anchor=align)
            
        # Scrollbars
        vsb = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(table_container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Grid placement
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        table_container.grid_rowconfigure(0, weight=1)
        table_container.grid_columnconfigure(0, weight=1)
        
        # Event binding: click on row populates the left input form
        self.tree.bind("<<TreeviewSelect>>", self.on_table_row_select)

    def build_analytics_cards(self):
        """Displays real-time summary statistics cards at the bottom right."""
        self.stats_frame = tk.Frame(self.right_pane, bg=self.LIGHT_BG, pady=6)
        self.stats_frame.pack(fill=tk.X)
        
        # Define 4 KPI cards
        self.card_total = self._create_kpi_card(self.stats_frame, "Total Enrolled", "0", "#0284c7")
        self.card_passed = self._create_kpi_card(self.stats_frame, "Passed Students", "0", "#16a34a")
        self.card_failed = self._create_kpi_card(self.stats_frame, "Failed Students", "0", "#dc2626")
        self.card_avg = self._create_kpi_card(self.stats_frame, "Class Average", "0.0%", "#7c3aed")
        
        self.card_total.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))
        self.card_passed.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=4)
        self.card_failed.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=4)
        self.card_avg.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(4, 0))

    def _create_kpi_card(self, parent, title, initial_value, color):
        """Helper to create KPI metric box."""
        card = tk.Frame(parent, bg=self.CARD_BG, padx=8, pady=6,
                        highlightbackground=self.BORDER_COLOR, highlightthickness=1)
        
        lbl_title = tk.Label(card, text=title, font=("Segoe UI", 8), bg=self.CARD_BG, fg="#64748b")
        lbl_title.pack(anchor="w")
        
        lbl_val = tk.Label(card, text=initial_value, font=("Segoe UI", 12, "bold"),
                           bg=self.CARD_BG, fg=color)
        lbl_val.pack(anchor="w")
        
        card.value_label = lbl_val  # Attach reference for easy update
        return card

    def create_status_bar(self):
        """Creates bottom status bar with operational feedback."""
        self.status_bar = tk.Label(
            self.root,
            text="Ready. System initialized with JSON storage. Developed by Shivani (26MCA20231).",
            font=("Segoe UI", 8),
            bd=1,
            relief=tk.SUNKEN,
            anchor="w",
            bg="#f1f5f9",
            fg="#475569",
            padx=10,
            pady=3
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_status(self, message):
        """Updates the status bar label."""
        self.status_bar.config(text=message)

    # ==================================================================================
    # FORM INPUT VALIDATION & EXTRACTION (Syllabus: Operators, Conditionals, Types)
    # ==================================================================================
    
    def extract_and_validate_inputs(self):
        """
        Validates all user entries from GUI.
        Demonstrates:
          - String methods: strip(), replace()
          - Membership testing 'not in'
          - Type conversion to float
          - Conditional range checking (0 <= mark <= 100)
          - Error handling via early returns
        """
        uid = self.entry_uid.get().strip().upper()
        name = self.entry_name.get().strip()
        section = self.entry_section.get().strip().upper()
        semester = self.entry_semester.get().strip()
        
        # Validation 1: UID non-empty
        if not uid:
            messagebox.showerror("Validation Error", "Student UID is mandatory. Please enter a valid UID.")
            self.entry_uid.focus_set()
            return None
            
        # Validation 2: Name non-empty and alphabetic characters/spaces
        if not name:
            messagebox.showerror("Validation Error", "Student Name cannot be blank.")
            self.entry_name.focus_set()
            return None
            
        # Check if name contains valid characters (letters and spaces only)
        # Syllabus: 'for' loop and 'not in' membership operator
        is_valid_name = True
        for char in name:
            if not (char.isalpha() or char.isspace()):
                is_valid_name = False
                break
        if not is_valid_name:
            messagebox.showerror("Validation Error", "Name should only contain alphabetic letters and spaces.")
            self.entry_name.focus_set()
            return None

        # Validation 3: Subject Marks verification
        marks_dict = {}
        for subject, entry_widget in self.subject_entries.items():
            raw_val = entry_widget.get().strip()
            if not raw_val:
                messagebox.showerror("Validation Error", f"Marks for '{subject}' cannot be blank.")
                entry_widget.focus_set()
                return None
            
            try:
                mark_float = float(raw_val)
            except ValueError:
                messagebox.showerror("Validation Error", f"Marks for '{subject}' must be a valid number.")
                entry_widget.focus_set()
                return None
                
            # Range check: marks must be between 0 and 100
            if mark_float < 0.0 or mark_float > 100.0:  # Syllabus: Logical 'or' & comparison
                messagebox.showerror("Validation Error",
                                     f"Marks for '{subject}' must be between 0 and 100. Entered: {mark_float}")
                entry_widget.focus_set()
                return None
                
            marks_dict[subject] = round(mark_float, 2)
            
        return {
            "uid": uid,
            "name": name,
            "section": section if section else "4-A",
            "semester": semester if semester else "1",
            "marks": marks_dict
        }

    # ==================================================================================
    # GUI ACTION HANDLERS (Syllabus: Event-driven logic & CRUD operations)
    # ==================================================================================

    def on_calculate_preview(self):
        """Performs calculation and updates the quick preview box without saving."""
        data = self.extract_and_validate_inputs()
        if not data:
            return
            
        marks_values = list(data["marks"].values())
        total = calculate_total_marks(marks_values)
        percentage = calculate_percentage(total)
        is_passed, failed_subs = evaluate_pass_fail(data["marks"])
        grade = determine_grade(percentage, is_passed)
        result_text = "PASS" if is_passed else "FAIL"
        
        self.lbl_preview_total.config(text=f"Total: {total} / 500")
        self.lbl_preview_pct.config(text=f"Percentage: {percentage}%")
        self.lbl_preview_grade.config(text=f"Grade: {grade}")
        
        res_color = self.SUCCESS_GREEN if is_passed else self.DANGER_RED
        self.lbl_preview_result.config(text=f"Result: {result_text}", fg=res_color)
        
        self.set_status(f"Calculated: Total={total}, Percentage={percentage}%, Grade={grade}, Result={result_text}")

    def on_add_student(self):
        """Adds a new student record after duplicate checks and calculations."""
        data = self.extract_and_validate_inputs()
        if not data:
            return
            
        target_uid = data["uid"]
        
        # Check if student already exists using linear search
        existing_student, _ = linear_search_student(self.records, target_uid)
        if existing_student is not None:
            messagebox.showerror("Duplicate Record",
                                 f"Student with UID '{target_uid}' already exists in the system!")
            return
            
        # Calculate academic performance metrics
        marks_values = list(data["marks"].values())
        total = calculate_total_marks(marks_values)
        percentage = calculate_percentage(total)
        is_passed, _ = evaluate_pass_fail(data["marks"])
        grade = determine_grade(percentage, is_passed)
        result = "PASS" if is_passed else "FAIL"
        
        # Construct record dictionary (Syllabus: Dictionary creation)
        new_record = {
            "uid": target_uid,
            "name": data["name"],
            "section": data["section"],
            "semester": data["semester"],
            "marks": data["marks"],
            "total": total,
            "percentage": percentage,
            "grade": grade,
            "result": result
        }
        
        # Append to record list and save to JSON
        self.records.append(new_record)
        save_student_records(self.records, DATA_FILE)
        
        # Refresh views
        self.refresh_table(self.records)
        self.update_statistics_display()
        self.clear_form()
        
        messagebox.showinfo("Success", f"Student '{target_uid} - {data['name']}' added successfully!")
        self.set_status(f"Student record {target_uid} saved to database.")

    def on_update_student(self):
        """Updates the currently selected student's marks and details."""
        if not self.selected_uid:
            messagebox.showwarning("Selection Required", "Please select a student from the table to update.")
            return
            
        data = self.extract_and_validate_inputs()
        if not data:
            return
            
        # Locate the record to update
        _, index = linear_search_student(self.records, self.selected_uid)
        if index == -1:
            messagebox.showerror("Error", f"Student with UID '{self.selected_uid}' not found.")
            return
            
        # Calculate new metrics
        marks_values = list(data["marks"].values())
        total = calculate_total_marks(marks_values)
        percentage = calculate_percentage(total)
        is_passed, _ = evaluate_pass_fail(data["marks"])
        grade = determine_grade(percentage, is_passed)
        result = "PASS" if is_passed else "FAIL"
        
        # Update record attributes
        self.records[index] = {
            "uid": data["uid"],
            "name": data["name"],
            "section": data["section"],
            "semester": data["semester"],
            "marks": data["marks"],
            "total": total,
            "percentage": percentage,
            "grade": grade,
            "result": result
        }
        
        save_student_records(self.records, DATA_FILE)
        self.refresh_table(self.records)
        self.update_statistics_display()
        
        messagebox.showinfo("Updated", f"Student record '{data['uid']}' successfully updated!")
        self.set_status(f"Student {data['uid']} record updated.")

    def on_delete_student(self):
        """Deletes the selected student record with confirmation."""
        if not self.selected_uid:
            messagebox.showwarning("Selection Required", "Please select a student from the table to delete.")
            return
            
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to permanently delete record for UID: {self.selected_uid}?"
        )
        if not confirm:
            return
            
        _, index = linear_search_student(self.records, self.selected_uid)
        if index != -1:
            del self.records[index]  # Syllabus: List deletion operator
            save_student_records(self.records, DATA_FILE)
            self.refresh_table(self.records)
            self.update_statistics_display()
            self.clear_form()
            messagebox.showinfo("Deleted", f"Record for UID '{self.selected_uid}' deleted.")
            self.set_status(f"Deleted student record {self.selected_uid}.")

    def on_table_row_select(self, event):
        """Populates form fields when user clicks on a table row."""
        selected_items = self.tree.selection()
        if not selected_items:
            return
            
        item_id = selected_items[0]
        row_values = self.tree.item(item_id, "values")
        if not row_values:
            return
            
        uid = row_values[0]
        student, _ = linear_search_student(self.records, uid)
        if not student:
            return
            
        self.selected_uid = student["uid"]
        
        # Populate text entries
        self.entry_uid.delete(0, tk.END)
        self.entry_uid.insert(0, student["uid"])
        
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, student["name"])
        
        self.entry_section.delete(0, tk.END)
        self.entry_section.insert(0, student.get("section", "4-A"))
        
        self.entry_semester.delete(0, tk.END)
        self.entry_semester.insert(0, student.get("semester", "1"))
        
        # Populate marks entries
        student_marks = student.get("marks", {})
        for subject, entry_widget in self.subject_entries.items():
            entry_widget.delete(0, tk.END)
            val = student_marks.get(subject, 0.0)
            entry_widget.insert(0, str(val))
            
        # Update preview readout
        self.lbl_preview_total.config(text=f"Total: {student['total']} / 500")
        self.lbl_preview_pct.config(text=f"Percentage: {student['percentage']}%")
        self.lbl_preview_grade.config(text=f"Grade: {student['grade']}")
        
        res_color = self.SUCCESS_GREEN if student["result"] == "PASS" else self.DANGER_RED
        self.lbl_preview_result.config(text=f"Result: {student['result']}", fg=res_color)
        
        self.set_status(f"Loaded student details for {student['name']} ({student['uid']}).")

    def on_search_student(self):
        """Executes search query and filters table records."""
        query = self.entry_search.get()
        if not query.strip():
            self.refresh_table(self.records)
            return
            
        results = filter_students_by_query(self.records, query)
        self.refresh_table(results)
        self.set_status(f"Search query '{query}' matched {len(results)} student(s).")

    def on_show_all(self):
        """Clears search filter and displays all records."""
        self.entry_search.delete(0, tk.END)
        self.refresh_table(self.records)
        self.set_status(f"Displaying all {len(self.records)} enrolled student records.")

    def clear_form(self):
        """Resets all input fields and preview readouts."""
        self.selected_uid = None
        self.entry_uid.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_section.delete(0, tk.END)
        self.entry_section.insert(0, "4-A")
        self.entry_semester.delete(0, tk.END)
        self.entry_semester.insert(0, "1")
        
        for entry_widget in self.subject_entries.values():
            entry_widget.delete(0, tk.END)
            
        self.lbl_preview_total.config(text="Total: -- / 500")
        self.lbl_preview_pct.config(text="Percentage: -- %")
        self.lbl_preview_grade.config(text="Grade: --")
        self.lbl_preview_result.config(text="Result: --", fg="#64748b")
        
        # Deselect any selected row in table
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection())
            
        self.set_status("Form cleared. Ready for new input.")

    def refresh_table(self, dataset):
        """Clears and re-populates the Treeview table with records."""
        # Remove existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Insert rows from dataset (Syllabus: 'for' loop)
        for student in dataset:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    student["uid"],
                    student["name"],
                    student.get("section", "4-A"),
                    student.get("semester", "1"),
                    f"{student['total']:.2f}",
                    f"{student['percentage']:.2f}%",
                    student["grade"],
                    student["result"]
                )
            )

    def update_statistics_display(self):
        """Recalculates and refreshes the KPI analytics cards."""
        stats = compute_class_statistics(self.records)
        self.card_total.value_label.config(text=str(stats["total_students"]))
        self.card_passed.value_label.config(text=str(stats["pass_count"]))
        self.card_failed.value_label.config(text=str(stats["fail_count"]))
        self.card_avg.value_label.config(text=f"{stats['class_average']:.1f}%")

    # ==================================================================================
    # REPORTING & MARKSHEET GENERATION (Syllabus: Formatted Strings & Presentation)
    # ==================================================================================

    def on_view_marksheet(self):
        """Opens an attractive popup displaying the formal Marksheet for selected student."""
        selected_items = self.tree.selection()
        if not selected_items and not self.selected_uid:
            messagebox.showwarning("Select Student", "Please select a student from the table to view Marksheet.")
            return
            
        uid = self.selected_uid
        if not uid and selected_items:
            uid = self.tree.item(selected_items[0], "values")[0]
            
        student, _ = linear_search_student(self.records, uid)
        if not student:
            messagebox.showerror("Error", "Student record not found.")
            return
            
        self.show_marksheet_dialog(student)

    def show_marksheet_dialog(self, student):
        """Displays modal dialog containing official formatted result card."""
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Official Marksheet - {student['name']} ({student['uid']})")
        dialog.geometry("620x650")
        dialog.resizable(False, False)
        dialog.configure(bg="#f8fafc")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Build formatted ASCII marksheet string
        marksheet_text = self.generate_formatted_marksheet_text(student)
        
        # Header banner
        header = tk.Frame(dialog, bg=self.NAVY_DARK, padx=15, pady=10)
        header.pack(fill=tk.X)
        tk.Label(header, text="INSTITUTE OF COMPUTER APPLICATIONS",
                 font=("Segoe UI", 12, "bold"), fg="#ffffff", bg=self.NAVY_DARK).pack()
        tk.Label(header, text="MCA Semester 1 - Grade Card / Academic Transcript",
                 font=("Segoe UI", 9), fg="#94a3b8", bg=self.NAVY_DARK).pack()
                 
        # Text display area
        text_frame = tk.Frame(dialog, padx=12, pady=10, bg="#f8fafc")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        txt = tk.Text(text_frame, font=("Courier New", 9), wrap="none", bg="#ffffff",
                      fg="#0f172a", bd=1, relief=tk.SOLID, padx=10, pady=10)
        txt.insert("1.0", marksheet_text)
        txt.config(state="disabled")  # Read-only
        txt.pack(fill=tk.BOTH, expand=True)
        
        # Action Buttons
        btn_box = tk.Frame(dialog, bg="#f8fafc", pady=10)
        btn_box.pack(fill=tk.X)
        
        btn_save = tk.Button(
            btn_box, text="💾 Save to File", font=("Segoe UI", 9, "bold"),
            bg=self.PRIMARY_BLUE, fg="#ffffff", padx=12, pady=4, cursor="hand2",
            command=lambda: self.save_marksheet_to_file(student, marksheet_text)
        )
        btn_save.pack(side=tk.LEFT, padx=(20, 10))
        
        btn_close = tk.Button(
            btn_box, text="Close", font=("Segoe UI", 9),
            bg="#e2e8f0", fg=self.TEXT_MAIN, padx=12, pady=4, cursor="hand2",
            command=dialog.destroy
        )
        btn_close.pack(side=tk.RIGHT, padx=20)

    def generate_formatted_marksheet_text(self, student):
        """
        Creates clean, fixed-width formatted academic transcript.
        Demonstrates:
          - String formatting with f-strings
          - Fixed column widths for alignment
          - Loops for tabular rows
        """
        border_line = "=" * 64
        sep_line = "-" * 64
        
        lines = [
            border_line,
            "               MASTER OF COMPUTER APPLICATIONS (MCA)            ",
            "                  SEMESTER 1 EXAMINATION REPORT                 ",
            border_line,
            f"  Student Name : {student['name']:<24} UID     : {student['uid']}",
            f"  Course       : MCA General             Section : {student.get('section', '4-A')}",
            f"  Semester     : 1                       Status  : Regular",
            sep_line,
            f"  {'Subject Name':<32} {'Max':<6} {'Obt':<6} {'Result':<8}",
            sep_line
        ]
        
        # Add each subject row
        for sub_name in SUBJECTS:
            mark = student["marks"].get(sub_name, 0.0)
            status = "PASS" if mark >= PASSING_MARKS else "FAIL"
            lines.append(f"  {sub_name:<32} {100:<6} {mark:<6.1f} {status:<8}")
            
        lines.append(sep_line)
        lines.append(f"  {'TOTAL MARKS (OUT OF 500)':<32} {500:<6} {student['total']:<6.1f}")
        lines.append(f"  {'PERCENTAGE':<32} {student['percentage']:<6.2f}%")
        lines.append(f"  {'FINAL GRADE':<32} {student['grade']}")
        lines.append(f"  {'OVERALL RESULT':<32} {student['result']}")
        lines.append(border_line)
        lines.append("  GRADING SCALE:")
        lines.append("  A+ (90-100) | A (80-89) | B+ (70-79) | B (60-69)")
        lines.append("  C  (50-59)  | D (40-49) | F  (<40 - Fail in subject/overall)")
        lines.append(border_line)
        lines.append("  Verified By: Examination Controller     Date of Issue: 31/10/2026")
        lines.append(border_line)
        
        return "\n".join(lines)

    def save_marksheet_to_file(self, student, text_content):
        """Exports individual marksheet as a .txt file."""
        filename = f"Marksheet_{student['uid']}_{student['name'].replace(' ', '_')}.txt"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile=filename,
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            return
            
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_content)
            messagebox.showinfo("Export Successful", f"Marksheet saved successfully to:\n{file_path}")
        except IOError as error:
            messagebox.showerror("Export Failed", f"Could not save file: {error}")

    def on_export_class_report(self):
        """Exports a complete batch summary report with statistics as a text file."""
        if not self.records:
            messagebox.showwarning("No Data", "No student records available to export.")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="MCA_Sem1_Section4A_Performance_Report.txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            return
            
        stats = compute_class_statistics(self.records)
        border = "=" * 80
        
        report_lines = [
            border,
            "     STUDENT PERFORMANCE & RESULT MANAGEMENT SYSTEM - BATCH REPORT",
            "                  COURSE: MCA GENERAL | SECTION: 4-A",
            border,
            f"Generated on  : 31-Oct-2026",
            f"Prepared By   : Shivani (UID: 26MCA20231)",
            f"Total Students: {stats['total_students']}",
            f"Passed        : {stats['pass_count']} ({stats['pass_percentage']}%)",
            f"Failed        : {stats['fail_count']}",
            f"Class Average : {stats['class_average']}%",
            f"Highest Score : {stats['highest_percentage']}%",
            f"Lowest Score  : {stats['lowest_percentage']}%",
            border,
            "SUBJECT-WISE CLASS AVERAGES:",
        ]
        
        for sub, avg_val in stats["subject_averages"].items():
            report_lines.append(f"  - {sub:<32} : {avg_val:.2f} / 100")
            
        report_lines.append(border)
        report_lines.append(f"{'UID':<14} {'Name':<22} {'Total':<10} {'Percentage':<14} {'Grade':<8} {'Result':<8}")
        report_lines.append("-" * 80)
        
        for st in self.records:
            report_lines.append(
                f"{st['uid']:<14} {st['name']:<22} {st['total']:<10.1f} {st['percentage']:<14.2f} {st['grade']:<8} {st['result']:<8}"
            )
            
        report_lines.append(border)
        report_lines.append("                         *** END OF REPORT ***")
        report_lines.append(border)
        
        try:
            with open(file_path, "w", encoding="utf-8") as report_file:
                report_file.write("\n".join(report_lines))
            messagebox.showinfo("Export Complete", f"Class report exported successfully to:\n{file_path}")
            self.set_status(f"Exported class report to {os.path.basename(file_path)}.")
        except IOError as error:
            messagebox.showerror("Export Failed", f"Unable to write report: {error}")


# ======================================================================================
# MODULE 5: APPLICATION ENTRY POINT (Syllabus: Program Structure & __main__ idiom)
# ======================================================================================

def main():
    """
    Main driver execution point of the program.
    Initializes Tk root window and enters the main event loop.
    """
    root = tk.Tk()
    app = StudentPerformanceApp(root)
    root.mainloop()


if __name__ == "__main__":
    # Syllabus: Standard Python program execution guard
    main()
