import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
   
    df=pd.read_csv("adult.data.csv")


    df=pd.DataFrame(df)
    race_count=df.groupby(by='race').size().sort_values(ascending=False)


    df[(df.sex == "Male")]['age'].mean()
    average_age_men = df[(df.sex == "Male")]['age'].mean().round(1)


    percentage_bachelors = df[df.education == "Bachelors"].education.count()/df.education.count()*100
    percentage_bachelors=float(round(percentage_bachelors,1))


    df['advanced_degree'] = np.where((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate'), True, False)
    higher_education=df[(df.advanced_degree)].advanced_degree.count().round(1)
    lower_education=df[(~df.advanced_degree)].advanced_degree.count().round(1)

    # percentage with salary >50K
    higher_education_rich=df[(df.advanced_degree)&(df.salary=='>50K')].advanced_degree.count()/higher_education*100
    higher_education_rich=round(float(higher_education_rich),1)

    lower_education_rich=df[(~df.advanced_degree)&(df.salary=='>50K')].advanced_degree.count()/lower_education.round(1)*100
    lower_education_rich=round(float(lower_education_rich),1)


    min_work_hours = df['hours-per-week'].min()

    num_min_workers=df.loc[(df['hours-per-week'] == min_work_hours)].age.count()
    rich_workers_min=df.loc[(df.salary=='>50K')&(df['hours-per-week'] == min_work_hours)].age.count()

    rich_percentage=round(rich_workers_min/num_min_workers,1)*100


    country_percentage_rich=df.loc[(df.salary=='>50K')].groupby(by='native-country').size()/df.groupby(by='native-country').size()
    top_country=country_percentage_rich[country_percentage_rich.eq(country_percentage_rich.max())]
    highest_earning_country=top_country.index[0]
    highest_earning_country_percentage=round(float(top_country.values[0]*100),1)


    india_professions=df.loc[(df['native-country']=='India') & (df['salary']=='>50K')].groupby(by='occupation').salary.count()
    india_professions=india_professions.sort_values(ascending=False)
    top_IN_occupation = india_professions.head(1).index[0]



    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
