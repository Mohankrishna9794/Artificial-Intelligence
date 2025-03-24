Code:
diet(diabetes, 'Eat high-fiber foods, avoid sugar and processed carbs.').
diet(hypertension, 'Reduce salt intake, eat fruits, vegetables, and low-fat dairy.').
diet(obesity, 'Eat low-calorie, high-protein foods, and exercise regularly.').
diet(heart_disease, 'Consume omega-3 fatty acids, whole grains, and avoid trans fats.').
diet(anemia, 'Eat iron-rich foods like spinach, red meat, and legumes.').
diet(kidney_disease, 'Limit protein, sodium, and potassium intake.').
suggest_diet(Disease) :-
    diet(Disease, Advice),
    write('Diet recommendation for '), write(Disease), write(': '), nl,
    write(Advice), nl.
Query 1: suggest_diet(diabetes).
Diet recommendation for diabetes:
Eat high-fiber foods, avoid sugar and processed carbs.
Query 2: suggest_diet(hypertension).
Diet recommendation for hypertension:
Reduce salt intake, eat fruits, vegetables, and low-fat dairy.
