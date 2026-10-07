# Student Performance Analysis System
A comprehensive, beginner-friendly Python data analysis project built using **Python 3**, **Pandas**, and **NumPy**. This system processes student academic records from a CSV file, computes individual grades and pass/fail statuses, evaluates overall class metrics, generates subject and department performance summaries, identifies students needing academic attention, and exports reports into CSV files.

---
## Table of Contents
1. [Project Overview](#project-overview)
2. [Objective](#objective)
3. [Technologies Used](#technologies-used)
4. [Concepts Covered](#concepts-covered)
5. [Features](#features)
6. [Dataset Description](#dataset-description)
7. [Project Structure](#project-structure)
8. [Installation](#installation)
9. [How to Run](#how-to-run)
10. [Sample Output](#sample-output)
11. [Grade Rules](#grade-rules)
12. [Output Files](#output-files)
13. [GitHub Upload Instructions](#github-upload-instructions)
14. [Conclusion](#conclusion)

---

## 1. Project Overview

The **Student Performance Analysis System** is designed as a college-level Python assignment project. It demonstrates how to perform end-to-end data analysis without relying on advanced machine learning frameworks or databases. It reads raw data from `students.csv`, cleans and checks for missing values, computes analytical metrics dynamically using Pandas and NumPy, and generates formatted terminal output alongside CSV summary files.

---

## 2. Objective

- Automate the process of evaluating student marks and attendance percentages.
- Assign standard letter grades (`A+`, `A`, `B`, `C`, `D`, `F`) and performance categories (`Excellent`, `Good`, `Average`, `Poor`).
- Determine Pass/Fail status for each student.
- Perform statistical analysis using NumPy arrays (Average, Highest, Lowest marks, Average Attendance).
- Group data by **Subject** and **Department** using Pandas `groupby()` to extract statistical insights.
- Flag students who need academic intervention based on marks (< 50) or attendance (< 75%).
- Export final analytical results to downloadable CSV files for institutional record-keeping.

---

## 3. Technologies Used

- **Python 3.x**: Core programming language.
- **Pandas**: Used for CSV data loading (`read_csv`), DataFrame manipulation, data filtering, sorting, grouping (`groupby`), and saving reports (`to_csv`).
- **NumPy**: Used for efficient numerical vector calculations (`np.array`, `np.mean`, `np.max`, `np.min`).

*No Machine Learning, Flask, Django, Streamlit, or external database systems are required.*

---

## 4. Concepts Covered

- **Python Fundamentals**: Variables, primitive & complex data types, custom functions, modular design (`import`), control flow (`if/elif/else`), try-except error handling.
- **Pandas Data Analysis**: `read_csv()`, DataFrames, Series operations, `.apply()`, conditional filtering, sorting values, `groupby()` aggregation, `isnull()`, `.to_csv()`.
- **NumPy Computations**: Array conversions, `np.mean()`, `np.max()`, `np.min()`.
- **File & Data I/O**: Automated CSV file reading and writing.

---
## 5. Features
- **Automated Grade & Result Computation**: Applies grading logic to every record dynamically.
- **Data Integrity & Missing Value Inspection**: Scans dataset for missing entries and prints a health check.
- **Top 5 Performers Leaderboard**: Automatically sorts and lists top-scoring students.
- **Subject-Wise Analysis**: Groups marks and student counts per subject (Python, Data Science, Machine Learning, SQL, Mathematics).
- **Department-Wise Analysis**: Aggregates records across departments (CSE, AI&DS).
- **Early Warning System**: Identifies students with low marks (< 50) or low attendance (< 75%).
- **Automated Report Generation**: Exports 3 distinct CSV reports upon execution.

---
## 6. Dataset Description

The initial dataset is stored in `students.csv` and contains 25 student records.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `Student_ID` | Integer | Unique identifier for each student (e.g., 101, 102) |
| `Name` | String | Full name of the student |
| `Department` | String | Department name (`CSE`, `AI&DS`) |
| `Subject` | String | Enrolled subject (`Python`, `Data Science`, `Machine Learning`, `SQL`, `Mathematics`) |
| `Marks` | Float / Int | Marks obtained out of 100 |
| `Attendance` | Float / Int | Class attendance percentage (0 to 100) |
---
## 7. Project Structure
```text
student-performance-analysis/
│
├── main.py                         # Main execution script orchestrating data processing
├── functions.py                    # Modular reusable helper functions
├── students.csv                    # Input dataset containing student records
├── README.md                       # Complete project overview & instructions
├── PROJECT_DOCUMENTATION.md        # Detailed project technical documentation
├── requirements.txt                # Python package dependencies (pandas, numpy)
└── .gitignore                      # Version control ignore rules
```
**Generated Files (Created automatically after running `main.py`):**
```text
├── student_performance_result.csv  # Complete dataset with Grade, Result, Performance columns
├── subject_analysis.csv            # Aggregated statistics by Subject
└── department_analysis.csv         # Aggregated statistics by Department
```
---
## 8. Installation
1. **Clone or Download** this project folder to your local system.
2. Open a command prompt / terminal inside the project directory.
3. Install the required Python libraries using `pip`:
```bash
pip install -r requirements.txt
```
---
## 9. How to Run
Execute the main program using Python:

```bash
python main.py
```

---

## 10. Sample Output

When `main.py` is executed, it displays formatted console output:

```text
============================================================
        STUDENT PERFORMANCE ANALYSIS SYSTEM
============================================================

[INFO] Successfully loaded dataset: 'students.csv'

------------------------------------------------------------
TOTAL STUDENTS
------------------------------------------------------------
Total Student Records Processed: 25

------------------------------------------------------------
DATA CHECK (MISSING VALUES)
------------------------------------------------------------
Missing values per column:
Student_ID    0
Name          0
Department    0
Subject       0
Marks         0
Attendance    0
dtype: int64

------------------------------------------------------------
OVERALL ANALYSIS
------------------------------------------------------------
Average Marks      : 71.96
Highest Marks      : 96.00
Lowest Marks       : 32.00
Average Attendance : 80.80%
Passed Students    : 22
Failed Students    : 3

------------------------------------------------------------
GRADE DISTRIBUTION
------------------------------------------------------------
Grade A+  : 6 student(s)
Grade A   : 5 student(s)
Grade B   : 4 student(s)
Grade C   : 3 student(s)
Grade D   : 4 student(s)
Grade F   : 3 student(s)

------------------------------------------------------------
TOP 5 PERFORMING STUDENTS
------------------------------------------------------------
 Student_ID          Name Department  Marks Grade  Attendance
        122 Tanvi Deshmukh      AI&DS     96    A+          97
        111  Siddharth Rao        CSE     95    A+          98
        104     Priya Nair      AI&DS     94    A+          96
        102   Anjali Verma      AI&DS     91    A+          95
        117   Varun Mishra        CSE     90    A+          91

------------------------------------------------------------
STUDENTS NEEDING ATTENTION
------------------------------------------------------------
 Student_ID           Name  Marks  Attendance Grade Result
        105   Vikram Singh     65          72     C   Pass
        107     Amit Patel     38          68     F   Fail
        109    Karan Joshi     54          70     D   Pass
        112     Divya Bhat     45          80     D   Pass
        113   Aakash Kumar     62          65     C   Pass
        115    Manish Jain     32          55     F   Fail
        118     Shreya Das     58          74     D   Pass
        121 Gaurav Choudhary   42          60     D   Pass
        124  Isha Malhotra     35          50     F   Fail

------------------------------------------------------------
FINAL REPORT (SAVING OUTPUT FILES)
------------------------------------------------------------
[SAVED] Complete Processed Data -> student_performance_result.csv
[SAVED] Subject-Wise Summary   -> subject_analysis.csv
[SAVED] Department-Wise Summary -> department_analysis.csv
============================================================
Analysis completed successfully.
============================================================
```
---
## 11. Grade Rules

| Marks Range | Letter Grade | Result Status | Performance Category |
| :--- | :--- | :--- | :--- |
| **90 – 100** | **A+** | Pass | Excellent |
| **80 – 89** | **A** | Pass | Excellent |
| **70 – 79** | **B** | Pass | Good |
| **60 – 69** | **C** | Pass | Good |
| **50 – 59** | **D** | Pass | Average |
| **Below 50** | **F** | Pass (if 40-49) / Fail (if < 40) | Poor (if < 40) / Average |
*Note: Passing cutoff marks is **40**. Marks below 40 are evaluated as **Fail**.*
---
## 12. Output Files
1. `student_performance_result.csv`:
   Contains all original student columns along with computed `Grade`, `Result`, and `Performance` columns.
2. `subject_analysis.csv`:
   Contains aggregated subject metrics: `Subject`, `Total_Students`, `Average_Marks`, `Highest_Marks`, `Lowest_Marks`.
3. `department_analysis.csv`:
   Contains aggregated department metrics: `Department`, `Total_Students`, `Average_Marks`, `Highest_Marks`, `Lowest_Marks`.
   
---
## 13. GitHub Upload Instructions

Follow these commands to publish this project to GitHub:

1. Open terminal inside the project directory:
   ```bash
   cd "student-performance-analysis"
   ```
2. Initialize Git repository:
   ```bash
   git init
   ```
3. Add all files to staging:
   ```bash
   git add .
   ```
4. Commit changes:
   ```bash
   git commit -m "Initial Student Performance Analysis Project"
   ```
5. Rename branch to `main`:
   ```bash
   git branch -M main
   ```
6. Add your remote GitHub repository URL:
   ```bash
   git remote add origin YOUR_GITHUB_REPOSITORY_URL
   ```
7. Push the files:
   ```bash
   git push -u origin main
   ```
### Files to Verify on GitHub:
- `main.py`
- `functions.py`
- `students.csv`
- `README.md`
- `PROJECT_DOCUMENTATION.md`
- `requirements.txt`
- `.gitignore`
---
## 14. Conclusion
The **Student Performance Analysis System** offers an easy-to-understand, modular Python codebase for academic performance evaluation. It highlights practical applications of core Python concepts, error handling, Pandas DataFrame aggregation, and NumPy statistical calculations in a beginner-friendly project format.
