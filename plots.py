from typing import Union
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_histogram(*, data: pd.DataFrame, feature: str, text: str = ""):
    """This returns a Seaborn Histogram."""
    sns.histplot(data=data, x=feature)
    plt.title(f"Distribution of {feature!r} {text}", size=16)
    plt.tight_layout()
    plt.show()


def display_count(
    data: pd.DataFrame, feature: str, hue: Union[None, str] = None, rotation: int = 90
):
    """This is used to make a count plot of the specified categorical variable.
    Params:

    data: Pandas DF
        The source DataFrame containing the variable.
    feature: str
        The numerical variable to plot.
    rotation: int, default=90
        The x-label ticks rotation in degrees.
    hue: None or str, default=None
        Should be something that can be interpreted by
        :func:`color_palette`, or a dictionary mapping
        hue levels to matplotlib colors.

    Returns:

    A Seaborn count plot
    """
    fig, ax = plt.subplots(figsize=(7, 5))

    sns.countplot(x=feature, data=data, hue=hue, ax=ax, palette="Paired")
    plt.xticks(rotation=rotation)
    ax.set_xlabel(f"{feature}", size=13)
    ax.set_title(f"Frequency Distribution of {feature!r}", size=15)
    ax.grid(visible=False)

    # Annotate the chart
    for bar in ax.patches:
        x_val = bar.get_x() + bar.get_width() / 2  # x pos
        y_val = bar.get_height()  # y pos
        ax.annotate(
            text=y_val,  # text pos
            xy=(x_val, y_val),  # (x, y)
            xytext=(0, 6),  # text position
            ha="center",  # horizontal alignment
            va="center",  # vertical alignment
            size=10,  # text size
            textcoords="offset points",
        )

    fig.tight_layout()
    plt.show()    