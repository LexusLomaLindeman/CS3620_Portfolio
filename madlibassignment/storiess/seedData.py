from django_seed import Seed
from models import StoryInfo

seeder = Seed.seeder()

#
#StoryName:
#StoryURL:
#Story:
#Description:
#Verbcount:
#Adjective:
#Noun:
#Pronouns:
#Names:

story1Name = "The Picnic Adventure"
story1Url = "thepicnicadventur"
story1Story = "One sunny afternoon, [name1] decided to pack a [noun1]"
" and head to the park. Along the way, [pronoun1] met [name2], "
"who carried a basket filled with [adjective1] [noun2]. They "
"both decided to [verb1] together under a [adjective2] [noun3]. "
"Suddenly, a [adjective2] [noun3] appeared and tried to [verb2] "
"the food. Everyone started to [verb3], but in the end, they "
"laughed and shared the [noun4] happily."
story1Description = "A lighthearted story about a group of friends going on a picnic that turns into a funny mishap."
story1Verbcount = 2
story1Adjective = 3
story1Noun = 5
story1Pronouns = 1
story1Names = 2

seeder.add_entity(StoryInfo, story1Name,story1Url,story1Story,story1Description,story1Verbcount,story1Adjective,story1Noun,story1Pronouns,story1Names)


inserted_pks = seeder.execute()