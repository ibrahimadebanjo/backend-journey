

---

# SQL & Database Design Documentation

## Table of Contents

1. [Core Database Concepts](https://www.google.com/search?q=%231-core-database-concepts)
2. [Entities, Attributes, and Table Design](https://www.google.com/search?q=%232-entities-attributes-and-table-design)
3. [Relational Database Management Systems (RDBMS)](https://www.google.com/search?q=%233-relational-database-management-systems-rdbms)
4. [Introduction to SQL](https://www.google.com/search?q=%234-introduction-to-sql)
5. [Database Design & Schema Framework](https://www.google.com/search?q=%235-database-design--schema-framework)
6. [Key Constraints & Integrity](https://www.google.com/search?q=%236-key-constraints--integrity)
7. [Database Relationships](https://www.google.com/search?q=%237-database-relationships)
* [One-to-One (1:1)](https://www.google.com/search?q=%23one-to-one-11)
* [One-to-Many (1:N)](https://www.google.com/search?q=%23one-to-many-1n)
* [Many-to-Many (M:N) & Junction Tables](https://www.google.com/search?q=%23many-to-many-mn--junction-tables)



---

## 1. Core Database Concepts

### What is a Database?

* **Data:** Anything we can store in a database, write down, or that has a value (e.g., in a website scenario).
* **Database:** An organized collection of data stored and accessed electronically.

### Database Types

#### 1. Relational Databases

* **Definition:** A system that organizes and stores data in tables (rows and columns) logically connected to one another using **keys** and **relationships**.
* **Advantage over Spreadsheets:** Guarantees strict **data integrity** and transaction safety via ACID principles (All-or-Nothing transactions).
* *Examples:* PostgreSQL, MySQL, Oracle.

#### 2. NoSQL Databases

* **Definition:** Designed to handle massive volumes of unstructured or semi-structured data (e.g., emails, social media feeds, IoT streams) using flexible schema models.
* *Examples:*
* **Document DBs:** Store data in JSON-like structures (e.g., MongoDB).
* **Key-Value Stores:** Highly scalable datasets stored as key-value pairs (e.g., Redis).
* **Graph DBs:** Treat relationships as first-class data points, mapping out physical connections (e.g., Neo4j).



#### 3. Cloud & Distributed Databases

* Hosted on remote cloud infrastructure (e.g., Amazon RDS, Google Cloud SQL, Azure SQL). They provide elastic, on-demand scalability without on-premise hardware overhead.

---

## 2. Entities, Attributes, and Table Design

* **Entity:** A real-world object or concept you want to store data about.

$$\text{Rule: } 1 \text{ Entity} = 1 \text{ Table}$$


* *Example:* If you have `Movie`, `Actor`, and `Download`, you must build **3 distinct tables**.


* **Entity Type:** Represents the category of the entity (e.g., `User`, `Customer`).
* **Attribute:** A specific property or detail that describes an entity.

$$\text{Rule: } 1 \text{ Attribute} = 1 \text{ Column}$$


* **Atomic Value:** A fundamental design rule stating that **the value inside a single cell must store exactly one thing** (no lists, arrays, or multi-valued fields within a single entry).
* **Tuple / Row:** All attribute values grouped together for a single unique record.

### Table Schema Visualization

```
Entity: User
┌───────────────┬──────────────────────────┬────────────────────────┐
│  id (Col 1)   │   Username (Col 2)       │   Password (Col 3)     │  <── Columns (Attributes)
├───────────────┼──────────────────────────┼────────────────────────┤
│  1            │   Ibrahim                │   2026                 │  <── Row 1 (Tuple R1)
│  2            │   Fatima                 │   2024                 │  <── Row 2 (Tuple R2)
└───────────────┴──────────────────────────┴────────────────────────┘

```

---

## 3. Relational Database Management Systems (RDBMS)

An **RDBMS** is software that interacts with the underlying storage to manage physical data, enforce rules, and run queries.

### Core Architectural Responsibilities

* **File Management:** Manages how data is physically laid out on hard drives, servers, or computers.
* **Presentation Layer:** Formats physical data into clean, logical tables for frontend consumption.
* **View Mechanism:** Controls and changes the way data is presented dynamically without changing the underlying physical tables.
* **Consistency Enforcer:** Ensures frontend inputs stay consistent with database schema constraints.

---

## 4. Introduction to SQL

**SQL (Structured Query Language)** is the standardized language used to communicate with an RDBMS.

### Sub-Categories of SQL

1. **DDL (Data Definition Language):** Defines, creates, or alters the physical structure/schema of the database.
* *Commands:* `CREATE`, `ALTER`, `DROP`.


2. **DML (Data Manipulation Language):** Manipulates, updates, or retrieves the actual data records within those schemas.
* *Commands:* `INSERT`, `UPDATE`, `DELETE`, `SELECT`.



### Naming Conventions

* **SQL Keywords:** Write in **UPPERCASE** (e.g., `CREATE TABLE`, `SELECT`, `JOIN`).
* **Table Names:** Write in **lowercase** (e.g., `user`, `comment`).
* **Multi-word/Spaces:** Use **underscores** (e.g., `user_id`, `created_at`).
* **Foreign Keys:** Maintain the exact same name as the referenced primary key in lowercase to keep relations clear.

---

## 5. Database Design & Schema Framework

A clean database design separates data into distinct, normalized tables to prevent **update anomalies** and **redundancy**.

```
         ┌───────────────────────────┐
         │     Conceptual Schema     │ ───► Determines how concepts relate
         └─────────────┬─────────────┘
                       │
                       ▼
         ┌───────────────────────────┐
         │      Logical Schema       │ ───► Maps physical table columns/types
         └─────────────┬─────────────┘
                       │
                       ▼
         ┌───────────────────────────┐
         │      Physical Schema      │ ───► Defines RDBMS engines & server hosting
         └───────────────────────────┘

```

1. **Conceptual Schema:** Translates real-world rules into logical relationships (e.g., mapping how a "User" owns a "Sale").
2. **Logical Schema:** Sets the exact architectural layout of tables, columns, data types, and primary-to-foreign key connections.
3. **Physical Schema:** Implements the design into the chosen engine (e.g., PostgreSQL) and handles physical performance aspects like server hardware, partition strategies, and storage types.

---

## 6. Key Constraints & Integrity

* **Data Integrity:** Guarantees that data is complete, accurate, up to date, and free of broken table links.
* **Keys as Identifiers:** Keys must be **unique**.
* *Best Practice:* Use auto-incrementing integers or UUIDs (e.g., `id`) instead of natural attributes like names or emails which can change or duplicate.


* **The Key Flow Principle:** 
$$\text{Parent Table } \{\text{Primary Key}\} \xrightarrow{\text{Inheritance}} \text{Child Table } \{\text{Foreign Key}\}$$


* A Child table's **Foreign Key (FK)** inherits and points directly back to a Parent table's **Primary Key (PK)**.



---

## 7. Database Relationships

### One-to-One (1:1)

An entity in Table A is associated with exactly one entity in Table B, and vice versa.

* *Example:* Every citizen in the US has exactly one unique Social Security Number.

```
       ┌──────────┐ 1              1 ┌──────────┐
       │ Entity 1 │─────────────────│ Entity 2 │
       └──────────┘                 └──────────┘

```

#### Database Design Pattern

To implement a 1:1 relationship, place the Primary Key of one table into the other table as a Foreign Key, and enforce a **Unique Constraint** on that Foreign Key column.

```
Table: user (Parent)           Table: card (Child)
┌────────────┬───────────┐     ┌────────────┬───────────┬─────────────────┐
│ id (PK)    │ name      │     │ id (PK)    │ card_no   │ user_id (FK, U) │
├────────────┼───────────┤     ├────────────┼───────────┼─────────────────┤
│ 63         │ Ibrahim   │◄──┐ │ 901        │ 4532...   │ 63              │
└────────────┴───────────┘   └─└────────────┴───────────┴─────────────────┘

```

---

### One-to-Many (1:N)

A single record in a Parent table can associate with multiple records in a Child table, but each Child record points to only one Parent record.

* *Example:* One **User** can write multiple **Comments** or own multiple **Cards**.

```
                    ┌───► Comment_1
       ┌──────┐     │
       │ User │─────┼───► Comment_2
       └──────┘     │
                    └───► Comment_3

```

#### Database Design Pattern

Place the Parent table's Primary Key inside the Child table as a Foreign Key (without a unique constraint on the child side, allowing it to repeat).

```
Table: user (Parent)           Table: card (Child)
┌────────────┬───────────┐     ┌────────────┬───────────┬───────────────┐
│ id (PK)    │ name      │     │ id (PK)    │ card_no   │ user_id (FK)  │
├────────────┼───────────┤     ├────────────┼───────────┼───────────────┤
│ 63         │ Ibrahim   │◄──┐ │ 101        │ 5543...   │ 63            │
└────────────┴───────────┘   ├──│ 102        │ 3782...   │ 63            │
                             └──│ 103        │ 4111...   │ 63            │

```

---

### Many-to-Many (M:N) & Junction Tables

Multiple records in Table A can relate to multiple records in Table B.

* *Example:* **Students** can enroll in multiple **Classes**, and those **Classes** contain multiple **Students**.
* *Warning:* **Directly linking M:N tables without an intermediary is a bad database pattern.** It leads to severe redundancy, massive empty spaces, and broken relational structures.

```
[ Student Table ]             [ Class Table ]
   - student_id                  - class_id
        │                           │
        └───────► [ Junction ] ◄────┘
                  - student_id (FK)
                  - class_id (FK)

```

#### Database Design Pattern (The Junction Table)

To properly model an M:N relationship, break it into two **1:N** relationships using an intermediate **Junction Table** (or Associative/Bridge Table) containing the foreign keys of both parents.

```
Table: student (Parent A)
┌──────────────────┬─────────────────┐
│ student_id (PK)  │ name            │
├──────────────────┼─────────────────┤
│ 75               │ John            │
│ 89               │ Jack            │
│ 95               │ Colleen         │
└──────────────────┴─────────────────┘

Table: student_class (Junction Table)
┌──────────────────┬────────────────┐
│ student_id (FK)  │ class_id (FK)  │
├──────────────────┼────────────────┤
│ 75               │ 6              │  ───► John takes Class 6
│ 75               │ 7              │  ───► John takes Class 7
│ 89               │ 6              │  ───► Jack takes Class 6
│ 95               │ 8              │  ───► Colleen takes Class 8
└──────────────────┴────────────────┘

Table: class (Parent B)
┌───────────────┬──────────────────┐
│ class_id (PK) │ class_name       │
├───────────────┼──────────────────┤
│ 6             │ Science          │
│ 7             │ English          │
│ 8             │ Mathematics      │
└───────────────┴──────────────────┘


# Advanced Relational Database Design & Querying

## 1. Physical Architecture, Keys & Constraints

### Key Principles

* **Primary Key (PK):** Every table has only one primary key within itself. It is always **NOT NULL**.
* **Foreign Key (FK):** A table can contain one or more foreign keys referencing other primary keys in other tables.
* **Not Null Foreign Key:** Setting an FK to `NOT NULL` means values are required. Typically, every foreign key can be set to `NOT NULL`, but it can be changed, updated, or manipulated to keep all connection links across all tables intact.
* *Rule:* FKs are generally optional or use `NOT NULL` only when strictly necessary.



#### Structural Mapping Between Keys

```
Table A: launching_table          Table B: Binding_table
┌───────────┬──────────────┐      ┌──────────────┬──────────────┐
│ class_id  │ binding_id   │      │ binding_id   │              │
├───────────┼──────────────┤      ├──────────────┼──────────────┤
│ 64        │ 7            │───┐  │ 7            │              │
│ 38        │ 7            │───┼─►│ 16           │              │
│ 163       │ 7            │───┘  │ 49           │              │
│ 8         │ 14           │─────►│ 3            │              │
└───────────┴──────────────┘      └──────────────┴──────────────┘



### Key Classifications

1. **Simple Key:** The key is composed of **one single column**.
2. **Composite Key:** The key is composed of **two or more columns** (e.g., using natural columns).
3. **Compound Key:** A key composed of two or more columns, but where the table itself contains columns that are keys in their own right (e.g., combining multiple foreign keys to grant key status).

---

### Referential Integrity: Foreign Key Constraints

Constraints govern how actions executed on a **Parent Table** affect the **Child Table**.

```
               [ Keyword A ] ───► Applies to Parent actions: ON DELETE, ON UPDATE
                     │
                     ▼
               [ Keyword B ] ───► The arguments executed on the Child table:
                                  ┌───────────────┐
                                  │    RESTRICT   │
                                  │    CASCADE    │
                                  │   SET NULL    │
                                  └───────────────┘

```

#### Behavioral Rules

* **RESTRICT:** (e.g., `ON DELETE RESTRICT`) If you try to delete a record in the parent table, the engine will throw an error, preventing the parent table record from being deleted if dependent child records exist.
* **CASCADE:** Performs the exact same action done on the parent to the corresponding records in the child (e.g., all-round updates or deletions pass down automatically).
* **SET NULL:** Automatically sets the child table's foreign key cells to `NULL` when the parent record is updated or deleted.
* *Critical Rule:* For `SET NULL` to work, the child table's foreign key columns must **not** have the `NOT NULL` characteristic set.



---

## 2. Entity Relationship Modeling & Normalization

### Structural Frameworks

* **ER Model** (Entity Relationship Model)
* **ERD Model** (Entity Relationship Diagram)
* **EER Model** (Enhanced Entity Relationship Model)
* *Definition:* These models refer to the structural method of drawing out a database architecture.
* *Terminology:* A **Relation** is a table, while a **Relationship** is the physical connection between two tables.



```
[ User Table ]                          [ Comment Table ]
┌────────────────────────┐              ┌────────────────────────┐
│ user_id (PK)           │              │ comment_id (PK)        │
│ username               │──────────────│ user_id (FK)           │
│ password               │              └────────────────────────┘
│ (Indexing Foreign Key) │
└────────────────────────┘

```

### Cardinality and Modality

* **Cardinality:** The relationship type concerning row counts between tables (e.g., a row of one table mapping to one or many rows of another table).
* *Example (1 to Many):* One Cardholder can hold many Cards.


```
[ Card holder ] ───┼───────────◄ [ Card ]

```


* **Modality:** Defines whether a relationship link is optional or mandatory.
* `0` means the foreign key **does not** have the `NOT NULL` constraint (Optional).
* `1` means the foreign key **has** the `NOT NULL` constraint (Required).



```
Modality Notation Mappings:

1. Optional-One (Doesn't have NOT NULL / Required)
   ───┼───────────◯─┼───

2. Mandatory-One (Have NOT NULL / Required)
   ───┼───────────┼─┼───

3. Optional-Many (Doesn't have NOT NULL / Required)
   ───┼───────────◯─◄───

4. Mandatory-Many (Have NOT NULL / Required)
   ───┼───────────┼─◄───

```

### Database Normalization

Normalization involves processing a database step-by-step to eliminate structural conflicts:

1. **1st Normal Form (1NF):** Achieved by making everything atomic (removing any multi-valued attributes or repeating groups).
2. **2nd Normal Form (2NF):** Achieved by removing any partial dependencies.
3. **3rd Normal Form (3NF):** Achieved by removing any transitive dependencies.

---

## 3. Database Indexes & Engines

### Index Classifications

* **Clustered Index:** Organizes the physical data storage blocks sequentially in a way that is highly optimized and easy to look up (e.g., functioning like a phonebook).
* *Note:* The Primary Key automatically acts as a clustered index.


* **Non-Clustered Index:** A separate pointer reference structure that points directly back to the target data addresses.
* **Composite Index:** An index created across two or more columns simultaneously, usually placed on columns heavily targeted for structural searches.

### System Data Types

There are three general kinds of core types:

1. **Date Types:** Consists of `Date time` (stores month/day/year), `Time`, and `Timestamp` (a numerical marker of time showing when something occurred).
2. **Strings:** Contains text subcategories such as `CHAR()`.
3. **Numeric:** Handles integers, decimal systems (Base-10 representations), and floating points/binary fields (Base-2 representations processing `0`s and `1`s).

---

## 4. SQL JOINS & Advanced Queries

Joins extract separated data structural items and assemble them into a user-friendly format.

```
    Table A       Table B
  ┌─────────┐   ┌─────────┐
  │         │   │         │
  │      ┌──┼───┼──┐      │
  │      │  │▒▒▒│  │      │  ◄── Inner Join Returns Intersected Area Only
  │      └──┼───┼──┘      │      (Returns Table C structure)
  └─────────┘   └─────────┘

```

### Inner Joins

* **Definition:** Compares tables and returns only the rows where the join condition matches in both datasets.
* *Note:* IDs used to bridge tables do not necessarily have to be selected or presented in the output; they are often used strictly behind the scenes to merge the primary-to-foreign key layers.

```sql
-- Standard Single Inner Join Syntax
SELECT Firstname, Lastname, amount_paid 
FROM Customer 
INNER JOIN card 
ON Customer.customer_id = card.customer_id;

```

#### Inner Joins Across 3 Tables

To link multiple tables together, daisy-chain multiple `INNER JOIN` statements with corresponding join conditions.

```
┌────────────┐               ┌───────────────┐               ┌─────────────┐
│    user    │ ─────────────►│    Comment    │ ─────────────►│    Video    │
└────────────┘ [Join Cond 1] └───────────────┘ [Join Cond 2] └─────────────┘

```

```sql
-- 3-Table Inner Join Execution Syntax
SELECT username, title, Comment 
FROM User
INNER JOIN Comment 
  ON User.user_id = Comment.user_id          -- First join condition
INNER JOIN Video 
  ON Video.video_id = Comment.video_id;       -- Second join condition

```

---

### Outer Joins

Outer joins extract matching data, alongside unmatched entries from the source tables.

1. **Left Outer Join:** Returns all rows from the left table, plus matching records from the right table.
2. **Right Outer Join:** Returns all rows from the right table, plus matching records from the left table.
3. **Full Outer Join:** Returns all records when there is a match in either the left or right table.

---

### Aliases (`AS`)

Aliases are temporary names given to tables or columns to make queries cleaner and highly readable.

```sql
-- Column Aliasing Syntax
SELECT email AS Contact, first_name AS "First name", Last_name AS "Last name" 
FROM User;

-- Table Aliasing Syntax
SELECT U.user_id 
FROM User AS U;

```

---

### Self Joins

A Self Join is a query variant where **a table is joined to itself**.

```
      ┌───┐
      │   │ ◄─┐
      │   │ ──┘ Loops back to itself
      └───┘
   Table View

```

* *Rule:* To perform a self-join, **you must use aliases** to give the table two distinct query names within the command loop.

```sql
-- Self Join Implementation Syntax Example
SELECT V1.fn, V1.Ln, V1.email AS "Referred by" 
FROM user AS V1
INNER JOIN user AS V2
  ON V1.referred_by = V2.user_id;

```