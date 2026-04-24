def basic_stats(df):
    print("\n--- Basic Statistics ---")
    
    stats = df.describe()
    print(stats)
def top_students(df):
    print("\n--- Top 5 Students ---") 
    sorted_df = df.sort_values(by='Marks', ascending=False)
    top5 = sorted_df.head(5)
    print(top5)
def low_performers(df):
    print("\n--- Students with Marks < 50 ---")
    low = df[df['Marks'] < 50]
    if len(low) == 0:
        print("No students found")
    else:
        print(low)
def group_analysis(df):
    print("\n--- Group Analysis ---")
    print("\nBased on Attendance:")
    att_group = df.groupby('AttendanceLevel')
    for name, group in att_group:
        avg_marks = group['Marks'].mean()
        print(name, "->", avg_marks)
    print("\nBased on Study Hours:")
    study_group = df.groupby('StudyCategory')
    for name, group in study_group:
        avg_marks = group['Marks'].mean()
        print(name, "->", avg_marks)
def insights(df):
    print("\n--- Key Insights ---")
    avg_marks = df['Marks'].mean()
    avg_att = df['Attendance'].mean()
    avg_study = df['StudyHours'].mean()
    print("Average Marks:", round(avg_marks, 2))
    print("Average Attendance:", round(avg_att, 2))
    print("Average Study Hours:", round(avg_study, 2))
    print("\nSome observations I found:")
    print("1. Students with higher study hours mostly have better marks")
    print("2. Attendance also seems to affect marks")
    print("3. Some students study enough but still score low")
    print("4. Combination of attendance and study is important")
    print("5. Data cleaning helped in getting better results")