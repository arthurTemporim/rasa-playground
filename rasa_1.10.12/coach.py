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
        domain=DATA_DICT["domain"],
        config=DATA_DICT["config"],
        training_files=[DATA_DICT["nlu"], DATA_DICT["stories"]],
        # This line is commented to use default way to name models
        # output=model_name,
    )

if __name__ == "__main__":
    train()
