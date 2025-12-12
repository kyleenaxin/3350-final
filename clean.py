import pandas as pd

# randomly select 1000 talks for analysis
data = pd.read_csv("data/ted_talks_en.csv")
# drop unncessary cols
df = data.drop(["talk_id", "available_lang", "url", "published_date", "related_talks", "event"], axis = 1)
print(len(df))

df = df[df["native_lang"] == "en"]
df = df.dropna()
# convert date to pandas date
df['recorded_date'] = pd.to_datetime(df['recorded_date'])
# keep only talks after 2000
df = df[df['recorded_date'] >= '2000-01-01']
print(len(df))

df_sampled = df.sample(n=1000, random_state=42)
df_sampled.to_csv("data/tedtalk_sample.csv")