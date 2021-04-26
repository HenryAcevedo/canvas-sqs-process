import boto3
import time
import json
import re
import logging
from course_tabs import set_default_navigation

# Get the service resource
sqs = boto3.resource("sqs")

# Get the queue
queue = sqs.get_queue_by_name(QueueName="canvas-live-events-queue-name")

if __name__ == "__main__":
    acc = re.compile("xxxx0+")
    logging.basicConfig(
        filename="./logs/courses.log",
        filemode="a",
        format="%(asctime)s - %(message)s",
        level=logging.INFO,
        datefmt="%m/%d/%Y %I:%M:%S %p %Z",
    )

    while True:
        for message in queue.receive_messages():
            event = json.loads(message.body)
            course_id = re.sub(acc, "", event["body"]["course_id"])

            # Print out the body of the message
            logging.info(f"Starting {course_id}")
            set_default_navigation(course_id)
            logging.info(f"Finished {course_id}")

            # Let the queue know that the message is processed
            message.delete()
        time.sleep(2)
