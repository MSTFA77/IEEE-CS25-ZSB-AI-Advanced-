import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult_data.csv")
    
    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100 * (df['education'] == 'Bachelors').sum() / df.shape[0], 1)
    
    # 4. Percentage with advanced education (Bachelors, Masters, or Doctorate) who earn >50K
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]
    
    advanced = round(100 * (higher_education['salary'] == '>50K').sum() / higher_education.shape[0], 1)
    non_advanced = round(100 * (lower_education['salary'] == '>50K').sum() / lower_education.shape[0], 1)
    
    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_workers.shape[0]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round(100 * rich_min_workers / num_min_workers, 1)
    
    # 7. What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_percentage_by_country = (rich_counts / country_counts * 100).dropna()
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max(), 1)
    
    # 8. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    
    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {advanced}%")
        print(f"Percentage without higher education that earn >50K: {non_advanced}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "advanced_education_rich": advanced,
        "non_advanced_education_rich": non_advanced,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }

if __name__ == '__main__':
    calculate_demographic_data()
