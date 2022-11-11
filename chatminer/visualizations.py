import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


<<<<<<< Updated upstream
def sunburst(df: pd.DataFrame, figureName: str = "sunburst"):
=======
def sunburst(df: pd.DataFrame, figuresavename: str):
>>>>>>> Stashed changes
    df_circle = df.groupby(by="hour")["message"].count().reset_index()

    time = df_circle["hour"]
    count = df_circle["message"]

    c = np.zeros(24)
    c[time] = count
    count = c

    ax = plt.subplot(111, projection="polar")

    x = np.arange(0, 2 * np.pi, 2 * np.pi / len(count)) + np.pi / len(count)

    ax.bar(x, count, width=2 * np.pi / len(count), alpha=0.4, color="#e76f51", bottom=0)

    max_ind = np.argmax(count)
    ax.bar(
        x[max_ind],
        count[max_ind],
        bottom=0,
        width=2 * np.pi / len(count),
        alpha=1,
        color="#e76f51",
    )

    ax.bar(
        x,
        np.max(count) * np.ones(len(count)),
        width=2 * np.pi / len(count),
        alpha=0.15,
        bottom=0,
        color="#cb997e",
        edgecolor="black",
    )

    ax.set_theta_direction(-1)
    ax.grid(False)
    ax.spines["polar"].set_visible(False)
    ax.set_theta_offset(np.pi / 2)
    ax.set_xticks(np.linspace(0, 2 * np.pi, 24, endpoint=False))
    ticks = [
        "12 AM",
        "",
        "",
        "3 AM",
        "",
        "",
        "6 AM",
        "",
        "",
        "9 AM",
        "",
        "",
        "12 PM",
        "",
        "",
        "3 PM",
        "",
        "",
        "6 PM",
        "",
        "",
        "9 PM",
        "",
        "",
    ]
    ax.set_xticklabels(ticks)
    ax.set_title("Messages per Daytime", fontdict={"fontsize": 15})
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.tight_layout()
<<<<<<< Updated upstream
    plt.show()
	plt.savefig(figureName + ".png")


def wordcloud(df: pd.DataFrame, stopwords: list, figureName: str = "wordcloud"):
=======
    #plt.show()
    plt.savefig("./figures/" + figuresavename + "_sunburst.png")
    plt.close()


def wordcloud(df: pd.DataFrame, stopwords: list, figuresavename: str):
>>>>>>> Stashed changes
    messages = [word.split() for word in df["message"].values]
    words = [word.lower() for sublist in messages for word in sublist]

    stopwords = STOPWORDS.update(stopwords)

    wordcloud = WordCloud(
        stopwords=stopwords,
        max_font_size=90,
        width=800,
        height=400,
        background_color="white",
        colormap="magma",
        min_word_length=2,
        max_words=400,
        min_font_size=12,
    )
    wordcloud.generate(" ".join(words))

    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
<<<<<<< Updated upstream
    plt.show()
	plt.savefig(figureName + ".png")
=======
    #plt.show()
    plt.savefig("./figures/" + figuresavename + "_wordcloud.png")
    plt.close()

def weekday_plot(df: pd.DataFrame, figuresavename: str): # added weekday plot
    
    days = {1: "Monday",
           2: "Tuesday",
           3: "Wednesday",
           4: "Thursday",
           5: "Friday",
           6: "Saturday",
           7: "Sunday",}
    df_weekday = df.groupby(by="weekday")["message"].count().reset_index()

    x = list(days.keys())
    y = []
    for d in days.values():
        i = df_weekday.index[df_weekday['weekday'] == d].tolist()[0]
        y.append( df_weekday.iloc[i]["message"])

    ax = plt.subplot(111)
    ax.bar(x, y, color="#9CA3D6", bottom=0)
    ticks = list(days.values())
    ax.set_xticks(np.linspace(1, 8, 7, endpoint=False))
    ax.set_xticklabels(ticks)
    ax.set_title("Messages per Day", fontdict={"fontsize": 15})
    plt.tight_layout()
    #plt.show()
    plt.savefig("./figures/" + figuresavename + "_weekday.png")
    plt.close()

def month_plot(df: pd.DataFrame, figuresavename: str): # added month plot
    
    months = {1: "January",
           2: "February",
           3: "March",
           4: "April",
           5: "May",
           6: "June",
           7: "July",
           8: "August",
           9: "September",
           10: "October",
           11: "November",
           12: "December"}
    df_month = df.groupby(by="month")["message"].count().reset_index()

    x = list(months.keys())
    y = []
    for m in months.values():
        i = df_month.index[df_month['month'] == m].tolist()[0]
        y.append( df_month.iloc[i]["message"])

    ax = plt.subplot(111)
    ax.bar(x, y, color="#B3DDC4", bottom=0)
    ticks = [ m[:3] for m in months.values()]
    ax.set_xticks(np.linspace(1, 13, 12, endpoint=False))
    ax.set_xticklabels(ticks)
    ax.set_title("Messages per Month", fontdict={"fontsize": 15})
    plt.tight_layout()
    #plt.show()
    plt.savefig("./figures/" + figuresavename + "_month.png")
    plt.close()
>>>>>>> Stashed changes
