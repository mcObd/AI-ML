import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
from bokeh.plotting import figure, show

# month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# sales = [200, 220, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430]
# plt.plot(month, sales)
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.title('Monthly Sales')
# plt.show()

# # SEABORN
# df = pd.DataFrame(
#     {
#         'class' : ['A','A','B','B'],
#         'Score' : [80,90,85,95]
#     }
# )
#
# sns.barplot(data=df, x='class', y='Score')
# plt.show()

# sns.boxplot(data=df, x='class', y='Score')
# plt.show()

# PLOTLY
# fig = px.bar(x=['Lagos', 'Abuja', 'Ibadan'], y = [15,4,3],
#              labels={'x' : 'City', 'y' : 'Population (In Millions)'},
#              title='City Population'
#              )
# fig.show()

# # BOKEH
p = figure(title='Sales Trend', x_axis_label='Month', y_axis_label='Sales')
p.line([1,2,3,4], [10,25,15,30],line_width=2)
show(p)
