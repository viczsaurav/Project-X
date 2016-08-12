# Project-X
App Challenge

Following are the components + functionalities:

Step 1: Emulate Existing system:  (Unique service key/Txn id to identify each request/response)

1) **Enrollment app (.Net)** – Backend + FrontEnd Enrollment page
-  	a. Responsible for capturing enrollments from UI page
- 	b. Calling CONFIG app to check for Merchant specific configurations
- 	c. Call NOTIFICATION app to notify Users
- 	d. Use app method signatures
- 	e. Database:User, Cards (each user can have multiple Cards)

2) **Config App (Java)** – Backend + FrontEnd
-   a. UI page to upload config setting per merchant/ Form to fill config details merchant wise
- 	b. UI page to view the config settings in a tabular form
- 	c. Called by ENROLLMENT app +  NOTIFICATION app to check for Merchant specific configurations
- 	d. Use app method signatures
- 	e. Database: Merchant_Code, Key, Value, Description

3) **Notification App (Python)** – Backend + FrontEnd
-   a. UI page to emulate received SMS from user
- 	b. Calling CONFIG app to check for Merchant specific configurations
- 	c. Calling ENROLLMENT app to transfer User details
- 	d. Use app method signatures
- 	e. Database: User_Phone, SMS

Step 2: Create Central App: (Unique service key/Txn id from above apps to identify each request/response)

1) **Adapters for existing systems** (.Net) - Backend
-   a. Using Method signatures/Contracts from existing system to create adapters
- 	b. Adapters should be transparent to each app to intercept each call between system components
- 	c. Push Request/response from each call to Kafka message queue alongside additional metrics
- 	d. Implement Heatbeat mechanism between apps.
- 	e. Implement Mocking capability for each app failure in adapters.
- 	f. DataBase – TBD

2) **Reader App(Java/Python)**- Backend
-   a. Resposible for reaching Request//Response queues from Kakfa and writing to DB
-   b. Will expose web-services to be consumed by JS Heat Map for multiple metrics.
-   c. Database - TBD

3) **Heat Map (JavaScript)** – FrontEnd
-	a. U- I to show components and their relation in real time
- 	b. Will call READER app to get data from DB
- 	c. Metrics to show:
- 		i.   Performance – Time taken per request between each component
- 		ii.  Volumes -  Number of Transactions + Size of Txns (Component-wise - > Service Method )
- 		iii. Heartbeat – Check about availability of each app in real time
-   	iv.  Service Mocking
-   	v.   End-to-End Flow map
