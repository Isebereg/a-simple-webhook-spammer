from discord_webhooks import DiscordWebhooks

webhook_url = input('#webhook url: ')

message = input('#Enter Message: ')
monke = int(input('#Enter Amount of Messages: '))


webhook = DiscordWebhooks(webhook_url)

webhook.set_content(title='#webhook title',
                    description=message,
                    color=0xF58CBA)

webhook.set_footer(text='')



for i in range(monke):
    webhook.send()
