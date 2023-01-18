import requests
import json

class SmsMan:
	def __init__(self,api_key):
		self.api_key = api_key
		self.api_url ="http://api.sms-man.com/control/"

	def getBalance(self):
		url = f"get-balance?token={self.api_key}"
		r = requests.get(self.api_url+url)
		jsonOutput = json.loads(r.text)
		return jsonOutput

	def requestPhone(self,service, country):
		url = f"get-number?token={self.api_key}&country_id={country}&application_id={service}"
		r = requests.get(self.api_url+url)
		jsonOutput = json.loads(r.text)
		return jsonOutput
 
	def getSms(self,request_id):
		url = f"get-sms?token={self.api_key}&request_id={request_id}"
		r = requests.get(self.api_url+url)
		jsonOutput = json.loads(r.text)
		print(f"{jsonOutput}")
		if "error_code" in jsonOutput:
			return False
		else:
			return jsonOutput

	def getServices(self):
		url = f"applications?token={self.api_key}"
		r = requests.get(self.api_url+url)
		jsonOutput = json.loads(r.text)
		return jsonOutput

	def getCountries(self):
		url = f"countries?token={self.api_key}"
		r = requests.get(self.api_url+url)
		jsonOutput = json.loads(r.text)
		return jsonOutput

	def changeRequestStatus(self,request_id,status):
		validStatus = ["ready","close","reject","used"]
		if status not in validStatus:
			return {"error":"invalid status"}
		url = f"set-status?token={self.api_key}&request_id={request_id}&status={status}"
		r = requests.get(self.api_url+url)
		jsonOutput = json.loads(r.text)
		return jsonOutput

	def getCountryInfos(self,countryName):
		countries = self.getCountries()
		out = False
		for count in countries:
			currObj = countries[count]
			if(f"{countryName}" in currObj["title"] ):
				out = currObj
				break
		return out

	def getServiceInfos(self,serviceName):
		services = self.getServices()
		out = False
		for obj in services:
			currObj = services[obj]
			if(f"{serviceName}" in currObj["title"]):
				out = currObj
				break
		return out

if __name__ == "__main__":
	print("this is a module, don't run it like this")
