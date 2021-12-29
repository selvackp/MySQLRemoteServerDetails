# MySQLRemoteServerDetails
MySQLRemoteServerDetails

As per the requirements basic details are listed in this script

	1. OS Version
	2. Find Physical host / VMWare
	3. MySQL Port
	4. Total RAM / Total CPU and Cores
	5. How many Database and Size ?
	6. Disk Space
 
Note : 

	1.We have used AWS EC2 Instance to test the code , if you are using VMWare or OnPrem Host Just ignore key_filename 
	2.re_host_password - If no password for AWS machine just enter to fill the next details
	3.re_host_key_file - If no keys just enter to move next step . We have tested AWS machine , so its required to pass pem key file to connect
	4.re_host_IP - If any IP works , pass that to RemoteHost IP
