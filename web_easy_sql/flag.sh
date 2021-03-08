mysqld_safe &

mysql_ready() {
		mysqladmin ping --socket=/run/mysqld/mysqld.sock --user=root --password=root > /dev/null 2>&1
	}

	while !(mysql_ready)
	do
			echo "waiting for mysql ..."
				sleep 3
			done
if [[ -f /var/www/html/db_flag.sql ]]; then
	    mysql -e "source /var/www/html/db_flag.sql" -uroot -proot
	        rm -f /var/www/html/db_flag.sql
	fi

mysql -e "USE supersqli;INSERT INTO $FLAG_TABLE VALUES('$FLAG');" -uroot -proot

chown -R root:root /var/www/html/
chmod -R 755 /var/www/html/
