
### LAB Setup Instructions

## 1.1 Prerequisite 
1. Sign up for WatsonStudio account 
[Register for WatsonStudio](https://dataplatform.cloud.ibm.com/registration/stepone)
You will need this in the 2 Part of the Lab 

2. Sign up for Weather Company API Key
[TWC APIKey](https://callforcode.weather.com/register)
We have API keys already setup in the lab but just to be safe you should use your own.

3. Get your geo location or your city (Lat/Lon)
[Get your Location](https://www.latlong.net/) 
We will use this for to personalize your Weather Station Location. Note down latitude & longitude.

### Note: 
Since we using VM box all our location would be the same based on the DataCenter location.
so please get your location before the lab using the link above.


## The LAB Part 1
Before the LAB starts we will go thru some introductions and a walkthru of the LAB and the excerises.
You will setup your Node-RED instance with your API key and the Lat/Lon as well as your LAB ID.

You can request the LAB ID here once the LAB is opened.

[Claim your LAB ID](https://thinklab1239.mybluemix.net/claimid)

Detailed instruction and excerise can be found here.

[Lab Instructions Part 1](https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/Lab1239-PartOne.pdf)

## The LAB Part 2
Part 2 is about Watson Studio using a Jupyter Notebook to Analyse the weather data and creating data queries to retieve the data into Node-RED and display it in a dashboard

Sign up for WatsonStudio account 
[Register for WatsonStudio](https://dataplatform.cloud.ibm.com/registration/stepone)

[Lab Instructions Part 2](https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/Lab1239-PartTwo.pdf)

Download this this github and Import the WS-PartOne.ipynb Python Notebook

## The LAB Part 3
Part 3 is about Watson Studio with aJupyter Notebook to Predict the weather data using a SARIMAX model.
We will use the data for the previouse exerise and create a seaonal prediction model. We will queries which we can trigger from node-red and display the forecast data in a dashboard.

Sign up for WatsonStudio account 
[Register for WatsonStudio](https://dataplatform.cloud.ibm.com/registration/stepone)

[Lab Instructions Part 3](https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/Lab1239-PartThree.pdf)

## Extras

Python - there is some python sdk code which you can use on your desktop at home to access the IoT Platform.
Watson Auto AI - you can use the clean weather data and Watson Auto AI to create/deploy a model which can be triggered via APIs. 

THE END!




version: mvk20200501
