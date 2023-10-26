import seaborn as sns 
import matplotlib.pyplot as plt


def plot_survival_bar_per_state(data, feature_name):
    sns.set_style("whitegrid")
    _, axes = plt.subplots(nrows=1, ncols=1, figsize=(14,6))
    ax = sns.barplot(
        y=data[feature_name],x=data['season'].astype(str),
        hue=data["death_next_season"].apply(lambda x : "Death" if x == 1 else "Survived"), ax=axes,
        palette="blend:#D8A348,#1D1D1D"#, errcolor="darkred"
    )
    #  
    ax.set_ylabel(f"{feature_name.upper()} from start of June to end of August")
    ax.set_xlabel("Did not survived until next season")
    ax.tick_params(labelrotation=90)
    plt.title(f"{feature_name.upper()} during 2020-2022 seasons \n for hives that survived or not")
    plt.show()