import json
import os
import dialogflow_api
import sys


def main():
    if len(sys.argv) > 1:
        load_dotenv()
        GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID')

        file_with_training_phrases = sys.argv[1]

        with open(file_with_training_phrases) as file:
            train_data = json.load(file)

        print('[*] Обучение бота...')

        for intent_name, training_phrases in train_data.items():
            print(f'[*] {intent_name}...', end=' ')

            train_questions = training_phrases['questions']
            train_answer = training_phrases['answer']
            dialogflow_api.create_intent(GOOGLE_PROJECT_ID, intent_name, train_questions, train_answer)
            
            print('Ok.')

        print('[*] Бот готов к бою!')

    else:
        print('[*] Не указан путь к файлу с тренировочными фразами.')


if __name__ == '__main__':
    main()
    
