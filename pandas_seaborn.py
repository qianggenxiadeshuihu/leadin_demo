import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pm_data = pd.read_csv("Shanghai_2016_HourlyPM25_created20170103.csv", skiprows=3)
print pm_data.columns

pm_month_day_hour_value = pm_data.loc[:, ['Month', 'Day', 'Hour', 'Value']]
print pm_month_day_hour_value

print "after clean"

pm_month_day_hour_value = pm_month_day_hour_value[pm_month_day_hour_value.Value >= 0]
print pm_month_day_hour_value

print pm_month_day_hour_value.Month.value_counts()
print pm_month_day_hour_value.Day.value_counts()
print pm_month_day_hour_value.Hour.value_counts()
print pm_month_day_hour_value.Value.value_counts()

print pm_month_day_hour_value.describe()

sns.pairplot(pm_month_day_hour_value, diag_kind="kde")

# sns.boxplot(x="Month", y="Value", data=pm_month_day_hour_value)

# sns.jointplot(x="Month", y="Value", data=pm_month_day_hour_value)

plt.show()
