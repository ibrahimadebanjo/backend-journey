
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

## 3. PostgreSQL Data Types & Advanced Column Structures

### Core Data Types Breakdown

* **`VARCHAR(length)`:** Variable character string with a defined maximum length limit (e.g., `VARCHAR(50)`, `VARCHAR(100)`).
* **`TEXT`:** Unlimited-length string field. Use single quotes (`'text'`) for values.
* **`INTEGER`:** 4-byte standard integer values.
* **`BIGINT`:** 8-byte large integer storage (ideal for large count metrics like `total_views`).
* **`NUMERIC(precision, scale)`:** Exact numeric storage (e.g., `NUMERIC(10,2)` stores 10 total digits with 2 digits after the decimal point—ideal for monetary prices).
* **`BOOLEAN`:** Logical boolean field (`true` / `false`).
* **`SERIAL`:** Auto-incrementing integer key generator.
* **`UUID`:** Universally Unique Identifier for generating non-sequential primary keys.
* **`JSONB`:** Binary JSON data structure for flexible, queryable unstructured data.

---

### Creating Tables with Advanced Types (UUID, JSONB & Defaults)

#### Generating UUIDs & Working with JSONB

```sql
-- Ensure pgcrypto or uuid-ossp extension is enabled for gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Table using UUID, JSONB, and automated Timestamp defaults
CREATE TABLE basics.events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_name TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW()
);

```

> **Casting Rule:** PostgreSQL requires `::` for explicit type casting with **no spaces** between the double colons (e.g., `'{}'::jsonb`).

---

### Basic Table Syntax & Executed Query Examples

#### Creating `basics.students`

```sql
CREATE TABLE basics.students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER CHECK (age >= 18),
    created_at TIMESTAMP DEFAULT NOW()
);

```

#### Executed Query: `basics.products`

```sql
CREATE TABLE basics.products (
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

## 4. Data Insertion & Query Executions

### Rules for Quoting & Order

* **Single Quotes (`'...'`):** Strictly used for text values and strings.
* **Double Quotes (`"..."`):** Reserved exclusively for schema, table, or column names with special formatting.
* **Column Alignment:** Values inserted must strictly follow the column order defined in the table or the explicit target column list.

---

### Inserting Records

#### Inserting JSONB & Default Data into `basics.events`

```sql
INSERT INTO basics.events (event_name, metadata)
VALUES 
    ('Conference', '{"attendant": "Ibrahim"}'),
    ('Webinar', '{"attendant": "Owolabi"}');

```

#### Ordered Value Insertions with Optional/Default Fields

```sql
INSERT INTO basics.value_example (nickname, bio, score)
VALUES 
    (NULL, 'Learning', 10),
    ('', 'empty_nickname', 20),
    ('Ibrahim', '', 0);

```

#### Executed Data Insertion: `basics.students`

```sql
INSERT INTO basics.students (name, email, age) 
VALUES 
  ('ibrahim', 'ibrahim@gmail.com', 24),
  ('owolabi', 'owolabi@gmail.com', 24);

```

#### Executed Data Insertion: `basics.products`

```sql
INSERT INTO basics.products (name, description, stock, total_views, price)
VALUES ('LA', 'antibiotics', 5, 100, 400.00);

```

---

## 5. Handling `NULL`, Empty Strings, and Zero Values

It is critical to distinguish between missing data, empty text, and numerical zero:

* **`NULL`:** Represents an unknown or missing value.
* **Empty String (`''`):** Represents a known string value containing zero characters.
* **Zero (`0`):** Represents an actual numeric value of 0.

```sql
-- Querying NULL values
SELECT * FROM basics.value_example 
WHERE nickname IS NULL;

-- Querying Empty Strings
SELECT * FROM basics.value_example 
WHERE nickname = '';

-- Querying Numeric Zero
SELECT * FROM basics.value_example 
WHERE score = 0;

```

---

## 6. Database Constraints

Database constraints enforce strict integrity rules at the storage level, providing significantly stronger validation than backend application code.

### The 6 PostgreSQL Constraint Types

1. **`NOT NULL`:** Prevents a column from accepting `NULL` values, forcing every row to contain a valid entry.
2. **`UNIQUE`:** Guarantees that all values in a column (or group of columns) are distinct across rows. Allows `NULL` by default.
3. **`PRIMARY KEY`:** Combines `NOT NULL` and `UNIQUE` into a single unique constraint that identifies each row.
4. **`FOREIGN KEY`:** Links a column to a primary key column in another table, maintaining referential integrity between tables.
5. **`CHECK`:** Evaluates column values using a specific boolean expression; rejects any row where the condition returns `false`.
6. **`EXCLUSION`:** Ensures that if any two rows are compared on specified columns using specific operators, at least one comparison returns `false`.

> **Note on Primary Keys:** Operating without a Primary Key makes updating, deleting, and referencing individual rows in a table exceptionally difficult.

---

## 7. Data Querying, Filtering & Aliases

### Basic Projection & `IN` Operator

The `IN` operator allows checking a column against a list of specified values.

```sql
SELECT name, category, price, stock, description 
FROM products 
WHERE price IN (400.00, 200.00, 500.00);

```

### Column & Table Aliases (`AS`)

Aliases allow renaming columns or tables temporarily for output readability.

```sql
SELECT 
    name AS product_name,
    price AS selling_price,
    stock AS available_quantity
FROM products AS p;

```

### Logical Filtering (`WHERE`, `AND`, `OR`, `NOT`)

```sql
-- Single Logical Condition
SELECT name, category, price 
FROM products 
WHERE category = 'electronics' AND price > 1000;

-- Multiple Conditional Checks
SELECT name, category, price, stock 
FROM products 
WHERE (category = 'electronics' OR category = 'furniture') 
  AND stock > 0;

-- Negation Check
SELECT name, category 
FROM products 
WHERE NOT category = 'furniture';

```

### Pattern Matching (`LIKE`, `ILIKE`)

* **`LIKE`:** Case-sensitive pattern matching.
* **`ILIKE`:** Case-insensitive pattern matching.
* **`%` Wildcard:** Matches any sequence of zero or more characters.
* **`_` Wildcard:** Matches exactly one single character.

```sql
-- Case-Sensitive Search (Starts with "Wireless")
SELECT name, price 
FROM products 
WHERE name LIKE 'Wireless%';

-- Case-Insensitive Search (Contains "desk" anywhere)
SELECT name, category, price 
FROM products 
WHERE name ILIKE '%desk%';

```

> **Other Comparison Operators:** `BETWEEN`, `NOT IN`, `AND`.

---

## 8. Data Manipulation (Updating & Deleting Rows)

### Updating Single or Multiple Records

```sql
-- Updating a Single Row via Key/Identifier
UPDATE products 
SET price = 1199.50 
WHERE sku = '023-441';

-- Updating Multiple Rows with Functions
UPDATE products 
SET price = ROUND(price * 1.10, 2) 
WHERE category = 'Stationery';

-- Updating Status based on Stock Level
UPDATE products 
SET is_active = FALSE 
WHERE stock = 0;

```

### Deleting Records

```sql
DELETE FROM products 
WHERE name = 'Unknown';

```

---

## 9. Table Relationships & Foreign Keys

### One-to-Many Relationships

To establish references to another table's primary key, define a foreign key linking the child table to the parent table.

```sql
-- Parent Table Reference Example
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES Users(id)
);

CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id UUID NOT NULL REFERENCES posts(id)
);

```

### Many-to-Many Relationships & Junction Tables

A many-to-many relationship requires a intermediate (junction) table containing foreign keys from both primary tables, often combining them into a **Composite Primary Key**.

```sql
-- Entity Table 1
CREATE TABLE tags (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL UNIQUE
);

-- Junction Table linking Posts and Tags
CREATE TABLE post_tags (
    post_id UUID NOT NULL REFERENCES posts(id),
    tag_id UUID NOT NULL REFERENCES tags(id),
    PRIMARY KEY (post_id, tag_id)  -- Composite Primary Key
);

```

> **Terminology Mapping:**
> * `User.id` = Base Parent Key
> * `posts.user_id` = Foreign Key pointing to `Users(id)`
> 
> 

---

## 10. Table Joins (`INNER JOIN`, `LEFT JOIN`)

When joining tables, place the target connection table after the join type.

### Join Types Breakdown

1. **`INNER JOIN`:** Returns only matching rows that exist in both tables.
2. **`LEFT JOIN`:** Keeps all rows from the left table. If matching records exist in the right table, it returns them; if no match exists, it fills the right table columns with `NULL`.

```sql
-- Standard Inner Join with Column Aliases
SELECT 
    Users.name AS author_name,
    posts.title AS post_title,
    posts.status
FROM Users 
INNER JOIN posts ON Users.id = posts.user_id 
ORDER BY Users.name, posts.title;

-- Multi-Table Join Query (Posts -> Users & Comments)
SELECT 
    p.title AS post_title,
    p.status,
    p.views,
    u.name AS author_name,
    c.body AS comment_body
FROM posts AS p
INNER JOIN Users AS u ON p.user_id = u.id
LEFT JOIN comments AS c ON p.id = c.post_id
ORDER BY p.views DESC;

-- Many-to-Many Join Query Across Junction Table
SELECT 
    posts.title AS post_title,
    tags.name AS tag_name
FROM posts
INNER JOIN post_tags ON posts.id = post_tags.post_id
INNER JOIN tags ON post_tags.tag_id = tags.id
ORDER BY posts.title, tags.name;

```

---

## 11. Aggregations, Grouping & Pagination

### Aggregate Functions

Calculates a single result from multiple rows:

* **`COUNT()`:** Returns the total number of rows/entries.
* **`SUM()`:** Calculates the total added value.
* **`AVG()`:** Calculates the mathematical average.
* **`MIN()`:** Finds the smallest value.
* **`MAX()`:** Finds the largest value.

```sql
SELECT COUNT(*) AS total_posts FROM posts;

SELECT 
    SUM(views) AS total_views,
    AVG(views) AS avg_views
FROM posts;

```

---

### `GROUP BY` and `HAVING` Clauses

* **`WHERE`:** Filters individual normal rows **before** grouping occurs.
* **`GROUP BY`:** Groups rows sharing common column values.
* **`HAVING`:** Filters summarized groups **after** aggregation occurs.

```sql
-- Find authors who have written at least 2 posts
SELECT 
    u.name AS author_name,
    COUNT(p.id) AS total_posts,
    SUM(p.views) AS total_views
FROM Users AS u
LEFT JOIN posts AS p ON u.id = p.user_id
GROUP BY u.id, u.name
HAVING COUNT(p.id) >= 2
ORDER BY total_posts DESC;

```

---

### Pagination (`LIMIT` and `OFFSET`)

Used to segment query output into pages.

```sql
-- Page 1 (First 5 records)
SELECT name, price 
FROM products 
ORDER BY name DESC 
LIMIT 5 OFFSET 0;

-- Page 2 (Next 5 records)
SELECT name, price 
FROM products 
ORDER BY name ASC 
LIMIT 5 OFFSET 5;

```

---

## 12. Advanced Tables, Subqueries, Transactions & Indexes

### Tables with `CHECK` Validation Constraints

```sql
CREATE TABLE posts (
    title TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'published')),
    views INTEGER NOT NULL DEFAULT 0 CHECK (views >= 0)
);

```

---

### Subqueries (Nested Queries)

A subquery is a query nested inside another SQL statement.

```sql
-- Select posts with views above average
SELECT title, status, views 
FROM posts 
WHERE views > (
    SELECT AVG(views) 
    FROM posts
)
ORDER BY views DESC;

```

---

### SQL Transactions

Transactions bundle multiple SQL commands together as a single atomic unit of execution.

```sql
BEGIN;
-- Run multiple SQL statements safely here
COMMIT;

```

---

### Database Indexes

Indexes significantly accelerate query lookups and row retrieval speeds across large tables.

```sql
-- Creating a Composite Index across multiple columns
CREATE INDEX IF NOT EXISTS idx_posts_status_views 
ON posts (status, views DESC);

```

---

## 13. PostgreSQL Extensions Summary

Extensions add specialized features and plugin tools directly into your PostgreSQL database.

```sql
-- Syntax to install an extension
CREATE EXTENSION IF NOT EXISTS "extension_name";

```

### Common Extensions

1. **`uuid-ossp`:** Provides functions for generating random UUID key structures.
2. **`pgcrypto`:** Provides functions to encrypt sensitive data, hash passwords, and generate UUIDs via `gen_random_uuid()`.
3. **`postgis`:** Enables spatial, geographic mapping, GPS location tracking, and distance calculations.
4. **`pg_trgm`:** Adds trigram-based text search functions for fuzzy string search optimizations.