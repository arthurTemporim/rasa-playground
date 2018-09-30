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

when appears `Attaching to rasa_rasa_1` means that the container is running.

* Access the container:

```sh
sudo docker ps
```

see the name of the container, probably `rasa_rasa_1`

Execute the running container

```sh
sudo docker exec -it <container_name> bash
```

Now you can run RASA commands in the container, and use any editor because
a volume is mapping the `bot/` directory to the container, and the changes
are updated automatically.

## RASA commands

* Train nlu:
```sh
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

* Train with using nlu examples
```sh
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

* Run locally:
```sh
python -m rasa_core.run -d models/dialogue
```

## References
[Quickstart](https://rasa.com/docs/core/quickstart/)
