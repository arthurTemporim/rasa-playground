train_1:
	python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue

train_2:
	python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

run_intent:
	python -m rasa_core.run -d models/dialogue

run_api:
	python -m rasa_core.run --enable_api -d models/dialogue/ -u models/current/nlu/
