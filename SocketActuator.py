import sys
import time
import os
os.environ["QT_PREFERRED_BINDING"]=os.pathsep.join(["PyQt5"])
sys.path.append("C:\\Program Files\\FreeCAD 0.18\\bin\\Lib\\site-packages\\PyQt5")
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.uic import loadUi
import os
import socket
import threading
class MainUi(QMainWindow) :
	def __init__(self, parent=None) :
		super(MainUi, self).__init__(parent)	
		self.init_ui()
		fileMenu = self.menuBar().addMenu("File(文件)")
		loadAction=fileMenu.addAction("Load(加载)")
		loadAction.setShortcut('Ctrl+L')
		sendAction=fileMenu.addAction("Send(发送)")
		sendAction.setShortcut('Ctrl+S')
		loadAction.triggered.connect(self.loadui)
		sendAction.triggered.connect(self.data_send)
		self.setWindowTitle('Actuator(驱动器)')
		self.message1='{"area":0,"volume":0}'
	def init_ui(self):
		self.setFixedSize(580,580)
		self.main_widget = QWidget()
		self.main_layout = QGridLayout()
		self.main_widget.setLayout(self.main_layout)
		self.right_widget = QWidget()
		self.right_layout = QGridLayout()
		self.right_widget.setLayout(self.right_layout)
		self.main_layout.addWidget(self.right_widget,0,2,12,10)
		self.setCentralWidget(self.main_widget)
		self.dataSend()
		self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.test_addr = ('127.0.0.1', 24567)
	def loadui(self):
		name_filter = "Graph files (*.ui)"
		savepath = QFileDialog.getOpenFileName(filter=name_filter)
		if type(savepath) in [tuple, list]:
			fpath = savepath[0]
		else:
			fpath = savepath
		if not fpath == '':
			with open(fpath, 'r') as f:
				fpath.replace('/',"//")
				self.right_layout.addWidget(loadUi(fpath))
	def dataSend(self):
		client_thread1 = threading.Thread(target=self.data_receive)
		client_thread1.start()
	def data_send(self):
		self.name = self.findChildren(QLineEdit)
		length_name = len(self.name)	
		self.d = dict()
		self.obj_Name_array = []
		for i in self.name:
			self.d[i.objectName()] = float(i.text())
			self.obj_Name_array.append(i.objectName())
		for i in self.name:
			self.d[i.objectName()] = float(i.text())
		data = str(self.d)
		#client
		test_data = data
		print ('send_data = ', test_data)
		print ('prepare to send ------')
		start=time.time()
		self.udp_socket.sendto(test_data.encode('utf-8'), self.test_addr)
		#time.sleep(1)
		end=time.time()
		print(end-start)
		print ('send_addr = ', self.test_addr)
		print ('send end ------')
	def data_receive(self):
		udp_socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bind_addr = ('127.0.0.1', 20001)
		print ('bind_addr = ', bind_addr)
		udp_socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		udp_socket1.bind(bind_addr)
		while True:
			print('begin to listen')
			revc_data  = udp_socket1.recvfrom(1024)
			#1024 maximum bytes
			print ('revc_data = ', revc_data)
			print ('data = ', revc_data[0])
			print ('ip_port = ', revc_data[1])
			if revc_data[0].decode('utf-8') != None:
				message = revc_data[0].decode('utf-8')
				rece = eval(message)
				rece_keys = list(rece.keys())
				for n in rece_keys :
					for j in self.obj_Name_array :
						if j == n :
							self.findChild(QLineEdit, j).setText(str(rece[j]))
if __name__ == "__main__":
	app = QApplication(sys.argv)
	the_window = MainUi()
	the_window.show()
	sys.exit(app.exec_())