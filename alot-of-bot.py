#
#   alot-of-bot
#   A bot for Alot
#   --------------
import os
import time
import praw

from requests import HTTPError

#   Reddit
#   ------
reddit = praw.Reddit('ThanksAlot by /u/my_hat_stinks v1.3')
reddit.login( username=os.environ['REDDIT_USER'], password=os.environ['REDDIT_PASS'] )
alotbot = reddit.get_redditor( os.environ['REDDIT_USER'] )

subreddits = {}
subreddits['pcmasterrace'] = {
    'limit' : 6, # Max 1 post per 6 hours (4 per day) as per mod request
    'footer' : "\n___\n[Glorious Alot Master Race](http://i.imgur.com/vNcacVA.png) bot. May your framerates be high and your Alots furry.\n" }
subreddits['halflife'] = { 'footer' : "\n___\nI like [Freeman Alot.](http://i.imgur.com/NTSGfr9.png)\n" }
subreddits['alotofbot'] = {}
subreddits['alot'] = {}
# subreddits['adviceanimals'] = {} # Asshole mods!

# Wall of Shame
# -------------
# Moderators that ban without justification!
# /r/gaming - Absolutely no reasonable explanation! http://i.imgur.com/cBWjSYC.png
# /r/AskReddit - Where responding is banworthy! http://i.imgur.com/deoOUmA.png
# /r/AdviceAnimals - New policies, apparently. http://i.imgur.com/s9YAtAg.png

# Other subreddits:
# /r/funny, strict no bots policy
# /r/videos, strict no bots policy (And incredibly rude mods http://i.imgur.com/aPnVRZz.png )
# /r/pcmasterrace, ban lifted with additional restrictions

#   Blacklist
#   ---------
blacklist_user = [os.environ['REDDIT_USER'], "AlotOfLoops", "WeylandTheDwarf"]
if os.environ['REDDIT_USER']!="alot-of-bot":
    blacklist_user.append( "alot-of-bot" ) # In case this code is used in another bot

blacklist_phrase = ["(#bot)", "(#nobots)"] # Don't respond to bots or people that don't want bots

#   Phrases
#   -------
phrase = {} # Source inaccurate? Send a pm to /u/alot-of-bot to get it fixed!
phrase['thanks'] = { 'response' : "[You're welcome!](http://i.imgur.com/2GlMqob.png)",
'trigger' : ["thanks alot", "thanks, alot", "alot of thanks"] }

phrase['alotofbot'] = { 'response' : "[Alot of bot!](http://i.imgur.com/MFfdZHA.png)",
'trigger' : ["alot-of-bot", "alot bot", "alot of bot", "alotofbot", "bot alot", "bots alot"],
'source' : "^^Image ^^created ^^for ^^/u/alot-of-bot" }
phrase['alotofalot'] = { 'response' : "[Alot of alots.](http://i.imgur.com/p3gPZ18.png)",
'trigger' : ["alot of alots", "alots alot"],
'source' : "^^Image ^^from ^^[Calistilaigh](http://www.reddit.com/user/Calistilaigh)" }

phrase['time'] = { 'response' : "[Alot Time!](http://i.imgur.com/4eT0Bhr.png)",
'trigger' : ["alot of time", "alot of the time", "alot time", "time alot", "time for alot", "alot oclock", "alot o'clock", "alot o clock"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['money'] = { 'response' : "[Alot of Money!](http://i.imgur.com/nh4q0Sg.jpg)",
'trigger' : ["alot of money", "alot of the money", "money alot"] }

phrase['happy'] = { 'response' : "[Alot happier.](http://i.imgur.com/t8aZv4L.png)",
'trigger' : ["alot happier", "alot of happiness", "happy alot", "happy, alot", "good, alot", "good alot"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['love'] = { 'response' : "[Alot loves you too!](http://i.imgur.com/aijArTU.jpg)",
'trigger' : ["love you alot", "love you, alot", "love u alot", "love u, alot", "alot of love", "love alot", "<3 u alot", "<3 you alot", "<3 alot", "alot <3"],
'source' : "[^^Image ^^by ^^sylvacoer](http://sylvacoer.deviantart.com/art/i-love-u-alot-253301165)"}

phrase['care'] = { 'response' : "[Alot cares too!](http://i.imgur.com/GrFe75O.png)",
'trigger' : ["care alot", "care about this alot", "cares about this alot", "care alot", "cares alot"],
'source' : "^^Hyperbole ^^and ^^a ^^Half ^^original ^^image" }

phrase['real'] = { 'response' : "[Alot of reality.](http://i.imgur.com/yCeaOLR.jpg)",
'trigger' : ["alot of reality", "real alot"],
'source' : "[^^Image ^^by ^^arixystix](http://www.arixystix.com/blog/2010/11/17/the-alot-is-better-than-you-at-everything/)"}

phrase['hear'] = { 'response' : "[Alot is loud!](http://i.imgur.com/meMj4pj.png)",
'trigger' : ["hear that alot", "alot is loud"],
'source' : "^^Hyperbole ^^and ^^a ^^Half ^^original ^^image" }

phrase['fire'] = { 'response' : "[Alot of Fire!](http://i.imgur.com/H6TMICT.png)",
'trigger' : ["alot of fire", "fire alot", "alot of heat", "hot alot"],
'source' : "^^Hyperbole ^^and ^^a ^^Half ^^original ^^image" }

phrase['better'] = { 'response' : "[Alot is better.](http://i.imgur.com/m29Q9W4.png)",
'trigger' : ["alot better", "better alot"],
'source' : "^^Image ^^from ^^[Nicksaurus](http://www.reddit.com/user/Nicksaurus) ^^at ^^/r/alot" }

phrase['sad'] = { 'response' : "[Alot just want to be left alone...](http://i.imgur.com/8UdC8F2.png)",
'trigger' : ["sad alot", "sad, alot", "leave alot alone", "left alone alot"],
'source' : "^^Hyperbole ^^and ^^a ^^Half ^^original ^^image" }
phrase['cry'] = { 'response' : "[Alot of sadness...](http://i.imgur.com/ok9am0S.png)",
'trigger' : ["alot of sadness", "cry alot", "crying alot"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['charge'] = { 'response' : "[Charging Alot!](http://i.imgur.com/dKvzDSj.png)",
'trigger' : ["charging alot", "alot charging", "charge alot", "charges alot"],
'source' : "^^Hyperbole ^^and ^^a ^^Half ^^original ^^image" }

phrase['dangerous'] = { 'response' : "[Alot more dangerous!](http://i.imgur.com/jDMDx04.png)",
'trigger' : ["alot more dangerous", "alot is dangerous", "dangerous alot", "alot dangerous"],
'source' : "^^Hyperbole ^^and ^^a ^^Half ^^original ^^image" }

phrase['alotmasterrace'] = { 'response' : "[Glorious Alot Master Race.](http://i.imgur.com/vNcacVA.png)",
'trigger' : ["alot of master race", "alot of masterrace", "alot master race", "alot masterrace", "alotmasterrace", "alot of pcmr", "pcmr alot", "master race alot", "masterrace alot"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['work'] = { 'response' : "[Alot of Work!](http://i.imgur.com/HYJxiak.png)",
'trigger' : ["alot of work", "work alot"],
'source' : "^^Image ^^from ^^[eggswithcheese](http://www.reddit.com/user/eggswithcheese) ^^at ^^/r/alot"}

phrase['eat'] = { 'response' : "[Eat Alot?](http://i.imgur.com/H0E6O9P.png)",
'trigger' : ["eat alot", "delicious alot", "hungry for alot"],
'source' : "^^Image ^^from ^^[IdleGamesRock](http://www.reddit.com/user/IdleGamesRock) ^^at ^^/r/alot" }

phrase['anger'] = { 'response' : "[Alot of Anger!](http://i.imgur.com/MLWMsaz.jpg)",
'trigger' : ["angry alot", "alot of anger", "rage alot", "alot of rage", "mad alot"],
'source' : "^^Image ^^from ^^[Fizzee](http://www.reddit.com/user/Fizzee) ^^at ^^/r/alot" }

phrase['people'] = { 'response' : "[Alot of People.](http://i.imgur.com/aj1iVum.jpg)",
'trigger' : ["alot of people"],
'source' : "^^Image ^^from ^^[Fizzee](http://www.reddit.com/user/Fizzee) ^^at ^^/r/alot" }

phrase['notalot'] = { 'response' : "[Not Alot?](http://i.imgur.com/71NZKXk.png)",
'trigger' : ["not alot", "no alot", "no, alot", "bad alot", "bad, alot"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['link'] = { 'response' : "[Link Alot](http://i.imgur.com/gCKIpLi.png)",
'trigger' : ["link alot", "alot of link", "links alot", "zelda alot", "alot of zelda"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['art'] = { 'response' : "[Alot of Art](http://i.imgur.com/imbSLiW.jpg)",
'trigger' : ["draw alot", "drawing alot", "drawn alot", "drew alot", "alot of drawing", "art alot", "alot of art"],
'source' : "[^^Image ^^by ^^chrispygraphics](http://chrispygraphics.deviantart.com/art/Alot-173274809)" }

phrase['karma'] = { 'response' : "[Alot of Karma](http://i.imgur.com/d2JF3oE.jpg)",
'trigger' : ["alot of karma", "karma alot", "alot of upvote", "upvote alot"],
'source' : "^^Image ^^from ^^[Rhythmic](http://www.reddit.com/user/Rhythmic) ^^at ^^/r/alot" }

phrase['paint'] = { 'response' : "[Alot of paint](http://i.imgur.com/CjH7htI.png)",
'trigger' : ["alot of paint", "paint alot", "painting alot", "painted alot", "paints alot"],
'source' : "^^Image ^^from ^^[AlotOfMSPaint](http://www.reddit.com/user/AlotOfMSPaint)" }

phrase['party'] = { 'response' : "[Party Alot!](http://i.imgur.com/ietupyB.png)",
'trigger' : ["alot of party", "alot of parties", "party alot", "partied alot", "parties alot", "alot of birthday", "birthday alot"],
'source' : "^^Image ^^from ^^[AlotOfMSPaint](http://www.reddit.com/user/AlotOfMSPaint)" }

phrase['freeman'] = { 'response' : "[Freeman Alot.](http://i.imgur.com/NTSGfr9.png)",
'trigger' : ["alot of freeman", "alot of gordon freeman", "freeman alot", "half-life alot", "halflife alot", "half life alot", "alot of half-life", "alot of halflife", "alot of half life"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['beautiful'] = { 'response' : "[Alot is beautiful!](http://i.imgur.com/rQYVMiy.png)",
'trigger' : ["beautiful alot", "alot of beauty", "makeup alot", "alot of makeup"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['spiders'] = { 'response' : "[Alot of spiders!](http://i.imgur.com/tNLqGQC.png)",
'trigger' : ["alot of spider", "spider alot", "spiders alot"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['gold'] = { 'response' : "[Alot of gold!](http://i.imgur.com/fcFss7H.gif)",
'trigger' : ["alot of gold", "gold alot", "golden alot", "golds alot", "alot of gild", "gild alot", "gilds alot", "gilded alot"],
'source' : "^^Image ^^from ^^[Fizzee](http://www.reddit.com/user/Fizzee) ^^at ^^/r/alot" }

# Naughty words!
phrase['nsfw'] = { 'response' : "[Alot NSFW.](http://i.imgur.com/F6PLi4e.png)",
'trigger' : ["alot of penis", "alot of boobs", "alot of porn", "alot nsfw", "alot of nsfw", "penis alot", "boobs alot", "porn alot", "sex alot", "alot of sex", "alot of dick", "dick alot", "alot of cum", "cum alot", "fuck alot", "alot of fuck", "fucking alot", "alot of dildos", "dildo alot", "dildos alot"],
'source' : "^^Image ^^editted ^^for ^^/u/alot-of-bot" }

phrase['bull'] = { 'response' : "[Alot of Bullshit!](http://i.imgur.com/s2Q7HMX.png)",
'trigger' : ["alot of bullshit", "bullshit alot", "alot of shit", "shit alot"],
'source' : "^^Image ^^from ^^[Deltr0nZer0](http://www.reddit.com/user/Deltr0nZer0) ^^at ^^/r/alot" }

# Used when there's no custom subreddit footer
footer_default = """
___
_I'm just a bot! ^^Don't ^^hurt ^^me!_
""" 

# Non-autoamted footer
footer_maual = """
___
_This comment was not automated!_

_^^Comment ^^will ^^be ^^removed ^^if ^^downvoted_ ^^| [_^^Bot ^^Source_](http://pastebin.com/JtBuWff4) ^^| ^^[_Confused?_](http://hyperboleandahalf.blogspot.co.uk/2010/04/alot-is-better-than-you-at-everything.html) 
"""

# Generic footer text
response_footer = """
_^^Comment ^^will ^^be ^^removed ^^if ^^downvoted_ ^^| ^^[_Source_](http://pastebin.com/JtBuWff4) ^^| ^^[_Confused?_](http://hyperboleandahalf.blogspot.co.uk/2010/04/alot-is-better-than-you-at-everything.html) 

"""

#   Temporary variables
#   -------------------
last_id = {}       # ID of the last comment we checked
last_time = {}     # Time of the last comment
next_post = {}     # Time of next post for limited subreddits

for subname in subreddits: # Fill with placeholders
    last_id[subname] = ''
    last_time[subname] = 0

#   Search a subreddit
#   ------------------
def search_sub( subname ):
    if 'limit' in subreddits[subname]:
        if subname not in next_post: # We've restarted or something, we need to find our last post
            next_post[subname] = 0 # If we've never posted
            for comment in alotbot.get_comments(limit=100):
                if (comment.subreddit.display_name.lower())==subname: # It's the right sub
                    next_post[subname] = comment.created_utc + (subreddits[subname]['limit'] * 3600) # Hours to seconds
                    break
        if next_post[subname]>time.time():
            print( "Failed to search subreddit '"+subname+"', limit reached." )
            return
    
    print( "Searching subreddit '" + subname + "'..." )
    sub = reddit.get_subreddit(subname) # Get our subreddit
    
    try:
        for comment in sub.get_comments(limit=100, place_holder=last_id[subname]):
            text = comment.body.lower() # Lower case
            if (comment.author.name in blacklist_user) or (any(string in text for string in blacklist_phrase)): # Blacklisted
                continue
            
            if (comment.id==last_id[subname]): # We've already checked it (This should be the last in the loop)
                continue
            
            if comment.saved: # It's saved, that means we've processed it before
                break
            
            if (comment.created_utc>last_time[subname]): # If this is the latest comment, store the data
                last_time[subname] = comment.created_utc
                last_id[subname] = comment.id
            
            for k in phrase: # Search each phrase
                if any(string in text for string in phrase[k]["trigger"]): # If it matches
                    comment.save() # Simplest way to keep it saved between sessions - Save it on Reddit!
                    print( "MATCH: " + k )
                    print( "RESPOND: " + phrase[k]["response"] )
                    
                    footer = ""
                    if 'footer' in subreddits[subname]: # Custom subreddit footer
                        footer = subreddits[subname]['footer'] + response_footer
                    else:
                        footer = footer_default + response_footer # Default footer
                    
                    if 'source' in phrase[k]: # Image source
                        footer = footer + phrase[k]['source']
                    else:
                        footer = footer + "^^Image ^^source ^^unknown" # Source unknown
                    
                    footer = footer + " [](#bot)" # Tag our post as a bot post for other bots to see
                    
                    comment.reply( phrase[k]["response"] + footer ) # Post reply
                    
                    if 'limit' in subreddits[subname]:
                        next_post[subname] = time.time() + (subreddits[subname]['limit'] * 3600)
                        break # Break to prevent two replies when subreddit is limited
    except AttributeError:
        print( "Something went wrong! Missing attribute" ) # How did this even happen?

#   Scan submissions
#   ----------------
def alot_cleanup(): # Remove downvoted submissions
    print( "Starting  alot-of-bot comment cleanup..." )
    for comment in alotbot.get_comments(limit=100):
        if comment.score<=-1:
            print( "Removing comment!" )
            comment.delete()
        elif not comment.saved:
            text = comment.body.lower()
            if not (("#bot" in text) or ("#nobot" in text)): # Non-automated response
                comment.save()
                comment.edit( comment.body + footer_maual )

#   Main
#   ----
next_cleanup = 1
while True:
    next_cleanup=next_cleanup-1
    if next_cleanup<=0:
        try:
            alot_cleanup()
        except HTTPError as err:
            print( "ERROR: HTTP Error in Cleanup." )
        except praw.errors.RateLimitExceeded as err:
            print( "ERROR: Rate limit exceeded." )
        next_cleanup=10
    
    print( "Starting checks..." )
    for subname in subreddits:
        try:
            search_sub(subname)
        except HTTPError as err:
            print( "ERROR: HTTP Error in subreddit '" + subname + "'." )
        except praw.errors.RateLimitExceeded as err:
            print( "ERROR: Rate limit exceeded." )
    print( "Done!" )
    time.sleep( 20 )