#open a file
# file = open('seaslug.txt',mode='r')
# print(file.read())
# #Check whether file file is closed
# print(file.closed)
# #Close file
# file.close()
# print(file.closed)

#read & print the first 3 lines
# with open('seaslug.txt') as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#import this

####Using NumPy to import flat files
# import numpy as np
# filename ='mnist_kaggle_some_rows.csv'
# digits = np.loadtxt(filename, delimiter=',')
# print(type(digits))
# #select and reshape a row
# im = digits[21,1:]
# im_sq = np.reshape(im,(28,28))
# #plot reshape data
# import matplotlib.pyplot as plt
# plt.imshow(im_sq,cmap ="Greys",interpolation="nearest")
# plt.show()

##Customizing your Numpy import
# import numpy as np
# filename ='mnist_kaggle_some_rows.csv'
# data  = np.loadtxt(filename,delimiter=',',usecols=[0,3],skiprows=1)
# print(data)

##Importing different datatypes
# import numpy as np
# file = 'seaslug.txt'
# data = np.loadtxt(file, delimiter='\t',dtype=str)
# print(data)
# data_float = np.loadtxt(file,delimiter='\t',dtype=float,skiprows=1)
# print(data_float[9])
# #Plot a scatterplot of the data
# import matplotlib.pyplot as plt
# plt.scatter(data_float[:,0],data_float[:,1])
# plt.xlabel('time(min.)')
# plt.ylabel('percentage of larve')
# plt.show()

##Working with mixed datatypes (1)
# import numpy as np
# data = np.genfromtxt('titanic_sub.csv',delimiter=',',names =True,dtype=None)
# print(data['Survived'])
# ##Working with mixed datatypes (2)
# d = np.recfromcsv('titanic_sub.csv',delimiter=',',names =True,dtype=None)
# print(d[:3])

####Importing flat files using pandas
##Using pandas to import flat files as DataFrames (1)
# import pandas as pd
# file = 'titanic_sub.csv'
# df = pd.read_csv(file)
# #View the head of the DataFrame
# print(df.head())

##Using pandas to import flat files as DataFrames (2)
import numpy as np
import pandas as pd
file = 'mnist_kaggle_some_rows.csv'
#read the first 5 rows of the file into a DataFrame
data = pd.read_csv(file,nrows=5,header=None)
#Buid a numpy array from the DataFrame
data_array = data.values
print(type(data_array))

##Customizing your pandas import
# import matplotlib.pyplot as plt
# file = 'titanic_sub.csv'
# #na_values as NA or NaN,sep="\t"
# data = pd.read_csv(file,sep=',',comment="#",na_values=['Nothing'])
# print(data.head())
# #plot 'Age' Variable in a histogram
# pd.DataFrame.hist(data[['Age']])
# plt.xlabel('Age (years)')
# plt.ylabel('count')
# plt.show()

####Not so flat any more
# import os
# wd = os.getcwd()
# print(os.listdir(wd))

##Loading a pickled file
# import pickle
# with open('data.pkl',mode='rb') as file:
#     d = pickle.load(file)
# print(d)
# print(type(d))

##Listing sheets in Excel files
# import pandas as pd
# file ='battledeath.xlsx'
# x1 = pd.ExcelFile(file)
# print(x1.sheet_names)
##Importing sheets from Excel files
# df1 = x1.parse('2004')
# print(df1.head())
# #load a sheet into a DataFrame by index
# df2 = x1.parse(0)
# print(df2.head())
##Customizing your spreadsheet import
# df1 = x1.parse(0,skiprows=[0],names=['Country','AAM due to War (2002)'])
# print(df1.head())
# # Parse the first column of the second sheet and rename the column: df2
# df2 = x1.parse(1, parse_cols=[0,1], skiprows=[0],names=['Country','2004'])
# print(df2.head())

#### importing SAS files
# Import sas7bdat package
# from sas7bdat import SAS7BDAT
# import matplotlib.pyplot  as plt
# # Save file to a DataFrame: df_sas
# with SAS7BDAT('sales.sas7bdat') as file:
#     df_sas = file.to_data_frame()
# # Print head of DataFrame
# print(df_sas.head())
# # Plot histograms of a DataFrame feature (pandas and pyplot already imported)
# pd.DataFrame.hist(df_sas[['P']])
# plt.ylabel('count')
# plt.show()
# ##Using read_stata to import Stata files
# df = pd.read_stata('disarea.dta')
# print(df.head())
# pd.DataFrame.hist(df[['disa10']])
# plt.xlabel('Extent of disease')
# plt.ylabel('Number of countries')
# plt.show()

####Using File to import HDF5 files
# Import packages
# import numpy as np
# import h5py
# # Assign filename: file
# file =  'LIGO_data.hdf5'
# # Load file: data
# data = h5py.File(file, 'r')
# # Print the datatype of the loaded file
# print(type(data))
# # Print the keys of the file
# for key in data.keys():
#     print(key)
# # Get the HDF5 group: group
# group = data['strain']
# # Check out keys of group
# for key in group.keys():
#     print(key)
# ##Extracting data from your HDFS file
# # Set variable equal to time series data: strain
# strain = data['strain']['Strain'].value
# # Set number of time points to sample: num_samples
# num_samples = 10000
# # Set time vector
# time = np.arange(0, 1, 1/num_samples)
# # Plot data
# plt.plot(time, strain[:num_samples])
# plt.xlabel('GPS Time (s)')
# plt.ylabel('strain')
# plt.show()


####load mat file --MATLAB file
# Import package
# import scipy.io
# import matplotlib.pyplot as plt
# # Load MATLAB file: mat
# mat = scipy.io.loadmat('ja_data2.mat')
# # Print the datatype type of mat
# print(type(mat))
# print(mat.keys())
# print(type(mat['CYratioCyt']))
# print(np.shape(mat['CYratioCyt']))
# # Subset the array and plot it
# data = mat['CYratioCyt'][25, 5:]
# fig = plt.figure()
# plt.plot(data)
# plt.xlabel('time (min.)')
# plt.ylabel('normalized fluorescence (measure of expression)')
# plt.show()


####Introduction to relational databases
##Creating a database engine
# from sqlalchemy import create_engine
# import pandas as pd
# engine = create_engine('sqlite:///Chinook.sqlite')
# print(engine.table_names())
# con = engine.connect()
# re = con.execute('select * from album')
# df = pd.DataFrame(re.fetchall())
# con.close()
# print(df.head())
##Customizing the Hello World of SQL Queries
# Open engine in context manager
# Perform query and save results to DataFrame: df
# with engine.connect() as con:
#     rs = con.execute("SELECT LastName, Title FROM Employee where employeeid >=6 order by BirthDate")
#     df = pd.DataFrame(rs.fetchmany(size=3))
#     df.columns = rs.keys()
# # Print the length of the DataFrame df
# print(len(df))
# # Print the head of the DataFrame df
# print(df.head())

####Querying relational databases directly with pandas
# Execute query and store records in DataFrame: df
# df = pd.read_sql_query("SELECT * FROM Album", engine)
# # Print head of DataFrame
# print(df.head())
# # Open engine in context manager and store query result in df1
# with engine.connect() as con:
#     rs = con.execute("SELECT * FROM Album")
#     df1 = pd.DataFrame(rs.fetchall())
#     df1.columns = rs.keys()
# # Confirm that both methods yield the same result
# print(df.equals(df1))

##Pandas for more complex querying
# df2 = pd.read_sql_query(
#     "SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate",
#     engine)
# print(df2.head())
#
# ##The power of SQL lies in relationships between tables: INNER JOIN
# with engine.connect() as con:
#     rs1 = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
#     df4 = pd.DataFrame(rs1.fetchall())
#     df4.columns = rs1.keys()
# # Print head of DataFrame df
# print(df4.head())
#
# ##Filtering your INNER JOIN
# df5 = pd.read_sql_query(
#     "SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
#     engine
# )
# # Print head of DataFrame
# print(df5.head())


####Importing flat files from the web
# from urllib.request import urlretrieve
# import matplotlib.pyplot as plt
# import pandas as pd
# url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# # urlretrieve(url,'winequality-red.csv')
# # df = pd.read_csv('winequality-red.csv',sep=';')
# # print(df.head())
# ##Opening and reading flat files from the web
# df = pd.read_csv(url,sep=';')
# print(df.head())
# #plot first column of df
# pd.DataFrame.hist(df.ix[:,0:1])
# plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$')
# plt.ylabel('count')
# plt.show()
# print(df.columns)

##Importing non-flat files from the web xls
# url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# x1 = pd.read_excel(url,sheet_name=None)
# #print the sheetname to the shell
# print(x1.keys())
# #print the head of the firs sheet(using its name ,NOT its index
# print(x1['1700'].head())

####Performing HTTP requests in Python using urllib
# from urllib.request import urlopen,Request
# url = "http://www.datacamp.com/teach/documentation"
# request = Request(url)
# #Sends the request and catches the response
# response = urlopen(request)
# print(type(response))
# html = response.read()
# print(html)
# response.close()

####Performing HTTP requests in Python using requests
# import requests
# url = "http://www.datacamp.com/teach/documentation"
# r = requests.get(url)
# text = r.text
# print(text)

####Parsing HTML with BeautifulSoup
# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.python.org/~guido/'
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc)
# pretty_soup = BeautifulSoup.prettify(soup)
# #print(pretty_soup)
# # Get the title of Guido's webpage: guido_title
# guido_title = soup.title
# #print(guido_title)
# guido_text = soup.get_text()
# #print(guido_text)
# # Find all 'a' tags (which define hyperlinks): a_tags
# a_tags = soup.find_all('a')
# #print the urls to the shel
# for link in a_tags:
#     print(link.get('href'))

####Introduction to APIs and JSONs
##Loading and exploring a JSON
#load JSON:json_data
# import json
# with open('a_movie.json') as json_file:
#     json_data = json.load(json_file)
# #print each key-value pair in json_data
# for k in json_data.keys():
#     print(k +":",json_data[k])

####API requests
##http://www.omdbapi.com/
import requests
import json
# Assign URL to variable: url
# url = 'http://www.omdbapi.com/?apikey=ff21610b&t=the+social+network'
# r = requests.get(url)
# #print(r.text)
# json_data = r.json()
# for k in json_data.keys():
#     print(k + ":" ,json_data[k])

##Checking out the Wikipedia API
# Assign URL to variable: url
# url ='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
# # Package the request, send the request and catch the response: r
# r = requests.get(url)
# # Decode the JSON data into a dictionary: json_data
# json_data = r.json()
# # Print the Wikipedia page extract
# pizza_extract = json_data['query']['pages']['24768']['extract']
# print(pizza_extract)


# Import package
import tweepy
import MyStreamListener
# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Initialize Stream listener
l = MyStreamListener()
# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)
# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])
##Load and explore your Twitter data
# Import package
import json
# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'
# Initialize empty list to store tweets: tweets_data
tweets_data = []
# Open connection to file
tweets_file = open(tweets_data_path, "r")
# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
# Close connection to file
tweets_file.close()
# Print the keys of the first tweet dict
print(tweets_data[0].keys())
# Import package
import pandas as pd
# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
# Print head of DataFrame
print(df.head())
##A little bit of Twitter text analysis
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]
# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
##Plotting your Twitter data
# Import packages
import matplotlib.pyplot as plt
import seaborn as sns
# Set seaborn style
sns.set(color_codes=True)
# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']
# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
