from turtle import speed


d = int(input("Enter the total distance in meters :",))
h = int(input("Enter the time in hours :",))
m = int(input("Enter the time in minutes :",))
s = int(input("Enter the time in seconds :",))
speed1 = d/(h*3600+m*60+s)
speed2 = (d/1000)/(h+(m/60))+(s/3600)
speed3 = (d*.6213/1000)/(h+(m/60))+(s/3600)
print("Your speed in meter/sec is :",speed1)
print("Your speed in Km/hr is :",speed2)
print("Your speed in Miles/hr is :",speed3)