#第一部分为爬取“今日课程"
import requests

dic={}
cookies = 'semester.id=626; JSESSIONID=82C3FFE1D41741B3F0FC9F490ABA73C9; GSESSIONID=82C3FFE1D41741B3F0FC9F490ABA73C9'
demo1 = cookies.split(';')#cookies需要实时更新，过期并不提醒。
for line in demo1:
    key,value = line.split('=',1)
    dic[key] = value

r = requests.get('http://202.199.224.119:8080/eams/loginExt.action',cookies = dic)
print(r.text)

  