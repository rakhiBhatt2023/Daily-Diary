from session17G import Visitor

visitor = Visitor()
visitor.add_visitor()
print(visitor.to_CSV)

file = open('Visitors.CSV','a')
file.write(visitor.to_CSV())