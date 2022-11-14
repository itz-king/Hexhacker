from Asuna import *
import logging
import Asuna.modules

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")

print("Bot Starting....")
asunaub.start()
asuna.start()
asunaub.run_until_disconnected()
asuna.run_until_disconnected()