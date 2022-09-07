# Creating and activating virtual environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Running docker-compose with docker-compose.yml
docker-compose up -d

# Waiting 10s for docker container to start
sleep 10
 
# Creating topic messages
 docker compose exec broker \
    kafka-topics --create \
    --topic messages \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1   

# Creating topic output
docker compose exec broker \
    kafka-topics --create \
    --topic output \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1

# Running producer.py and main.py
python3 producer.py
python3 main.py