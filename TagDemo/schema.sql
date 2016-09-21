drop table if exists tags;
create table tags (
        id integer primary key autoincrement,
        tag_id text not null,
        lastupdate datetime null
);

drop table if exists points;
create table points (
        id integer primary key autoincrement,
        tag_id text not null,
        send_time datetime null,
        recv_time datetime not null,
        status text null
        lat real not null,
        lon real not null,
	results text not null
);

