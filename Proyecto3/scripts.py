import pandas as pd
import random
from datetime import datetime, timedelta

users = pd.read_csv('Users.csv')
films = pd.read_csv('Film.csv')

n = len(users)
m = len(films)


Userids = []
Movieids = []
watchDates = []
Durations = []
Finished = []
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
while count <=n*5:
    rand_date = random_date(start_date, end_date)
    random_person = random.randint(0,n-1)
    random_movie = random.randint(0,m-1)
    duration = films['Duration'][random_movie]
    random_duration = random.choice([duration/2, duration])
    random_seen = (random_duration == duration)
    Userids.append(random_person+1)
    Movieids.append(random_movie+1)
    watchDates.append(rand_date)
    Durations.append(random_duration)
    Finished.append(random_seen)
    count+=1
    

watched = pd.DataFrame({'UserID':Userids, 'MovieID':Movieids, 'WatchDate':watchDates, 'Duration':Durations, 'Finished':Finished})
watched.to_csv('Watched.csv',index=False)