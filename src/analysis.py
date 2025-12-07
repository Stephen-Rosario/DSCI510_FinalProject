import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

def plot_grade_distribution(df):
    plt.figure(figsize=(8,4))
    sns.histplot(df["g3"], kde=True)
    plt.title("Final Grade Distribution")
    plt.savefig("results/grade_distribution.png")

def plot_study_time_boxplot(df):
    plt.figure(figsize=(8,4))
    sns.boxplot(x="studytime", y="g3", data=df)
    plt.title("Study Time vs. Final Grades")
    plt.savefig("results/studytime_boxplot.png")

def correlation_heatmap(df):
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("results/correlation_heatmap.png")

def internet_ttest(df):
    """Perform t-test on internet vs no-internet students."""
    with_net = df[df["internet"] == 1]["g3"]
    without_net = df[df["internet"] == 0]["g3"]
    return ttest_ind(with_net, without_net, equal_var=False)
