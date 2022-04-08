{% include navbar.html %}



# Create Task Here
[Code](https://github.com/danaylevy2004/thesuperidolenthusiasts/blob/main/templates/createtask/hangman.html)
    
### Written Response
3a <br />
i. Describes the overall purpose of the program <br /> 
The purpose of the program is to entertain the user while also being a helpful study tool. <br>
ii. Describes what functionality of the program is demonstrated in the video  <br />
The program will display the word that the user will need to guess with the actual letters replaced with underscores. The user than fills in a text box with their guess. the program will take that guess and compare it with the secret word. this repeats until the user either gives up or gets the word. <br>
iii. Describes the input and output of the program demonstrated in the video <br />
the input is the user's guesses and the output is the underscores changing to their correct guesses and upon completion of the game a note that congratulates them for finishing. <br>

3b two code segments <br />
i. The first program code segment must show how data have been stored in the list.  <br />
```
var words = ["database", "variables", "python", "collaboration", "html", "java", "binary", "string", "data", "data abstraction", "crud", "deployment", "binary search", "binary search", "bits", "bytes", "router",];
```

 <br>
ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.  <br />

```
var word = words[Math.floor(Math.random() * words.length)];
```

iii.  Identifies the name of the list being used in this response <br />
The name of the list is *words* and you can see it being used in the second snippet of code. 
iv.  Describes what the data contained in the list represent in your program <br />
The data contained in the list is the words/terms that are being used in the hangman game. 
v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or
how it would be written differently, if you did not use the list <br />
The way the program works as a whole is that it picks a single word for the user to guess, if there were not to be a list the program would only be able to display one word for the user to guess over and over. In other words the list allows the user to play the game more times than one. 

3c two code segments <br />
i. The first program code segment must be a student-developed procedure that: <br />
□ Defines the procedure’s name and return type (if necessary) <br />
□ Contains and uses one or more parameters that have an effect
on the functionality of the procedure <br />
□ Implements an algorithm that includes sequencing, selection,
and iteration  <br />

```
while (remainingLetters > 0) {
        alert(answerArray.join(" "));
        var guess = prompt ("Guess a letter.");
    }
```

ii. The second program code segment must show where your student-developed procedure is being called in your program. <br />

```
if (guess == null){
            break;
        }    // !== not equal to   (one)
        else if (guess.length !== 1){
            alert("Please use a single letter.");
        }
        else {
            for (var j = 0; j < word.length; j++){
                if (word[j] === guess ){
                    answerArray [j] = guess;
                    remainingLetters--;
                }
            }
        }
```

iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program <br />
The procedure above is taking the user inputs and comparing them to the remaining letters everytime the user makes an new input in order to see if there is a correct letter found. 
iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. <br />
The way the Algorithm above works is that while there are remaining letters for the user to guess the program will prompt the user to make an input. When the user inputs a single letter the algorithm will check to see if it is a correct word. if the user inputs more than one letter the algorithm will instead ask the user to only submit one letter. 

3d <br />
i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. <br />
Our code uses a while statement which means that instead of calling the procedure each time the user submits an answer it will automatically take the submission and compare the input to the answer. An example of this working would be if the secret word was python and the user guessed "o" the algorithm would see that the o is a correct letter and so it will replace one of the underscores with an o instead. 

ii.  Describes what condition(s) is being tested by each call to the procedure  <br />
The condition that is being tested by each call is whether or not the input letter is one that matches with a letter in the secret word. Continuing the example above the condition being tested is whether or not there is an o in the word python (there is so it is true).
iii. Identifies the result of each call <br />
the result of the call when it is true is that the program will update the displayed string of underscores to let the user know how many letters they have to guess. Python will be displayed as "_ _ _ _ _ _" and when they guess a correct letter like o it will be updated to show "_ _ _ _ o _". 
