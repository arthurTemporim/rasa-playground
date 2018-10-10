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

* Runing the bot in console simply:

```sh
python -m rasa_core.run -d models/dialogue -u models/current/nlu
```

* Runing with API enabled:

```sh
python -m rasa_core.run --enable_api -d models/dialogue/ -u models/current/nlu/
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

### RASA API script

* While building a bot you will realise the need to understand the changes 
made in `intents`, `stories`, `epochs` ammounts, etc. Thinking in it, i
created a script that returns some importants data to understand
the changes that you made cause in your bot.

#### Usage

* Running the script:

```sh
python scripts/api.py
```

* Script result:

```
--------------------------------------------------
['Utter: ', 'action_listen']
['User Message: ', 'hi']
['Intent: ', 'greet']
['Confidence: ', 0.959172785282135]
--------------------------------------------------
['Utter: ', 'utter_greet']
['Utter: ', 'action_listen']
['User Message: ', 'good']
['Intent: ', 'mood_great']
['Confidence: ', 0.9660112261772156]
--------------------------------------------------
['Utter: ', 'utter_happy']
['Utter: ', 'action_listen']
['User Message: ', 'hi']
['Intent: ', 'greet']
['Confidence: ', 0.959172785282135]
--------------------------------------------------
['Utter: ', 'utter_greet']
['Utter: ', 'action_listen']
['User Message: ', 'bad']
['Intent: ', 'mood_unhappy']
['Confidence: ', 0.9680836796760559]
--------------------------------------------------
['Utter: ', 'utter_cheer_up']
['Utter: ', 'utter_did_that_help']
['Utter: ', 'action_listen']
['User Message: ', 'yes']
['Intent: ', 'mood_affirm']
['Confidence: ', 0.9524214863777161]
--------------------------------------------------
['Utter: ', 'utter_happy']
['Utter: ', 'action_listen']
['User Message: ', 'hi']
['Intent: ', 'greet']
['Confidence: ', 0.959172785282135]
--------------------------------------------------
['Utter: ', 'utter_greet']
['Utter: ', 'action_listen']
['User Message: ', 'bad']
['Intent: ', 'mood_unhappy']
['Confidence: ', 0.9680836796760559]
--------------------------------------------------
['Utter: ', 'utter_cheer_up']
['Utter: ', 'utter_did_that_help']
['Utter: ', 'action_listen']
['User Message: ', 'no']
['Intent: ', 'mood_deny']
['Confidence: ', 0.9748631715774536]
--------------------------------------------------
['Utter: ', 'utter_goodbye']
['Utter: ', 'action_listen']
```

## References
* [Quickstart](https://rasa.com/docs/core/quickstart/)
* [Api Tracker](https://rasa.com/docs/core/api/tracker/)
* [Debugging RASA](https://rasa.com/docs/core/debugging/)
* [Synonyms](https://rasa.com/docs/nlu/0.13.6/dataformat/)
