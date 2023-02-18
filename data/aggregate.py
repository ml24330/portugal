import pandas as pd

TOPICS = [
    "automotive industry",
    "auto insurance",
    "second hand car",
    "mobile phone",
    "mercedes benz",
    "electrical appliance",
    "wifi",
    "clothing",
    "shoes",
    "underwear",
    "electricity",
    # "energy", 
    "gasoline",
    "tobacco",
    "video game",
    "t-shirt",
    "natural gas",
    # "health care", LATER
    "furniture",
    "interior design",
    "ebook",
    "novel",
    "footwear",
    # "lingerie",
    # "real estate",
    # "life insurance",
    # "dessert",
    # "potato",
    # "coffee",
    # "bottled water",
    # "margarine",
    # "offal",
    # "juice",
    # "jam" LATER
]


df = pd.DataFrame()

energy = pd.read_csv("combined.csv")["energy"]
df["energy"] = energy

for topic in TOPICS:

    ratios = []

    for year in range(2006, 2019):
        compared = pd.read_csv(f"raw/--{topic}-{year}.csv", skiprows=[0], index_col="Week").iloc[1:,:]

        column_with_max = pd.Series((compared == 100).astype(int).sum().values).idxmax()

        energy_reference = pd.read_csv(f"raw/energy-{year}.csv").iloc[1:,0]
        other_reference = pd.read_csv(f"raw/{topic}-{year}.csv").iloc[1:,0]


        if column_with_max == 0:
            ratio = sum(compared.iloc[:,-1].astype(int))/sum(other_reference.astype(int))
        elif column_with_max == 1:
            ratio = sum(energy_reference.astype(int))/sum(compared.iloc[:,0].astype(int))

        ratios.append(ratio)

    before = pd.read_csv("combined.csv")[topic]
    after = before*sum(ratios)/14
    
    df[topic] = after



df.to_csv("test.csv")