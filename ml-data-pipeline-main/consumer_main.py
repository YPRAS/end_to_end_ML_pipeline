from src.kafka_consumer.json_consumer import consumer_using_sample_file

from src.constant import SAMPLE_DIR
import os
if __name__=='__main__':

    topics = os.listdir(SAMPLE_DIR)
    print(f'topics: [{topics}]')
    for topic in topics:
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        consumer_using_sample_file(topic="device_sensor_topic",file_path = sample_file_path)