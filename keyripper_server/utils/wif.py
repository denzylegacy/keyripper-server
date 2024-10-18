import bitcoinlib


def generate_wif(private_key):
    """Converts a private key to Wallet Import Format (WIF)."""
    key = bitcoinlib.keys.Key(private_key)
    return key.wif()
