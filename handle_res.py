import xmltodict
import pprint

payment_success = """<FIXML xsi:schemaLocation="http://www.finacle.com/fixml executeFinacleScript.xsd" xmlns="http://www.finacle.com/fixml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <Header>
      <ResponseHeader>
         <RequestMessageKey>
            <RequestUUID>FEBA_1582887129176</RequestUUID>
            <ServiceRequestId>executeFinacleScript</ServiceRequestId>
            <ServiceRequestVersion>10.2</ServiceRequestVersion>
            <ChannelId>CRM</ChannelId>
         </RequestMessageKey>
         <ResponseMessageInfo>
            <BankId>03</BankId>
            <TimeZone>GMT+05:00</TimeZone>
            <MessageDateTime>2020-03-17T19:37:52.371</MessageDateTime>
         </ResponseMessageInfo>
         <UBUSTransaction>
            <Id/>
            <Status/>
         </UBUSTransaction>
         <HostTransaction>
            <Id/>
            <Status>SUCCESS</Status>
         </HostTransaction>
         <HostParentTransaction>
            <Id/>
            <Status/>
         </HostParentTransaction>
         <CustomInfo/>
      </ResponseHeader>
   </Header>
   <Body>
      <executeFinacleScriptResponse>
         <ExecuteFinacleScriptOutputVO></ExecuteFinacleScriptOutputVO>
         <executeFinacleScript_CustomData>
            <tranStatus>Success</tranStatus>
            <PmtOrderId>0316</PmtOrderId>
            <fintranDate>12-03-2020 00:00:00</fintranDate>
            <mobNumWB>9108648156</mobNumWB>
         </executeFinacleScript_CustomData>
      </executeFinacleScriptResponse>
   </Body>
</FIXML>"""



account_details="""
<FIXML xsi:schemaLocation="http://www.finacle.com/fixml executeFinacleScript.xsd" xmlns="http://www.finacle.com/fixml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <Header>
      <ResponseHeader>
         <RequestMessageKey>
            <RequestUUID>FEBA_1582887129176</RequestUUID>
            <ServiceRequestId>executeFinacleScript</ServiceRequestId>
            <ServiceRequestVersion>10.2</ServiceRequestVersion>
            <ChannelId>CRM</ChannelId>
         </RequestMessageKey>
         <ResponseMessageInfo>
            <BankId>03</BankId>
            <TimeZone>GMT+05:00</TimeZone>
            <MessageDateTime>2020-03-25T18:51:19.024</MessageDateTime>
         </ResponseMessageInfo>
         <UBUSTransaction>
            <Id/>
            <Status/>
         </UBUSTransaction>
         <HostTransaction>
            <Id/>
            <Status>SUCCESS</Status>
         </HostTransaction>
         <HostParentTransaction>
            <Id/>
            <Status/>
         </HostParentTransaction>
         <CustomInfo/>
      </ResponseHeader>
   </Header>
   <Body>
      <executeFinacleScriptResponse>
         <ExecuteFinacleScriptOutputVO></ExecuteFinacleScriptOutputVO>
         <executeFinacleScript_CustomData>
            <STATUS>SUCCESS</STATUS>
            <ResData>Valid Customer</ResData>
            <AcctId>12345678901</AcctId>
            <CustId>123456</CustId>
            <SchemeType>SBA</SchemeType>
            <AcctCrncyCode>USD</AcctCrncyCode>
            <FirstName>FALDHIN.T.</FirstName>
            <MiddleName>MUHAMMAD &/OR  FATMA FALDHIN</MiddleName>
            <LastName>MUHAMMAD</LastName>
            <DateOfBirth>13-12-2001</DateOfBirth>
            <Gender>M</Gender>
            <MobileNumber>+918328282078</MobileNumber>
            <EmailID>NA</EmailID>
            <NationalID>123456</NationalID>
            <PassportNumber>NA</PassportNumber>
            <DrivingLicense>NA</DrivingLicense>
            <VoterID>NA</VoterID>
            <AccoutStatus>D</AccoutStatus>
            <FrezStatus>D</FrezStatus>
            <registeredAtbranch>Y</registeredAtbranch>
         </executeFinacleScript_CustomData>
      </executeFinacleScriptResponse>
   </Body>
</FIXML>
"""
xml_response="""<?xml version="1.0" encoding="UTF-8"?>
<FIXML xmlns="http://www.finacle.com/fixml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.finacle.com/fixml executeFinacleScript.xsd">
    <Header>
        <ResponseHeader>
            <RequestMessageKey>
                <RequestUUID>7c95866bxbd_317</RequestUUID>
                <ServiceRequestId>executeFinacleScript</ServiceRequestId>
                <ServiceRequestVersion>10.2</ServiceRequestVersion>
                <ChannelId>COR</ChannelId>
            </RequestMessageKey>
            <ResponseMessageInfo>
                <BankId>02</BankId>
                <TimeZone>GMT+05:30</TimeZone>
                <MessageDateTime>2024-07-26T13:51:19.628</MessageDateTime>
            </ResponseMessageInfo>
            <UBUSTransaction>
                <Id/>
                <Status/>
            </UBUSTransaction>
            <HostTransaction>
                <Id/>
                <Status>SUCCESS</Status>
            </HostTransaction>
            <HostParentTransaction>
                <Id/>
                <Status/>
            </HostParentTransaction>
            <CustomInfo/>
        </ResponseHeader>
    </Header>
    <Body>
        <executeFinacleScriptResponse>
            <ExecuteFinacleScriptOutputVO/>
            <executeFinacleScript_CustomData>
                <CustAcctInquiry_RES>
                    <AcctDtls>
                        <account>25049482001</account>
                        <balance>82691455</balance>
                        <schmcode>ODL01</schmcode>
                        <schmType>ODA</schmType>
                        <acctCurrency>RWF</acctCurrency>
                    </AcctDtls>
                    <AcctDtls>
                        <account>25049482002</account>
                        <balance>748958.86</balance>
                        <schmcode>ODF01</schmcode>
                        <schmType>ODA</schmType>
                        <acctCurrency>USD</acctCurrency>
                    </AcctDtls>
                    <AcctDtls>
                        <account>25049482003</account>
                        <balance>902458</balance>
                        <schmcode>ODL01</schmcode>
                        <schmType>ODA</schmType>
                        <acctCurrency>RWF</acctCurrency>
                    </AcctDtls>
                    <AcctDtls>
                        <account>25049482004</account>
                        <balance>897278</balance>
                        <schmcode>ODL01</schmcode>
                        <schmType>ODA</schmType>
                        <acctCurrency>RWF</acctCurrency>
                    </AcctDtls>
                    <AcctDtls>
                        <account>25049482005</account>
                        <balance>0</balance>
                        <schmcode>ODL01</schmcode>
                        <schmType>ODA</schmType>
                        <acctCurrency>RWF</acctCurrency>
                    </AcctDtls>
                    <numOfAccounts>5</numOfAccounts>
                </CustAcctInquiry_RES>
            </executeFinacleScript_CustomData>
        </executeFinacleScriptResponse>
    </Body>
</FIXML>
"""


"""

def get_all_tags(res):
    if isinstance(res,dict):
        for key,val in res.items():
            yield key
            yield from get_all_tags(val)
    

def get_value(data,tag):
    if isinstance(data,list):
        for val in data:
            yield from get_value(val,tag)
    
    elif isinstance(data,dict):
        for key,val in data.items():
            if key==tag and val is not None:
                yield val
            yield from get_value(val,tag)
    else:
        return data



# xml_doc = payment_success
xml_doc = account_details
# xml_doc = xml_response

res = dict()
try:
    res = xmltodict.parse(xml_doc)
except Exception as e:
    print(f"Exception occured during parsing =====> {e}")


tags = list(get_all_tags(res))
for tag in tags:
    val_of_tag = list( get_value(res,tag))
    print(tag,"--------------------->: ",end="")
    if val_of_tag==[] or val_of_tag is None:
        print("no value found")
    elif len(val_of_tag)==1:
        pprint.pprint(val_of_tag[0])
    else:
        pprint.pprint(val_of_tag)

        """