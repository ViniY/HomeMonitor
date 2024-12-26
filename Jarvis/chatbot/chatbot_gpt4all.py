from gpt4all import GPT4All
import logging 



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
# Define a basic formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# Add the formatter to the handler
console_handler.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(console_handler)



def load_model(model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'):
    logger.info('Start loading model with name of : {}', model_name)
    if model_name:
        model = GPT4All(model_name)
    else:
        model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")# downloads / loads a 4.66GB LLM
    logger.info('Successfully load the model : {}', model_name)
    return model


# Main loop to keep the model running
if __name__ == "__main__":
    model = load_model()
    logger.info('model on running : {}')
    while(True):
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        with model.chat_session():
            print(model.generate(user_input, max_tokens=1024))