import seaborn as sns
import pandas as pd 
from matplotlib import pyplot as plt 
df=pd.read_excel('data.xlsx')
#sns.scatterplot(x="Gender",y="Purchase Iphone",hue="Salary",data=df)
#2
#sns.distplot(df['Age'])
#3
#sns.distplot(df['Age'],hist=True,color='green')  
#4 
#sns.barplot(x="Gender",y="Purchase Iphone",data=df)
#5
#sns.lineplot(x='Gender',y='Purchase Iphone',data=df)
#6
sns.boxplot(x='Gender',y='Purchase Iphone',data=df)
plt.title("Iris Gender Vs Iphone")
plt.xlabel("Gender")
plt.ylabel("Purchase Iphone")
plt.show()