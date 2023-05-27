import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

books = pd.read_csv('books.csv')
music = pd.read_csv('music.csv')
ratings = pd.read_csv('ratings.csv')

bookratings = pd.merge(ratings,books,on='bookid')
musicratings = pd.merge(ratings,books,on='musicid')