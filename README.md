# Simple rasa bot

This is a simple console rasa bot configuration made using [rasa quickstart](https://rasa.com/docs/core/quickstart/).

## Usage

* Initialize docker:

```sh
sudo docker-compose up
```

when appers `Attaching to rasa_rasa_1` means that the container is running.

* Access the container:

```sh
sudo docker ps
```

see the name of the container, probably `rasa_rasa_1`

Execute the runing container

```sh
sudo docker exec -it <container_name> bash
```

## RASA commands

* train nlu:

```sh
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

* Run locally:

```sh
python -m rasa_core.run -d models/dialogue
```

## Reference
[rasa quickstart](https://rasa.com/docs/core/quickstart/)
