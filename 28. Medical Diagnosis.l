Code:
disease(flu) :- has_symptom(fever), has_symptom(cough), has_symptom(sore_throat).
disease(cold) :- has_symptom(runny_nose), has_symptom(sneezing), has_symptom(cough).
disease(covid) :- has_symptom(fever), has_symptom(cough), has_symptom(loss_of_taste_smell).
disease(malaria) :- has_symptom(fever), has_symptom(chills), has_symptom(sweating).
has_symptom(Symptom) :-
    write('Do you have '), write(Symptom), write('? (yes/no): '),
    read(Response),
    Response == yes.
diagnose :-
    disease(Disease),
    write('You may have '), write(Disease), nl,
    fail.  % Backtrack to check for other diseases

diagnose :-
    write('Diagnosis complete. If no disease was identified, consult a doctor.'), nl.
Query 1: diagnose.
Do you have fever? (yes/no): yes.
Do you have cough? (yes/no): yes.
Do you have sore_throat? (yes/no): yes.
You may have flu.
Do you have loss_of_taste_smell? (yes/no): no.
Do you have runny_nose? (yes/no): no.
Diagnosis complete. If no disease was identified, consult a doctor.
