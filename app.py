import os
import flwr as fl
import client
from server import get_server_strategy

# Make tensorflow log less verbose
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define Flower app entry point
def main():
    fl.simulation.simulation_app(
        client_fn=create_client,
        num_clients=3,
        config=fl.server.ServerConfig(num_rounds=3),
        strategy=get_server_strategy(),
    )

def create_client(cid: str) -> fl.client.Client:
    return client.Client()

# Required function for flwr run to discover
app = main
