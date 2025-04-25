# Federated Learning-based Intrusion Detection System (IDS)

This project implements a **Federated Learning-based Intrusion Detection System (IDS)** to detect cybersecurity threats in a distributed environment. The system uses **Federated Learning** to collaboratively train machine learning models across multiple clients, all while keeping the data decentralized and private. The system is built using **Python**, **TensorFlow**, **Flower** for federated learning, and **Docker** for containerization.

### Key Technologies:
- **Federated Learning** (via **Flower**)
- **Python**
- **TensorFlow**
- **Docker** (for containerization)
- **Pipenv** (for dependency management)

## Project Structure

```
Federated-Learning-based-Intrusion-Detection-System-IDS/
├── 📁 config
│   └── docker-compose.yml               # Docker Compose configuration file
│
├── 📁 Docker
│   ├── Dockerfile.client                # Dockerfile for the client container
│   └── Dockerfile.server                # Dockerfile for the server container
│
├── 📁 data
│   ├── UNSW_NB15_training-set.csv       # Training dataset
│   └── UNSW_NB15_testing-set.csv        # Testing dataset
│
├── 📁 utils
│   ├── __init__.py                      # Makes the 'utils' folder a Python package
│   ├── data_loader.py                   # Data loading and preprocessing
│   ├── model_loader.py                  # Model creation and training functions
│   └── plot.py                          # Plotting the model architecture
│
├── 📄 .gitignore                        # Git ignore configuration
├── 📄 Pipfile                           # Pipenv environment definition
├── 📄 Pipfile.lock                      # Locked package versions
├── 📄 app.py                            # Main entry point for the application
├── 📄 client.py                         # Client-side logic for federated learning
├── 📄 server.py                         # Server-side logic for federated learning
├── 📄 model.png                         # Visualized model architecture
└── 📄 README.md                         # Project overview and setup instructions
```
## Installation

### Prerequisites

Ensure you have the following installed:
- **Docker**: For containerizing the application and managing environments.
- **Docker Compose**: For defining and running multi-container Docker applications.
- **Python 3.8+**: Required to run the code locally.
- **Pipenv**: For dependency management. Install it using:

   ```bash
   pip install pipenv
   ```

### Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Chukwuemeka-James/Fedeerated-Learning-based-Intrusion-Detection-System-IDS.git
   cd Federated-Learning-based-Intrusion-Detection-System-IDS
   ```

2. **Install Python dependencies using Pipenv**:
     ```bash
     pipenv install
     ```

## **Running the System:** There are three way `A, B, or C`

### A. Running Manually (Without Docker)

If you want to run the project manually (without Docker), you can follow these steps:

1. **Start the server**:
   In the terminal, navigate to the project directory and run:
   ```bash
   python server.py
   ```

2. **Start the clients**:
   Open separate terminals for each client and run the following commands:
   ```bash
   python client.py
   ```
   Repeat this for at `least three clients`, this is needed to satisfy the `min_fit_clients`, `min_evaluate_clients`, and `min_available_clients` configuration.. Each client will connect to the server and start the federated learning process.


### B. Running Manually **Flower Simulation** (With `app.py`)

   **Run the simulation**:
   To run the entire federated learning simulation, you can use:
   ```bash
   python app.py
   ```
   This script orchestrates the interactions between the server and the clients, simulating the federated learning process.
 
### C. Running with Docker

   To start the system with Docker and Docker Compose, follow these steps:

1. **Build and start the Docker containers**:
   ```bash
   docker-compose -f Config/docker-compose.yml up --build
   ```
   This will start the **server** container and **3 client containers** by default. Each client trains a local model on a portion of the data and then sends its model updates to the server for aggregation.

2. **Verify the system**:
   Once the containers are up, you can verify the system's operation by checking the logs and ensuring that the federated learning process is running as expected. The server container aggregates the model updates from the clients and creates a global model.


## Plotting the Model Architecture

To visualize the model architecture, the system generates a plot of the neural network structure and saves it in the `docs` folder. The plot is generated in the following file: `docs/model_plot.png`.

To plot the architecture, the function `plot_model_architecture` in `utils/plot.py` is used, which internally calls `plot_model` from **TensorFlow**:

   ```bash
   python utils/plot.py
   ```

This will generate a graphical representation of the model architecture, which can be useful for understanding the model's structure and layers.

## [Dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)

This project uses the **[UNSW-NB15 dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)**, a modern benchmark dataset for evaluating intrusion detection systems. It was created by the Cyber Range Lab of the Australian Centre for Cyber Security (ACCS) and contains realistic network traffic data. The dataset includes both **benign and malicious** records, with 49 features and 9 types of attacks such as **Fuzzers**, and **Exploits**  **Analysis**, **Backdoors**, **DoS (Denial of Service)**, **Generic**, **Reconnaissance**, **Shellcode**, and **Worms**. It provides a rich set of attributes for building effective machine learning models for cybersecurity tasks. It is split into two parts:

- **Training Data**: `data/UNSW_NB15_training-set.csv`
- **Testing Data**: `data/UNSW_NB15_testing-set.csv`

The data loader script (`utils/data_loader.py`) handles data preprocessing and loading.


### Finally: 

***Special thank to [salihardakizil](https://github.com/oqadiSAK) who inspired this work.***