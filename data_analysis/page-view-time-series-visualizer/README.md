# Page View Time Series Visualizer

You will be working on this project with our Gitpod starter code.

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

- [Python for Everybody Video Course (14 hours)](https://www.youtube.com/watch?v=8DvywoWv6fI)
- [How to Analyze Data with Python Pandas (10 hours)](https://www.youtube.com/watch?v=vmEHCJofslg)

## Project Overview

For this project, you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from **2016-05-09 to 2019-12-03**. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

## Tasks

Use the data to complete the following tasks:

1. **Import the Data**
    - Use Pandas to import the data from `"fcc-forum-pageviews.csv"`. Set the index to the date column.
  
2. **Clean the Data**
    - Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.

3. **Draw Line Plot**
    - Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to `"examples/Figure_1.png"`.
    - **Title:** Daily freeCodeCamp Forum Page Views 5/2016-12/2019
    - **X-axis label:** Date
    - **Y-axis label:** Page Views

4. **Draw Bar Plot**
    - Create a `draw_bar_plot` function that draws a bar chart similar to `"examples/Figure_2.png"`. It should show average daily page views for each month grouped by year.
    - **Legend:** Month labels with a title of "Months"
    - **X-axis label:** Years
    - **Y-axis label:** Average Page Views

5. **Draw Box Plot**
    - Create a `draw_box_plot` function that uses Seaborn to draw two adjacent box plots similar to `"examples/Figure_3.png"`. These box plots should show how the values are distributed within a given year or month and how it compares over time.
    - **Title (First Chart):** Year-wise Box Plot (Trend)
    - **Title (Second Chart):** Month-wise Box Plot (Seasonality)
    - Ensure the month labels on the bottom start at "Jan" and that the x and y axes are labeled correctly.

For each chart, make sure to use a copy of the data frame.

## Development

- Write your code in `time_series_visualizer.py`. For development, you can use `main.py` to test your code.

## Testing

- The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience.

