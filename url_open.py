import urllib.request

def url_open(url:str) -> list:
    """
    Функция возвращает список строк, прочитанный из файла на удаленном сервере.
    
    """
    lst = list()    
        
    with urllib.request.urlopen(url) as webpage:
        # где webpage - файловый объект, кот. содержит информацию об открываемом файле.
        for line in webpage: 
            # преобразуем тип bytes в str с исп. кодировки utf-8            
            lst.append(line.decode('utf-8').strip())
    return lst   
