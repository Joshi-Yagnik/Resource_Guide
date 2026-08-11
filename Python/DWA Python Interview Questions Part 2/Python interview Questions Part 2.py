# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC ## **DataX Data Engineering Bootcamp Enroll to Learn End to End**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Python Interview Questions for Data Engineers

# COMMAND ----------

# MAGIC %md
# MAGIC **Question 1: Find Duplicate Records**

# COMMAND ----------

customer_ids=[101,102,103,101,104,102,105]
seen=set()
duplicate=set()

for customer_id in customer_ids:
    if customer_id in seen:
        duplicate.add(customer_id)
    else:
        seen.add(customer_id)
print(duplicate)


# COMMAND ----------

# MAGIC %md
# MAGIC **Question 2: Count Frequency of Values**
# MAGIC

# COMMAND ----------

categories = [
    "Electronics",
    "Fashion",
    "Electronics",
    "Grocery",
    "Fashion",
    "Electronics",
    "Electronics",
    "Electronics",
    "Electronics"
]
frequency={}
for category in categories:
    frequency[category]=frequency.get(category,0)+1
print(frequency)



# COMMAND ----------

# MAGIC %md
# MAGIC **Question 3: Flatten Nested JSON**
# MAGIC

# COMMAND ----------

data = {
    "customer_id": 101,
    "customer_name": "Anurag",
    "orders": [
        {"order_id": 1, "amount": 500},
        {"order_id": 2, "amount": 800}
    ]
}

records=[]
for orders in data['orders']:
    records.append({
        "customer_id":data["customer_id"],
        "customer_name":data["customer_name"],
        "order_id":orders["order_id"],
        "amount":orders["amount"]
    })
display(records)



# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------


