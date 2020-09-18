import logging
import coloredlogs
import rasa

coloredlogs.install()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DOMAIN_FILE = "domain.yml"
NLU_FILE = "data/nlu.md"
STORIES_FILE = "data/stories.md"
CONFIG_FILE = "config.yml"
DATA_DICT = {
    "domain": DOMAIN_FILE,
    "nlu": NLU_FILE,
    "stories": STORIES_FILE,
    "config": CONFIG_FILE,
}

def train(data=DATA_DICT):
    rasa.train(
        domain=DOMAIN_FILE,
        config=CONFIG_FILE,
        training_files=[NLU_FILE, STORIES_FILE],
        # output=model_name,
    )

if __name__ == "__main__":
    train()
