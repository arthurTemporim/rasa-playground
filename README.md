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

## Reference
[rasa quickstart](https://rasa.com/docs/core/quickstart/)
