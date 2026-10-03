class UIErrorMsg:
    """UI 상에 노출되는 에러 메시지 텍스트를 상수로 관리합니다."""
    # 공통 서브스트링으로 관리하여 Web과 Mobile 모두에서 to_contain_text / contains(@label) 로 호환되게 함
    LOGIN_EMPTY_BOTH = "아이디, 비밀번호를 입력해주세요"
    LOGIN_EMPTY_ID = "아이디를 입력해주세요"
    LOGIN_EMPTY_PASSWORD = "비밀번호를 입력해주세요" 
    LOGIN_UNKNOWN_USER = "존재하지 않는"
    LOGIN_WRONG_PASSWORD = "일치하지 않습니다"
    FIND_ACCOUNT_EMPTY = "입력"
    FIND_ACCOUNT_NOT_FOUND = "일치하는 정보가 없습니다."

class AssertMsg:
    """Assertion 실패 시 출력할 공통 로그 메시지를 상수로 관리합니다."""
    ERROR_MISMATCH = "실제 에러 메시지가 기대와 다릅니다."
    NOT_DISPLAYED = "에러 메시지가 노출되지 않았습니다."
    LOGIN_SUCCESS_FAIL = "로그인 후 메인 화면(게시글 리스트)으로 이동하지 않았습니다."
    LOGOUT_FAIL = "로그아웃 후 로그인 화면으로 이동하지 않았습니다."
    POST_NOT_FOUND = "작성한 게시글이 목록에 노출되지 않습니다."
    POST_NOT_DELETED = "삭제된 게시글이 여전히 보입니다."
    AUTH_MENU_VISIBLE = "타인이 작성한 글/댓글인데도 더보기(수정/삭제) 메뉴가 노출됩니다."
    SEARCH_EMPTY_FAIL = "'게시글이 없습니다.' 메시지가 노출되지 않았습니다."
    FIND_ID_FAIL = "찾은 아이디가 화면에 노출되지 않았습니다."
