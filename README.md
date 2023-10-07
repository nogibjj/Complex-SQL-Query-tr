# Complex-SQL-Query-tr

[![CI](https://github.com/nogibjj/Complex-SQL-Query-tr/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Complex-SQL-Query-tr/actions/workflows/cicd.yml)


Week 6 Mini-Project
Tianji Rao

## Purpose
The purpose of this project is to use a complex SQL query on a Cloud data sever, Azure, on sample datasets to realize joins, aggregation, and sorting. 
Here, we use `alcohol.csv` as a sample dataset, convert it to a `.db` file. Then, we create a new toy dataset call `toyDB.db` and combin these two datasets. 

## Workflow
![Workflow](workflow.png)

## Preparation
1. Create: create a new codespaces with all required packages loaded.   
2. Extract data `make extract`: Extract `alcohol.csv` data from the url.     
3. Transform and load data `make transform_load`.

## Complex SQL Code
```
SELECT a.country,
    SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
    AS total_alcohol_consumption
FROM default.alcoholDB AS a
INNER JOIN default.toyDB AS t ON a.id = t.id
GROUP BY a.country
ORDER BY total_alcohol_consumption DESC
LIMIT 10
```
This is a SQL query that selects data from two tables, "alcoholDB" and "toyDB," and calculates the total alcohol consumption for each country based on the sum of beer_servings, spirit_servings, and wine_servings. The query then orders the results in descending order of total alcohol consumption and limits the output to the top 10 rows.

## Expected Output


|country|total_alcohol_consumption|
|:--:|:------------:|:----:|
|1|Andorra|695|
|2|Grenada|665|
|3|Czech Republic|665|
|4|France|648|
|5|Lithuania|643|
|6|Luxembourg|640|
|7|Germany|638|
|8|Hungary|634|
|9|Ireland|596|
|10|Belgium|591|


## Actions 
1. **Format**: `make format`    
2. **Lint**: `make lint`
3. **Test**: `make test`
4. **extract**: `make extract`
5. **transform_load**: `make transform_load`
6. **query**: `make transform_load`

## Reference
1. https://github.com/databricks/databricks-sql-python
2. https://github.com/nogibjj/cloud-database-LAB
3. https://learn.microsoft.com/en-us/azure/databricks/sql/admin/create-sql-warehouse
