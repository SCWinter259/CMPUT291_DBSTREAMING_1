-- Data prepared by Casper Nguyen
-- CCID: hoangtru

PRAGMA foreign_keys = ON;

insert into customers values ('c100', 'Youssef Amer', 'ANGRY');
insert into customers values ('c200', 'Daniel Akanmu', 'Dak');
insert into customers values ('c300', 'Casper Nguyen', 'SCWinter');

insert into editors values ('e100', 'RD291');
insert into editors values ('e200', 'smurfguy');
insert into editors values ('e300', 'chocolate');

insert into moviePeople values ('p001', 'Robert Downey Jr', 1965);
insert into moviePeople values ('p002', 'Terrence Howard', 1969);
insert into moviePeople values ('p003', 'Gwyneth Paltrow', 1972);
insert into moviePeople values ('p004', 'Don Cheadle', 1964);
insert into moviePeople values ('p005', 'Scarlett Johansson', 1984);
insert into moviePeople values ('p006', 'Samuel L. Jackson', 1948);
insert into moviePeople values ('p007', 'Jon Favreau', 1966);
insert into moviePeople values ('p008', 'Chris Evans', 1981);
insert into moviePeople values ('p009', 'Hayley Atwell', 1982);
insert into moviePeople values ('p010', 'Sebastian Stan', 1982);
insert into moviePeople values ('p011', 'Dominic Cooper', 1978);
insert into moviePeople values ('p012', 'Anthony Mackie', 1978);
insert into moviePeople values ('p013', 'Jeremy Renner', 1971);
insert into moviePeople values ('p014', 'Chadwick Boseman', 1976);
insert into moviePeople values ('p015', 'Paul Bettany', 1971);
insert into moviePeople values ('p016', 'Elizabeth Olsen', 1989);
insert into moviePeople values ('p017', 'Paul Rudd', 1969);
insert into moviePeople values ('p018', 'Tom Holland', 1996);
insert into moviePeople values ('p019', 'Mark Ruffalo', 1967);
insert into moviePeople values ('p020', 'Chris Hemsworth', 1983);
insert into moviePeople values ('p021', 'Tom Hiddleston', 1981);
insert into moviePeople values ('p022', 'Aaron Taylor-Johnson', 1990);

insert into movies values (10, 'Iron Man', 2008, 126);
insert into casts values (10, 'p001', 'Tony Stark');
insert into casts values (10, 'p002', 'James "Rhodey" Rhodes');
insert into casts values (10, 'p003', 'Virginia "Pepper" Potts');

insert into movies values (20, 'Iron Man 2', 2010, 125);
insert into casts values (20, 'p001', 'Tony Stark');
insert into casts values (20, 'p004', 'James "Rhodey" Rhodes');
insert into casts values (20, 'p003', 'Virginia "Pepper" Potts');
insert into casts values (20, 'p005', 'Natasha Romanoff');
insert into casts values (20, 'p006', 'Nick Fury');

insert into movies values (30, 'Iron Man 3', 2013, 131);
insert into casts values (30, 'p001', 'Tony Stark');
insert into casts values (30, 'p004', 'James "Rhodey" Rhodes');
insert into casts values (30, 'p003', 'Virginia "Pepper" Potts');
insert into casts values (30, 'p007', 'Harold "Happy" Hogan');

insert into movies values (40, 'Captain America: The First Avenger', 2011, 124);
insert into casts values (40, 'p008', 'Steve Rogers');
insert into casts values (40, 'p009', 'Peggy Carter');
insert into casts values (40, 'p010', 'James "Bucky" Barnes');
insert into casts values (40, 'p011', 'Howard Stark');

insert into movies values (50, 'Captain America: The Winter Soldier', 2014, 136);
insert into casts values (50, 'p008', 'Steve Rogers');
insert into casts values (50, 'p005', 'Natasha Romanoff');
insert into casts values (50, 'p010', 'James "Bucky" Barnes');
insert into casts values (50, 'p012', 'Sam Wilson');
insert into casts values (50, 'p009', 'Peggy Carter');
insert into casts values (50, 'p006', 'Nick Fury');

insert into movies values (60, 'Captain America: Civil War', 2016, 147);
insert into casts values (60, 'p008', 'Steve Rogers');
insert into casts values (60, 'p001', 'Tony Stark');
insert into casts values (60, 'p005', 'Natasha Romanoff');
insert into casts values (60, 'p010', 'James "Bucky" Barnes');
insert into casts values (60, 'p012', 'Sam Wilson');
insert into casts values (60, 'p004', 'James "Rhodey" Rhodes');
insert into casts values (60, 'p013', 'Hawkeye');
insert into casts values (60, 'p014', 'Black Panther');
insert into casts values (60, 'p015', 'Vision');
insert into casts values (60, 'p016', 'Wanda Maximoff');
insert into casts values (60, 'p017', 'Ant Man');
insert into casts values (60, 'p018', 'Peter Parker');

insert into movies values (70, 'The Avengers', 2012, 143);
insert into casts values (70, 'p001', 'Tony Stark');
insert into casts values (70, 'p008', 'Steve Rogers');
insert into casts values (70, 'p019', 'Bruce Banner');
insert into casts values (70, 'p020', 'Thor');
insert into casts values (70, 'p005', 'Natasha Romanoff');
insert into casts values (70, 'p013', 'Hawkeye');
insert into casts values (70, 'p021', 'Loki');
insert into casts values (70, 'p006', 'Nick Fury');

insert into movies values (80, 'Avengers: Age of Ultron', 2015, 141);
insert into casts values (80, 'p001', 'Tony Stark');
insert into casts values (80, 'p020', 'Thor');
insert into casts values (80, 'p019', 'Bruce Banner');
insert into casts values (80, 'p008', 'Steve Rogers');
insert into casts values (80, 'p005', 'Natasha Romanoff');
insert into casts values (80, 'p013', 'Hawkeye');
insert into casts values (80, 'p004', 'James "Rhodey" Rhodes');
insert into casts values (80, 'p016', 'Wanda Maximoff');
insert into casts values (80, 'p022', 'Pietro Maximoff');
insert into casts values (80, 'p015', 'Vision');
insert into casts values (80, 'p012', 'Sam Wilson');
insert into casts values (80, 'p009', 'Peggy Carter');
insert into casts values (80, 'p006', 'Nick Fury');

insert into recommendations values (10, 20, 0.8);
insert into recommendations values (10, 30, 0.5);
insert into recommendations values (20, 30, 0.5);
insert into recommendations values (20, 40, 0.9);
insert into recommendations values (30, 50, 0.6);
insert into recommendations values (30, 80, 0.7);
insert into recommendations values (40, 50, 0.6);
insert into recommendations values (40, 30, 0.5);
insert into recommendations values (50, 80, 0.7);
insert into recommendations values (50, 30, 0.5);
insert into recommendations values (60, 30, 0.5);
insert into recommendations values (60, 40, 0.9);
insert into recommendations values (70, 80, 0.7);
insert into recommendations values (70, 50, 0.6);
insert into recommendations values (80, 10, 0.9);
insert into recommendations values (80, 40, 0.9);

insert into sessions values (1, 'c100', '2022-01-07', 160);
insert into sessions values (2, 'c100', '2021-06-26', 240);
insert into sessions values (3, 'c100', '2021-02-10', 180);
insert into sessions values (4, 'c200', '2022-01-22', 170);
insert into sessions values (5, 'c200', '2021-09-06', 240);
insert into sessions values (6, 'c200', '2021-05-15', 250);
insert into sessions values (7, 'c300', '2021-09-24', 230);
insert into sessions values (8, 'c300', '2021-08-09', 50);
insert into sessions values (9, 'c300', '2021-04-04', 250);
insert into sessions values (10, 'c100', '2021-10-18', 320);
insert into sessions values (11, 'c100', '2021-08-16', 240);
insert into sessions values (12, 'c100', '2021-08-23', 80);
insert into sessions values (13, 'c200', '2021-06-17', 310);
insert into sessions values (14, 'c200', '2021-03-04', 100);
insert into sessions values (15, 'c200', '2021-05-07', 240);
insert into sessions values (16, 'c300', '2021-04-22', 170);
insert into sessions values (17, 'c300', '2021-07-12', 320);
insert into sessions values (18, 'c300', '2021-07-29', 180);

insert into watch values (1, 'c100', 30, 25);
insert into watch values (1, 'c100', 10, 80);
insert into watch values (2, 'c100', 20, 86);
insert into watch values (3, 'c100', 60, 95);
insert into watch values (10, 'c100', 30, 60);
insert into watch values (11, 'c100', 40, 57);
insert into watch values (12, 'c100', 50, 25);
insert into watch values (4, 'c200', 10, 75);
insert into watch values (4, 'c200', 40, 100);
insert into watch values (5, 'c200', 20, 65);
insert into watch values (6, 'c200', 80, 75);
insert into watch values (13, 'c200', 10, 30);
insert into watch values (14, 'c200', 20, 25);
insert into watch values (15, 'c200', 60, 95);
insert into watch values (7, 'c300', 10, 90);
insert into watch values (8, 'c300', 40, 95);
insert into watch values (9, 'c300', 30, 45);
insert into watch values (9, 'c300', 80, 55);
insert into watch values (16, 'c300', 80, 30);
insert into watch values (17, 'c300', 20, 92);
insert into watch values (18, 'c300', 70, 94);

insert into follows values ('c100', 'p001');
insert into follows values ('c100', 'p002');
insert into follows values ('c100', 'p003');
insert into follows values ('c200', 'p022');
insert into follows values ('c200', 'p021');
insert into follows values ('c200', 'p020');
insert into follows values ('c300', 'p001');
insert into follows values ('c300', 'p005');
insert into follows values ('c300', 'p006');
insert into follows values ('c300', 'p008');
insert into follows values ('c300', 'p009');
insert into follows values ('c300', 'p016');
insert into follows values ('c300', 'p018');
insert into follows values ('c300', 'p019');
insert into follows values ('c300', 'p020');
insert into follows values ('c300', 'p021');