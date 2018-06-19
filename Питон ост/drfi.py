def count_lines(x):
    count=0
    count2=0
    fin = open(x)
    for i in fin:
        count+=1
        for j in i.split():
            count2+=1
    print(count)
    print(count2)
        
