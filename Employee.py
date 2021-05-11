import pandas as pd


df=pd.read_csv("data.csv")                  #read

print(df)


df['start_time'] = pd.to_datetime(df.start_time)
df['end_time'] = pd.to_datetime(df.end_time)


wages=100
days=30
consider_working_hours=(df.end_time.dt.hour)-(df.start_time.dt.hour)
working_hours=(df.end_time.dt.hour+df.end_time.dt.minute/60)-(df.start_time.dt.hour+df.start_time.dt.minute/60)
monthly_salary=consider_working_hours*wages*days
print(working_hours)
print(monthly_salary)


df["Montly_salary"] = monthly_salary
df.to_csv('output.csv',index=False,columns=['empid','ename',"Montly_salary"])
print(df.columns)         #to print columns names





