{% include navbar.html %}



# Data Structures replit



<div class="row justify-content-center" style="margin: 2%;">
    <iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@Pqhantom/Tri-3-Matthew-Cao-Manaka-2?lite=true#menu.py">
    </iframe>
</div>

# Code Snippets 

## Week 2
This Week I learned about OOP which is Object Oriented Programming. I don't really have too good of a grasp on it yet but here is the factorial function using it. 
```
class Factorial:
  def __init__(self):
    self.factorial = [1,1]
    
  def __call__ (self,num):
    if num <= 1:
      pass #goes to the end return statement
    else:
      self.factorial.append(num * self(num-1)) 
    return self.factorial[num]
```

## Week 1
This week I made a database and printed the information using a for loop, a while loop, and a recursive loop. Below is an example of the while loop. 
```
def while_loop(): #prints using a while loop
    n = 0
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

```

## Week 0
The very first one, This week I learned how to make a menu using some very cool lists. Below you can see lists for a menu and it's submenu.
```
w1_list = [
  ["Fibonacci", fibonacci.Fibonacci],
  ["Database", database.tester]
]

alist = [
  ["Database For Loop", database.for_loop],
  ["Database While Loop", database.while_loop],
  ["Database Recursive Loop", database.rec_loop],  
]
```
