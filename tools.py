import os

COURSES = {
    1: [("MS-251", "Probability & Statistics", 3.0), ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0), ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5), ("GE-190", "Functional English", 3.0)],
    2: [("CC-112", "Programming Fundamentals", 3.0), ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0), ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0), ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0), ("HQ-002", "Quran Translation - II", 0.5)],
    3: [("CC-211", "Object Oriented Programming", 3.0), ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0), ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0), ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5)],
    4: [("CC-213", "Data Structures", 3.0), ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0), ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0), ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5)],
    5: [("CC-313", "Analysis of Algorithms", 3.0), ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0), ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0), ("HQ-005", "Quran Translation - V", 0.5)],
    6: [("CC-311", "Operating Systems", 3.0), ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0), ("HQ-006", "Quran Translation - VI", 0.5)],
    7: [("CC-411", "Final Year Project - I", 2.0), ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0), ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0), ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0), ("HQ-007", "Quran Translation - VII", 0.5)],
    8: [("CC-412", "Final Year Project - II", 4.0), ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0), ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0), ("HQ-008", "Quran Translation - VIII", 0.5)],
}

GRADE_SCALE = [(85, 4.0), (80, 3.7), (75, 3.3), (70, 3.0), (65, 2.7),
               (61, 2.3), (58, 2.0), (55, 1.7), (50, 1.0)]


def marks_to_grade_points(marks: int) -> float | str:
    """Use when marks need to be converted into PUCIT grade points.

    Args:
        marks: Marks obtained, from 0 to 100.
    """
    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"
    for cutoff, points in GRADE_SCALE:
        if marks >= cutoff:
            return points
    return 0.0


def calculate_semester_gpa(grade_points: list[float], credit_hours: list[float]) -> float | str:
    """Use when the semester GPA needs to be calculated from grade points and credit hours.

    Args:
        grade_points: Grade points of each course.
        credit_hours: Credit hours of each course, same order and length as grade_points.
    """
    if len(grade_points) != len(credit_hours):
        return "Error: grade points and credit hours must have the same length"
    if len(grade_points) == 0:
        return "Error: lists cannot be empty"
    if any(ch <= 0 for ch in credit_hours):
        return "Error: credit hours must be greater than 0"
    total_points = sum(g * c for g, c in zip(grade_points, credit_hours))
    return total_points / sum(credit_hours)


def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float,
                       semester_gpa: float, semester_credit_hours: float) -> float | str:
    """Use when a student's CGPA needs to be projected after a semester.

    Args:
        current_cgpa: CGPA before this semester (0-4).
        completed_credit_hours: Credit hours completed before this semester.
        semester_gpa: GPA of the new semester (0-4).
        semester_credit_hours: Credit hours of the new semester.
    """
    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"
    if semester_gpa < 0 or semester_gpa > 4:
        return "Error: semester GPA must be between 0 and 4"
    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"
    if semester_credit_hours <= 0:
        return "Error: semester credit hours must be greater than 0"
    return ((current_cgpa * completed_credit_hours) + (semester_gpa * semester_credit_hours)) / (
        completed_credit_hours + semester_credit_hours)


def required_gpa_for_target(target_cgpa: float, current_cgpa: float,
                            completed_credit_hours: float, remaining_credit_hours: float) -> float | str:
    """Use when a student wants to know the GPA needed to reach a target CGPA.

    Args:
        target_cgpa: Desired final CGPA (0-4).
        current_cgpa: Current CGPA (0-4).
        completed_credit_hours: Credit hours finished so far.
        remaining_credit_hours: Credit hours still to be taken.
    """
    if target_cgpa < 0 or target_cgpa > 4:
        return "Error: target CGPA must be between 0 and 4"
    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"
    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"
    if remaining_credit_hours <= 0:
        return "Error: remaining credit hours must be greater than 0"
    return (target_cgpa * (completed_credit_hours + remaining_credit_hours)
            - current_cgpa * completed_credit_hours) / remaining_credit_hours


def get_semester_courses(semester: int) -> str:
    """Use when a student asks for the courses and credit hours of a semester.

    Args:
        semester: Semester number, 1 to 8.
    """
    if semester < 1 or semester > 8:
        return "Error: semester must be between 1 and 8"
    return "\n".join(f"{code}: {name} - {ch} credit hours" for code, name, ch in COURSES[semester])


def get_remaining_credit_hours(current_semester: int) -> float | str:
    """Use when the remaining graded credit hours from a semester onward are needed.

    Args:
        current_semester: Semester number, 1 to 8. Counting starts from this semester.
    """
    if current_semester < 1 or current_semester > 8:
        return "Error: semester must be between 1 and 8"
    return sum(c[2] for s in range(current_semester, 9) for c in COURSES[s])


def save_report(filename: str, content: str) -> str:
    """Use when the student asks to save a useful GPA, CGPA, or target plan report.

    Args:
        filename: Name of the report file, e.g. report.txt.
        content: Full text of the report.
    """
    try:
        filename = os.path.basename(filename)  # blocks paths like ../../x
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Report saved successfully as {filename}"
    except Exception as e:
        return f"Error: could not save report: {e}"