import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

books = pd.read_csv('books.csv')
music = pd.read_csv('music.csv')
ratings = pd.read_csv('ratings.csv')

bookratings = pd.merge(ratings,books,on='bookid')
musicratings = pd.merge(ratings,books,on='musicid')

bookmatrix = bookratings.pivot_table(index='userid',columns='bookid',values='rating').fillna(0)
musicmatrix = musicratings.pivot_table(index='userid',columns='musicid',values='rating').fillna(0)

def filtering(matrix):
    similaritymatrix=cosine_similarity(matrix,dense_output=True)
    recommendations = {}
    for userindex,userrows in enumerate(matrix):
        similarusers = similaritymatrix[userindex]
        userratings = userrows
        
        similaruserindices = np.argsort(-similaruser)[1:]
        similaruserratings = matrix[similaruserindices]

        weightedsum = np.dot(similaruserratings.T,similarusers[1:])
        weightedaverage = weightedsum/np.sum(np.abs(similarusers[1:]))

        recommendationscores = np.where(userratings == 0,weightedaverage,0)

        topindices = np.argsort(-recommendationscores)[:5]

        recommendations[userindex] = topindices.tolist()

        return recommendations

bookrecommendations = filtering(bookmatrix)
musicrecommendations = filtering(musicmatrix)
print("Book Recommendations for user :")
for bookid in bookrecommendations[1]:
    booktitle=book.loc[books['bookid'] == bookid,'title'].value[0]
    print(booktitle)


print("\nMusic Recommendations for user 1:")
for musicid in musicrecommendations[1]:
    musictitle = music.loc[music['musicid'] == musicid,'title'].value[0]
    print(musictitle)


