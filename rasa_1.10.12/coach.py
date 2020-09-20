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
        domain=data["domain"],
        config=data["config"],
        training_files=[data["nlu"], data["stories"]],
        # This line is commented to use default way to name models
        # output=model_name,
    )

if __name__ == "__main__":
    train()
