import os
import time

backup_path = "C:/xampp/backup"
mysql_path = "E:/xampp/mysql/bin"
database_name = "def"
mysql_username = "root"
mysql_password = ""

if not os.path.exists(backup_path):
    os.mkdir(backup_path)

backup_file = os.path.join(backup_path, f"{database_name}_backup_{time.strftime('%Y%m%d_%H%M%S')}.sql")

command = f"{mysql_path}/mysqldump.exe --user={mysql_username} --password={mysql_password} {database_name} > {backup_file}"
os.system(command)