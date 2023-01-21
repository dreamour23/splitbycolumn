import pandas as pd

Input_file = input('Please give name of the textfile and its extension (like uberall.txt): ')

textfile = Input_file

Input_split = input('Please give column to split by: ')

Input_sep = input('Is the file tab separated? Enter yes or no: ')

if Input_sep[0] == 'y':
    df = pd.read_csv(textfile, dtype=object, sep='\t')
else:
    df = pd.read_csv(textfile, dtype=object)


# create the dataframe
#df = pd.read_csv(textfile, dtype=object, sep='\t')
#df = pd.read_csv(textfile, dtype=object)

# groupby the desired column and iterate through the groupby object
for group, dataframe in df.groupby(Input_split):
    
    # save the dataframe for each group to a csv
    dataframe.to_csv(f'{group}.txt', sep='\t', index=False)