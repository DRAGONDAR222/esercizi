-- Tipi di dato non standard

CREATE DOMAIN Stringa AS varchar(255);

CREATE DOMAIN RealGEZ AS real
CHECK (value >= 0);

CREATE DOMAIN RealZO AS real
CHECK (value IN (0,1));

CREATE DOMAIN posinteger AS integer
CHECK (value >= 0);

CREATE TYPE Indirizzo AS (
  via Stringa,
  civico Stringa,
  CAP integer
);

CREATE DOMAIN CodiceFiscale AS char(16);

CREATE DOMAIN PartitaIVA AS char(11)
CHECK (value ~ '^[0-9]{11}$');

CREATE DOMAIN Telefono AS varchar(20)
CHECK (value ~ '^\+?[0-9\s\-\(\)]{6,20}$');

CREATE DOMAIN Email AS varchar(254)
CHECK (value ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

CREATE TYPE stato AS ENUM (
  'in preparazione',
  'inviato',
  'da saldare',
  'saldato'
);
