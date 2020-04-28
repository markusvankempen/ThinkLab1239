import time
import sys
import uuid
import argparse
import wiotp.sdk
authMethod = "token"

# Initialize the device client.

deviceOptions = {
            "identity": {"orgId": "n8ve7d", "typeId": "pws", "deviceId": "pws42"},
            "auth": {"token": "pws42pws42"},
}


def commandProcessor(cmd):
    print("Command received: %s" % cmd.data)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor


# Connect and send datapoint(s) into the cloud
deviceCli.connect()
for x in range(0, 10):
    data = {"name": "pws42", "temperature": x}

    def myOnPublishCallback():
        print("Confirmed event %s received by WIoTP\n" % x)

    success = deviceCli.publishEvent("weather", "json", data, qos=0, onPublish=myOnPublishCallback)
    if not success:
        print("Not connected to WIoTP")

    time.sleep(10)


# Disconnect the device and application from the cloud
deviceCli.disconnect()
