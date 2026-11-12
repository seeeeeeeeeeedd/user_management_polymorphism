from user import User


class Moderator(User):
    def get_permissions(self) -> str:
        return 'Права модератора'
