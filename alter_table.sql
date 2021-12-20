drop table if exists rating_statistics;

create table rating_statistics(
    book_id int unsigned NOT NULL primary key,
    average_rating float,
    ratings_count int,
    ratings_1 int,
    ratings_2 int,
    ratings_3 int,
    ratings_4 int,
    ratings_5 int
	-- Additional Constraints
);

insert into rating_statistics (
    book_id, 
    average_rating,
    ratings_count,
    ratings_1,
    ratings_2,
    ratings_3,
    ratings_4,
    ratings_5
) select 
    book_id, 
    average_rating,
    ratings_count,
    ratings_1,
    ratings_2,
    ratings_3,
    ratings_4,
    ratings_5
from books;

-- alter table books drop average_rating;
-- alter table books drop ratings_count;
-- alter table books drop ratings_1;-
-- alter table books drop ratings_2;
-- alter table books drop ratings_3;
-- alter table books drop ratings_4;
-- alter table books drop ratings_5;
