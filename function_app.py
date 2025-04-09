import azure.functions as func
import logging
import cryptography

app = func.FunctionApp()

@app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="mysbqueue",
                               connection="SERVICE_BUS_CONNECTION") 
def servicebus_queue_trigger(azservicebus: func.ServiceBusMessage):
    logging.info('Python ServiceBus Queue trigger processed a message: %s',
                azservicebus.get_body().decode('utf-8'))
