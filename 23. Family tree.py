Code:
parent(john, mary).
parent(john, mike).
parent(mary, lisa).
parent(mary, tom).
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
male(john).
male(mike).
male(tom).
female(mary).
female(lisa).

Query 1: parent(X, mary).
X = john.
Query 2: sibling(lisa, X).
X = tom.
