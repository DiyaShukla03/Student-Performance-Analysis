import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Fill missing values
    df['Marks'].fillna(df['Marks'].mean(), inplace=True)
    df['StudyHours'].fillna(df['StudyHours'].median(), inplace=True)
    
    # Remove outliers
    df = df[(df['StudyHours'] <= 15) & (df['Marks'] <= 100)]
    
    return df


def feature_engineering(df):
    # Performance category
    def performance(marks):
        if marks >= 80:
            return "Excellent"
        elif marks >= 60:
            return "Good"
        else:
            return "Needs Improvement"

    df['Performance'] = df['Marks'].apply(performance)

    # Effort Score
    df['EffortScore'] = df['StudyHours'] * df['Attendance']

    # Attendance Level
    df['AttendanceLevel'] = pd.cut(
        df['Attendance'],
        bins=[0, 60, 80, 100],
        labels=['Low', 'Medium', 'High']
    )

    # Study Category
    df['StudyCategory'] = pd.cut(
        df['StudyHours'],
        bins=[0, 4, 8, 15],
        labels=['Low', 'Medium', 'High']
    )

    return df