create table if not exists `t_admin` (
    `id` int unsigned not null auto_increment,
    `username` varchar(16) not null default '' comment '用户名',
    `phone` varchar(16) not null default '' comment '手机号',
    `role` int unsigned not null default 0 comment '角色ID',
    `time` timestamp not null default current_timestamp comment '注册时间',
    primary key(`id`),
    unique key `idx_username` (`username`),
    key `idx_phone` (`phone`),
    key `idx_role` (`role`),
    key `idx_time` (`time`)
) engine=InnoDB default charset utf8 comment '管理员表';
