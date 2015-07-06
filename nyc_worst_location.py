## NYC worst collision locations

df['LOCATION'].value_counts()
worst_loc = df['LOCATION'].value_counts()
worst_loc = pd.DataFrame(worst_loc)
worst_loc['location'] = worst_loc.index
worst_loc['location'] = worst_loc['location'].str.replace('(', '')
worst_loc['location'] = worst_loc['location'].str.replace(')', '')
worst_loc['location'] = worst_loc['location'].str.replace(' ', '')

worst_loc.columns = ['count', 'location']
worst_loc.reset_index(level=0, inplace=True)
worst_loc.drop('index', axis=1, inplace=True)
#worst_loc
worst_loc_latitude = worst_loc['location'].str.split(',').apply(pd.Series, 1)
worst_loc= pd.concat([worst_loc, worst_loc_latitude], axis=1)
worst_loc.drop('location', axis=1, inplace=True)
worst_loc.columns = ['count', 'latitude', 'longitude']

# saving
worst10_loc = worst_loc[:10]
worst10_loc.to_csv('worst10_loc.csv')
