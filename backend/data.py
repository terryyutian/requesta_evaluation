from typing import Dict, List

# --- PLACEHOLDER DATA ---
# Replace with your actual passages, questions, and vocabulary list.

PASSAGES: Dict[str, Dict] = {
    "p1": {
        "id": "p1x1",
        "title": "Passage",
        "text": '''
Biological anthropology focuses on the earliest processes in the biological and sociocultural development of human beings as well as the biological diversity of contemporary humans. In other words, biological anthropologists study the origins, evolution, and diversity of our species. Some biological anthropologists use genetic data to explore the global distribution of human traits such as blood type or the ability to digest dairy products. Some study fossils to learn how humans have evolved and migrated. Some study our closest animal relatives, the primates, in order to understand what biological and social traits humans share with primates and explore what makes humans unique in the animal world. \n\n
The Dutch primatologist Carel van Schaik spent six years observing orangutans in Sumatra, discovering that these reclusive animals are actually much more social than previously thought (2004). Moreover, van Schaik observed that orangutans use a wide variety of tools and pass down skills to their young. By studying these primates, van Schaik and other biological anthropologists gain insight into the origins of human intelligence, technology, and culture. These researchers also warn that habitat loss, illegal hunting, and the exotic pet trade threaten the survival of our fascinating primate cousins.\n\n
Biological anthropologists frequently combine research among primates with evidence from the human fossil record, genetics, neuroscience, and geography to answer questions about human evolution. Sometimes their insights are startling and unexpected. Anthropologist Lynne Isbell argues that snakes have played a key role in the evolution of human biology, particularly our keen sense of sight and our ability to communicate through language (Isabell, 2009). Isbell’s “snake detection theory” posits that primates developed specialized visual perception as well as the ability to communicate what they were seeing in order to alert others to the threat of venomous snakes in their environment. She points to the near-universal fear of snakes shared by both humans and primates and has documented the prevalence of snake phobia in human myth and folklore. Isbell’s research highlights how human-animal relations are central to humanity, shaping both biology and culture.\n\n
Not all biological anthropologists study primates. Many biological anthropologists study fossilized remains in order to chart the evolution of early hominins, the evolutionary ancestors of modern humans. In this field of study, anthropologists consider the emergence and migration of the various species in the hominin family tree as well as the conditions that promoted certain biological and cultural traits. Some biological anthropologists examine the genetic makeup of contemporary humans in order to learn how certain genes and traits are distributed in human populations across different environments. Others examine human genetics looking for clues about the relationships between early modern humans and other hominins, such as Neanderthals.

 '''
    },
    "p2": {
        "id": "p2x2",
        "title": "Passage",
        "text": '''
The first, and perhaps most crucial, elements of culture we will discuss are values and beliefs. Value does not mean monetary worth in sociology, but rather ideals, or principles and standards members of a culture hold in high regard. Values are deeply embedded and are critical for learning a culture’s beliefs, which are the tenets or convictions that people hold to be true. Individual cultures in a society have personal beliefs, but they also shared collective values. To illustrate the difference, U.S. citizens may believe in the American Dream—that anyone who works hard enough will be successful and wealthy. Values shape a society by suggesting what is good and bad, beautiful and ugly, sought or avoided.\n\n
Consider the value that the U.S. places upon youth. The U.S. also has an individualistic culture, meaning people place a high value on individuality and independence. In contrast, many other cultures are collectivist, meaning the welfare of the group takes priority over that of the individual. Fulfilling a society’s values can be difficult.\n\n
Values often suggest how people should behave, but they don’t accurately reflect how people do behave. Values portray an ideal culture, the standards society would like to embrace and live up to. But ideal culture differs from real culture. In an ideal culture, there would be no traffic accidents, murders, poverty, or racial tension. But in real culture, police officers, lawmakers, educators, and social workers constantly strive to prevent or address these issues.\n\n
One of the ways societies strive to maintain its values is through rewards and punishments. When people observe the norms of society and uphold its values, they are often rewarded. People sanction unwanted or inappropriate behaviors by withholding support, approval, or permission, or by implementing sanctions. We may think of ‘sanction’ as a negative term, but sanctions are forms of social control, ways to encourage conformity to cultural norms or rules. Breaking norms and rejecting values can lead to cultural sanctions such as earning a negative label like ‘lazy’ or to legal sanctions, such as traffic tickets, fines, or imprisonment. Utilizing social control encourages most people to conform regardless of whether authority figures (such as law enforcement) are present.\n\n
They change across time and between groups as people evaluate, debate, and change collective social beliefs. Values also vary from culture to culture. For example, cultures differ in their values about what kinds of physical closeness are appropriate in public. It’s rare to see two male friends or coworkers holding hands in the U.S. where that behavior often symbolizes romantic feelings. But in many nations, masculine physical intimacy is considered natural in public. Simple gestures, such as hand-holding, carry great symbolic differences across cultures.

'''
    },
}

QUESTIONS: Dict[str, List[Dict]] = {
    # Each passage id maps to 5 MCQs
    "p1": [
        {
            "id": "p1q1",
            "prompt": "What methods do biological anthropologists use to study the origins, evolution, and diversity of humans?",
            "choices": [
                {"id": "a", "text": "A) They analyze ancient texts and historical artifacts."},
                {"id": "b", "text": "B) They examine genetic data, fossils, and primate behavior."},
                {"id": "c", "text": "C) They focus on linguistic variations and cultural folklore."},
                {"id": "d", "text": "D) They study oceanic currents and geological formations."},
            ],
            "correct_choice_id": "b"
        },
        # add 4 more...
        {"id": "p1q2","prompt":"What does Lynne Isbell's 'snake detection theory' suggest about the role of snakes in human evolution?",
         "choices":[{"id":"a","text":"A) They contributed to the development of sophisticated genetic traits."},
                    {"id":"b","text":"B) They influenced the evolution of visual perception and communication."},
                    {"id":"c","text":"C) They led to significant changes in fossilized skeletal structures."},
                    {"id":"d","text":"D) They were essential in establishing primate social hierarchies."}],
                    "correct_choice_id":"b"},
        {"id": "p1q3","prompt":"How does studying the behavior of primates like tool use and social skills help in understanding human development?",
         "choices":[{"id":"a","text":"A) It demonstrates the genetic differences between primates and other animals."},
                    {"id":"b","text":"B) It provides insight into the origins of human intelligence, culture, and technology."},
                    {"id":"c","text":"C) To learn about early hominin migration patterns"},
                    {"id":"d","text":"D) To examine the evolution of tool-making abilities"}],
                    "correct_choice_id":"b"},
        {"id": "p1q4","prompt":"Why do biological anthropologists study primates to understand human evolution and modern biodiversity?",
         "choices":[{"id":"a","text":"A) To investigate the global distribution of human genetic traits"},
                    {"id":"b","text":"B) To gain insights into the development of human intelligence and culture"},
                    {"id":"c","text":"C) They recognized Indigenous peoples as exotic subjects for examination, similar to natural specimens."},
                    {"id":"d","text":"D) They focused on the preservation of Indigenous cultures to prevent their extinction."}],
                    "correct_choice_id":"a"},
        {"id": "p1q5","prompt":"Which statement best summarizes the text?",
         "choices":[{"id":"a","text":"A) Biological anthropology focuses only on genetic data and fossils to study human evolution."},
                    {"id":"b","text":"B) Biological anthropology highlights the threats to primates and their impact on human evolution."},
                    {"id":"c","text":"C) Biological anthropology examines human origins, evolution, and diversity through multiple methods and notable research contributions."},
                    {"id":"d","text":"D) Biological anthropology is primarily concerned with the influence of external factors like snakes on human development."}],
                    "correct_choice_id":"c"},
    ],
    "p2": [
        {"id":"p2q1","prompt":"How are values defined in sociology?",
            "choices":[{"id":"a","text":"A) As customary practices that members of a culture perform."},
                       {"id":"b","text":"B) As ideals or principles held in high regard by a culture."},
                       {"id":"c","text":"C) As monetary worth assigned to cultural artifacts."},
                       {"id":"d","text":"D) As natural laws governing cultural interactions."}],
                       "correct_choice_id":"b"},
        {"id":"p2q2","prompt":"How do societies use rewards and sanctions in social control?",
         "choices":[{"id":"a","text":"A) To encourage conformity to cultural norms."},
                    {"id":"b","text":"B) As tools for maintaining economic equality."},
                    {"id":"c","text":"C) As a way to enforce dietary practices."},
                    {"id":"d","text":"D) To promote technological advancement."}],
                    "correct_choice_id":"a"},
        {"id":"p2q3","prompt":"What does the disparity between ideal culture and real culture suggest about societal efforts to maintain values in the face of ongoing challenges?",
         "choices":[{"id":"a","text":"A) It highlights inconsistencies in how values are applied across different cultures."},
                    {"id":"b","text":"B) It indicates that societies actively work to uphold their values despite real-world difficulties."},
                    {"id":"c","text":"C) It illustrates that maintaining societal values is considered less important than facing current issues."},
                    {"id":"d","text":"D) It reflects that values are static and unchanging regardless of societal progress."}],
                    "correct_choice_id":"b"},
        {"id":"p2q4","prompt":"How might cultures differ in their views on public displays of physical intimacy?",
         "choices":[{"id":"a","text":"A) Societal pressures typically lead to similar values across all cultures regarding public intimacy."},
                    {"id":"b","text":"B) Public hand-holding among friends is generally perceived the same globally."},
                    {"id":"c","text":"C) Different societies attribute distinct symbolic meanings to acts like hand-holding."},
                    {"id":"d","text":"D) Values concerning public intimacy remain constant and do not evolve over time."}],
                    "correct_choice_id":"c"},
        {"id":"p2q5","prompt":"Which of the following best expresses the main idea of the text?",
         "choices":[{"id":"a","text":"A) Values and beliefs are insignificant in shaping societal norms."},
                    {"id":"b","text":"B) Values and beliefs are key in shaping cultural identity and societal norms, while also evolving across cultures."},
                    {"id":"c","text":"C) Crime and poverty are results of the failure of societal values."},
                    {"id":"d","text":"D) Social control mechanisms are responsible for enforcing values regardless of cultural differences."}],
                    "correct_choice_id":"b"},
    ],
}

# 60 vocab strings. Replace with your curated list.
KNOWN_WORDS = {
    "scornful","stoutly","ablaze","moonlit","lofty","hurricane","flaw",
    "unkempt","breeding","festivity","screech","savory","shin","fluid",
    "allied","slain","recipient","eloquence","cleanliness","dispatch",
    "ingenious","bewitch","plaintively","hasty","lengthy","fray","upkeep",
    "majestic","nourishment","turmoil","carbohydrate","scholar","turtle",
    "cylinder","censorship","celestial","rascal","muddy","listless","wrought"
}

TOKENS = [
    "mensible","scornful","stoutly","ablaze","kermshaw","moonlit","lofty",
    "hurricane","flaw","alberation","unkempt","breeding","festivity","screech",
    "savory","plaudate","shin","fluid","spaunch","allied","slain","recipient",
    "exprate","eloquence","cleanliness","dispatch","rebondicate","ingenious",
    "bewitch","skave","plaintively","kilp","interfate","hasty","lengthy","fray",
    "crumper","upkeep","majestic","magrity","nourishment","abergy","proom",
    "turmoil","carbohydrate","scholar","turtle","fellick","destription",
    "cylinder","censorship","celestial","rascal","purrage","pulsh","muddy",
    "quirty","pudour","listless","wrought",
]

VOCAB: List[Dict] = [
    {"id": f"v{i:02d}", "token": t, "is_word": (t in KNOWN_WORDS)}
    for i, t in enumerate(TOKENS, start=1)
]
