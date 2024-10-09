import tweepy
import keys

# Authentication
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

# Function to tweet
def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    # print("Tweeted successfully!")

# Opening the file that contains the variables
with open('variables.txt') as f:
    lines = f.readlines()
    variablesString = ' '.join(lines)
    variablesList = variablesString.split(' ')
    
# Sentences to be used
negativeSentences = ["Não", "Não!", "Não =(", "Nem", "Ainda não", "Pior que não", "Jamais", "Tampouco", "Também não", "Negativo", "De modo algum", "De jeito nenhum", "De maneira nenhuma", "No", "Nom", "Nein", "Nananinanão", "De forma alguma", "Hoje não"]

# Sentences management
sentenceOfTheDayIndex = int(variablesList[0])
sentenceOfTheDay = negativeSentences[sentenceOfTheDayIndex]

# Image management
imageOfTheDay =  'images/' + variablesList[1] + '.jpg'
imageOfTheDayIndex = int(variablesList[1])

# print(variablesList)
# print(imageOfTheDay)

# Day management
currentlyDay = int(variablesList[2])

if __name__ == '__main__':
    api = api()
    tweet(api, sentenceOfTheDay, imageOfTheDay)
    api.update_profile(description=f"Esse perfil é um bot que atualiza o cidadão sobre o status do asfaltamento da Rua Anchieta.\n\nEstamos no status do dia: {currentlyDay}")

    # Indexs control
    sentenceOfTheDayIndex += 1
    currentlyDay += 1
    imageOfTheDayIndex += 1

    if sentenceOfTheDayIndex > 18:
        sentenceOfTheDayIndex = 0

    if imageOfTheDayIndex > 5:
        imageOfTheDayIndex = 1
    
    # Rewriting the variables to the file
    with open('variables.txt', 'w') as f:
        f.write(f'{sentenceOfTheDayIndex} {imageOfTheDayIndex} {currentlyDay}')
