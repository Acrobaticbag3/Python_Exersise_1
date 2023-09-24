Assignment 2 VG tasks

Assignment 8 Counting Digits:
    - Description: Write a program countdigits.py, which for any given positive number n 
      (read from the keyboard) prints the number of zeros, odd digits, and even digits of 
      the integer. In this case we consider zeros to be neither odd nor even. An example 
      of an execution:

    - Solution: My imidiate though for this task was to use a list, we can then pass the 
      values through a function that check wheter an integer in odd, even or 0. Then based
      off of that information we can update the corresponding variable and return the value.

    - Problems: I incountered a logical issue with how I updated the variables odd, even, 
      and zeros. The issue arises because integers are immutable, meaning that when you 
      pass them as arguments to a function you're essentially passing their values, not 
      references to the original variables. Further more it turns out that I was updating
      the variables in the incorrect order