# Technologies Used
* Python
* Django
* Bootstrap
* Jquery/Javascript

# Game Plan
* Randomly generate a word and make call to Oxford Dictionary API to collect synonyms
* A small form will submit user's guesses to back end
* Synonyms are hidden from user but will alert them when their guess matches up with results
* If user is logged in, they will be able to click any guess and submit it to their personal study guide
* Another API call will collect definitions for study guide
* A countdown from 10 seconds will restart with every user submission
* Once user can think of no more, countdown comes to 0 and form is disabled

# End Result
![guess](./my_vocab/static/vocab_screenshot.png)

# Challenges
* Jquery ajax call to post to back end
* Rendering database elements on the front end
* Couldn't quite implement a counter for correct guesses

# What I'd Do With More Time
* Pull in an API to randomly generate words as opposed to selecting from a hard-coded list
* Better style incorrect and correct guesses
* Include more information than definition in study guide