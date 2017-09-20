from pandas import DataFrame

from .eng_freq_data import eng_freq_df

df = DataFrame.from_csv('data/top-1m.csv')

super_list = []


def split_word_in_letters(*args, **kwargs):
    super_list.extend(list(args[0].Domain.split('.')[0]))
    return list(args[0].Domain.split('.')[0])


def first_letter(*args, **kwargs):
    return args[0].Domain[0]


def last_letter(*args, **kwargs):
    return args[0].Domain.split('.')[0][-1]


df.apply(split_word_in_letters, axis=1)
df['first'] = df.apply(first_letter, axis=1)
df['last'] = df.apply(last_letter, axis=1)

df_1 = df.groupby('first').count()['last']
df_1 = DataFrame(df_1)
df_1.rename_axis('letter', inplace=True)
df_1.columns = ['first_count']
df_1['last_count'] = df.groupby('last').count()['first']
df_1['first_percent'] = df_1['first_count']/df_1['first_count'].sum()*100
df_1['last_percent'] = df_1['last_count']/df_1['last_count'].sum()*100

df_2 = DataFrame(super_list, columns=['letters'])
df_2.reset_index(inplace=True)
df_2 = df_2.groupby('letters').count()
df_2.columns = ['count']
df_2['percentage'] = (df_2/df_2.sum())*100
df_2['eng_freq'] = eng_freq_df
