import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json,urllib2,re

#http://data.eastmoney.com/bbsj/201803/yjyg.html 业绩预告



url='http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=YJBB20_YJYG&token=70f12f2f4f091e459a279469fe49eca5&st=ndate&sr=-1&p=2&ps=30&js=var%20GyBAnEiK={pages:(tp),data:%20(x)}&filter=(IsLatest=%27T%27)(enddate=^2018-03-31^)&rt=50790621'
req = urllib2.Request(url=url);
res = urllib2.urlopen(req);
res = res.read();
s1, sData =res.split('data: ',1);
#print(sData)
sData = sData.lstrip("[");
sData = sData.rstrip("}");
sData = sData.rstrip("]");
#print(sData)
sData =sData.replace('},{','}|{');
sDataArr = sData.split('|');
#print(sDataArr[0])
#print(len(sDataArr))

dataArr =[1]*len(sDataArr);
for index in range(len(sDataArr)):
  dataArr[index] = json.loads(sDataArr[index]);


print(dataArr[0]["scode"]);

increaseArr =[];
for x in dataArr:
	 if x["forecasttype"] == "预增":
	 	print(x["sname"]);
	 	increaseArr.append(x);
	 	pass




jsonData = '{"scode":"000622","sname":"恒立实业","sclx":"深交所主板","enddate":"2018-03-31T00:00:00","forecastl":"-3000000","forecastt":"-2000000","increasel":"-2.29","increaset":"31.81","forecastcontent":"预计2018年1-3月归属于上市公司股东的净利润亏损200万元–300万元。","changereasondscrpt":"经营性亏损,公司销售订单不足。","forecasttype":"续亏","yearearlier":-2932838.96,"ndate":"2018-04-14T00:00:00","hymc":"机械行业","zfpx":14.76,"jlrpx":-2500000.0,"forecast":"unknown","IsLatest":"T"}';

text = json.loads(jsonData);
#print(text["forecastcontent"])










