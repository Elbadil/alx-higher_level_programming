-- script that creates a table second_table in the database hbtn_0c_0 in my MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name VARCHAR(256),
    score int
);
INSERT INTO second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 12),
    (3, 'Bab', 14),
    (4, 'George', 8);