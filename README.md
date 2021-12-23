Pre-conditions: Database named books has been created.

Before create_load.sql loading data to database, you may need to download data from:
https://www.kaggle.com/tranhungnghiep/goodbooks6m

Create table and load data:
Connected to sql server and run three .sql files in the following sequence:
create_load.sql
alter_table.sql
add_index.sql
(Note: all tables have already been created. If you want to create again, you may need to drop the existing tables.)

Test CLI:
Pre-conditions: Installed python3, including pymysql, pandas and their required packages.

In terminal, go to the folder of the code files, and start the program with command:
python main.py


sample test case:

register
testcaseuser
123


create_user
username2
password2

create_group
group_name2

join_group
1

group_members


search
s -tag allon -read F
search
s -name 1984
search
s -read F -authors Stephenie Meyer

read
3

rate
3
4
good

note
1
a note

recommand

quit
