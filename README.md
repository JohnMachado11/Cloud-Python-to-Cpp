## Cloud-Python-to-Cpp

This project was designed to leverage **several** `Google Cloud Platform` cloud services to create a robust and automated system which can be interacted with via `C++` code. 

Why `C++`? The use case of that programming language specifically in the context of this project would be for example, having a `C++` based physical device pull from the cloud the latest `firmware` it needs or just any kind of data from the cloud really.

Ultimately in the end, a secure API to pull data from a `BigQuery` database table was designed and it can actually be called by **any** programming language as long as the correct credentials get sent in `json` format to the `Auth_Func`. 

The programming language `Python` is utilized to create the entire backend component on `Google Cloud Platform`. 

`Firebase` is also utilized as part of the authentication system. 

`Looker Studio` data visualization dashboard for viewing data from the `BigQuery` table located [here](https://lookerstudio.google.com/u/2/reporting/6a9eaf10-58c9-4d75-8690-9a2759b7a256/page/VibFD). 

For testing of the API, if anyone is interested reach out directly via email [here](cpp.cloud.project@gmail.com). 


------

`Google Cloud Platform` technologies:

- `Artifact Registry` - Stores the latest Docker image builds for `Cloud Run`

- `BigQuery` - Data warehouse which stores the table of data we interact with

- `Cloud Build` - Monitors GitHub repo and automates the process of deploying new code into the cloud

- `Cloud Functions (Gen 2)` - The backend for the project. Within each Cloud Function is the `Python` code. 

- `Cloud Run` - Generation 2 of `Cloud Functions` is actually `Cloud Run` behind the scenes. Therefore `Python` code executes here. 

- `Cloud Scheduler` - Cron job scheduler for any job in the cloud

- `Cloud Storage` - Stores the latest `Python` code for the `Cloud Functions`

- `Looker Studio` - Data visualization tool

- `Secret Manager` - Secure storage system for sensitive data

`Firebase` technologies:

- `Authentication` - Stores the user account data

-----

### System Flow

`C++` --> `Auth_Func` --> `Compute_Func` --> `BigQuery`

Values of the 5 most recent records from the BigQuery table get returned to the `C++` code in the end. 

----
### Cloud Functions

1. `Auth_Func` - Publically Accessible (could be private as well)
2. `Compute_Func` - Private
3. `Insert_Int_Func` - Private

Let's talk about each:

1. `Auth_Func` The authentication system.   

- Everything starts here. Way before any data can be extracted from the `BigQuery` database table, a `request` from the user has to pass multiple tests before the code can proceeed. 

- 1. The `request` cannot be empty and the `json` must have the correct keys, `email` and `password`.
- 2. The value of the `email` key of the `json` must be a string.
- 3. The format of the value of the `email` key of the `json` must be in the correct format e.g. `"name@domain.com"`.
- 4. The value of the `password` key of the `json` must be a string.
- 5. The `email` and `password` must correlate to an existing user within `Firebase Authentication`.
  
- If everything checks out, then the `Compute_Func` `Cloud Function` gets called directly from the `Auth_Func`.

2. `Compute_Func` The computation system. Computation in the sense of enumerating, listing out. 

- The job of the `Compute_Func` is to simply extract the values of the 5 most recent records from a `BigQuery` table. 
- Those values are then placed into a list. 
- That list is converted to a string and then the string is returned to the `Auth_Func`. 

3. `Insert_Int_Func` The data insertion system. 

- The `Insert_Int_Func` operates independently from the `Auth_Func` and `Compute_Func` and its automated. 
- `Insert_Int_Func` is triggered every **6 hours** by `Cloud Scheduler`
- A randomized integer between the ranges of 0-75 is inserted into a `BigQuery` table

---

`Python`

Backend was designed with `Python` version `3.9`.

Libraries:

`google-cloud-secret-manager==2.12.6` - [PyPi url](https://pypi.org/project/google-cloud-secret-manager/)

`google-cloud-bigquery==3.5.0` - [PyPi url](https://pypi.org/project/google-cloud-bigquery/)

`python-dotenv==0.21.0`- [PyPi url](https://pypi.org/project/python-dotenv/)

`Pyrebase4==4.5.0` - [PyPi url](https://pypi.org/project/Pyrebase4/)

`pyarrow==11.0.0` - [PyPi url](https://pypi.org/project/pyarrow/)

`pandas==1.5.3` - [PyPi url](https://pypi.org/project/pandas/)

---

`C++`

Code tested and compiled on MacOS Ventura. 

- Compiler: `g++` 
- `C++` Standard: `17`

How to run `C++` code:

Be aware that preset credentials will be required to access the API.

- Be inside `C++/Cloud_Caller/src` folder
- Open terminal
- Type `g++ -o main main.cpp -lcurl` on terminal
- Type `./main` on terminal

Libraries:

`libucurl` - https://curl.se/libcurl/

