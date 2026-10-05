from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create a TCP socket and connect to the mail server.
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    try:
        recv = clientSocket.recv(1024).decode()

        # Send HELO and receive the server's reply.
        heloCommand = 'HELO Alice\r\n'
        clientSocket.sendall(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()

        # Specify the sender.
        clientSocket.sendall('MAIL FROM:<alice@example.com>\r\n'.encode())
        recv2 = clientSocket.recv(1024).decode()

        # Specify the recipient.
        clientSocket.sendall('RCPT TO:<bob@example.com>\r\n'.encode())
        recv3 = clientSocket.recv(1024).decode()

        # Request permission to send the message data.
        clientSocket.sendall('DATA\r\n'.encode())
        recv4 = clientSocket.recv(1024).decode()

        # Send the message without waiting for a reply between data and endmsg.
        clientSocket.sendall(msg.encode())
        clientSocket.sendall(endmsg.encode())
        recv5 = clientSocket.recv(1024).decode()

        # End the SMTP session and receive the goodbye reply.
        clientSocket.sendall('QUIT\r\n'.encode())
        recv6 = clientSocket.recv(1024).decode()
    finally:
        clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
