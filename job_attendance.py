import pandas as pd
import matplotlib as plt

filename="/content/drive/MyDrive/Tasks_project/att_report.csv"

att_data = pd.read_csv(filename, index_col="Card Number")
att_data.head(10)

sort_d = att_data.sort_values(['Name', 'Gen Time'], ascending=True)
sort_d.head(12)


reset = sort_d.reset_index()
a = reset["Gen Time"].str.split(" ", expand=True)
x = a[0]
y = a[1]

print(a)
print(x)
print(y)


a["Name"] = reset["Name"]
a.head(10)

a["Name"]


a1 = a.rename(columns={0:"Date", 1:"Time"})
a1.head(12)



a_gr = a1.groupby(["Date", "Name"]).Time.min()
aa1 = pd.DataFrame(a_gr)
aa1 = aa1.rename(columns={"Time":"Intime"})
#a_gr["1"]
#print(a_gr.head(20))
a_gr = a1.groupby(["Date", "Name"]).Time.max()
aa1["Outtime"] = (pd.DataFrame(a_gr)).Time
aa1
#print(a_gr.head(20))
print(aa1.head(20))
print(aa1.tail(20))


aa1.to_csv("/content/drive/MyDrive/Tasks_project/one.csv")

df = pd.read_csv("/content/drive/MyDrive/Tasks_project/one.csv")
df.head()
