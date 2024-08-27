# Workshop # 1 ETL

This workshop is part of a data engineering challenge in Python, aimed at demonstrating knowledge in data management, transformation, and creating visualizations from it.

![image](https://github.com/caroldvarela/images/blob/main/Proyect.png)
## Workshop Description

We will work with a dataset of candidates, including 50,000 candidates who participated in selection processes, provided in a CSV file. The fields found are:

- **First Name:** The candidate's first name.
- **Last Name:** The candidate's last name.
- **Email:** The candidate's email address.
- **Country:** The candidate's country of residence or origin.
- **Application Date:** The date the candidate submitted their application.
- **Yoe (Years of Experience):** Indicates the number of years of experience the candidate has in their field.
- **Seniority:** Defines the candidate's level of seniority, which can be categorized into levels such as Junior, Senior, etc.
- **Technology:** Indicates the primary technology or tech stack the candidate has experience with or excels in.
- **Code Challenge Score:** The score obtained by the candidate in the code challenge.
- **Technical Interview:** The score obtained by the candidate in the technical interview.

## Workshop notebooks


### 1. Data Migration

- **File:** `Data_migration.ipynb`
- **Description:** Imports the CSV file, transforms it, and migrates it to a relational PostgreSQL database using SQLAlchemy. In this step, the necessary tables are also created in the database.

### 2. Exploratory Data Analysis (EDA)

- **File:** `EDA.ipynb`
- **Description:** Performs exploratory analysis of the data loaded into the database. This includes identifying null values, reviewing data types, analyzing data distribution, and searching for patterns and correlations.

### 3. Data Transformation

- **File:** `Data_transformation.ipynb`
- **Description:** Performs deeper data transformation, such as creating new columns (e.g., the `Hired` column) and categorizing technologies. The transformed data is loaded back into the database.

## Prerequisites

- Python 3.8+ 🐍
- PostgreSQL 🗃️
- Virtual environment (recommended) 🌍

## Setting Up the Environment

1. Clone this repository:

    ```bash
    git clone https://github.com/caroldvarela/workshop-01.git
    cd workshop-01
    ```

2. Create the database:

    ```sql
    CREATE DATABASE your_db_name;
    ```

3. Create a `.env` file in the root of the project with the following environment variables for connecting to the PostgreSQL database:

    ```env
    PGDIALECT=your_host
    PGUSER=your_db_password
    PGPASSWD=your_db_user
    PGHOST=your_host_adress
    PGPORT=5432
    PGDB=your_db_name
    WORK_DIR=your_working_directory
    ```

4. Set up and activate your virtual environment:

    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

You are now ready to start working on this workshop.


# Creating a Dashboard in Power BI from PostgreSQL

Follow these steps to connect Power BI to a PostgreSQL database and create your dashboard.

## Step 1: Obtain Data

Ensure you have the dataset and that it is already loaded into a PostgreSQL database.

## Step 2: Open Power BI Desktop

1. **Launch Power BI Desktop:** Open Power BI Desktop on your computer.

## Step 3: Connect to PostgreSQL

1. **Go to Home Tab:**
   - Click on the **"Home"** tab in the top menu.

2. **Get Data:**
   - Click on the **"Get Data"** button on the Home ribbon.

3. **Select Data Source:**
   - In the "Get Data" window, select **"More…"** to open the full list of data sources.

![image](https://github.com/caroldvarela/images/blob/main/Dashboard_1.png)

   - Scroll down and choose **"PostgreSQL database"** from the list.
   - Click **"Connect"**.
     
![image](https://github.com/caroldvarela/images/blob/main/Dashboard_2.png)

4. **Enter Server Details:**
   - In the **"PostgreSQL database"** window, enter the **Server** and **Database** details:
     - **Server:** Your PostgreSQL server address (e.g., `localhost` or `your_host`).
     - **Database:** The name of your PostgreSQL database.
![image](https://github.com/caroldvarela/images/blob/main/Dashboard_3.png)

5. **Verify Connection:**
   - Power BI will attempt to connect to your PostgreSQL database. If successful, you will see a list of available tables.

## Step 5: Select Tables

1. **Select the Desired Tables:**

![image](https://github.com/caroldvarela/images/blob/main/Dashboard_4.png)

2. **Preview and Transform Data (Optional):**
   - If you need to make any transformations or adjustments to the data before loading it into Power BI, click **"Transform Data"** instead of **"Load"**. This will open the Power Query Editor where you can perform data cleaning and transformation tasks.

## Step 6: Build Your Dashboard

   - Once your data is loaded into Power BI, you can start creating visualizations. Drag and drop fields from your tables onto the report canvas to create charts, tables, and other visual elements.
   - Customize the layout and design of your dashboard. Add filters, slicers, and interactive elements to make your dashboard informative and user-friendly.
   - Save your Power BI file and, if desired, publish it to the Power BI service for sharing and collaboration.

Congratulations! You have successfully created a dashboard in Power BI using data from a PostgreSQL database. 
