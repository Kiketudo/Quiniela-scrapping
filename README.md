# Quiniela-scrapping
Simple python application that randomly calculates results for a pool based on data obtained from beSoccer with web scrapping.
The app gets the matches of "La quiniela" for this week. Then seeks for those matches in bessocer and gets the data.

The algorithm for the winner of each match is bassed on the chance of victory Besoccer team analysts give to each team.
Having those percentages a random result is given but the chances are not the same.
Example:

Real Madrid Vs FC Barcelona

Chance RM: 40% 

Chance tie: 20%

Chance FCB: 40%

A random number from 1 to 100 is given. If it is from 0 to 40 RM wins, if it is from 40 to 60 is a tie and if its from 60 to 100 FCB wins.
for example the number is 25, so RM wins.
