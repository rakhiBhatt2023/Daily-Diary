def fun(f): # Passing Functions as Input 
              #👉 Yahan fun ek function hai jo ek aur function ko input (argument) ke roop mein leta hai.
    print(f)   #print(f) se function ka reference print hota hai (uska address)
    f() # Nesting of Functions


def hello():
    print('hello all')

# Passing Function inside another function as input
fun(hello)     