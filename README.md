#Analysis of World Cup Qualification Draw
A simple awk program to read in the seedings and calculate the net world ranking points of a group, the pot position score to evaluate how tough the draw is for a group, ie. Pot 1 Seed 1 would be tough where as Pot 1 seed 9 would be better.

#Python version
 python groups.py

#AWK version
 awk -f groups.awk seedings.csv

#To Do /Thoughts
+ Read in the group value?
+ Loop round each group i.e. Array/Set {A,C,D,E,F,G,H,I}
+ Evaluate a higher score for a higher draw in higher pots (i.e. seed 1 in pot 1is worse to get than seed 1 in pot 3 ) 
+ Graph bar +/-
