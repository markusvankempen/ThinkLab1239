
import time
import sys
import uuid
import argparse
import wiotp.sdk
import wiotp.sdk.application
import json
#a-8n44qz-g9kxaf4qur
#3s@ssLla*9(r+OPB8x
myConfig = {
    "identity": {
        "appId": "CHANGEME"
    },
    "auth": {
        "key": "a-n8ve7d-qzetkpxh1d",
        "token": "CM92*Wbsxad&V2Dxvn"
    }
}

def myEventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    print(str % (event.format, event.eventId, event.device, json.dumps(event.data)))

tableRowTemplate = "%-33s%-30s%s"


def mySubscribeCallback(mid, qos):
    if mid == statusMid:
        print("<< Subscription established for status messages at qos %s >> " % qos[0])
    elif mid == eventsMid:
        print("<< Subscription established for event messages at qos %s >> " % qos[0])


def myEventCallback(event):
    #print(event)
    print("%-33s%-30s%s" % (event.timestamp.isoformat(), event.device, event.eventId + ": " + json.dumps(event.data)))


def myStatusCallback(status):
    if status.action == "Disconnect":
        summaryText = "%s %s (%s)" % (status.action, status.clientAddr, status.reason)
    else:
        summaryText = "%s %s" % (status.action, status.clientAddr)
    print(tableRowTemplate % (status.time.isoformat(), status.device, summaryText))


def interruptHandler(signal, frame):
    client.disconnect()
    sys.exit(0)

client = None
#client = wiotp.sdk.application.ApplicationClient(config=myConfig, logHandlers=None)
try:
    client = wiotp.sdk.application.ApplicationClient(config=myConfig, logHandlers=None)
    # If you want to see more detail about what's going on, set log level to DEBUG
    # import logging
    # client.logger.setLevel(logging.DEBUG)
    client.connect()
except wiotp.sdk.ConfigurationException as e:
    print(str(e))
    sys.exit()
except wiotp.sdk.UnsupportedAuthenticationMethod as e:
    print(str(e))
    sys.exit()
except wiotp.sdk.ConnectionException as e:
    print(str(e))
    sys.exit()

print("(Press Ctrl+C to disconnect)")

client.deviceEventCallback = myEventCallback
client.deviceStatusCallback = myStatusCallback
client.subscriptionCallback = mySubscribeCallback
typeId="pws"
deviceId="pws00"
statusMid = client.subscribeToDeviceStatus(typeId, deviceId)
event="weather"
#eventsMid = client.subscribeToDeviceEvents(typeId, deviceId, event)
eventsMid = client.subscribeToDeviceEvents(typeId)
print("=============================================================================")
print(tableRowTemplate % ("Timestamp", "Device", "Event"))
print("=============================================================================")

while True:
    time.sleep(1)
