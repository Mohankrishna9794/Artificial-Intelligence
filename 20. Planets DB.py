Code:
planet(mercury, terrestrial).
planet(venus, terrestrial).
planet(earth, terrestrial).
planet(mars, terrestrial).
planet(jupiter, gas_giant).
planet(saturn, gas_giant).
planet(uranus, ice_giant).
planet(neptune, ice_giant).
same_type(P1, P2) :-
    planet(P1, Type),
    planet(P2, Type),
    P1 \= P2.

Query 1: planet(X, terrestrial).
Output:
X = mercury ;
X = venus ;
X = earth ;
X = mars.

Query 2: same_type(mars, X).
Output:
X = mercury ;
X = venus ;
X = earth.
