import requests



def translate(key='', text='', lang='en'):
    # sourceLang = detect(text)
    # if sourceLang != 'en':
    r = requests.get(
        f'https://translation.googleapis.com/language/translate/v2?key={key}&q={text}&target={lang}')
    json_object = r.json()
    result = (json_object['data']['translations'][0]['translatedText'],
              json_object['data']['translations'][0]['detectedSourceLanguage'])
    # else:
    #     result = (text, 'en')
    return result


if __name__ == '__main__':
    print(translate('AIzaSyAbJY_u6cGsBBV597HpQ778NYXHDplYP7M', 'hello', 'es'))
