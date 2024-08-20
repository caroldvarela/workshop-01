import pandas as pd

class Transform:
        def __init__(self, file):
                self.df = pd.read_csv(file, sep=';', encoding='utf-8')


        def rename_columns(self):
                # Rename columns to match the SQLAlchemy model
                self.df.rename(columns={
                'First Name': 'First_Name',
                'Last Name': 'Last_Name',
                'Application Date': 'Application_Date',
                'Code Challenge Score': 'Code_Challenge_Score',
                'Technical Interview Score': 'Technical_Interview_Score'
                }, inplace=True)
                
                

        def insert_ids(self):
                self.df['ID'] = range(1, len(self.df) + 1)
