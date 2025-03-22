Code:
sum(0, 0).
sum(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum(N1, Sum1),
    Sum is N + Sum1.
Query:
sum(5, Sum).
Sum = 15
sum(10, Sum).
Sum = 55
