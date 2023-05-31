import pandas as pd
import random
from datetime import datetime, timedelta

users = pd.read_csv('Users.csv')
persons = pd.read_csv('Person.csv')
liked = pd.read_csv('Liked.csv')
watched = pd.read_csv('Watched.csv')

n = len(users)
m = len(persons)

comments = ['Amazing acting, one of my favorites,', 'I would watch them again!', 'Great!', 'One of the best performances I have seen', 'Good acting, would recommend watching them',
            'They made me cry', 'Amazing performance', 'Incredible dynamics', 'Outstanding vocabulary']


Userids = []
Personids = []
rateDates = []
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


count = 0

for i in range(int(n)):
    for j in range(random.randint(1,5)):
        user = random.randint(0,n)
        rand_date = random_date(start_date, end_date)
        random_person = random.randint(0,m)
        comment = random.sample(comments, random.randint(0,3))
        rating = random.randint(3,5)
        Userids.append(user)
        Personids.append(random_person)
        rateDates.append(rand_date)
        Ratings.append(rating)
        Comments.append(comment)
        

    

follows = pd.DataFrame({'UserID':Userids, 'PersonID':Personids, 'Followed_since':rateDates,'Ratings':Ratings, 'Comments':Comments})
follows.to_csv('Follows.csv',index=False)