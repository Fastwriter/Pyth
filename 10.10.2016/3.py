def count(word, letter):
    count=0
    for index in word:
        if(index == letter):
            count = count + 1
    print(count)

count('qwyreioujknlfvfwjifnklsmf cldskf', 'f')
