**yum update & python3 install**

```
[ec2-user@ip-172-31-49-54 ~]$ sudo yum update

[ec2-user@ip-172-31-49-54 ~]$ sudo ln -s /usr/bin/python3 /usr/bin/python
[ec2-user@ip-172-31-49-54 ~]$ python -V
Python 3.6.8
```

**Stop Firewalld**

```
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo service firewalld stop
Redirecting to /bin/systemctl stop firewalld.service
```

**Create venv and project directory**

```
ec2-user@ip-172-31-49-54:/home/ec2-user> mkdir venv
ec2-user@ip-172-31-49-54:/home/ec2-user> cd venv/
ec2-user@ip-172-31-49-54:/home/ec2-user/venv> python -m venv myproject
ec2-user@ip-172-31-49-54:/home/ec2-user/venv> cd myproject/
ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> ls
bin  include  lib  lib64  pyvenv.cfg
ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> source bin/activate
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject>

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> pip install Flask
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> pip install --upgrade pip


```

**Create first flask app**

```
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> vi setenv.sh
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> cat setenv.sh
export FLASK_APP=pybo
export FLASK_ENV=dev
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> source setenv.sh
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> env|grep FLASK
FLASK_APP=pybo
FLASK_ENV=dev

```

**Run Flask App and Test**

```
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> flask run --host='0.0.0.0'
 * Serving Flask app 'pybo' (lazy loading)
 * Environment: dev
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.31.49.54:5000/ (Press CTRL+C to quit)

ec2-user@ip-172-31-49-54:/home/ec2-user> curl localhost:5000
Hello, Pybo!

```

**Install ORM Library**

```
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> pip install Flask-Migrate


```

**Install Oracle client library**

```
ec2-user@ip-172-31-49-54:/home/ec2-user> wget https://download.oracle.com/otn_software/linux/instantclient/211000/instantclient-basic-linux.x64-21.1.0.0.0.zip

ec2-user@ip-172-31-49-54:/home/ec2-user> unzip instantclient-basic-linux.x64-21.1.0.0.0.zip

ec2-user@ip-172-31-49-54:/home/ec2-user> echo "export LD_LIBRARY_PATH=/home/ec2-user/instantclient_21_1:$LD_LIBRARY_PATH" >> .bash_profile

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> pip install --upgrade cx_Oracle

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> source ~/.bash_profile
ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> env|grep LD
LD_LIBRARY_PATH=/home/ec2-user/instantclient_21_1:
OLDPWD=/home/ec2-user
ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> source bin/activate

```

**Install Oracle XE**

```
ec2-user@ip-172-31-49-54:/home/ec2-user> wget https://download.oracle.com/otn-pub/otn_software/db-express/oracle-database-xe-18c-1.0-1.x86_64.rpm

curl -o compat-libcap1-1.10-7.el7.x86_64.rpm http://mirror.centos.org/centos/7/os/x86_64/Packages/compat-libcap1-1.10-7.el7.x86_64.rpm

curl -o compat-libstdc++-33-3.2.3-72.el7.x86_64.rpm http://mirror.centos.org/centos/7/os/x86_64/Packages/compat-libstdc++-33-3.2.3-72.el7.x86_64.rpm

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum -y localinstall compat-libcap1-1.10-7.el7.x86_64.rpm

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum -y localinstall compat-libstdc++-33-3.2.3-72.el7.x86_64.rpm

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum -y localinstall oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum -y localinstall oracle-database-xe-18c-1.0-1.x86_64.rpm

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum -y install libnsl

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo mkdir -p /oracle/oradata
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo chown -R oracle:oinstall /oracle

ec2-user@ip-172-31-49-54:/home/ec2-user> vi /etc/sysconfig/oracle-xe-18c.conf
ec2-user@ip-172-31-49-54:/home/ec2-user> cat /etc/sysconfig/oracle-xe-18c.conf
#This is a configuration file to setup the Oracle Database.
#It is used when running '/etc/init.d/oracle-xe-18c configure'.

# LISTENER PORT used Database listener, Leave empty for automatic port assignment
LISTENER_PORT=1521

# EM_EXPRESS_PORT Oracle EM Express URL port
EM_EXPRESS_PORT=5500

# Character set of the database
CHARSET=AL32UTF8

# Database file directory
# If not specified, database files are stored under Oracle base/oradata
DBFILE_DEST=/oracle/oradata

# SKIP Validations, memory, space
SKIP_VALIDATIONS=false


ec2-user@ip-172-31-49-54:/home/ec2-user> sudo /etc/init.d/oracle-xe-18c configure
Specify a password to be used for database accounts. Oracle recommends that the password entered should be at least 8 characters in length, contain at least 1 uppercase character, 1 lower case character and 1 digit [0-9]. Note that the same password will be used for SYS, SYSTEM and PDBADMIN accounts:
Confirm the password:
Configuring Oracle Listener.
Listener configuration succeeded.
Configuring Oracle Database XE.
Enter SYS user password:
**********
Enter SYSTEM user password:
*******
Enter PDBADMIN User Password:
************
Prepare for db operation
7% complete
Copying database files
File "/etc/oratab" is not accessible.
29% complete
Creating and starting Oracle instance
30% complete
31% complete
34% complete
38% complete
41% complete
43% complete
Completing Database Creation
47% complete
50% complete
Creating Pluggable Databases
54% complete
71% complete
Executing Post Configuration Actions
93% complete
Running Custom Scripts
100% complete
Database creation complete. For details check the logfiles at:
 /opt/oracle/cfgtoollogs/dbca/XE.
Database Information:
Global Database Name:XE
System Identifier(SID):XE
Look at the log file "/opt/oracle/cfgtoollogs/dbca/XE/XE.log" for further details.

Connect to Oracle Database using one of the connect strings:
     Pluggable database: ip-172-31-49-54.ap-northeast-2.compute.internal/XEPDB1
     Multitenant container database: ip-172-31-49-54.ap-northeast-2.compute.internal
Use https://localhost:5500/em to access Oracle Enterprise Manager for Oracle Database XE
```

**oracle user**

```

oracle@ip-172-31-49-54:/home/oracle> cat .bash_profile
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

export ORACLE_HOME=/opt/oracle/product/18c/dbhomeXE
export ORACLE_SID=XE
export PATH=$ORACLE_HOME/bin:$PATH
export PS1='\u@\h:$PWD> '

alias ss='sqlplus / as sysdba'
alias cdo='cd $ORACLE_HOME'
alias cdn='cd $ORACLE_HOME/network/admin'

stty erase

set -o vi

oracle@ip-172-31-49-54:/home/oracle> . .bash_profile
oracle@ip-172-31-49-54:/home/oracle> ss

oracle@ip-172-31-49-54:/home/oracle> lsnrctl status

LSNRCTL for Linux: Version 18.0.0.0.0 - Production on 22-JUL-2021 06:48:50

Copyright (c) 1991, 2018, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=ip-172-31-49-54.ap-northeast-2.compute.internal)(PORT=1521)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 18.0.0.0.0 - Production
Start Date                22-JUL-2021 06:25:40
Uptime                    0 days 0 hr. 23 min. 10 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Default Service           XE
Listener Parameter File   /opt/oracle/product/18c/dbhomeXE/network/admin/listener.ora
Listener Log File         /opt/oracle/diag/tnslsnr/ip-172-31-49-54/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=ip-172-31-49-54.ap-northeast-2.compute.internal)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=127.0.0.1)(PORT=5500))(Security=(my_wallet_directory=/opt/oracle/admin/XE/xdb_wallet))(Presentation=HTTP)(Session=RAW))
Services Summary...
Service "XE" has 1 instance(s).
  Instance "XE", status READY, has 1 handler(s) for this service...
Service "XEXDB" has 1 instance(s).
  Instance "XE", status READY, has 1 handler(s) for this service...
Service "c7b175ead6d282b0e05336311fac1ed0" has 1 instance(s).
  Instance "XE", status READY, has 1 handler(s) for this service...
Service "xepdb1" has 1 instance(s).
  Instance "XE", status READY, has 1 handler(s) for this service...
The command completed successfully

oracle@ip-172-31-49-54:/opt/oracle/product/18c/dbhomeXE/network/admin> cat tnsnames.ora
# tnsnames.ora Network Configuration File: /opt/oracle/product/18c/dbhomeXE/network/admin/tnsnames.ora
# Generated by Oracle configuration tools.

XE =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = ip-172-31-49-54.ap-northeast-2.compute.internal)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = XE)
    )
  )

xepdb =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = ip-172-31-49-54.ap-northeast-2.compute.internal)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = xepdb1)
    )
  )

LISTENER_XE =
  (ADDRESS = (PROTOCOL = TCP)(HOST = ip-172-31-49-54.ap-northeast-2.compute.internal)(PORT = 1521))

oracle@ip-172-31-49-54:/opt/oracle/product/18c/dbhomeXE/network/admin> sqlplus system@xepdb

SQL> create user oshop identified by oshop default tablespace users temporary tablespace temp quota unlimited on users;

User created.

SQL> grant connect,resource to oshop;

Grant succeeded.

```

**Gnome Install**

```
https://devopscube.com/how-to-setup-gui-for-amazon-ec2-rhel-7-instance/

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum -y update
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum groupinstall -y "Server with GUI"
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo systemctl set-default graphical.target
Removed /etc/systemd/system/default.target.
Created symlink /etc/systemd/system/default.target → /usr/lib/systemd/system/graphical.target.
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo systemctl default
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm
Retrieving http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo yum install -y xrdp tigervnc-server

ec2-user@ip-172-31-49-54:/home/ec2-user> chcon --type=bin_t /usr/sbin/xrdp
ec2-user@ip-172-31-49-54:/home/ec2-user> chcon --type=bin_t /usr/sbin/xrdp-sesman
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo systemctl start xrdp
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo systemctl enable xrdp
Created symlink /etc/systemd/system/multi-user.target.wants/xrdp.service → /usr/lib/systemd/system/xrdp.service.
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo firewall-cmd --permanent --add-port=3389/tcp
success
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo firewall-cmd --reload
success
ec2-user@ip-172-31-49-54:/home/ec2-user> sudo passwd ec2-user
Changing password for user ec2-user.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.

ec2-user@ip-172-31-49-54:/home/ec2-user> sudo su
root@ip-172-31-49-54:/home/ec2-user> passwd
root@ip-172-31-49-54:/home/ec2-user> passwd
Changing password for user root.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.

Using RDP


```

**download demo app**

```
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> wget https://cdn.app.compendium.com/uploads/user/e7c690e8-6ff9-102a-ac6d-e4aebca50425/c352d68a-546c-4af7-94d8-04e1e09e802c/File/5b7db3474953c30fc46bd272f295fc68/demo.zip

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> unzip demo.zip

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> vi setenv.sh
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> cat setenv.sh
export FLASK_APP=pybo
export FLASK_ENV=dev
export PYTHON_USERNAME=oshop
export PYTHON_PASSWORD=oshop
export PYTHON_CONNECTSTRING=172.31.49.54/xepdb1
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> source setenv.sh
(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> env|grep PYTHON
PYTHON_PASSWORD=oshop
PYTHON_CONNECTSTRING=172.31.49.54/xepdb1
PYTHON_USERNAME=oshop

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> diff demo.py ~/demo.py.bak
29,33c29
<     print(sys.platform)
<     cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/instantclient_21_1")
< elif sys.platform.startswith("linux"):
<     cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/instantclient_21_1")
<     print("LINUX" + sys.platform)
---
>     cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/instantclient_19_3")
188,189c184
<     #app.run(port=int(os.environ.get('PORT', '8080')))
<     app.run(host='0.0.0.0',port=int(os.environ.get('PORT', '8080')))
---
>     app.run(port=int(os.environ.get('PORT', '8080')))



```

**Demo Test**

```

(myproject) ec2-user@ip-172-31-49-54:/home/ec2-user/venv/myproject> flask run --host=0.0.0.0
 * Serving Flask app 'demo' (lazy loading)
 * Environment: dev
 * Debug mode: off
LINUXlinux
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.31.49.54:5000/ (Press CTRL+C to quit)

kiwony@kiwonymac.com:/Users/kiwony> curl http://15.165.34.91:5000/user/1
chris%

SQL> select * from tab;

TNAME                          TABTYPE        CLUSTERID
------------------------------ ------------- ----------
DEMO                           TABLE

SQL> select * from demo;

        ID USERNAME
---------- ----------------------------------------
         1 chris

kiwony@kiwonymac.com:/Users/kiwony> curl http://15.165.34.91:5000/post/john
Inserted john with id 2%
kiwony@kiwonymac.com:/Users/kiwony> curl http://15.165.34.91:5000/user/2
john%

SQL> /

        ID USERNAME
---------- ----------------------------------------
         1 chris
         2 john

```
