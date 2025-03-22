Code:
dob(john, '1990-05-14').
dob(mary, '1985-11-23').
dob(alex, '2000-07-30').
dob(susan, '1995-03-10').
find_dob(Name, DOB) :- dob(Name, DOB).

Output:
Query1: dob(Name, DOB).
Name = john,
DOB = '1990-05-14' 

Query2: find_dob(john, DOB).
DOB = '1990-05-14'.
