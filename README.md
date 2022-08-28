# CMPUT291_DBSTREAMING_1

## About
This is the Mini-project 1 of CMPUT 291, UAlberta, Winter 2022
This is a model of a movie streaming service, using Python and SQLite.

## Project Specifications

### Database Specification
You are given the following relational schema
- `moviePeople(pid, name, birthYear)`
- `movies(mid, title, year, runtime)`
- `casts(mid, pid, role)`
- `recommendations(watched, recommended, score)`
- `customers(cid, name, pwd)`
- `sessions(sid, name, pwd)`
- `watch(sid, cid, mid, duration)`
- `follows(cid, pid)`
- `editors(eid, pwd)`

### Login Screen
The first screen of your system should provide options for both customers and editors to login. Both class of users should be able to login using a valid id (respectively denoted as `cid` and `eid` for
customers and editors) and a password, denoted with `pwd`. You can assume customers and editors are disjoint, meaning the same id cannot be in both tables. After a successful login, the system should
detect whether it is a customer or an editor and provide the proper menues as discussed next.

Unregistered customers should be able to sign up by providing a unique `cid` and additionally a name, and a password. Passwords are not encrypted in this project. After a successful signup, customers
should be able to perform the subsequent customer operations (possibly chosen from a menu) as discussed next.

Users should be able to logout, which directs them to the first screen of the system. There must be also an option to exit the program directly.

### System Functionalities
After a successful login, customers should be able to perform all of the following tasks:
1. ***Start a session***: The user should be able to start a session. For each session, a unique session id should be assigned by your system, the session date should be set to the current date and the
   duration should be set to null.
2. ***Search for movies***: The customer should be able to provide one or more unique keywords, and the system should retrieve all movies that have any of those keywords in title, cast member name or
   cast member role. For each match, at least the title, the year, and the duration should be displayed, and the result should be ordered based on the number of matching keywords with movies matching
   the largest number of keywords listed on top. If there are more than 5 matching movies, at most 5 matches will be shown at a time, letting the user select a movie or see more matches. The customer
   should be able to select a movie and see more information about the movie including the cast members and the number of customers who have watched it (the difinition of watched in this project is
   having watched more than half of the duration of the movie). On a movie screen, the customer should have the option to (1) select a cast member and follow it, and to (2) start watching the movie.
3. ***End watching a movie***: The customer should be able to end a movie being watched. If the customer is watching multiple movies, there should be an option to select any of them and end it. The
   duration watched should be set to the time passed in minutes from the time it started until the current time. The duration watched cannot exceed the duration of the movie.
4. ***End the session***: The user should be able to end the current session. The duration should be set in minutes to the time passed in minutes from the time the session started until the current time.
   If the customer has been watching any movies, those will end and the duration watched will be recorded. Again the duration watched cannot exceed the duration of the movie.

Editors should be able to perform the following actions:
1. ***Add a movie***: The editor should be able to add a movie by providing a unique movie id, a title, a year, a runtime and a list of cast members and their roles. To add a cast member, the editor
   will enter the id of the cast member, and your system will look up the member and will display the name and the birth year. The editor can confirm and provide the cast member role or reject the cast
   member. If the cast member does not exist, the editor should be able to add the member by providing a unique id, a name, and a birth year.
2. ***Update a recommendation***: The editor should be able to select a mothly, an annual or an all-time report and see a listing of movie pairs m1, m2, such that some of the customers who have watched m1,
   have also watched m2 within the chosen period. Any such pair should be listed with the number of customers who have watched them within the chosen period, ordered from the largest to the smallest number,
   and with an indicator if the pair is in the recommended list and the score. The editor should be able to select a pair and (1) add it to the recommended list (if not there already) or update its score,
   or (2) delete a pair from the recommended list.

### Other Specifications
- **String matching**: Except the password which are case sensitive, all other string matches (including id, name, title, etc) are case-insnsitive. This means the keyword "Spiderman" will match spiderman,
  SPIDERMAN, and SpiderMan, and you cannot make any assumption on the case of the strings in the database. The database can have strings in uppercase, lowercase or any mixed format.
- **Error checking**: Every good programmer should do some basic error checking to make sure the data entered is correct. Your system should not break down when the user makes a mistakes.
- **Security**: Must counter SQL injection attackes and make the password non-visible at the time of typing 