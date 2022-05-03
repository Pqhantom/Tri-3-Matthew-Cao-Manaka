{% include navbar.html %}



# Create Task Here
[Code](https://github.com/Pqhantom/Mathue-s-Cre8-Task/blob/main/trivia.py)
    
### Written Response
3a. 
The purpose of the program is to determine whether or not the user is human enough to answer basic questions about animals correctly. The program can also serve to gauge whether or not the user should be respected amongst their peers or not. The user is asked a question and is instructed to type a response. The program will determine whether or not the user is correct and give them an appropriate response. The input of the program is the user’s answer and the output of the program is whether or not they were correct. 

3b. i
	qadb = [] 
qadb.append({
  "Question": "What animal goes Meow?",
  "Answer": "cat"
})
qadb.append({
  "Question": "What animal goes Moo?",
  "Answer": "cow"
})
qadb.append({
  "Question": "What animal goes woof?",
  "Answer": "dog"
})

ii.
def brain():
  print("In order to prove your humanity please type the answer to the following question.")
  n = random.randint(0, 2)
  question = qadb[n]["Question"]
  x = input(question + "\n")
  checker(x, n, question) 
Iii-v.
The name of the list being used in the program is qadb which stands for Question Answer DataBase. The data that is contained in the list is, well, a Question and an Answer. The list manages complexity in my program because if I didn’t use a list the only other way I’d know how to make this is to have each question and answer set be in separate functions with all of the code to check for the user’s input and correctness underneath. Then I would have the program randomly choose the whole set of question, answer, input code, and output code. In other words it would probably triple the length of my program with redundant code. 



3c. i
	def checker(x, n, question): # procedure with three parameters
  if x == qadb[n]["Answer"]: # selection
   print("C O N G R A T U L A T I O N S  Y O U  A R E  A  H U M A N !")
   quit()
   
  else: 
    while x != question: # iteration 
      print("Unfortunately you are a robot.")
      x = input(question + "\n") # sequencing
      checker(x, n, question)
ii.
	def brain():
  print("In order to prove your humanity please type the answer to the following question.")
  n = random.randint(0, 2)
  question = qadb[n]["Question"]
  x = input(question + "\n")
  checker(x, n, question) # call to procedure
Iii-iv.
The algorithm’s name is checker and what it does is it gets three parameters; x, n, and question. These three parameters lets the program know what the user’s input was, which question and answer set is being used, and the question that is being used. When the algorithm is called the first thing that it does is compare the answer to the user’s response and sees if they are the same. If they are the same it will print out a message telling them they are right and then end the program. If it sees that the user’s input is not the same as the answer it will instead display a message telling them that they are not correct and start a loop that will allow the user to keep guessing until they get it right. 

3d. 
The first test case is if the user gets the question right on the first try. If the question is, “What animal goes meow?” and the user types “cat” then the program will print a message telling them that they are right and end. In the second case if the user instead types “dog” for the question, “what animal goes meow?” it will tell them that they are wrong and ask them the question again. If they continue to get the question wrong the program will simply keep telling them so and asking the same question until they get it right. Once they get it right it will congratulate them and end. 
The first test case is if the user gets the question right on the first try. If the question is, “what animal goes meow?” and the user types “cat” the program will compare their input with the answer from the list. Since the input matches it will tell the user that they are right and end the program. In the Second scenario the user will get the answer wrong multiple times before getting the right answer. If the question is still, “what animal goes meow?” but this time the user responds with “dog” then the program will compare the answer with the input and see that they do not match. Because they do not match and therefore are wrong the program will now tell the user that they are wrong and ask them the question again. It will keep telling them that it is wrong and ask them the question until they respond with the correct answer. 

### Crossover Comment
Code meets all collegeboard requirements, written portion is a bit unorganized. The code should be formatted in the code style instead of just copy and pasted on.
