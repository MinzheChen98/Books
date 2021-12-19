-- Database books
drop table if exists ratings;
drop table if exists to_read;
drop table if exists book_tags;
drop table if exists tags;
drop table if exists books;drop table if exists users;

create table tags (
     tag_id int unsigned NOT NULL primary key, 
     tag_name varchar(32)
     -- Additional Constraints
);
load data infile '/var/lib/mysql-files/tags.csv' ignore into table tags
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines;

create table users (
     user_id int unsigned NOT NULL primary key, 
     user_name varchar(32) NOT NULL,
     admin decimal(1) NOT NULL,
     password varchar(128) NOT NULL
     -- Additional Constraints
);


create table books(
     book_id int unsigned NOT NULL primary key,
     goodreads_book_id int unsigned,
     best_book_id int unsigned,
     work_id int unsigned,
     books_count int unsigned,
     isbn varchar(16),
     isbn13 char(13),
     authors varchar(64),
     original_publication_year decimal(4),
     original_title varchar(160),
     title varchar(160),
     language_code char(16),
     average_rating float,
     ratings_count int,
     work_ratings_count int,
     work_text_reviews_count int,
     ratings_1 int,
     ratings_2 int,
     ratings_3 int,
     ratings_4 int,
     ratings_5 int,
     image_url varchar(512),
     small_image_url varchar(512)
	-- Additional Constraints
);
load data infile '/var/lib/mysql-files/books.csv' ignore into table books
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines;

create table book_tags(
     goodreads_book_id int unsigned,
     tag_id int unsigned,
     count int,
	-- Additional Constraints
     CONSTRAINT FK_book_tag_id FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
load data infile '/var/lib/mysql-files/book_tags.csv' ignore into table book_tags
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines;


create table to_read(
     user_id int unsigned NOT NULL,
     book_id int unsigned NOT NULL,
	-- Additional Constraints
     constraint PK_read primary key (user_id, book_id)
);
load data infile '/var/lib/mysql-files/to_read.csv' ignore into table to_read
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines;
alter table to_read add constraint FK_read_user_id foreign key(user_id) REFERENCES users(user_id);
alter table to_read add constraint FK_read_book_id foreign key(book_id) REFERENCES books(book_id);


create table ratings(
     user_id int unsigned NOT NULL,
     book_id int unsigned NOT NULL,
     rating decimal(1),
		 -- Additional Constraints
     constraint PK_rating primary key (user_id, book_id)
);
load data infile '/var/lib/mysql-files/ratings.csv' ignore into table ratings
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines;
alter table ratings add constraint FK_rating_user_id foreign key(user_id) REFERENCES users(user_id);
alter table ratings add constraint FK_rating_book_id foreign key(book_id) REFERENCES books(book_id);
