## Room Temperature Monitoring Through Google Assistant
<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198419/_Ue2Sb7BPf2.blob?auto=compress%2Cformat&w=900&h=675&fit=min">
</p>
<br/>

---
#### Trigger Google Assitant by saying "What's the Room Temperature" and you will be notified by IFTTT with your current room Temperature.
---
### Requirements
#### <center> Hardware Components </center>

- [BoLT IoT Bolt WiFi Module](https://www.hackster.io/bolt/products/bolt-wifi-module?ref=project-ba(39dc))
- Temperature Sensor - LM 35
- Jumper Wires (generic)
- USB-A to Micro-USB Cable

#### <center> Software apps and Online services </center>
- [BolT IoT BolT cloud](https://www.hackster.io/bolt/products/bolt-cloud?ref=project-ba39dc)
- [IFTTT Maker Service](https://www.hackster.io/ifttt/products/maker-service?ref=project-ba39dc)
---
Start by saying "Hey Google, What's the temperature"

<br/>
<p align="center">
  <img src="https://hackster.imgix.net/uploads/attachments/1198425/screenshot_20201001-093009_U7KaH22JS8.jpg?auto=compress%2Cformat&w=740&h=555&fit=max" title="Google Assistant"
</p>

IFTTT will notify you by a notification of your current room temperature where you have set the Temperature sensor.

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198426/screenshot_20201001-093144_rHuwyONU45.jpg?auto=compress%2Cformat&w=740&h=555&fit=max" title="Notification by IFTTT">
</p>

---

For Setup and Software Installation Refer to:

- [SETUP](./SETUP.md)
- [INSTALL](./INSTALL.md)

---

## Running

Perform the necessary Installations

Place the main.py and conf.py file in the same directory
make an environment variable FLASK_APP which has the value main.py by:-
        
```bash
  export FLASK_APP=main.py
```
Then run the app by 
```bash        
  flask run
```

---