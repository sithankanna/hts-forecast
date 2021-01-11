# import relevant python libraries
import pandas as pd

sales = pd.read_csv('/Users/user/hts-forecast/volume/data/raw/sales_train_evaluation.csv')
cal = pd.read_csv('/Users/user/hts-forecast/volume/data/raw/calendar.csv')

#def categorize(frame, category):
 #   newframe = frame[frame.dept_id == category]
  #  newframe2 = newframe.drop(['id', 'dept_id', 'cat_id', 'state_id'], axis = 'columns')
   # return newframe2

#categorize(sales, FOODS_3)