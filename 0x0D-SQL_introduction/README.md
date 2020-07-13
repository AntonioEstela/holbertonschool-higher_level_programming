# MySQL - Introduction
Project done during **Full Stack Software Engineering studies** at **Holberton School**. It aims to learn about databases, relational databases, subqueries, tables, **MySQL** statements and functions.

## Technologies
* `MySQL 5.7` (version 5.7.8-rc)
* Tested on Ubuntu 14.04 LTS

## Files

All the following files are scripts of MySQL:

| Filename | Description |
| -------- | ----------- |
| [`0-list_databases.sql`](0-list_databases.sql) | Lists all databases of a MySQL server |
| [`1-create_database_if_missing.sql`](1-create_database_if_missing.sql) | Creates the database `hbtn_0c_0` in a MySQL server |
| [`2-remove_database.sql`](2-remove_database.sql) | Deletes the database `hbtn_0c_0` in a MySQL server |
| [`3-list_tables.sql`](3-list_tables.sql) | Lists all the tables of a database in a MySQL server |
| [`4-first_table.sql`](4-first_table.sql) | Creates a table called `first_table` in the current database |
| [`5-full_table.sql`](5-full_table.sql) | Prints the full description of the table `first_table` from the database `hbtn_0c_0`  |
| [`6-list_values.sql`](6-list_values.sql) | Lists all rows of the table `first_table` from the database `hbtn_0c_0` |
| [`7-insert_value.sql`](7-insert_value.sql) | Inserts a new row in the table `first_table` of the database `hbtn_0c_0` |
| [`8-count_89.sql`](8-count_89.sql) | Displays the number of records with `id=89` in the table `first_table` of the database `hbtn_0c_0` |
| [`9-full_creation.sql`](9-full_creation.sql) | Creates a table `second_table` in the database `hbtn_0c_0` |
| [`10-top_score.sql`](10-top_score.sql) | Lists all records of the table `second_table` of the database `hbtn_0c_0` |
| [`11-best_score.sql`](11-best_score.sql) | Lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` |
| [`12-no_cheating.sql`](12-no_cheating.sql) | Updates the score of Bob to `10` in the table `second_table` |
| [`13-change_class.sql`](13-change_class.sql) | Removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` |
| [`14-average.sql`](14-average.sql) | Computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` |
| [`15-groups.sql`](15-groups.sql) | Lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` |
| [`16-no_link.sql`](16-no_link.sql) | Lists all records of the table `second_table` of the database `hbtn_0c_0` |
| [`100-move_to_utf8.sql`](100-move_to_utf8.sql) | Converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`)  |
| [`101-avg_temperatures.sql`](101-avg_temperatures.sql) | Displays the average temperature (Fahrenheit) by city ordered by temperature (descending) |
| [`102-top_city.sql`](102-top_city.sql) | Displays the top 3 of cities temperature during July and August ordered by temperature (descending) |
| [`103-max_state.sql`](103-max_state.sql) | Displays the max temperature of each state (ordered by State name) |

## License
<a href="url"><img src="data:image/png;base64,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" align="middle" width="100" height="60"></a> SQL - Introduction is open source and therefore free to download and use without permission.


## Developed by

### [**Antonio Estela**](https://github.com/AntonioEstela) Full Stack Software Engineer sutdent at [**Holberton School**](https://www.holbertonschool.com/)

- [**Twitter**](https://twitter.com/Antonio__Estela) **|** [**Linkedin**](https://www.linkedin.com/in/antonio-josé-estela-7b2a64156/)