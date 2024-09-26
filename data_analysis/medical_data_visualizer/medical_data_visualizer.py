import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math

# 1
df = pd.read_csv("medical_examination.csv")

# 2
overweight = []
# print(df)

# 3

for i in df["id"]:
    weight = df.loc[df["id"] == i, "weight"].iloc[0]
    height = df.loc[df["id"] == i, "height"].iloc[0] / 100
    if weight / math.pow(height, 2) > 25:
        overweight.append(1)
    else:
        overweight.append(0)

df["overweight"] = overweight

df['cholesterol'] = np.where(df["cholesterol"] == 1, 0, 1)
df['gluc'] = np.where(df["gluc"] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_melt = pd.melt(df,
        id_vars=["cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]
    )

    # 6
    df_cat = sns.catplot(
        x="variable", kind="count", hue="value", data=df_melt,  col="cardio"
    )
    df_cat.set_axis_labels("variable", "total")

    # 7
    plt.show()

    # 8
    fig = df_cat.fig

    # 9
    fig.savefig("catplot.png")
    return fig


# draw_cat_plot()


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df["ap_lo"]<=df["ap_hi"])&
                 (df['height'] >= df['height'].quantile(0.025)) & 
                  (df['height'] <= df['height'].quantile(0.975))&
                  (df['weight'] >= df['weight'].quantile(0.025)) & 
                  (df['weight'] <= df['weight'].quantile(0.975))
                  ]
    


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', ax=ax)
    # 16
    fig.savefig("heatmap.png")
    return fig

draw_heat_map()