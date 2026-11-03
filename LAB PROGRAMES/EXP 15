parent(john, mary).
parent(mary, sam).
parent(john, david).
parent(david, alice).

father(X, Y) :-
    parent(X, Y),
    male(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
