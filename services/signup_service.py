def perform_signup(signup_page, data: dict):
    signup_page.signup(
        user_id=data["user_id"],
        password=data["password"],
        repassword=data["repassword"],
        name=data["name"],
        email=data["email"]
    )