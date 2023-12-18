# Accessing Databases with SQL magic🪄

In this hands-on tutorial, you will create a table, insert some data, 
and retrieve the results using the SQLite database with python🐍

**Objectives**
Perform simplified database access using SQL "magic"

**Snippet**:

```python
country = "Canada"
%sql select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = :country
```

