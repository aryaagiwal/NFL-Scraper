import pandas as pd
import matplotlib.pyplot as plt


def generate_all_team_wins():
    data_df = pd.read_csv("./standings.csv")
    fig, axes = plt.subplots(nrows=4, ncols=8, figsize=(64, 64))
    for idx, team_name in enumerate(pd.unique(data_df["Names"])):
        subplot_index = (idx // 8, idx - (8 * (idx // 8)))
        team_df = data_df.loc[data_df['Names'] == team_name]
        team_df.plot(ax=axes[subplot_index], x="Year", y="Wins")
        axes[subplot_index].title.set_text(team_name)
    plt.savefig("teamwins.png")



