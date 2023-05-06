"""
Milestone 1:  Immutable vs Mutable objects
Create 1 var, then a 2nd var that is equal to the first.
Change one of the 2 vars and see what happens.
If the type allows, try changing both the contents (an element
in a list or dict) as well as setting equal to a new obj.
"""

# int test (immutable object)
a = 1
b = a
# Change one of the vars and see what happens
b = 2
print('Binding for b has changed from 1 to 2--> id(a) =',id(a),a,'id(b) =',id(b),b)  

# float test (immutable object)
c = 1.1
d = c
# Change one of the vars to see what happens
d = 2.1
print('Binding for d has changed from 1.1 to 2.1--> id(c) =',id(c),c,'id(d)=',id(d),d)  

# str test (immutable object)
e = 'e'
f = e
f = 'f'
print('Binding for f has changed from "e" to "f"--> id(e)=',id(e), e,'id(f)= ', id(f),f)

#list test (mutable object)
g = [1,2,3]
h = g
h[1] *= 100
print('Binding for h is the same as the binding for g--> id(g)=',id(g), g,'id(h) =',id(h),h)

#tuple test (immutable object)
i = (1,2,3)
j = i
#j[1] = 200  tuples are immutable --> results in a TypeError
j = (3,4,5)
print('Binding for j has changed from "i" to "j"--> id(i)=',id(i),i,'id(j)=',j)

#dict test (mutable object)
k = {'a':1, 'b':2, 'c':3}
l = k
l['b'] *= 100
print('Binding for l is the same as the binding for l--> id(k)=',id(k), k,'id(l) =',id(l),l)

print()
print()
#Print understanding of how variables behave
print('1. Variables assigned to mutable objects keep the same binding and refer to the same object')
print('2. Variables assigned to immutable objects change their binding because the objects are immutable and refer to a different object instead.')
