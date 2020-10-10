## 1. Hardware Setup

- Connect the VCC pin of LM-35 sensor to 5V pin of the Bolt device.

- Connect the GND pin of LM-35 sensor to GND pin of the Bolt device.

- Connect the analog output pin of LM-35 sensor to Analog input (A0) pin of the Bolt device.

- Make use of the male to female jumper wires to connect the temperature sensor to the bolt module

## 2. Get the Bolt Cloud API and Device ID

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198427/screenshot_from_2020-10-01_09-36-41_gI1ENSLyTI.png?auto=compress%2Cformat&w=740&h=555&fit=max">
</p>

## 3. Set up a localhost URL

Type the below command to generate a public URL for a localhost 

- ssh -R 80:localhost:PORT_NUMBER ssh.localhost.run
- Replace the [PORT_NUMBER] which you want to use for getting the POST request

<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198431/screenshot_from_2020-10-01_09-45-19_mMtGetbZjv.png?auto=compress%2Cformat&w=740&h=555&fit=max">
</p>

## 4. Setup the IFTTT module

Get the IFTTT app from this [link](https://play.google.com/store/apps/details?id=com.ifttt.ifttt&hl=en_IN)

- open the IFTTT app
- Click on create

<br/>

<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198432/screenshot_20201001-094633_hVutega7se.jpg?auto=compress%2Cformat&w=740&h=555&fit=max">
</p>

- Now, we have to set up two things: (If This, Then That)
- Click On If This and search for Google Assistant and Fill the required forms

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198433/screenshot_20201001-094832_SIEhTG5btb.jpg?auto=compress%2Cformat&w=740&h=555&fit=max">
</p>

- Save it.
- Now, click on Then That
- And Then search for webhooks (and set up it by filling required data)

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198434/screenshot_20201001-094839_YzOAhAI0Ow.jpg?auto=compress%2Cformat&w=740&h=555&fit=max">
</p>

Notice that I have put /temperatureRead after my URL that I have generated It is handled in the python decorator route.

- Save the current module.
- Now, go and create another module to receive the notification
- Same, as the above procedure GoTo create
- Setup If this using webhook and then that as notifications

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198437/screenshot_20201001-095416_VFu9S14L9b.jpg?auto=compress%2Cformat&w=740&h=555&fit=max">
</p>

- In the message, I have chosen value1.
- Now, The IFTTT setup is complete.

Get The IFTTT API key form this [link](https://ifttt.com/maker_webhooks)

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198442/screenshot_from_2020-10-01_10-02-17_L8WPe6GY0H.png?auto=compress%2Cformat&w=740&h=555&fit=max" title="Click on Documentation to get the API_KEY">
</p>

## Hardware Connection Image

<br/>
<p align="center">
    <img src="https://hackster.imgix.net/uploads/attachments/1198445/bc4efe5-10_eGgJFkOKnE.jpg?auto=compress%2Cformat&w=740&h=555&fit=max" title="Hardware Connection of BolT wifi module and LM-35 sensor">
</p>
