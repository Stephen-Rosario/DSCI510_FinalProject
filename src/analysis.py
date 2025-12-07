import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import pandas as pd


def plot_grade_distribution(df: pd.DataFrame) -> None:
    """Save histogram of final grade distribution."""
    plt.figure()
    sns.histplot(df["g3"], kde=True)
    plt.title("Final Grade Distribution")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Count")
    plt.savefig("results/grade_distribution.png")
    plt.close()


def plot_studytime(df: pd.DataFrame) -> None:
    """Save boxplot of study time vs final grade."""
    plt.figure()
    sns.boxplot(x="studytime", y="g3", data=df)
    plt.title("Study Time vs Final Grade")
    plt.xlabel("Study Time Category")
    plt.ylabel("Final Grade (G3)")
    plt.savefig("results/studytime_boxplot.png")
    plt.close()


def correlation_heatmap(df: pd.DataFrame) -> None:
    """Save correlation heatmap of numeric features."""
    plt.figure(figsize=(12, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap")
    plt.savefig("results/correlation_heatmap.png")
    plt.close()


def internet_ttest(df: pd.DataFrame):
    """
    Perform t-test comparing final grades for students
    with and without home internet.
    """
    with_net = df[df["internet"] == 1]["g3"]
    without_net = df[df["internet"] == 0]["g3"]
    return ttest_ind(with_net, without_net, equal_var=False)

