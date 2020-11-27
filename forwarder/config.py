from auto_forwarder.sample_config import Config


class Development(Config):
    API_KEY = "1404188198:AAGRUjFdVHIOlS98O5_7SOLbmFOAf95sJZc"  # Your bot API key
    OWNER_ID = 1400548428  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001251125753]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001467098472]  # List of chat id's to forward messages to.
    
    WORKERS = 4