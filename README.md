# DX NetOps Spectrum Event Configuration Analyzer
A tool to analyze free space in the Event Configuration File of DX NetOps Spectrum, allowing for better organization of Events as they are added.


### Purpose
If you are like me, you want to create events relating to a specific purpose or MIB sequentially for better organization.  
The in-built Event Configuration browser does not always make available space immediately obvious.  
When creating an event, the suggested Event Code is not always the first available Event Code.  
This script will analyze an export of Spectrums Event Configuration and suggest available space depending on how many Events you want to create.  
Only Custom Event Codes (0xfff0000) are suggested.


### Usage
1 - Export the Event Configuration table to CSV from Spectrum Oneclick.  
2 - Run the script with the following command, including the necessary input variables  
```
spectrum-event-config-analyzer.py <EventConfigurationFile.csv> <minimum required space>`  
```
For example, if I require at least 25 free event codes, I would run:  
```
spectrum-event-config-analyzer.py EventConfigurationFile.csv 25
```  
3 - The results will be output to console.  


### Results
Running the example command above provided the following results on my Event Configuration file:  
```
Found gaps that can fit 25 Events:
Gap starts at 0xFFF000BE with available space of 31 Events.
Gap starts at 0xFFF00674 with available space of 236 Events.
Gap starts at 0xFFF00772 with available space of 160 Events.
Gap starts at 0xFFF0089D with available space of 99 Events.
Gap starts at 0xFFF009A5 with available space of 1627 Events.
All space from 0xFFF01376 onwards is free. Available space: 1043594 Events.

```  


### Requirements
* This script was written with Python 3.9, but should be compatible with 3.6 upwards. 
* Modules required are csv and sys, both of which are included in Python 3.x
* Tested against DX NetOps Spectrum 23.3.13

