import pandas as pd

df = pd.read_csv('ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv')

# 提取 year 和 month_num（可选）
df['year'] = df['month'].str[:4].astype(int)
# df['month_num'] = df['month'].str[-2:].astype(int)  # 如果你以后也要月信息可以加


def parse_lease(lease_str):
    parts = lease_str.split(' ')
    years = int(parts[0])
    months = int(parts[2]) if len(parts) > 2 else 0
    return round(years + months / 12, 2)

df['remaining_lease_year'] = df['remaining_lease'].apply(parse_lease)

columns_to_keep = ['year', 'town', 'flat_type', 'resale_price', 'flat_model', 'remaining_lease_year']
df_cleaned = df[columns_to_keep]

# 可选：保存处理后的文件
df_cleaned.to_csv('data.csv', index=False)
