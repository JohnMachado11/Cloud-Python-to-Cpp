## Cloud-Python-to-Cpp

This project was designed to leverage **several** `Google Cloud Platform` cloud services to create a robust and automated system which can be interacted with via `C++` code. 

Why `C++`? The use case of that programming language specifically in the context of this project would be for example, having a `C++` based physical device pull from the cloud the latest `firmware` it needs, or just any kind of data from the cloud really.

Ultimately in the end, a secure API to pull data from a `BigQuery` database table was designed and it can actually be called by **any** programming language as long as the correct credentials get sent in `json` format to the `Auth_Func`. 

The programming language `Python` is utilized to create the entire backend component on `Google Cloud Platform`. 

`Firebase` is also utilized as part of the authentication system. 

------

`Google Cloud Platform` technologies:

- `Artifact Registry` - Stores the latest Docker image builds for `Cloud Run`

- `BigQuery` - Data warehouse which stores the table of data we interact with

- `Cloud Build` - Monitors GitHub repo and automates the process of deploying new code into the cloud

- `Cloud Functions (Gen 2)` - The backend for the project. Within each Cloud Function is the `Python` code. 

- `Cloud Run` - Generation 2 of `Cloud Functions` is actually `Cloud Run` behind the scenes. Therefore `Python` code executes here. 

- `Cloud Scheduler` - Cron job scheduler for any job in the cloud

- `Cloud Storage` - Stores the latest `Python` code for the `Cloud Functions`

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

- The `Insert_Int_Func` operates independently from the `Auth_Func` and `Compute_Func`. 
- `Insert_Int_Func` is triggered every **6 hours** by `Cloud Scheduler`
- A randomized integer between the ranges of 0-75 is inserted into a `BigQuery` table


