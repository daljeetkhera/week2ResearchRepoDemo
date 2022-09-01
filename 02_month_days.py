month = input("Enter the name of the month: ",)
mydict = {"January":"31 days", "February":"28/29 days", "March":"31 days",
 "April":"30 days", "May":"31 days", "June":"30 days", "July":"31 days",
 "August":"31 days", "September":"30 days", "October":"31 days",
 "November":"30 days", "December":"31 days"}
# if month in mydict(mydict.keys):
print("No. of days:",(mydict.get(month)))
# print(list(mydict.keys()))
# print(mydict.values())
# print(mydict.items())
