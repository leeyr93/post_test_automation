from utils.config import get_env

URL_MAIN = get_env("BASE_URL", "http://localhost:50005/")

URL_SIGNUP = URL_MAIN + 'join'
URL_LOGIN = URL_MAIN + 'login'
URL_BOARD_LIST = URL_MAIN + 'board_list'
URL_BOARD_WRITE = URL_MAIN + 'board_write'
URL_BOARD_SEARCH = URL_MAIN + 'board_search'
URL_FIND_ID = URL_MAIN + 'find_id'
URL_FIND_PW = URL_MAIN + 'find_pw'
URL_RESET_PW = URL_MAIN + 're_pw'
