dob(john, '1990-05-14').
dob(mary, '1985-11-23').
dob(alex, '2000-07-30').
dob(susan, '1995-03-10').
find_dob(Name, DOB) :- dob(Name, DOB).
