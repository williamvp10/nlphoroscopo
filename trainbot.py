from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter

data_json='./data/data.json'
config_file='config.json'
model_dir='./models/nlu'
name='horoscopebot'

def train_bot():
    training_data = load_data(data_json)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = name)

def predict_intent(text):
    dirr=model_dir+'/default/'+name
    interpreter = Interpreter.load(dirr)
    print(interpreter.parse(text))
    return interpreter.parse(text)