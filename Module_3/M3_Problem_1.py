class Person:
    def set_details(self,name,age):
        self.name=name
        self.age=age

p=Person()
p.name='Alice'
p.age=25

print("Name :",p.name)
print("Age  :",p.age)