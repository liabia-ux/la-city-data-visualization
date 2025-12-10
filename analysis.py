# Khalia Anderson 12/05/25
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Creating a scatterplot for Council District and the Start Year

#Reading my data from HW#4
city_df = pd.read_json('https://data.lacity.org/resource/tkh9-tssh.json')

#I had to figure out how to convert the location start date into just a singular year hence a new column called start_year
city_df['start_year'] = pd.to_datetime(city_df.location_start_date).dt.year

#Since this is two informations of data instead of one series, I have two (including my newly created one so that they can be ploted together.
council_district_series = city_df.council_district
start_year_series = city_df.start_year

fig = plt.figure()

#Creating a scatterplot with seaborn
sns.scatterplot(x=start_year_series, y=council_district_series, hue=council_district_series)

#This is creating the title
plt.title("Council District by Business Start Year")

#This is creating the X-Axis 
plt.xlabel("Start Year")

#This is creating the Y-Axis 
plt.ylabel("Council District")

#This is is me saving the figure
plt.savefig("Council district by start year", dpi=300)
plt.show()

############################################################################################
#Creating a histogram for Council District and how many are in each district

#Reading my data
city_df = pd.read_json('https://data.lacity.org/resource/tkh9-tssh.json')

council_district_series = city_df.council_district

fig = plt.figure()

#Creating a histogram with seaborn
sns.histplot(council_district_series)

#This is creating the title
plt.title('Distribution of Council Districts')

#This is creating the X-Axis 
plt.xlabel('Council District')

#This is creating the Y-Axis 
plt.ylabel('Frequency')

#This is bringing it all together and showing it 
plt.show()

