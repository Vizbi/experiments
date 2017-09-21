from pandas import DataFrame

from .eng_freq_data import eng_bigram_freq_df, eng_monogram_freq_df

df = DataFrame.from_csv('data/top-1m.csv')

monogram_list = []
bigram_list = []

def split_word_in_letters(*args, **kwargs):
    monogram_list.extend(list(args[0].Domain.split('.')[0]))
    return list(args[0].Domain.split('.')[0])

def split_words_in_bigram(*args, **kwargs):
    domain = args[0].Domain.split('.')[0]
    bigram_list.extend([domain[x:x+2] for x in range(len(domain) - 1)])

def first_letter(*args, **kwargs):
    return args[0].Domain[0]


def last_letter(*args, **kwargs):
    return args[0].Domain.split('.')[0][-1]


df.apply(split_word_in_letters, axis=1)
df.apply(split_words_in_bigram, axis=1)
df['first'] = df.apply(first_letter, axis=1)
df['last'] = df.apply(last_letter, axis=1)

df_1 = df.groupby('first').count()['last']
df_1 = DataFrame(df_1)
df_1.rename_axis('letter', inplace=True)
df_1.columns = ['first_count']
df_1['last_count'] = df.groupby('last').count()['first']
df_1['first_percent'] = df_1['first_count']/df_1['first_count'].sum()*100
df_1['last_percent'] = df_1['last_count']/df_1['last_count'].sum()*100

monogram_df = DataFrame(monogram_list, columns=['letters'])
monogram_df.reset_index(inplace=True)
monogram_df = monogram_df.groupby('letters').count()
monogram_df.columns = ['count']
monogram_df['percentage'] = (monogram_df/monogram_df.sum())*100
monogram_df['eng_freq'] = eng_monogram_freq_df


bigram_df = DataFrame(bigram_list, columns=['bigram'])
bigram_df.reset_index(inplace=True)
bigram_df = bigram_df.groupby('bigram').count()
bigram_df.columns = ['count']
bigram_df['percentage'] = (bigram_df/bigram_df.sum())*100
bigram_df['eng_freq'] = eng_bigram_freq_df
