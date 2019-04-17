# The new RASA!

* Install the new rasa pip package, the version used here is the latest from 
**04/16/2019** and is a **pre-release** (`rasa==0.14.0a9`):

```sh
pip install -r requirements.txt
```

* Now the **Magic** begins! Rasa will help you to create your bot! Use the
command `rasa init` to start the magic show:

```sh
rasa init

Welcome to Rasa! 🤖

To get started quickly, I can assist you to create an initial project.
If you need some help to get from this template to a bad ass contextual assistant, checkout our quickstart guidehere: https://rasa.com/docs/core/quickstart

Now let's start! 👇
```

* As you can see, this script will help you with questions to configure
and create your **Rasa chatbot**:

```sh
? Please enter a folder path where I should create the initial project [default: current directory] .
```

```sh
? Directory '/home/arthur/Repositories/arthur/rasa_playground/rasa-stack' is not empty. Continue?  Yes
Created project directory at '/home/arthur/Repositories/arthur/rasa_playground/rasa-stack'.
Your bot is ready to go!
```

* After the step above, all the basic files will be generated, we can check
it:

```sh
ls
actions.py  credentials.yml  domain.yml     __init__.py  README.md
config.yml  data             endpoints.yml  __pycache__  requirements.txt
```

* But not stops there, **Rasa** will help you to  train your new first bot!

```sh
? Do you want me to train an initial model for the bot? 💪🏽  Yes
Processed Story Blocks: 100%|██████████████████████████████████████████| 4/4 [00:00<00:00, 4131.30it/s, # trackers=1]
Processed Story Blocks: 100%|██████████████████████████████████████████| 4/4 [00:00<00:00, 2190.24it/s, # trackers=4]
Processed Story Blocks: 100%|██████████████████████████████████████████| 4/4 [00:00<00:00, 694.05it/s, # trackers=12]
Processed Story Blocks: 100%|██████████████████████████████████████████| 4/4 [00:00<00:00, 1042.06it/s, # trackers=7]
Processed actions: 14it [00:00, 13210.41it/s, # examples=14]
2019-04-16 23:24:48.019510: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
masking (Masking)            (None, 5, 19)             0
_________________________________________________________________
lstm (LSTM)                  (None, 32)                6656
_________________________________________________________________
dense (Dense)                (None, 13)                429
_________________________________________________________________
activation (Activation)      (None, 13)                0
=================================================================
Total params: 7,085
Trainable params: 7,085
Non-trainable params: 0
_________________________________________________________________
2019-04-16 23:24:48 INFO     rasa.core.policies.keras_policy  - Fitting model with 62 total samples and a validation split of 0.1
Epoch 1/100
62/62 [==============================] - 1s 11ms/step - loss: 2.5878 - acc: 0.0645
Epoch 2/100
62/62 [==============================] - 0s 229us/step - loss: 2.5454 - acc: 0.0806
Epoch 3/100
62/62 [==============================] - 0s 163us/step - loss: 2.5171 - acc: 0.1290
Epoch 4/100
```

* The output bellow is the end of the awesome `rasa init` command:

```sh
Epoch 99/100
62/62 [==============================] - 0s 95us/step - loss: 0.7322 - acc: 0.8387
Epoch 100/100
62/62 [==============================] - 0s 91us/step - loss: 0.7824 - acc: 0.8387
2019-04-16 23:24:50 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2019-04-16 23:24:50 INFO     rasa.core.agent  - Persisted model to '/tmp/tmpy4bslp1g/core'
2019-04-16 23:24:50 WARNING  rasa_nlu.config  - You have specified the pipeline template 'tensorflow_embedding' which has been renamed to 'supervised_embeddings'. Please update your code as it will no longer work with future versions of Rasa NLU.
2019-04-16 23:24:50 INFO     rasa_nlu.training_data.loading  - Training data format of /tmp/tmpv2z4z6_w/fdfdefcdcdd546bb946534fcac7a9a83_nlu.md is md
2019-04-16 23:24:50 INFO     rasa_nlu.training_data.training_data  - Training data stats:
	- intent examples: 39 (6 distinct intents)
	- Found intents: 'goodbye', 'mood_great', 'greet', 'mood_affirm', 'mood_deny', 'mood_unhappy'
	- entity examples: 0 (0 distinct entities)
	- found entities:

2019-04-16 23:24:50 INFO     rasa_nlu.model  - Starting to train component WhitespaceTokenizer
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Finished training component.
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Starting to train component RegexFeaturizer
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Finished training component.
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Starting to train component CRFEntityExtractor
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Finished training component.
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Starting to train component EntitySynonymMapper
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Finished training component.
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Starting to train component CountVectorsFeaturizer
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Finished training component.
2019-04-16 23:24:50 INFO     rasa_nlu.model  - Starting to train component EmbeddingIntentClassifier
2019-04-16 23:24:51 INFO     rasa_nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|██████████████████████████████████████████████| 300/300 [00:00<00:00, 315.27it/s, loss=0.096, acc=1.000]
2019-04-16 23:24:52 INFO     rasa_nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.096, train accuracy=1.000
2019-04-16 23:24:52 INFO     rasa_nlu.model  - Finished training component.
2019-04-16 23:24:52 INFO     rasa_nlu.model  - Successfully saved model into '/tmp/tmpy4bslp1g/nlu'
Train path: '/tmp/tmpy4bslp1g'.
Your bot is trained and ready to take for a spin!
? Do you want to speak to the trained bot on the command line? 🤖  No
Ok 👍🏼. If you want to speak to the bot later, change into the project directory and run 'rasa shell'.
```

* As we can see, now we have all the files and configurations needed to
start the development of your chatbot. The folder `models` was created
too so you are able to run your new chatbot:

```sh
ls
actions.py  credentials.yml  domain.yml     __init__.py  __pycache__  requirements.txt
config.yml  data             endpoints.yml  models       README.md
```

* Ok, now you need to now 2 things:

1. type `rasa` in your terminal
2. type `-h`, so will be `rasa -h`

And that's it, with this command you have all you know about the new rasa!
If you are not beliving, you can see the ouput:

```sh
rasa -h
usage: rasa [-h] [--version]
            {init,run,shell,train,interactive,test,show,data,up} ...

Rasa command line interface. Rasa allows you to build your own conversational
assistants 🤖. The 'rasa' command allows you to easily run most common commands
like creating a new bot, training or evaluating models.

positional arguments:
  {init,run,shell,train,interactive,test,show,data,up}
                        Rasa commands
    init                Create a new project from a initial_project
    run                 Start a Rasa server which loads a trained model
    shell               Speak to a trained model on the command line
    train               Train the Rasa bot
    interactive         Teach the bot with interactive learning
    test                Test a trained model
    show                Visualize Rasa Stack data
    data                Utils for the Rasa training files
    up                  Run the Rasa Interface

optional arguments:
  -h, --help            show this help message and exit
  --version             Print installed Rasa version
```

* Ok, but if you want to use the comand `rasa run` and you don't know
how to use it? Try this:

```sh
rasa run -h
usage: rasa run [-h] [-v] [-vv] [--quiet] [-p PORT] [--auth_token AUTH_TOKEN]
                [--cors [CORS [CORS ...]]] [--enable_api] [-o LOG_FILE]
                [-c CONNECTOR] [--endpoints ENDPOINTS]
                [--jwt_secret JWT_SECRET] [--jwt_method JWT_METHOD] [-m MODEL]
                [--credentials CREDENTIALS]
                [model-as-positional-argument] {core,nlu,actions} ...

positional arguments:
  model-as-positional-argument
                        Path to a trained Rasa model. If a directory is
                        specified, it will use the latest model in this
                        directory. (default: None)
  {core,nlu,actions}
    core                Run a trained Core model
    nlu                 Run a trained NLU model
    actions             Run the action server

optional arguments:
  -h, --help            show this help message and exit
  -o LOG_FILE, --log_file LOG_FILE
                        store log file in specified file (default:
                        rasa_core.log)
  --endpoints ENDPOINTS
                        Configuration file for the connectors as a yml file
                        (default: None)
  -m MODEL, --model MODEL
                        Path to a trained Rasa model. If a directory is
                        specified, it will use the latest model in this
                        directory. (default: models)
  --credentials CREDENTIALS
                        Authentication credentials for the connector as a yml
                        file (default: credentials.yml)

Python Logging Options:
  -v, --verbose         Be verbose. Sets logging level to INFO (default: 20)
  -vv, --debug          Print lots of debugging statements. Sets logging level
                        to DEBUG (default: None)
  --quiet               Be quiet! Sets logging level to WARNING (default:
                        None)

Server Settings:
  -p PORT, --port PORT  port to run the server at (default: 5005)
  --auth_token AUTH_TOKEN
                        Enable token based authentication. Requests need to
                        provide the token to be accepted. (default: None)
  --cors [CORS [CORS ...]]
                        enable CORS for the passed origin. Use * to whitelist
                        all origins (default: None)
  --enable_api          Start the web server api in addition to the input
                        channel (default: False)

Channels:
  -c CONNECTOR, --connector CONNECTOR
                        service to connect to (default: None)

JWT Authentication:
  --jwt_secret JWT_SECRET
                        Public key for asymmetric JWT methods or shared
                        secretfor symmetric methods. Please also make sure to
                        use --jwt_method to select the method of the
                        signature, otherwise this argument will be ignored.
                        (default: None)
  --jwt_method JWT_METHOD
                        Method used for the signature of the JWT
                        authentication payload. (default: HS256)
```

* That's it, everything more easier!

* Let's try something:

```sh
rasa run --enable_api
'None' not found. Using default location 'endpoints.yml' instead.
2019-04-16 23:54:52 INFO     root  - Starting Rasa Core server on http://localhost:5005
[2019-04-16 23:54:52 -0300] [6127] [INFO] Goin' Fast @ http://0.0.0.0:5005
2019-04-16 23:54:52 INFO     sanic.root  - Goin' Fast @ http://0.0.0.0:5005
2019-04-16 23:54:52.411889: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-04-16 23:54:52 INFO     tensorflow  - Restoring parameters from /tmp/tmp7kf30dmc/nlu/component_5_EmbeddingIntentClassifier.ckpt
[2019-04-16 23:54:53 -0300] [6127] [INFO] Starting worker [6127]
2019-04-16 23:54:53 INFO     sanic.root  - Starting worker [6127]
```

* And now let's send a message to our bot:

```sh
curl -XPOST localhost:5005/conversations/default/respond -d '{"query":"Hello"}'
```

* The Answer:

```sh
[{"recipient_id":"default","text":"Hey! How are you?"}]
```


## Final Considerations

Thank you for reading this simple example of what Rasa will bring to us in
the next days and weeks, i hope you like it!

Fell free to comment, Fork and leave comments in issues or some other ways.
Thank you very much!
