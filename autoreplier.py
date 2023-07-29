import time

from telethon import TelegramClient, connection, events
import os

# Текст для реплая
message = "Извини, меня не будет до следующей недели 😢"

if __name__ == '__main__':
    api_id = os.environ['API_ID'] #123456
    api_hash = os.environ['API_HASH'] #'abcdefghij'
    phone = os.environ['PHONE'] #'+12345678900'
    session_file = os.environ['SESSION_FILE'] # '/path/to/file/session'
    password = os.environ['PASSWORD'] # если включена двуфакторная
    proxy = os.environ['TPPROXY']
    pport = int( os.environ['PPORT'])
    pkey = os.environ['PKEY']

    print(proxy, pport, pkey)

    client = TelegramClient(
        session_file, 
        api_id, 
        api_hash, 
        sequential_updates=True,
        connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
        proxy=(proxy, pport, pkey)
    )

    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private: 
            from_ = await event.client.get_entity(event.from_id)
            if not from_.bot: 
                print(time.asctime(), '-', event.message)
                time.sleep(1)
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')