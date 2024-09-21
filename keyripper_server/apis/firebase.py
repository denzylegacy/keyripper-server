# -*- coding: utf-8 -*-

from typing import Union
import json
import firebase_admin
from firebase_admin import credentials, db, initialize_app

from keyripper_server.infra import log, FIREBASE_URL, FIREBASE_API_KEY


class Firebase:
    """Class to manage connections and operations with Firebase Realtime Database."""

    @staticmethod
    def firebase_launcher(_credentials: credentials.Certificate) -> None:
        """Initializes the Firebase app if it's not already initialized."""
        if not firebase_admin._apps:
            initialize_app(
                _credentials, {"databaseURL": FIREBASE_URL}
            )

    def __init__(self) -> None:
        self.default_entry_ensurer("root", {"successful_connection_phrase": "Hello, world!"})

    def firebase_connection(self, reference_path: str) -> Union[db.Reference, None]:
        """
        Connects to the Firebase Database and returns a reference to the specified path.
        
        Args:
            reference_path (str): The reference path in the Firebase Realtime Database.
        
        Returns:
            Union[db.Reference, None]: Returns the Firebase reference or None if an error occurs.
        """
        try:
            if FIREBASE_API_KEY:
                self.firebase_launcher(credentials.Certificate(json.loads(FIREBASE_API_KEY)))
            else:
                self.firebase_launcher(
                    credentials.Certificate(
                        r"keyripper_server/apis/c18de10c13.json"
                    )
                )

            return db.reference(reference_path)
        except Exception as e:
            log.error(f"Error establishing Firebase connection: {e}")
            return None

    def default_entry_ensurer(self, reference_path: str, default_data: dict) -> None:
        """
        Check if the initial key in Firebase exists, and if not, creates it with default data.
        
        Args:
            reference_path (str): The reference path of the initial key to be validated.
            default_data (dict): Default data to initialize the key if it does not exist.
        """
        try:
            ref = self.firebase_connection(reference_path)
            if ref is not None:
                ref.set(default_data)
                log.info(f"Initial key '{reference_path}' created with default data.")
            else:
                print("refrefref", ref)
                log.info(f"Initial key '{reference_path}' already exists in Firebase.")
        except Exception as e:
            log.error(f"Error validating or creating initial key in Firebase: {e}")


if __name__ == "__main__":
    firebase = Firebase()
    
    firebase.default_entry_ensurer("root", {"successful_connection_phrase": "Hello, world!"})
