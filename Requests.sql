--1.1
SELECT  ps.*  FROM passenger ps
	JOIN ticket tick ON tick.passenger_id = ps.passenger_id
	JOIN route_segment rs ON rs.ticket_id = tick.ticket_id
	JOIN airport ap ON ap.airport_id = rs.airport_flight_id
	JOIN class_of_service cs_planned ON cs_planned.class_of_service_id = rs.class_of_service_id
	WHERE ap.name_airport='Лос-Анджелес'
	AND cs_planned.name_class='Бизнес'
	AND rs.number_of_baggage = 0;




--1.2
SELECT  ps.*  AS FINAL_CLASS FROM passenger ps
	JOIN ticket tick ON tick.passenger_id = ps.passenger_id
	JOIN route_segment rs ON rs.ticket_id = tick.ticket_id
	JOIN airport ap ON ap.airport_id = rs.airport_flight_id
	JOIN class_of_service cs_planned ON cs_planned.class_of_service_id = rs.class_of_service_id
	JOIN flight_final_set ffs ON ffs.flight_final_set_id = rs.flight_final_set_id
	JOIN seat s ON s.seat_id = ffs.seat_id
	JOIN class_of_service cs_final ON cs_final.class_of_service_id = s.class_of_service_id
	WHERE ap.name_airport='Лос-Анджелес'
	AND rs.number_of_baggage = 0
	AND cs_planned.name_class <> cs_final.name_class;  



--2
SELECT COUNT(*) from airplane 
	JOIN airplane_flight af ON af.airplane_id = airplane.airplane_id 
	JOIN flight f ON f.flight_id = af.flight_id
	JOIN airport airport_flight ON airport_flight.airport_id = f.airport_flight_id
	JOIN airport airport_land   ON airport_land.airport_id = f.airport_of_landing_id
	WHERE airport_flight.name_airport = 'Торонто' AND airport_land.name_airport ='Пулково'

--3.1 
SELECT  airport_flight.name_airport , count(*) FROM ticket  tick
	JOIN route_segment rs ON rs.ticket_id = tick.ticket_id
	JOIN flight_final_set ffs ON ffs.flight_final_set_id = rs.flight_final_set_id
	JOIN flight f ON f.flight_id = ffs.flight_id
	JOIN airport airport_flight ON airport_flight.airport_id = rs.airport_flight_id
	WHERE EXTRACT(YEAR FROM f.date_and_time_flight) = 2024
	GROUP BY airport_flight.name_airport



--3.2 

SELECT airport.name_airport, count(*) FROM airport 
	JOIN flight f ON f.airport_flight_id  = airport.airport_id
	JOIN airplane_flight  af ON af.flight_id = f.flight_id
	JOIN airplane ON airplane.airplane_id = af.airplane_id
	JOIN seat s ON s.airplane_id = airplane.airplane_id
	WHERE EXTRACT(YEAR FROM  f.date_and_time_flight) = 2024
	GROUP BY airport.name_airport




--4 MAX
SELECT a.airplane_id,  COUNT(af.flight_id) 
    FROM airplane a
    JOIN airplane_flight af ON a.airplane_id = af.airplane_id
    GROUP BY a.airplane_id, a.registration_number,a.model, a.number_of_baggage
	HAVING COUNT(af.flight_id) =(SELECT count_flight
		FROM (
			SELECT COUNT(af.flight_id)AS count_flight FROM  airplane a
    			JOIN airplane_flight af ON a.airplane_id = af.airplane_id
    			GROUP BY a.airplane_id
				ORDER BY count_flight DESC
	LIMIT 1
) AS counts) 


--4 MIN
SELECT a.airplane_id,  COUNT(af.flight_id) 
    FROM airplane a
    JOIN airplane_flight af ON a.airplane_id = af.airplane_id
    GROUP BY a.airplane_id, a.registration_number,a.model, a.number_of_baggage
	HAVING COUNT(af.flight_id) =(SELECT count_flight
		FROM (
			SELECT COUNT(af.flight_id)AS count_flight FROM  airplane a
    			JOIN airplane_flight af ON a.airplane_id = af.airplane_id
    			GROUP BY a.airplane_id
				ORDER BY count_flight ASC
	LIMIT 1
) AS counts) 



--5


SELECT amount_seat ,count(*) FROM(
SELECT f.flight_id, count(*)AS amount_seat from flight f
	JOIN airplane_flight af ON af.flight_id = f.flight_id
	JOIN airplane a ON a.airplane_id = af.airplane_id
	JOIN seat s ON s.airplane_id = a.airplane_id
	GROUP BY f.flight_id
) AS airplane_seat
	GROUP BY amount_seat
	
	
	
	
	
--6
SELECT  p.passenger_id,  p.first_name,  p.last_name,  COUNT(t.ticket_id) AS ticket_count FROM  passenger p
	JOIN  ticket t ON t.passenger_id = p.passenger_id
	GROUP BY p.passenger_id, p.first_name,  p.last_name
	HAVING COUNT(t.ticket_id) >(SELECT COUNT(t.ticket_id) FROM ticket t WHERE t.passenger_id = 1)








--7 

SELECT plan.registration_number
FROM airplane plan
WHERE plan.airplane_id NOT IN(
SELECT DISTINCT plan.airplane_id FROM airplane plan
	JOIN airplane_flight af ON af.airplane_id = plan.airplane_id
	JOIN flight f ON f.flight_id = af.flight_id
	JOIN airport port_flight ON port_flight.airport_id = f.airport_flight_id
	JOIN airport port_landing ON port_landing.airport_id = f.airport_of_landing_id
	WHERE port_landing.name_airport = 'Сингапур Чанги'
	OR port_flight.name_airport  = 'Сингапур Чанги'
	ORDER BY plan.airplane_id
)
	



--8

SELECT a.airplane_id, cs.name_class,
	(
		SELECT COUNT(*)
		FROM airplane_flight af
		JOIN flight f ON f.flight_id = af.flight_id
		JOIN flight_final_set ffs ON ffs.flight_id = f.flight_id
		JOIN route_segment rs ON rs.flight_final_set_id = ffs.flight_final_set_id
		JOIN class_of_service cs1 ON cs1.class_of_service_id = rs.class_of_service_id
		WHERE af.airplane_id = a.airplane_id 
		AND cs1.class_of_service_id = cs.class_of_service_id
	) AS count_occupied
FROM airplane a
CROSS JOIN class_of_service cs
ORDER BY a.airplane_id;












