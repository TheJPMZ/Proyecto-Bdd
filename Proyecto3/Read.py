import pandas as pd
import random
from datetime import datetime, timedelta

users = pd.read_csv('Users.csv')
Originals = pd.read_csv('Original_content.csv')
liked = pd.read_csv('Liked.csv')
watched = pd.read_csv('Watched.csv')

n = len(users)
m = len(Originals)

comments = ['Amazing Book, one of my favorites,', 'I would read it again!', 'Great!', 'One of the best books I have read', 'Good Book, would recommend',
            'It made me cry', 'Amazing plot', 'Incredible story', 'Outstanding scenery']


Userids = []
OGS = []
rateDates = []
authors = []
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

movies = Originals['ID']
user = users['ID']

count = 0

for i in range(int(n/2)):
    for j in range(random.randint(1,2)):
        user = random.randint(0,n)
        rand_date = random_date(start_date, end_date)
        random_book = random.randint(0,m-1)
        comment = random.sample(comments, random.randint(0,3))
        author = Originals['CreatorAuthor'][random_book]
        rating = random.randint(2,5)
        Userids.append(user+1)
        OGS.append(random_book+1)
        rateDates.append(rand_date)
        authors.append(author)
        Ratings.append(rating)
        Comments.append(comment)
        

    

read = pd.DataFrame({'UserID':Userids, 'BookID':OGS, 'RateDates':rateDates, 'Author':authors, 'Ratings':Ratings, 'Comments':Comments})
read.to_csv('Read.csv',index=False)