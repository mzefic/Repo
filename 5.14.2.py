a = 0
b = 145

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

return_week = b//7
return_day = (b%7)+a
if return_day >= 6:
    return_day = return_day-6

if return_day==0:
    x="Monday"
    #print("It's Monday")
elif return_day==1:
    x="Tuesday"
    #print("It's Tuesday")
elif return_day==2:
    x="Wednesday"
    #print("It's Wednesday")
elif return_day==3:
    x="Thursday"
    #print("It's Thursday")
elif return_day==4:
    return_day="Friday"
    #print("It's Friday")
elif return_day==5:
    x="Saturday"
    #print("It's Saturday")
elif return_day==6:
    x="Sunday"
    #print("It's Sunday")
#else:
    #print("bad input")

print("You will return on ", x,",on the ", return_week, " week")