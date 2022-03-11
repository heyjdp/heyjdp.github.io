--- 
title: "\U0001f4bb Sudoku Solver (by the Prime Minister of Singapore, Hsien Loong Lee) \U0001f30a \U0001f9e9 \U0001f469\u200D\U0001f4bb" 
date: 2021-07-10T11:00:00+02:00 
draft: false 
tags: ["tech", "c", "development", "games"] 
# author: "Jas" 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
katex: true
cover:
    image: "/post-img/sudoku-puzzles-1200x630.jpg" # image path/url
    alt: "Partially solved sudoku puzzles and pencil" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

So, in 2015, the Prime Minister of Singapore, Hsien Loong Lee, posted a C language sudoku solver to leetcode.com and I can see a lot of bitwise manipulation in the code. I think it is worth our time to take the solution to pieces and see how it runs so fast.

<!--more-->

## Sudoku Puzzles

Sudoku, also known as Su Doku, popular form of number game. In its simplest and most common configuration, sudoku consists of a 9 × 9 grid with numbers appearing in some of the squares. The object of the puzzle is to fill the remaining squares, using all the numbers 1–9 exactly once in each row, column, and the nine 3 × 3 subgrids. Sudoku is based entirely on logic, without any arithmetic involved, and the level of difficulty is determined by the quantity and positions of the original numbers. The puzzle, however, raised interesting combinatorial problems for mathematicians, two of whom proved in 2005 that there are 6,670,903,752,021,072,936,960 possible sudoku grids.

![Easy sudoku.com puzzle](/post-img/easy-sudoku-com-puzzle.jpg)

Although sudoku-type patterns had been used earlier in agricultural design, their first appearance in puzzle form was in 1979 in a New York-based puzzle magazine, which called them Number Place puzzles. They next appeared in 1984 in a magazine in Japan, where they acquired the name sudoku (abbreviated from "suuji wa dokushin ni kagiru", meaning "the numbers must remain single"). In spite of the puzzle’s popularity in Japan, the worldwide sudoku explosion had to wait another 20 years.

## Original Post

I found this headline posted on [Hacker News](https://news.ycombinator.com/item?id=30174763) although, **fair warning**, most of the comment thread is political about Singapore, Hsien Loong Lee, his background in Mathematics at Cambridge University, and other non-technical opinionated guff. I recommend you skip it.

I feel we are better off looking at the code, and seeing if we can reverse the technique to look for clever things

The [original solution on leetcode.com](https://leetcode.com/problems/sudoku-solver/discuss/15796/Singapore-prime-minister-Lee-Hsien-Loong%27s-Sudoku-Solver-code-runs-in-1ms) shows that it passes all 6/6 test cases in 1ms, which is very impressive. There is a bitly link to the original code, and a MIT license making the code open source for anyone to use for any purpose.

## It is MIT licensed

The C code comes with a [bitly link to a Google Folder](http://bit.ly/1zfIGMc) that contains the following `License.txt` file:

```txt
The MIT License (MIT)

Copyright (c) 2015 Lee Hsien Loong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## The C code example Sudoku Solver

The folder also contains the following `Sudoku2.cpp` C code, below is a copy of the sudoku solver C code from the folder, lets take a look:

```c {linenos=table}
#include "stdio.h"

int InBlock[81], InRow[81], InCol[81];

const int BLANK = 0;
const int ONES = 0x3fe; // Binary 1111111110

int Entry[81];				  // Records entries 1-9 in the grid, as the corresponding bit set to 1
int Block[9], Row[9], Col[9]; // Each int is a 9-bit array

int SeqPtr = 0;
int Sequence[81];

int Count = 0;
int LevelCount[81];

void SwapSeqEntries(int S1, int S2)
{
	int temp = Sequence[S2];
	Sequence[S2] = Sequence[S1];
	Sequence[S1] = temp;
}

void InitEntry(int i, int j, int val)
{
	int Square = 9 * i + j;
	int valbit = 1 << val;
	int SeqPtr2;

	// add suitable checks for data consistency

	Entry[Square] = valbit;
	Block[InBlock[Square]] &= ~valbit;
	Col[InCol[Square]] &= ~valbit; // Simpler Col[j] &= ~valbit;
	Row[InRow[Square]] &= ~valbit; // Simpler Row[i] &= ~valbit;

	SeqPtr2 = SeqPtr;
	while (SeqPtr2 < 81 && Sequence[SeqPtr2] != Square)
		SeqPtr2++;

	SwapSeqEntries(SeqPtr, SeqPtr2);
	SeqPtr++;
}

void PrintArray()
{
	int i, j, valbit, val, Square;
	char ch;

	Square = 0;

	for (i = 0; i < 9; i++)
	{
		if (i % 3 == 0)
			putc('\n', stdout);
		for (j = 0; j < 9; j++)
		{
			if (j % 3 == 0)
				putc(' ', stdout);
			valbit = Entry[Square++];
			if (valbit == 0)
				ch = '-';
			else
			{
				for (val = 1; val <= 9; val++)
					if (valbit == (1 << val))
					{
						ch = '0' + val;
						break;
					}
			}
			putc(ch, stdout);
		}
		putc('\n', stdout);
	}
}

void ConsoleInput()
{
	int i, j;
	char InputString[80];

	for (i = 0; i < 9; i++)
	{
		printf("Row[%d] : ", i + 1);
		scanf("%s", InputString);

		for (j = 0; j < 9; j++)
		{
			char ch = InputString[j];
			if (ch >= '1' && ch <= '9')
				InitEntry(i, j, ch - '0');
		}
	}

	PrintArray();
}

void PrintStats()
{
	int i, j, S;

	printf("\nLevel Counts:\n\n");

	S = 0;
	while (LevelCount[S] == 0)
		S++;

	i = 0;

	while (S < 81)
	{
		int Seq = Sequence[S];
		printf("(%d, %d):%4d ", Seq / 9 + 1, Seq % 9 + 1, LevelCount[S]);
		if (i++ > 4)
		{
			printf("\n");
			i = 0;
		}
		S++;
	}

	printf("\n\nCount = %d\n", Count);
}

void Succeed()
{
	PrintArray();
	PrintStats();
}

int NextSeq(int S)
{
	int S2, Square, Possibles, BitCount;
	int T, MinBitCount = 100;

	for (T = S; T < 81; T++)
	{
		Square = Sequence[T];
		Possibles = Block[InBlock[Square]] & Row[InRow[Square]] & Col[InCol[Square]];
		BitCount = 0;
		while (Possibles)
		{
			Possibles &= ~(Possibles & -Possibles);
			BitCount++;
		}

		if (BitCount < MinBitCount)
		{
			MinBitCount = BitCount;
			S2 = T;
		}
	}

	return S2;
}

void Place(int S)
{
	LevelCount[S]++;
	Count++;

	if (S >= 81)
	{
		Succeed();
		return;
	}

	int S2 = NextSeq(S);
	SwapSeqEntries(S, S2);

	int Square = Sequence[S];

	int BlockIndex = InBlock[Square],
		RowIndex = InRow[Square],
		ColIndex = InCol[Square];

	int Possibles = Block[BlockIndex] & Row[RowIndex] & Col[ColIndex];
	while (Possibles)
	{
		int valbit = Possibles & (-Possibles); // Lowest 1 bit in Possibles
		Possibles &= ~valbit;
		Entry[Square] = valbit;
		Block[BlockIndex] &= ~valbit;
		Row[RowIndex] &= ~valbit;
		Col[ColIndex] &= ~valbit;

		Place(S + 1);

		Entry[Square] = BLANK; // Could be moved out of the loop
		Block[BlockIndex] |= valbit;
		Row[RowIndex] |= valbit;
		Col[ColIndex] |= valbit;
	}

	SwapSeqEntries(S, S2);
}

int main(int argc, char *argv[])
{
	int i, j, Square;

	for (i = 0; i < 9; i++)
		for (j = 0; j < 9; j++)
		{
			Square = 9 * i + j;
			InRow[Square] = i;
			InCol[Square] = j;
			InBlock[Square] = (i / 3) * 3 + (j / 3);
		}

	for (Square = 0; Square < 81; Square++)
	{
		Sequence[Square] = Square;
		Entry[Square] = BLANK;
		LevelCount[Square] = 0;
	}

	for (i = 0; i < 9; i++)
		Block[i] = Row[i] = Col[i] = ONES;

	ConsoleInput();
	Place(SeqPtr);
	printf("\n\nTotal Count = %d\n", Count);

	return 0;
}
```

So, just reading through I can see some obvious stuff, some more interesting things that will need a few moments to understand, and at least two opportunities to optimize the code.

## First run of the code

If you didn't yet [setup VS Code for C code debugging](/2022/01/c-code-development-in-vs-code-for-macos/), go ahead and do that now.

So, the entry point of the code is the `main()` function, as with any other C code. Let's take a look at what it does.

```c {linenos=table}
int i, j, Square;

for (i = 0; i < 9; i++)
    for (j = 0; j < 9; j++)
    {
        Square = 9 * i + j;
        InRow[Square] = i;
        InCol[Square] = j;
        InBlock[Square] = (i / 3) * 3 + (j / 3);
    }

for (Square = 0; Square < 81; Square++)
{
    Sequence[Square] = Square;
    Entry[Square] = BLANK;
    LevelCount[Square] = 0;
}

for (i = 0; i < 9; i++)
    Block[i] = Row[i] = Col[i] = ONES;
```

We have a standard double-loop for a two dimensional array in variables `i` and `j`, and we can see that it is initializing the global integer arrays `int InBlock[81], InRow[81], InCol[81];`. We should not for completeness that this is C code, so the arrays are all zero indexed, meaning that the indices `i,j` range from `0..8` and the counter `Square` goes from `0..80`. The interesting looking part of this code simply sets up a block indexer:

```txt
InBlock[] = 111 222 333
            111 222 333
            111 222 333
            444 555 666
            444 555 666
            444 555 666
            777 888 999
            777 888 999
            777 888 999
```

Further, we have some single dimensional arrays being initialized: `int Sequence[81], Entry[81], LevelCount[81];`. Also, we initialize the `Block[], Row[] and Col[]` arrays.

So indeed for the first run, set a breakpoint at `ConsoleInput();` in `main()` and let's check that those arrays are initialized as we think they will be.

![Debugging C code sudoku solver](/post-img/debugging-sudoku-solver-c-code.jpg)

Okay, so the next thing the code does is receive input on the command line so that the user can set up the puzzle array.

![Running C code sudoku solver](/post-img/running-sudoku-solver-c-code.jpg)

But, we don't want to have to type all of that in every time we run the code, so instead, we will force the values into the array. To make this work, we will add a global flag called `TestMode` and when it is set, we will ignore the console input and instead load the test values.

```c
int TestMode = 1;
...
void TestInput()
{
	// 1-- 47- ---
	// --- 162 7-4
	// -6- --- ---
	// 871 -45 9-6
	// 3-- --- -51
	// 256 -9- -7-
	// -27 -1- 5-8
	// -15 68- -42
	// 6-3 --- 1--

	InitEntry(0, 0, 1);
	InitEntry(0, 3, 4);
	InitEntry(0, 4, 7);

	InitEntry(1, 3, 1);
	InitEntry(1, 4, 6);
	InitEntry(1, 5, 2);
	InitEntry(1, 6, 7);
	InitEntry(1, 8, 4);
    <---snip--->
}
...
if (TestMode == 0)
    ConsoleInput();
else
    TestInput();
```

## Code Optimization

We can clean up the array initialization code with a modification to the globals:

```c
int Sequence[81] = {0};
int LevelCount[81] = {0};
```

If, for some reason, you don't trust C style array initialization then calling `memset(Sequence, 0, 81); memset(LevelCount, 0, 81);` in `main()` would do the same job. And can also be used in the main body of the code at run-time rather than just at initialization.

Now, we can get rid of the second loop in `main()` and replace the initialization code with the following:

```c
    int i, j, Square;

	for (i = 0; i < 9; i++)
		for (j = 0; j < 9; j++)
		{
			Square = 9 * i + j;
			InRow[Square] = i;
			InCol[Square] = j;
			InBlock[Square] = (i / 3) * 3 + (j / 3);
    		Sequence[Square] = Square;
		}

	for (i = 0; i < 9; i++)
		Block[i] = Row[i] = Col[i] = ONES;
```

The function should make a very simple check to see if `S1 == S2` and return before doing any swapping:

```c
void SwapSeqEntries(int S1, int S2)
{
	if (S1 == S2) return;
	int temp = Sequence[S2];
	Sequence[S2] = Sequence[S1];
	Sequence[S1] = temp;
}
```

I find the `PrintArray()` function to be quite clunky, personally not a fan of `putc()`, but I stuck with it for now. I am surprised that the author didn't know that the mathematical inverse of \\(2^x\\) is \\(log_2(x)\\), so I made that change (and had to `#include "math.h"` for the function). The `PrintArray()` function main loop now appears:

```c
    for (i = 0; i < 9; i++)
	{
		if (i % 3 == 0)
			putc('\n', stdout);
		for (j = 0; j < 9; j++)
		{
			if (j % 3 == 0)
				putc(' ', stdout);
			valbit = Entry[Square++];
			if (valbit == 0)
				ch = '-';
			else
				ch = '0' + log2(valbit);
			putc(ch, stdout);
		}
		putc('\n', stdout);
	}
```
