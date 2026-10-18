CREATE SCHEMA IF NOT EXISTS clinic;

DROP TABLE IF EXISTS clinic.invoices CASCADE;
DROP TABLE IF EXISTS clinic.visits CASCADE;
DROP TABLE IF EXISTS clinic.appointments CASCADE;
DROP TABLE IF EXISTS clinic.pets CASCADE;
DROP TABLE IF EXISTS clinic.vets CASCADE;
DROP TABLE IF EXISTS clinic.owners CASCADE;


CREATE TABLE clinic.owners (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone VARCHAR(20),
    email TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL
);


CREATE TABLE clinic.vets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    phone VARCHAR(20),
    email TEXT UNIQUE
);


CREATE TABLE clinic.pets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL, -- Dog, Cat, Bird
    breed TEXT,
    age INT,
    owner_id INT NOT NULL REFERENCES clinic.owners(id) ON DELETE CASCADE
);

CREATE TABLE clinic.appointments (
    id SERIAL PRIMARY KEY,
    pet_id INT NOT NULL REFERENCES clinic.pets(id) ON DELETE CASCADE,
    vet_id INT NOT NULL REFERENCES clinic.vets(id),
    appointment_date DATE NOT NULL,
    reason TEXT
);


CREATE TABLE clinic.visits (
    id SERIAL PRIMARY KEY,
    appointment_id INT NOT NULL UNIQUE REFERENCES clinic.appointments(id) ON DELETE CASCADE,
    visit_date DATE NOT NULL,
    diagnosis TEXT,
    treatment TEXT
);

CREATE TABLE clinic.invoices (
    id SERIAL PRIMARY KEY,
    visit_id INT NOT NULL UNIQUE REFERENCES clinic.visits(id) ON DELETE CASCADE,
    amount DECIMAL(10,2) NOT NULL,
    status TEXT NOT NULL DEFAULT 'unpaid', 
    issued_date DATE NOT NULL
);