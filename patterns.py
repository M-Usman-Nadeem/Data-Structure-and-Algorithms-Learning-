# pattern 1
# star_pattern_one=""
n = int(input())
# for i in range(n):
#     for j in range(n):
#         star_pattern_one+="*"
#     if(i!=(n-1)):
#      star_pattern_one+="\n"

# print(star_pattern_one)
# star_pattern_two
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
# print(end="\n")
# star_pattern_three
# for i in range(1, n+1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(1, i*2):
#         print("*", end="")
#     print(end="\n")
# star_pattern_four
# for i in range(n,0,-1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(1, i*2):
#         print("*", end="")
#     print(end="\n")
    # star_pattern_five
for i in range(1,n+1):
    number_pattern=""
    for j in range(1,i+1):
     number_pattern= str(1 if j%2!=0 else 0) + number_pattern
    print(number_pattern)