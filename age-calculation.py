import datetime
# from datetime import datetime,date

year = int(input("Please Enter The Year: "))
monthe = int(input("Please Enter The monyh: "))
day = int(input("Please Enter The day: "))

tody_date = datetime.datetime.now()
DBO = datetime.datetime(year,monthe,day)
# print(tody_date)
# print(DBO)
# tody_date = datetime.now()
# tody_date2 =date.today()

age = tody_date - DBO
final_age = age.days / 365
print("Your Age is: " , int(final_age))

