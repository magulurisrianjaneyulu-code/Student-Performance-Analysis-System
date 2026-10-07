# PROJECT DOCUMENTATION
## Student Performance Analysis System
---
### 1. Project Title
**Student Performance Analysis System**

---
### 2. Objective
The primary objective of this project is to develop an automated, Python-based academic analysis tool that processes student raw records from CSV data, computes individual academic results and letter grades, calculates statistical class metrics using NumPy, performs subject-wise and department-wise analysis using Pandas, flags students requiring academic assistance, and automatically exports clean CSV report summary files.

---
### 3. Problem Statement
Educational institutions often struggle to manually analyze large volumes of student performance data. Manually computing grades, calculating average marks, checking attendance thresholds, and identifying failing or low-performing students is time-consuming and prone to human error. There is a need for a lightweight, automated software solution built with fundamental data processing libraries (Pandas and NumPy) that can instantly transform raw CSV student data into actionable insights and structured downloadable reports.

---
### 4. Technologies Used
- **Python 3**: Core language used for writing program logic and modular functions.
- **Pandas**: Used for reading CSV files, data cleaning, filtering, sorting, DataFrame manipulation, grouping, and exporting output CSV files.
- **NumPy**: Used for performing numerical calculations on arrays (e.g., mean, maximum, and minimum values).

---
### 5. Dataset Description
The system reads input data from `students.csv`. The dataset includes 25 student records with realistic variations across departments, subjects, marks, and attendance levels.

#### Required Columns:
- `Student_ID`: Unique integer identifier for each student (e.g., 101, 102).
- `Name`: Full name of the student.
- `Department`: Department code (`CSE` or `AI&DS`).
- `Subject`: Course subject (`Python`, `Data Science`, `Machine Learning`, `SQL`, or `Mathematics`).
- `Marks`: Marks obtained by the student (0 to 100).
- `Attendance`: Percentage of classes attended (0 to 100).

---
### 6. Project Structure
```text
student-performance-analysis/
│
├── main.py                         # Primary execution file
├── functions.py                    # Module containing custom reusable functions
├── students.csv                    # Input student dataset
├── README.md                       # High-level project summary and instructions
├── PROJECT_DOCUMENTATION.md        # Detailed technical documentation
├── requirements.txt                # Dependency requirements (pandas, numpy)
└── .gitignore                      # Git ignore rule file
```

---
### 7. Implementation Steps

1. **Environment Setup & Dependency Check**: Define required libraries in `requirements.txt` (`pandas` and `numpy`).
2. **Modular Function Creation (`functions.py`)**:
   - `calculate_grade(marks)`: Assigns standard letter grades (`A+` to `F`).
   - `pass_fail(marks)`: Evaluates pass (>= 40) or fail (< 40) status.
   - `performance_category(marks)`: Assigns qualitative category (`Excellent`, `Good`, `Average`, `Poor`).
3. **Data Ingestion with Error Handling**:
   - Open and read `students.csv` using `pd.read_csv()`.
   - Implement `try-except` blocks to handle missing or corrupt files safely.
4. **Data Preprocessing & Validation**:
   - Check total records using `len(df)`.
   - Inspect missing values using `df.isnull().sum()`.
5. **Feature Engineering**:
   - Apply helper functions from `functions.py` using Pandas `.apply()` to dynamically generate `Grade`, `Result`, and `Performance` columns.
6. **Statistical Analysis with NumPy**:
   - Convert `Marks` and `Attendance` columns to NumPy arrays.
   - Compute mean, max, and min marks using `np.mean()`, `np.max()`, and `np.min()`.
   - Calculate average attendance.
7. **Grade Distribution**:
   - Calculate frequency counts of each grade using `df['Grade'].value_counts()`.
8. **Top 5 Leaderboard**:
   - Sort DataFrame by `Marks` descending using `df.sort_values()` and select top 5.
9. **Grouped Analysis**:
   - Group data by `Subject` and calculate total student count, average, max, and min marks using `.groupby()` and `.agg()`.
   - Group data by `Department` and calculate corresponding statistics.
10. **Attention Required Identification**:
    - Filter students with `Marks < 50` OR `Attendance < 75%`.
11. **Report Exporting**:
    - Export processed records and summaries to `student_performance_result.csv`, `subject_analysis.csv`, and `department_analysis.csv`.

---
### 8. Python Concepts Used
- **Variables & Data Types**: Strings, integers, floats, booleans, lists, and dictionaries.
- **Control Flow**: `if-elif-else` conditional statements for grade determination.
- **Custom Functions**: Writing modular, parameterized, reusable functions with clear docstrings.
- **Module Importing**: Importing custom code (`from functions import ...`) and standard/third-party packages.
- **Exception Handling**: `try-except` blocks catching `FileNotFoundError`, `EmptyDataError`, `ValueError`, and `TypeError`.

---
### 9. Pandas Concepts Used
- `pd.read_csv()`: Reading tabular data from CSV files.
- `DataFrame`: Core tabular data structure manipulation.
- `isnull().sum()`: Identifying missing values across columns.
- `apply()`: Applying custom functions row-wise/column-wise across Series.
- `sort_values()`: Sorting rows based on marks in descending order.
- `groupby()` & `agg()`: Grouping data by categorical features (Subject/Department) and applying aggregation functions (`count`, `mean`, `max`, `min`).
- `to_csv()`: Exporting cleaned and transformed DataFrames back to CSV files.

---
### 10. NumPy Concepts Used
- `np.array()`: Converting Pandas Series into numerical arrays.
- `np.mean()`: Calculating the arithmetic mean of marks and attendance.
- `np.max()`: Finding the highest mark obtained.
- `np.min()`: Finding the lowest mark obtained.

---
### 11. Functions Used

#### 1. `calculate_grade(marks)`
- **Input**: `marks` (float/int)
- **Output**: String representation of grade (`A+`, `A`, `B`, `C`, `D`, `F`)
- **Rules**:
  - 90 - 100: A+
  - 80 - 89: A
  - 70 - 79: B
  - 60 - 69: C
  - 50 - 59: D
  - Below 50: F
#### 2. `pass_fail(marks)`
- **Input**: `marks` (float/int)
- **Output**: `'Pass'` if `marks >= 40` else `'Fail'`
#### 3. `performance_category(marks)`
- **Input**: `marks` (float/int)
- **Output**: Qualitative rating (`'Excellent'`, `'Good'`, `'Average'`, `'Poor'`)

---
### 12. Features
- Automated data processing pipeline.
- Custom grading and pass/fail logic.
- NumPy-powered aggregate statistics.
- Leaderboard of Top 5 performing students.
- Subject-level and Department-level aggregation summaries.
- At-risk student identification.
- Automatic creation of 3 exportable CSV report files.

---
### 13. Analysis Performed
- **Overall Class Analysis**: Evaluates class mean mark, highest score, lowest score, average attendance, total passes, and total fails.
- **Grade Distribution**: Computes frequency count for each letter grade.
- **Subject-Wise Analysis**: Compares academic performance across subjects (Python, Data Science, ML, SQL, Math).
- **Department-Wise Analysis**: Compares CSE vs. AI&DS department averages and score ranges.
- **Low Attendance / Low Marks Intervention**: Identifies students with marks below 50 or attendance under 75%.
- 
---
### 14. Sample Results
- **Total Students Processed**: 25
- **Average Marks**: ~71.96
- **Highest Mark**: 96.0 (Tanvi Deshmukh)
- **Lowest Mark**: 32.0 (Manish Jain)
- **Average Attendance**: ~80.80%
- **Passed Students**: 22
- **Failed Students**: 3
---
### 15. Output Files
1. `student_performance_result.csv`: Master processed dataset containing original columns plus `Grade`, `Result`, and `Performance`.
2. `subject_analysis.csv`: Aggregated summary statistics organized by subject.
3. `department_analysis.csv`: Aggregated summary statistics organized by department.
---

### 16. Conclusion
The **Student Performance Analysis System** effectively demonstrates how basic Python programming combined with fundamental data analysis libraries (Pandas & NumPy) can solve real-world educational data challenges. The project maintains modularity, readability, robust error handling, and beginner-friendly structure ideal for academic project submissions.
