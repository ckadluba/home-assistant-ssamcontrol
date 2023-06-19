import requests

@service
def ssamcontrol(account, password, pin_code, mode):
    """yaml
name: SSAMControl Alarm
description: arms or disarms a SSAMControl alarm system.
fields:
  account:
     description: login name of the SSAMControl account
     required: true
  password:
     description: hashed password of the SSAMControl account
     required: true
  pin_code:
     description: numeric PIN code configured for the alarm panel
     required: true
  mode:
     description: panel mode to be set
     example: disarm
     required: true
     selector:
       select:
         options:
           - arm
           - disarm
"""
    # Request auth token
    auth_url = "https://admin.ssamcontrol.com/REST/v2/auth/login"
    auth_body = {
        "account": account,
        "password": password,
        "dealer_group": "",
        "pw_encrypted": "hashed",
        "login_entry": "web"
    }
    log.info("Sending token request to %s", auth_url)
    auth_response = task.executor(requests.post, auth_url, data=auth_body)
    auth_response_json = auth_response.json()
    token = auth_response_json["token"]
    
    # Set arm/disarm mode
    mode_url = "https://admin.ssamcontrol.com/REST/v2/panel/mode"
    mode_headers = {
        "token": token
    }
    mode_body = {
        "area": "1",
        "mode": mode,
        "pincode": pin_code,
        "format": "1"
    }
    log.info("Sending request to %s with mode %s", mode_url, mode)
    mode_response = task.executor(requests.post, mode_url, headers=mode_headers, data=mode_body)
    if mode_response.status_code != 200:
        log.error("Error setting mode %s: %s", mode, mode_response.text)
    else:
        log.info("Set mode %s successfully", mode)
