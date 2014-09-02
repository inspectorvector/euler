import willie
import random
from threading import Timer

# Good and evil ratio for player amounts: if 5: 3g 2e, if 6: 4g 2e, if 7: 4g 3e, if 8: 5g 3e, if 9: 6g 3e, if 10: 6g 4e
# initially, special roles will be Merlin and Assassin only. Others will simply be Loyal servants of Arthur or the Minions of Mordred.

@willie.module.commands('init') # manually initializes stuff, as i couldn't get setup working.
def initialise(bot, trigger):
    bot.say('Initialised!')
    bot.seats_available = True
    bot.game_runner = None
    bot.people_seated = []
    bot.lsoa = [] # loyal servants of arthur: the good team
    bot.mom = [] # minions of mordred: the evil team
    bot.merlin = None
    bot.assassin = None

@willie.module.commands('avalon')
def avalon(bot, trigger):
    if not bot.seats_available:
        bot.say('A game of Avalon is already underway.')
        return
    bot.game_runner = trigger.nick
    bot.say(bot.game_runner + ' wants to play Avalon. Type .join to take a seat at the round table. ' + bot.game_runner + ', type .start when everyone is ready to begin the game.')

@willie.module.commands('join')
def join(bot, trigger):
    if bot.seats_available:
        if trigger.nick not in bot.people_seated:
            bot.people_seated.append(trigger.nick)
            bot.say(trigger.nick + ' is now seated at the round table.')
            return
        elif trigger.nick in bot.people_seated:
            bot.say(trigger.nick + ', you are already sat at the round table.')
    else:
        bot.say('You may not sit at the round table at this time.')


@willie.module.commands('start')
def start(bot, trigger):
    if bot.game_runner == trigger.nick:
        bot.say('Welcome to a new game of Avalon!')
        bot.seats_available = False
        if len(bot.people_seated) < 5:
            bot.say('Sorry, not enough people are at the round table for a game to be played.')
            initialise(bot, trigger)
        if len(bot.people_seated) == 5:
        if len(bot.people_seated) == 6:
        if len(bot.people_seated) == 7:
        if len(bot.people_seated) == 8:
        if len(bot.people_seated) == 9:
        if len(bot.people_seated) == 10:
    else:
        bot.say('You are not the current game runner, or a game of Avalon has not been started.')

def