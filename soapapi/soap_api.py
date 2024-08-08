"""
SOAP : simple object access protocol
    application communication protocol
    platform independent
    based on XML

elements:
    1. envelope that identifies the XML document as SOAP message
    2. Header that contains header info
    3. Body that contains call and response info
    4. Fault that contains error and status info

Rules :
    1. SOAP msg must be encoded using XML
    2. SOAP msg must be soap envelope namespace
    3. msg must not contain DTD reference
    4. msg must not contains XML processing instructions

    

skeleton SOAP message:

<?xml version="1.0"?>

<soap:Envelope
xmlns:soap="http://www.w3.org/2003/05/soap-envelope" it is a namespace
soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

<soap:Header>
...
</soap:Header>

<soap:Body>
...
  <soap:Fault>
  ...
  </soap:Fault>
</soap:Body>

</soap:Envelope> 

"""

# encoding style :
# syntax   soap:encodingStyle="URI"
"""
<?xml version ="1.0">
<soap:Envelope
 xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
soap: encodingStyle="https://www.w3.org/2003/05/soap-encoding">

...
msg info
...

</soap:Envelope>
"""

"""
soap Header
    optional to add header
    contains specific info like (authentication, payment, etc) about soap msg
    if header is present it must be first child of envelope
    --> All immediate child of Header must be namespace-qualifies


<?xml version="1.0"?>
<soap:Envelope
xmnls:soap="https://www.w3.ord/2003/02/soap-envelope"
soap:emcodingStyle="https://www.w3.ord/2003/02/soap-encoding">

<soap:Header>
   <m:Trans xmlns:m="https://www.w3.ord/transcation/"
   soap:mustUnderstand="1">234
   </m:Trans>
</soap:Header>
...
...

</soap:Envelope>
"""

# above xml contains a header with Trans element and a mustUnderstand attribute with value of 1 and value of 234

"""
SOAP defines 3 attributes in default namespace:
    1. mustUnderstand
    2. actor
    3. encodingStyle

    atributes deines how msg should be processed
"""

"""
3. ecodingStyle
    used to define data types used in document
    will b e applied to th elements content and its child

Soap msg has no default encoding

ex
soap:encodingStyle="URI"

"""

"""
4. soap Body
    required
    contains actual soap msg
    immediate child may be namespace-qualified


<?xml version="1.0"?>

<soap:Envelope
xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

<soap:Body>
  <m:GetPrice xmlns:m="https://www.w3schools.com/prices">
    <m:Item>Apples</m:Item>
  </m:GetPrice>
</soap:Body>

</soap:Envelope> 



above requests the price od apples
m:GetPrice and items are application specific elements not part of soap namespace

"""


"""
5. soap Fault
    optional - used to indicate error msg
    holds error and status info
    if present must appear as child of body
    can only appear once in msg

fault sub elemnts:
    <faultcode> - code for identifying fault
    <faultstring> - human redable explanation of fault
    <faultactor> info about who caused fault to happen
    <detail> Holds application specific error info related to body
    
fault codes:
    error                desc
    VersionMismatch  Found an invalid namepsace for element
    MustUnderstand   An immediate child of gheader with mustUnderstand attribute set to 1 was not understood
    Client           The message was incorrectly formed ot contained incorrect info
    Server           There was a problem  with server so the message could not proceed
"""

"""
HTTP protocol

request msg:

POST /item HTTP/1.1
Host: 1889.123.255.239
Content-Type: text/plain
Content-Length: 200


status codes:
200 OK
Content-Type: text/plain
Content-Length: 200

or

400 Bad Request
Content-Length: 0
"""

"""
SOAP Binding

HTTP - at least two headers Content-Type and Content-Length
SMTP - used as last resort or particular cases

"""



"""
SOAP Request:
POST /InStock HTTP/1.1
Host: www.example.org
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>

<soap:Envelope
xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

<soap:Body xmlns:m="http://www.example.org/stock">
  <m:GetStockPrice>
    <m:StockName>IBM</m:StockName>
  </m:GetStockPrice>
</soap:Body>

</soap:Envelope>
"""

"""
SOAP response:
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>

<soap:Envelope
xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

<soap:Body xmlns:m="http://www.example.org/stock">
  <m:GetStockPriceResponse>
    <m:Price>34.5</m:Price>
  </m:GetStockPriceResponse>
</soap:Body>

</soap:Envelope>

"""