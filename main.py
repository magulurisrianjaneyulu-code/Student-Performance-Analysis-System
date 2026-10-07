"""
============================================================
        STUDENT PERFORMANCE ANALYSIS SYSTEM
============================================================
import sys
import pandas as pd
import numpy as np
from functions import calculate_grade, pass_fail, performance_category
def main():
    print("=" * 60)
    print("        STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 60)
    print()
    # ------------------------------------------------------
    # STEP 1: READ DATASET WITH ERROR HANDLING
    # ------------------------------------------------------
    csv_filename = "students.csv"
    try:
        df = pd.read_csv(csv_filename)
        print(f"[INFO] Successfully loaded dataset: '{csv_filename}'")
    except FileNotFoundError:
        print(f"[ERROR] The file '{csv_filename}' was not found. Please ensure it exists in the project directory.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"[ERROR] The file '{csv_filename}' is empty. Please provide valid student data.")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while reading '{csv_filename}': {e}")
        sys.exit(1)

    # Validate required columns
    required_columns = ['Student_ID', 'Name', 'Department', 'Subject', 'Marks', 'Attendance']
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        print(f"[ERROR] Missing required column(s) in CSV: {missing_cols}")
        sys.exit(1)

    print()

    # ------------------------------------------------------
    # STEP 2: DISPLAY COMPLETE DATASET
    # ------------------------------------------------------
    print("-" * 60)
    print("COMPLETE STUDENT DATASET")
    print("-" * 60)
    print(df.to_string(index=False))
    print()

    # ------------------------------------------------------
    # STEP 3: DISPLAY TOTAL NUMBER OF STUDENTS
    # ------------------------------------------------------
    print("-" * 60)
    print("TOTAL STUDENTS")
    print("-" * 60)
    total_students = len(df)
    print(f"Total Student Records Processed: {total_students}")
    print()

    # ------------------------------------------------------
    # STEP 4: CHECK AND DISPLAY MISSING VALUES
    # ------------------------------------------------------
    print("-" * 60)
    print("DATA CHECK (MISSING VALUES)")
    print("-" * 60)
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values)
    
    # Fill or clean if any missing numeric values present
    if df['Marks'].isnull().any() or df['Attendance'].isnull().any():
        print("[WARNING] Missing numeric values detected. Filling with median values.")
        df['Marks'] = df['Marks'].fillna(df['Marks'].median())
        df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())

    print()

    # ------------------------------------------------------
    # STEP 5: CALCULATE GRADE, RESULT, AND PERFORMANCE
    # ------------------------------------------------------
    # Apply custom functions from functions.py using Pandas .apply()
    df['Grade'] = df['Marks'].apply(calculate_grade)
    df['Result'] = df['Marks'].apply(pass_fail)
    df['Performance'] = df['Marks'].apply(performance_category)

    # ------------------------------------------------------
    # STEP 6 & 7: OVERALL ANALYSIS USING NUMPY
    # ------------------------------------------------------
    print("-" * 60)
    print("OVERALL ANALYSIS")
    print("-" * 60)

    # Convert DataFrame columns to NumPy arrays for calculations
    marks_array = np.array(df['Marks'], dtype=float)
    attendance_array = np.array(df['Attendance'], dtype=float)

    # Calculate metrics using NumPy functions
    avg_marks = np.mean(marks_array)
    max_marks = np.max(marks_array)
    min_marks = np.min(marks_array)
    avg_attendance = np.mean(attendance_array)

    # Pass / Fail count
    pass_count = (df['Result'] == 'Pass').sum()
    fail_count = (df['Result'] == 'Fail').sum()

    print(f"Average Marks      : {avg_marks:.2f}")
    print(f"Highest Marks      : {max_marks:.2f}")
    print(f"Lowest Marks       : {min_marks:.2f}")
    print(f"Average Attendance : {avg_attendance:.2f}%")
    print(f"Passed Students    : {pass_count}")
    print(f"Failed Students    : {fail_count}")
    print()
    # ------------------------------------------------------
    # STEP 8: GRADE DISTRIBUTION
    # ------------------------------------------------------
    print("-" * 60)
    print("GRADE DISTRIBUTION")
    print("-" * 60)
    grade_counts = df['Grade'].value_counts()
    for grade, count in grade_counts.items():
        print(f"Grade {grade:3s} : {count} student(s)")
    print()
    # ------------------------------------------------------
    # STEP 9: TOP 5 PERFORMING STUDENTS
    # ------------------------------------------------------
    print("-" * 60)
    print("TOP 5 PERFORMING STUDENTS")
    print("-" * 60)
    top_5 = df.sort_values(by='Marks', ascending=False).head(5)
    top_5_display = top_5[['Student_ID', 'Name', 'Department', 'Marks', 'Grade', 'Attendance']]
    print(top_5_display.to_string(index=False))
    print()
    # ------------------------------------------------------
    # STEP 10: SUBJECT-WISE PERFORMANCE ANALYSIS
    # ------------------------------------------------------
    print("-" * 60)
    print("SUBJECT-WISE PERFORMANCE")
    print("-" * 60)
    subject_analysis = df.groupby('Subject').agg(
        Total_Students=('Student_ID', 'count'),
        Average_Marks=('Marks', 'mean'),
        Highest_Marks=('Marks', 'max'),
        Lowest_Marks=('Marks', 'min')
    ).reset_index()
    # Format numeric values for display
    subject_analysis_display = subject_analysis.copy()
    subject_analysis_display['Average_Marks'] = subject_analysis_display['Average_Marks'].round(2)
    print(subject_analysis_display.to_string(index=False))
    print()
    # ------------------------------------------------------
    # STEP 11: DEPARTMENT-WISE PERFORMANCE ANALYSIS
    # ------------------------------------------------------
    print("-" * 60)
    print("DEPARTMENT-WISE PERFORMANCE")
    print("-" * 60)
    department_analysis = df.groupby('Department').agg(
        Total_Students=('Student_ID', 'count'),
        Average_Marks=('Marks', 'mean'),
        Highest_Marks=('Marks', 'max'),
        Lowest_Marks=('Marks', 'min')
    ).reset_index()
    department_analysis_display = department_analysis.copy()
    department_analysis_display['Average_Marks'] = department_analysis_display['Average_Marks'].round(2)
    print(department_analysis_display.to_string(index=False))
    print()
    # ------------------------------------------------------
    # STEP 12: STUDENTS NEEDING ATTENTION
    # (Condition: Marks < 50 OR Attendance < 75%)
    # ------------------------------------------------------
    print("-" * 60)
    print("STUDENTS NEEDING ATTENTION")
    print("-" * 60)
    attention_condition = (df['Marks'] < 50) | (df['Attendance'] < 75)
    attention_students = df[attention_condition][['Student_ID', 'Name', 'Marks', 'Attendance', 'Grade', 'Result']]
  
    if len(attention_students) > 0:
        print(attention_students.to_string(index=False))
    else:
        print("No students require special attention.")
    print()
    # ------------------------------------------------------
    # STEP 13, 14, 15: SAVE RESULTS TO CSV FILES
    # ------------------------------------------------------
    print("-" * 60)
    print("FINAL REPORT (SAVING OUTPUT FILES)")
    print("-" * 60)
    result_csv = "student_performance_result.csv"
    subj_csv = "subject_analysis.csv"
    dept_csv = "department_analysis.csv"
    try:
        df.to_csv(result_csv, index=False)
        print(f"[SAVED] Complete Processed Data -> {result_csv}")
        subject_analysis_display.to_csv(subj_csv, index=False)
        print(f"[SAVED] Subject-Wise Summary   -> {subj_csv}")
        department_analysis_display.to_csv(dept_csv, index=False)
        print(f"[SAVED] Department-Wise Summary -> {dept_csv}")
    except Exception as e:
        print(f"[ERROR] Failed to write output CSV files: {e}")
    print()
    print("=" * 60)
    print("Analysis completed successfully.")
    print("=" * 60)
if __name__ == "__main__":
    main()
