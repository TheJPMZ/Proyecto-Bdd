import pandas as pd
import random
from datetime import datetime, timedelta

users = pd.read_csv('Users.csv')
films = pd.read_csv('Film.csv')
watched = pd.read_csv('Watched.csv')
print(watched)

n = len(users)
m = len(films)

comments = ['Amazing film, one of my favorites,', 'I would watch it again!', 'Great!', 'One of the best movies I have watched', 'Good film, would recommend',
            'It made me cry', 'Amazing plot', 'Incredible visuals', 'Outstanding cinematography']

Userids = []
Movieids = []
rateDates = []
Genres = []
Ratings = []
Comments = []
random.seed(230901)


def random_date(start_date, end_date):
    # Convert start and end dates to datetime objects
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the total number of days between the start and end dates
    total_days = (end_datetime - start_datetime).days

    # Generate a random number of days offset
    random_days = random.randint(0, total_days)

    # Add the random number of days to the start date
    random_date = start_datetime + timedelta(days=random_days)

    # Format the random date as a string
    random_date_str = random_date.strftime("%Y-%m-%d")

    return random_date_str


start_date = "2022-01-01"
end_date = "2023-05-30"

movies = films['ID']
user = users['ID']

count = 0

for userId in range(n):
    for j in range(random.randint(0,len(watched.loc[watched['UserID']==userId+1][['UserID', 'MovieID']]))):
        rand_date = random_date(start_date, end_date)
        random_movie = random.randint(0,m-1)
        us_watched = watched.loc[watched['UserID']==userId+1][['UserID', 'MovieID']]
        #print(" ")
        #print(us_watched)
        #print(" ")
        while random_movie+1 not in list(us_watched['MovieID']):
            random_movie = random.randint(0,m-1)
        comment = random.sample(comments, random.randint(1,3))
        genre = films['Genre'][random_movie]
        rating = random.randint(3,5)
        Userids.append(userId+1)
        Movieids.append(random_movie+1)
        rateDates.append(rand_date)
        Genres.append(genre)
        Ratings.append(rating)
        Comments.append(comment)
        

    

liked = pd.DataFrame({'UserID':Userids, 'MovieID':Movieids, 'RateDates':rateDates, 'Genres':Genres, 'Ratings':Ratings, 'Comments':Comments})
liked.to_csv('Liked.csv',index=False)