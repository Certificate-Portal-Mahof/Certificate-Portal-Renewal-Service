import os
import threading

from db.db import MongoConnector


def certificate_renewal():
    pass


def start_certificate_renewal():
    expiry_check_thread = threading.Thread(target=certificate_renewal)
    expiry_check_thread.daemon = True
    expiry_check_thread.start()


def main():
    try:
        MongoConnector().init(mongodb_uri=os.getenv("MONGODB_URI"), db_name=os.getenv("DB_NAME"))
        start_certificate_renewal()
    finally:
        MongoConnector().close_connection()


if __name__ == "__main__":
    main()
