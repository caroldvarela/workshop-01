from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Candidates(base):
    __tablename__ = 'Candidates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    applicationdate = Column(Date, nullable=False)
    country = Column(String(100), nullable=False)
    yoe = Column(Integer, nullable=False)  # Years of Experience
    seniority = Column(String(100), nullable=False)
    technology = Column(String(100), nullable=False)
    codechallengescore = Column(Integer, nullable=False)
    technicalinterviewscore = Column(Integer, nullable=False)
    hired = Column(Integer, nullable=False)  # 0 or 1

    def __str__ (self):
        return f"{self.Candidates.__table__}"