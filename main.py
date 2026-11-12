from user import User
from admin import Admin
from moderator import Moderator

UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Показать права пользователя',
    '2': 'Показать права администратора',
    '3': 'Показать права модератора',
    '0': 'Выйти из программы'
}

(USER_PERMISSION_COMMAND, ADMIN_PERMISSION_COMMAND, MODERATOR_PERMISSION_COMMAND, EXIT_COMMAND) = commands.keys()

user = User()
admin = Admin()
moderator = Moderator()


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def show_permissions(user_object: User) -> None:
    print(f'Права пользователя: {user_object.get_permissions()}')


is_program_running = True

while is_program_running:
    print_commands()
    user_command_number = input('Выберите действие и укажите его номер: ').strip()

    if user_command_number in commands:
        if user_command_number == USER_PERMISSION_COMMAND:
            show_permissions(user)
        elif user_command_number == ADMIN_PERMISSION_COMMAND:
            show_permissions(admin)
        elif user_command_number == MODERATOR_PERMISSION_COMMAND:
            show_permissions(moderator)
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
