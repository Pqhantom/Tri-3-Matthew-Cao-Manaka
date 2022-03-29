InfoDb = []
InfoDb.append({
  "FirstName": "Bob",
  "LastName": "Bobbert",
  "Age": "10",
  "Prefered": ["vanilla", " chocolate", " peanut"]
})

InfoDb.append({
  "FirstName": "Rob",
  "LastName": "Robbert",
  "Age": "11",
  "Prefered": ["vanilla", " cookie dough", " peanut"]
})

InfoDb.append({
  "FirstName": "Hob",
  "LastName": "Hobbert",
  "Age": "15",
  "Prefered": ["Strawberry", " chocolate", " banana"]
})


InfoDb.append({
  "FirstName": "Tod",
  "LastName": "Toddert",
  "Age": "17",
  "Prefered": ["guava", " orange", " melon"]
})
#prints the all the data
def print_data(n):
  print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
  print("Age: ",(InfoDb[n]["Age"]),)
  
  print("\t", "Prefered Ice Cream Flavor: ", end="")
  print(",".join(InfoDb[n]["Prefered"]))
  print()

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0) 
    print("Recursive loop")
    recursive_loop(0) 

def for_loop(): #prints usinga for loop C:
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n): #prints using a while loop
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recur_loop(n):   # omits n amount of times 
  if n < len(InfoDb):
    print_data(n)
    recur_loop(n+1)
    return 

