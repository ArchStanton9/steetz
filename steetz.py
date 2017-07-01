import rtg
from exchangelib import *

recipients = [
    'testwic1@skbkontur.ru',
    'testwic2@skbkontur.ru',
    'testwic3@skbkontur.ru',
]

login = 'KONTUR\\testWic4'
password = 'password'
credentials = Credentials(username=login, password=password)
account = Account(primary_smtp_address='testWic4@skbkontur.ru', credentials=credentials, autodiscover=True)


def send_message(recipient):
    try:
        essay = rtg.random()
        m = Message(
            account=account,
            subject=essay.subject,
            folder=account.sent,
            body=essay.body,
            to_recipients=[Mailbox(email_address=recipient)])

        m.send_and_save()
        print(f"\t + message '{essay.subject}' is shipped to {recipient}")
    except:
        print(f"\t - message '{essay.subject}' was failed. Unknown error.")


def procedure(count: int, box: int):
    if box == 0:
        print('recipients: ', recipients)
        print('messages: ', count*len(recipients))
        for i in range(count):
            for recipient in recipients:
                send_message(recipient)

    else:
        recipient = recipients[box-1]
        print('recipient: ', recipient)
        print('messages: ', count)
        for i in range(count):
            send_message(recipient)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-count',
                        type=int,
                        default=1,
                        help='Количество сообщений которое будет отправлено на каждый ящик. Не больше 3.')

    parser.add_argument('-box',
                        type=int,
                        default=0,
                        help='На какой ящик отправить сообщение. По умолчанию, все адреса участвуют в рассылке.')

    args = parser.parse_args()

    if int(args.count) not in range(1, 4):
        raise IndexError("Количество сообщений должно быть больше 0 но не больше 3.")

    if int(args.box) not in range(0, 4):
        raise IndexError("Неверный индекс ящика. Значение должно быть в интервале от 0 до 3.")

    print('Processing...')
    procedure(args.count, args.box)
