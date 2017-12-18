BEGIN TRANSACTION;
CREATE TABLE `student` (
	`st_id`	integer,
	`st_date_of_joining`	datetime,
	`st_full_name`	varchar(1),
	`st_grade`	varchar(2),
	`st_parent_name`	varchar(1),
	`st_parent_phone`	varchar(10),
	`st_parent_email`	varchar(50),
	`st_phone`	varchar(10),
	`st_email`	varchar(50),
	`st_address_1`	varchar(70),
	`st_address_2`	varchar(70),
	`st_zip`	varchar(6),
	PRIMARY KEY(st_id)
);

INSERT INTO `student` (st_id,st_full_name,st_parent_name,st_parent_phone,st_parent_email,st_phone,st_email) VALUES (1,'Nikhil 
Anand',NULL,NULL,NULL,NULL,NULL);
INSERT INTO `student` (st_id,st_full_name,st_parent_name,st_parent_phone,st_parent_email,st_phone,st_email) VALUES (2,'Vivek Verma',NULL,NULL,NULL,NULL,NULL);
INSERT INTO `student` (st_id,st_full_name,st_parent_name,st_parent_phone,st_parent_email,st_phone,st_email) VALUES (3,'Satvik Tripathi',NULL,NULL,NULL,NULL,NULL);
INSERT INTO `student` (st_id,st_full_name,st_parent_name,st_parent_phone,st_parent_email,st_phone,st_email) VALUES (4,'Manasi Vinay Nair','',NULL,NULL,NULL,NULL);
INSERT INTO `student` (st_id,st_full_name,st_parent_name,st_parent_phone,st_parent_email,st_phone,st_email) VALUES (5,'Anisa Subbiah',NULL,NULL,NULL,NULL,NULL);
INSERT INTO `student` (st_id,st_full_name,st_parent_name,st_parent_phone,st_parent_email,st_phone,st_email) VALUES (7,'Akash Anand',NULL,NULL,NULL,NULL,NULL);
CREATE TABLE 'st_feedback' (
st_id integer,
course_id varchar(10),
fb_id1 integer,
fb_id2 integer,
fb_id3 integer,
fb_id4 integer,
fb_id5 integer,
fb_rating1 integer,
fb_rating2 integer,
fb_rating3 integer,
fb_rating4 integer,
fb_rating5 integer,
comments varchar(1000),
oth_1 varchar(100),
oth_2 varchar(100),
oth_3 varchar(100),
oth_4 varchar(100),
oth_5 varchar(100),
PRIMARY KEY(st_id,course_id)
);
INSERT INTO `st_feedback` (st_id,course_id,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_rating1,fb_rating2,fb_rating3,fb_rating4,fb_rating5,comments,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (3,'2',6,7,8,4,5,5,5,3,4,5,'','Object-oriented programming using Java
','Web development using PHP','','','NULL');
INSERT INTO `st_feedback` (st_id,course_id,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_rating1,fb_rating2,fb_rating3,fb_rating4,fb_rating5,comments,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (4,'2',6,7,8,4,5,5,5,5,5,5,'I think it is perfect!','Object-oriented programming using Java
','Web development using PHP','','Android app development','NULL');
INSERT INTO `st_feedback` (st_id,course_id,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_rating1,fb_rating2,fb_rating3,fb_rating4,fb_rating5,comments,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (5,'2',6,7,8,4,5,5,5,5,5,5,'Nothing at all. This course was perfect. I loved it completely.','Object-oriented programming using Java
','Web development using PHP','','Android app development','NULL');
CREATE TABLE 'feedback' (
fb_id integer,
fb_text  varchar(300),
PRIMARY KEY(fb_id)
);
INSERT INTO `feedback` (fb_id,fb_text) VALUES (1,'Projects are helping me apply each topic to a real situation');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (2,'Problems used in 
the course were appropriately difficult');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (3,'Speed of the course is appropriate');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (4,'I was satisfied with the 
instruction provided');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (5,'I would recommend this course to other students ');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (6,'My confidence in building applications by myself has improved');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (7,'I am comfortable with working on the SQLite DB Management System');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (8,'My comfort with working on PyQt + DB (client server) has improved');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (9,'Projects helped students learn OOPs techniques used in software development');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (10,'Overall course was appropriately difficult');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (11,'I would recommend this course to students for becoming proficient in Python');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (12,'I learnt how Gamemaker works in general');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (13,'I can now design and make simple games using Gamemaker');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (14,'I got introduced into programming - functions/variables/lists/if conditions');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (15,'I enjoyed coming to class and creating programs on Scratch and Gamemaker');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (16,'Projects helped me learn techniques used in software development');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (17,'I was satisfied with the course pace and difficulty level');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (18,'The projects were interesting and not too difficult');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (19,'I was satisfied by the course altogether');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (20,'Exercises we did in class helped reinforce concepts');
INSERT INTO `feedback` (fb_id,fb_text) VALUES (21,'I enjoy coming to class creating new projects using different concepts');
CREATE TABLE "courses" (
	`course_id`	integer,
	`course_name`	varchar(20),
	`fb_id1`	integer,
	`fb_id2`	integer,
	`fb_id3`	integer,
	`fb_id4`	integer,
	`fb_id5`	integer,
	`fb_id6`	INTEGER,
	`oth_1`	varchar(100),
	`oth_2`	varchar(100),
	`oth_3`	varchar(100),
	`oth_4`	varchar(100),
	`oth_5`	varchar(100),
	PRIMARY KEY(course_id)
);
INSERT INTO `courses` (course_id,course_name,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (1,'Python I - Core Python',16,2,3,4,5,NULL,'Object Oriented Programming with Java','Web developing using PHP','Web Design using HTML and CSS','Python II -Creating apps for the laptop','Android app development using Java');
INSERT INTO `courses` (course_id,course_name,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (2,'Python II - Creating apps for the laptop',6,7,8,4,5,NULL,'Object-oriented programming using Java
','Web development using PHP','Web design using HTML/CSS','Android app development',NULL);
INSERT INTO `courses` (course_id,course_name,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (3,'Object Oriented Programming using Java',9,2,10,4,5,NULL,'Core Python','Creating Python GUI applications','Web development using PHP','Web design using HTML and CSS','Android app development using Java');
INSERT INTO `courses` (course_id,course_name,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (4,'Learning to Code',12,14,15,4,5,NULL,'Core Python','Object-oriented programming using Java
','Web design using HTML/CSS','Web development using PHP',NULL);
INSERT INTO `courses` (course_id,course_name,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (5,'Web Design using HTML and CSS',17,18,16,19,5,NULL,'Web development using PHP','Game Design','Core Python','Object-oriented programming using Java
',NULL);
INSERT INTO `courses` (course_id,course_name,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (6,'Scratch',17,20,16,21,5,NULL,'Core Python','Object Oriented Programming with Java','Web Design using HTML and CSS','Web developing using PHP',NULL);
COMMIT;


CREATE TABLE `st_course` (
	`st_id`	INTEGER,
	`c_id`	INTEGER,
	`date`	varchar(10),
	`instructor_name`	varchar(30),
	PRIMARY KEY(st_id,c_id)
);

CREATE TABLE `batch` (
	`batch_id`	INTEGER,
	`course_id`	INTEGER,
	`batch_start_date`	datetime,
	`batch_instructor`	varchar(30),
	`batch_day`	varchar(10
	`batch_time`	varchar(5),
	PRIMARY KEY(batch_id),
        UNIQUE (course_id, batch_start_date)
);

CREATE TABLE `st_batch_link` (
	`st_id`	INTEGER,
	`batch_id`	INTEGER,
	`comments`	VARCHAR(100),
	`active_flag`	varchar(1),
	`fees_due`	INTEGER,
	`fees_paid`	INTEGER,
	`amount_comment`	VARCHAR(100),
	PRIMARY KEY(st_id,batch_id)
);