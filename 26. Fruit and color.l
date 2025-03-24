Code:
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(cherry, red).
find_fruit_by_color(Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), nl,
    fail.
find_fruit_by_color(_).
Query 1: find_fruit_by_color(yellow).
banana
mango
Query 2: find_fruit_by_color(red).
apple
cherry
