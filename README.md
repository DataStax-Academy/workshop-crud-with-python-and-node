# 🎓🔥 CRUD operations with NodeJS and Python

[![License Apache2](https://img.shields.io/hexpm/l/plug.svg)](http://www.apache.org/licenses/LICENSE-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://gitpod.io/#https://github.com/DataStax-Academy/workshop-crud-with-python-and-node/)
![version](https://img.shields.io/badge/version-0.0.1-blue)
[![Discord](https://img.shields.io/discord/685554030159593522)](https://discord.com/widget?id=685554030159593522&theme=dark)

Welcome to the *CRUD operations with NodeJS and Python with Astra* workshop! In this two-hour workshop, the Developer Advocate team of DataStax shows you the basics of connecting, updating and reading records from the powerful distributed NoSQL database Apache Cassandra.

Using Astra, the cloud based Cassandra-as-a-Service platform delivered by DataStax, we will cover the very first steps for every developer who wants to try to learn a new database: **CRUD operations.**

## Video Recordings 

- 📺 [Wednesday, october 7th *(NAM Time)*](https://www.youtube.com/watch?v=3KsR59Y2_Uw)

- 📺 [Thursday, october 8th *(IST Time)*](https://www.youtube.com/watch?v=axR9SHYnfMs)


## Table of Contents

1. [Database Setup **(ASTRA)**](#1-setup-database) 
2. [IDE Setup **(GITPOD)**](#2-setup-ide) 
2. [Hands-on](#)
    1. [Execute CRUD operations with **NodeJS**](crud-nodejs/README.md)
    2. [Execute CRUD operations with **Python**](crud-python/README.md)
3. [Materials](#)
    1. [Ask Questions on community](https://community.datastax.com/)
    2. [Join our Discord chat](https://bit.ly/cassandra-workshop)
    2. [Get the Slides](slides/Presentation.pdf)

## 1. Setup Database

To get started with a free-forever, zero-install Cassandra database **[click here](https://dtsx.io/workshop)** 🚀. 

- **✅ Step 1a. SignIn** : 

*expected output*
<img src="https://user-images.githubusercontent.com/1936716/103555190-7c63fd80-4e75-11eb-97d7-732d37969c40.png" width=“700” />

- **✅ Step 1b. You'll then be directed to the summary page. Locate the button `Add Database`**

*expected output*
<img src="https://user-images.githubusercontent.com/1936716/103556066-d0bbad00-4e76-11eb-9f36-ce456bb12e57.png" width=“700” />

- **✅ Step 1b. Choose the free plan and select your region**

**Free tier**: 5GB storage, no obligation

**Provider**: This will determine what cloud provider your database will run on

**Region**: This is where your database will reside physically (choose one close to you or your users). For people in EMEA please use `europe-west-1`, idea here is to reduce latency.

Once your values are selected click "Configure Database"

*expected output*
<img src="https://user-images.githubusercontent.com/1936716/103558072-ba632080-4e79-11eb-83e8-df49cf2c5243.png" width=“700” />

- **✅ Step 1c. Configure and create your database**

While Astra allows you to fill in these fields with values of your own choosing, please follow our reccomendations to make the rest of the exercises easier to follow. If you don't, you are on your own! :)

- **Database name** - `myastracluster` 

- **Keyspace name** - `spacecraft`

- **Database User name (case sensitive)** - `SUser`

- **Password (case sensitive)** - `SPassword1`. Fill in both the password and the confirmation fields.

- **Create the database**. Click the `Create Database` button.

*expected output*
<img src="https://user-images.githubusercontent.com/1936716/103559170-56415c00-4e7b-11eb-8c9e-e3409e51b4e8.png" width=“700” />

You will see your new database `pending` in the Dashboard.

*expected output*
<img src="https://user-images.githubusercontent.com/1936716/103559267-78d37500-4e7b-11eb-8e84-669e925f88c6.png" width=“700” />

The status will change to `Active` when the database is ready, this will only take 2-3 minutes. You will also receive an email address when it is ready.

*expected output*
<img src="https://user-images.githubusercontent.com/1936716/103559322-90126280-4e7b-11eb-8bb8-b935bf74b0ae.png" width=“700” />


- **✅ Step 1d. View your Database and connect**

Let’s review the database you have configured. Select your new database in the lefthand column.

<img src="https://user-images.githubusercontent.com/1936716/103559452-c4861e80-4e7b-11eb-8cea-a28f3624b44f.png" width=“700” />


- **✅ Step 1e. Connect via CQL console**

In the Summary screen for your database, select **_CQL Console_** from the top menu in the main window. This will take you to the CQL Console and log you in.


<img src="https://user-images.githubusercontent.com/1936716/103560763-f0a29f00-4e7d-11eb-82d5-febc37351136.png" width=“700” />

- **✅ Step 1f. Create the schema**

You are now logged to the Database. The prompt should look like `token@cqlsh>`. 

Navigate to the keyspace (you can have multiple keyspaces in the same database)

```cql
use spacecraft;
```

Create the schema (tables, index, user-defined-type...):

```sql
CREATE TYPE IF NOT EXISTS location_udt (
    x_coordinate double,
    y_coordinate double,
    z_coordinate double
);

CREATE TABLE IF NOT EXISTS spacecraft_journey_catalog (
    spacecraft_name text,
    journey_id timeuuid,
    active boolean,
    end timestamp,
    start timestamp,
    summary text,
    PRIMARY KEY (spacecraft_name, journey_id)
);

CREATE TABLE IF NOT EXISTS spacecraft_pressure_over_time (
    spacecraft_name text,
    journey_id timeuuid,
    reading_time timestamp,
    pressure double,
    pressure_unit text,
    PRIMARY KEY ((spacecraft_name, journey_id), reading_time)
);

CREATE TABLE IF NOT EXISTS spacecraft_speed_over_time (
    spacecraft_name text,
    journey_id timeuuid,
    reading_time timestamp,
    speed double,
    speed_unit text,
    PRIMARY KEY ((spacecraft_name, journey_id), reading_time)
);

CREATE TABLE IF NOT EXISTS spacecraft_temperature_over_time (
    spacecraft_name text,
    journey_id timeuuid,
    reading_time timestamp,
    temperature double,
    temperature_unit text,
    PRIMARY KEY ((spacecraft_name, journey_id), reading_time)
);

CREATE TABLE IF NOT EXISTS spacecraft_location_over_time (
    spacecraft_name text,
    journey_id timeuuid,
    reading_time timestamp,
    location frozen<location_udt>,
    location_unit text,
    PRIMARY KEY ((spacecraft_name, journey_id), reading_time)
);
```

Check that all tables were created:

```sql
describe tables;
```

*Expected output*
```bash
KVUser@cqlsh:spacecraft> desc tables;

spacecraft_journey_catalog     spacecraft_temperature_over_time
spacecraft_pressure_over_time  spacecraft_location_over_time
spacecraft_speed_over_time
```

## 2. Setup IDE

**✅  Open Gitpod** : [Gitpod](http://www.gitpod.io/?utm_source=datastax&utm_medium=referral&utm_campaign=datastaxworkshops) is an IDE 100% online based on Eclipse Theia. To initialize your environment simply click on the button below *(CTRL + Click to open in new tab)*

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/DataStax-Academy/workshop-crud-with-python-and-node/)

💥💥💥

[🏠 Back to Table of Contents](#table-of-contents)
