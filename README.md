# Picture Round Game

This is a simple game of word association. 
Two images will represent classic literature or film. At some point in time the player would have heard of the some of the books or film.

https://picture-round.herokuapp.com/ 

# UX

This website provides a simple quiz game with pictures. Away from the norm of a pub quiz that involves some extra thought. 

* Wireframes are located in img/wireframes 

### User Story
* The player first sees a prompt to enter there username.
* Once entered they are greeted with a message welcoming them to the game and to press the start button.
* On pressing the start button the game will appear. 
* They have six questions in front of them. 
* The player enters there answers for each question and presses enter at the bottom of the list of questions. 
* The quiz disappears and the player can see which question they got right and which they got wrong. 
* If they want to see what the answer is they can press check your answers. 
* At the bottom of the screen, there is the leaderboard with the top six players. 
* If the user is unsure what game is they can press the sample question. Where two images will be presented and the user can understand how to get to the answer. 

# Features
### Existing Features
* The player can enter in a username which will store there score and show it at the end. 
* The answers to all the questions can be seen but are hidden from the user unless they want to know.
* A leaderboard of players at the bottom
* A sample question for the user to understand how it is played. 

### Features left to Implement
* Currently, all the questions can be seen at once. The next step is to put an enter button under each question. 
Once the correct answer has been entered it will move onto the next question. Updating a score as the player goes along. 

# Technologies Used 
* Python 
* Flask
* Jquary
* cloudflare
* bootstrap

# Testing 
Testing was manual and automated.
The manual side was implanting a function, feature or style. Saving the change and checking the site. 
Any changes that did not happen as expected were investigated. 
By checking the error message from flask or testing through inspecting the sight. 
Print statements were entered to test all functions in python. 

Part of the user experience of playing the game was to have a username so I could track there score through the game and give them a result. 
I went about building functions in picture.py that would save the username save_user and there score.
To link the question with the username I built the function get_user 
To check that I was getting the correct usernames and the correct question I put in print statements to show that correct player and question were been collected.
Once that was checked I tested it with question.html to see how it looked on the site. 

I used unittest to check answers and inputs from players with there username on picture_unittest.py
The same was done to a lesser extant on picture_test.py

A strange problem arose with the project where I was unable to show one question at a time. 
All the questions showed at once and if I put an enter a question button it behaved as if the all the question had been answered. 
I tried to fix the problem by rewriting the question function on run.py 
I kept getting an error message to do with the ID which I put down to the information was not coming from the json file correctly.

# Deployment
To run the code locally run.py
There are no differances between heroku and github. 

# Credits

### Content
The Picture Round Game was designed by Sarah Mullen-Rackow and me to use your quiz questions and answers. 

### Media 
All the photographs used where taken from https://pixabay.com/en/editors_choice/ 

### Acknowledgements
Jim Richmond, Haley Schafer and Andres Correa who helmet with understanding errors.  