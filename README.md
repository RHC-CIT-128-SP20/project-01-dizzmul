# CIT 128 - Project 01 - Student Directed Project

**Version:** 01/19/2020

## Student Info

* Alexander Rodriguez
* 37902
* Spring 2020



## Directions

Answer the questions being asked by the program using approproiate information.

The first question will ask you what map you are playing on. The possible answers are "The Lab", "interchange", "Woods", "Customs", "Factory", "Reserve", "Shoreline". The Lab and Reserve are riskier ventures than the other maps so the program will be more likely to suggest more expensive ammo if you go there.

The next question will ask about your budget. Better ammo costs more money, so the higher you say your budget is then the more likely the program will suggest top-notch ammunition.

After that you will be asked which type of gun you will be using. All of the available guns and their cartridge size are listed here: https://escapefromtarkov.gamepedia.com/Weapons
Your response is not case-sensitive but you do need to include all hyphens and spaces exactly as they are on that list. The program will use this info to determine which size ammo to suggest. For example if you select a 9x18mm gun such as the PP-91, the program
will then-on only recommend 9x18mm ammo.

Lastly, you will have to indicate whether or not you are focusing on killing "scavs." Scavs are non-player characters within Tarkov that will shoot you on site. Their guns aren't typically all that great and neither is their armor. They aren't too much of a threat compared to real players who are also roaming around, so if your focus is on killing them then the program will be far more likely to recommend you cheaper ammo.

This ammo chart, while not totally comprehensive of ALL the guns and ammo types, can be used to cross-reference this program to see if it's recommending the appropriate ammo. https://i.redd.it/eawzvoj4blc41.png


## Program Description

This program will help you select which ammo type you should be using within the game Escape From Tarkov. It will determine which ammunition you will most likely need given the map, the expected armor value of your opponents, the gun you're using, and the price of the ammo. It will also factor in how much money you have overall and help you decide which ammo would be best on a budget or which will be better to buy if you have a lot of money to spend

## Rubric / Grading Scale

* Working program per the above program description
  * Input checks to ensure user does not enter random data(20 pt)
  * Non-random data should be properly digested by the program as expected(10 pt)
  * Comments that describe different sections of the code (5 pt)
  * Program suggests an ammo type that actually fits the gun(i.e program doesnt suggest 9x18mm rounds for a 5.56x45mm gun, only suggests 9x18 rounds) (20 pt)
  * Program accuarately accounts for the user's budget and situation when suggesting ammo (20 pt)
  * Code is easy to read and understand (5 pt)
* Turn in Drafts Updates in Canvas
  * Draft 1 (5pt)
  * Draft 2 (5pt)
  * Draft 3 (5pt)
  * Draft 4 (5pt)

Total Points: 100

### Additional Grading Notes

* Programmers must have attention to detail, as a result up to __2 Points__ may be taken for not updating the student info (Name, CRN, Semester Year) in the __Markdown__ and __Python Comments__.
* Customers will not pay for programs that do not work, as a result up to __50 Points__ may be taken for programs that do not run due to syntax errors.
* Programmers tend to forget how large programs work over time, as a result up to __4 Points__ may be taken for programs that do not have a _reasonable_ amount of comments that describe key sections of code.
* Minimum of 4 or more commits made to GitHub showing incremental programming changes towards the final program (4pt)
  * 1 Commit may be for updating Student Info in the Markdown and Python File
  * 3 Commits must be for programming updates to source code
  * If a unit test is available, no changes made to the Unit Test will count towards the required commits (nor should there be any changes made to this file).
  * This is a team project, all group members must have at least one commit with code changes. Updating student info does not count.
* All programs must have your Github URL submitted in Canvas via the assignment page. Unsubmitted Github repos will receive __0 Points__.
* Programs that have been submitted and received a grade will not be regraded, unless the instructor makes a request for changes.
* If a program is eligible for regrading, it is the responsibility of the student to inform the instructor when the program is ready for regrading.
