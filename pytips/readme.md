## unique elements in a list
```py
alist = [1 ,1, 2, 2, 2, 2, 3]
xlist = []
for a in alist:
    if x not in xlist:
        xlist.append(x)   
```
## lambda function

### sorting list of tuples w.r.t sth
```py
x = [(0.3, {'a' : (1, 2)})  ,  (0.01, {'b' : (2, 2)}), (0.1, {'a' : (1, 2)}), (0.03, {'a' : (1, 2)})]
x.sort(key=lambda x: -x[0])
print(x)
x.sort(key=lambda x: x[0], reverse=False)
print(x)
```
output
```py
[(0.3, {'a': (1, 2)}), (0.1, {'a': (1, 2)}), (0.03, {'a': (1, 2)}), (0.01, {'b': (2, 2)})]
[(0.01, {'b': (2, 2)}), (0.03, {'a': (1, 2)}), (0.1, {'a': (1, 2)}), (0.3, {'a': (1, 2)})]
```
### filter: filter list of tuples w.r.t given criterion
```py
x = [(0.3, {'a' : (1, 2)})  ,  (0.01, {'b' : (2, 2)}), (0.1, {'a' : (1, 2)}), (0.03, {'a' : (1, 2)})]

xlist = list(
    filter(
        lambda x: x[0] < 0.2, x
    )
)

print(xlist)
```
output
```py
[(0.01, {'b': (2, 2)}), (0.1, {'a': (1, 2)}), (0.03, {'a': (1, 2)})]
```
```py
x = [(0.3, {'a' : (1, 2), 'b' : (2, 2)}),  
     (0.01, {'a' : (1, 2), 'b' : (2, 2)}), 
     (0.1, {'a' : (1, 2), 'b' : (.1, 2)}), 
     (0.03, {'a' : (1, 2), 'b' : (2, 2)})]


xlist = list(
    filter(
        lambda x: x[1]['b'][0] == .1, x
    )
)
```
output
```py
[(0.1, {'a': (1, 2), 'b': (0.1, 2)})]
```
### map + filter: filter list of tuples w.r.t given criterion and fetch value first value in filtered tuples
```py
x = [(0.3, {'a' : (1, 2)})  ,  (0.01, {'b' : (2, 2)}), (0.1, {'a' : (1, 2)}), (0.03, {'a' : (1, 2)})]

xlist = list(
    map(
        lambda x : x[0], x
    )
)
print (xlist)

xlist = list(
    map (
        lambda x : x[0],
        filter(
        lambda x: x[0] < 0.2, x
        )
    )    
)

print(xlist)
```
output
```py
[0.3, 0.01, 0.1, 0.03]
[0.01, 0.1, 0.03]
```
