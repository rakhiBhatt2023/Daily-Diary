name = 'ishant'
# names = 'john', 'jennie', 'jim'
names = ('john', 'jennie', 'jim')

print(name, type(name), id(name))
print(names, type(names), id(names))
print(names[0], type(names[0]), id(names[0]))

name = 'auribises'
names = 'sia', 'leo', 'kim' # whole tuple elements change so its a new tuple

print(name, type(name), id(name))
print(names, type(names), id(names))

names[0] = 'harry'   # cant cahnge tuple value

# TUPLE: Read Only, IMMUTABLE