import requests

question = input('Enter your question for ther magic 8 ball:')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

try:
    response = requests.get(magic_8_ball_url).json()
    print(response)
    answer = response['magic'] ['answer']
    print(f'The magic 8 ball says....  {answer}')
except Exception as e:
    print(e)
    print('Sorry, cant not contact the magic 8 ball right now')