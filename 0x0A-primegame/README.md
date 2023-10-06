<p><h1>0x0A. Prime Game :fire:</h1></p>

## Description :house:
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.<br>

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

## Tasks
#
## [0. Prime Game](./0-prime_game.py) <br>
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.
<br>
They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.
<br>
Prototype: `def isWinner(x, nums)`<br>
where x is the number of rounds and nums is an array of `n`<br>
Return: name of the player that won the most rounds<br>
If the winner cannot be determined, return `None`<br>
You can assume `n` and `x` will not be larger than 10000<br>
You cannot import any packages in this task<br>
Example:
<br>
`x = 3, nums = [4, 5, 1]`<br>
First round: `4`<br>
<br>
Maria picks 2 and removes `2, 4`, leaving `1, 3` <br>
Ben picks `3` and removes `3`, leaving `1`<br>
`Ben` wins because there are no prime numbers left for `Maria` to choose<br>
Second round: `5`<br>

`Maria` picks `2` and removes `2`, `4`, leaving `1`, `3`, `5`<br>
Ben picks `3` and removes `3`, leaving `1`, `5`<br>
Maria picks `5` and removes `5`, leaving `1`<br>
`Maria` wins because there are no prime numbers left for `Ben` to choose<br>
Third round: `1`<br>
<br>
`Ben` wins because there are no prime numbers for `Maria` to choose

**Result: Ben has the most wins**

```
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
carrie@ubuntu:~/0x0A-primegame$
```

```
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
```

## Author
- *[Betini Akarandut :fire:](https://github.com/betiniakarandut)*