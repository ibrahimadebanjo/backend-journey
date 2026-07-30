
---

# PostgreSQL & Supabase Documentation

## 1. Setup & Environment Configuration

### Essentials for Writing PostgreSQL on Mobile

1. **A PostgreSQL Database to Run Queries On:** Cloud database instance (e.g., hosted via Supabase).
2. **An IDE/App for Writing Queries:** A mobile SQL client (e.g., aSQL App) connected via a connection string.

---

### Supabase Features & Capabilities

* **Database + SQL:** Host a PostgreSQL database in the cloud, run queries, create tables/indexes/joins, and import/export CSV data.
* **Auto-Generated REST API:** Create a table, and Supabase automatically generates an API layer—enabling instant frontend/mobile app fetching without backend coding.
* **Authentication:** Managed email/password login, Google, GitHub, Twitter, and phone OTP login systems.
* **Storage / File Hosting:** Upload and store images, PDFs, CSVs, videos, and profile pictures for users, generating public URLs for files.

---

### Connecting to aSQL App via Connection String

* **Host:** `db.vlnxddqfeernivepqfing.supabase.co`
* **Port:** `5432`
* **Username:** `postgres`
* **Password:** *Your Supabase Database Password*
* **Database Name:** `postgres`
* **SSL:** Enabled (`ON`) / Encrypted Password

> **Note:** Upon connecting, multiple built-in system schemas will be visible (e.g., `auth`, `storage`, `public`).

---

## 2. Database Management & Schemas

```
Database Hierarchy Mapping:
┌─────────────────────────────────────────┐
│ Database                                │
│   └─► Schemas (Folders)                 │
│         └─► Tables (Files)              │
│               └─► Rows (Data)           │
└─────────────────────────────────────────┘

```

### Managing Databases

```sql
-- Create a new database
CREATE DATABASE db_name;

-- Drop database safely if it exists
DROP DATABASE IF EXISTS db_name;

-- System checks
SELECT current_database();  -- Check active database
SELECT current_user;        -- Check active user
SELECT version();           -- Check Postgres version

```

> **Note on Supabase Architecture:** In Supabase, you get a single pre-configured database called `postgres`. Instead of creating multiple isolated databases, manage environment separation by creating **Schemas** (folders inside the database).

---

### Creating & Managing Custom Schemas

```sql
-- Create a new custom schema
CREATE SCHEMA IF NOT EXISTS basics;

-- List all custom and system schemas in the database
SELECT schema_name 
FROM information_schema.schemata 
ORDER BY schema_name;

```

#### System Schemas vs Custom Schemas

* **`auth`:** Managed internally by Supabase for user authentication data.
* **`storage`:** Managed internally by Supabase for file storage metadata.
* **`public`:** The default schema.
* **`basics` (Custom):** User-defined schemas created to house application tables separately.

---

## 3. PostgreSQL Data Types & Table Syntax

### Core Data Types Breakdown

* **`VARCHAR(length)`:** Variable character string with a defined maximum length limit (e.g., `VARCHAR(50)`, `VARCHAR(100)`).
* **`TEXT`:** Unlimited-length string field. Use single quotes (`'text'`) for values.
* **`INTEGER`:** 4-byte standard integer values.
* **`BIGINT`:** 8-byte large integer storage (ideal for large count metrics like `total_views`).
* **`NUMERIC(precision, scale)`:** Exact numeric storage (e.g., `NUMERIC(10,2)` stores 10 total digits with 2 digits after the decimal point—ideal for monetary prices).
* **`BOOLEAN`:** Logical boolean field (`true` / `false`).
* **`SERIAL`:** Auto-incrementing integer key generator.

---

### Table Creation Syntax

#### Creating the `basics.students` Table

```sql
CREATE TABLE basics.students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER CHECK (age >= 18),
    created_at TIMESTAMP DEFAULT NOW()
);

```

#### Executed Query: Creating the `basics.products` Table

```sql
CREATE TABLE basics.products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    stock INTEGER DEFAULT 0,
    total_views BIGINT DEFAULT 0,
    price NUMERIC(10,2),
    is_active BOOLEAN DEFAULT true
);

```

---

## 4. Data Insertion & Execution Results

### String Rules in PostgreSQL

* **Single Quotes (`'...'`):** Strictly used for text values and strings.
* **Double Quotes (`"..."`):** Reserved exclusively for schema, table, or column names with special formatting.

---

### Inserting Records

#### Executed Data Insertion: `basics.students`

```sql
INSERT INTO basics.students (name, email, age) 
VALUES 
  ('ibrahim', 'ibrahim@gmail.com', 24),
  ('owolabi', 'owolabi@gmail.com', 24);

```

#### Query Result Output: `basics.students`

```
Status: Success (2 Rows Returned)
Execution Time: 299ms

┌──────────┬────────────────────┬─────┐
│ NAME     │ EMAIL              │ AGE │
├──────────┼────────────────────┼─────┤
│ ibrahim  │ ibrahim@gmail.com  │ 24  │
│ owolabi  │ owolabi@gmail.com  │ 24  │
└──────────┴────────────────────┴─────┘

```

#### Executed Data Insertion: `basics.products`

```sql
INSERT INTO basics.products (name, description, stock, total_views, price)
VALUES ('LA', 'antibiotics', 5, 100, 400.00);

```

---

## 5. PostgreSQL Extensions

Extensions add functionality and features to a database instance.

```sql
-- Syntax to install a new plugin extension
CREATE EXTENSION IF NOT EXISTS "extension_name";

```

### Essential Extensions

1. **`uuid-ossp`:** Enables functions like `uuid_generate_v4()` to generate universally unique random primary key IDs.
2. **`pgcrypto`:** Adds cryptographic functions for encrypting data and hashing passwords directly inside queries.
3. **`postgis`:** Provides spatial and geographic objects for mapping, GPS tracking, and distance metrics.
4. **`pg_trgm`:** Adds trigram matching functions for fuzzy searching and text indexing performance.