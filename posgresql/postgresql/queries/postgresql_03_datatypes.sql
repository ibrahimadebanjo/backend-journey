CREATE EXTENSION IF NOT EXISTS pycrypto;

CREATE TABLE basics.events (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
event_name TEXT NOT NULL,
metadata JSONB DEFAULT '{}'::jsonb,
created_at TIMESTAMP DEFAULT NOW()
);


INSERT INTO basics.events ( event_name, metadata)
VALUES
(
'conference', 
'{"attendat" : "Ibrahim"} '
),
(
'webiner',
'{"attendant" : "owolabi"}'
);
