from hexhacker import *
import logging
import hexhacker.modules

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")

print("Bot Starting....")
hexhackerub.start()
hexhackerub.run_until_disconnected()
