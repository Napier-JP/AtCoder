# Python3 備忘録

PerlとかC#とかいろいろ触っているうちに母語に訛りが生じないように…

## 基本構文

### list, tuple, set, dictionary
* emptyList = []

```
li = ["piyo", True, 1729]
print(li[-1]) # 1729
print(len(li)) # 3
li.append("foo") # ["piyo", True, 1729, "foo"]
print(len[3:1:-1]) # ["foo", 1729]
print(li.pop(0)) # "piyo", and li is [True, 1729, "foo"]
```

* emptyTuple = ()
* singleElemTuple = (42,)

Elements in a tuple are immutable.

* emptySet = set()

```
someSet = set(2, 4, 7)
someSet.add(9) # set(2,4,7,9)
someSet.add(4) # set(2,4,7,9)
someSet.remove(2) # set(4,7,9)

otherSet = set(5, 7)
print(someSet & otherSet) # set(7)
```

* emptyDict = {}     or dict()
* someDict = {"key1": 1, "key2": False, "key3":[3,14,15,92]}


### print
* print("some-string-here")
* print(someInt + anotherInt)

### if, for, while
* if <CONDITION>: do something

```
if someVar == "meets condition" && functionThatReturnsTrue(arg1, arg2):
    doSomething()
elif blah is True:
    doOtherThing()
else:
    pass
```

* for Var in String/List/other iterables: do something(Var)

```
for _ in range(3):
    beep()
```

```
for name in personList:
    print("Hello %s" %(name))
```

```
evenNumberSequenceList = [num * 2 for num in range(3,8)] #[6,8,10,12,14]