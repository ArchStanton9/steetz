import rtg
from mailer import MessageSender

recipients = [
    'testwic1@skbkontur.ru',
    'testwic2@skbkontur.ru',
    'testwic3@skbkontur.ru',
    'testwic4@skbkontur.ru'
]


def send_message(sender, recipient):
    try:
        essay = rtg.random()
        sender.send(recipient, essay.subject, essay.body)
        print(f"\t + message '{essay.subject}' is shipped to {recipient}")
    except Exception as ex:
        print(f"\t - message '{essay.subject}' was failed. Unknown error. {ex}")


def procedure(count: int, box: int):
    sender = MessageSender()

    if box == 0:
        print('recipients: ', recipients)
        print('messages: ', count*len(recipients))
        for i in range(count):
            for recipient in recipients:
                send_message(sender, recipient)

    else:
        recipient = recipients[box-1]
        print('recipient: ', recipient)
        print('messages: ', count)
        for i in range(count):
            send_message(sender, recipient)

    print("Procedure complete.")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-count',
                        type=int,
                        default=1,
                        help='Количество сообщений которое будет отправлено на каждый ящик. Не более 400.')

    parser.add_argument('-box',
                        type=int,
                        default=0,
                        help='На какой ящик отправить сообщение. По умолчанию, все адреса участвуют в рассылке.')

    args = parser.parse_args()

    if int(args.count) not in range(1, 400):
        raise IndexError("Количество сообщений должно быть больше 0 но не больше 400.")

    if int(args.box) not in range(0, 5):
        raise IndexError("Неверный индекс ящика. Значение должно быть в интервале от 1 до 4.")

    print('Processing...')
    procedure(args.count, args.box)
