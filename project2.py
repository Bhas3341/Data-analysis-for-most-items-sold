import pandas as pd
by=pd.read_excel('/Users/bhaskaryuvaraj/Documents/Python project files/Global Superstores.xlsx')

#display first 6 & last 9 lines of data
by.head(6)
by.tail(9)
#check the datatype
#using indexing method extract 3,6 row in 3,5 col
#write a code to see any NA/blank cell is there r not
by.isnull().sum()
#Create a summary Report
by.describe()

#understand the data by India,united state country wise East and central asia region
by['Country'].unique()
cw['Region'].unique()
cw=by[((by['Country']=='India') | (by['Country']=='United States')) & ((by['Region']=='East')|
        (by['Region']=='Central Asia'))]
cw['Country'].unique()
cw.groupby(['Country','Region'])['Sales','Profit','Shipping Cost'].sum()


#understand the data by Us Market where sales>5000
usa=cw[(cw['Country']=='United States') & (cw['Sales']>5000)]

#calculate the profit Margin,Demand Ratio


#Change the column name Product Id to product_id  
by.rename(columns={'Product ID':'product_id'},inplace=True)
#create a subset of india data n perform rest pof the study based on india data only
Ind=by[by['Country']=='India']
#find the total number of record
len(Ind)
#the total number of records is 1555
import datetime as dt
#fint the total revenue generated year on year
Ind['order year']=Ind['Order ID'].str[3:7]
Ind['order year 1']=Ind['Order Date'].dt.year
Ind.groupby('order year')['Profit'].sum()

#order year
#2011    19928.505
#2012    27438.795
#2013    32896.860
#2014    48807.675

#find the category contribution maximum to the total India revenue
total_profit=Ind['Profit'].sum()
Ind.groupby('Category')['Profit'].sum()
#Category
#Furniture          42435.030
#Office Supplies    30544.155
#Technology         56092.650
#from this it is clear that technology contributes maximum to total India revenue

#find Category wise subcategory wise Profit(Total Profit,average profit,Maximum,minimum Profit)
Ind.groupby(['Category','Sub-Category'])['Profit'].sum()
Ind.groupby(['Category','Sub-Category'])['Profit'].mean()
Ind.groupby(['Category','Sub-Category'])['Profit'].max()
Ind.groupby(['Category','Sub-Category'])['Profit'].min()

#what was the month on month sales trend in each of the buiseness year
Ind['month name']=Ind['Order Date'].dt.month_name()
Ind.groupby(['order year','month name'])['Sales'].sum()
#order year  month name
#2011        April          2424.510
#            August        13487.820
#            December       9665.640
#            February       5963.010
#            January         622.710
#            July           1272.375
#            June           7612.275
#            March          2044.800
#            May            3475.260
#            November      17990.835
#            October       15743.190
#            September     11093.580
#2012        April          6252.750
#            August        11774.205
#            December      21221.160
#            February      20274.960
#            January        8953.530
#            July           1523.040
#            June          11902.710
#            March          1736.730
#            May           16633.890
#            November       7728.975
#            October       25352.445
#            September      8138.640
#2013        April          4397.010
#            August        26687.265
#            December      13398.600
#            February       3266.505
#            January        8146.080
#            July           9004.560
#            June          22468.230
#            March          9310.320
#            May           16985.280
#            November      12278.280
#            October        7540.020
#            September     18246.930
#2014        April          9955.200
#            August        23032.305
#            December      12079.545
#            February        153.900
#            January       10048.920
#            July          13223.610
#            June          14672.670
#            March         18782.220
#            May           24865.470
#            November      32858.190
#            October       23856.345
#            September     21503.610

#find the corelation among sales,profit,quantity,discount,shipment cost
Ind['Sales'].corr(Ind['Profit'])
Ind.describe()

#find the order spread across order priority
Ind['Order Priority'].describe()
#the above two questions are related to data science

#find the shipment cost by shipmode
Ind.groupby('Ship Mode')['Shipping Cost'].sum()

#which is the most profitable catgory ,sub catrogary
Ind.groupby(['Category','Sub-Category'])['Profit'].sum().plot(kind='bar')
#overall Technology,phone category, sub-category make the most profit respectively
Ind.groupby('Sub-Category')['Profit'].sum().plot(kind='bar')
#phone sub-category makes the most profit
Ind.groupby('Category')['Profit'].sum().plot(kind='bar')
#technology category makes the most profit

#which product is selling highest all across
Ind['Product Name'].unique()
Ind.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(1)
ab=Ind['Product Name'].unique()
#cardinal Index tab,clear is the highest sold product with a count of 36
#by=Ind.groupby('Product Name')
#by.first()

#which product is selling lowest all across
abc=Ind.groupby('Product Name')['Quantity'].sum().sort_values(ascending=True)==Ind.groupby('Product Name')['Quantity'].sum().sort_values(ascending=True).min()
abc=pd.DataFrame(abc)
abc.groupby('Quantity')["Quantity"].sum()
Ind.groupby('Product Name')['Quantity'].sum().sort_values(ascending=True).head(1)
#Product Name
#Xerox Parchment Paper, Premium            1
#Hon Bag Chairs, Red                       1
#Hon File Folder Labels, 5000 Label Set    1
#Hon Steel Folding Chair, Black            1
#Brother Ink, Digital                      1
#                                         ..
#Stiletto Letter Opener, Steel             1
#StarTech Card Printer, Wireless           1
#StarTech Inkjet, Wireless                 1
#Samsung Signal Booster, with Caller ID    1
#Accos Thumb Tacks, Assorted Sizes         1
#from the above code it is found that 62 products are least sold with count of just 1,with xerox parchment paper,
# premium as 1st in the list
