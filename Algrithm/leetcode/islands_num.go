package main

/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
*/

import "fmt"

func main() {
	fmt.Println(numIslands(testInput))
}

var testInput = [][]byte{
	{1, 1, 0, 1, 0},
	{1, 1, 0, 1, 0},
	{1, 1, 0, 0, 0},
	{0, 0, 0, 0, 0},
}

func numIslands(grid [][]byte) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	iCounter := NewIslandsNumCounter(grid)
	return iCounter.IslandsNum()
}

type IslandsNumCounter struct {
	Input     [][]byte
	SignArray [][]bool
	Line      int
	Column    int
}

func NewIslandsNumCounter(grid [][]byte) *IslandsNumCounter {
	line := len(grid)
	column := len(grid[0])
	sign := make([][]bool, line)
	for i := 0; i < line; i++ {
		sign[i] = make([]bool, column)
	}
	return &IslandsNumCounter{
		Input:     grid,
		Line:      line,
		Column:    column,
		SignArray: sign,
	}
}

func (this *IslandsNumCounter) IslandsNum() int {
	Num := 0
	for {
		i, j := this.findOneIslandStart()
		if i == -1 && j == -1 {
			return Num
		}
		Num = Num + 1
		//sign all this land
		this.signOneLand(i, j)
	}
	return 0
}

func (this *IslandsNumCounter) findOneIslandStart() (line, column int) {
	for i := 0; i < this.Line; i++ {
		for j := 0; j < this.Column; j++ {
			if !this.SignArray[i][j] && this.Input[i][j] == 1 {
				return i, j
			}
		}
	}
	return -1, -1
}

func (this *IslandsNumCounter) signOneLand(line, column int) {
	if this.SignArray[line][column] == true {
		return
	}

	// if value is 1, continue to sign
	// if value is 0, return
	if this.Input[line][column] == 1 {
		this.SignArray[line][column] = true
	} else {
		return
	}

	// to sign neighbor node
	if line+1 < this.Line {
		this.signOneLand(line+1, column)
	}
	if line-1 >= 0 {
		this.signOneLand(line-1, column)
	}

	if column+1 < this.Column {
		this.signOneLand(line, column+1)
	}

	if column-1 >= 0 {
		this.signOneLand(line, column-1)
	}
}
