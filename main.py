from src.preprocess import load_data, clean_data, feature_engineering
from src.analysis import basic_stats, top_students, low_performers, group_analysis, insights

def main():
    # Step 1: Load data
    df = load_data("data/student_dataset.csv")

    print("\nInitial Data:")
    print(df.head())

    # Step 2: Clean data
    df = clean_data(df)

    # Step 3: Feature Engineering
    df = feature_engineering(df)

    print("\nProcessed Data:")
    print(df.head())

    # Step 4: Analysis
    basic_stats(df)
    top_students(df)
    low_performers(df)
    group_analysis(df)

    # Step 5: Insights (UPDATED)
    insights(df)


if __name__ == "__main__":
    main()