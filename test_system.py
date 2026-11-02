"""
Automated Test Verification Script for Student Performance & Result Management System
Tests all syllabus concepts, business logic, calculations, match-case, and data integrity.
"""
import os
import json
from student_management_system import (
    calculate_total_marks,
    calculate_percentage,
    evaluate_pass_fail,
    determine_grade,
    linear_search_student,
    filter_students_by_query,
    compute_class_statistics,
    load_student_records,
    save_student_records,
    SUBJECTS
)

def run_all_tests():
    print("==================================================")
    print("RUNNING AUTOMATED VERIFICATION SUITE")
    print("Student: Shivani (UID: 26MCA20231) | MCA Sem 1")
    print("==================================================")

    # Test 1: Total calculation
    marks = [94.0, 89.0, 86.0, 92.0, 90.0]
    total = calculate_total_marks(marks)
    assert total == 451.0, f"Expected 451.0, got {total}"
    print("[PASS] Test 1: Total marks calculation verified (451.0/500)")

    # Test 2: Percentage calculation
    pct = calculate_percentage(total)
    assert pct == 90.2, f"Expected 90.2, got {pct}"
    print("[PASS] Test 2: Percentage calculation verified (90.2%)")

    # Test 3: Pass/Fail Evaluation
    marks_pass = {
        "Python Programming": 78.0,
        "Data Structures & Algorithms": 72.0,
        "Computer Architecture": 68.0,
        "Discrete Mathematics": 74.0,
        "Operating Systems": 70.0
    }
    is_p, failed_subs = evaluate_pass_fail(marks_pass)
    assert is_p is True and len(failed_subs) == 0, "Expected all pass"
    print("[PASS] Test 3a: All subjects pass check verified")

    marks_fail = {
        "Python Programming": 65.0,
        "Data Structures & Algorithms": 34.0, # < 40 Fail
        "Computer Architecture": 58.0,
        "Discrete Mathematics": 62.0,
        "Operating Systems": 60.0
    }
    is_p_fail, failed_subs_fail = evaluate_pass_fail(marks_fail)
    assert is_p_fail is False and "Data Structures & Algorithms" in failed_subs_fail
    print("[PASS] Test 3b: Single subject failure detected correctly (<40)")

    # Test 4: Grade match-case verification
    assert determine_grade(95.0, True) == "A+"
    assert determine_grade(90.0, True) == "A+"
    assert determine_grade(85.0, True) == "A"
    assert determine_grade(75.0, True) == "B+"
    assert determine_grade(65.0, True) == "B"
    assert determine_grade(55.0, True) == "C"
    assert determine_grade(45.0, True) == "D"
    assert determine_grade(35.0, True) == "F"
    assert determine_grade(85.0, False) == "F" # Failed a subject despite 85% avg
    print("[PASS] Test 4: Match-case grade determination across all tiers verified")

    # Test 5: Linear search with while loop and break
    dummy_records = [
        {"uid": "26MCA20231", "name": "Shivani", "percentage": 90.2, "result": "PASS", "marks": marks_pass},
        {"uid": "26MCA20202", "name": "Aman Sharma", "percentage": 72.4, "result": "PASS", "marks": marks_pass},
        {"uid": "26MCA20219", "name": "Sneha Gupta", "percentage": 55.8, "result": "FAIL", "marks": marks_fail}
    ]
    student, idx = linear_search_student(dummy_records, "26MCA20231")
    assert student is not None and idx == 0 and student["name"] == "Shivani"
    print("[PASS] Test 5: Linear search (while loop + break) verified")

    # Test 6: Filter records with for loop and continue
    filtered = filter_students_by_query(dummy_records, "aman")
    assert len(filtered) == 1 and filtered[0]["uid"] == "26MCA20202"
    print("[PASS] Test 6: Filter records (for loop + continue) verified")

    # Test 7: Class statistics
    stats = compute_class_statistics(dummy_records)
    assert stats["total_students"] == 3
    assert stats["pass_count"] == 2
    assert stats["fail_count"] == 1
    assert stats["highest_percentage"] == 90.2
    print("[PASS] Test 7: Class statistics computation verified")

    # Test 8: Data loading and initial sample generation
    records = load_student_records("test_data.json")
    assert len(records) >= 5, "Expected at least 5 sample records"
    assert os.path.exists("test_data.json")
    # Clean up test file
    os.remove("test_data.json")
    print("[PASS] Test 8: Data persistence and initial seed file verified")

    print("==================================================")
    print("ALL 8 VERIFICATION TESTS PASSED SUCCESSFULLY! [OK]")
    print("==================================================")

if __name__ == "__main__":
    run_all_tests()
