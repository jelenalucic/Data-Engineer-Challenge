import json
from threading import Timer

from kafka import KafkaConsumer
from kafka import KafkaProducer
from queue import PriorityQueue

priority_queue = PriorityQueue()

unique_user_ids = set()
all_user_ids = list()

minute_counter = 0


def count_number_of_unique_uids():
    global minute_counter
    minute_counter += 1

    print(f'Minute [{minute_counter}]: Number of consumed messages in a minute is {len(all_user_ids)}.')
    print(f'Minute [{minute_counter}]: Number of unique user ids in a minute is {len(unique_user_ids)}.\n')

    # Clear all user ids in each iteration
    all_user_ids.clear()
    unique_user_ids.clear()


def produce():
    for message in priority_queue.queue:
        producer.send('output', message[1])


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

producer_timer = RepeatingTimer(5.0, produce)
producer_timer.start()

counting_timer = RepeatingTimer(60.0, count_number_of_unique_uids)
counting_timer.start()

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    producer = KafkaProducer(
        bootstrap_servers='localhost:9092'
    )

    for message in consumer:
        value = json.loads(message.value)

        uid = value['uid']
        unique_user_ids.add(uid)
        all_user_ids.append(uid)

        timestamp = value['ts']
        priority_queue.put((timestamp, message.value))
