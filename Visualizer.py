import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 220, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430]
plt.plot(month, sales)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.show()

df = pd.DataFrame(
    {
        'class' : ['A','A','B','B'],
        'Score' : [80,90,85,95]
    }
)

sns.barplot(data=df, x='class', y='Score')
plt.show()

sns.boxplot(data=df, x='class', y='Score')
plt.show()
