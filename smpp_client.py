import smpplib.client
import smpplib.consts
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Define server details
SMPP_SERVER = "127.0.0.1"
SMPP_PORT = 2775
SYSTEM_ID = "test"
PASSWORD = "password"

# Initialize the client
client = smpplib.client.Client(SMPP_SERVER, SMPP_PORT)

try:
    # Connect and bind
    client.connect()
    client.bind_transmitter(system_id=SYSTEM_ID, password=PASSWORD)

    # Send an SMS
    message = "Hello, SMPP Server!"
    client.send_message({
        'short_message': message.encode(),
        'source_addr_ton': smpplib.consts.SMPP_TON_ALNUM,
        'source_addr': "1234",
        'dest_addr_ton': smpplib.consts.SMPP_TON_INTERNATIONAL,
        'destination_addr': "567890",
        'esm_class': 0,
        'data_coding': smpplib.consts.SMPP_ENCODING_DEFAULT,
    })

    logging.info(f"Message sent: {message}")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    try:
        client.unbind()  # Attempt to unbind before disconnecting
    except smpplib.exceptions.PDUError:
        logging.warning("Client was not bound or already unbound.")

    client.disconnect()
    logging.info("SMPP client disconnected successfully")