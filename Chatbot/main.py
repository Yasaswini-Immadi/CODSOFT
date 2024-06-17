import re
import main2 as long


def probability(u_message, recognised_words, single=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in u_message:
        if word in recognised_words:
            message_certainty += 1

    
    percentage = float(message_certainty) / float(len(recognised_words))

   
    for word in required_words:
        if word not in u_message:
            has_required_words = False
            break


    if has_required_words or single:
        return int(percentage * 100)
    else:
        return 0


def check_message(message):
    highest_prob = {}

    
    def response(bot_response, list_of_words, single=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = probability(message, list_of_words, single, required_words)


    response('Hello Yasaswini! How are your doing?', ['hello', 'hi', 'hey', 'hey there'], single=True)
    response('See you Yasaswini!', ['bye', 'goodbye','see you'], single=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks','Thank you','Thanks a lot'], single=True)
    response('Take one step at a day but, NEVER GIVE UP!', ['Can', 'you', 'cheer', 'me','up'], required_words=['cheer'])
    response('Ypu can go for a jog,draw something pretty or just watch your fav movie!', ['suggest', 'me', 'a', 'leisure', 'activity'], required_words=['activity'])
    
    
    
    response(long.PARKS, ['suggest', 'amusement','parks'], required_words=['parks'])
    response(long.EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.SLEEP, ['I', 'am', 'not','able','to','sleep'], required_words=['sleep'])

    best_match = max(highest_prob, key=highest_prob.get)
    return long.out_of_box() if highest_prob[best_match] < 1 else best_match



def get_response(u_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', u_input.lower())
    response = check_message(split_message)
    return response



while True:
    print('Bot: ' + get_response(input('You: ')))
