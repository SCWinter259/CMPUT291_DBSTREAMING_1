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

You can create a new user account if you don't have one:

![Register](https://github.com/SCWinter259/CMPUT291_DBSTREAMING_1/assets/87864997/737290d1-ac41-4377-91b0-1d0c811a7a8f)

After successful login, you will come to a search movie screen, where you can search for movies using part of their titles or cast members' names. Results with the most keyword matches will appear on top:

![Search](https://github.com/SCWinter259/CMPUT291_DBSTREAMING_1/assets/87864997/faa2bad3-895b-440d-8862-d3adbd096e3a)

You can see more information about the movie:

![MovieInfo](https://github.com/SCWinter259/CMPUT291_DBSTREAMING_1/assets/87864997/0cb85d16-207c-44a6-a2ce-bd0288557f35)

You can choose to follow cast members or watch the movie:

![Follow](https://github.com/SCWinter259/CMPUT291_DBSTREAMING_1/assets/87864997/152d953b-6d5e-4317-a052-55a20bf8360a)
![Watch](https://github.com/SCWinter259/CMPUT291_DBSTREAMING_1/assets/87864997/a173e3bd-3487-453b-bead-74aeb045b5a5)

You can also go back or logout any time. Your session and your watch time will be recorded in the database.

## Coming Soon

- Editor features
- Safe checks for login/register
