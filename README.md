# Conway's Game of Life
```
            ___                               _                   
           / __\___  _ ____      ____ _ _   _( )__                
          / /  / _ \| '_ \ \ /\ / / _` | | | |/ __|               
         / /__| (_) | | | \ V  V / (_| | |_| |\__ \               
         \____/\___/|_| |_|\_/\_/ \__,_|\__, ||___/               
                                        |___/                     
      ___                              __     __ _  __      
     / _ \__ _ _ __ ___   ___    ___  / _|   / /(_)/ _| ___ 
    / /_\/ _` | '_ ` _ \ / _ \  / _ \| |_   / / | | |_ / _ \ 
   / /_\\ (_| | | | | | |  __/ | (_) |  _| / /__| |  _|  __/
   \____/\__,_|_| |_| |_|\___|  \___/|_|   \____/_|_|  \___|

```

## Shortcuts / Commands
 - Press C for 1 random block              

 - Press S for 1 Generation interval       

 - Press D for 20 Generation interval      

 - Press F for 50 Generation interval      

 - Press Y to save the game

 - Press X to load the savestate

 - Press V to reload the board

 - Press Q to to quit the game and close the window


## Start Parameter

`python conways_game_of_life.py {GRID-SIZE as int} {BLOCK-LENGTH as int}`

**GRID-SIZE:**
is the Quantity of squares

**BLOCK-LENGTH:**
is the length in pixel


**Example:**
`python conways_game_of_life.py 10 20`

## Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick.[nb 1] Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations. 

## Source

 - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
