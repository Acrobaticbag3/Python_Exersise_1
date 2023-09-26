Assignment 2 VG tasks

Assignment 8 Counting Digits:
    - Solution: My imidiate though for this task was to use a list, we can then pass the 
      values through a function that check wheter an integer in odd, even or 0. Then based
      off of that information we can update the corresponding variable and return the value.

    - Problems: I incountered a logical issue with how I updated the variables odd, even, 
      and zeros. The issue arises because integers are immutable, meaning that when you 
      pass them as arguments to a function you're essentially passing their values, not 
      references to the original variables. Further more it turns out that I was updating
      the variables in the incorrect order

Assaingment 9 Birthday Candles:
    - Solution: For this task i knew that I had to use a for loop to loop through my logic. My idea here
      was to make a for loop that loops for as long as the var i != the constant AGE + 1. Inside the loop
      I would go ahead and make an if statement where I check if we have less candles than is needed for 
      the birthday if we do then we buy another box and refill our current candle count, if we don't need 
      it we just use up some of our current candles.

    - Problems: I had major problems when it came to how I should structure the code for this project. 
      After a few failed attempts I decided that a change of plans was in order, I decided that the best
      corse of action was to collect my thoughts somewhere and then use that as a base to make the program.
      I created .txt file named birthday_candles_psudo and wrote psudo code.

Assignment 13 ABCD:
    - Solution: Since we have a four digit combination of numbers we can use a quadrople nested loop. One loop
      for each digit. This iterates through all possible combinations of values that a, b, c and d can have. 
      After that all you need to figure out is the correct check to have at the center of the quadrople nest.
      Whitch in this case was: is a, b, c, d == 4 x (d, c, b, a) than we've found the numbers.

    - Problems: Honestly, this task for me was quite easy. I didn't really struggle with it, since all I had to 
      figure out was the proper end condition. In the description of the task they give away that you need to use 
      a quadrople nested for loop. The main thing to figure out from there is that the quadrople nested loop 
      relates to the four digit combination that we are trying to find.

Assignment 14 Calculating Pi
    - Solution: I decided to skip this task for a while since I did not really know what to do or how to begin to solve 
      this task. But of course, I'd have to do this task soner or later. It took me a bit of time to figure out what a 
      potential solution to this problem could be, but I figured that preghaps the Monte Carlo method was a good ide.
      Thats because the task contains: Random sampling i.e. estimating the value of π through random points, geometric 
      relationship.

    - Problems: My main problem was figuring out that first off all, the Monte Carlo method is applicable here. Secondly
      figuring out how to apply the Monte Carlo method was a bit difficult. But some googles searches later and a bit of
      brute forcing my way forward lead to me finding a solution.

Assignmnet 20 Salary:
    - Solution: This task was also quite simple to me, I decided to take the user input of salaries as a list, so that I then
      could make a function where i do simple math and use simple list functions to accomplish my task. There isn't really 
      anything more to add here.

    - Problems: I didn't really incounter any significant problems while working on this task, the most major thing I could
      consider a "problem" was how to store the information from the user (whitch i do by using a list). And proparly how to 
      use that information.

Assignment 21 Drunken Sailor:
    - Solution: This task was also surprisingly one of the easier ones, however it was quite fun to me. I decided that the
      best solution would be to simulate the movements of the drunken sailors on a grid. Each sailor, start at the origin 
      (0, 0). I simulat their steps randomly in four directions: up, down, left, or right. I then used a loop to iterate 
      through each sailor, and within that loop, I simulated their steps. I used a random choice to determine the direction 
      of each step. finnaly I after every step checked if the sailor was still inside the bounderise of our grid.

    - Problems: The main problem here was figuring out how to simulate the sailors taking a random step. Though once I 
      figured out that I could simply use a for loop to iterate through each sailor and thair stepes the task became a lot
      easier. Figuring out how to simulate a random step wasent too hard.