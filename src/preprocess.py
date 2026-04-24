import pandas as pd
def load_data(path):
    print("Loading data...")
    df = pd.read_csv(path, sep='\t')
    print("Data loaded successfully")
    print("First few rows:")
    print(df.head())
    return df
def clean_data(df):
    print("\n--- Cleaning Data ---")

    # check missing values
    print("Missing values before cleaning:")
    print(df.isnull().sum())

    # fill missing values
    marks_mean = df['Marks'].mean()
    study_median = df['StudyHours'].median()

    df['Marks'] = df['Marks'].fillna(marks_mean)
    df['StudyHours'] = df['StudyHours'].fillna(study_median)

    # sometimes attendance can also have missing values
    if df['Attendance'].isnull().sum() > 0:
        df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    # remove outliers step by step
    print("\nRemoving outliers...")

    before_rows = len(df)

    df = df[df['StudyHours'] <= 15]
    df = df[df['Marks'] <= 100]

    after_rows = len(df)

    print("Rows before:", before_rows)
    print("Rows after:", after_rows)

    return df


def feature_engineering(df):
    print("\n--- Feature Engineering ---")

    # performance category
    performance_list = []

    for m in df['Marks']:
        if m >= 80:
            performance_list.append("Excellent")
        elif m >= 60:
            performance_list.append("Good")
        else:
            performance_list.append("Needs Improvement")

    df['Performance'] = performance_list

    # effort score
    df['EffortScore'] = df['StudyHours'] * df['Attendance']

    # attendance level
    df['AttendanceLevel'] = pd.cut(
        df['Attendance'],
        bins=[0, 60, 80, 100],
        labels=['Low', 'Medium', 'High']
    )

    # study category
    df['StudyCategory'] = pd.cut(
        df['StudyHours'],
        bins=[0, 4, 8, 15],
        labels=['Low', 'Medium', 'High']
    )

    print("New columns added: Performance, EffortScore, AttendanceLevel, StudyCategory")

    return df