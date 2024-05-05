the bin/windows is basically inside the extracted folder. on linux its just bin/zooke.... no windows

./bin/windows/zookeeper-server-start.bat config/zookeeper.properties
./bin/windows/kafka-server-start.bat config/server.properties
./bin/windows/kafka-topics.bat --bootstrap-server localhost:9092 --topic NeaveTopic --create
./bin/windows/kafka-console-producer.bat --topic NeaveTopic --bootstrap-server localhost:9092
./bin/windows/kafka-console-consumer.bat --topic NeaveTopic --from-beginning --bootstrap-server localhost:9092
