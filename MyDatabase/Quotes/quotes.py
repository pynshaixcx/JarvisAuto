import random
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',115)

def engine_speak(text):
    text = str(text)
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[7].id)
    engine.setProperty('rate',115)
    engine.runAndWait()


def Quotes():
    qtes = ["Life isn't about getting and having  it's about giving and being. Kevin Kruse",
"Whatever the mind of man can conceive and believe  it can achieve. Napoleon Hill",
"Strive not to be a success  but rather to be of value. Albert Einstein",
"Two roads diverged in the woods  and I took the one less traveled by  And that has made all the difference", 
"I attribute my success to this: I never gave or took any excuse. Florence Nightingale",
"You miss 100% of the shots you don't take. Wayne Gretzky",
"The most difficult thing is the decision to act  the rest is merely tenacity. Amelia airhart",
"Every strike brings me closer to the next home run. Babe Ruth",
"Definiteness of purpose is the starting point of all achievement. W Clement Stone",
"We must balance conspicuous consumption with conscious capitalism. Kevin Kruse",
"Life is what happens to you while you're busy making other plans. John Lennon",
"We become what we think about. -Earl Nightingale",
"Life is 10% what happens to me and 90% of how I react to it. Charles Swindoll",
"The most common way people give up their power is by thinking they don't have any. Alice Walker",
"The mind is everything. What you think you become. Buddha",
"The best time to plant a tree was 20 years ago. The second best time is now. Chinese Proverb",
"An unexamined life is not worth living. Socrates",
"Eighty percent of success is showing up. Woody Allen",
"Your time is limited  so don't waste it living someone else's life. Steve Jobs",
"Winning isn't everything  but wanting to win is.  Vince Lombardi",
"I am not a product of my circumstances. I am a product of my decisions. Stephen Covey",
"Every child is an artist. The problem is how to remain an artist once he grows up. Pablo Picasso",
"You can never cross the ocean until you have the courage to lose sight of the shore. Christopher Columbus",
"Either you run the day  or the day runs you. Jim Rohn",
"Whether you think you can or you think you can't  you're right. Henry Ford",
"The two most important days in your life are the day you are born and the day you find out why. Mark Twain",
"There is only one way to avoid criticism: do nothing  say nothing  and be nothing. Aristotle",
"Ask and it will be given to you; search  and you will find; knock and the door will be opened for you. Jesus",
"The only person you are destined to become is the person you decide to be. Ralph Waldo Emerson",
"Go confidently in the direction of your dreams. Live the life you have imagined. Henry David Thoreau",
"Everything you've ever wanted is on the other side of fear. George Addair",
"We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light. Plato",
"Teach thy tongue to say I do not know  and thous shalt progress. Maimonides",
"Start where you are. Use what you have. Do what you can. Arthur Ashe",
"Everything has beauty  but not everyone can see. Confucius",
"How wonderful it is that nobody need wait a single moment before starting to improve the world. Anne Frank",
"When I let go of what I am  I become what I might be. Lao Tzu",
"Life is not measured by the number of breaths we take  but by the moments that take our breath away. Maya Angelou",
"Happiness is not something readymade. It comes from your own actions. Dalai Lama",
"If you're offered a seat on a rocket ship  don't ask what seat! Just get on.Sheryl Sandberg",
"If the wind will not serve  take to the oars. Latin Proverb",
"You can't fall if you don't climb. But there's no joy in living your whole life on the ground. Unknown",
"We must believe that we are gifted for something  and that this thing  at whatever cost  must be attained. Marie Curie",
"Too many of us are not living our dreams because we are living our fears. Les Brown",
"Challenges are what make life interesting and overcoming them is what makes life meaningful. Joshua J. Marine",
"If you want to lift yourself up  lift up someone else. -Booker T. Washington",
"Limitations live only in our minds. But if we use our imaginations  our possibilities become limitless. Jamie Paolinetti",
"A 1200-pound horse eats about seven times it's own weight each year. HOLY SHIT THAT'S A LOT!",
"Don't worry about what anybody else is going to do. The best way to predict the future is to invent it.",
"Premature optimization is the root of all evil (or at least most of it) in programming.",
"No problem should ever have to be solved twice.",
"Attitude is no substitute for competence.",
"It is said that the real winner is the one who lives in today but able  to see tomorrow.",
"Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it.",
"A year spent in artificial intelligence is enough to make one believe in God.",
"Within a computer natural language is unnatural.",
"A little learning is a dangerous thing.",
"Einstein argued that there must be simplified explanations of nature, because God is not capricious or arbitrary.",
"There really is no learning without doing.",
"The only problems we can really solve in a satisfactory manner are those that finally admit a nicely factored solution.",
"The best way to learn to live with our limitations is to know them.",
"An expert is, according to my working definition someone who doesn't need to look up answers to easy questions",
"The programmer must seek both perfection of part and adequacy of collection.",
"Thus, programs must be written for people to read, and only incidentally for machines to execute.",
"An interpreter raises the machine to the level of the user program, a compiler lowers the user program to the level of the machine language.",
"Everything should be made as simple as possible, but no simpler.",
"The great dividing line between success and failure can be expressed in five words, I did not have time.",
"When your enemy is making a very  serious mistake, don't be impolite and disturb him.",
"A charlatan makes obscure what is clear; a thinker makes clear what is obscure.",
"The three chief virtues of a programmer are: Laziness, Impatience and Hubris.",
"All non-trivial abstractions, to some degree, are leaky.",
"XML wasn't designed to be edited by humans on a regular basis.",
"Premature abstraction is an equally grevious sin as premature optimization.",
"You can have premature generalization as well as premature optimization.",
"He causes his sun to rise on the evil and the good, and sends rain on the righteous and the unrighteous.",
"A language that doesn't affect the way you think about programming, is not worth knowing.",
"Men never do evil so completely and cheerfully as when they do it from religious conviction.",
"Everybody makes their own fun. If you don't make it yourself, it ain't fun it's entertainment.",
"If we wish to count lines of code, we should not regard them as lines produced but as lines spent.",
"Omit needless words.",
"I have never met a man so ignorant that I couldn't learn something from him.",
"Philosophy: the finding of bad reasons for what one believes by instinct.",
"Fools! Don't they know that tears are a woman's most effective weapon",
"It's like a condom; I'd rather have it and not need it than need it and not have it.",
"C++ is history repeated as tragedy. Java is history repeated as farce.",
"Simplicity takes effort",
"Show, don't tell.",
"In God I trust; I will not be afraid. What can mortal man do to me",
"Linux is only free if your time has no value.",
"Code is poetry.",
"If you choose not to decide, you still have made a choice.",
"Civilization advances by extending the number of important operations which we can perform without thinking about them.",
"The function of wisdom is to discriminate between good and evil. ",
"Mistakes were made.",
"I would rather be an optimist and be wrong than a pessimist who proves to be right. The former sometimes wins, but never the latter.",
"Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.",
"The direct pursuit of happiness is a recipe for an unhappy life.",
"All problems in computer science can be solved by another level of indirection.",
"For the things we have to learn before we can do them, we learn by doing them.",
"There are many ways to avoid success in life, but the most sure-fire just might be procrastination.",
"Dont give users the opportunity to lock themselves.",
"Any fool can make the simple complex, only a smart person can make the complex simple.",
"Only bad designers blame their failings on the users.",
"When all you have is a hammer, everything looks like a nail.",
"If there is a will, there is a way.",
"Having large case statements in an object-oriented language is a sure sign your design is flawed.",
"The choice of the university is mostly important for the piece of paper you get at the end. The education you get depends on you.",
"Remember that you are humans in the first place and only after that programmers.",
"As builders and creators finding the perfect solution should not be our main goal. We should find the perfect problem.",
"Just like carpentry, measure twice cut once.",
"The good thing about reinventing the wheel is that you get a round one.",
"I feel it is everybodies obligation to reach for the best in themselves and use that for the interest of mankind.",
"Resume writing is just like dating, or applying for a bank loan, in that nobody wants you if you're desperate.",
"If I tell you I'm good, you would probably think I'm boasting. If I tell you I'm no good, you know I'm lying.",
"If something isn’t working, you need to look back and figure out what got you excited in the first place.",
"Pay attention to opportunity cost at all times. Doing one thing means not doing other things. This is a form of risk that is very easy to ignore, to your detriment.",
"Seize any opportunity, or anything that looks like opportunity. They are rare, much rarer than you think.",
"Things which matter most must never be at the mercy of things which matter least.",
"Don't have good ideas if you aren't willing to be responsible for them.",
"It is impossible to sharpen a pencil with a blunt axe. It is equally vain to try to do it with ten blunt axes instead.", 
"If we wish to count lines of code, we should not regard them as lines produced but as lines spent.",
"The most damaging phrase in the language is, It's always been done that way.",
"The only thing a man should ever be 100% convinced of is his own ignorance.",
"In theory, there’s no difference between theory and practice. But in practice, there is.",
"Act from reason, and failure makes you rethink and study harder. Act from faith, and failure makes you blame someone and push harder.",
"Measure everything you can about the product, and you'll start seeing patterns.",
"Quality of the people is better than the quality of the business idea.",
"Crappy people can screw up the best idea in the world.",
"The only constant in the world of hi-tech is change.",
"Write it properly first. It's easier to make a correct program fast, than to make a fast program correct.",
"You can’t get to version 500 if you don’t start with a version 1.",
"The wonderful and frustrating thing about understanding yourself is that nobody can do it for you.",
"When you have eliminated the impossible, whatever remains, however improbable, must be the truth.",
"In order to understand what another person is saying, you must assume that it is true and try to find out what it could be true of.",
"A journey of a thousand miles must begin with a single step.",
"No art, however minor, demands less than total dedication if you want to excel in it.",
"The minute you put the blame on someone else you’ve switch things from being a problem you can control to a problem outside of your control.",
"State is the root of all evil. In particular functions with side effects should be avoided.",
"It is better to be quiet and thought a fool than to open your mouth and remove all doubt.",
"Simplicity means the achievement of maximum effect with minimum means.",
"Normality is the route to nowhere.",
"The problem is that Microsoft just has no taste. And I don't mean that in a small way, I mean that in a big way.",
"Good work is no done by humble men.",
"Simplicity and pragmatism beat complexity and theory any day.",
"Remember, always be yourself ... unless you suck!",
"All great things require great dedication.",
"I'm always happy to trade performance for readability as long as the former isn't already scarce.",
"The definition of insanity is doing the same thing over and over again and expecting different results.",
"A no uttered from the deepest conviction is better than a yes merely uttered to please or what is worse, to avoid trouble.",
"The general principle for complexity design is this: Think locally, act locally.",
"Programming is the art of figuring out what you want so precisely that even a machine can do it.",
"Making All Software Into Tools Reduces Risk.",
"Two people should stay together if together they are better people than they would be individually",
"To the optimist, the glass is half full. To the pessimist, the glass is half empty. To the engineer, the glass is twice as big as it needs to be.",
"Whatever is worth doing at all, is worth doing well.",
"We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.",
"The best is the enemy of the good.",
"The job of a leader today is not to create followers. It’s to create more leaders.",
"You can recognize truth by its beauty and simplicity. When you get it right, it is obvious that it is right.",
"Talkers are no good doers.",
"Photography is painting with light",
"Good artists copy. Great artists steal.",
"The problem is that small examples fail to convince, and large examples are too big to follow.",
"We are the sum of our behaviours; excellence therefore is not an act but a habit.",
"The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise.",
"Every man prefers belief to the exercise of judgment.",
"It’s hard to grasp abstractions if you don’t understand what they’re abstracting away from.",
"I find that the harder I work, the more luck I seem to have.",
"Don't stay in bed, unless you can make money in bed.",
"If everything seems under control, you're not going fast enough.",
"Chance favors the prepared mind.",
"Controlling complexity is the essence of computer programming.",
"The function of good software is to make the complex appear to be simple.",
"Measuring programming progress by lines of code is like measuring",
"aircraft building progress by weight.",
"First learn computer science and all the theory.  Next develop a programming style.  Then forget all that and just hack.",
"To iterate is human, to recurse divine.",
"The best thing about a boolean is even if you are wrong, you are only off by a bit.",
"Everything that can be invented has been invented.",
"We will never become a truly paper-less society until the Palm Pilot folks come out with WipeMe 1.0.",
"If it keeps up, man will atrophy all his limbs but the push-button finger.",
"I guess, when you're drunk, every woman looks beautiful and every language looks.",
"Many of life's failures are people who did not realize how close they were to success when they gave up.",
"The only way of discovering the limits of the possible is to venture a little way past them into the impossible.",
"Any sufficiently advanced technology is undistinguishable from magic.",
"Good ideas are out there for anyone with the wit and the will to find them.",
"Beware of bugs in the above code; I have only proved it correct, not tried it.",
"The human brain starts working the moment you are born and never stops until you stand up to speak in public.",
"The trouble with the world is that the stupid are always cocksure and the intelligent are always filled with doubt.",
"Simple things should be simple. Complex things should be possible.",
"All creativity is an extended form of a joke.",
"If you don't fail at least 90 percent of the time, you're not aiming high enough.",
"Revolutions come from standing on the shoulders of giants and facing in a better direction.",
"If it looks like a duck, walks like a duck, and quacks like a duck, it's a duck.",
"The greatest challenge to any thinker is stating the problem in a way that will allow a solution.",
"The ability to simplify means to eliminate the unnecessary so that the necessary may speak.",
"However beautiful the strategy, you should occasionally look at the results.",
"Genius is 1% inspiration and 99% perspiration.",
"I’d rather write programs to write programs than write programs.",
"I had to learn how to teach less, so that more could be learned.",
"The Work Begins Anew, The Hope Rises Again, And The Dream Lives On.",
"The hardest part of design ... is keeping features out.",
"Before software can be reusable it first has to be usable.",
"Perpetual optimism is a force multiplier.",
"Be the change you want to see in the world.",
"The art of getting someone else to do something you want done because he wants to do it",
"No one is all evil. Everybody has a good side. If you keep waiting, it will comme up.",
"Experience is what you get when you don't get what you want.",
"Luck is where preparation meets opportunity.",
"The greatest of all weaknesses is the fear of appearing weak.",
"It's easier to ask forgiveness than it is to get permission.",
"An investment in knowledge always pays the best interest.",
"Natives who beat drums to drive off evil spirits are objects of scorn to smart Americans who blow horns to break up traffic jams.",
"Never do the impossible. People will expect you to do it forever after.",
"Give up control. You never really had it anyway.",
"Only two things are infinite, the universe and human stupidity. And I'm not so sure about the former.",
"The important thing is not to stop questioning.",
"Do not accept anything because it comes from the mouth of a respected person.",
"Work as intensely as you play and play as intensely as you work.",
"A witty saying proves nothing",
"Sound methodology can empower and liberate the creative mind; it cannot inflame or inspire the drudge.",
"Do not spoil what you have by desiring what you have not; but remember that what you now have was once among the things only hoped for.",
"Nobody can make you feel inferior without your consent.",
"If you tell the truth, you don't have to remember anything",
"You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
"The opposite of love is not hate, it's indifference.",
"Life is what happens to you while you're busy making other plans.",
"Whenever you find yourself on the side of the majority, it is time to pause and reflect.",
"To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
"It is not a lack of love, but a lack of friendship that makes unhappy marriages.",
"In terms of energy, it's better to make a wrong choice than none at all.",
"Courage is grace under pressure.",
"Before enlightenment, chop wood and carry water. After enlightenment, chop wood and carry water.",
"Acknowledging the negative doesn't mean sniveling [whining, complaining]; it means facing the truth and then moving on.",
"Whatever you can do, or dream you can, begin it. Boldness has genius, power, and magic in it."
    ]
    quotes = random.choice(qtes)
    print(quotes)
    engine_speak(quotes)