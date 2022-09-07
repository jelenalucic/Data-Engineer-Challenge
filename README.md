# Data Engineer Challenge
 This challenge is done as a part of recruitment process. The goal of the challenge is to have a tool to stream data from `kafka` and counting unique users per minute.


# How to run with Docker

 - Download GitHub repository
 - Open Terminal and change directory to the downloaded GitHub repository
 - Run the application in Terminal with command ./run.sh
 - run.sh will 
		 - activate virtual environment `venv`
		 - download and install needed Python packages
		 - create docker container using `docker-compose.yml` file
		 - create two topics named `messages` and `output`
		 - runs producer.py which creates one producer that writes data from the sample into `messages` topic
		 - runs main.py which creates one consumer and one producer that reads from topic `messages` and outputs the results to topic 'output'

# How to run locally
- Create project in PyCharm, VSCode or IDE of your choice. However, you need to active virtual environment, and it is created by default when you create a project in PyCharm or you can activate it using the following commands in terminal:
	> python3 -m venv venv 

	>source venv/bin/activate
- The next step includes installing dependencies which are quoted in the `requirements.txt` file, and this is done using the following two commands: 
	> pip install --upgrade pip

	>  pip install -r requirements.txt
- Afterwards, create two topics -`messages` and `output`. Make sure you have `kafka` and `zookeper` running. You can create topics using commands listed below:
	>kafka-topics.sh --bootstrap-server localhost:9092 --topic messages --create --partitions 1 --replication-factor 1
	
	>kafka-topics.sh --bootstrap-server localhost:9092 --topic output --create --partitions 1 --replication-factor 1
- Finally, run producer.py and then run main.py file. 

# The results

The solution gives us information about how many unique users are processed in each minute. Also, we have insight into how many messages are being processed per minute to assess the efficiency of the dataflow.

The throughput could be improved by increasing the number of producers and consumers, creating them with multiple partitions.

When counting the number of unique users, `set` data structure is being used, since it stores unique elements of the same type, and therefore no `user_id` duplicates are found.

When creating a statistic, e.g. per minute, with frames arriving late we can use a `priority queue` data structure. Consumer puts all the upcoming messages in that priority queue, and on each 5.0 seconds (which is the maximum latency for 99.9% of the frames) producer sends all the messages to the `output` topic. Priority queue ensures that all the elements are sorted ascending by the `timestamp` property.


