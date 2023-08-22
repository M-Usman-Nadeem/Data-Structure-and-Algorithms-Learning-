# pattern 1
star_pattern_one=""
n=int(input())
for i in range(n):
    for j in range(n):
        star_pattern_one+="*"
    if(i!=(n-1)):
     star_pattern_one+="\n"    

print(star_pattern_one)    
 