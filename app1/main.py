
#===========================================================================
# Test 3

#  We have a list of three strings defined in the code area.

# Extend the code so your program prints out the following out of that list:

# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

# filenames = ['document', 'report', 'presentation']

# for index, file in enumerate(filenames):
#     print(f"{index}-{file}.txt")
# =============================================================================

# Test 4

# We have a list of two IPs in the code area.

# Extend the code so your program:

# 1. Prompts the user to input an index (e.g., 0 or 1).

# 2. Depending on the user input, the program should return either You chose 100.122.133.111 or You chose 100.122.133.111

# Note: In order for the system to mark your exercise as correct, your code should return the exact output (i.e., upper case Y in You chose and no spaces or other characters after the IP.

# For example: Enter the index of the IP you want: 1
# You chose 100.122.133.111 

# Solution

# ips = ['100.122.133.105', '100.122.133.111']


# user_prompt = int(input("input an index 0 or 1: "))
# choice = ips[user_prompt]
# xchoice = "You chose"
# print(f'{xchoice} {choice}')

# =========================================================================================

[2010-04-24 07:51:54,393] DEBUG - [main] BulkOpsClient.main(): Execution begin.

[2010-04-24 07:51:54,393] DEBUG - [main] BulkOpsClient.main(): List of all 
configurations loaded: {numofthreads=1, impstatchkinterval=30, maxloginattempts=1, 
manifestfiledir=.\Manifest\, sessionkeepchkinterval=300, routingurl=https://
sso.crmondemand.com, hosturl=http://sdchs20n263.us.oracle.com, testmode=debug, 
maxthreadfailure=1, logintimeoutms=180000, csvblocksize=1000, maxsoapsize=10240}

[2010-04-24 07:51:54,393] DEBUG - [main] BulkOpsClient.main(): List of all options 
loaded: {password=*********, clientloglevel=detailed, waitforcompletion=False, 
datetimeformat=usa, importloglevel=errors, datafilepath=.\\data\\account1.csv, 
operation=insert, help=False, mapfilepath=.\\data\\account1.map, 
clientlogfiledir=., recordtype=account, duplicatecheckoption=externalid, 
username=oracle/oracle, csvdelimiter=,}

[2010-04-24 07:51:54,393]  INFO - [main] Attempting to log in...

[2010-04-24 07:51:55,081]  INFO - [main] Successfully logged in as: wchung/eric

[2010-04-24 07:51:55,081] DEBUG - [main] BulkOpsClient.doImport(): Execution begin.

[2010-04-24 07:51:55,081]  INFO - [main] Validating Oracle Data Loader On Demand 
Import request...

[2010-04-24 07:51:55,081] DEBUG - [main] FieldMappingManager.parseMappings(): 
Execution begin.

[2010-04-24 07:51:55,097] DEBUG - [main] FieldMappingManager.parseMappings(): 
Execution complete.

[2010-04-24 07:51:55,331] DEBUG - [Thread-1] ODWSSessionKeeperThread.Run(): 
Submitting BulkOpImportGetRequestDetail WS call

[2010-04-24 07:51:55,331]  INFO - [main] A SOAP request was sent to the server to 
create the import request.

[2010-04-24 07:51:55,862] DEBUG - [Thread-1] 
SOAPImpRequestManager.sendImportGetRequestDetail(): SOAP request sent successfully 
and a response was received

[2010-04-24 07:51:55,862] DEBUG - [Thread-1] ODWSSessionKeeperThread.Run(): 
BulkOpImportGetRequestDetail WS call finished

[2010-04-24 07:51:55,862] DEBUG - [Thread-1] ODWSSessionKeeperThread.Run(): SOAP 
response status code=OK

[2010-04-24 07:51:55,862] DEBUG - [Thread-1] ODWSSessionKeeperThread.Run(): Going 
to sleep for 300 seconds.

[2010-04-24 07:51:55,862] DEBUG - [main] 
SOAPImpRequestManager.handleSoapFaultException(): Handling SoapFaultException.

[2010-04-24 07:51:55,862] DEBUG - [main] There was an error sending the SOAP request 
to web service: SBL-ODU-01005

[2010-04-24 07:51:55,862] DEBUG - [main] BulkOpsClient.sendValidationRequest(): 
Experienced SOAP Request Rate Limit error while sending the validation request.  Will 
try to send again in 1 sec.

[2010-04-24 07:51:56,862]  INFO - [main] A SOAP request was sent to the server to 
create the import request.

[2010-04-24 07:52:01,268]  INFO - [main] A response to the SOAP request sent to 
create the import request on the server has been received.

[2010-04-24 07:52:01,268] DEBUG - [main] 
SOAPImpRequestManager.sendImportCreateRequest(): SOAP request sent successfully and 
a response was received

[2010-04-24 07:52:01,268]  INFO - [main] Oracle Data Loader On Demand Import 
validation PASSED.

[2010-04-24 07:52:01,268] DEBUG - [main] BulkOpsClient.sendValidationRequest(): 
Execution complete.

[2010-04-24 07:52:01,268] DEBUG - [main] BulkOpsClient.submitImportRequest(): 
Execution begin.

[2010-04-24 07:52:01,268] DEBUG - [main] BulkOpsClient.submitImportRequest(): 
Sending CSV Data Segments.

[2010-04-24 07:52:01,268] DEBUG - [main] CSVDataSender.CSVDataSender(): 
CSVDataSender will use 1 threads.

[2010-04-24 07:52:01,268]  INFO - [main] Submitting Oracle Data Loader On Demand 
Import request with the following Request Id: 1QA2-Q5NU1...

[2010-04-24 07:52:01,268] DEBUG - [main] CSVDataSender.sendCSVData(): Creating 
thread 0

[2010-04-24 07:52:01,284]  INFO - [main] Import Request Submission Status: Started

[2010-04-24 07:52:01,284] DEBUG - [main] CSVDataSender.sendCSVData(): Starting 
thread 0

[2010-04-24 07:52:01,284] DEBUG - [main] CSVDataSender.sendCSVData(): There are 
pending requests. Going to sleep.

[2010-04-24 07:52:01,284] DEBUG - [Thread-3] CSVDataSenderThread.run(): Thread 0 
submitting CSV Data Segment: 1 of 1

[2010-04-24 07:52:02,487]  INFO - [Thread-3] A response to the import data SOAP 
request sent to the server has been received.

[2010-04-24 07:52:02,487] DEBUG - [Thread-3] 
SOAPImpRequestManager.sendImportDataRequest(): SOAP request sent successfully and a 
response was received

[2010-04-24 07:52:02,487]  INFO - [Thread-3] A SOAP request containing import data 
was sent to the server: 1 of 1

[2010-04-24 07:52:02,487] DEBUG - [Thread-3] CSVDataSenderThread.run(): There is no 
more pending request to be picked up by Thread 0.

[2010-04-24 07:52:02,487] DEBUG - [Thread-3] CSVDataSenderThread.run(): Thread 0 
terminating now.

[2010-04-24 07:52:06,284]  INFO - [main] Import Request Submission Status: 100.00%

[2010-04-24 07:52:07,284]  INFO - [main] Oracle Data Loader On Demand Import 
submission completed succesfully.

[2010-04-24 07:52:07,284] DEBUG - [main] BulkOpsClient.submitImportRequest(): 
Execution complete.

[2010-04-24 07:52:07,300] DEBUG - [main] BulkOpsClient.doImport(): Execution 
complete.

[2010-04-24 07:52:07,300]  INFO - [main] Attempting to log out...

[2010-04-24 07:52:09,487]  INFO - [main] oracle/oracle is now logged out.

[2010-04-24 07:52:09,487] DEBUG - [Thread-1] ODWSSessionKeeperThread.Run(): 
Interrupted.

[2010-04-24 07:52:09,487] DEBUG - [main] BulkOpsClient.main(): Execution complete.


