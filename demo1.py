#��һ����Ϊ��ȡ�����տγ�"
import requests

dic={}
cookies = 'semester.id=626; JSESSIONID=82C3FFE1D41741B3F0FC9F490ABA73C9; GSESSIONID=82C3FFE1D41741B3F0FC9F490ABA73C9'
demo1 = cookies.split(';')#cookies��Ҫʵʱ���£����ڲ������ѡ�
for line in demo1:
    key,value = line.split('=',1)
    dic[key] = value

r = requests.get('http://202.199.224.119:8080/eams/loginExt.action',cookies = dic)
print(r.text)

  