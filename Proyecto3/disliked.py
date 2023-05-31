import pandas as pd
import random
from datetime import datetime, timedelta

users = pd.read_csv('Users.csv')
films = pd.read_csv('Film.csv')
liked = pd.read_csv('Liked.csv')
watched = pd.read_csv('Watched.csv')

n = len(users)
m = len(films)

comments = ['Horrible film, one of the worst I have seen,', 'I never watch it again!', 'Awful!', 'One of the best worst I have watched', 'Terrible film, would not recommend',
            'It made me angry', 'Awful plot', 'C-tier visuals', 'Okay cinematography']

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
    for j in range(random.randint(0, len(watched.loc[watched['UserID']==userId+1][['UserID', 'MovieID']])-1)):
        rand_date = random_date(start_date, end_date)
        random_movie = random.randint(0,m-1)
        while random_movie+1 in list(liked.loc[liked['UserID']==userId]['MovieID']) and random_movie+1 not in list(watched.loc[watched['UserID']==userId]['MovieID']):
            random_movie = random.randint(0,m-1)
        comment = random.sample(comments, random.randint(1,3))
        genre = films['Genre'][random_movie]
        rating = random.randint(1,3)
        Userids.append(userId+1)
        Movieids.append(random_movie+1)
        rateDates.append(rand_date)
        Genres.append(genre)
        Ratings.append(rating)
        Comments.append(comment)
        

    

disliked = pd.DataFrame({'UserID':Userids, 'MovieID':Movieids, 'RateDates':rateDates, 'Genres':Genres, 'Ratings':Ratings, 'Comments':Comments})
disliked.to_csv('Disliked.csv',index=False)