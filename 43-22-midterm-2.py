import numpy as np
gender=[]
daily_screen=[]
num_app=[]
file_open=open("File/mobile_usage_behavioral_analysis.csv","r")
heading=file_open.readline()
line_file = file_open.readline()
while (len(line_file)>0):
    arr = line_file.strip().split(',')
    gender.append(arr[2])
    daily_screen.append(float(arr[4]))
    num_app.append(float(arr[5]))
    line_file = file_open.readline()
file_open.close()
print("Gender List:",gender)
print("Daily Screen List:",daily_screen)
print("Number App List:",num_app)

daily_screen_list=np.array(daily_screen)

print("Daily Screen List Mean:",daily_screen_list.mean())
print("Daily Screen List Max:",daily_screen_list.max())
print("Daily Screen List Min:",daily_screen_list.min())
num_app_list=np.array(num_app)
print("Num App List Mean:",num_app_list.mean())
print("Num App List Max:",num_app_list.max())
print("Num App List Min:",num_app_list.min())

