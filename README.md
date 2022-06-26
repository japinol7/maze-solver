## Maze Solver

	Creates and solves mazes of NxN cells with a start and a goal.

	version: 0.0.3
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol


## Usage

	mazesolver [-h] [-c] [-p] [-n NAME] [-nr ROWS] [-nc COLUMNS] [-t]

	optional arguments:
	  -h, --help            show this help message and exit
      -c,           --create
	                        create a new maze instead of loading one.
      -n,           --name
	                        the maze's name (without extension). Ex: maze_01 
                            This name plus and extension will be the file to load or to create. 
      -p,           --print
	                        print the maze created or load and the maze solution to the console.
      -nr,           --rows
	                        the number of rows. Must be between 4 and 2000.
      -nc,           --columns
	                        the number of columns. Must be between 4 and 2000.
	  -t, 			--debugtraces
	                        show debug back traces information when something goes wrong


**Default optional arguments**

	create 	            False
	name 	            maze_01
	print 	            False
	rows             	32
	columns   		    12
	debugtraces		    False


**Examples of usage**

	If mazesolver has not been installed as an app:
		$ python -m mazesolver
		$ python -m mazesolver --create --name maze_02 --rows 50 --columns 40


**To make The Maze Solver work**

	Do this:
	    1. Clone this repository in your local system.
	    2. Go to its folder in your system.
	    3. $ python -m mazesolver
