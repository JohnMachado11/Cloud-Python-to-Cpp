## Cloud-Python-to-Cpp

This project was designed to leverage **several** `Google Cloud Platform` cloud services to create a robust and automated system which can be interacted with via `C++` code. 

In the end, a secure API to pull data from a `BigQuery` database table was designed and it can actually be called by **any** programming language as long as the correct credentials get sent in `json` format.

The programming language `Python` is utilized to create the entire backend component on `Google Cloud Platform`. 

`Firebase` is also utilized as part of the authentication system. 

------

**`Google Cloud Platform` technologies:**

1. `Artifact Registry` - Stores the latest Docker image builds for the Cloud Functions

2. `BigQuery` - Data warehouse 

3. `Cloud Build` - Monitors GitHub repo and automates the process of deploying new code into the cloud

4. `Cloud Functions (Gen 2)` - The backend for the project. With each Cloud Function is the `Python` code. 

5. `Cloud Run` - Generation 2 of `Cloud Functions` is actually `Cloud Run` behind the scenes. Therefore `Python` code executes here. 

6. `Cloud Scheduler` - Cron job scheduler for any job in the cloud

7. `Secret Manager` - Secure storage system for sensitive data

**`Firebase` technologies:**

1. `Authentication` - Stores the user account data

-----

### System Flow

`C++` --> `Auth_Func` --> `Compute_Func` --> `BigQuery`

Values of the 5 most recent records from the BigQuery table get returned to the `C++` code in the end. 

----
### Cloud Functions

1. `Auth_Func` = Authentication System
2. `Compute_Func` = Computation System
3. `Insert_Int_Func` = Data Insertion System





