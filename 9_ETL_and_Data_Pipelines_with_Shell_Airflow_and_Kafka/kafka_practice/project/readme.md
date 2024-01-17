# Kafka Python Client

Kafka has a distributed client-server architecture. For the server side, Kafka is a cluster with many
associated servers called broker, acting as the event broker to receive, store, and distribute events. All those brokers are managed by another distributed system called ZooKeeper to ensure all
brokers work in an efficient and collaborative way.

Kafka uses a TCP based network communication protocol to exchange data between clients and servers

For the client side, Kafka provides different types of clients such as: - Kafka CLI, which is a collection of shell scripts to communicate with a Kafka server - Many high-level programming APIs such as Python, Java, and Scala - REST APIs - Specific 3rd party clients made by the Kafka community

###kafka-python### is a Python client for the Apache Kafka distributed stream processing system, which aims
to provide similar functionalities as the main Kafka Java client.

With ###kafka-python###, you can easily interact with your Kafka server such as managing topics, publish, and consume
messages in Python programming language.

Note: Code snippets provided in this article are just for your reference but not the complete working code.

## Install

        pip install kafka-python

## Class

### KafkaAdminClient

The main purpose of KafkaAdminClient class is to enable fundamental administrative management operations
on kafka server such as creating/deleting topic, retrieving, and updating topic configurations and so on.

### Create new topics

Next, the most common usage of admin_client is managing topics such as creating and deleting topics.
Create empty topic list
Then we use the NewTopic class to create a topic with name equals bankbranch,
partition nums equals to 2, and replication factor equals to 1.

### Describe a topic

Once new topics are created, we can easily check its configuration details using describe_configs()
method

## KafkaProducer

Now we have a new bankbranch topic created, we can start produce messages to the topic.

For ###kafka-python###, we will use ###KafkaProducer### class to produce messages.
Since many real-world message values are in the format of JSON, we will show you how to publish JSON messages as an example.

Since Kafka produces and consumes messages in raw bytes, we need to encode our JSON messages and serialize them
into bytes.

For the ###value_serializer### argument, we define a lambda function to take a Python dict/list object and
serialize it into bytes.

Then, with the KafkaProducer created, we can use it to produce two ATM transaction messages in JSON format.

## KafkaConsumer

In the previous step, we published two JSON messages. Now we can use the KafkaConsumer class to
consume them.

We just need to define and create a ###KafkaConsumer### subscribing to the topic bankbranch.

Once the consumer is created, it will receive all available messages from the topic bankbranch. Then we
can iterate and print them
