# HomeMonitor
给自己的圣诞礼物</br>
A Xmas gift for myself.
Due to the lockdown this year, dont have really much choices to have my vacation, so I just got these rasperri pi stuff. 
So, this project is mainly aimming on using raspberry pi to develop a smart home system which can understand the voice command and 
do some work for the users. 
Its not really fancy as it sounds like right now, but lets see where it goes. 
Currently, I have implemented several useful functionalities like voice recognition which can translate the voice into text.
Then the baby jarvis will match the keywords like "weather" " time" stuff like that, and fetch the related inforamtion online,
and report to the users by voice. 




due to 今年lockdown 了， 所以很sad 不能出去玩。
准备树莓派搞一搞， 弄个家庭各种数据的监控

菜鸡没玩过 看别人做的很好玩， 所以准备自己写一个。
玩玩看吧
总之很期待

后续有可能写一个智能识别的小车 用来放牧我的🐱



<div>  Pins Layout for Raspberry Pi Pico
</div>    
<img src="raspberry_pi_pico_pinout.png" width="700" height="620" />
</p>


## 功能 ：
- 温度 & 湿度 ： 
    - 使用原件：DHT11
- 气体检测
    - 使用原件 ：MQ5
- 声音监测：
    - 使用原件 ：LM386

Now having more ideas for the aspect of home security. In this project, it will also monitoring the front door, it will be able to check if the comming person is living here or not. If not, then it will predict the height and weight of the person and store this info with the face of the comming person into the database. 
And when the ppl leaving the house, it will automatically remove the info of this person. The time phase of deletetion is customizable, by default it will be three days. 

The audio detector will also capture the voice of ppl, it should be able to detect different languages, and analyze the frequency for different person which could also be used to help verify different person. 



