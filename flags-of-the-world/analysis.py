from pandas import DataFrame

df_world = DataFrame.from_csv('data.csv')
df_usa = DataFrame.from_csv('data-usa.csv')

num_of_countries_with_a_color = df_world.groupby('Color').nunique()['Country'].sort_values(ascending=False)
num_of_us_countries_with_a_color = df_usa.groupby('Color').nunique()['Number of Pixels'].sort_values(ascending=False)

countries_with_num_of_colors_in_flag = df_world.groupby('Country').nunique()['Color'].sort_values(ascending=False)
countries_with_num_of_colors_in_flag_usa = df_usa.groupby('Country').nunique()['Color'].sort_values(ascending=False)

country_with_most_colors_in_flag = countries_with_num_of_colors_in_flag.reset_index()
country_with_most_colors_in_flag = country_with_most_colors_in_flag[
    country_with_most_colors_in_flag['Color'] == country_with_most_colors_in_flag.max()['Color']]

country_with_most_colors_in_flag_usa = countries_with_num_of_colors_in_flag_usa.reset_index()
country_with_most_colors_in_flag_usa = country_with_most_colors_in_flag_usa[
    country_with_most_colors_in_flag_usa['Color'] == country_with_most_colors_in_flag_usa.max()['Color']]

country_with_least_colors_in_flag = countries_with_num_of_colors_in_flag.reset_index()
country_with_least_colors_in_flag = country_with_least_colors_in_flag[
    country_with_least_colors_in_flag['Color'] == country_with_least_colors_in_flag.min()['Color']]

country_with_least_colors_in_flag_usa = countries_with_num_of_colors_in_flag_usa.reset_index()
country_with_least_colors_in_flag_usa = country_with_least_colors_in_flag_usa[
    country_with_least_colors_in_flag_usa['Color'] == country_with_least_colors_in_flag_usa.min()['Color']]

average_number_of_colors_on_flag = df_world.groupby('Color').nunique()['Country'].sort_values(ascending=False).sum() / df_world[
    'Country'].nunique()

average_number_of_colors_on_flag_usa = df_usa.groupby('Color').nunique()['Country'].sort_values(ascending=False).sum() / df_usa[
    'Country'].nunique()

print(num_of_countries_with_a_color)
print(num_of_us_countries_with_a_color)
print(countries_with_num_of_colors_in_flag)
print(countries_with_num_of_colors_in_flag_usa)
print(country_with_most_colors_in_flag)
print(country_with_most_colors_in_flag_usa)
print(country_with_least_colors_in_flag)
print(country_with_least_colors_in_flag_usa)
print(average_number_of_colors_on_flag)
print(average_number_of_colors_on_flag_usa)
