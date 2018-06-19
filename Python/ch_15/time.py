class time:
    def __init__(self, h=0, m=0, s=0):
        self.hour = (h+(m+s//60)//60)%60
        self.minute = (m+s//60)%60
        self.second = s%60

    def __str__(self):
        return ("%.2d:%.2d:%.2d" %(self.hour, self.minute, self.second))
    def __add__(self, other):
        s=self.second+other.second
        m=self.minute+other.minute
        h=self.hour+other.hour
        a=self.hour = (h+(m+s//60)//60)%60
        b=self.minute = (m+s//60)%60
        c=self.second = s%60
        t=time()
        return time(a,b,c)
t=time(10, 59 , 66)
print(t)
t2=time(2, 2, 34)
print(t2)
t3=t+t2
print(t3)
