# Databricks notebook source
# DBTITLE 1,Common Libraries Imported
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import Window

# COMMAND ----------

# MAGIC %md
# MAGIC # Question 1
# MAGIC ### Flatten the Nested Order Data

# COMMAND ----------

customer_data = [
    (
        101,
        "Anurag",
        [
            {"order_id": 1, "product": "Laptop", "amount": 50000},
            {"order_id": 2, "product": "Mouse", "amount": 1000}
        ]
    ),
    (
        102,
        "Stuti",
        [
            {"order_id": 3, "product": "Keyboard", "amount": 2500}
        ]
    ),
    (
        103,
        "Rahul",
        []
    )
]


# COMMAND ----------

# DBTITLE 1,Step 1 for Question 1 -> Define the Schema
order_schema = ArrayType(
    StructType([
        StructField("order_id", IntegerType(), True),
        StructField("product", StringType(), True),
        StructField("amount", IntegerType(), True)
    ])
)

customer_schema=StructType([
        StructField("customer_id", IntegerType(), True),
        StructField("customer_name", StringType(), True),
        StructField("orders", order_schema, True)
    ])

# COMMAND ----------

# DBTITLE 1,Step 2 of Question 1 --> Display the Data in Dataframe
customer_df= spark.createDataFrame(customer_data,customer_schema)
display(customer_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Explode the Array

# COMMAND ----------

explode_df=customer_df.withColumn("order",explode_outer(col("orders")))
display(explode_df)

# COMMAND ----------

# DBTITLE 1,Step 4--> Extract the Fields from the Struct
final_orders_df=explode_df.select(
    "customer_id",
    "customer_name",
    col("order.order_id").alias("order_id"),
    col("order.product").alias("product"),
    col("order.amount").alias("amount")

)
display(final_orders_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Question 2
# MAGIC ### Union DataFrames with Different Column Orders
# MAGIC You are getting daily files in that the columns are same but the order of the columns are different 
# MAGIC
# MAGIC so how you will safely combine them?

# COMMAND ----------

day1_data = [
    (1, "Anurag", 50000),
    (2, "Stuti", 60000)
]
day2_data = [
    (70000, 3, "Shruti"),
    (80000, 4, "Shalini")
]
day1_data_df=spark.createDataFrame(day1_data,["emp_id","emp_name","salary"])
day2_data_df=spark.createDataFrame(day2_data,["salary","emp_id","emp_name"])

display(day1_data_df)
display(day2_data_df)

# COMMAND ----------

# DBTITLE 1,Wrong method to do union in such cases
wrong_union=day1_data_df.union(day2_data_df)
display(wrong_union)

# COMMAND ----------

# DBTITLE 1,Correct method to do union in such cases
correct_union=day1_data_df.unionByName(day2_data_df)
display(correct_union)

# COMMAND ----------

# MAGIC %md
# MAGIC If there is a scenario where There is a new Dataframe having missing columns

# COMMAND ----------

day3_data = [
    (5, "Vaishnav", 90000, "IT")
]

day3_df = spark.createDataFrame(
    day3_data,
    ["emp_id", "emp_name", "salary", "department"]
)
display(day3_df)

# COMMAND ----------

combined_df=day3_df.unionByName(correct_union,)
display(combined_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Followup Questions --> Does union remove duplicates?

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------


