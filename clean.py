import pandas as pd

data = pd.read_csv("data/ted_talks_en.csv")
# drop unncessary cols
df = data.drop(["talk_id", "available_lang", "url", "published_date", "related_talks", "event"], axis = 1)

df = df[df["native_lang"] == "en"]
df = df.dropna()
# convert date to pandas date
df['recorded_date'] = pd.to_datetime(df['recorded_date'])

# keep only talks after 2000
df = df[df['recorded_date'] >= '2000-01-01']

# keep only talks with one speaker
df = df[df['all_speakers'].str.count(':') == 1].reset_index(drop=True)

# randomly select 1000 talks for analysis
df_sampled = df.sample(n=1000, random_state=42)
df_sampled.to_csv("data/tedtalk_sample.csv")