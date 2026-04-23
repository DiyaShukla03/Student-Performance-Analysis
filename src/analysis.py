def basic_stats(df):
    print("\nBasic Statistics:\n", df.describe())


def top_students(df):
    print("\nTop 5 Students:\n", df.sort_values(by='Marks', ascending=False).head())


def low_performers(df):
    print("\nStudents with Marks < 50:\n", df[df['Marks'] < 50])


def group_analysis(df):
    print("\nAverage Marks by Attendance Level:\n",
          df.groupby('AttendanceLevel')['Marks'].mean())

    print("\nAverage Marks by Study Category:\n",
          df.groupby('StudyCategory')['Marks'].mean())


def insights():
    print("\nKey Insights:")
    print("1. Higher study hours generally improve marks.")
    print("2. Attendance has a strong positive impact on performance.")
    print("3. Students with low attendance perform poorly.")
    print("4. EffortScore (combined metric) is a better indicator than single factors.")
    print("5. Removing outliers improves analysis accuracy.")