# General
In this knowledge-packed module, you’ll explore general and reference enterprise data warehousing architecture. 
You’ll discover how data cubes relate to star schemas. Then you’ll learn how to slice, dice, drill up or down, 
roll up, and pivot relative to data cubes. Next, you will examine the capabilities of materialized views, their 
benefits, and how to apply them. You’ll learn how data organization using facts and dimensions and their related 
tables organizes information. Then, you will explore how to use normalization to create a snowflake schema as 
an extension of the star schema. You will learn about populating a data warehouse, incremental data updates, 
verifying data, querying data, interpreting an entity-relationship diagram for a star schema, creating a materialized 
view, and applying the CUBE and ROLLUP options. ​You’ll also discover how organizations can benefit by implementing staging.

## Learning Objectives
- Describe a general data warehousing architecture and its component layers and distinguish between general and reference enterprise data warehouse architecture.
- Describe the relationship of a data cube to a star schema and describe the actions of slice, dice, drill up or down, roll up, and pivot as they relate to data cubes.
- Describe materialized views and recall two use cases for them.
- Create a star schema using fact and dimension tables.
- Build a data warehouse staging area.
- Verify data quality for a data warehouse.
- List the main steps for populating a data warehouse​, describe methods for change detection and incremental loading, and manually create and populate tables for a sales star schema.
- Interpret an entity-relationship diagram for a star schema.
- Write queries using grouping sets, rollups, cubes.
- Create a materialized query table (MQT).

## mytest.py
The testing framework provides the following tests:
- check_for_nulls - this test will check for nulls in a column
- check_for_min_max - this test will check if the values in a column are with a range of min and max values
- check_for_valid_values - this test will check for any invalid values in a column
- check_for_duplicates - this test will check for duplicates in a column

Each test can be authored by mentioning a minimum of 4 parameters.

- testname - The human readable name of the test for reporting purposes
- test - The actual test name that the testing micro framework provides
- table - The table name on which the test is to be performed
- column - The table name on which the test is to be performed
