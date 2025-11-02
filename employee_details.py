class programmer:
    def __init__(self,name,salary,commission):
        self.name = name
        self.salary=salary
        self.commission=commission

p = programmer("shivam",1000000,200000)
print(p.name,p.salary,p.commission)

p2= programmer("abhay",200000,20000)
print(p2.name,p2.salary,p2.commission)

p3 = programmer("kapil",300000,2000)
print(p3.name,p3.salary,p3.commission)
        
