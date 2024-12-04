# -*- coding: utf-8 -*-
def monthName(id, language):
    months_rus = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
    months_en = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    if language == 'ru': return months_rus[id-1]
    elif language =='en': return months_en[id-1]