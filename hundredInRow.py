people = list(range(1, 101))  
i = 0
while len(people) > 1:
    i = (i + 1) % len(people)  
    people.pop(i)            
    i = i % len(people)      
print(people[0])               