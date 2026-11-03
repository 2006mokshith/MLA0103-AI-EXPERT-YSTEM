edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 3).
edge(c, e, 6).
edge(d, e, 2).

heuristic(a, 7).
heuristic(b, 5).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 0).

best_route(Start, Goal, Path) :-
    search([[Start]], Goal, ReversePath),
    reverse(ReversePath, Path).

search([[Goal|Rest]|_], Goal, [Goal|Rest]).

search([[Current|Rest]|Others], Goal, Path) :-
    findall(
        [Next,Current|Rest],
        (edge(Current, Next, _),
         \+ member(Next, [Current|Rest])),
        NewPaths
    ),
    append(Others, NewPaths, Updated),
    sort_paths(Updated, Sorted),
    search(Sorted, Goal, Path).

sort_paths(Paths, Sorted) :-
    predsort(compare_paths, Paths, Sorted).

compare_paths(Order, [A|_], [B|_]) :-
    heuristic(A, HA),
    heuristic(B, HB),
    compare(Order, HA, HB).
