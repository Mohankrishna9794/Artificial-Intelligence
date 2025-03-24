Code:
hanoi(1, A, C, _) :- 
    write('Move disk from '), write(A), write(' to '), write(C), nl.
hanoi(N, A, C, B) :- 
    N > 1,
    M is N - 1,
    hanoi(M, A, B, C),
    hanoi(1, A, C, _),
    hanoi(M, B, C, A).
Query 1: hanoi(3, left, right, center).
Output:
Move disk from left to right
Move disk from left to center
Move disk from right to center
Move disk from left to right
Move disk from center to left
Move disk from center to right
Move disk from left to right
