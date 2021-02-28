class GithubApiError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = 'Rate limit Reached!'
        else:
            message = f"Status Code: {status_code}"
            super().__init__(message)


