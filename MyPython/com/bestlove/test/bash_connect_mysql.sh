#!/bin/bash
echo 正在连接MySQL数据库...
mysql -h 192.168.1.108 -P 3306 -u webnav -pwebnav webnav --default-character-set=utf8  < webnav2.sql <  webnav3.sql > webnav23.log
echo 执行SQL完毕...
echo 关闭MySQL数据库

