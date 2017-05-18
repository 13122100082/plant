CREATE TABLE IF NOT EXISTS `tb_duty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `title` varchar(128) NOT NULL,
  `content` varchar(1024) NOT NULL,
  `status` tinyint(2) NOT NULL COMMENT '是否完成',
  `is_show` tinyint(2) NOT NULL COMMENT '是否展示',
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

insert into todolist values (null, 1, '滑旱冰', 0, now());
insert into todolist values (null, 2, '学习', 0, now());


CREATE TABLE IF NOT EXISTS `tb_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `status` tinyint(2) NOT NULL COMMENT '是否完成',
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS user (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(64) NOT NULL,
  `role_id` int(11) NOT NULL COMMENT '角色ID',
  `status` tinyint(2) NOT NULL DEFAULT 0 COMMENT '用户状态 0：启用 -1：禁用',
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


insert into user values (null, 'admin', '123456', '15201107323', 'admin@qq.com', 1, 1, now());