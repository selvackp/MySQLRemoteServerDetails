# Required libraries for program
import paramiko
from mysql.connector import connect, Error

# Required libraries to connect
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Remote server details to enter
print('Enter the RemoteHost Login Details')
print('----------------------------------')
print('\t')
re_host_IP = input("RemoteHost IP: ")  # If any IP works , pass that to RemoteHost IP
re_host_user = input("RemoteHost Username: ")
re_host_password = input("RemoteHost Password: ")  # If no password for AWS machine just enter to fill the next details
re_host_key_file = input(
    "RemoteHost keyfile name: ")  # If no keys just enter to move next step . # We have tested AWS machine , so its required to pass pem key file to connect .
print('\t')

try:
    # Remote Host Server Connectivity
    client.connect(re_host_IP, username=re_host_user, password=re_host_password, key_filename=re_host_key_file)
    stdin, stdout, stderr = client.exec_command('cat /proc/version')
    print('Remote Server OS and Version')
    print('----------------------------')
    print(stdout.readlines()[0])
    print('\t')
    print('Remote Server Total CPU and Cores')
    print('---------------------------------')
    stdin, stdout, stderr = client.exec_command('lscpu')
    print('Total CPU/Core count for Remote server: ', stdout.readlines()[3])
    print('\t')
    print('Connected Server Total RAM in GB')
    print('--------------------------------')
    stdin, stdout, stderr = client.exec_command('vmstat -s')
    print('Total RAM for Remote server: ', stdout.readlines()[0])
    print('\t')
    print('Connected Server Total Disk Spaces')
    print('----------------------------------')
    stdin, stdout, stderr = client.exec_command('df -h --total')
    print('Total Disk for Remote server: ', stdout.read().decode())
    print('\t')

    # MySQL Basic Details code below
    with connect(
            host=re_host_IP,
            user=input("Enter Remote MySQL Username: "),
            password=input("Enter Remote MySQL Password: "),
    ) as connection:
        print('\t')
        get_database_host = "select @@hostname"
        with connection.cursor() as cursor:
            cursor.execute(get_database_host)
            database_host = cursor.fetchone()
            print("Successfully connected Remote MySQL Server :", database_host[0])
            print('\t')
        print(database_host[0], 'Database Name and Size in MB')
        print('----------------------------------------------')
        get_database_size = "SELECT table_schema AS 'Database', ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)' FROM information_schema.TABLES GROUP BY table_schema;"
        with connection.cursor() as cursor:
            cursor.execute(get_database_size)
            database_size = cursor.fetchall()
            for row in database_size:
                dbname, dbsize = row
                print('{} - {}'.format(dbname, dbsize))
        select_port = 'SELECT @@port'
        with connection.cursor() as cursor:
            cursor.execute(select_port)
            database_port = cursor.fetchone()
            print('\t')
            print('Database Port :')
            print('---------------')
            print(database_host[0], 'Server MySQL Port is :', database_port[0])
        client.close()

except Error as e:
    print(e)
    exit()
