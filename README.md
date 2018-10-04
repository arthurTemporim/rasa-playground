# Simple rasa bot

This is a simple console rasa bot configuration made using [RASA quickstart](https://rasa.com/docs/core/quickstart/).

## Usage

I create a docker to run the rasa comands, so is not necessary to use
a virtualenv or install in your pc the rasa configurations, just follow
this topic and you will have a docker runing to use rasa commands.

* Initialize docker:

```sh
sudo docker-compose up
```

when appears `Attaching to rasa_playground_rasa_1` means that the container is running.

* Access the container:

```sh
sudo docker ps
```

see the name of the container, probably `rasa_playground_rasa_1`

Execute the running container

```sh
sudo docker exec -it <container_name> bash
```

Now you can run RASA commands in the container, and use any editor because
a volume is mapping the `bot/` directory to the container, and the changes
are updated automatically.

## RASA commands

* Train a Dialogue Model:

This will train the dialogue model and store it into models/dialogue

```sh
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

* Train with using nlu examples:

```sh
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

* Directly sending in the intents in the domain:

To try the bot in this mode is needed to call the intents directly, like: `/greet` or `/goodby`

```sh
python -m rasa_core.run -d models/dialogue
```

### Other ways to run

* Runing the bot in console simply:

```sh
python -m rasa_core.run -d models/dialogue -u models/current/nlu
```

* Runing with API enabled and using log file:

```sh
python -m rasa_core.run --enable_api -d models/dialogue/ -u models/current/nlu/ -o out.log
```

### Using RASA API

* Post a message to bot API:

```sh
curl -XPOST localhost:5005/conversations/default/respond -d '{"query":"Hello"}'
```

* Show track information about the bot execution like `confidence`, `timestamp` and `intent` data.
```sh
curl http://localhost:5005/conversations/default/tracker
```
### Script

```sh
python scripts/api.py
```

## References
[Quickstart](https://rasa.com/docs/core/quickstart/)
