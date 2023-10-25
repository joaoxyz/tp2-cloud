import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

dataset = pd.read_csv('datasets/playlist-sample-ds1.csv')

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_items = apriori(df, min_support=0.6)

with open("model-results.json", mode="w") as f:
    f.write(frequent_items.to_json())