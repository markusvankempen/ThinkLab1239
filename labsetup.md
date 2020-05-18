
### LAB Setup Instructions

## 1.1 Prerequisite 

1. Sign up for a Weather Company API Key (optional) 

[TWC APIKey](https://callforcode.weather.com/register) 
We have API keys already set up in the lab but just to be safe you should use your own.

2. Get your geo location or your city (Lat/Lon)

[Get your Location](https://www.latlong.net/) 
We will use this to personalize your Weather Station Location. Note down latitude & longitude.

3. Think2020 is over but you can create this LAB yourself 

You can still use the preconfigure Cloud Enviroments using/claiming your enviroment via 
[Claim your LAB ID](https://thinklab1239.mybluemix.net/claimid)
(See LAB Part 1 as well)
#### Note: These envirments are refresh every night so export your flows!

Or you can create your own IBM Cloud Instance/Envrioment using the instructions below

https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/NotPartofTheLab-SelfDeploymentAtHome.pdf

Alternataively you can install Node-RED and Jupyter notebooks locally follow the instruction and excecises 

## The LAB Part 1
Before the LAB starts we will go through some introductions and a walkthrough of the LAB and the excerises.
You will set up your Node-RED instance with your API key and the Lat/Lon as well as your LAB ID.

You can request the LAB ID here once the LAB is opened - only during think2020

[Claim your LAB ID](https://thinklab1239.mybluemix.net/claimid)

Detailed instruction and excecises can be found here.

[Lab Instructions Part 1](https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/Lab1239-PartOne.pdf)

## The LAB Part 2
Part 2 is about Watson Studio using a Jupyter Notebook to analyse the weather data and create data queries to retrieve the data into Node-RED and display it in a dashboard

Prerequisite 

Sign up for WatsonStudio account 
[Register for WatsonStudio](https://dataplatform.cloud.ibm.com/registration/stepone)

[Lab Instructions Part 2](https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/Lab1239-PartTwo.pdf)

Download this this github and Import the WS1-...ipynb Python Notebook

## The LAB Part 3
Part 3 is about Watson Studio with a Jupyter Notebook to predict the weather data using a SARIMAX model.
We will use the data for the previous exerise and create a seasonal prediction model. We will create queries which we can trigger from node-red and display the forecast data in a dashboard.

Sign up for WatsonStudio account 
[Register for WatsonStudio](https://dataplatform.cloud.ibm.com/registration/stepone)

[Lab Instructions Part 3](https://github.com/markusvankempen/ThinkLab1239/blob/master/instructions/Lab1239-PartThree.pdf)

Download this this github and Import the WS2-... .ipynb Python Notebook
## Extras

Python: There is some python sdk code which you can use on your desktop at home to access the IoT Platform.
Watson Auto AI - you can use the clean weather data and Watson Auto AI to create/deploy a model which can be triggered via APIs. 

THE END!




version: mvk20200518
