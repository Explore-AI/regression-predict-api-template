# Flask-based Model API
#### EXPLORE Data Science Academy Regression Predict

## 1) Overview

This repository forms the basis of *Task 2* for the **Regression Predict** within EDSA's Data Science course. It hosts template code which will enable students to deploy their own developed models through a web server-based API.   

#### 1.1) Wait, what is an API again?

[![What is an API](assets/imgs/What_is_an_API.png)](https://youtu.be/s7wmiS2mSXY)

An API - or Application Programming Interface - refers to a set of procedures and protocols that allows us to send and request information between ourselves and remote applications. You can think of this as a channel of communication to a remote server using specific commands that allow you to use their applications without needing to host that functionality yourself. Many types of API's exist, but for this predict task we are interested specifically in Web API's. These allow us to send and receive information using web development languages, such as HTML and JSON. The video above provides a simple and intuitive explanation of how API's operate.

#### 1.2) How our API will work

![Flask Web-server](assets/imgs/API.png)

##### Description of files

Several files within this repository enable the correct functioning of our API. We provide a high-level description of these salient files within the table below:

| File Name              | Description                                                                          |
| :--------------------- | :--------------------                                                                |
| `api.py`               | Flask web server application definition and instantiation.                           |
| `model.py`             | Contains helper functions to separate model specific code from our API definition.   |
| `utils/request.py`     | Simple script to simulate a POST request sent to our API.                            |
| `utils/train_model.py` | Code used to train the simple model used for demonstration of the API's functioning. |

## 2) Usage Instructions

#### 2.1) Creating a copy of this repo

| :zap: WARNING :zap: |
|:--------------------|
|Do **NOT** *clone* this repository. Instead follow the instructions in this section to *fork* the repo.|

As described within the Predict instructions for the Regression Sprint, this code represents a *template* from which you can base your own model's API. As such, in order to modify the template to serve your own model (and the associated code changes which are required for this), you will need to **[fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)** this repository. Failing to do this will lead to complications when trying to work on the API remotely.

![Fork Repo](assets/imgs/fork_repo.png)  

To fork the repo, simply ensure that you are logged into your GitHub account, and then click on the 'fork' button at the top of this page as indicated within the figure above.


#### 2.2) Running the API on your local machine

As a first step to becoming familiar with our API's functioning, we recommend setting up a running instance on your own local machine.

To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

 1. Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
 pip install -U flask numpy pickle json pandas scikit-learn
 ```

 2. Clone the *forked* repo to your local machine.

 ```bash
 git clone https://github.com/{your-account-name}/regression-predict-api-template.git
 ```  

 3. Navigate to the base of the cloned repo, and run the API web-server initialisation script.

 ```bash
 cd regression-predict-api-template/
 python api.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
----------------------------------------
Model succesfully loaded
----------------------------------------
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

4. Leave the web server script running within the current bash/terminal session. Open a new session, and navigate to the `utils` subfolder of the cloned repo.

```
cd {your/custom/path}/regression-predict-api-template/utils/
```

5. Run the `request.py` script located within the utils subfolder to simulate a POST request for our running API.

```
python request.py
```

If you receive an error at this point, please ensure that the web server is still running in your original bash/terminal session. If the script ran successfully, you should receive similar output to the message shown below:

```
Sending POST request to web server API at: http://127.0.0.1:5000/api_v0.1

Querying API with the following data:
 ['Order_No_21660', 'User_Id_1329', 'Bike', 3, 'Business', 31, 5, '12:16:49 PM', 31, 5, '12:22:48 PM', 31, 5, '12:23:47 PM', 31, 5, '12:38:24 PM', 4, 21.8, nan, -1.2795183, 36.8238089, -1.273056, 36.811298, 'Rider_Id_812', 4402, 1090, 14.3, 1301]

Received POST response:
**************************************************
API prediction result: 1547.3014476106036
The response took: 0.004323 seconds
**************************************************
```

Congratulations! You've now officially deployed your first web server API, and have successfully received a response from it.

With these steps completed, we're now ready to both modify the template code to place our own model within the API, and to host this API within an AWS EC2 instance. These processes are outlined within the sections below.  

#### 2.3) Updating the API to use your own model

#### 2.4) Running the API on a remote AWS EC2 instance



### FAQ

This section of the repo will be periodically updated to represent common questions which may arise around its use. If you detect any problems/bugs, please [create an issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue) and we will do our best to resolve it as quickly as possible.

We wish you all the best in your learning experience :rocket:

![Explore Data Science Academy](assets/imgs/EDSA_logo.png)
