import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Email Sender')

        # Create layout
        layout = QVBoxLayout()

        # Add email fields
        self.to_label = QLabel('To:')
        self.to_edit = QLineEdit()
        layout.addWidget(self.to_label)
        layout.addWidget(self.to_edit)

        self.subject_label = QLabel('Subject:')
        self.subject_edit = QLineEdit()
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_edit)

        self.message_label = QLabel('Message:')
        self.message_edit = QLineEdit()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_edit)

        # Add send button
        send_button = QPushButton('Send Email')
        send_button.clicked.connect(self.send_email)
        layout.addWidget(send_button)

        # Set layout
        self.setLayout(layout)

    def send_email(self):
        # Get email details
        to_email = self.to_edit.text()
        subject = self.subject_edit.text()
        message = self.message_edit.text()

        # Set up email message
        msg = MIMEMultipart()
        msg['From'] = 'your_email@gmail.com'  # Replace with your Gmail address
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('your_email@gmail.com', 'your_password')  # Replace with your Gmail address and password
        smtp_server.send_message(msg)
        smtp_server.quit()

        # Optional: Show confirmation message
        print("Email sent successfully.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailWindow()
    window.show()
    sys.exit(app.exec_())
