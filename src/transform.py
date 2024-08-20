import pandas as pd

def __init__(self, file):
        self.df = pd.read_csv(file, sep=';', encoding='utf-8')


def clean_data(self):
        # Rename columns to match the SQLAlchemy model
        self.df.rename(columns={
            'FirstName': 'First_Name',
            'LastName': 'Last_Name',
            'ApplicationDate': 'Application_Date',
            'CodeChallengeScore': 'Code_Challenge_Score',
            'TechnicalInterviewScore': 'Technical_Interview_Score'
        }, inplace=True)
        
        # Convert dates to datetime format
        self.df['Application_Date'] = pd.to_datetime(self.df['Application_Date'])
        
        # Handle missing values if needed
        # Example: self.df.fillna('', inplace=True)


def insert_ids(self):
        # Añadir una columna 'ID' con valores secuenciales empezando desde 1
        self.df['ID'] = range(1, len(self.df) + 1)
