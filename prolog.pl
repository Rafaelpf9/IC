% notas
nota(joao,5.0).
nota(maria,6.0).
nota(joana,8.0).
nota(joao,5.0).
nota(maria,6.0).
nota(joana,8.0).
nota(mariana,9.0).
nota(cleuza,8.5).
nota(jose,6.5).
nota(jaoquim,4.5).
nota(mara,4.0).
nota(mary,10.0).

aprovado(X):-
	nota(X,Y),Y >= 7.
recuperando(X):-
	nota(X,Y),Y <7,Y >= 5.
reprovado(X):-
	nota(X,Y),Y > 5.


----------------------------------
% Progenitor
progenitor(maria,joao).
progenitor(jose,joao).
progenitor(maria,ana).
progenitor(jose,ana).
progenitor(joao,mario).
progenitor(ana,helena).
progenitor(ana,joana).
progenitor(helena,carlos).
progenitor(mario,carlos).
sexo(ana,feminino).
sexo(maria,feminino).
sexo(joana,feminino).
sexo(helena,feminino).
sexo(mario,masculino).
sexo(joao,masculino).
sexo(jose,masculino).
sexo(carlos,masculino).
irma(X,Y):- progenitor(A,X),
 progenitor(A,Y),
 X\==Y,
 sexo(X,feminino).
irmao(X,Y):- progenitor(A,X),
 progenitor(A,Y),
 X\==Y,
 sexo(X,masculino).
descendente(X,Y):- progenitor(X,Y).
descendente(X,Y):- progenitor(X,A),
 descendente(A,Y).
avo(X,Y):- progenitor(X,A),
 progenitor(A,Y),
 sexo(X,masculino).
mae(X,Y):- progenitor(X,Y),
 sexo(X,feminino).
pai(X,Y):- progenitor(X,Y),
 sexo(X,masculino).
tio(X,Y):- irmao(X,A),
 progenitor(A,Y).
primo(X,Y):-irmao(A,B),
 progenitor(A,X),
 progenitor(B,Y),
 X\==Y.
primo(X,Y):-irma(A,B),
 progenitor(A,X),
 progenitor(B,Y),
 X\==Y.
% questoes:
q1:- progenitor(jose,joao).
q1b:- pai(jose,joao).
q2(X):- mae(maria,X).
q2b(L):-findall(X,mae(maria,X),L).
q3(X):- primo(mario,X).
q3b(L):- findall(X,primo(mario,X),L).
q3c(L):- findall(X,primo(mario,X),LR),list_to_set(LR,L).
q4(X):- tio(_,X).
q4b(L):- findall(X,tio(_,X),LR),list_to_set(LR,L).
q5(X):- descendente(X,carlos).
q5b(L):- findall(X,descendente(X,carlos),L).
q6a(X):- irmao(helena,X).
q6b(X):- irma(helena,X).




------------------------
% Fatorial
factorial(0,1). 

factorial(N,F) :-
   N>0,
   N1 is N-1,
   factorial(N1,F1),
   F is N * F1.
