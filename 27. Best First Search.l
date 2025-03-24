Code:
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 2).
heuristic(e, 1).
heuristic(f, 5).
heuristic(g, 0).
best_first_search(Start, Goal, Path) :-
    search([Start], Goal, Path).
search([Goal|Rest], Goal, [Goal|Rest]) :-
    write('Path Found: '), write([Goal|Rest]), nl.
search([Current | Rest], Goal, Path) :-
    findall(Next, (edge(Current, Next), \+ member(Next, [Current | Rest])), NextNodes),
    sort_by_heuristic(NextNodes, SortedNodes),
    append(SortedNodes, Rest, NewQueue),
    search(NewQueue, Goal, Path).
sort_by_heuristic(Nodes, Sorted) :-
    map_list_to_pairs(heuristic, Nodes, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

Query 1: best_first_search(a, g, Path).
Path Found: [g,b]
Path = [g, b] .
