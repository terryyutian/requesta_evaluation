from typing import Dict, List

# --- PLACEHOLDER DATA ---
# Replace with your actual passages, questions, and vocabulary list.

PASSAGES: Dict[str, Dict] = {
    "p1": {
        "id": "p1x1",
        "title": "Passage",
        "text": '''The conservation movement began in the 19th century as people in Europe and America began to realize that human settlement and the exploitation of the world’s natural resources had led to the destruction or endangerment of numerous animals, plants, and significant environments. Efforts began in the 1860s to understand and protect the remaining natural landscapes and habitats. These efforts were partly motivated by concern for wildlife and natural areas. However, also significant were the concerns of sporting organizations and recreationists. The primary aim of early conservation efforts was to preserve significant natural ecosystems for parks or wilderness areas so that sportspeople and outdoor enthusiasts would have places to hunt, fish, and explore. Many areas preserved by these early efforts are still protected today, such as Yellowstone and Yosemite National Parks in the United States. \n\n
An element of this early period of conservation was the effort to collect specimens for display in natural history museums. This collection effort was part of a movement known as naturalism, which seeks to understand the world and the laws that govern it by direct observation of nature. The late 19th and early 20th centuries saw a marked growth in naturalist collections worldwide as many cities and nations sought to establish and fill their own natural history museums. These collections have been particularly useful to zooarchaeologists and archaeobotanists, who use specimen collections of mammals, birds, fish, and plants to identify natural objects and animal remains found at human burial sites. Many archaeology labs have collections of animal skeletons for comparative anatomy, analysis, and identification.\n\n
In addition to animal specimens, Native American baskets and other Indigenous art objects were collected and placed in natural history museums. When visiting the Auckland Museum in Auckland, New Zealand, visitors today encounter two large totem poles in the foyer. Northwest Coast totem poles are common in most older museums throughout the world. These totem poles were gathered from America’s Northwest Coast in the late 19th and early 20th centuries as part of the worldwide conservation and naturalism movement. Most museums sought to purchase such artifacts, but in some cases, artifacts were stolen when Indigenous owners were unwilling to sell them. Many natural history museums also established dioramas depicting both Indigenous peoples and animals in their “natural” world. The practice of installing dioramas of Indigenous people is now heavily criticized because of the implication that Indigenous peoples are akin to animals and plants. Many museums have stopped this practice and have even dropped the phrase natural history from their names. However, the Smithsonian Institution’s National Museum of Natural History in Washington, DC, and the American Museum of Natural History in New York both maintain the designation and still display dioramas of Indigenous peoples.
 '''
    },
    "p2": {
        "id": "p2x2",
        "title": "Passage",
        "text": '''Imagine that someone handed you a babbling baby and said to you, “Teach this baby the basic rules and values of our culture.” What would you do? \n\n
Likely, you’d start by teaching the baby your language. Without language, it’s pretty hard to teach rules and values (unless you are a really good mime). Luckily, babies come into the world with special cognitive abilities that make them ready to learn language. Most babies undergo a rapid process of language learning between the ages of nine months and three years. Babies proceed through a set of stages that allow them to learn language just by being exposed to surrounding talk. Many scholars study the problem of language acquisition, examining precisely how humans manage to learn language in a diversity of sociocultural contexts. \n\n
So your babbling baby would probably learn language just by being exposed to it. But what if someone wanted to hasten the process or make sure their baby was particularly excellent with language?\n\n
An American would probably interact with the baby in a particular way, sitting the baby on their lap facing them, pointing to objects and asking basic questions in a quiz-like fashion. “See the cookie? Where did the cookie go? In my tummy!” The person might say these types of things while talking in a high-pitched, sing-song voice. Linguists call this type of talk “motherese.” In many other cultures, caregivers do not interact with babies in this way. In some cultures, oversimplified “baby talk” is considered detrimental to language learning. The context of language learning might involve a whole host of characters beyond the baby and the caregiver, encompassing all household relatives, neighbors, visitors, and even strangers. Language is not always “taught” to babies, but is often witnessed and overheard. Rather than quizzing her baby American style, a mother in Kaluli society in Papua New Guinea is more likely to sit her baby on her lap facing outward, talking “for” the baby in conversations with siblings (Ochs and Schieffelin [1984] 2001). In West Africa, babies spend large parts of the day wrapped on the backs of their mothers where face-to-face interaction with her is impossible. But they overhear the talk around them all day long, and people frequently engage their attention in brief interactions. In the field of language socialization, researchers go beyond the various stages of language learning to focus on the social contexts in which language is acquired. As social contexts shape the way children learn language, language itself becomes a means of learning about sociocultural life.\n\n
Whether facing their caregivers or facing out to the social world around them, babies in all cultures learn to be proficient in their languages. And yet, in American culture, the notion persists that language proficiency relies on very precise forms of interaction between caregiver and baby, the American model of motherese. Every culture has specific ideas about language, how it is acquired, how it varies across social groups, how it changes over time, etc. These ideas are termed language ideologies. Some of these ideas, like the notion that babies have a special “window” of opportunity for learning language, are supported by linguistic research. Others, however, are challenged by ethnographic and cross-cultural research.
'''
    },
}

QUESTIONS: Dict[str, List[Dict]] = {
    # Each passage id maps to 5 MCQs
    "p1": [
        {
            "id": "p1q1",
            "prompt": "When did the conservation movement begin and what issue did it address?",
            "choices": [
                {"id": "a", "text": "A) 17th century, focusing on land discovery and colonization."},
                {"id": "b", "text": "B) 18th century, focusing on agricultural innovations."},
                {"id": "c", "text": "C) 19th century, addressing the destruction caused by human activities."},
                {"id": "d", "text": "D) 20th century, addressing industrial pollution."},
            ],
            "correct_choice_id": "b"
        },
        # add 4 more...
        {"id": "p1q2","prompt":"Why are natural history collections significant to zooarchaeologists and archaeobotanists?",
         "choices":[{"id":"a","text":"A) They help identify animal remains at human burial sites."},
                    {"id":"b","text":"B) They provide insights into the history of conservation efforts."},
                    {"id":"c","text":"C) They offer protection to endangered species."},
                    {"id":"d","text":"D) They serve as attractions in natural history museums."}],
                    "correct_choice_id":"c"},
        {"id": "p1q3","prompt":"What does the dual focus of early conservation efforts reveal about the motivations behind protecting natural landscapes in the 19th century?",
         "choices":[{"id":"a","text":"A) It was aimed solely at preserving species from extinction due to human activity."},
                    {"id":"b","text":"B) It facilitated the rise of natural history museums to educate the public."},
                    {"id":"c","text":"C) It served both ecological preservation and recreational needs, such as hunting and exploring."},
                    {"id":"d","text":"D) It highlighted tensions between Indigenous peoples and conservationists."}],
                    "correct_choice_id":"a"},
        {"id": "p1q4","prompt":"What does the collection and display of Indigenous artifacts and the creation of dioramas in museums suggest about the mindset of the collectors during the late 19th and early 20th centuries?",
         "choices":[{"id":"a","text":"A) They viewed Indigenous cultures as worthy of study on the same level as natural ecosystems."},
                    {"id":"b","text":"B) They considered Indigenous cultures to be evolving similarly to other societies."},
                    {"id":"c","text":"C) They recognized Indigenous peoples as exotic subjects for examination, similar to natural specimens."},
                    {"id":"d","text":"D) They focused on the preservation of Indigenous cultures to prevent their extinction."}],
                    "correct_choice_id":"d"},
        {"id": "p1q5","prompt":"What is the main idea of the text?",
         "choices":[{"id":"a","text":"A) The 19th-century conservation movement solely focused on preserving hunting areas."},
                    {"id":"b","text":"B) Museums played a crucial role in both conservation and controversial representation."},
                    {"id":"c","text":"C) Indigenous artifacts were a major concern in the conservation movement."},
                    {"id":"d","text":"D) The 19th-century conservation and naturalism movements impacted environmental awareness and museum practices."}],
                    "correct_choice_id":"a"},
    ],
    "p2": [
        {"id":"p2q1","prompt":"What cognitive abilities do babies have that make them ready to learn language?",
            "choices":[{"id":"a","text":"A) Distinct problem-solving skills specific to linguistic challenges."},
                       {"id":"b","text":"B) Innate abilities that allow them to process and acquire language."},
                       {"id":"c","text":"C) Skills for understanding complex grammatical structures."},
                       {"id":"d","text":"D) Unique methods to express culturally specific values."}],
                       "correct_choice_id":"a"},
        {"id":"p2q2","prompt":"How is 'motherese' used to interact with babies in American culture?",
         "choices":[{"id":"a","text":"A) It emphasizes silence and eye contact as interaction methods."},
                    {"id":"b","text":"B) It incorporates high-pitched, sing-song talk and quizzing."},
                    {"id":"c","text":"C) It involves constant physical gestures without verbal engagement."},
                    {"id":"d","text":"D) It uses monotonous tones to encourage calmness."}],
                    "correct_choice_id":"d"},
        {"id":"p2q3","prompt":"In contrast to the American model focusing on direct interaction with infants, how do some cultures approach language acquisition?",
         "choices":[{"id":"a","text":"A) By engaging infants in constant face-to-face interaction with caregivers"},
                    {"id":"b","text":"B) By encouraging infants to participate in structured language lessons"},
                    {"id":"c","text":"C) By involving infants in large group discussions to foster speech"},
                    {"id":"d","text":"D) By exposing infants to language through observation and overhearing"}],
                    "correct_choice_id":"b"},
        {"id":"p2q4","prompt":"How do cultural practices challenge the notion that direct interaction, like 'motherese', is essential for language proficiency?",
         "choices":[{"id":"a","text":"A) By showing that caregiver interaction often leads to confusion in language learning"},
                    {"id":"b","text":"B) By emphasizing the importance of overhearing and indirect exposure in language learning"},
                    {"id":"c","text":"C) By indicating that language proficiency primarily requires direct caregiver instruction"},
                    {"id":"d","text":"D) By demonstrating that passive listening does not contribute to language acquisition"}],
                    "correct_choice_id":"c"},
        {"id":"p2q5","prompt":"Which of the following best expresses the main idea of the text?",
         "choices":[{"id":"a","text":"A) Babies have an innate ability to learn language, and cultural practices influence this process."},
                    {"id":"b","text":"B) Language learning by babies is uniform across all cultures."},
                    {"id":"c","text":"C) The only effective way babies learn language is through direct interaction with caregivers."},
                    {"id":"d","text":"D) Sociocultural contexts play no role in a baby's language acquisition process."}],
                    "correct_choice_id":"b"},
    ],
}

# 63 vocab strings. Replace with your curated list.
VOCAB: List[Dict] = [
    {"id": f"v{i:02d}", "token": t}
    for i, t in enumerate([
        "platery","denial","generic","mensible","scornful","stoutly","ablaze","kermshaw","moonlit","lofty",
        "hurricane","flaw","alberation","unkempt","breeding","festivity","screech","savoury","plaudate","shin",
        "fluid","spaunch","allied","slain","recipient","exprate","eloquence","cleanliness","dispatch","rebondicate",
        "ingenious","bewitch","skave","plaintively","kilp","interfate","hasty","lengthy","fray","crumper",
        "upkeep","majestic","magrity","nourishment","abergy","proom","turmoil","carbohydrate","scholar","turtle",
        "fellick","destription","cylinder","censorship","celestial","rascal","purrage","pulsh","muddy","quirty", "pudour", "listless", "wrought"
    ], start=1)
]
