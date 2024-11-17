# die-hard-jug-riddle

`jug.py` builds a directed graph representing the state transitions of the jug riddle from Die Hard.

The state is represented as a tuple (V3, V5), whose values represent the volumes of water left in the 3L and 5L jugs respectively.  There are 6 transitions at each state as follows:
1. Fill V3
2. Fill V5
3. Empty V3 to sink
4. Empty V5 to sink
5. Pour V3 into V5
6. Pour V5 into V3
