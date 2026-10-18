-- OWNERS (15)
INSERT INTO clinic.owners (name, phone, email, address) VALUES
('Ibrahim Adebanjo', '08158310258', 'ibro@gmail.com', '12, Bolanle St, Lagos'),
('Aisha Bello', '08031234567', 'aisha.b@gmail.com', '5, Aminu Kano Cres, Abuja'),
('Chinedu Okafor', '09087654321', 'chinedu.o@yahoo.com', '22, Enugu Rd, Onitsha'),
('Fatima Sani', '07065432198', 'fatima.s@hotmail.com', '10, Zoo Rd, Kano'),
('Tunde Bakare', '08123456789', 'tunde.bakare@gmail.com', '15, Allen Ave, Ikeja'),
('Zainab Musa', '08099887766', 'zainab.m@gmail.com', '3, Garki Area 11, Abuja'),
('Emeka Nwosu', '09011223344', 'emeka.n@gmail.com', '8, Owerri Rd, Owerri'),
('Hauwa Ali', '07088776655', 'hauwa.ali@gmail.com', '18, Kaduna Rd, Zaria'),
('Sola Adeyemi', '08155667788', 'sola.ade@yahoo.com', '20, Ring Rd, Ibadan'),
('Ngozi Eze', '08077665544', 'ngozi.eze@gmail.com', '11, Ogui Rd, Enugu'),
('Yusuf Garba', '09066554433', 'yusuf.g@gmail.com', '7, Maiduguri Rd, Kano'),
('Kemi Olatunji', '07033221100', 'kemi.o@gmail.com', '9, Lekki Phase 1, Lagos'),
('Abdul Ahmed', '08144332211', 'abdul.ahmed@gmail.com', '14, Wuse 2, Abuja'),
('Blessing Okoro', '08055443322', 'blessing.o@gmail.com', '6, Benin-Asaba Rd, Benin'),
('Sadiq Umar', '09077665544', 'sadiq.u@gmail.com', '2, Sokoto Rd, Gusau');

-- VETS (5 is enough, they repeat)
INSERT INTO clinic.vets (name, specialty, phone, email) VALUES
('Dr. Funke Alabi', 'Small Animals', '08012345678', 'funke.alabi@vet.com'),
('Dr. John Doe', 'Surgery', '09023456789', 'john.doe@vet.com'),
('Dr. Amina Lawal', 'Dermatology', '07034567890', 'amina.l@vet.com'),
('Dr. Peter Obi', 'Exotic Pets', '08145678901', 'peter.obi@vet.com'),
('Dr. Grace Johnson', 'General Practice', '08056789012', 'grace.j@vet.com');

-- PETS (15) - owner_id 1 to 15
INSERT INTO clinic.pets (name, species, breed, age, owner_id) VALUES
('Bingo', 'Dog', 'German Shepherd', 3, 1),
('Whiskers', 'Cat', 'Persian', 2, 2),
('Max', 'Dog', 'Labrador', 5, 3),
('Coco', 'Dog', 'Poodle', 1, 1),
('Simba', 'Cat', 'Maine Coon', 4, 4),
('Rocky', 'Dog', 'Bulldog', 2, 5),
('Milo', 'Cat', 'Siamese', 1, 6),
('Buddy', 'Dog', 'Golden Retriever', 6, 7),
('Luna', 'Cat', 'British Shorthair', 3, 8),
('Charlie', 'Dog', 'Beagle', 2, 9),
('Daisy', 'Rabbit', 'Angora', 1, 10),
('Oscar', 'Dog', 'Rottweiler', 4, 11),
('Bella', 'Cat', 'Ragdoll', 2, 12),
('Zara', 'Dog', 'Husky', 3, 13),
('Kitty', 'Bird', 'Parrot', 2, 14);

-- APPOINTMENTS (15) - linking pets and vets
INSERT INTO clinic.appointments (pet_id, vet_id, appointment_date, reason) VALUES
(1, 1, '2026-01-10', 'Annual Vaccination'),
(2, 3, '2026-01-11', 'Skin rash'),
(3, 2, '2026-01-12', 'Leg injury'),
(4, 1, '2026-01-13', 'Deworming'),
(5, 5, '2026-01-14', 'General checkup'),
(6, 1, '2026-01-15', 'Coughing'),
(7, 3, '2026-01-16', 'Fur loss'),
(8, 2, '2026-01-17', 'Surgery consultation'),
(9, 5, '2026-01-18', 'Vomiting'),
(10, 1, '2026-01-19', 'Ear infection'),
(11, 4, '2026-01-20', 'Not eating'),
(12, 2, '2026-01-21', 'Fracture'),
(13, 5, '2026-01-22', 'Lethargy'),
(14, 1, '2026-01-23', 'Vaccination'),
(15, 4, '2026-01-24', 'Wing injury');

-- VISITS (15) - one per appointment
INSERT INTO clinic.visits (appointment_id, visit_date, diagnosis, treatment) VALUES
(1, '2026-01-10', 'Healthy', 'DHPP Vaccine given'),
(2, '2026-01-11', 'Fungal infection', 'Antifungal cream'),
(3, '2026-01-12', 'Sprain', 'Rest + Painkillers'),
(4, '2026-01-13', 'Worms', 'Deworming tablet'),
(5, '2026-01-14', 'Healthy', 'Routine check - OK'),
(6, '2026-01-15', 'Kennel cough', 'Antibiotics 5 days'),
(7, '2026-01-16', 'Allergy', 'Antihistamine'),
(8, '2026-01-17', 'Needs surgery', 'Scheduled for next week'),
(9, '2026-01-18', 'Food poisoning', 'IV fluids + Diet'),
(10, '2026-01-19', 'Otitis', 'Ear drops'),
(11, '2026-01-20', 'Dental issue', 'Teeth cleaning'),
(12, '2026-01-21', 'Fracture confirmed', 'Cast applied'),
(13, '2026-01-22', 'Anemia', 'Iron supplements'),
(14, '2026-01-23', 'Healthy', 'Rabies vaccine'),
(15, '2026-01-24', 'Feather damage', 'Vitamin supplements');

-- INVOICES (15) - one per visit
INSERT INTO clinic.invoices (visit_id, amount, status, issued_date) VALUES
(1, 15000.00, 'paid', '2026-01-10'),
(2, 8000.00, 'paid', '2026-01-11'),
(3, 25000.00, 'unpaid', '2026-01-12'),
(4, 5000.00, 'paid', '2026-01-13'),
(5, 10000.00, 'paid', '2026-01-14'),
(6, 12000.00, 'unpaid', '2026-01-15'),
(7, 7000.00, 'paid', '2026-01-16'),
(8, 50000.00, 'unpaid', '2026-01-17'),
(9, 20000.00, 'paid', '2026-01-18'),
(10, 9000.00, 'paid', '2026-01-19'),
(11, 15000.00, 'unpaid', '2026-01-20'),
(12, 40000.00, 'paid', '2026-01-21'),
(13, 11000.00, 'paid', '2026-01-22'),
(14, 15000.00, 'paid', '2026-01-23'),
(15, 6000.00, 'unpaid', '2026-01-24');