# 13th Question's Solution
print("Pushpendra Singh \n18EJICS126 \nB.Tech. CSE 6th semester B section")
def named(temp):
    sum = 0
    for i in temp:
        sum = sum +temp[i]
    return sum/7
Temp = {'Sunday':44,'Monday':38,'Tuesday':42,'Wednesday':40,'Thrusday':41,'Friday':30,'Saturday':32}
print(named(Temp))
