from kafka import KafkaProducer
import gzip

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092'
    )

    json_file = open('./stream.jsonl', 'rb')
    for line in json_file:
        producer.send('messages', line)
