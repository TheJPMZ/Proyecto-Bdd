import pandas as pd
import random


worked = pd.read_csv('Workedwith.csv')
Pcompanies = pd.read_csv('PCompanies.csv')

worked.pop('PersonName')
worked.pop('CompanyName')


random.seed(230901)

worked['CompanyID'] = [random.randint(1,len(Pcompanies)) for i in range(len(worked))]

worked.to_csv('Workedfor.csv', index=False)