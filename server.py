import smpplib
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Define a function to handle bind requests
def on_bind(connection):
    logging.info(f"Client bound: {connection.system_id}")
    return True  # Allow binding

# Define a function to handle incoming messages
def on_submit_sm(pdu, connection):
    logging.info(f"Received message: {pdu.short_message.decode()}")
    return pdu.create_response()

# Create an SMPP server instance
server = smpplib.server.SMPPServer(('0.0.0.0', 2775))  # Listening on port 2775

# Register event handlers
server.set_handler('bind_transmitter', on_bind)
server.set_handler('bind_receiver', on_bind)
server.set_handler('bind_transceiver', on_bind)
server.set_handler('submit_sm', on_submit_sm)

# Start the server
logging.info("Starting SMPP server on port 2775...")
server.serve_forever()