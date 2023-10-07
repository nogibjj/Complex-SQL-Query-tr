```sql
SELECT * FROM alcoholDB;
```

```sql
SELECT * FROM alcoholDB;
```

```sql
DELETE FROM alcoholDB WHERE id=10;
```

```sql
UPDATE alcoholDB SET 
        country=country_A, 
        beer_sevringst=
        10,
        spirit_servings=10, 
        wine_servings=10, 
        total_pure_alcohol=10,
        WHERE id=3;
```

```sql
DELETE FROM alcoholDB WHERE id=1;
```

```sql
UPDATE alcoholDB SET 
        country=country_A, 
        beer_sevringst=
        1,
        spirit_servings=1, 
        wine_servings=1, 
        total_pure_alcohol=1.1,
        WHERE id=1000;
```

```sql
SELECT * FROM alcoholDB;
```

```sql
Complex Query
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql
SELECT a.country, SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption FROM default.alcoholDB AS a INNER JOIN default.toyDB AS t ON a.id = t.id GROUP BY a.country ORDER BY total_alcohol_consumption DESC LIMIT 10;
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql
SELECT a.country, SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption FROM default.alcoholDB AS a INNER JOIN default.toyDB AS t ON a.id = t.id GROUP BY a.country ORDER BY total_alcohol_consumption DESC LIMIT 10;
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='Grenada', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
                AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='Grenada', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
                AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='Grenada', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql
SELECT a.country, SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption FROM default.alcoholDB AS a INNER JOIN default.toyDB AS t ON a.id = t.id GROUP BY a.country ORDER BY total_alcohol_consumption DESC LIMIT 10;
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
                AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
                AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql
SELECT a.country, SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption FROM default.alcoholDB AS a INNER JOIN default.toyDB AS t ON a.id = t.id GROUP BY a.country ORDER BY total_alcohol_consumption DESC LIMIT 10;
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
                AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

```sql

            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) 
                AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            
```

```response from databricks
[Row(country='Andorra', total_alcohol_consumption=695), Row(country='Grenada', total_alcohol_consumption=665), Row(country='Czech Republic', total_alcohol_consumption=665), Row(country='France', total_alcohol_consumption=648), Row(country='Lithuania', total_alcohol_consumption=643), Row(country='Luxembourg', total_alcohol_consumption=640), Row(country='Germany', total_alcohol_consumption=638), Row(country='Hungary', total_alcohol_consumption=634), Row(country='Ireland', total_alcohol_consumption=596), Row(country='Belgium', total_alcohol_consumption=591)]
```

