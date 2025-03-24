Code:
cannot_fly(ostrich).
cannot_fly(penguin).
can_fly(Bird) :- 
    \+ cannot_fly(Bird), 
    write(Bird), write(' can fly.'), nl.
can_fly(Bird) :- 
    cannot_fly(Bird), 
    write(Bird), write(' cannot fly.'), nl.

Query 1: can_fly(sparrow).
sparrow can fly.
Query 2: can_fly(ostrich).
ostrich cannot fly.
