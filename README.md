# keyripper-server
 A server that manages and distributes blocks of private key ranges. It works with a Rust-based client that performs the key search operations on the secp256k1 elliptic curve.

## Prerequisites

Before starting, make sure Python 3.10 or later is installed on your machine. If Python is not installed, follow the instructions [here](https://www.python.org/downloads/).

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/denzylegacy/keyripper-server.git
   cd keyripper-server
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

After installing the dependencies, run the main script using the following command:

```bash
python app.py
```

This command will start the project and run the main script `app.py`.

## Contributions

Feel free to open issues or pull requests. Feedback is always welcome!
