# Rasa 1.2.2 


## API Usage

* `bot`:
```sh
rasa run -vv --enable-api -p 5005
```

* `actions`:
```sh
rasa run actions
```

### Rasa API HTTP requests

Check the [http-api documentation](https://rasa.com/docs/rasa/api/http-api)

* `tracker`:

```sh
curl http://localhost:5005/conversations/default/tracker
```

* `domain.yml`:

```sh
curl -X GET http://localhost:5005/domain \
            -H "Accept: application/json"
```

* `intent`:

```sh
curl -X POST http://localhost:5005/model/parse \
             -H 'Content-Type: application/json' \
             -d '{"text": "Hello!"}'
```

* Having a conversation with the chatbot:

```sh
curl -XPOST http://localhost:5005/webhooks/rest/webhook \
            -H 'Content-Type: application/json' \
            -d '{"sender":"default","message":"hello"}'
```

## Installation

Create a `python virtualenv`, and install the dependencies:

```sh
pip install -r requirements.txt
```

## References

* [rasa-ptbr-boilerplate](https://github.com/lappis-unb/rasa-ptbr-boilerplate)
