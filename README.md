# fib.py
Calculate [n] amount of fibonacci numbers

## Usage
```
usage: fib.py [-h] [-l] amount

Calculate [n] amount of fibonacci numbers

positional arguments:
  amount      How many numbers to calculate

optional arguments:
  -h, --help  show this help message and exit
  -l, --last  Print out only the last number
  ```


## Examples
```
D:\git\fib.py>python fib.py 10
F[0]: 0
F[1]: 1
F[2]: 1
F[3]: 2
F[4]: 3
F[5]: 5
F[6]: 8
F[7]: 13
F[8]: 21
F[9]: 34
F[10]: 55
```
```
D:\git\fib.py>python fib.py 100 --last
F[100]: 354224848179261915075
```