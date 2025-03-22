Code:
student(john, cs101).
student(alice, cs102).
student(bob, cs101).
student(eve, cs103).
teacher(mr_smith, cs101).
teacher(ms_jones, cs102).
teacher(dr_brown, cs103).
teaches(Teacher, Student) :-
    student(Student, SubjectCode),
    teacher(Teacher, SubjectCode).

Query1:
teaches(mr_smith, john).
true.
Query2:
teaches(ms_jones, bob).
false.
Query3:
teaches(Teacher, alice).
Teacher = ms_jones.
