# Home Assistant SSAMControl

This repository contains a script for [hacs-pyscipt](https://github.com/custom-components/pyscript) to enable support for turning SSAMControl alarm systems on and off with [Home Assistant](https://www.home-assistant.io/).

# DISCLAIMER

I created this script for my own use and it worked fine in my environment using the most recent versions of Home Assistant, Pyscritps and the SSAMControl server as of 2023-06-19. 

That being said, I have to add that I take absolutely no responsibility for any problems or damage caused when you are using this script.  If you rely on this software for any important purpose, like securing your house, please do a code review and carefully decide if you want to use it. I cannot be held responsible in any case. Usage is completely at your own risk!

# Prerequisites

* Home Assistant 2023.6.2 or higher (https://www.home-assistant.io/)
* Home Assistant Add-on: File editor (https://github.com/home-assistant/addons/blob/master/configurator/README.md)
* HACS (https://hacs.xyz/)
* Pyscript 1.4.0 or higher (https://github.com/custom-components/pyscript)

# Installation

1. Copy the file ssamcontrol.py into your Home Assistant pyscript directory (e.g. /config/pyscript/ssamcontrol.py)
2. In the secrets file /config/secrets.yaml create the following secrets for the ssamcontrol script. Replace the strings in angle brackets with your values.
   ```yaml
   ssamcontrol_account: <your ssamcontrol username>
   ssamcontrol_password: <your ssamcontrol hashed password>
   ssamcontrol_pin_code: <your panel pin code>

   ```
   The hashed password can be easily gathered if you login to https://admin.ssamcontrol.com/home/ and check the body of token request that is sent in the browser dev tools (Ctrl-Shift-I).
3. Optional: define a switch to be able to use the script conveniently with your secrets. Insert the following into your  config/configuration.yaml.
   ```yaml
   switch:
     - platform: template
       switches:
         ssamcontrol:
           turn_on:
             service: pyscript.ssamcontrol
             data:
               account: !secret ssamcontrol_account
               password: !secret ssamcontrol_password
               pin_code: !secret ssamcontrol_pin_code
               mode: arm
           turn_off:
             service: pyscript.ssamcontrol
             data:
               account: !secret ssamcontrol_account
               password: !secret ssamcontrol_password
               pin_code: !secret ssamcontrol_pin_code
               mode: disarm
   ```