def score(x):
    const = 10000000000000.0
    score = 0
    for i in x:
        score= (const)*(ord(i)-25) + score  
        const = const/27
    return score
lop=["akadn","lapqkiik","aaaaa","lakaka","zsebro","qpowi","abcd","aaaa","zzzz"]
for x in lop:
    print(score(x))
print()
lop.sort()
for x in lop:
    print(score(x))
mq = None
asdf = [1,3,mq]
print(all(asdf))