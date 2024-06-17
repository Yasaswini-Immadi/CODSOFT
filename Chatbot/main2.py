import random

EATING = "I don't require to eat because.....i am a SUPER BOT! haha"
PARKS = "Wonderla, Mount Opera,Imagica are some great choices"
SLEEP="Turn on a humidifier,a nice scented candle and lofi music,just watch you falling into deep sleep within seconds"

def out_of_box():
    response = ["Could you please re-phrase that? ",
                "I didn't quite understand you.",
                "Sorry?",
                "I did not catch you.Can i help you with something else?","Sorry i cannot help you with that,please check other resources for further help"][
        random.randrange(5)]
    return response