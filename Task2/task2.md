## Task2 Submission
This is a submission for Task 2  
You can find the ROS package [here](https://github.com/Garvit-g/Learn-ROS/tree/main/beginner_tutorials)


* Writing a code for  [talker](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/talker.py) and [listener](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/listener.py) in ros and making them a node and running it
```
   roscore
   rosrun beginner_tutorials talker.py
   rosrun beginner_tutorials listener.py
```  
 <img src="https://github.com/Garvit-g/Learn-ROS/blob/main/Data/talker_listener.png">
 * Writing a code for sending int through [talker](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/talker_int.py)  and obtaining integer on [listener](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/subscriber_int.py)  in ros and making them a node and running it


 ```
   roscore
   rosrun beginner_tutorials talker_int.py
   rosrun beginner_tutorials listener_int.py
```  
  <img src="https://github.com/Garvit-g/Learn-ROS/blob/main/Data/int_talker.png">
  
  * Writing a code for sending char through [talker](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/talker_char.py) and obtaining integer on [listener](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/subscriber_char.py) in ros and making them a node and running it


```
   roscore
   rosrun beginner_tutorials talker_char.py
   rosrun beginner_tutorials subscriber_char.py
```  
  <img src="https://github.com/Garvit-g/Learn-ROS/blob/main/Data/char_talker.png">
  * Writing a code for sending bool through   [talker](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/talker_bool.py)   and obtaining bool on   [listener](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/subscriber_bool.py)   in ros and making them a node and running it





``` 
   roscore
   rosrun beginner_tutorials talker_bool.py
   rosrun beginner_tutorials subscriber_bool.py
```


  <img src="https://github.com/Garvit-g/Learn-ROS/blob/main/Data/bool_talker.png">
  
  * Sending a custom message using talker and listener in Ros
  
  * Making msg file 
  
   
   ```
    roscd beginner_tutorials
    mkdir msg
    echo "int64 num" > msg/Num.msg
   ```   
  * Using rosmsg 
  
    ```
    rosmsg show beginner_tutorials/Num
    ```
   * Creating a srv
   ``` 
    roscd beginner_tutorials
    mkdir srv
    roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv
    rossrv show AddTwoInts
   ```    
   * Writing code for [Talker](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/custom_talker2.py) and [Listener](https://github.com/Garvit-g/Learn-ROS/blob/main/beginner_tutorials/scripts/custom_listener2.py)
   <img src="https://github.com/Garvit-g/Learn-ROS/blob/main/Data/Custom_message.png">
   
   
   
 ``` 
    roscd beginner_tutorials
    chmod +x custom_talker2.py
    chmod +x custom_listener2.py
    
    rosrun beginner_tutorials custom_talker2.py
    rosrun beginner_tutorials custom_listener2.py
``` 





   
   
