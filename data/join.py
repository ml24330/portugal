import pandas as pd

TOPICS = [
    "automotive industry",
    "auto insurance",
    "second hand car",
    "mobile phone",
    "mercedes benz",
    "electrical appliance",
    "wifi",
    "food",
    "clothing",
    "shoes",
    "underwear",
    "electricity",
    "energy",
    "gasoline",
    "tobacco",
    "video game",
    "t-shirt",
    "natural gas",
    # "health care",
    "furniture",
    "interior design",
    "ebook",
    "novel",
    "footwear",
    "lingerie",
    # "real estate",
    # "life insurance"
]


df = pd.DataFrame()

for topic in TOPICS:

    S = pd.Series()
    
    multiplier = 1

    first_series = pd.read_csv(f"raw/{topic}-2006.csv").iloc[1:,0]
    S = pd.concat([S, first_series])

    for year in range(2007, 2019):
        reference_series = pd.read_csv(f"raw/{topic}-{year}-ref.csv").iloc[1:,0]
        weeks = len([d for d in list(reference_series.index) if d.startswith(str(year-1))])
        reference_sum_prev = sum([int(n) for n in list(reference_series[:weeks])])
        reference_sum_new = sum([int(n) for n in list(reference_series[weeks:])])

        initial_series_prev = pd.read_csv(f"raw/{topic}-{year-1}.csv").iloc[1:,0]
        initial_series_new = pd.read_csv(f"raw/{topic}-{year}.csv").iloc[1:,0]
        initial_sum_prev = sum([int(n) for n in list(initial_series_prev)])
        initial_sum_new = sum([int(n) for n in list(initial_series_new)])

        multiplier *= (reference_sum_new*initial_sum_prev)/(initial_sum_new*reference_sum_prev)

        corrected_series_new = initial_series_new.astype(int)*multiplier

        S = pd.concat([S, corrected_series_new])

    df[topic] = S

df.to_csv("combined.csv")