from llm import create_llm

history = []

while True:
    user_question = input('User: ')
    if user_question.lower() == 'quit':
        break
    answer = create_llm(user_question, history)
    print(f'Assistant: {answer}')

    history.append(f'User: {user_question}')
    history.append(f'Assistant: {answer}')