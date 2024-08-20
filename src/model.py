from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Candidates(base):
    __tablename__ = 'Candidates'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    First_Name = Column(String(100), nullable=False)
    Last_Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    Application_Date = Column(Date, nullable=False)
    Country = Column(String(100), nullable=False)
    YOE = Column(Integer, nullable=False)  # Years of Experience
    Seniority = Column(String(100), nullable=False)
    Technology = Column(String(100), nullable=False)
    Code_Challenge_Score = Column(Integer, nullable=False)
    Technical_Interview_Score = Column(Integer, nullable=False)

    def __str__ (self):
        return f"Candidate(id={self.id}, firstname={self.firstname}, lastname={self.lastname})"