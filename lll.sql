BEGIN TRANSACTION;
CREATE TABLE "st_feedback" (
	`st_id`	integer,
	`course_id`	varchar(10),
	`fb_id1`	integer,
	`fb_id2`	integer,
	`fb_id3`	integer,
	`fb_id4`	integer,
	`fb_id5`	integer,
	`fb_id6`	INTEGER,
	`fb_rating1`	integer,
	`fb_rating2`	integer,
	`fb_rating3`	integer,
	`fb_rating4`	integer,
	`fb_rating5`	integer,
	`fb_rating6`	INTEGER,
	`comments`	varchar(1000),
	`oth_1`	varchar(100),
	`oth_2`	varchar(100),
	`oth_3`	varchar(100),
	`oth_4`	varchar(100),
	`oth_5`	varchar(100),
	PRIMARY KEY(st_id,course_id)
);
INSERT INTO `st_feedback` (st_id,course_id,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,fb_rating1,fb_rating2,fb_rating3,fb_rating4,fb_rating5,fb_rating6,comments,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (3,'2',6,7,8,4,5,NULL,5,5,3,4,5,NULL,'','Object-oriented programming using Java
','Web development using PHP','','','NULL');
INSERT INTO `st_feedback` (st_id,course_id,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,fb_rating1,fb_rating2,fb_rating3,fb_rating4,fb_rating5,fb_rating6,comments,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (4,'2',6,7,8,4,5,'',5,5,5,5,5,NULL,'I think it is perfect!','Object-oriented programming using Java
','Web development using PHP','','Android app development','NULL');
INSERT INTO `st_feedback` (st_id,course_id,fb_id1,fb_id2,fb_id3,fb_id4,fb_id5,fb_id6,fb_rating1,fb_rating2,fb_rating3,fb_rating4,fb_rating5,fb_rating6,comments,oth_1,oth_2,oth_3,oth_4,oth_5) VALUES (5,'2',6,7,8,4,5,NULL,5,5,5,5,5,NULL,'Nothing at all. This course was perfect. I loved it completely.','Object-oriented programming using Java
','Web development using PHP','','Android app development','NULL');
COMMIT;
