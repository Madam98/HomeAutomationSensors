# Description

Initially, the project was used to create a system that communicates between home sensors and a mobile app. By setting up and using VPN communication through OpenVPN software, it was possible to control parameters remotely from outside the home network.

As of today, the system on which the application resided (using a RaspberryPi 3B computer) has been swapped with OpenMediaVault to learn the issues and consolidate knowledge of DevOps. With the use of Portainer, a Dockerfile will be added to the repository for easy building and configuration of the entire application.


#### Description of the project concept

The main goal of the project is to build a device for the user that will perform the most important functions needed to monitor his apartment. The device will monitor several factors that change in the environment:

- monitoring temperature and humidity in the apartment (https://botland.com.pl/czujniki-multifunkcyjne/9301-czujnik-temperatury-i-wilgotnosci-dht11-60c.html)
- monitoring of smoke and chad in the room (https://botland.com.pl/czujniki-gazow/3027-czujnik-dymu-i-latwopalnych-gazow-mq-2-polprzewodnikowy-modul-niebieski-5904422303693.html)
- monitoring whether a new person has entered the room + PIR (https://botland.com.pl/kamery-do-raspberry-pi/4522-kamera-hd-night-vision-e-ov5647-5mpx-dla-raspberry-pi-moduly-ir-waveshare-10300-5904422332860.html)
- A/D converter 3008 SPI-DIP (https://botland.com.pl/przetworniki/2358-przetwornik-a-c-mcp3008-10-bitowy-8-kanalowy-spi-dip-5904422302696.html)

<figure>
    <center><img src=".\Images\schematic.png" alt="Trulli" style="transform:rotate(-90deg); width:55%"></center>
    <figcaption align = "center"><b></b></figcaption>
</figure>

<figure>
    <center><img src=".\Images\build.png" alt="Trulli" style="width:50%"></center>
<figcaption align = "center"><b</b></figcaption>
</figure>

In order to exchange and record information, a sqlite3 database was used and communication through an API was created  










