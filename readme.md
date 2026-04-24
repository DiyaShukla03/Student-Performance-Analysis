# Student Performance Analysis System

## Objective
The goal of this project is to analyze how study hours and attendance affect student marks. 
Instead of just assuming that more study always leads to better results, I wanted to check it using actual data. 
I also tried to see whether attendance plays an equally important role or not.

## Dataset Description
The dataset used in this project is a simple CSV file with the following columns:

- StudyHours → Number of hours a student studies per day  
- Attendance → Percentage of attendance in classes  
- Marks → Marks obtained by the student  

Some values in the dataset were missing and a few were unrealistic (like marks greater than 100), so preprocessing was required.

## Steps Performed

### 1. Data Loading
- Loaded the dataset using pandas
- Checked the first few rows to understand structure
- Verified number of rows and columns

### 2. Data Cleaning
- Found missing values in StudyHours and Marks
- Filled missing Marks using mean value
- Filled missing StudyHours using median (since it is more stable)
- Removed outliers such as:
  - StudyHours > 15
  - Marks > 100

### 3. Feature Engineering
- Created a new column "Performance" based on marks:
  - Excellent → Marks ≥ 80  
  - Good → Marks between 60 and 79  
  - Needs Improvement → Marks < 60  
- Created another column "EffortScore" = StudyHours × Attendance  
  This was done to combine both factors into a single metric.

### 4. Data Analysis
- Identified top 5 students based on marks
- Found students scoring less than 50
- Compared StudyHours vs Marks
- Compared Attendance vs Marks

### 5. Group-Based Analysis
- Grouped students based on attendance levels (Low, Medium, High)
- Grouped students based on study hours (Low, Medium, High)
- Calculated average marks for each group to observe patterns

## Key Insights

1. Students who study more generally perform better, but there are exceptions  
2. Attendance has a strong impact — even students with good study hours scored low when attendance was poor  
3. Students with both high study hours and high attendance performed the best  
4. EffortScore helped in understanding overall effort better than individual factors  
5. Removing outliers improved the reliability of results  
6. Some students with moderate study hours still scored well due to consistent attendance  

