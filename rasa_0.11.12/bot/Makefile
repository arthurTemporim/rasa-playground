train:
	python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
	python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue --epochs 190

run_nlu_test:
	python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
	python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue --epochs 190
	python -m rasa_core.run -d models/dialogue/ -u models/current/nlu/ --debug --enable_api 

run_intent:
	python -m rasa_core.run -d models/dialogue

run:
	python -m rasa_core.run -d models/dialogue/ -u models/current/nlu/ --debug --enable_api 
