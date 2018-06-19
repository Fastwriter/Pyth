class time:
    def __init__(self, h=0, m=0 ,s=0):
        self.second=s%60
        self.minute=(m+s//60)%60
        self.hour=(h+(m+s//60)//60)%24
    def __str__(self):
        return('%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))
    def __add__(self, other):
        t=time()
        a=self.second+other.second
        b=self.minute+other.minute
        c=self.hour+other.hour
        t.second=a%60
        t.minute=(b+a//60)%60
        t.hour=(c+(b+a//60)//60)%24
        return t

t1=time(11,2,58)
print(t1)
t2=time(10,57,2)
print(t2)
print(t1+t2)
