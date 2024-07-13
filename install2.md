```

ssh-keygen -t rsa -C "184918308@qq.com"
cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfMJkO51TMw9KOD6KKINhIujcS64zQZ0n9P2TQCgce6q1zllxC0fGwXjTwdvaPvR2eCoQlr2Rbyt3txRjz3w+eATA0IW+dnBhF83UlryoEuPf+5+9Bl1TdDoGEBndQPRV4gWM3CjQYW9OsfJRiyDUa+kNSl0NVcrJEFhSB5i4AItjkUzp3d/LUz21oz8vN7QTy/ZSzz82cIAs/BkLHmYyDJsB5rWH27CUHmVathgkLw9k7IdumXEMSZN5Ife4KLySLMjsr36eS2mTTMeL5U2y1DFQFcAGWu7KA+B0BvtikOBxljIsMDrr8MOSvhYJnGwCE/s9S/+YpJ0BNSBmxlPghm1LfuhCMuN+AtwFELxDjxZ6bV/vLyDD1GtxnXEHhC85s3qCQ1LK3yAlkI/yOipIj2pl/uHG4uEacK0dKtnINyTtMkaciiqBrLX1Ou5P18012K1x9auYnkCQPPRHGg0N0GUFP8f3yFsf3aRqDtBPaFPvwTD5oqzB7XEEVzYAEah8= 184918308@qq.com

git clone git@github.com:upempty/flog.git

yum install nodejs

cd /myhome/programming/git/flog/fe/frontend
-- npm cache clean --force
npm config set registry https://registry.npmmirror.com
npm install
npm run dev (in frontend folder)

Your application is running here: http://0.0.0.0:8081

http://121.43.133.208:8080
无法访问后设置一条规则 防火墙菜单 允许 tcp和端口8080-8099

src/main.js
axios.defaults.baseURL = 'http://121.43.133.208:9000/'

pip3 install Django
pip3 install django-cors-headers
pip3 install djangorestframework

cd /myhome/programming/git/flog/blog
python manage.py migrate
python manage.py runserver 0.0.0.0:9000


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

```

[root@VM-16-14-centos frontend]# uname -r
5.14.0-474.el9.x86_64
[root@VM-16-14-centos frontend]#


vi src/main.js
//axios.defaults.baseURL = 'http://121.43.133.208:9000/'
axios.defaults.baseURL = 'http://118.25.176.102:9000/'

[root@VM-16-14-centos frontend]# pip --version
pip 21.3.1 from /usr/lib/python3.9/site-packages/pip (python 3.9)
[root@VM-16-14-centos frontend]# pip3 --version
pip 21.3.1 from /usr/lib/python3.9/site-packages/pip (python 3.9)
[root@VM-16-14-centos frontend]#


pip install Django
pip install django-cors-headers
pip install djangorestframework

python manage.py migrate
python manage.py runserver 0.0.0.0:9000

//ok
curl -s http://127.0.0.1:9000/decoration/cart/

//need to set public ip's firewall rule:
//via https://console.cloud.tencent.com/lighthouse/instance/detail?rid=4&id=lhins-qvxla03w&tab=firewall
//then both below access ok.
curl -s http://118.25.176.102:9000/decoration/cart/
http://118.25.176.102:9000/decoration/cart/


```
