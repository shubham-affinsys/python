import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"
service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

header = zeep.xsd.Element(
    "Header",
    zeep.xsd.ComplexType(
        [
            zeep.xsd.Element(
                "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
            ),
            zeep.xsd.Element(
                "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
            ),
        ]
    ),
)

header_value = header(Action=method_url,To=service_url)
client = zeep.Client(wsdl=wsdl_url)
country_code="IN"

result = client.service.CountryIntPhoneCode(
    sCountryISOCode = country_code,
    _soapheaders = [header_value]
)

print(f"Phone Code for {country_code} is {result}")

country_code="US"
# service call
result = client.service.CountryIntPhoneCode(
    sCountryISOCode = country_code,
    _soapheaders = [header_value]
)

#POST request
response = client.service.CountryIntPhoneCode(
    sCountryISOCode=country_code,
    _soapheaders=[header_value]
)

print(f"Phone Code for {country_code} is {result}")
print(response)

# import requests
# # SOAP request URL
# url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
#
# # structured XML
# payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
# 			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
# 				<soap:Body>
# 					<CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
# 						<sCountryISOCode>IN</sCountryISOCode>
# 					</CountryIntPhoneCode>
# 				</soap:Body>
# 			</soap:Envelope>"""
# # headers
# headers = {
# 	'Content-Type': 'text/xml; charset=utf-8'
# }
# # POST request
# response = requests.request("POST", url, headers=headers, data=payload)
#
# # prints the response
# print(response.text)
# print(response)
