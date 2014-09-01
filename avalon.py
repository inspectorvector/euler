import willie
import random
from threading import Timer

# Good and evil ratio for player amounts: if 5: 3g 2e, if 6: 4g 2e, if 7: 4g 3e, if 8: 5g 3e, if 9: 6g 3e, if 10: 6g 4e
# initially, special roles will be Merlin and Assassin only. Others will simply be Loyal servants of Arthur or the Minions of Mordred.


@willie.module.commands('avalon')
def avalon(bot, trigger):
    if not seats_available:
        bot.say('a game of Avalon is already underway.')
        break
    seats_available = True

    game_runner = trigger.nick
    bot.say(game_runner + ' wants to play Avalon. Type .join to take a seat at the round table. ' + game_runner + ', type .start when everyone is ready.')

@willie.module.commands('start')
def start(bot, trigger):
    if game_runner != trigger.nick:
        bot.say('You are not the current game runner, or a game of Avalon has not been started.')
    else:
        bot.say('Welcome to Avalon')





