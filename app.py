import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr

def analyze_csv(file):
    data = pd.read_csv(file)

    # Basic info
    rows, cols = data.shape
    mean_time = round(data['Attempt_Time_Seconds'].mean(), 2)
    accuracy = round(data['Correct'].mean() * 100, 2)

    insight_text = f"""
    DATA SUMMARY
    ----------------
    Total Rows: {rows}
    Total Columns: {cols}

    Average Attempt Time: {mean_time} seconds
    verall Accuracy: {accuracy} %

    📌 Observation:
    - More attempt time generally reduces accuracy
    """

    # Correlation
    corr = data.corr(numeric_only=True)

    # Heatmap
    plt.figure(figsize=(4,4))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    heatmap_fig = plt.gcf()
    plt.close()

    # Scatter plot
    plt.figure(figsize=(5,4))
    sns.scatterplot(
        data=data,
        x='Attempt_Time_Seconds',
        y='Correct',
        hue='Question_Difficulty'
    )
    plt.title("Attempt Time vs Correct")
    scatter_fig = plt.gcf()
    plt.close()

    return insight_text, heatmap_fig, scatter_fig


interface = gr.Interface(
    fn=analyze_csv,
    inputs=gr.File(label="Upload CSV File"),
    outputs=[
        gr.Textbox(label="Important Insights"),
        gr.Plot(label="Correlation Heatmap"),
        gr.Plot(label="Scatter Plot")
    ],
    title="📘 Online Exam Answer Attempt Time Analysis",
    description="Upload exam CSV file to see key insights and visual analysis"
)

interface.launch()
