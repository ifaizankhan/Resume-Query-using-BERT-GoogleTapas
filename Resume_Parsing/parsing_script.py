#Requirements

#Pyresparser
#pip install pyresparser

#spaCy
#python -m spacy download en_core_web_sm

#nltk
#python -m nltk.downloader words
import pyresparser
from pyresparser import ResumeParser
import pandas as pd

r1 = ResumeParser('/Users/faizan/Documents/BASF_Challange/Resume_Parsing/Resume.pdf').get_extracted_data()
r2 = ResumeParser('/Users/faizan/Documents/BASF_Challange/Resume_Parsing/Daniyal.pdf').get_extracted_data()
r3 = ResumeParser('/Users/faizan/Documents/BASF_Challange/Resume_Parsing/Saad.pdf').get_extracted_data()


#Creating list of dictionaries
list_resume = [r1, r2, r3]

#Creating dataframe from dictonaries
df = pd.DataFrame(list_resume)

print(df)