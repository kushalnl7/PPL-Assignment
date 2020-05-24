:- initialization(main).
main :- write('\n Welcome to the Flight Management System').

flight(toronto,aircanada,london,550,420).
flight(toronto,united,london,700,480).
flight(toronto,united,madrid,1000,600).
flight(toronto,ibeira,madrid,850,540).
flight(toronto,aircanada,madrid,950,540).

flight(london,aircanada,toronto,575,440).
flight(london,united,toronto,725,500).
flight(london,ibeira,barcelona,295,320).

flight(barcelona,ibeira,london,260,270).
flight(barcelona,ibeira, valencia,150,105).
flight(barcelona,ibeira, madrid,160,95).
flight(barcelona,aircanada,madrid,140,90).

flight(madrid, aircanada, barcelona, 175, 105).
flight(madrid, ibeira, barcelona, 205, 110).
flight(madrid, ibeira, valencia, 115, 95).
flight(madrid, ibeira, malaga, 125, 105).
flight(madrid, ibeira, toronto, 875, 525).
flight(madrid, united, toronto, 1025, 585).
flight(madrid, aircanada, toronto, 975, 525).

flight(valencia, ibeira, barcelona, 150, 95).
flight(valencia, ibeira, madrid, 80, 70).
flight(valencia, ibeira, malaga, 120, 140).

flight(malaga, ibeira, valencia, 130, 150).
flight(malaga, ibeira, madrid, 100, 90).

flight(paris, united, toulouse, 85,  180).

flight(toulouse, united, paris, 75, 150).

airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).


printflights(A, B) :-
	(flight(A, C, B, D, E);
	flight(B, C, A, D, E)),
	printFlight(A, C, B, D, E),
	printFlight(B, C, A, D, E).


printdetails(A, C, B, D, E):-
	write('\n\nFlight Name : '),
	write(C),
	write('\n\nDeparture From : '),
	write(A),
	write('\n\nArrival To : '),
	write(B),
	write('\n\nPrice : '),
	write(D),	
	write('\n\nDuration : '),	
	write(E),
	write(' minutes').
                                                                                                                                                                            

/*(a) Is there a flight from Toronto to Madrid?.*/
flight_xtoy(X, Y) :- flight(X,B,Y,D,E), printdetails(X, B, Y, D, E).


/*#(b) A flight from city A to city B with airline C is cheap if its price is less than $400. */
is_cheap(A, C, B):-flight(A, C, B, P, _), P < 400.    


/*#(c) Is it possible to go from Toronto to ::Paris in two flights? .*/
is_possible_xtoy_twoflight(A, B):-flight(A, _,Z, _, _),flight(Z, _, B, _, _), Z \== A, Z \== B. 


/*#(d) A flight from city A to city B with airline C is preferred if it’s cheap (see (b)) or it’s with Air Canada. */
is_cheap_is_aircanada(A, B):-(flight(A, C, B, P, _), P < 400); (flight(A, C, B, P, _), C == aircanada). 


/*#(e) If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. */
/*is_united_is_aircanada(A, B):-flight(A, C, B, _, _), C \== united.*/


/*#(e) If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. */
is_united_is_aircanada(A, B):-flight(A, C, B, _, _), C == united -> flight(A, D, B, _, _), D==aircanada.












