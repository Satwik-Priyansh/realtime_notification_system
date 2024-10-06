import asyncio
from aiosmtpd.controller import Controller
from email.message import EmailMessage

class DebuggingHandler:
    async def handle_DATA(self, server, session, envelope):
        # Parse the email content
        message = EmailMessage()
        message.set_payload(envelope.content)
        print(f"Received message from: {envelope.mail_from}")
        print(f"Message recipients: {envelope.rcpt_tos}")
        print(f"Message data:\n{envelope.content.decode('utf8', errors='replace')}")
        return '250 OK'

if __name__ == '__main__':
    controller = Controller(DebuggingHandler(), hostname='localhost', port=1025)
    controller.start()

    print("SMTP Debugging Server running on localhost:1025...")
    try:
        # Create a new event loop and set it as the current loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_forever()
    except KeyboardInterrupt:
        print("Stopping SMTP server...")
        controller.stop()