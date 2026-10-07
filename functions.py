"""
Student Performance Analysis System - Helper Functions
This module contains utility functions for calculating student grades,
pass/fail results, and performance categories based on academic marks.
"""

def calculate_grade(marks):
    """
    Calculates letter grade based on marks obtained.
    
    Grade Rules:
    90 - 100 : A+
    80 - 89  : A
    70 - 79  : B
    60 - 69  : C
    50 - 59  : D
    Below 50 : F
    """
    try:
        marks = float(marks)
        if marks >= 90:
            return 'A+'
        elif marks >= 80:
            return 'A'
        elif marks >= 70:
            return 'B'
        elif marks >= 60:
            return 'C'
        elif marks >= 50:
            return 'D'
        else:
            return 'F'
    except (ValueError, TypeError):
        return 'N/A'


def pass_fail(marks):
    """
    Determines pass/fail status based on marks.
    
    Rules:
    Marks >= 40 : Pass
    Marks < 40  : Fail
    """
    try:
        marks = float(marks)
        if marks >= 40:
            return 'Pass'
        else:
            return 'Fail'
    except (ValueError, TypeError):
        return 'N/A'


def performance_category(marks):
    """
    Categorizes overall student performance.
    
    Rules:
    80 - 100 : Excellent
    60 - 79  : Good
    40 - 59  : Average
    Below 40 : Poor
    """
    try:
        marks = float(marks)
        if marks >= 80:
            return 'Excellent'
        elif marks >= 60:
            return 'Good'
        elif marks >= 40:
            return 'Average'
        else:
            return 'Poor'
    except (ValueError, TypeError):
        return 'N/A'
