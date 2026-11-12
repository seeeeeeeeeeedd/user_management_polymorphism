from user import User


class Admin(User):
    def get_permissions(self) -> str:
        return 'Администратор: полный доступ'
