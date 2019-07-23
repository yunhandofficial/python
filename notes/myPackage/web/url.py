
def my_url(itemPerPage=10, **kwargs):
    if itemPerPage not in range(1,11):
        return "1~10사이의 숫자를 입력하세요"
    if 'key' not in kwargs or 'targetDt' not in kwargs:
        return '필수값 누락'
        
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemPerPage={itemPerPage}&'

    for key, value in kwargs.items():
        base_url += f'{key}={value}&'
        
    return base_url