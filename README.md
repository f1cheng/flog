# flog
## env
```  
--150.158.168.151 root/c..i()
--81.68.228.238 root/c..1()
--111.230.243.15 root/Cf......
```  

## script to execute
```
source run.sh
source client.sh

git add .
git commit -m 'abc'
git push origin HEAD:main

```

## backend class based view
### get from db and new url to access
```
cd /home/cf/program/
source my_pyenv/bin/activate
cd /home/cf/program/flog/blog/
python manage.py runserver 0.0.0.0:9000
```

#### curl for get test
```
curl -s http://150.158.168.151:9000/decoration/cart/
```

#### web for get test
```
http://150.158.168.151:9000/decoration/cart/
```

### post to db
#### only when model table updating, it is required to execute two commands
```
python manage.py makemigrations
python manage.py migrate
```

#### view to post db
```
```

#### curl to post db
```
1. curl -H "Content-Type:application/json" -X POST --data '{"name":"fei"}' http://150.158.168.151:9000/decoration/cart/
2. ➜  
~client request:
curl -H "Content-Type:application/json" -X POST --data '{"payid":5215, "name":"test155", "fee":55, "paydate": "2021-02-19"}' http://150.158.168.151:9001/decoration/cart/
~server response:
{"data": [{"payid": 5215, "name": "test155", "fee": 55, "paydate": "2021-02-19"}], "status": 200, "msg": "new"}% 
```

### put(update) to db
```
~client request:
curl -H "Content-Type:application/json" -X PUT --data '{"payid":555, "name":"test15", "fee":555, "paydate": "2021-02-19"}' http://150.158.168.151:9001/decoration/cart/
~server response:
{"data": [{"payid": 555, "name": "test15", "fee": 555, "paydate": "2021-02-19"}], "msg": "update", "status": 200}%
```

### delete from db
```
~client request:
curl -H "Content-Type:application/json" -X DELETE --data '{"payid":555, "name":"test15", "fee":555, "paydate": "2021-02-19"}' http://150.158.168.151:9001/decoration/cart/
~server response:
{"data": [{"payid": 555, "name": "test15", "fee": 555, "paydate": "2021-02-19"}], "msg": "delete", "status": 200}% 
```


## frontend vue bsed view
### create vue project
```
cd /home/cf/program/web_vue/
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install webpack -g
cnpm install vue-cli -g
--vue init webpack frontend
cd frontend
cnpm install
vim /home/cf/program/web_vue/frontend/config/index.js
==change host from localhost to 0.0.0.0, so that public ip can be accessed via outside of the server
-> host: '0.0.0.0' 
cnpm run dev
Your application is running here: http://0.0.0.0:8082

==client accessing via url
http://150.158.168.151:8082/

new:
cd /home/cf/program/flog/fe/frontend
cnpm run dev
http://150.158.168.151:8080/
```

### project to load data to UI from django
```
cd /home/cf/program/web_vue/frontend/
cnpm i element-ui -S

==src/main.js change the url IP@
axios.defaults.baseURL = 'http://150.158.168.151:9000/'

-         <template scope="scope">
+         <template slot-scope="scope">

seems executing npm run dev---killed.!!!
but cnpm run dev

main important thing is 'cnpm install' sucessfully, 
to reboot host, 
then both 'cnpm run dev' and 'npm run dev' commands work.
```

### add vue axios get/post/put/delete functions with ugly UI:)
```
-              <td> <el-date-picker v-model="InData.paydate" type="datetime" placeholder="选择time" value-format="yyyy-mm-dd hh:mm:ss"></el-date-picker> </td>
+              <td> <el-date-picker v-model="InData.paydate" type="datetime" placeholder="chosse time" value-format="yyyy-MM-dd HH:mm:ss"></el-date-picker> </td>
```
