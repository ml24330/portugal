import pandas as pd
from categories import TOPICS

TOPICS.remove("energy")
df = pd.DataFrame()

energy = pd.read_csv("combined.csv")["energy"]
df["energy"] = energy

for topic in TOPICS:

    ratios = []

    for year in range(2006, 2019):
        compared = pd.read_csv(f"raw/--{topic}-{year}.csv", skiprows=[0], index_col="Week").iloc[1:,:]
        compared = compared.replace("<1","0.5")

        column_with_max = pd.Series((compared == 100).astype(int).sum().values).idxmax()

        energy_reference = pd.read_csv(f"raw/energy-{year}.csv").iloc[1:,0]
        other_reference = pd.read_csv(f"raw/{topic}-{year}.csv").iloc[1:,0]


        if column_with_max == 0:
            ratio = sum(compared.iloc[:,-1].astype(float))/sum(other_reference.astype(float))
        elif column_with_max == 1:
            ratio = sum(energy_reference.astype(float))/sum(compared.iloc[:,0].astype(float))

        ratios.append(ratio)

    before = pd.read_csv("combined.csv")[topic]
    after = before*sum(ratios)/14
    
    df[topic] = after



df.to_csv("comparable.csv")