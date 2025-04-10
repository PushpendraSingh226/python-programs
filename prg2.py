Star_pattern = "*********"
for i in range(1,len(Star_pattern)):
    print(Star_pattern[1:i+1])
    for j in range(1,len(Star_pattern)):
     print(Star_pattern[1:-j+1])
