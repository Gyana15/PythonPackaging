import pandas as pd

def stack_fill():
    print('Gyan')
    df = pd.read_csv('FL_insurance_sample.csv')
    df.fillna(method='ffill' , inplace=True)
    df['policyID'] = df['policyID'].astype('Int64')
    print(df)

stack_fill()