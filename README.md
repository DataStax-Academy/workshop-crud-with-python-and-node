🎓🔥 CRUD operations with NodeJS and Python with Astra 🔥🎓

Welcome to the 'CRUD operations with NodeJS and Python with Astra' workshop! In this two-hour workshop, the Developer Advocate team of DataStax shows you the basics of connecting, updating and reading records from the powerful distributed NoSQL database Apache Cassandra. Using Astra, the cloud based Cassandra-as-a-Service platform delivered by DataStax, we will cover the very first steps for every developer who wants to try to learn a new database: CRUD operations. 

It doesn't matter if you join our workshop live or you prefer to do at your own pace, we have you covered. In this repository, you'll find everything you need for this workshop:

- Materials used during presentations
- Hands-on exercises
- Workshop videos
  - [First workshop](https://youtu.be/Zf1TTwD4ibQ) [NAM Time]
  - [Second workshop](https://youtu.be/pVLN6FsUeyo) [IST Time]
- [Discord chat](https://bit.ly/cassandra-workshop)
- [Questions and Answers](https://community.datastax.com/)

## Table of Contents

| Title  | Description
|---|---|
| **Slide deck** | [Slide deck for the workshop](slides/Presentation.pdf) |
| **1. Create your Astra instance** | [Create your Astra instance](#1-create-your-astra-instance) |
| **2. Execute CRUD operations with NodeJS** | [CRUD with NodeJS](crud-nodejs/README.md) |
| **3. Execute CRUD operations with Python** | [CRUD with Python](crud-python/README.md) |


## 1. Create your Astra instance

`ASTRA` service is available at url [https://astra.datastax.com](https://dtsx.io/workshop). `ASTRA` is the simplest way to run Cassandra with zero operations at all - just push the button and get your cluster. `Astra` offers **10 Gb Tier Free Forever** and you **don't need a credit card** or anything to sign-up and use it. 

**✅ Step 1a. Register (if needed) and Sign In to Astra** : You can use your `Github`, `Google` accounts or register with an `email`.

Make sure to chose a password with minimum 8 characters, containing upper and lowercase letters, at least one number and special character

- [Registration Page](https://dtsx.io/workshop)

- [Authentication Page](https://dtsx.io/workshop)

![my-pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/login-1000.png?raw=true)


**✅ Step 1b. Choose the free plan and select your region**

![my-pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/choose-a-plan-1000-annotated.png?raw=true)

- **Select the free tier**: 5GB storage, no obligation

- **Select the region**: This is the region where your database will reside physically (choose one close to you or your users). For people in EMEA please use `europe-west-1` idea here is to reduce latency.

**✅ Step 1c. Configure and create your database**

You will find below which values to enter for each field.

![my-pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/create-and-configure-annotated-1000.png?raw=true)

- **Fill in the database name** - `killrvideocluster.` While Astra allows you to fill in these fields with values of your own choosing, please follow our reccomendations to make the rest of the exercises easier to follow. If you don't, you are on your own! :)

- **Fill in the keyspace name** - `killrvideo`. It's really important that you use the name killrvideo (with no 'e' in "killr") here in order for all the exercises to work well. We realize you want to be creative, but please just roll with this one today.

- **Fill in the Database User name** - `KVUser`. Note the user name is case-sensitive. Please use the case we suggest here.

- **Fill in the password** - `KVPassword1`. Fill in both the password and the confirmation fields. Note that the password is also case-sensitive. Please use the case we suggest here.

- **Create the database**. Review all the fields to make sure they are as shown, and click the `Create Database` button.

You will see your new database `pending` in the Dashboard.

![my-pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/dashboard-pending-1000.png?raw=true)

The status will change to `Active` when the database is ready, this will only take 2-3 minutes. You will also receive an email address when it is ready.

**✅ Step 1d. View your Database and connect**

Let’s review the database you have configured. Select your new database in the lefthand column.

Now you can select to connect, to park the database, to access CQL console or Studio.

![my-pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/summary-1000.png?raw=true)


[🏠 Back to Table of Contents](#table-of-contents)

