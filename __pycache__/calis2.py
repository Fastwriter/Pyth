class time:
    def __init__(self, h=0, m=0, s=0):
        self.second=s%60
        self.minute=(m+s//60)%60
        self.hour=(h+(m+s//60)//60)%24
    def __str__(self):
        return ('%.2d:%.2d:%.2d' %(self.hour,self.minute, self.second))
    def __add__(self, self2):
        tad=time()
        tad.second=(self.second+self2.second)%60
        tad.minute=((self.minute+self2.minute)+(self.second+self2.second)//60)%60
        tad.hour=(((self.hour+self2.hour)+(((self.minute+self2.minute)+(self.second+self2.second)//60))//60)%24)
        return tad

t=time(10, 59, 62)
t2=time(11, 45, 44)
print(t+t2)
