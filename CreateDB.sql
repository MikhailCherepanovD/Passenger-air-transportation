DROP TABLE IF EXISTS passenger CASCADE;
DROP TABLE IF EXISTS ticket CASCADE;
DROP TABLE IF EXISTS route_segment CASCADE;
DROP TABLE IF EXISTS class_of_service CASCADE;
DROP TABLE IF EXISTS flight_final_set CASCADE;
DROP TABLE IF EXISTS seat CASCADE;
DROP TABLE IF EXISTS class_of_service_airplane CASCADE;
DROP TABLE IF EXISTS airplane  CASCADE;
DROP TABLE IF EXISTS airplane_flight  CASCADE;
DROP TABLE IF EXISTS flight CASCADE ;
DROP TABLE IF EXISTS airport CASCADE;

CREATE TABLE passenger(
	passenger_id SERIAL PRIMARY KEY,
	last_name varchar(50),
	first_name varchar(30),
	middle_name varchar(30),
	passport_series char(4)  CHECK(passport_series ~ '[0-9]{4}'),
	passport_number char(7)  CHECK(passport_number ~ '[0-9]{7}'),
	date_of_birth DATE CHECK (date_of_birth >= '1890-01-01' AND date_of_birth <= CURRENT_DATE)
);

CREATE TABLE ticket(
    ticket_id SERIAL PRIMARY KEY,
    passenger_id INT
);

CREATE TABLE route_segment(
    route_segment_id SERIAL PRIMARY KEY,
	ticket_id INT,
    airport_flight_id INT,
	
    airport_of_landing_id INT,
    class_of_service_id INT,
    flight_final_set_id INT,
    number_of_baggage INT CHECK (number_of_baggage>=0 AND number_of_baggage<100)
);

CREATE TABLE flight_final_set(
    flight_final_set_id SERIAL PRIMARY KEY,
    flight_id INT,
    seat_id INT,
    number_of_baggage INT CHECK (number_of_baggage>=0 AND number_of_baggage<100)
);



CREATE TABLE class_of_service(
    class_of_service_id SERIAL PRIMARY KEY,
    name_class varchar(30)
);

CREATE TABLE seat(
    seat_id SERIAL PRIMARY KEY,
    class_of_service_id INT,
    airplane_id INT,
    number_of_seat varchar(5)
);

CREATE TABLE class_of_service_airplane(
    airplane_id INT,
    class_of_service_id INT,
	PRIMARY KEY (airplane_id, class_of_service_id)
);

CREATE TABLE airplane(
    airplane_id SERIAL PRIMARY KEY,
    model varchar(80),
	registration_number varchar(15),
    number_of_baggage INT CHECK (number_of_baggage>=0 AND number_of_baggage<250000)
);

CREATE TABLE airplane_flight(
    airplane_id INT,
    flight_id INT,
	PRIMARY KEY (airplane_id, flight_id)
);

CREATE TABLE flight(
    flight_id SERIAL PRIMARY KEY,
    airport_flight_id INT,
    airport_of_landing_id INT,
    date_and_time_flight TIMESTAMP CHECK (date_and_time_flight >= '1903-12-17 00:00:00' AND date_and_time_flight <= '2124-04-29 00:00:00'),
    date_and_time_landing TIMESTAMP CHECK (date_and_time_landing >= '1903-12-17 00:00:00' AND date_and_time_landing <= '2124-04-29 00:00:00')
);

CREATE TABLE airport(
	airport_id SERIAL PRIMARY KEY,
  	name_airport varchar(70),
	country varchar(60)
);

CREATE TABLE seat(
    seat_id SERIAL PRIMARY KEY,
    class_of_service_id INT,
    airplane_id INT,
    number_of_seat varchar(5)
);

ALTER TABLE route_segment 
	ADD FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
	ADD FOREIGN KEY (airport_flight_id) REFERENCES airport(airport_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
 	ADD FOREIGN KEY (airport_of_landing_id) REFERENCES airport(airport_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (class_of_service_id) REFERENCES class_of_service(class_of_service_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (flight_final_set_id) REFERENCES flight_final_set(flight_final_set_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;



ALTER TABLE ticket
    ADD FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;



ALTER TABLE flight_final_set
    ADD FOREIGN KEY (flight_id) REFERENCES flight(flight_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (seat_id) REFERENCES seat(seat_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;

ALTER TABLE seat
    ADD FOREIGN KEY (class_of_service_id) REFERENCES class_of_service(class_of_service_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (airplane_id) REFERENCES airplane(airplane_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;

ALTER TABLE class_of_service_airplane
    ADD FOREIGN KEY (airplane_id) REFERENCES airplane(airplane_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (class_of_service_id) REFERENCES class_of_service(class_of_service_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;



ALTER TABLE airplane_flight
    ADD FOREIGN KEY (airplane_id) REFERENCES airplane(airplane_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (flight_id) REFERENCES flight(flight_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;



ALTER TABLE flight
    ADD FOREIGN KEY (airport_flight_id) REFERENCES airport(airport_id)
	ON UPDATE CASCADE ON DELETE NO ACTION,
    ADD FOREIGN KEY (airport_of_landing_id) REFERENCES airport(airport_id)
	ON UPDATE CASCADE ON DELETE NO ACTION;


 CREATE INDEX passenger_last_name_idx ON passenger (last_name);
 CREATE INDEX passenger_passport_number_idx ON passenger (passport_number);
 CREATE INDEX passenger_passport_series_idx ON passenger (passport_series);
 CREATE INDEX passenger_passenger_id_idx ON passenger (passenger_id);


 CREATE INDEX route_segment_ticket_id_idx ON route_segment (ticket_id);
 CREATE INDEX route_segment_airport_flight_id_idx ON route_segment (airport_flight_id);
 CREATE INDEX route_segment_airport_of_landing_id_idx ON route_segment (airport_of_landing_id);
 CREATE INDEX route_segment_class_of_service_id_idx ON route_segment (class_of_service_id);
 CREATE INDEX route_segment_flight_final_set_id_idx ON route_segment (flight_final_set_id);


 CREATE INDEX flight_final_set_flight_id_idx ON flight_final_set (flight_id);
 CREATE INDEX flight_final_set_seat_id_idx ON flight_final_set (seat_id);

 CREATE INDEX flight_airport_flight_id_idx ON flight (airport_flight_id);
 CREATE INDEX flight_airport_of_landing_id_idx ON flight (airport_of_landing_id);

 CREATE INDEX airport_name_airport_idx ON airport (name_airport);

 CREATE INDEX class_of_service_name_class_idx ON class_of_service (name_class);


 CREATE INDEX airplane_flight_airplane_id_idx ON airplane_flight (airplane_id);
 CREATE INDEX airplane_flight_flight_id_idx ON airplane_flight (flight_id);



 CREATE INDEX class_of_service_airplane_airplane_id_idx ON class_of_service_airplane (airplane_id);
 CREATE INDEX class_of_service_airplane_class_of_service_id_idx ON class_of_service_airplane (class_of_service_id);


 CREATE INDEX seat_class_of_service_id_idx ON seat (class_of_service_id);
 CREATE INDEX seat_airplane_id ON seat (airplane_id);

