# Human Classes
### With examples of four pillars of OOP

![image](https://user-images.githubusercontent.com/110176257/183023165-56154ae8-83d4-47e9-8d8f-a2b217581863.png)


## Four Piillars
### Abstraction 
Abstraction is a way of handling complexity. For example, hiding unnecessary data from the user and showing only what is relevant.

![image](https://user-images.githubusercontent.com/110176257/183029343-3722b867-f075-4d99-be7d-d1c0c925fd46.png)

The code above defines Female class. 
In the code below the implemetation details of the function are abstracted.

![image](https://user-images.githubusercontent.com/110176257/183029896-effcdca1-7adb-4003-8552-d58ac099cc66.png)


It returns:

![image](https://user-images.githubusercontent.com/110176257/183030176-70ba243d-efec-43eb-a73b-08cffbe9da07.png)


### Encapsulation

The Male class has private attributes, as stated by the __ prefix


![image](https://user-images.githubusercontent.com/110176257/183030585-519df715-bba4-4a21-b388-f108e3e3dbb1.png)


When the user tries to call this private attribute, they are told it does not exist
![image](https://user-images.githubusercontent.com/110176257/183030935-8db4d6d1-6106-4ab6-a15f-315da203fa58.png)

![image](https://user-images.githubusercontent.com/110176257/183030970-8ef5787f-fc30-448e-924f-e08209b6b831.png)


### Inheritance 

There are parent and child classes, as illustrated in the diagram at the top of the file. 
Inheritence means a child class can inherit all of the attributes and functions of the parent class. 
In the code below, you can see the name attribute of the Male class requires an input for each object made. 
Boy class inherits the attributes of the Male class and therefore requires an input when an object is made as well.

![image](https://user-images.githubusercontent.com/110176257/183034025-f6f7ea34-f67e-49cc-be27-e82bb5927120.png)

![image](https://user-images.githubusercontent.com/110176257/183034132-8900b40f-4e1a-4dd2-bf16-d722be0bff31.png)

![image](https://user-images.githubusercontent.com/110176257/183034191-b20da984-95d5-4046-b51a-20fe354588f9.png)


### Polymorphism 

In the following code, the attribute "facial_hair" is inherited from the Male class by the Boy class. But it is morphed to be False by default instead of True by default as children dont tend to have facial hair.

![image](https://user-images.githubusercontent.com/110176257/183035360-aff531a0-a0eb-47fb-99fe-cf161a1c8174.png)

![image](https://user-images.githubusercontent.com/110176257/183035461-13281567-0f9e-4a9c-9157-433734b6fa7a.png)




