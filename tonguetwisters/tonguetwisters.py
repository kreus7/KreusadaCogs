import random

from redbot.core import commands
from redbot.core.bot import Red

TONGUE_TWISTERS = [
    'She sells sea shells by the sea shore.',
    'Peter Piper picked a peck of pickled peppers.',
    'Betty Botter bought some butter.',
    'How much wood would a woodchuck chuck if a woodchuck could chuck wood?',
    'Fuzzy Wuzzy was a bear, Fuzzy Wuzzy had no hair.',
    'If a dog chews shoes, whose shoes does he choose?',
    'I scream, you scream, we all scream for ice cream.',
    'I saw Susie sitting in a shoeshine shop.',
    'How can a clam cram in a clean cream can?',
    'Sheena leads, Sheila needs.',
    'The sixth sick sheikh’s sixth sheep’s sick.',
    'Pad kid poured curd pulled cod.',
    'A synonym for cinnamon is a cinnamon synonym.',
    'Seventy-seven benevolent elephants.',
    'Six shy shysters, shyly shy six shy oysters.',
    'Dizzy lizards driving lazy lizards.',
    'Dandy dandelions are decidedly delicious.',
    'Dapper dachshunds danced daintily.',
    'Tacky teachers talking about typography.',
    'Thirty-three thirsty, thundering thoroughbreds.',
    'Red lorry, yellow lorry.',
    'Unique New York.',
    'Blue blob, black blob.',
    'A big black bear sat on a big black rug.',
    'Six sleek swans swam swiftly southwards.',
    'Daring ducks dived into dewy daffodils.',
    'Drab dreadlocks draped drearily.',
    'Toy boat. Toy boat. Toy boat.',
    'She sees cheese.',
    'Truly rural.',
    'Good blood, bad blood.',
    'Flash message.',
    'Six slippery snails, slid slowly seaward.',
    'Four furious friends fought for the phone.',
    'Eleven benevolent elephants.',
    'Two tiny tigers take two taxis to town.',
    'Giddy goats gobbled up gooseberries, getting good at gobbling green grapes.',
    'Two toads, totally tired.',
    'Ten tall trees.',
    'Tiny Tim’s tiny toes.',
    'Witches watch watches which witches watch.',
    'Ghoulish goblins and gargoyles go galloping.',
    'Black bats blithely blinked back.',
    'Spooky spiders spin silk.',
    'Creepy crawlers creepily crawl.',
    'Mumbling mimes mimic more mellow mimes.',
    'Nifty nightingales nail nightly notes.',
    'Oddly oblong oranges oscillate overtly.',
    'Plucky penguins practically picnic on plums.',
    'Quaint quails quietly quiver and quake.',
    'Rusty robots repair rugged roads.',
    'Silly snakes slither slowly southward.',
    'Tumbling tigers take terrible tumbles.',
    'Unusually ugly unicorns under umbrellas.',
    'Vivacious vultures vie for vivid visions.',
    'Wily walruses whistle while wandering westward.',
    'Extra-large xylophones excite xenophobic x-rays.',
    'Yelling yaks yearn for yams.',
    'Zany zebras zigzag zooming zestfully.',
    'Dull ducks don’t dance daily.',
    'Betty bought butter but the butter was bitter, so Betty bought better butter to make the bitter butter better.',
    '“Surely Sylvia swims!” shrieked Sammy surprised. “Someone should show Sylvia some strokes so she shall not sink.”',
    'Brisk brave brigadiers brandished broad bright blades, blunderbusses, and bludgeons—balancing them badly.',
    'She stood on the balcony, inexplicably mimicking him hiccuping, and amicably welcoming him in.',
    'Susie works in a shoeshine shop. Where she shines she sits, and where she sits she shines.',
    'If you must cross a course cross cow across a crowded cow crossing, cross the cross coarse cow across the crowded cow crossing carefully.',
    'I thought a thought. But the thought I thought wasn’t the thought I thought I thought. If the thought I thought I thought had been the thought I thought, I wouldn’t have thought I thought.',
    'If practice makes perfect and perfect needs practice, I’m perfectly practised and practically perfect.',
    'Lesser leather never weathered wetter weather better.',
    'The great Greek grape growers grow great Greek grapes.',
    'Freshly fried fresh flesh.',
    'Silly Sally swiftly shooed seven silly sheep.',
    'The thirty-three thieves thought that they thrilled the throne throughout Thursday.',
    'Knapsack straps.',
    'Which wristwatches are Swiss wristwatches?',
    'Fred fed Ted bread, and Ted fed Fred bread.',
    'A skunk sat on a stump and thunk the stump stunk, but the stump thunk the skunk stunk.',
    'Vickie’s vacationing in various vague and vibrant valleys.',
    'Thieves thrive through this thrifty Thursday.',
    'Quirky quokkas quickly quiz each other.',
    'Picky people pick Peter Pan Peanut Butter, ’tis the peanut butter picky people pick.',
    'Six sick hicks nick six slick bricks with picks and sticks.',
    'The big bug bit the little beetle, but the little beetle bit the big bug back.',
    'Can you can a can as a canner can can a can?',
    'Vincent vowed vengeance very vehemently.',
    'A proper copper coffee pot.',
    'Around the rugged rocks, the ragged rascal ran.',
    'Brisk brave brigadiers brandished broad bright blades.',
    'Can clams cram in a clean cream can?',
    'Eleven owls licked eleven, little, licorice lollipops.',
    'Five frantic frogs fled from fifty fierce fishes.',
    'Giggling gaggles of geese gander at the gooseberry garden.',
    'Harry Hunt hunts heavy hairy hares.',
    'I wish to wash my Irish wristwatch.',
    'Larry sent the latter a letter later.',
    'Many an anemone sees an enemy anemone.',
    'Noisy noises annoy an oyster most.',
    'Quick queens quack quick quacks quicker.',
    'Rolling red wagons.',
    'Seven slick slimey snakes slowly sliding southward.',
    'The big black bug bled black blood.',
    'Twelve twins twirled twelve twigs.',
    'Very well, very well, very well varied.',
    'We surely shall see the sun shine soon.',
    'Xylophones exist or so existentialists insist.',
    'Yellow butter, purple jelly, red jam, black bread.',
    'A dragonfly, a dragonfly, a dragonfly.',
    'Five frantic frogs fled from fifty fierce fishes.',
    'How much wood would a woodchuck chuck, if a woodchuck could chuck wood?',
    'Seven selfish shellfish.',
    'Unique New York.',
    'You know New York, you need New York, you know you need unique New York.',
    'Three free throws.',
    'A skunk sat on a stump and thunk the stump stunk, but the stump thunk the skunk stunk.'
] # Feel free to PR and submit more!


class TongueTwisters(commands.Cog):
    """Generate tongue twisters."""

    __author__ = "Kreusada"
    __version__ = "1.0.0"

    def __init__(self, bot: Red):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        context = super().format_help_for_context(ctx)
        return f"{context}\n\nAuthor: {self.__author__}\nVersion: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        return

    @commands.is_owner()
    @commands.command()
    async def tonguetwister(self, ctx: commands.Context):
        """Generate a tonguetwister."""
        await ctx.send(random.choice(TONGUE_TWISTERS))