import json, urllib, time
from datetime import datetime

def CreaArchivo():
    archivo1=open('art.txt','a')
    archivo2=open('cpm.txt','a')
    archivo3=open('epm.txt','a')


def consulta_art():
	#Manejo de JsonArray
	#arreglos iniciados con valores random
	array=[3]
	Json=[array]
	def urlapp():
		#URL average response time
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance|Business%20Transactions|WLS1033|APP|Average%20Response%20Time%20%28ms%29&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
				print array
   			#grabar archivos en txt
			archivo1=open('art.txt','a')
			archivo1.write (time.strftime('%d/%m/%y-')+time.strftime('%H:%M:%S') +","+ str(array) + "," )
	def urlapp_bolsa():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Bolsas%7CAverage%20Response%20Time%20%28ms%29&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
	   		#grabar archivos en txt
			archivo1=open('art.txt','a')
			archivo1.write (str(array) + "," )
	def urlapp_cuenta():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Cuenta%7CAverage%20Response%20Time%20%28ms%29&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo1=open('art.txt','a')
			archivo1.write (str(array) + "," )
	def urlapp_plan():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Plan%7CAverage%20Response%20Time%20%28ms%29&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo1=open('art.txt','a')
			archivo1.write (str(array) + "," )
			archivo1.close()
	def urlapp_trafico():
		#URL APP.TRAFICO CALLS FOR MINUTE
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Trafico%7CAverage%20Response%20Time%20%28ms%29&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo1=open('art.txt','a')
			archivo1.write (str(array) + "\n" )
			archivo1.close()
    	urlapp=urlapp()
    	urlappbolsa=urlapp_bolsa()
    	urlappcuenta=urlapp_cuenta()
    	urlappplan=urlapp_plan()
    	urlapptrafico=urlapp_trafico()
def consulta_cpm():
	#Manejo de JsonArray
	#arreglos iniciados con valores random
	array=[3]
	Json=[0,"hola","ciao",array]
	def urlapp():
		#URL call per minute
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
				print array
   			#grabar archivos en txt
			archivo2=open('cpm.txt','a')
			archivo2.write (time.strftime('%d/%m/%y-')+time.strftime('%H:%M:%S') +","+ str(array) + "," )
	def urlapp_bolsa():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Bolsas%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
	   		#grabar archivos en txt
			archivo2=open('cpm.txt','a')
			archivo2.write (str(array) + "," )
	def urlapp_cuenta():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Cuenta%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo2=open('cpm.txt','a')
			archivo2.write (str(array) + "," )
	def urlapp_plan():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Plan%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo2=open('cpm.txt','a')
			archivo2.write (str(array) + "," )
			archivo2.close()
	def urlapp_trafico():
		#URL APP.TRAFICO CALLS FOR MINUTE
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Trafico%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo2=open('cpm.txt','a')
			archivo2.write (str(array) + "\n" )
			archivo2.close()
    	urlapp=urlapp()
    	urlappbolsa=urlapp_bolsa()
    	urlappcuenta=urlapp_cuenta()
    	urlappplan=urlapp_plan()
    	urlapptrafico=urlapp_trafico()
def consulta_epm():
	#Manejo de JsonArray
	#arreglos iniciados con valores random
	array=[3]
	Json=[0,"hola","ciao",array]
	def urlapp():
		#URL error per minute
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP%7CErrors%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
				print array
   			#grabar archivos en txt
			archivo3=open('epm.txt','a')
			archivo3.write (time.strftime('%d/%m/%y-')+time.strftime('%H:%M:%S') +","+ str(array) + "," )
	def urlapp_bolsa():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Bolsas%7CErrors%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
	   		#grabar archivos en txt
			archivo3=open('epm.txt','a')
			archivo3.write (str(array) + "," )
	def urlapp_cuenta():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Cuenta%7CErrors%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo3=open('epm.txt','a')
			archivo3.write (str(array) + "," )
	def urlapp_plan():
		#URL
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Plan%7CErrors%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo3=open('epm.txt','a')
			archivo3.write (str(array) + "," )
			archivo3.close()
	def urlapp_trafico():
		#URL APP.TRAFICO CALLS FOR MINUTE
		url ="http://10.43.11.143:8090/controller/rest/applications/Portales/metric-data?metric-path=Business%20Transaction%20Performance%7CBusiness%20Transactions%7CWLS1033%7CAPP.Trafico%7CErrors%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=15&output=json"
		response = urllib.urlopen(url)
		datos = json.loads(response.read())
		for data in datos:
			for metrics in data['metricValues']: #Acceder a Metricas
				array=metrics['value']
			print array
		  		#grabar archivos en txt
			archivo3=open('epm.txt','a')
			archivo3.write (str(array) + "\n" )
			archivo3.close()
    	urlapp=urlapp()
    	urlappbolsa=urlapp_bolsa()
    	urlappcuenta=urlapp_cuenta()
    	urlappplan=urlapp_plan()
    	urlapptrafico=urlapp_trafico()

class TestClass:

    @staticmethod
    def StaticMethod():
        print ("static")
        crear=CreaArchivo()
        query= consulta_art()
        print 'art'
        query1=consulta_cpm()
        print 'cpm'
        query2=consulta_epm()
        print 'epm'
    def __init__(self):
        print ("constructor")

    def __del__(self):
        print ("destructor")



while True:

    obj= TestClass()
    # the following both are ok.
    obj.StaticMethod()

    del obj
    time.sleep(60)
