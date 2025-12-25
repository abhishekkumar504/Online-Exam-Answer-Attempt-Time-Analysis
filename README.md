# Online Exam Answer Attempt Time Analysis
## Project Overview :

This project  is about to analyzes how much time students take to answer online exam questions and how that time is related to question difficulty and correctness.
The aim is to understand what quesions are hard or easy for students on the basis of what time they spend on each quesions for better data analysis .

## Dataset Information ( data of students )

The dataset contains 75 records with the following columns:
- Student_ID – Unique ID for each student
- Question_ID – Question number (Q1 to Q5)
- Question_Difficulty – Difficulty level (Easy, Medium, Hard)
- Attempt_Time_Seconds – Time taken to answer (in seconds)
- Correct – Answer status (1 = Correct, 0 = Wrong)


## Tools & Libraries Used ###

1. Python
2. NumPy – Numerical operations
3. Pandas – Data analysis and manipulation
4. Matplotlib – Basic data visualization
5. Seaborn – Advanced plots and heatmaps

## Steps Performed in the Project ###
1. Data Loading & Inspection
- CSV file loaded using Pandas
- First few rows checked using head()
- Data structure verified using info()

2. Data Cleaning
- Checked for null values -> none found
- Checked for duplicate rows -> none found

3. Statistical Analysis:

- Used describe() to get:

      - Mean attempt time
      - Minimum & maximum time
      - Standard deviation
      

4. Difficulty-wise Analysis
- Easy questions took the least time
- Hard questions took the most time
- Medium questions were in between

5. Correlation Analysis
Calculated correlation between:
- Attempt time
- Correct answers
- Found a negative correlation, meaning:

> As attempt time increases, chances of correct answer decrease

## Visualizations Used 

1. Heatmap
Shows correlation between attempt time and correctness

2. Scatter Plot
Displays relationship between time taken and correct answers
Color-coded by question difficulty

3. Line Plot
Shows average attempt time for each question
These plots help in visual understanding of patterns.

# Key Insights
- Students answer easy questions faster
- Hard questions take more time and have more wrong answers
- Spending too much time does not always mean a correct answer
- Attempt time can be a good indicator of question difficulty
