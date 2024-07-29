n=int(input())
fd={}
fa=[]
for i in range(n):
    word=input()
    if word in fd:
        fd[word]+=1
    else:
        fd[word]=1
        fa.append(word)
print(len(fd))
output=[str(fd[word]) for word in fa]
print(*output)        
