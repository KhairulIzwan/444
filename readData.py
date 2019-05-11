#!/usr/bin/env python3

# pandas library
import pandas as pd

# headers name -- since an original file don't have the names header
names = ['distance', 'odo1', 'odo2', 'Q1', 'Q2', 'Q3', 'Q4', 'acc_x', 'acc_y', 'acc_z', 'acc_magnitude_y_and_z', 'gyro_x', 'gyro_y', 'gyro_z', 'time_speed']

# read excel file
df = pd.read_excel('/Users/khairulizwan/Scripts/444/Original Data//444_1.xlsx', sheet_name='Sheet1', header=None, index_col=None, names=names)

print(df.head())
