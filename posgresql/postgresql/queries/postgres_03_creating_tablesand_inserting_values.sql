CREATE TABLE basics.products(
id SERIAL PRIMARY KEY ,
name VARCHAR(50),
description TEXT,
stock INTEGER DEFAULT 0,
total_views BIGINT DEFAULT 0,
price NUMERIC(10,2),
is_active BOOLEAN DEFAULT true
);

INSERT INTO basics.products(name, description, stock, total_views, price)
VALUES
('LA', 'antibiotics', 5, 100, 400.00)