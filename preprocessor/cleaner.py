import re


#Удаляем ссылки
def del_paint(text):
    out = re.sub(r'http\S+', '', text)
    return out 


#Удаляем упоминания других пользователей
def del_description(text):
    out = re.sub(r'@\S+', '', text)
    return out


#Удаляем хэштеги
def del_teg(text):
    out = re.sub(r'#\S+', '', text)
    return out


#Удаляем пунктуацию
def del_punctuation(text):
    out = re.sub(r'\W', ' ', text)
    return out


#Удаляем нижнее подчеркивание
def del_low_slash(text):
    out = re.sub(r'_', '', text)
    return out


#Удаляем цифры
def del_number(text):
    out = re.sub(r'\d', '', text)
    return out


#Очищаем данные от мусора
def del_stop_words(text, stop_words):
    list_of_words = text.split()
    new_list = []
    for word in list_of_words:
        if word not in stop_words:
            new_list.append(i)
    return " ".join(new_list)


def clean_text(text):
    text = text.lower()
    text = del_paint(text)
    text = del_description(text)
    text = del_teg(text)
    text = del_punctuation(text)
    text = del_low_slash(text)
    text = del_number(text)
    text = del_stop_words(text)
    return text

