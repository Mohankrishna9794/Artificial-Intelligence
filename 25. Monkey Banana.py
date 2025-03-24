Code:
move(on_floor, push_box, near_banana).
move(near_banana, climb_box, on_box).
move(on_box, grab_banana, has_banana).
can_get_banana(has_banana) :-
    write('Monkey got the banana!'), nl.
can_get_banana(State) :-
    move(State, Action, NextState),
    write('Action: '), write(Action), nl,
    can_get_banana(NextState).
Query 1: can_get_banana(on_floor).
Action: push_box
Action: climb_box
Action: grab_banana
Monkey got the banana!
