"""
Discord Config
"""
# noinspection SpellCheckingInspection
webhook_url = ""


"""
Service List
"""
ServiceList = [
    {
        "name": "nginx",
        "bin": "/www/server/nginx/sbin/nginx",
        "restart_cmd": "/etc/init.d/nginx restart",
        "message": "Nginx寄了， 已重启。"
    },
    {
        "name": "mariadbd",
        "bin": "/www/server/mysql/bin/mariadbd",
        "restart_cmd": "/etc/init.d/mysqld restart",
        "message": "Mariadb寄了， 已重启。"
    },
    {
        "name": "php-fpm",
        "bin": "/www/server/php/74/sbin/php-fpm",
        "restart_cmd": "/etc/init.d/php-fpm-74 restart",
        "message": "php74寄了， 已重启。"
    },
{
        "name": "php-fpm",
        "bin": "/www/server/php/80/sbin/php-fpm",
        "restart_cmd": "/etc/init.d/php-fpm-80 restart",
        "message": "php80寄了， 已重启。"
    },
    {
        "name": "php-fpm",
        "bin": "/www/server/php/81/sbin/php-fpm",
        "restart_cmd": "/etc/init.d/php-fpm-81 restart",
        "message": "php81寄了， 已重启。"
    },
    {
        "name": "dockerd",
        "bin": "/usr/bin/dockerd",
        "restart_cmd": "systemctl restart docker",
        "message": "docker寄了， 已重启。"
    },
    {
        "name": "redis-server",
        "bin": "/www/server/redis/src/redis-server",
        "restart_cmd": "/etc/init.d/redis restart",
        "message": "Redis寄了， 已重启。"
    },
    {
        "name": "mongod",
        "bin": "/www/server/mongodb/bin/mongod",
        "restart_cmd": "/etc/init.d/mongodb restart",
        "message": "MongoDB寄了， 已重启。"
    }
]
