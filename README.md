# sms-man-wrapper
Python wrapper for sms-man.com

# Installation
For the moment sms-man-wrapper isn't available to pypi (i'm working on it)
first install the dependency using 
```
pip install requests
```
then download smsman.py in the folder where you need it then import it

# Usage 
To use this module register an account on [sms-man.com](https://sms-man.com/?ref=7J4fAfTCYsSA)
here you can grab your API key
then you can initiate SmsMan class like this :
```python
#import the module
from smsman import SmsMan

#initialize the sms object using your api key in the constructor
sms = SmsMan("YOUR API KEY"}

countryInfos = sms.getCountryInfos("France") # return the infos required for the API calls like ID etc

#etc...
```

#Functions 
Here's a list of all the functions : 
    - getBalance(): returns the current balance of your account
    - requestPhone(service, country): requests a phone number for a specific service and country
    - getSms(request_id): retrieves the SMS messages for a specific request
    - getServices(): returns a list of available services
    - getCountries(): returns a list of available countries
    - changeRequestStatus(request_id, status): changes the status of a request
    - getCountryInfos(countryName): returns the country information for a specific country
    - getServiceInfos(serviceName): returns the service information for a specific service
