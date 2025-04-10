print("Pushpendra Singh B3 Section")
print("--------------\nTime is:")
class Time:
    pass
time= Time()
time.hours = 9
time.minutes = 45
time.seconds = 49
def  print_time(t1):
    ct=Time()
    ct.hours =t1.hours
    ct.minutes = t1.minutes
    ct.seconds = t1.seconds
    print(ct.hours,":",ct.minutes,":",ct.seconds)

print_time(time)
