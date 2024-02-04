import pika, os

# Connection parameters
url = os.environ.get('CLOUDAMQP_URL', 'amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

# Message parameters
queue_name = 'exam'
message_body = "Hi CloudAMQP, this was fun!"
routing_key = 'b9485e2f-e3eb-41d1-b481-69e3ae477c26'
exchange_name = 'exchange.b9485e2f-e3eb-41d1-b481-69e3ae477c26'

# Declare exchange and queue, and bind them
channel.exchange_declare(exchange_name, exchange_type='direct', durable=True) # declare exchange
channel.queue_declare(queue_name, durable=True) # declare queue
channel.queue_bind(queue_name, exchange_name, routing_key) # create binding between queue and exchange

channel.basic_publish(
  body=message_body,
  exchange=exchange_name,
  routing_key=routing_key,
  properties=pika.BasicProperties(delivery_mode=2)
  )

# Delete exchange and bindings
channel.exchange_delete(exchange=exchange_name, if_unused=False)  # Force deletion

# Close connection
connection.close()

print(' Message sent.')
