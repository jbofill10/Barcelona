import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

'''Trying to find trends within the data set'''


def trends():
    # Read CSV
    df = pd.read_csv('./Data/accidents_2017.csv', delimiter=",")
    # Sum up mild injuries and serious injuries together row by row
    df['Total Injuries'] = df[['Mild injuries', 'Serious injuries']].apply(
        lambda a: a['Mild injuries'] + a['Serious injuries'], axis=1)

    # Group them together and make a new data frame
    days_injuries = df.groupby(['Part of the day'])['Total Injuries'].sum()
    days_injuries_df = pd.DataFrame(days_injuries)

    # Reindex the rows because pandas sorts rows by string order
    days_injuries_df=days_injuries_df.reindex(['Morning','Afternoon','Night'])

    # Plot dimensions
    plt.figure(figsize=(10, 8))
    plt.plot(days_injuries_df)

    sb.set_color_codes('dark')

    # Quadratic best fit since trend looked quadratic
    sb.regplot(range(3), [i[0] for i in days_injuries_df.values],
               order=2, ci=None, scatter_kws={"s": 30}, color='orange', line_kws={'linestyle': '--'})

    sb.set_style('dark')
    plt.title('Accident Count Respective to the Part of the Day')

    plt.savefig('./Population Graphs/AccidentTrends')

    plt.show()