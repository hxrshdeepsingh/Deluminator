import click
from .engine import sd
from .engine import pd

# Main
@click.group(help="⚡ Deluminator @v1.0")
def Deluminator():
    pass

@Deluminator.command()
@click.option('--host', required=True, type=str, help='Host for the server.')
@click.option('--port', required=True, type=int, help='Port for the server.')

# Server
def server(host, port):
    sd.main(host, port)

@Deluminator.command()
@click.option('--name', required=True, type=str, help='Name for the payload.')
@click.option('--host', required=True, type=str, help='Host for the payload.')
@click.option('--port', required=True, type=int, help='Port for the payload.')
@click.option('--time', required=True, type=int, help='Time for the payload.')

# Payload
def payload(name, host, port, time):
    pd.main(name, host, port, time)

if __name__ == '__main__':
    Deluminator()
