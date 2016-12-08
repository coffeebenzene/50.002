# 10!

A hardware game inspired by [2048](http://2048game.com/).

## Game Description

### 1.Overview

<insert overview pics>

This is an overview of the game. The above pictures are the game interface.
The interface components consist of 9 seven-segment led displays (in 3x3 square),
5 buttons (4 grey buttons for directions and red button for resetting), 2 big
led lights (at the top right corner) for signaling win/lose, and 2 small led
lights (at the bottom right corner) for display of game mode.


### 2. Getting Started

The game will start when player presses reset button. The grid will display all "10"
cells (see picture below)

<insert picture of loading screen>

Player then will choose game mode by pressing one of the direction button:
- UP: Easy Mode (both small led lights will be off)
- LEFT: Normal Mode (small green led light will be on)
- RIGHT: Hard Mode (small red led light will be on)
- DOWN: Extreme Mode (both small led lights will be on)

Player can then proceed to play the game. The game rules will be explained in the
next section of the documentation.

### 3. How to Play

If you are familiar with [2048](http://2048game.com/), this game is another version
of it with objective of getting to 10 and different combination of tiles. Instead
of addition, when 2 tiles are combined in 10!, a new tile with incremented value
(+1) will appear in place.

In case you are not familiar with [2048](http://2048game.com/), here is the full
explanation how to play 10!:

**Objective:** Use your arrow keys to move the tiles. When two tiles with the same
number touch, they merge into one! In this attempt, try to get a block of 10 and
you win the game

**Detail Interaction:** When a direction key is pressed, all tiles that are on
display will be moved to the corresponding direction all the way till they are
blocked by the wall or another tile. When 2 tiles with the same number hit each
other, they will be combined into one tile with incremented (+1) value (e.g.
2+2->3 or 5+5->6). A new tile will spawn randomly whenever you move the tiles
with direction buttons so you will need a bit of luck to win 10!

**Win/Lose Condition:** When any of the tile is incremented to 10, the game will
automatically stop, the big green led light on top right corner will light up,
 and you will be declared winner. If you fail to increment any of the tile to 10
 before running out of space for new tile to spawn, the game will also stop, the
 big red led light on the top right corner will light up, and it's a lost game.

Have fun playing! :boom: :tada: :confetti_ball:

## Implementation Analysis

### 1. Overall finite state machine design

### 2. Number & Position randomizer

### 3. Display mechanism
