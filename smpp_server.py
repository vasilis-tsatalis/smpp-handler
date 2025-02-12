from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)


class SMPPServer(LineReceiver):
    def connectionMade(self):
        """Handle new connection"""
        logging.info(f"New connection from {self.transport.getPeer()}")

    def lineReceived(self, line):
        """Handle incoming data"""
        logging.info(f"Received: {line.decode()}")
        response = b"Message received"
        self.sendLine(response)

    def connectionLost(self, reason):
        """Handle connection lost"""
        logging.info(f"Connection lost: {reason}")


class SMPPServerFactory(Factory):
    def buildProtocol(self, addr):
        return SMPPServer()


# Run the server on port 2775
logging.info("Starting SMPP server on port 2775...")
reactor.listenTCP(2775, SMPPServerFactory())
reactor.run()