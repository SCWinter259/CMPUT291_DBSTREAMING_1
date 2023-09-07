# CMPUT291_DBSTREAMING_1

**DB STREAMING 1** is a text-based movie streaming service, created using **Python** for logic, **SQLite** for database, and **Streamlit** for UI.

## Create database

The project tables and project demo data are given in `prj-tables.sql` and `project1_data.sql`. To create the database, please have sqlite3 installed and use the following BASH commands:

`touch [database name]`

`sqlite3 [database name] < prj-tables.sql`

`sqlite3 [database name] < project1_data.sql`

If you are on a Windows machine and have Git BASH installed, you can `cd` into the `data` folder and run the `createDB.sh` script.

## Using the app

To run the app, please have Streamlit installed and run `py -m streamlit run main.py`. You will first be greeted with a login screen:

![Login](https://github.com/SCWinter259/CMPUT291_DBSTREAMING_1/assets/87864997/c946c8eb-c5c4-4122-b8d2-67ddf4a2ce0d)
