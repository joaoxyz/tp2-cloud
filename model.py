import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv('datasets/2023_spotify_ds1.csv')

# Dataset cleanup
#df['song'] = list(zip(df.artist_name, df.track_name))
df = df.groupby(['pid', 'track_name'])['duration_ms'].sum().unstack().reset_index().fillna(0).set_index('pid')
df = df.applymap(lambda x: True if x > 0 else False)

frequent_itemsets = apriori(df, min_support=0.06, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules.to_pickle('model_results.pickle')