Bringing a Gun to a Trainer Fight
=================================

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately,
 you grabbed a beam weapon from an abandoned storeroom while you were running through 
 the station, so you have a chance to fight your way out. But the beam weapon is potentially
  dangerous to you as well as to the bunny trainers: its beams reflect off walls, 
  meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. 
You also know that if a beam hits a corner, it will bounce back in exactly the same direction. 
And of course, if the beam hits either you or the bunny trainer, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, trainer_position, distance) 
that gives an array of 2 integers of the width and height of the room, 
an array of 2 integers of your x and y coordinates in the room, 
an array of 2 integers of the trainer's x and y coordinates in the room, 
and returns an integer of the number of distinct directions that you can fire to hit the elite trainer, 
given the maximum distance that the beam can travel.

The room has integer dimensions `[1 < x_dim <= 1250, 1 < y_dim <= 1250]`. 
You and the elite trainer are both positioned on the integer lattice at different distinct positions 
(x, y) inside the room such that `[0 < x < x_dim, 0 < y < y_dim]`. 
Finally, the maximum distance that the beam can travel before becoming harmless will be 
given as an integer 1 < distance <= 10000.

For example, if you and the elite trainer were positioned in a room with dimensions `[3, 2]`, 
your_position `[1, 1]`, trainer_position `[2, 1]`, 
and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite trainer 
(given as vector bearings from your location): `[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]`. 
As specific examples, the shot at bearing `[1, 0]` is the straight line horizontal shot of distance 1, 
the shot at bearing `[-3, -2]` bounces off the left wall and then the bottom wall before hitting 
the elite trainer with a total shot distance of sqrt(13), and the shot at bearing `[1, 2]` 
bounces off just the top wall before hitting the elite trainer with a total shot distance of sqrt(5).


Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

```
-- Java cases --
Input:
Solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
Solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

-- Python cases --
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
```


# Solution

This one got me a little bit stuck because I didn't understand at the beginning that infinite angles are possible.
So I started generating what I thought it was "all possible directions" 
(I was taking width and height and using all possible combinations of them as directions). 
Using those directions I was just following them, inverting direction after bouncing on the walls, 
and calculating the distance of every step. With this solution it was really easy to check if I was killing myself or not during the process.
Some tests passed, including the given ones, but not all of them. I wondered then if more angles were possible.

Final solution was about mirroring the Trainer and myself, for that I just calculated the sum needed for every mirror 
(in %2 as there are two different steps will creating a mirror)
And just inverting the sign for x, for y and for both to get the other mirrors. 
Mirror are done until the maximum distance is passed.

Then, we have all locations of the Trainer and myself, we only need to shoot all of them, but we have to check if some of them are repeated
(trainer repeating same angle or a trainer after myself in the same angle) 
I was using Fractions at the beginning (I'm not very familiar with Python) but it's hard to use as some negative and positives can be equal. 
Finally, using `atan2` we can obtain an angle for x and y so it makes everything easier.
Storing all the angles in a `set` to ensure we don't have duplicates, we only need to check if every angle 
in Trainer's set is myself's angles and if in they are, which is closer.




