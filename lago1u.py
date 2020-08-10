import requests
import json
import csv
import time
import random
from urllib import parse
import pymysql
import self as self

data = ["Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522 (KHTML, like Gecko) Safari/419.3",
       "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
       "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
       "Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
       "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
       "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
       "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
       "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
]


class LaGouSpider(object):

    def __init__(self):
        # self.url = 'https://www.lagou.com/jobs/list_'+ job +'?labelWords=&fromSearch=true&suginput='
        self.post_url = 'https://www.lagou.com/jobs/positionAjax.json?px=defaul&needAddtionalResult=false'
        self.user_agent = self.read_user_agent()
        self.proxies = self.read_proxies()
        # self.creat_file()

    # 读取本地UA
    def read_user_agent(self):
            headers = data
            return headers

    # 读取本地Proxy
    def read_proxies(self):
            proxies = ['HTTPS://116.3.193.226:57959']
            return proxies


    def get_json(self, page_num,job):
        session = requests.session()
        session.headers = {'User-Agent': '%s' % random.choice(self.user_agent)[0],
                                'Referer': 'https://www.lagou.com/jobs/list_'+ job +'?labelWords=&fromSearch=true&suginput='}
        proxy = random.choice(self.proxies)
        session.proxies = {proxy[0]: '{}:{}'.format(proxy[1], proxy[2])}
        url = 'https://www.lagou.com/jobs/list_' + job + '?labelWords=&fromSearch=true&suginput='
        session.get(url)
        # print(session.proxies, session.cookies)

        data = {'first': 'false',
                'pn': '{}'.format(page_num),
                'kd': job,
                'sid': '2f99d51db5fb43949ed168e0237dbd99'}


        r = session.post(self.post_url, data=data)
        datas = json.loads(r.text)
        return datas

    def parse_data(self, datas):
            info = []
            for data in datas['content']['positionResult']['result']:
                positionName = data['positionName']
                companyFullName = pymysql.escape_string(data['companyFullName'])
                salary = pymysql.escape_string(data['salary'])
                workYear = pymysql.escape_string(data['workYear'])
                education = pymysql.escape_string(data['education'])
                positionId = data['positionId']
                result = (companyFullName, positionName, salary, workYear, education,str(positionId))

                info.append(result)
            return info

    def run(self,job):
        info = []
        info_2 = []
        for i in range(1, 10):
            datas = self.get_json(i,job)
            info.append(self.parse_data(datas))
            info_2 = info + (self.parse_data(datas))
            time.sleep(random.random())
        reuslt = [item for sub_list in info for item in sub_list]
        self.mysql(reuslt,job)
        return info_2
    def mysql(self,info,job):
           try:
                  conn = pymysql.connect(host='127.0.0.1',
                                         port=3306,
                                         user='root',
                                         password='chen0314',
                                         db='lagou',
                                         charset='utf8'
                                         )
           except pymysql.Error as e:
                  print("连接失败：%s" % e)
           # 使用cursor获取操作游标

           cursorr = conn.cursor()
           table_name = job
           cursorr.execute("drop table if exists %s" % table_name)
           # 数据库操作插入书法语句
           sql_createTb = """CREATE TABLE  `%s`(
                            公司名字  VARCHAR(255),
                            工作名称 VARCHAR(255),
                            薪水 VARCHAR(255),
                            工作经验 VARCHAR(255),
                            学历 VARCHAR(255),
                            公司编码 VARCHAR (255));
                            """% table_name
           cursorr.execute(sql_createTb)
           sql = "INSERT INTO `%s`" % table_name + "(公司名字,工作名称,薪水,工作经验,学历,公司编码) VALUES(%s, %s, %s, %s,%s,%s)"
           cursorr.executemany(sql, info)

           # 把数据提交到数据库
           conn.commit()
           # 关闭数据库
           conn.close()

           cursorr.close()



