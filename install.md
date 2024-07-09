```

ssh-keygen -t rsa -C "184918308@qq.com"

[root@VM-4-17-centos .ssh]# cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfMJkO51TMw9KOD6KKINhIujcS64zQZ0n9P2TQCgce6q1zllxC0fGwXjTwdvaPvR2eCoQlr2Rbyt3txRjz3w+eATA0IW+dnBhF83UlryoEuPf+5+9Bl1TdDoGEBndQPRV4gWM3CjQYW9OsfJRiyDUa+kNSl0NVcrJEFhSB5i4AItjkUzp3d/LUz21oz8vN7QTy/ZSzz82cIAs/BkLHmYyDJsB5rWH27CUHmVathgkLw9k7IdumXEMSZN5Ife4KLySLMjsr36eS2mTTMeL5U2y1DFQFcAGWu7KA+B0BvtikOBxljIsMDrr8MOSvhYJnGwCE/s9S/+YpJ0BNSBmxlPghm1LfuhCMuN+AtwFELxDjxZ6bV/vLyDD1GtxnXEHhC85s3qCQ1LK3yAlkI/yOipIj2pl/uHG4uEacK0dKtnINyTtMkaciiqBrLX1Ou5P18012K1x9auYnkCQPPRHGg0N0GUFP8f3yFsf3aRqDtBPaFPvwTD5oqzB7XEEVzYAEah8= 184918308@qq.com
[root@VM-4-17-centos .ssh]# ls
id_rsa  id_rsa.pub  known_hosts
[root@VM-4-17-centos .ssh]#



[root@VM-4-17-centos .ssh]# cd /home/cf
[root@VM-4-17-centos cf]# ls
[root@VM-4-17-centos cf]# git clone git@github.com:upempty/flog.git


yum install nodejs

npm install -g cnpm --registry=https://registry.npm.taobao.org

cnpm install

cnpm install --save marked
cnpm run dev

Your application is running here: http://0.0.0.0:8081

http://81.68.228.238:8081
无法访问后设置一条规则 防火墙菜单 允许 tcp和端口8080-8099
http://81.68.228.238:8081/#/


src/main.js
axios.defaults.baseURL = 'http://81.68.228.238:9000/'

--curl https://pyenv.run | bash
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel


[root@VM-4-17-centos flog]# yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
Last metadata expiration check: 0:49:13 ago on Sun 06 Feb 2022 10:15:02 PM CST.
Package zlib-devel-1.2.11-17.el8.x86_64 is already installed.
No match for argument: db4-devel
No match for argument: libpcap-devel
Error: Unable to find a match: db4-devel libpcap-devel
[root@VM-4-17-centos flog]# cat /etc/redhat-release
CentOS Linux release 8.0.1905 (Core)
[root@VM-4-17-centos flog]#

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.bash_profile
echo 'eval "$(pyenv init -)"' >>~/.bash_profile
exec $SHELL -l


[root@VM-4-17-centos ~]# cd ~/.pyenv
[root@VM-4-17-centos .pyenv]# mkdir cache
[root@VM-4-17-centos .pyenv]# cd cache

[root@VM-4-17-centos cache]# wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz
--2022-02-06 23:17:55--  https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz

wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz


/root/.pyenv/cache
[root@VM-4-17-centos cache]# ls
Python-3.8.0.tar.xz


[root@VM-4-17-centos cache]# pyenv install 3.8.0 -v
WARNING: Please make sure you remove any previous custom paths from your /root/.pydistutils.cfg file.
/tmp/python-build.20220206233327.2843768 ~/.pyenv/cac


[root@VM-4-17-centos cache]# python3
Python 3.6.8 (default, Mar 19 2021, 05:13:41)
[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit

pip3 install virtualenv -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

cd /home/cf/flog/
[root@VM-4-17-centos flog]# ls
blog  client.sh  fe  README.md  run.sh
[root@VM-4-17-centos flog]# cd ..
[root@VM-4-17-centos cf]# ls
flog
[root@VM-4-17-centos cf]# mkdir venv
[root@VM-4-17-centos cf]# cd venv
[root@VM-4-17-centos venv]# ls
[root@VM-4-17-centos venv]# python3 -m venv
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR
[root@VM-4-17-centos venv]# python3 -m venv ./
[root@VM-4-17-centos venv]# ls
bin  include  lib  lib64  pyvenv.cfg

chmod +x ./bin/activate

[root@VM-4-17-centos venv]# cd bin
[root@VM-4-17-centos bin]# ls


[root@VM-4-17-centos bin]# source activate
(venv) [root@VM-4-17-centos bin]#
(venv) [root@VM-4-17-centos bin]#



[root@VM-4-17-centos cache]# ls
Python-3.8.0.tar.xz
[root@VM-4-17-centos cache]# pwd
/root/.pyenv/cache
[root@VM-4-17-centos cache]# xz -d Python-3.8.0.tar.xz



Python-3.8.0.tar
[root@VM-4-17-centos cache]# tar -xvf Python-3.8.0.tar

cd Python-3.8.0
./configure prefix=/usr/local/python3
make && make install
export PATH=$PATH:/usr/local/python3/bin/

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

[root@VM-4-17-centos alternatives]# which python3.8
/usr/local/python3/bin/python3.8

update-alternatives --install /usr/bin/python3 python3 /usr/local/python3/bin/python3.8 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
update-alternatives --config python3


[root@VM-4-17-centos alternatives]# update-alternatives --config python3

There are 2 programs which provide 'python3'.

  Selection    Command
-----------------------------------------------
*+ 1           /usr/bin/python3.6
   2           /usr/local/python3/bin/python3.8

Enter to keep the current selection[+], or type selection number: 2
[root@VM-4-17-centos alternatives]#
[root@VM-4-17-centos alternatives]# python3
Python 3.8.0 (default, Feb  6 2022, 23:59:52)
[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
[root@VM-4-17-centos alternatives]# update-alternatives --config python3

There are 2 programs which provide 'python3'.

  Selection    Command
-----------------------------------------------
*  1           /usr/bin/python3.6
 + 2           /usr/local/python3/bin/python3.8

Enter to keep the current selection[+], or type selection number:
[root@VM-4-17-centos alternatives]#
[root@VM-4-17-centos alternatives]#
[root@VM-4-17-centos alternatives]#

python3.8 get-pip.py

python3 -m pip install virtualenv
python3 -m virtualenv venv
[root@VM-4-17-centos venv]# python3 -m virtualenv venv
Traceback (most recent call last):
  File "/usr/local/python3/lib/python3.8/runpy.py", line 183, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/usr/local/python3/lib/python3.8/runpy.py", line 142, in _get_module_details
    return _get_module_details(pkg_main_name, error)
  File "/usr/local/python3/lib/python3.8/runpy.py", line 109, in _get_module_details
    __import__(pkg_name)
  File "/usr/local/python3/lib/python3.8/site-packages/virtualenv/__init__.py", line 3, in <module>
    from .run import cli_run, session_via_cli
  File "/usr/local/python3/lib/python3.8/site-packages/virtualenv/run/__init__.py", line 11, in <module>
    from ..seed.wheels.periodic_update import manual_upgrade
  File "/usr/local/python3/lib/python3.8/site-packages/virtualenv/seed/wheels/__init__.py", line 3, in <module>
    from .acquire import get_wheel, pip_wheel_env_run
  File "/usr/local/python3/lib/python3.8/site-packages/virtualenv/seed/wheels/acquire.py", line 12, in <module>
    from .bundle import from_bundle
  File "/usr/local/python3/lib/python3.8/site-packages/virtualenv/seed/wheels/bundle.py", line 4, in <module>
    from .periodic_update import periodic_update
  File "/usr/local/python3/lib/python3.8/site-packages/virtualenv/seed/wheels/periodic_update.py", line 10, in <module>
    import ssl
  File "/usr/local/python3/lib/python3.8/ssl.py", line 98, in <module>
    import _ssl             # if we can't import it, let the error propagate
ModuleNotFoundError: No module named '_ssl'
[root@VM-4-17-centos venv]#


python3 -m venv .venv to create virtual env. not using virtualenv.


[root@VM-4-17-centos venv]# ls -lart
total 2564
drwxr-xr-x 4 root root    4096 Feb  7 00:01 ..
-rw-r--r-- 1 root root 2609803 Feb  7 00:03 get-pip.py
drwxr-xr-x 5 root root    4096 Feb  7 00:20 .venv
drwxr-xr-x 3 root root    4096 Feb  7 00:20 .
[root@VM-4-17-centos venv]# cd .venv
[root@VM-4-17-centos .venv]# ls
bin  include  lib  lib64  pyvenv.cfg
[root@VM-4-17-centos .venv]# activate bin/activate
-bash: activate: command not found
[root@VM-4-17-centos .venv]# source bin/activate
(.venv) [root@VM-4-17-centos .venv]#


source venv/bin/activate

(.venv) [root@VM-4-17-centos .venv]# python
Python 3.8.0 (default, Feb  6 2022, 23:59:52)
[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
(.venv) [root@VM-4-17-centos .venv]# python3
Python 3.8.0 (default, Feb  6 2022, 23:59:52)
[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(.venv) [root@VM-4-17-centos .venv]# python --version
Python 3.8.0
(.venv) [root@VM-4-17-centos .venv]#


python manage.py runserver 0.0.0.0:9000
Traceback (most recent call last):
  File "manage.py", line 10, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 12, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
(.venv) [root@VM-4-17-centos blog]#
(.venv) [root@VM-4-17-centos blog]#



(.venv) [root@VM-4-17-centos blog]# pip install Django
Looking in indexes: http://mirrors.tencentyun.com/pypi/simple
Collecting Django
  Downloading http


pip3 install django-cors-headers

 pip3 install djangorestframework
Looking in indexes: http://mirrors.tencentyun.com/pypi/simple
Collecting djangorestframework
  Downloading http://mirrors.tencentyun.com/pypi/packages/c8/45/2588c7c5a01a7da6822c6ffbc9a731d498c318a803a29ae780ec635ea41d/djangorestframework-3.13.1-py3-none-any.whl (958kB)
     |████████████████████████████████| 962kB 8.2MB/s
Collecting pytz (from djangorestframework)
  Downloading http://mirrors.tencentyun.com/pypi/packages/d3/e3/d9f046b5d1c94a3aeab15f1f867aa414f8ee9d196fae6865f1d6a0ee1a0b/pytz-2021.3-py2.py3-none-any.whl (503kB)
     |████████████████████████████████| 512kB 1.4MB/s
Requirement already satisfied: django>=2.2 in /home/cf/venv/.venv/lib/python3.8/site-packages (from djangorestframework) (4.0.2)
Requirement already satisfied: backports.zoneinfo; python_version < "3.9" in /home/cf/venv/.venv/lib/python3.8/site-packages (from django>=2.2->djangorestframework) (0.2.1)
Requirement already satisfied: asgiref<4,>=3.4.1 in /home/cf/venv/.venv/lib/python3.8/site-packages (from django>=2.2->djangorestframework) (3.5.0)
Requirement already satisfied: sqlparse>=0.2.2 in /home/cf/venv/.venv/lib/python3.8/site-packages (from django>=2.2->djangorestframework) (0.4.2)
Installing collected packages: pytz, djangorestframework
Successfully installed djangorestframework-3.13.1 pytz-2021.3
WARNING: You are using pip version 19.2.3, however version 22.0.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

--yum install sqlite*


python manage.py runserver 0.0.0.0:9000

ite3/dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ModuleNotFoundError: No module named '_sqlite3'

wget https://www.sqlite.org/2018/sqlite-autoconf-3240000.tar.gz
tar -xvzf sqlite-autoconf-3240000.tar.gz
cd sqlite-autoconf-3240000/
./configure --prefix=/usr/local/sqlite
make -j4&&sudo make install


[root@VM-4-17-centos cache]# ls
Python-3.8.0  Python-3.8.0.tar  sqlite-autoconf-3240000  sqlite-autoconf-3240000.tar.gz
[root@VM-4-17-centos cache]# cd Python-3.8.0/
[root@VM-4-17-centos Python-3.8.0]# pwd
/root/.pyenv/cache/Python-3.8.0


vi setup.py
查找" sqlite_inc_paths" 新增
'/usr/local/sqlite/include'
'/usr/local/sqlite/include/sqlite3'


./configure --enable-loadable-sqlite-extensions

make && sudo make install
find / -name _sqlite*.so


[root@VM-4-17-centos Python-3.8.0]# find / -name _sqlite*.so
/root/.pyenv/cache/Python-3.8.0/build/lib.linux-x86_64-3.8/_sqlite3.cpython-38-x86_64-linux-gnu.so
/usr/lib64/python3.6/lib-dynload/_sqlite3.cpython-36m-x86_64-linux-gnu.so
/usr/local/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so
[root@VM-4-17-centos Python-3.8.0]#


cp /usr/local/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so /usr/local/python3/lib/python3.8/lib-dynload/_sqlite3.so

cp /usr/local/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so /usr/local/python3/lib/python3.8/lib-dynload/_sqlite3.so

      lib64/      pyvenv.cfg
[root@VM-4-17-centos venv]# source .venv/bin/activate
(.venv) [root@VM-4-17-centos venv]# pwd
/home/cf/venv




(.venv) [root@VM-4-17-centos blog]# python manage.py runserver 0.0.0.0:9000
Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
rest.Article: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
rest.FeeItem: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
rest.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

System check identified 3 issues (0 silenced).

You have 1 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth.
Run 'python manage.py migrate' to apply them.
February 07, 2022 - 00:49:23
Django version 4.0.2, using settings 'blog.settings'
Starting development server at http://0.0.0.0:9000/
Quit the server with CONTROL-C.


http://81.68.228.238:8081/9000/

curl -s http://81.68.228.238:9000/decoration/cart/



[root@VM-4-17-centos blog]# source ../../
flog/ venv/
[root@VM-4-17-centos blog]# source ../../venv/.
./     ../    .venv/
[root@VM-4-17-centos blog]# source ../../venv/.venv/
bin/        include/    lib/        lib64/      pyvenv.cfg
[root@VM-4-17-centos blog]# source ../../venv/.venv/bin/activate
(.venv) [root@VM-4-17-centos blog]# python manage.py makemigrations
System check identified some issues:

WARNINGS:
rest.Article: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
rest.FeeItem: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
rest.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Migrations for 'rest':
  rest/migrations/0002_alter_user_first_name.py
    - Alter field first_name on user
(.venv) [root@VM-4-17-centos blog]# python manage.py migrate
System check identified some issues:

WARNINGS:
rest.Article: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
rest.FeeItem: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
rest.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the RestConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, rest, sessions
Running migrations:
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying rest.0002_alter_user_first_name... OK
(.venv) [root@VM-4-17-centos blog]#



python manage.py runserver 0.0.0.0:9000

防火墙加 	9000 和 tcp 允许



Last login: Mon Feb  7 00:52:48 2022 from 112.10.54.78
[root@VM-4-17-centos ~]# curl -s http://81.68.228.238:9000/decoration/cart/
{"data":[{"payid":1,"name":"装修1","fee":100,"paydate":"2021-08-03T16:00:00Z"},{"payid":2,"name":"装修2","fee":200,"paydate":"2021-08-29T13:35:34.995400Z"},{"payid":3,"name":"装修3","fee":100,"paydate":"2021-09-07T15:10:23.325160Z"}],"msg":"query","status":200}[root@VM-4-17-centos ~]#
[root@VM-4-17-centos ~]#
[root@VM-4-17-centos ~]#


Last login: Mon Feb  7 00:57:20 2022 from 112.10.54.78
[root@VM-4-17-centos ~]# cd /home/cf/flog/fe/
[root@VM-4-17-centos fe]# cd frontend/
[root@VM-4-17-centos frontend]# ls
build  config  index.html  node_modules  package.json  README.md  src  static
[root@VM-4-17-centos frontend]# cnpm run dev

> menu@1.0.0 dev /home/cf/flog/fe/frontend
> webpack-dev-server --inline --progress --config build/webpack.dev.conf.js

 17% building modules 64/81 modules 17 active ...rontend/src/components/decoration.vue{ parser: "babylon" } is de 95% emitting                                                                         
 DONE  Compiled successfully in 6855ms                                                                                                                                                      12:58:07 AM

 I  Your application is running here: http://0.0.0.0:8080


http://81.68.228.238:8080/#/decoration

cf/cf

滴滴嗒嗒, 小步向前! cf

小桥流水人家，倚坐门前屋檐下，仰望满天星星，化作一片片柳絮在空中飘荡。



  488  2022-02-08 14:49:40 git add *
  489  2022-02-08 14:49:43 git status
  491  2022-02-08 14:50:41 git config --global user.name 'upempty'
  493  2022-02-08 14:51:14 git config --global user.email '184918308@qq.com'
  494  2022-02-08 14:51:17 git commit -m 'new server update'
  495  2022-02-08 14:51:25 git status
  499  2022-02-08 14:52:16 git branch -a
  # to get from web latest 502  2022-02-08 14:54:25 git pull
  503  2022-02-08 14:54:41 pwd
  504  2022-02-08 14:54:43 ls
  505  2022-02-08 14:54:56 git push origin main




```
