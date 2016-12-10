# 10!

A hardware game inspired by [2048](http://2048game.com/).

## Game Description

### 1.Overview

![overview 1](./docs/img/overview_1.JPG)

![overview 2](./docs/img/overview_2.JPG)

![overview 3](./docs/img/overview_3.JPG)

This is an overview of the game. The above pictures are the game interface.
The interface components consist of 9 seven-segment led displays (in 3x3 square),
5 buttons (4 grey buttons for directions and red button for resetting), 2 big
led lights (at the top right corner) for signaling win/lose, and 2 small led
lights (at the bottom right corner) for display of game mode.


### 2. Getting Started

The game will start when player presses reset button. The grid will display all "10"
cells (see picture below)

![loading screen](./docs/img/loading.JPG)

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

## In-depth Technical Analysis

### 1. Overall finite state machine design

![state machine](./docs/img/state_machine.png)

The game state machine design is designed to run sequentially, effectively being
a large loop. Each state represents a logical step in the game process. The ALUFN
operations used in each state are shown at the top right of each state (in diagram).
6 ALUFNs are used.

However, not all states can be completed in a single clock cycle, thus some states
have substates in them to run multiple sequential operations to complete the state.
States with substates are represented by having a rectangle in the state oval (in diagram).
On each transition, the required variables for the next step have to be initialised.
eg. SELECT_POS uses row_index and col_index to iterate through the game_state,
thus SELECT_NUM has to set these 2 registers to 0.

The game starts at the WAIT_START to wait for difficulty input to initialise
variables (stored in registers).
The game loops in the right-side column until the win or lose conditions are met,
then it breaks out of the loop.
Both WIN and LOSE are halting conditions.

Brief description of looping states:
- COUNT_EMPTY: Counts the number of empty cells in the game board and stores it
in a register.
- CHECK_LOSE: If the number of empty cells is 0, it is not possible to continue
the game. The player loses. Otherwise, simply continue.
- MAKE_RAND1: Generates a random number for selecting the new number to spawn
from an array of numbers. This array is fixed at size 8, so only 3 bits are
needed to index.
- MAKE_RAND2: Generates a random integer for selecting the location to spawn
the new number in.
- SELECT_NUM: Uses number from MAKE_RAND1 to select new number to spawn from a
pre-set array of numbers.
- SELECT_POS: Uses number from MAKE_RAND2 to choose from the empty slots to
spawn the new number.
- ADD_NUM: Actually creates the new number from SELECT_NUM in the position from
SELECT_POS in the game state.
- WAIT_INPUT: Waits for user to press one of the arrow buttons to start the loop
again.
- SHIFT: Does the board shifting operation
- CHECK10: If there are any winning numbers of the board, the player wins.
Otherwise, simply continue.

By adopting a sequential style of processing, conceptualisation of the steps
needed is greatly simplified. Each state only needs to know what the required
variables for the next state to initialise are. Otherwise, the states are
effectively independent and modular.

Although some steps could be done in parallel to make the calculations faster
without additional cost, we decided to always use serial processing since it
would be simpler to plan and code. Furthermore, the entire cycle runs so fast
that speed does not matter (the loop takes 91 cycles, or 1.82ms. The multiplexed
display refreshes slower than this!).

### 2. Number & Position randomizer

### 3. Display mechanism
