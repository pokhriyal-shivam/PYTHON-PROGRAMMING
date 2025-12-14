number = [2,4,6,5,1,8,3]

new = [n*n for n in number if n%2 == 0]

print("originallist" , number )
print("updatedlist" , new)
