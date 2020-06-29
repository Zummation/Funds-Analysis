import pandas as pd

# nav = pd.read_csv('monthly_nav.csv').set_index('Date')
# sel = pd.read_csv('selected_funds.csv').fund_code.to_list()
# nav = nav[[col for col in nav.columns if col in set(sel)]]
# # print(len(set(sel).intersection(set(nav.columns))))

# for col in nav.columns:
#     last = nav[col].dropna()
#     if len(last) != 0:
#         last = last.index[-1]
#         nav[col].loc[:last] = nav[col].loc[:last].fillna(method='ffill')

# print(nav)
# print(sel)

# nav.to_csv('selected_nav_ffill.csv')

# a = set(sel) - set(nav.columns)
# a = list(a)
# pd.DataFrame(a).to_csv('กองที่หายไป.csv')

###############################################

df = pd.read_csv('selected_nav_ffill.csv')
df = df.replace(to_replace=0, method='ffill')
df.to_csv('selected_nav_ffill_2.csv', index=False)