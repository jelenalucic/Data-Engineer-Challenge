from kafka import KafkaProducer
import gzip

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092'
    )

    # Uncomment the following line of code if you're using stream.jsonl.gz instead of unzipped version
    # and comment out the line after that
    # with gzip.open('./stream.jsonl.gz', 'rb') as json_file:
    
    json_file = open('./stream.jsonl', 'rb')
    for line in json_file:
        producer.send('messages', line)
