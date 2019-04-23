import sys
import time
import os.path
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def ReadPdf(fileName,path):
	file = open(path + fileName+".PDF", 'rb') # 以二进制读模式打开
	praser = PDFParser(file)
	doc = PDFDocument()
	# 连接分析器 与文档对象
	praser.set_document(doc)
	doc.set_parser(praser)
	# 创建PDf 资源管理器 来管理共享资源
	rsrcmgr = PDFResourceManager()
	# 创建一个PDF设备对象
	laparams = LAParams()
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	# 创建一个PDF解释器对象
	interpreter = PDFPageInterpreter(rsrcmgr, device)

	fileTxt =open(path+"txt\\"+fileName+".txt", 'w',encoding='utf-8')
	# 循环遍历列表，每次处理一个page的内容
	for page in doc.get_pages(): # doc.get_pages() 获取page列表
	    interpreter.process_page(page)
	    # 接受该页面的LTPage对象
	    layout = device.get_result()
	    for x in layout:
	        if hasattr(x, "get_text"):
	        	#print(x.get_text())
	        	fileTxt.write(x.get_text())
	file.close()
	fileTxt.close()
pass

def ReaAllPdf():
	path = os.getcwd()+"\\伟明\\"
	files= os.listdir(path)
	for file in files: #遍历文件夹
		if file.find(".PDF") > 0:
			fileName = os.path.splitext(file)[0]
			print(fileName)
			ReadPdf(fileName,path)		
pass
ReaAllPdf()


