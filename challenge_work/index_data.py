'''


🗺️ Explore: Which index has produced the highest average annual return?
📊 Visualize: Create a plot visualizing a 30 day moving average for an index of your choosing.
🔎 Analyze: Compare the volatilities of the indexes included in the dataset.

What is Volatility?
Volatility is a measure of the rate of fluctuations in the price of a security over time. 
It indicates the level of risk associated with the price changes of a security. 
Investors and traders calculate the volatility of a security to assess past variations in the prices 
to predict their future movements.


Scenario:

You are working for an investment firm that is looking to invest in index funds.
They have provided you with a dataset containing the returns of 13 different indexes. 
Your manager has asked you to make short-term forecasts for several of the most promising 
indexes to help them decide which would be a good fund to include. 
Your analysis should also include a discussion of the associated risks and volatility of each fund you focus on.

You will need to prepare a report that is accessible to a broad audience. It should outline your 
motivation, steps, findings, and conclusions.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#get data from csv
csv_data = 'data/indexData.csv'
df = pd.read_csv(csv_data, index_col=None)

#function for fisrt challenge: calc highest annual return
df['Date'] = pd.to_datetime(df['Date'])  #convert 'Date' column to datetime   
#calc annual returns for each index
df['Year'] = df['Date'].dt.year


def highest_annual_return_pivot_table(df):
   
    df['Annual_Return'] = (df['Adj Close'] / df.groupby('Year')['Adj Close'].transform('first')) - 1

    #pivot table to get average annual return for each index
    pivot_avg_returns = pd.pivot_table(df, values='Annual_Return', index='Index', aggfunc='mean')

    #index with the highest average annual return
    index_highest_return = pivot_avg_returns.idxmax()
    highest_return = pivot_avg_returns.max()
    return index_highest_return


def highest_annual_return(df):
    #group data by 'Index' and calc the average annual return for each index
    grouped = df.groupby('Index')['Adj Close'].transform('first')
    df['Annual_Return'] = (df['Adj Close'] / grouped) - 1

    # calc average annual return for each index
    avg_returns = df.groupby('Index')['Annual_Return'].mean()

    # find the index with the highest average annual return
    index_highest_return = avg_returns.idxmax()
    highest_return = avg_returns.max()
    return index_highest_return



# print(highest_annual_return_pivot_table(df))
# print(highest_annual_return(df))


def moving_avg_plot(df):
    #df['Date'] = pd.to_datetime(df['Date'])

    #filter data for a specific 'Index'

    index_value = 'NYA'
    filtered_df = df[df['Index'] == index_value]

    #sort the data by 'Date' in ascending order
    filtered_df = filtered_df.sort_values('Date')

    #calculate 30-day moving average of 'Adj Close'
    filtered_df['30_Day_MA'] = filtered_df['Adj Close'].rolling(window=30).mean()

    #plot
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_df['Date'], filtered_df['Adj Close'], label='Adj Close')
    plt.plot(filtered_df['Date'], filtered_df['30_Day_MA'], label='30-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'30-Day Moving Average for Index: {index_value}')
    plt.legend()
    plt.show()

#print(moving_avg_plot(df))


def compare_volatilities(df):
    '''
    To compare the volatilities of different indexes in the dataset, 
    calculate the volatility as the standard deviation of the daily returns for each index.
    '''

    #calc daily returns for each index, creating a column named Daily_Return
    df['Daily_Return'] = df.groupby('Index')['Adj Close'].pct_change() #fractional change so mult by 100 next step

    #multiply the 'Daily_Return' column by 100
    df['Daily_Return'] = df['Daily_Return'].multiply(100)

    #calc volatility (standard deviation of daily returns) for each index
    volatility = df.groupby('Index')['Daily_Return'].std()

    #display in ascending order
    volatility_sorted = volatility.sort_values()
    return volatility_sorted

print(compare_volatilities(df))