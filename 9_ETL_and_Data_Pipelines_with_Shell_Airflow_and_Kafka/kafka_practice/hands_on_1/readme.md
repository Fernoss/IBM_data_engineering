# Hands-on Lab: Working with streaming data using Kafka
## Objectives
  - Download and install Kafka
  - Start the Zookeeper server for Kafka metadata management
  - Start the Kafka message broker service
  - Create a topic
  - Start a producer
  - Start a consumer

## Download Kafka
    wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
## Extract
    tar -xzf kafka_2.12-2.8.0.tgz
## Start ZooKeeper server
    cd kafka_2.12-2.8.0
    bin/zookeeper-server-start.sh config/zookeeper.properties
  ZooKeeper, as of this version, is required for Kafka to work. ZooKeeper is responsible for the overall management of Kafka cluster. 
  It monitors the Kafka brokers and notifies Kafka if any broker or partition goes down, or if a new broker or partition goes up.
## Start Kafka broker service
    # open new terminal
    cd kafka_2.12-2.8.0
    bin/kafka-server-start.sh config/server.properties
## Create a topic
    # open new terminal
    cd kafka_2.12-2.8.0
    bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092
## Start Producer
    # You need a producer to send messages to Kafka.
    bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092
  Once the producer starts, and you get the ‘>’ prompt, type any text message and press enter.
## Start Consumer
    # You need a consumer to read messages from Kafka
    # open new terminal
    cd kafka_2.12-2.8.0
    bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092
  You should see all the messages you sent from the producer appear here. You can go back to the producer terminal and type some more messages, one message per line, and you will see them appear here.



  
