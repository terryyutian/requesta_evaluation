from typing import Dict, List

# --- PLACEHOLDER DATA ---
# Replace with your actual passages, questions, and vocabulary list.

PASSAGES = {
    'p1': {
        'id': 'anthropology_1_2',
        'title': 'Passage',
        'text': """Biological anthropology focuses on the earliest processes in the biological and sociocultural development of human beings as well as the biological diversity of contemporary humans. In other words, biological anthropologists study the origins, evolution, and diversity of our species. Some biological anthropologists use genetic data to explore the global distribution of human traits such as blood type or the ability to digest dairy products. Some study fossils to learn how humans have evolved and migrated. Some study our closest animal relatives, the primates, in order to understand what biological and social traits humans share with primates and explore what makes humans unique in the animal world.\n\n
The Dutch primatologist Carel van Schaik spent six years observing orangutans in Sumatra, discovering that these reclusive animals are actually much more social than previously thought (2004). Moreover, van Schaik observed that orangutans use a wide variety of tools and pass down skills to their young. By studying these primates, van Schaik and other biological anthropologists gain insight into the origins of human intelligence, technology, and culture. These researchers also warn that habitat loss, illegal hunting, and the exotic pet trade threaten the survival of our fascinating primate cousins.\n\n
Biological anthropologists frequently combine research among primates with evidence from the human fossil record, genetics, neuroscience, and geography to answer questions about human evolution. Sometimes their insights are startling and unexpected. Anthropologist Lynne Isbell argues that snakes have played a key role in the evolution of human biology, particularly our keen sense of sight and our ability to communicate through language (Isabell, 2009). Isbell's "snake detection theory" posits that primates developed specialized visual perception as well as the ability to communicate what they were seeing in order to alert others to the threat of venomous snakes in their environment. She points to the near-universal fear of snakes shared by both humans and primates and has documented the prevalence of snake phobia in human myth and folklore. Isbell's research highlights how human-animal relations are central to humanity, shaping both biology and culture.\n\n
Not all biological anthropologists study primates. Many biological anthropologists study fossilized remains in order to chart the evolution of early hominins, the evolutionary ancestors of modern humans. In this field of study, anthropologists consider the emergence and migration of the various species in the hominin family tree as well as the conditions that promoted certain biological and cultural traits. Some biological anthropologists examine the genetic makeup of contemporary humans in order to learn how certain genes and traits are distributed in human populations across different environments. Others examine human genetics looking for clues about the relationships between early modern humans and other hominins, such as Neanderthals."""
    },
    'p2': {
        'id': 'anthropology_1_3',
        'title': 'Passage',
        'text': """As you might guess, linguistic anthropology focuses on language. Linguistic anthropologists view language as a primary means by which humans create their diverse cultures. Language combines biological and social elements. Some linguistic anthropologists study the origins of language, asking how language emerged in our biological evolution and sociocultural development and what aspects of language might have given early hominins an evolutionary advantage. Other linguistic anthropologists are interested in how language shapes our thinking processes and our views of the world. In addition to its cognitive aspects, language is a powerful tool for getting things done. Linguistic anthropologists also study how people use language to form communities and identities, assert power, and resist authority.\n\n
Linguistic anthropologists frequently conduct the same kinds of long-term, immersive research that cultural anthropologists do. Christopher Ball spent a year living and traveling with the Wauja, an indigenous group in Brazil (2018). He describes the many routine and ritualized ways of speaking in this community and how each kind of talk generates specific types of social action. "Chief speech" is used by leaders, while "bringing the spirits" is used for healing the sick. Ceremonial language is used for giving people names and for conducting exchanges between different indigenous groups. Ball, like many linguistic anthropologists, also examined public speeches, such as the ones delivered by Wauja leaders to protest a dam on a nearby river. Ball also analyzed the forms of language used by state officials and development workers to marginalize and subordinate indigenous groups such as the Wauja.\n\n
Language is central to the way we conceptualize ourselves and our lives. Have you ever been asked to write an essay about yourself, perhaps as part of a school assignment or college application? If so, you might have used different phrases and concepts than if you'd been chatting with a new acquaintance. The purpose and intended audience of our language use shapes the way we represent ourselves and our actions.\n\n
Anthropologist Summerson Carr examined an addiction treatment program for homeless women in the midwestern United States, looking at the role of language in the therapeutic process (2011). After observing therapy sessions and self-help meetings, she describes how addiction counselors promote a certain kind of "healthy talk" that conveys deep cultural notions about personhood and responsibility. As patients master this "healthy talk," they learn to demonstrate progress by performing very scripted ways of speaking about themselves and their addiction."""
    },
    'p3': {
        'id': 'anthropology_2_3',
        'title': 'Passage',
        'text': """Ethnography is still commonly used by cultural anthropologists. Practitioners today consult multiple informants during their research in order to gather a variety of perspectives on a culture or society. No one person has a full or authoritative view of their own culture; multiple viewpoints are essential to a full description. Many early anthropological studies only invited male perspectives, introducing a male bias into the resulting ethnographies. Now, anthropologists deliberately seek varied perspectives, consulting people of different genders and ages and who occupy different roles.\n\n
Anthropologists can introduce significant bias into an ethnography. Having an ethnocentric or etic perspective means someone is judging a culture according to the standards of their own culture and belief system. To observe a culture from the perspective of the people being researched is to have an emic perspective. In addition, an anthropologist's interpretation of the information gathered can significantly alter their research findings. Earlier anthropologists were primarily male and White, so their findings were based on interpretations made through these lenses. Feminist anthropology attempts to address this male bias. In the 1920s, female anthropologists such as Zora Neale Hurston and Ruth Benedict began publishing in the field, but not until the 1928 publication of Margaret Mead's Coming of Age in Samoa did a female anthropologist gain prominence.\n\n
Women's contributions and perspectives became much more pronounced in the later parts of the 20th century. Feminist anthropologists seek not only to claim a role for themselves in the field equal to that offered to men but also to expand the focal points of anthropological inquiry to include areas of life such as family, marriage, and child-rearing, as well as the economic and social roles played by women. The dominance of male anthropologists had biased analysis of human societies toward male-dominated roles and activities. It was also assumed that women in early societies had subservient roles to men, when in fact most early societies have now been found to be very egalitarian, with equal status accorded to women and men. Feminist anthropology has both expanded research to include women's roles and aimed to understand the gender roles in other societies on their own terms, rather than according to the gender roles of the researcher's own society.\n\n
Other perspectives emerged in anthropology in the 1970s as more members of minority groups began entering the field. One category of minority voices that has been a significant asset to anthropology is that of people with Indigenous ancestors. Practitioners with this type of background are part of a subfield called Indigenous anthropology."""
    },
    'p4': {
        'id': 'anthropology_4_4',
        'title': 'Passage',
        'text': """The theory of natural selection has five main components:\n\n
All organisms are capable of producing offspring faster than the food supply increases.\n\n
All organisms show variation.\n\n
There is a fierce struggle for existence, and those with the most suitable variations are most likely to survive and reproduce.\n\n
Variations, or traits, are passed on to offspring (inherited).\n\n
Small changes in every generation lead to major changes over long periods of time.\n\n
A popular but often-misunderstood concept related to natural selection is the term survival of the fittest. Survival of the fittest does not necessarily mean that the biggest and fastest survive; instead, it refers to those who are most evolutionarily fit. This means that an organism has traits that are sufficient for survival and will be passed on to future generations. The term survival of the fittest was not even introduced by Darwin; rather, it was first used by English philosopher, anthropologist, and sociologist Herbert Spencer, who promoted the now discredited ideology of social Darwinism. Social Darwinism applied the concept of Darwin's biological evolution to human societies, proposing that human culture was progressing toward the "perfect human." Spencer's writings became integrally related to the 19th-century rise of scientific racism and European colonialism.\n\n
Moth with speckled wings resting on the trunk of a tree with bark showing a similar pattern and coloration.\n\n
Examples of Darwin's theory of natural selection can be found throughout the natural world. Perhaps one of the best known is the color change observed in peppered moths in England during the 19th century. Before the Industrial Revolution, peppered moths in England were a light grey color, well camouflaged on tree branches and less likely to be eaten by birds. Occasionally, through the process of mutation, black moths would appear in the population, but these were usually quickly eaten because they were more visible against light-colored bark. When soot from coal factories began to cover the bark of the trees, the black moths became better camouflaged and the white moths were now more visible. Consequently, the black moths were the ones to survive to reproduce, while the white ones were eaten. In a few decades, all the peppered moths in the cities were black. The process was termed industrial melanism. As coal usage decreased and the bark of the trees once again became lighter in color, white moths again dominated the urban areas.\n\n
Examples of natural selection in modern times are numerous. Pesticide resistance in insects is a classic example. Pesticide resistance refers to the decreasing susceptibility of a pest population to a pesticide that previously was effective at controlling it. Pest species evolve pesticide resistance via natural selection, with the most resistant individuals surviving to pass on their ability to resist the pesticide to their offspring. Another good example is the rise of "superbugs," bacteria that have become increasingly resistant to antibiotics."""
    },
    'p5': {
        'id': 'anthropology_9_1',
        'title': 'Passage',
        'text': """Critical race theory (CRT), developed by legal scholars in the 1980s, asserts that much of the inequity experienced by oppressed people in the United States can be understood through the critical lens of race. CRT states that racism is endemic, or regularly found in the laws, policies, and institutions of the United States. Thus, people who are socialized in American institutions often do not see the ways in which racism plays out in their daily lives. Notions of color blindness and meritocracy uphold the idea that racism either does not exist or is actually related to class, socioeconomics, or other factors. Color blindness is the idea that people "don't see color," meaning that they are unaware of the ways in which someone may experience the world because of the color of their skin. A meritocracy is a system in which people succeed entirely through their own hard work; thus, someone who believes in the notion of meritocracy overlooks any structural or racial inequities that may keep individuals from accessing the resources necessary for success (Delgado and Stefancic 2013). In the United States, these two concepts are often used together to blame poor (especially poor Black) individuals and families for their own misfortunes instead of looking to structural causes of poverty and income inequality. The term welfare queen is often used by politicians and the media to refer to a specific (Black or minority) demographic, even though statistically, White women are the most common recipients of government benefits. One way to challenge everyday endemic racism is to utilize counter-storytelling. These stories counteract the socialized assumptions that keep people of color marginalized. For instance, counter-stories are important in challenging the power of stereotypes such as the "welfare queen."\n\n
Critical race theory has become a hotly debated topic among politicians in the United States. CRT is often misunderstood by critics, who see it as a one-sided examination of (particularly American) history and society because CRT examines society through the lens of power and oppression. It often focuses on which groups benefit from cultural changes, including such things as civil rights legislation, essential to a democracy's guarantee of equal opportunity and protection under the law. In anthropology, CRT is an important tool for examining both modern institutions and the experiences of individuals in the United States, especially in regard to social inequalities. As just one example, CRT can shed light on the decisions made by those in power when redrawing the boundaries of voting districts. These decisions are often made with the goal of cementing a majority for a particular political party while diluting the voting power of citizens who don't typically belong that party, a practice known as gerrymandering. It is important for social scientists to consider the potential role of race and racism in making these decisions. If race and/or racism were found to be a factor, then these political decisions would be considered an example of systemic oppression."""
    },
    'p6': {
        'id': 'history_1_2',
        'title': 'Passage',
        'text': """During the Middle Ages, most Europeans lived in small villages that consisted of a manorial house or castle for the lord, a church, and simple homes for the peasants or serfs, who made up about 60 percent of western Europe's population. The lords owned the land; knights gave military service to a lord and carried out his justice; serfs worked the land in return for the protection offered by the lord's castle or the walls of his city, into which they fled in times of danger from invaders. Thus, although they were technically free, serfs were effectively bound to the land they worked, which supported them and their families as well as the lord and all who depended on him. The Catholic Church, the only church in Europe at the time, also owned vast tracts of land and became very wealthy by collecting not only tithes (taxes consisting of 10 percent of annual earnings) but also rents on its lands.\n\n
Women often died in childbirth, and perhaps one-third of children died before the age of five. Without sanitation or medicine, many people perished from diseases we consider inconsequential today; few lived to be older than forty-five. Entire families, usually including grandparents, lived in one- or two-room hovels that were cold, dark, and dirty. A fire was kept lit and was always a danger to the thatched roofs, while its constant smoke affected the inhabitants' health and eyesight.\n\n
In an agrarian society, the seasons dictate the rhythm of life. Idleness meant hunger. When the land began to thaw in early spring, peasants started tilling the soil with primitive wooden plows and crude rakes and hoes. Then they planted crops of wheat, rye, barley, and oats, reaping small yields that barely sustained the population. Bad weather, crop disease, or insect infestation could cause an entire village to starve or force the survivors to move to another location.\n\n
Early summer saw the first harvesting of hay, which was stored until needed to feed the animals in winter. Men and boys sheared the sheep, now heavy with wool from the cold weather, while women and children washed the wool and spun it into yarn. The coming of fall meant crops needed to be harvested and prepared for winter. Livestock was butchered and the meat smoked or salted to preserve it. Winter brought the people indoors to weave yarn into fabric, sew clothing, thresh grain, and keep the fires going."""
    },
    'p7': {
        'id': 'history_3_1',
        'title': 'Passage',
        'text': """Farther west, the Spanish in Mexico, intent on expanding their empire, looked north to the land of the Pueblo Natives. Under orders from King Philip II, Juan de Oñate explored the American southwest for Spain in the late 1590s. The Spanish hoped that what we know as New Mexico would yield gold and silver, but the land produced little of value to them. In 1610, Spanish settlers established themselves at Santa Fe—originally named La Villa Real de la Santa Fe de San Francisco de Asís, or "Royal City of the Holy Faith of St. Francis of Assisi"—where many Pueblo villages were located. Santa Fe became the capital of the Kingdom of New Mexico, an outpost of the larger Spanish Viceroyalty of New Spain, which had its headquarters in Mexico City.\n\n
As they had in other Spanish colonies, Franciscan missionaries labored to bring about a spiritual conquest by converting the Pueblo to Catholicism. At first, the Pueblo adopted the parts of Catholicism that dovetailed with their own long-standing view of the world. However, Spanish priests insisted that natives discard their old ways entirely and angered the Pueblo by focusing on the young, drawing them away from their parents. This deep insult, combined with an extended period of drought and increased attacks by local Apache and Navajo in the 1670s—troubles that the Pueblo came to believe were linked to the Spanish presence—moved the Pueblo to push the Spanish and their religion from the area. Pueblo leader Popé demanded a return to native ways so the hardships his people faced would end. To him and to thousands of others, it seemed obvious that "when Jesus came, the Corn Mothers went away." The expulsion of the Spanish would bring a return to prosperity and a pure, native way of life.\n\n
In 1680, the Pueblo launched a coordinated rebellion against the Spanish. The Pueblo Revolt killed over four hundred Spaniards and drove the rest of the settlers, perhaps as many as two thousand, south toward Mexico. However, as droughts and attacks by rival tribes continued, the Spanish sensed an opportunity to regain their foothold. In 1692, they returned and reasserted their control of the area. Some of the Spanish explained the Pueblo success in 1680 as the work of the Devil. Satan, they believed, had stirred up the Pueblo to take arms against God's chosen people—the Spanish—but the Spanish, and their God, had prevailed in the end."""
    },
    'p8': {
        'id': 'history_3_2',
        'title': 'Passage',
        'text': """After Jacques Cartier's voyages of discovery in the 1530s, France showed little interest in creating permanent colonies in North America until the early 1600s, when Samuel de Champlain established Quebec as a French fur-trading outpost. Although the fur trade was lucrative, the French saw Canada as an inhospitable frozen wasteland, and by 1640, fewer than four hundred settlers had made their home there. The sparse French presence meant that colonists depended on the local native Algonquian people; without them, the French would have perished. French fishermen, explorers, and fur traders made extensive contact with the Algonquian. The Algonquian, in turn, tolerated the French because the colonists supplied them with firearms for their ongoing war with the Iroquois. Thus, the French found themselves escalating native wars and supporting the Algonquian against the Iroquois, who received weapons from their Dutch trading partners. These seventeenth-century conflicts centered on the lucrative trade in beaver pelts, earning them the name of the Beaver Wars. In these wars, fighting between rival native peoples spread throughout the Great Lakes region.\n\n
A handful of French Jesuit priests also made their way to Canada, intent on converting the native inhabitants to Catholicism. The Jesuits were members of the Society of Jesus, an elite religious order founded in the 1540s to spread Catholicism and combat the spread of Protestantism. The first Jesuits arrived in Quebec in the 1620s, and for the next century, their numbers did not exceed forty priests. Like the Spanish Franciscan missionaries, the Jesuits in the colony called New France labored to convert the native peoples to Catholicism. They wrote detailed annual reports about their progress in bringing the faith to the Algonquian and, beginning in the 1660s, to the Iroquois. These documents are known as the Jesuit Relations, and they provide a rich source for understanding both the Jesuit view of the Native Americans and the Native response to the colonizers.\n\n
One Native convert to Catholicism, a Mohawk woman named Kateri Tekakwitha, so impressed the priests with her piety that a Jesuit named Claude Chauchetière attempted to make her a saint in the Church. However, the effort to canonize Tekakwitha faltered when leaders of the Church balked at elevating a "savage" to such a high status; she was eventually canonized in 2012. French colonizers pressured the native inhabitants of New France to convert, but they virtually never saw Native peoples as their equals."""
    },
    'p9': {
        'id': 'history_3_3',
        'title': 'Passage',
        'text': """Promoters of English colonization in North America, many of whom never ventured across the Atlantic, wrote about the bounty the English would find there. The English migrants who actually made the journey, however, had different goals. In Chesapeake Bay, English migrants established Virginia and Maryland with a decidedly commercial orientation. Though the early Virginians at Jamestown hoped to find gold, they and the settlers in Maryland quickly discovered that growing tobacco was the only sure means of making money. Thousands of unmarried, unemployed, and impatient young Englishmen, along with a few Englishwomen, pinned their hopes for a better life on the tobacco fields of these two colonies.\n\n
A very different group of English men and women flocked to the cold climate and rocky soil of New England, spurred by religious motives. Many of the Puritans crossing the Atlantic were people who brought families and children. While the English in Virginia and Maryland worked on expanding their profitable tobacco fields, the English in New England built towns focused on the church, where each congregation decided what was best for itself. Many historians believe the fault lines separating what later became the North and South in the United States originated in the profound differences between the Chesapeake and New England colonies.\n\n
The source of those differences lay in England's domestic problems. Increasingly in the early 1600s, the English state church—the Church of England, established in the 1530s—demanded conformity, or compliance with its practices, but Puritans pushed for greater reforms. By the 1620s, the Church of England began to see leading Puritan ministers and their followers as outlaws, a national security threat because of their opposition to its power. As the noose of conformity tightened around them, many Puritans decided to remove to New England.\n\n
The troubles in England escalated in the 1640s when civil war broke out, pitting Royalist supporters of King Charles I and the Church of England against Parliamentarians, the Puritan reformers and their supporters in Parliament. In 1649, the Parliamentarians gained the upper hand and, in an unprecedented move, executed Charles I. In the 1650s, therefore, England became a republic, a state without a king. English colonists in America closely followed these events. Indeed, many Puritans left New England and returned home to take part in the struggle against the king and the national church. The turmoil in England made the administration and imperial oversight of the Chesapeake and New England colonies difficult, and the two regions developed divergent cultures."""
    },
    'p10': {
        'id': 'history_3_4',
        'title': 'Passage',
        'text': """Everywhere in the American colonies, a crushing demand for labor existed to grow New World cash crops, especially sugar and tobacco. This need led Europeans to rely increasingly on Africans, and after 1600, the movement of Africans across the Atlantic accelerated. The English crown chartered the Royal African Company in 1672, giving the company a monopoly over the transport of enslaved African people to the English colonies. Over the next four decades, the company transported around 350,000 Africans from their homelands. By 1700, the tiny English sugar island of Barbados had a population of fifty thousand enslaved people, and the English had encoded the institution of chattel slavery into colonial law.\n\n
This new system of African slavery came slowly to the English colonists, who did not have slavery at home and preferred to use servant labor. Nevertheless, by the end of the seventeenth century, the English everywhere in America—and particularly in the Chesapeake Bay colonies—had come to rely on enslaved Africans. While Africans had long practiced slavery among their own people, it had not been based on race. Africans enslaved other Africans as war captives, for crimes, and to settle debts; they generally used enslaved people for domestic and small-scale agricultural work, not for growing cash crops on large plantations. Additionally, African slavery was often a temporary condition rather than a lifelong sentence, and, unlike New World slavery, it was typically not heritable.\n\n
The growing slave trade with Europeans had a profound impact on the people of West Africa, giving prominence to local chieftains and merchants who traded enslaved people for European textiles, alcohol, guns, tobacco, and food. Africans also charged Europeans for the right to trade in enslaved people and imposed taxes on enslaved people purchases. Different African groups and kingdoms even staged large-scale raids on each other to meet the demand for enslaved people.\n\n
Once sold to traders, all captured people sent to America endured the hellish Middle Passage, the transatlantic crossing, which took one to two months. By 1625, more than 325,800 Africans had been shipped to the New World, though many thousands perished during the voyage. An astonishing number, some four million, were transported to the Caribbean between 1501 and 1830. When they reached their destination in America, Africans found themselves trapped in shockingly brutal slave societies. In the Chesapeake colonies, they faced a lifetime of harvesting and processing tobacco.\n\n
Everywhere, Africans resisted slavery, and running away was common. In Jamaica and elsewhere, escaped enslaved people created maroon communities, groups that resisted recapture and eked out a living from the land, rebuilding their communities as best they could. When possible, they adhered to traditional ways, following spiritual leaders such as Vodun priests."""
    },
    'p11': {
        'id': 'lifespan_development_1_2',
        'title': 'Passage',
        'text': """In addition to studying what changes are expected and how they occur, developmental psychologists ask when we should expect certain skills to develop, and whether there are windows of opportunity for these that affect developmental outcomes. Is it possible to speed up development if we introduce an experience at just the right time? Is it possible to hinder or even prevent the development of a particular ability or characteristic altogether, such as speech? What are the impacts of highly enriching environments? What are the impacts of being deprived of certain experiences, such as human contact?\n\n
Scientists have learned that across nearly all psychological characteristics, humans are highly adaptable. They observe normative developmental outcomes, meaning those that are typical or expected, across a wide range of environmental conditions. Certainly, there are optimal environments for these developmental outcomes, but good outcomes occur even in suboptimal circumstances. This is central to resilience, an individual's capacity for and "process of adapting well in the face of adversity, trauma, tragedy, threats or even significant sources of stress" (American Psychological Association [APA], 2014). It takes extreme deprivation to severely restrict a developing human's potential, as well as such deprivation occurring at specific developmental times. In other words, resilience is common and lifespan development principles can be applied to increase the likelihood of resilience.\n\n
A critical period is the developmental age range in which certain experiences are required for a psychological or physical ability to develop (Colombo et al., 2019). For example, it appears that exposure to human speech is necessary in the early years of life for typical language development. Consider the 1970s case of Genie, a child who was severely neglected and isolated to the point that she was rarely spoken to. Upon her rescue at age thirteen years, Genie faced the monumental task of learning a language (a primary task of infants and toddlers) with an adolescent (post-pubescent) brain (Jones, 1995). Genie became the subject of intense study and remediation efforts by doctors, speech pathologists, and psychologists (Fromkin et al., 1974). Despite her extreme early deprivation, she made many improvements in language comprehension and speech production. However, her development of language differed markedly from what is normative. For example, language production and comprehension happen in the left hemisphere of the brain for the vast majority of humans, but Genie showed processing of language in her right cerebral hemisphere."""
    },
    'p12': {
        'id': 'lifespan_development_1_3',
        'title': 'Passage',
        'text': """Vygotsky (1978, 1998) proposed a sociocultural theory of cognitive development, emphasizing that thinking abilities are embedded within an individual's social and cultural context. Whereas Piaget's theory focused on a person's step-like journey of coming to understand the world, Vygotsky saw cognitive development as supported and propelled by social tools available to the individual learner. These social tools include language, direct support from others, and technological aids. Vygotsky, then, was among the first to recognize that language guides cognition and gives shape to ideas that can be readily communicated with others through words. One such example is private speech, whereby the learner may use words to audibly (or not) keep themselves on track during a difficult problem-solving session. If you've ever rehearsed a list of grocery items out loud while you searched for a place to record them, you've used language in such a way. Acronyms for remembering complex math concepts, such as PEMDAS (parentheses, exponents, multiplication, division, addition, and subtraction) for the order of arithmetic operations, are another example of language use supporting cognition.\n\n
The application of various forms of technology, another social tool, can allow an individual to perform complex tasks more easily than by relying on brain power alone. From this perspective, using a calculator to do basic calculations frees up the mind to think about the more important and complex parts of a word problem, for example. Word processing programs and apps that autocorrect spelling and grammar support thinking by allowing the writer to focus on the ideas of their message, instead of on the mechanics of writing.\n\n
Vygotsky is best known for championing social supports in propelling cognitive development and educational achievement. His notion of the zone of proximal development (ZPD) states that all of us are capable of thinking and achieving at a higher level than we may realize: there are concepts and ideas just beyond our current abilities that we are ready to master if only we have a little help, often from others. Educators and parents have used the idea of scaffolding to help learners achieve beyond their current level, gradually withdrawing support as the student becomes more competent. Learning how to ride a bicycle is a great example of scaffolding. Support for learning this difficult task can come through training wheels, or from a caregiver holding the bicycle seat while running alongside the child. As the child gains a sense of balance and masters the mechanics of pedaling and steering, the training wheels become less necessary and are eventually removed, and the caregiver lets go of the seat. The child has reached a new level of development with guided and temporary support."""
    },
    'p13': {
        'id': 'lifespan_development_1_4',
        'title': 'Passage',
        'text': """Research findings in psychology are often broken down by social or cultural sub-groups of particular interest or identification. These include biological sex, gender, race and ethnicity, religious beliefs, socioeconomic status, and cultural influences, among others. When developmental psychologists use these terms, they do so with the specific meanings they carry in psychology. These contexts are all important to the overall process of human development and our understanding of it.\n\n
Sex, gender, and sexual orientation are key components of human development and are distinctive terms (National Academies of Sciences, Engineering, & Medicine, 2022). An individual's sex is assigned at birth based on their biological anatomy and physiology (such as chromosomes). People may be assigned female, male, or intersex. An individual's sex should not be confused with their gender, which describes society's ideas about the roles, attitudes, and behaviors associated with someone's sex assignment. For example, being born with a penis results in being assigned the sex male; exhibiting behaviors such as participating in rough sports or suppressing emotions results in being associated with the gender male in cultures where those behaviors are associated with masculinity. Some people, researchers, and advocates aim to separate descriptors of sex (female and male) from those of gender (girl, woman, boy, man, nonbinary, and so on). While it is best to be as precise as possible, this practice is not universal and may be complicated when both sex and gender are involved in a topic or outcome. As a result, many studies or documents use sex and gender terms interchangeably.\n\n
The way a culture decides whether a characteristic or behavior is associated with a gender can also change over time. For example, in the United States the color blue is often associated with baby boys; however, if you looked to popular trends before the 1940s, pink was associated with boys and blue was associated with girls (Maglaty, 2011). Someone's psychological sense of their gender is their gender identity and reflects ideas about femininity, masculinity, non-binary characteristics, and other dimensions of gender. How someone labels their gender identity is also related to whether their gender matches society's expectations based on sex assignment. Conforming is denoted by the prefix cis- (such as a cis gender man) and non-conforming by the prefix trans- (such as a transgender individual). A person's sexual orientation includes their sexual identity, sexual behavior, and sexual attraction, or to whom someone is sexually attracted. Note that sexual attraction can differ from emotional attraction."""
    },
    'p14': {
        'id': 'lifespan_development_1_5',
        'title': 'Passage',
        'text': """A longitudinal design studies a group of participants over a period of time, re-assessing them at various points. If we are interested in the development of friendships during adolescence, we might recruit a group of fifty sixth-grade students. We would give them a personality inventory, collect background information about each, and ask them to complete surveys about their friendships. Then, we would find these same fifty participants at six-month or one-year intervals, re-assessing the same information. At the end of five or six years, we'd have a rich data set and a really good idea about how the number, type, and quality of friendships change across adolescence.\n\n
Often longitudinal studies are employed when researching various diseases in an effort to understand particular risk factors. Such studies often involve tens of thousands of individuals who are followed for several decades. Given the enormous number of people involved in these studies, researchers can feel confident that their findings can be generalized to the larger population. For instance, earlier longitudinal studies sponsored by the American Cancer Society provided some of the first scientific demonstrations of the now well-established links between increased rates of smoking and cancer (American Cancer Society, n.d.).\n\n
As with any research strategy, longitudinal research is not without limitations. For one, these studies require an incredible time investment by the researcher and research participants. Given that some longitudinal studies take years, if not decades, to complete, the results will not be known for a considerable period of time. Research participants must also be willing to continue their participation for an extended period of time, and this can be problematic. This is known as attrition, the gradual loss or dropping out of participants from the original pool. Another issue is test familiarity, known as practice effects. Since participants are given the same battery of measures including surveys multiple times, they might get used to the questions, which could alter the way they think about and respond to them.\n\n
Finally, and this is the most serious challenge in longitudinal research, the longer the study duration, the higher the risk of encountering cohort effects. This means that the research results, which in our hypothetical study would take five or six years to obtain, might end up being limited in their applicability beyond a certain cohort. Nevertheless, a longitudinal design comes closest to observing change within individuals over time, making this a highly valid and valuable approach."""
    },
    'p15': {
        'id': 'lifespan_development_9_3',
        'title': 'Passage',
        'text': """Adolescent thought is characterized by several other tendencies that stem from teens' new ability to think about what is possible. First is the ability to think in complex ways about abstract ideas. Adolescents become aware of the world of ideas that don't necessarily exist in physical form, and concepts, like justice, equality, equity, and truth take on new and profound importance. A child in the concrete operations stage might be able to talk about respect in simple terms, such as the give and take of mutual benefits (i.e., respect is when you are kind and share your things. An adolescent's description would be much more nuanced and might include a discussion of equality and fairness (another abstract yet real concept).\n\n
Adolescents are also able to think about multiple dimensions of a problem or situation and the way various factors combine to influence an observed outcome. For example, when faced with a dress code violation at school, a high school student might be able to see how the policy creates a standard against which all students are held, while also arguing against the lost class time that being sent home to change entails. Seeing the irony of such a situation is a hallmark of adolescent thinking and may lead to frustration and de-idealization of the adults who control their world. An appreciation of sarcasm, which relies on the ability to think in multiple dimensions and from multiple perspectives, also emerges in adolescence (Glenwright et al., 2017). Not only can adolescents begin to understand when sarcasm is being used, but they can begin to understand its functional use in public discourse. Questioning rules, especially rules that seem arbitrary, is another hallmark of the adolescent experience.\n\n
Because they can now think about possibilities, in both abstract ways and in multiple dimensions, adolescents also develop relativistic thinking, which is the belief that most truths and statements of fact are relative to the position of the observer (Chandler et al., 1990). Prior to this stage, children tend to think in absolutes (e.g., right versus wrong; good versus bad). Adolescents who have developed more relativistic thinking can simultaneously evaluate the possibility that both positions can exist, depending on whose perspective you are taking. For example, if two friends are discussing whose answer on a test was correct, a teenager would be able to see how both friends could be right given the context of their examples in the answer. They could then use this information to discuss with their instructor how to gain a better understanding of the material. When all things are possible and all perspectives can be considered, everyone can seem correct . . . and everyone can seem wrong. It's a matter of perspective."""
    },
    'p16': {
        'id': 'sociology_1_1',
        'title': 'Passage',
        'text': """All sociologists are interested in the experiences of individuals and how those experiences are shaped by interactions with social groups and society. To a sociologist, the personal decisions an individual makes do not exist in a vacuum. Cultural patterns, social forces and influences put pressure on people to select one choice over another. Sociologists try to identify these general patterns by examining the behavior of large groups of people living in the same society and experiencing the same societal pressures.\n\n
Consider the changes in U.S. families. The "typical" family in past decades consisted of married parents living in a home with their unmarried children. Today, the percent of unmarried couples, same-sex couples, single-parent and single-adult households is increasing, as well as is the number of expanded households, in which extended family members such as grandparents, cousins, or adult children live together in the family home. While 15 million mothers still make up the majority of single parents, 3.5 million fathers are also raising their children alone (U.S. Census Bureau, 2020).\n\n
Some sociologists study social facts—the laws, morals, values, religious beliefs, customs, fashions, rituals, and cultural rules that govern social life—that may contribute to these changes in the family. Do people in the United States view marriage and family differently over the years? Do employment and economic conditions play a role in families? Other sociologists are studying the consequences of these new patterns, such as the ways children influence and are influenced by them and/or the changing needs for education, housing, and healthcare.\n\n
Sociologists identify and study patterns related to all kinds of contemporary social issues. The "Stop and Frisk" policy, the emergence of new political factions, how Twitter influences everyday communication—these are all examples of topics that sociologists might explore.\n\n
A key component of the sociological perspective is the idea that the individual and society are inseparable. It is impossible to study one without the other. German sociologist Norbert Elias called the process of simultaneously analyzing the behavior of individuals and the society that shapes that behavior figuration.\n\n
Consider religion. While people experience religion in a distinctly individual manner, religion exists in a larger social context as a social institution. For instance, an individual's religious practice may be influenced by what government dictates, holidays, teachers, places of worship, rituals, and so on. In simpler terms, figuration means that as one analyzes the social institutions in a society, the individuals using that institution in any fashion need to be 'figured' in to the analysis."""
    },
    'p17': {
        'id': 'sociology_11_2',
        'title': 'Passage',
        'text': """
Functionalism\n\n
Functionalism emphasizes that all the elements of society have functions that promote solidarity and maintain order and stability in society. Hence, we can observe people from various racial and ethnic backgrounds interacting harmoniously in a state of social balance. Problems arise when one or more racial or ethnic groups experience inequalities and discriminations. This creates tension and conflict resulting in temporary dysfunction of the social system. To restore the society's pre-disturbed state or to seek a new equilibrium, the police department and various parts of the system require changes and compensatory adjustments.\n\n
Another way to apply the functionalist perspective to race and ethnicity is to discuss the way racism can contribute positively to the functioning of society by strengthening bonds between in-group members through the ostracism of out-group members. Consider how a community might increase solidarity by refusing to allow outsiders access. On the other hand, Rose (1951) suggested that dysfunctions associated with racism include the failure to take advantage of talent in the subjugated group, and that society must divert from other purposes the time and effort needed to maintain artificially constructed racial boundaries.\n\n
In the view of functionalism, racial and ethnic inequalities must have served an important function in order to exist as long as they have. Nash (1964) focused his argument on the way racism is functional for the dominant group, for example, suggesting that racism morally justifies a racially unequal society.\n\n
Interactionism\n\n
For symbolic interactionists, race and ethnicity provide strong symbols as sources of identity. In fact, some interactionists propose that the symbols of race, not race itself, are what lead to racism. Famed Interactionist Herbert Blumer (1958) suggested that racial prejudice is formed through interactions between members of the dominant group: Without these interactions, individuals in the dominant group would not hold racist views. These interactions contribute to an abstract picture of the subordinate group that allows the dominant group to support its view of the subordinate group, and thus maintains the status quo. An example of this might be an individual whose beliefs about a particular group are based on images conveyed in popular media, and those are unquestionably believed because the individual has never personally met a member of that group.\n\n
Another way to apply the interactionist perspective is to look at how people define their races and the race of others. Some people who claim a White identity have a greater amount of skin pigmentation than some people who claim a Black identity; how did they come to define themselves as Black or White?"""
    },
    'p18': {
        'id': 'sociology_3_1',
        'title': 'Passage',
        'text': """Although human societies have much in common, cultural differences are far more prevalent than cultural universals. For example, while all cultures have language, analysis of conversational etiquette reveals tremendous differences. In some Middle Eastern cultures, it is common to stand close to others in conversation. Americans keep more distance and maintain a large "personal space." Additionally, behaviors as simple as eating and drinking vary greatly from culture to culture. Some cultures use tools to put the food in the mouth while others use their fingers. If your professor comes into an early morning class holding a mug of liquid, what do you assume they are drinking? In the U.S., it's most likely filled with coffee, not Earl Grey tea, a favorite in England, or Yak Butter tea, a staple in Tibet.\n\n
Often, however, people express disgust at another culture's cuisine. They might think that it's gross to eat raw meat from a donkey or parts of a rodent, while they don't question their own habit of eating cows or pigs.\n\n
Such attitudes are examples of ethnocentrism, which means to evaluate and judge another culture based on one's own cultural norms. Ethnocentrism is believing your group is the correct measuring standard and if other cultures do not measure up to it, they are wrong. As sociologist William Graham Sumner (1906) described the term, it is a belief or attitude that one's own culture is better than all others. Almost everyone is a little bit ethnocentric.\n\n
A high level of appreciation for one's own culture can be healthy. A shared sense of community pride, for example, connects people in a society. But ethnocentrism can lead to disdain or dislike of other cultures and could cause misunderstanding, stereotyping, and conflict. Cultural imperialism is the deliberate imposition of one's own cultural values on another culture.\n\n
Colonial expansion by Portugal, Spain, Netherlands, and England grew quickly in the fifteenth century was accompanied by severe cultural imperialism. European colonizers often viewed the people in these new lands as uncultured savages who needed to adopt Catholic governance, Christianity, European dress, and other cultural practices.\n\n
A modern example of cultural imperialism may include the work of international aid agencies who introduce agricultural methods and plant species from developed countries into areas that are better served by indigenous varieties and agricultural approaches to the particular region. Another example would be the deforestation of the Amazon Basin as indigenous cultures lose land to timber corporations."""
    },
    'p19': {
        'id': 'sociology_4_1',
        'title': 'Passage',
        'text': """In the eighteenth century, Europe experienced a dramatic rise in technological invention, ushering in an era known as the Industrial Revolution. What made this period remarkable was the number of new inventions that influenced people's daily lives. Within a generation, tasks that had until this point required months of labor became achievable in a matter of days. Before the Industrial Revolution, work was largely person- or animal-based, and relied on human workers or horses to power mills and drive pumps.\n\n
Steam power began appearing everywhere. Instead of paying artisans to painstakingly spin wool and weave it into cloth, people turned to textile mills that produced fabric quickly at a better price and often with better quality. Rather than planting and harvesting fields by hand, farmers were able to purchase mechanical seeders and threshing machines that caused agricultural productivity to soar. Products such as paper and glass became available to the average person, and the quality and accessibility of education and health care soared. Gas lights allowed increased visibility in the dark, and towns and cities developed a nightlife.\n\n
One of the results of increased productivity and technology was the rise of urban centers. Workers flocked to factories for jobs, and the populations of cities became increasingly diverse. The new generation became less preoccupied with maintaining family land and traditions and more focused on acquiring wealth and achieving upward mobility for themselves and their families. People wanted their children and their children's children to continue to rise to the top, and as capitalism increased, so did social mobility.\n\n
It was during the eighteenth and nineteenth centuries of the Industrial Revolution that sociology was born. Life was changing quickly and the long-established traditions of the agricultural eras did not apply to life in the larger cities. Masses of people were moving to new environments and often found themselves faced with horrendous conditions of filth, overcrowding, and poverty. Social scientists emerged to study the relationship between the individual members of society and society as a whole.\n\n
It was during this time that power moved from the hands of the aristocracy and "old money" to business-savvy newcomers who amassed fortunes in their lifetimes. Families such as the Rockefellers and the Vanderbilts became the new power players and used their influence in business to control aspects of government as well. Eventually, concerns over the exploitation of workers led to the formation of labor unions and laws that set mandatory conditions for employees. Although the introduction of new technology at the end of the nineteenth century ended the industrial age, much of our social structure and social ideas—like family, childhood, and time standardization—have a basis in industrial society."""
    },
    'p20': {
        'id': 'sociology_5_2',
        'title': 'Passage',
        'text': """Some experts assert that who we are is a result of nurture—the relationships and caring that surround us. Others argue that who we are is based entirely in genetics. According to this belief, our temperaments, interests, and talents are set before birth. From this perspective, then, who we are depends on nature.\n\n
One way researchers attempt to measure the impact of nature is by studying twins. Some studies have followed identical twins who were raised separately. The pairs shared the same genetics but in some cases were socialized in different ways. Instances of this type of situation are rare, but studying the degree to which identical twins raised apart are the same and different can give researchers insight into the way our temperaments, preferences, and abilities are shaped by our genetic makeup versus our social environment.\n\n
For example, in 1968, twin girls were put up for adoption, separated from each other, and raised in different households. The adoptive parents, and certainly the babies, did not realize the girls were one of five pairs of twins who were made subjects of a scientific study (Flam 2007).\n\n
In 2003, the two women, then age thirty-five, were reunited. Elyse Schein and Paula Bernstein sat together in awe, feeling like they were looking into a mirror. Not only did they look alike but they also behaved alike, using the same hand gestures and facial expressions (Spratling 2007). Studies like these point to the genetic roots of our temperament and behavior.\n\n
Though genetics and hormones play an important role in human behavior, sociology's larger concern is the effect society has on human behavior, the "nurture" side of the nature versus nurture debate. What race were the twins? From what social class were their parents? All these factors affected the lives of the twins as much as their genetic makeup and are critical to consider as we look at life through the sociological lens.\n\n
Sociologists all recognize the importance of socialization for healthy individual and societal development. Structural functionalists would say that socialization is essential to society, both because it trains members to operate successfully within it and because it perpetuates culture by transmitting it to new generations. A conflict theorist might argue that socialization reproduces inequality from generation to generation by conveying different expectations and norms to those with different social characteristics. For example, individuals are socialized differently by gender, social class, and race. As in Chris Langan's case, this creates different (unequal) opportunities. An interactionist studying socialization is concerned with face-to-face exchanges and symbolic communication. For example, dressing baby boys in blue and baby girls in pink is one small way we convey messages about differences in gender roles."""
    },
}


QUESTIONS = {'p1': {'id': 'anthropology_1_2',
        'questions': {'baseline': [{'question_id': 'baseline_anthropology_1_2_1',
                                    'prompt': 'What did Carel van Schaik discover about orangutans '
                                              'during his study in Sumatra?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They prefer solitude and avoid social '
                                                         'interactions.'},
                                                {'id': 'b',
                                                 'text': 'B) They are less intelligent than '
                                                         'previously thought.'},
                                                {'id': 'c',
                                                 'text': 'C) They are more social and use a wide '
                                                         'variety of tools.'},
                                                {'id': 'd',
                                                 'text': 'D) They have no ability to learn new '
                                                         'skills.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_anthropology_1_2_2',
                                    'prompt': 'According to Lynne Isbell, what role did snakes '
                                              'play in human evolution?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They were a primary food source for '
                                                         'early humans.'},
                                                {'id': 'b',
                                                 'text': 'B) They contributed to the development '
                                                         'of human language and sight.'},
                                                {'id': 'c',
                                                 'text': 'C) They had no significant impact on '
                                                         'human evolution.'},
                                                {'id': 'd',
                                                 'text': 'D) They caused the extinction of early '
                                                         'hominins.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX1',
                                    'prompt': 'Which of the following is NOT an animal?',
                                    'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                {'id': 'b', 'text': 'B) Elephant'},
                                                {'id': 'c', 'text': 'C) Giraffe'},
                                                {'id': 'd', 'text': 'D) Computer'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_anthropology_1_2_3',
                                    'prompt': 'What might be a consequence of habitat loss and '
                                              'illegal hunting for primates, according to the '
                                              'text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Primates will become more social.'},
                                                {'id': 'b',
                                                 'text': 'B) Human intelligence will decline.'},
                                                {'id': 'c',
                                                 'text': 'C) The survival of primates is '
                                                         'threatened.'},
                                                {'id': 'd',
                                                 'text': 'D) Primates will migrate to urban '
                                                         'areas.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_anthropology_1_2_4',
                                    'prompt': 'Why might biological anthropologists study the '
                                              'genetic makeup of contemporary humans?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) To find ways to improve human genetic '
                                                         'traits.'},
                                                {'id': 'b',
                                                 'text': 'B) To create a universal human genetic '
                                                         'profile.'},
                                                {'id': 'c',
                                                 'text': 'C) To understand ancient human diets.'},
                                                {'id': 'd',
                                                 'text': 'D) To learn how certain genes and traits '
                                                         'are distributed across environments.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_anthropology_1_2_5',
                                    'prompt': 'What is the main focus of the text on biological '
                                              'anthropology?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The study of fossils and ancient '
                                                         'human remains exclusively.'},
                                                {'id': 'b',
                                                 'text': 'B) The impact of modern technology on '
                                                         'human evolution.'},
                                                {'id': 'c',
                                                 'text': 'C) The exploration of human origins, '
                                                         'evolution, and biological diversity '
                                                         'through various methods.'},
                                                {'id': 'd',
                                                 'text': 'D) Primatology as the only significant '
                                                         'area of study in anthropology.'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_anthropology_1_2_1',
                                    'prompt': 'Q1: Which combination of research approaches is '
                                              'used in biological anthropology to investigate '
                                              'human evolution?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Fossil record, genetics, linguistics, '
                                                         'archaeology, and geography.'},
                                                {'id': 'b',
                                                 'text': 'B) Fossil record, genetic data, primate '
                                                         'studies, neuroscience, and geography.'},
                                                {'id': 'c',
                                                 'text': 'C) Genetics, primate studies, '
                                                         'archaeology, ecology, and linguistics.'},
                                                {'id': 'd',
                                                 'text': 'D) Neuroscience, geography, cultural '
                                                         'ethnography, economics, and political '
                                                         'science.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_anthropology_1_2_2',
                                    'prompt': "Q2: What adaptations does Isbell's snake detection "
                                              'theory propose primates evolved in response to '
                                              'snake threats?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Greater manual skill for tool use to '
                                                         'capture snakes.'},
                                                {'id': 'b',
                                                 'text': 'B) Heightened smell and nocturnal habits '
                                                         'to avoid predators.'},
                                                {'id': 'c',
                                                 'text': 'C) Larger teeth and threat displays to '
                                                         'deter reptile attacks.'},
                                                {'id': 'd',
                                                 'text': 'D) Refined vision and communication to '
                                                         'warn of venomous snakes.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'QX3',
                                    'prompt': 'Select Option B below',
                                    'choices': [{'id': 'a', 'text': 'A) Red'},
                                                {'id': 'b', 'text': 'B) Green'},
                                                {'id': 'c', 'text': 'C) Blue'},
                                                {'id': 'd', 'text': 'D) Yellow'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_anthropology_1_2_3',
                                    'prompt': 'Q3: Which inference is best supported by van '
                                              "Schaik's findings that orangutans use tools and "
                                              'transmit skills to their young?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Cultural learning and problem-solving '
                                                         'likely reflect capacities that predate '
                                                         'humans and extend across primates.'},
                                                {'id': 'b',
                                                 'text': 'B) Human cultural distinctiveness arises '
                                                         'chiefly from language shaped by '
                                                         'ancestral snake-related threats.'},
                                                {'id': 'c',
                                                 'text': 'C) Orangutan societies exhibit cognition '
                                                         'and traditions essentially on par with '
                                                         'those of humans.'},
                                                {'id': 'd',
                                                 'text': 'D) Their tool behaviors are probably '
                                                         'products of captivity or training rather '
                                                         'than natural development.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_anthropology_1_2_4',
                                    'prompt': 'Q4: If the pressures of habitat loss, illegal '
                                              'hunting, and the pet trade persist, what is the '
                                              'most likely impact on research into human '
                                              'evolution?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) A pivot to fossil evidence that would '
                                                         'largely supplant insights from observing '
                                                         'living species.'},
                                                {'id': 'b',
                                                 'text': 'B) Diminished access to living '
                                                         'comparative models, constraining '
                                                         'inferences about human origins.'},
                                                {'id': 'c',
                                                 'text': 'C) Expanded testing of the '
                                                         'snake-detection theory, compensating for '
                                                         'the loss of field observations of apes.'},
                                                {'id': 'd',
                                                 'text': 'D) Greater emphasis on genetic surveys '
                                                         'of contemporary populations, yielding '
                                                         'similar clarity about early evolution.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_anthropology_1_2_5',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Biological anthropology integrates '
                                                         'evidence from primates, fossils, and '
                                                         'genetics to explain human origins, '
                                                         'evolution, and diversity.'},
                                                {'id': 'b',
                                                 'text': 'B) Primate research shows orangutans are '
                                                         'social, use tools, and pass skills to '
                                                         'offspring, revising earlier '
                                                         'assumptions.'},
                                                {'id': 'c',
                                                 'text': 'C) Scientists map hominin emergence and '
                                                         'migrations and analyze modern genetics '
                                                         'to chart trait distributions among human '
                                                         'groups.'},
                                                {'id': 'd',
                                                 'text': 'D) The snake detection theory links '
                                                         "venomous predators to primates' "
                                                         'specialized vision and communication, '
                                                         'echoed in fear and folklore.'}],
                                    'correct_choice_id': 'a'}]}},
 'p2': {'id': 'anthropology_1_3',
        'questions': {'baseline': [{'question_id': 'baseline_anthropology_1_3_6',
                                    'prompt': 'What did Christopher Ball study in the community of '
                                              'the Wauja?',
                                    'choices': [{'id': 'a', 'text': 'A) Traditional Wauja dances'},
                                                {'id': 'b', 'text': 'B) Ritual uses of language'},
                                                {'id': 'c', 'text': 'C) Agricultural practices'},
                                                {'id': 'd', 'text': 'D) Religious beliefs'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_anthropology_1_3_7',
                                    'prompt': "What specific purpose does 'chief speech' serve in "
                                              'the Wauja community?',
                                    'choices': [{'id': 'a', 'text': 'A) Healing the sick'},
                                                {'id': 'b', 'text': 'B) Asserting power'},
                                                {'id': 'c', 'text': 'C) Conducting exchanges'},
                                                {'id': 'd', 'text': 'D) Naming ceremonies'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX2',
                                    'prompt': 'Select color from the following:',
                                    'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                {'id': 'b', 'text': 'B) Rabbit'},
                                                {'id': 'c', 'text': 'C) Yellow'},
                                                {'id': 'd', 'text': 'D) Cat'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_anthropology_1_3_8',
                                    'prompt': 'Why might linguistic anthropologists be interested '
                                              'in public speeches delivered by indigenous leaders?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) To study the syntax used in '
                                                         'indigenous languages'},
                                                {'id': 'b',
                                                 'text': 'B) To understand how language is used in '
                                                         'political resistance'},
                                                {'id': 'c',
                                                 'text': 'C) To learn about traditional '
                                                         'storytelling methods'},
                                                {'id': 'd',
                                                 'text': 'D) To document rare languages'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_anthropology_1_3_9',
                                    'prompt': "What can be inferred about the role of 'healthy "
                                              "talk' in addiction therapy programs?",
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It is used to diagnose mental health '
                                                         'conditions'},
                                                {'id': 'b',
                                                 'text': 'B) It helps patients express emotions '
                                                         'creatively'},
                                                {'id': 'c',
                                                 'text': 'C) It reinforces societal norms about '
                                                         'behavior'},
                                                {'id': 'd',
                                                 'text': 'D) It encourages patients to speak in '
                                                         'unscripted ways'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_anthropology_1_3_10',
                                    'prompt': 'What is the main focus of the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The differences between linguistic '
                                                         'and cultural anthropology'},
                                                {'id': 'b',
                                                 'text': 'B) The impact of language on political '
                                                         'systems'},
                                                {'id': 'c',
                                                 'text': 'C) The role of language in shaping '
                                                         'cultures and identities'},
                                                {'id': 'd',
                                                 'text': 'D) The challenges of preserving '
                                                         'indigenous languages'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_anthropology_1_3_6',
                                    'prompt': 'Q1: How do linguistic anthropologists characterize '
                                              'language and what do they study about it?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) As a culture-making medium linking '
                                                         'biology and society; they study its '
                                                         'origins, cognitive effects, and roles in '
                                                         'community and identity.'},
                                                {'id': 'b',
                                                 'text': 'B) As a fixed genetic trait shaped by '
                                                         'evolution; they focus on inherited '
                                                         'grammar modules and uniform language '
                                                         'instincts across populations.'},
                                                {'id': 'c',
                                                 'text': 'C) As a message channel for transferring '
                                                         'data; they emphasize efficiency, noise '
                                                         'reduction, and accuracy rather than '
                                                         'social meaning or authority.'},
                                                {'id': 'd',
                                                 'text': 'D) As a neutral code detached from '
                                                         'social life; they prioritize cataloging '
                                                         'phonemes, morphemes, and prescriptive '
                                                         'rules over context and use.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_anthropology_1_3_7',
                                    'prompt': 'Q2: What social action is associated with "bringing '
                                              'the spirits" in Wauja speech?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Conducting exchanges between '
                                                         'indigenous groups.'},
                                                {'id': 'b',
                                                 'text': "B) Delivering leaders' formal "
                                                         'addresses.'},
                                                {'id': 'c',
                                                 'text': 'C) Giving people their names.'},
                                                {'id': 'd', 'text': 'D) Healing the sick.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'requesta_anthropology_1_3_8',
                                    'prompt': "Q3: What broader conclusion about language's role "
                                              "in political life is supported by Ball's findings "
                                              'on Wauja speeches and state discourse?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It both empowers communities to '
                                                         'contest projects and equips officials to '
                                                         'enforce hierarchy.'},
                                                {'id': 'b',
                                                 'text': 'B) It mainly preserves ritual traditions '
                                                         'and identities rather than shaping who '
                                                         'holds influence.'},
                                                {'id': 'c',
                                                 'text': 'C) It mostly mirrors cognitive patterns '
                                                         'and has limited impact on collective '
                                                         'action.'},
                                                {'id': 'd',
                                                 'text': 'D) It promotes neutral exchanges that '
                                                         'ease tensions between communities and '
                                                         'institutions.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_anthropology_1_3_9',
                                    'prompt': 'Q4: What is the most reasonable inference about how '
                                              'client progress is validated in a treatment setting '
                                              'that emphasizes scripted "healthy talk"?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Mastery of the promoted discourse is '
                                                         'taken to produce inner transformation.'},
                                                {'id': 'b',
                                                 'text': 'B) Progress is determined chiefly by '
                                                         'clinical biomarkers rather than spoken '
                                                         'accounts.'},
                                                {'id': 'c',
                                                 'text': 'C) Progress is recognized when clients '
                                                         "echo the program's set phrasing."},
                                                {'id': 'd',
                                                 'text': 'D) Staff favor spontaneous, '
                                                         'individualized reflections over '
                                                         'rehearsed formulations.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'QX1',
                                    'prompt': 'Which of the following is NOT an animal?',
                                    'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                {'id': 'b', 'text': 'B) Elephant'},
                                                {'id': 'c', 'text': 'C) Giraffe'},
                                                {'id': 'd', 'text': 'D) Computer'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'requesta_anthropology_1_3_10',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Counseling programs demonstrate that '
                                                         'scripted "healthy talk" can treat '
                                                         'addiction by reshaping how patients '
                                                         'describe themselves to staff and peers '
                                                         'and measure progress.'},
                                                {'id': 'b',
                                                 'text': 'B) Linguistic anthropology explains how '
                                                         'language makes culture and social life, '
                                                         'from evolution to everyday practice, '
                                                         'using ethnography to show speech shaping '
                                                         'identity, authority, and resistance.'},
                                                {'id': 'c',
                                                 'text': 'C) The central task of the field is '
                                                         'documenting endangered languages, such '
                                                         'as Wauja speech genres, to preserve '
                                                         'traditions, maintain identity, and '
                                                         'prevent marginalization.'},
                                                {'id': 'd',
                                                 'text': 'D) The discipline primarily traces '
                                                         "language's evolutionary origins and "
                                                         'cognitive benefits, giving brief '
                                                         'attention to culture while downplaying '
                                                         'how speech operates in power, identity, '
                                                         'and resistance.'}],
                                    'correct_choice_id': 'b'}]}},
 'p3': {'id': 'anthropology_2_3',
        'questions': {'baseline': [{'question_id': 'baseline_anthropology_2_3_11',
                                    'prompt': 'What perspective involves judging a culture by the '
                                              "standards of one's own culture?",
                                    'choices': [{'id': 'a', 'text': 'A) Etic perspective'},
                                                {'id': 'b', 'text': 'B) Emic perspective'},
                                                {'id': 'c', 'text': 'C) Feminist perspective'},
                                                {'id': 'd', 'text': 'D) Indigenous perspective'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'baseline_anthropology_2_3_12',
                                    'prompt': 'Who was the female anthropologist whose publication '
                                              'in 1928 brought prominence to women in the field?',
                                    'choices': [{'id': 'a', 'text': 'A) Ruth Benedict'},
                                                {'id': 'b', 'text': 'B) Margaret Mead'},
                                                {'id': 'c', 'text': 'C) Zora Neale Hurston'},
                                                {'id': 'd', 'text': 'D) Mary Leakey'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX5',
                                    'prompt': 'Choose Option B to show that you are reading '
                                              'carefully',
                                    'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                {'id': 'b', 'text': 'B) London'},
                                                {'id': 'c', 'text': 'C) Tokyo'},
                                                {'id': 'd', 'text': 'D) Rome'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_anthropology_2_3_13',
                                    'prompt': 'What can be inferred about the impact of male '
                                              'dominance in early anthropology studies?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It led to a comprehensive '
                                                         'understanding of all cultural roles.'},
                                                {'id': 'b',
                                                 'text': 'B) It resulted in biased interpretations '
                                                         'focused primarily on male roles and '
                                                         'perspectives.'},
                                                {'id': 'c',
                                                 'text': 'C) It accurately depicted gender roles '
                                                         'in early societies.'},
                                                {'id': 'd',
                                                 'text': 'D) It prevented the study of non-Western '
                                                         'cultures.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_anthropology_2_3_14',
                                    'prompt': 'What might be a reason for the emergence of '
                                              'Indigenous anthropology in the 1970s?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) A decline in interest in traditional '
                                                         'anthropological methods.'},
                                                {'id': 'b',
                                                 'text': 'B) An increase in funding for Indigenous '
                                                         'studies.'},
                                                {'id': 'c',
                                                 'text': 'C) The entry of more minority group '
                                                         'members into the field, providing '
                                                         'diverse perspectives.'},
                                                {'id': 'd',
                                                 'text': 'D) A shift in focus to studying only '
                                                         'Western societies.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_anthropology_2_3_15',
                                    'prompt': 'What is the main idea of the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The history of anthropology is '
                                                         'primarily about male anthropologists.'},
                                                {'id': 'b',
                                                 'text': 'B) Indigenous anthropology has become '
                                                         'the dominant subfield in modern times.'},
                                                {'id': 'c',
                                                 'text': 'C) Anthropology has evolved to include '
                                                         'diverse perspectives, addressing biases '
                                                         'and expanding the scope of research.'},
                                                {'id': 'd',
                                                 'text': 'D) Feminist anthropology focuses only on '
                                                         "women's roles in society."}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_anthropology_2_3_11',
                                    'prompt': 'Q1: Why do contemporary ethnographers consult '
                                              'informants of different genders, ages, and roles?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Because a single individual cannot '
                                                         'provide a complete or authoritative '
                                                         'account.'},
                                                {'id': 'b',
                                                 'text': 'B) To align interpretations with the '
                                                         "standards of the researcher's own "
                                                         'society.'},
                                                {'id': 'c',
                                                 'text': 'C) To maintain an emic stance throughout '
                                                         'the investigation.'},
                                                {'id': 'd',
                                                 'text': "D) To prioritize women's experiences "
                                                         "over men's in analysis."}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_anthropology_2_3_12',
                                    'prompt': 'Q2: How did feminist anthropology respond to male '
                                              'bias in earlier ethnographies?',
                                    'choices': [{'id': 'a',
                                                 'text': "A) Broadening inquiry to women's "
                                                         'economic, social, family, marriage, and '
                                                         'child-rearing roles, and using emic '
                                                         'interpretations.'},
                                                {'id': 'b',
                                                 'text': 'B) Concentrating inquiry on '
                                                         'male-dominated arenas such as warfare, '
                                                         'political leadership, and public ritual '
                                                         'to standardize cross-cultural '
                                                         'comparison.'},
                                                {'id': 'c',
                                                 'text': 'C) Confirming that early societies '
                                                         'generally assigned women subordinate '
                                                         'status relative to men across cultures.'},
                                                {'id': 'd',
                                                 'text': 'D) Replacing emic perspectives with etic '
                                                         "analyses rooted in the researcher's own "
                                                         'society to promote analytical clarity.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_anthropology_2_3_13',
                                    'prompt': 'Q3: Which outcome is most plausible as more women, '
                                              'minority, and Indigenous anthropologists '
                                              'participate in ethnographic research?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Fewer culture-bound readings and a '
                                                         'wider range of topics.'},
                                                {'id': 'b',
                                                 'text': 'B) Little change, since consulting '
                                                         'multiple informants already balances '
                                                         'viewpoints.'},
                                                {'id': 'c',
                                                 'text': 'C) More reliance on outsider analytic '
                                                         'frames to preserve objectivity across '
                                                         'cases.'},
                                                {'id': 'd',
                                                 'text': 'D) Stronger support for earlier claims '
                                                         'about male-dominated roles in past '
                                                         'societies.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'QX5',
                                    'prompt': 'Choose Option B to show that you are reading '
                                              'carefully',
                                    'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                {'id': 'b', 'text': 'B) London'},
                                                {'id': 'c', 'text': 'C) Tokyo'},
                                                {'id': 'd', 'text': 'D) Rome'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_anthropology_2_3_14',
                                    'prompt': 'Q4: An anthropologist conducts fieldwork by '
                                              'speaking mostly with older men who hold similar '
                                              'roles in the community. What is the most likely '
                                              'effect on the ethnographic account?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It would increase accuracy because '
                                                         'similar informants provide more reliable '
                                                         'data.'},
                                                {'id': 'b',
                                                 'text': 'B) It would reduce the chance of bias by '
                                                         'narrowing the range of viewpoints.'},
                                                {'id': 'c',
                                                 'text': 'C) It would skew the portrayal toward '
                                                         'their perspectives and omit important '
                                                         'dimensions.'},
                                                {'id': 'd',
                                                 'text': 'D) It would strengthen cultural '
                                                         'interpretation by promoting a consistent '
                                                         'insider stance.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'requesta_anthropology_2_3_15',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It claims feminist anthropology made '
                                                         'family, marriage, and child‑rearing the '
                                                         "field's central focus and primary lens."},
                                                {'id': 'b',
                                                 'text': 'B) It emphasizes emic, multi‑informant '
                                                         'ethnography that counters earlier male '
                                                         'and ethnocentric bias while widening who '
                                                         'participates and what is studied.'},
                                                {'id': 'c',
                                                 'text': 'C) It holds that insider scholars now '
                                                         'provide the most authoritative and '
                                                         'complete accounts, so anthropologists '
                                                         'increasingly rely on them for cultural '
                                                         'description and analysis.'},
                                                {'id': 'd',
                                                 'text': 'D) It says ethnography mainly turns on '
                                                         'choosing between etic and emic methods, '
                                                         'with findings determined by that single '
                                                         'choice.'}],
                                    'correct_choice_id': 'b'}]}},
 'p4': {'id': 'anthropology_4_4',
        'questions': {'baseline': [{'question_id': 'baseline_anthropology_4_4_16',
                                    'prompt': 'Which of the following is NOT one of the five main '
                                              'components of natural selection mentioned in the '
                                              'text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) All organisms show variation.'},
                                                {'id': 'b',
                                                 'text': 'B) Variations, or traits, are passed on '
                                                         'to offspring.'},
                                                {'id': 'c',
                                                 'text': 'C) All organisms can evolve new species '
                                                         'spontaneously.'},
                                                {'id': 'd',
                                                 'text': 'D) Small changes in every generation '
                                                         'lead to major changes over time.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_anthropology_4_4_17',
                                    'prompt': "Who introduced the term 'survival of the fittest'?",
                                    'choices': [{'id': 'a', 'text': 'A) Charles Darwin'},
                                                {'id': 'b', 'text': 'B) Herbert Spencer'},
                                                {'id': 'c', 'text': 'C) Alfred Russel Wallace'},
                                                {'id': 'd', 'text': 'D) Thomas Malthus'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX1',
                                    'prompt': 'Which of the following is NOT an animal?',
                                    'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                {'id': 'b', 'text': 'B) Elephant'},
                                                {'id': 'c', 'text': 'C) Giraffe'},
                                                {'id': 'd', 'text': 'D) Computer'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_anthropology_4_4_18',
                                    'prompt': 'Which of the following can be inferred about the '
                                              'effect of the Industrial Revolution on peppered '
                                              'moths?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It caused the extinction of white '
                                                         'moths.'},
                                                {'id': 'b',
                                                 'text': 'B) It led to an increase in the '
                                                         'population of black moths.'},
                                                {'id': 'c',
                                                 'text': 'C) It made moths more vulnerable to '
                                                         'predation.'},
                                                {'id': 'd',
                                                 'text': 'D) It resulted in the complete '
                                                         'disappearance of black moths in rural '
                                                         'areas.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_anthropology_4_4_19',
                                    'prompt': 'What can be inferred about the relationship between '
                                              'pesticide use and the evolution of pest species?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Pesticides have no impact on pest '
                                                         'populations.'},
                                                {'id': 'b',
                                                 'text': 'B) Pesticides lead to the immediate '
                                                         'eradication of all pests.'},
                                                {'id': 'c',
                                                 'text': 'C) Pesticides make it harder for pests '
                                                         'to survive in all environments.'},
                                                {'id': 'd',
                                                 'text': 'D) Pesticides cause pests to evolve '
                                                         'resistance over time.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_anthropology_4_4_20',
                                    'prompt': 'What is the main idea of the source text?',
                                    'choices': [{'id': 'a',
                                                 'text': "A) The history of the term 'survival of "
                                                         "the fittest' and its misapplications."},
                                                {'id': 'b',
                                                 'text': 'B) The role of natural selection in the '
                                                         'Industrial Revolution.'},
                                                {'id': 'c',
                                                 'text': 'C) The principles of natural selection '
                                                         'and examples of its impact in nature.'},
                                                {'id': 'd',
                                                 'text': 'D) The dangers of antibiotic resistance '
                                                         'and pesticide use in modern times.'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_anthropology_4_4_16',
                                    'prompt': 'Q1: How do major evolutionary changes arise over '
                                              'long periods under natural selection?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Through abrupt transformations within '
                                                         'a single generation.'},
                                                {'id': 'b',
                                                 'text': 'B) Through the accumulation of small '
                                                         'differences across generations.'},
                                                {'id': 'c',
                                                 'text': 'C) Through the inheritance of '
                                                         'characteristics acquired during life.'},
                                                {'id': 'd',
                                                 'text': 'D) Through the preferential survival of '
                                                         'the largest and fastest individuals.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_anthropology_4_4_17',
                                    'prompt': 'Q2: Which ideology promoted by Herbert Spencer '
                                              'applied biological evolution to human societies and '
                                              'is now discredited?',
                                    'choices': [{'id': 'a', 'text': 'A) Industrial melanism'},
                                                {'id': 'b', 'text': 'B) Natural selection'},
                                                {'id': 'c', 'text': 'C) Scientific racism'},
                                                {'id': 'd', 'text': 'D) Social Darwinism'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'QX1',
                                    'prompt': 'Which of the following is NOT an animal?',
                                    'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                {'id': 'b', 'text': 'B) Elephant'},
                                                {'id': 'c', 'text': 'C) Giraffe'},
                                                {'id': 'd', 'text': 'D) Computer'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'requesta_anthropology_4_4_18',
                                    'prompt': 'Q3: What pattern in trait prevalence is most '
                                              'supported when environmental conditions first '
                                              'change and later return to their prior state?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Trait frequencies can adjust to new '
                                                         'conditions, favoring suited traits, then '
                                                         'revert as previous conditions return.'},
                                                {'id': 'b',
                                                 'text': 'B) Trait frequencies can remain fairly '
                                                         'stable because short-term shifts rarely '
                                                         'outweigh existing variation.'},
                                                {'id': 'c',
                                                 'text': 'C) Trait frequencies move slowly over '
                                                         'long intervals, largely unaffected by '
                                                         'temporary environmental changes.'},
                                                {'id': 'd',
                                                 'text': 'D) Trait frequencies tend to become '
                                                         'fixed after selection, so later '
                                                         'reversals in conditions change them '
                                                         'little.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_anthropology_4_4_19',
                                    'prompt': 'Q4: What is the most likely long-term outcome when '
                                              'a single chemical control is used heavily and '
                                              'continuously against pests or bacteria?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Genetic diversity will decline, '
                                                         'making further adaptation unlikely.'},
                                                {'id': 'b',
                                                 'text': 'B) More individuals will carry '
                                                         'resistance traits, reducing '
                                                         'effectiveness.'},
                                                {'id': 'c',
                                                 'text': 'C) Repeated exposure will drive the '
                                                         'population to near elimination.'},
                                                {'id': 'd',
                                                 'text': 'D) The population will become '
                                                         'progressively easier to suppress over '
                                                         'time.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_anthropology_4_4_20',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The text analyzes the origins of '
                                                         '"survival of the fittest" and social '
                                                         'Darwinism, presenting them as the '
                                                         'central theme of evolution.'},
                                                {'id': 'b',
                                                 'text': 'B) The text argues that environmental '
                                                         'change—especially pollution—drives '
                                                         'evolution, as evidenced by the peppered '
                                                         'moth.'},
                                                {'id': 'c',
                                                 'text': 'C) The text explains how natural '
                                                         'selection operates, distinguishes '
                                                         'scientific fitness from social misuse, '
                                                         'and illustrates the process with classic '
                                                         'and modern cases.'},
                                                {'id': 'd',
                                                 'text': 'D) The text focuses on antibiotic and '
                                                         'pesticide resistance as problems created '
                                                         'by human technology rather than products '
                                                         'of selection.'}],
                                    'correct_choice_id': 'c'}]}},
 'p5': {'id': 'anthropology_9_1',
        'questions': {'baseline': [{'question_id': 'QX2',
                                    'prompt': 'Select color from the following:',
                                    'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                {'id': 'b', 'text': 'B) Rabbit'},
                                                {'id': 'c', 'text': 'C) Yellow'},
                                                {'id': 'd', 'text': 'D) Cat'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'QX5',
                                    'prompt': 'Choose Option B to show that you are reading '
                                              'carefully',
                                    'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                {'id': 'b', 'text': 'B) London'},
                                                {'id': 'c', 'text': 'C) Tokyo'},
                                                {'id': 'd', 'text': 'D) Rome'}],
                                    'correct_choice_id': 'b'}]}},
 'p6': {'id': 'history_1_2',
        'questions': {'baseline': [{'question_id': 'baseline_history_1_2_26',
                                    'prompt': 'Which of the following was a common cause of death '
                                              'for women during the Middle Ages?',
                                    'choices': [{'id': 'a', 'text': 'A) War'},
                                                {'id': 'b', 'text': 'B) Famine'},
                                                {'id': 'c', 'text': 'C) Childbirth'},
                                                {'id': 'd', 'text': 'D) Plague'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_history_1_2_27',
                                    'prompt': "What percentage of western Europe's population were "
                                              'peasants or serfs during the Middle Ages?',
                                    'choices': [{'id': 'a', 'text': 'A) 40 percent'},
                                                {'id': 'b', 'text': 'B) 50 percent'},
                                                {'id': 'c', 'text': 'C) 60 percent'},
                                                {'id': 'd', 'text': 'D) 70 percent'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'QX5',
                                    'prompt': 'Choose Option B to show that you are reading '
                                              'carefully',
                                    'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                {'id': 'b', 'text': 'B) London'},
                                                {'id': 'c', 'text': 'C) Tokyo'},
                                                {'id': 'd', 'text': 'D) Rome'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_history_1_2_28',
                                    'prompt': "Why might serfs have been considered 'effectively "
                                              "bound' to the land they worked?",
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They were legally enslaved by their '
                                                         'lords.'},
                                                {'id': 'b',
                                                 'text': 'B) They lacked the skills to survive '
                                                         'independently.'},
                                                {'id': 'c',
                                                 'text': 'C) Their livelihood and protection '
                                                         'depended on staying on the land.'},
                                                {'id': 'd',
                                                 'text': 'D) They were forbidden by the Church to '
                                                         'leave the land.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_history_1_2_29',
                                    'prompt': 'What can be inferred about the impact of the '
                                              'seasons on medieval agrarian life?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Seasons had little effect as food was '
                                                         'imported.'},
                                                {'id': 'b',
                                                 'text': 'B) Seasonal changes were crucial in '
                                                         'determining work and food supply.'},
                                                {'id': 'c',
                                                 'text': 'C) People worked indoors regardless of '
                                                         'the season.'},
                                                {'id': 'd',
                                                 'text': "D) The Church's calendar determined all "
                                                         'agricultural activities.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_history_1_2_30',
                                    'prompt': 'What is the main idea of the passage about life '
                                              'during the Middle Ages?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The Catholic Church was the sole '
                                                         'religious institution in Europe.'},
                                                {'id': 'b',
                                                 'text': 'B) Medieval life was dominated by '
                                                         'warfare and political intrigue.'},
                                                {'id': 'c',
                                                 'text': 'C) Life in the Middle Ages was dictated '
                                                         'by agrarian cycles and social '
                                                         'hierarchies.'},
                                                {'id': 'd',
                                                 'text': 'D) Technological advancements greatly '
                                                         'improved medieval living conditions.'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_history_1_2_26',
                                    'prompt': "Q1: About what proportion of western Europe's "
                                              'population were peasants or serfs in the Middle '
                                              'Ages?',
                                    'choices': [{'id': 'a', 'text': 'A) About one-third'},
                                                {'id': 'b', 'text': 'B) About two-fifths'},
                                                {'id': 'c', 'text': 'C) About three-fifths'},
                                                {'id': 'd', 'text': 'D) About four-fifths'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'requesta_history_1_2_27',
                                    'prompt': 'Q2: What outcome could result when harvests were '
                                              'ruined by bad weather, crop disease, or insects?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Butchering livestock and preserving '
                                                         'meat'},
                                                {'id': 'b',
                                                 'text': 'B) Early summer haymaking for winter '
                                                         'feed'},
                                                {'id': 'c', 'text': 'C) Mass hunger or relocation'},
                                                {'id': 'd',
                                                 'text': "D) Taking refuge behind the lord's "
                                                         'walls'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'requesta_history_1_2_28',
                                    'prompt': 'Q3: What trade-off for serfs is implied by working '
                                              '"in return for protection" while being "effectively '
                                              'bound" to the land?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Advancement widened through service '
                                                         'and trade, loosening established ranks.'},
                                                {'id': 'b',
                                                 'text': 'B) Church wealth let peasants negotiate '
                                                         'improved terms and shift between '
                                                         'estates.'},
                                                {'id': 'c',
                                                 'text': 'C) Safety and subsistence outweighed '
                                                         'personal autonomy and movement, '
                                                         'reinforcing a fixed social order.'},
                                                {'id': 'd',
                                                 'text': 'D) Seasonal work patterns let families '
                                                         'revise duties and obtain new plots when '
                                                         'needed.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'QX5',
                                    'prompt': 'Choose Option B to show that you are reading '
                                              'carefully',
                                    'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                {'id': 'b', 'text': 'B) London'},
                                                {'id': 'c', 'text': 'C) Tokyo'},
                                                {'id': 'd', 'text': 'D) Rome'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_history_1_2_29',
                                    'prompt': 'Q4: Given the described agricultural practices and '
                                              'risks, what can be inferred about medieval '
                                              "villages' capacity to handle failed harvests?",
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Church wealth supplied meaningful aid '
                                                         'during periods of scarcity.'},
                                                {'id': 'b',
                                                 'text': 'B) Manorial protection kept supplies '
                                                         'steady even when yields were poor.'},
                                                {'id': 'c',
                                                 'text': 'C) Seasonal tasks lessened dependence on '
                                                         'how the crops fared.'},
                                                {'id': 'd',
                                                 'text': 'D) Thin reserves meant bad seasons '
                                                         'quickly brought severe shortages.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'requesta_history_1_2_30',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The passage depicts feudal western '
                                                         'Europe as a Church-centered agrarian '
                                                         'society where serfdom, seasonal labor, '
                                                         'and harsh conditions shortened '
                                                         'lifespans.'},
                                                {'id': 'b',
                                                 'text': 'B) The passage focuses on how the '
                                                         'Catholic Church used tithes and rents to '
                                                         'build wealth and exert control over '
                                                         'medieval communities.'},
                                                {'id': 'c',
                                                 'text': 'C) The passage outlines the agricultural '
                                                         'calendar and the division of farm tasks '
                                                         'among men, women, and children in '
                                                         'medieval households.'},
                                                {'id': 'd',
                                                 'text': 'D) The passage describes the roles of '
                                                         'lords and knights in providing land '
                                                         'management, justice, and military '
                                                         'service within the feudal system.'}],
                                    'correct_choice_id': 'a'}]}},
 'p7': {'id': 'history_3_1',
        'questions': {'baseline': [{'question_id': 'baseline_history_3_1_31',
                                    'prompt': 'Who was ordered by King Philip II to explore the '
                                              'American southwest for Spain in the late 1590s?',
                                    'choices': [{'id': 'a', 'text': 'A) Hernando Cortés'},
                                                {'id': 'b', 'text': 'B) Francisco Pizarro'},
                                                {'id': 'c', 'text': 'C) Juan de Oñate'},
                                                {'id': 'd', 'text': 'D) Diego Velázquez'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_history_3_1_32',
                                    'prompt': 'What was the original name of Santa Fe when it was '
                                              'established as the capital?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) La Villa Real de la Santa Fe de San '
                                                         'Francisco de Asís'},
                                                {'id': 'b', 'text': 'B) Ciudad de la Nueva España'},
                                                {'id': 'c', 'text': 'C) San Juan de los Remedios'},
                                                {'id': 'd',
                                                 'text': 'D) El Pueblo de Nuestra Señora'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'baseline_history_3_1_33',
                                    'prompt': 'Why did the Pueblo people eventually reject '
                                              'Catholicism, according to the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They found it similar to their own '
                                                         'beliefs.'},
                                                {'id': 'b',
                                                 'text': 'B) They were forced to give up their '
                                                         'traditional practices.'},
                                                {'id': 'c',
                                                 'text': 'C) It brought them wealth and '
                                                         'prosperity.'},
                                                {'id': 'd',
                                                 'text': 'D) It was too complex to understand.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX2',
                                    'prompt': 'Select color from the following:',
                                    'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                {'id': 'b', 'text': 'B) Rabbit'},
                                                {'id': 'c', 'text': 'C) Yellow'},
                                                {'id': 'd', 'text': 'D) Cat'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_history_3_1_34',
                                    'prompt': 'What inference can be made about the Spanish '
                                              'explanation for their defeat in the Pueblo Revolt '
                                              'of 1680?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They believed it was due to their own '
                                                         'military weaknesses.'},
                                                {'id': 'b',
                                                 'text': 'B) They attributed it to natural '
                                                         'disasters.'},
                                                {'id': 'c',
                                                 'text': 'C) They considered it a political '
                                                         'failure.'},
                                                {'id': 'd',
                                                 'text': 'D) They thought it was the work of the '
                                                         'Devil.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_history_3_1_35',
                                    'prompt': 'What is the main idea of the passage?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The Spanish were successful in '
                                                         'converting the Pueblo people to '
                                                         'Catholicism.'},
                                                {'id': 'b',
                                                 'text': 'B) The Pueblo people willingly accepted '
                                                         'Spanish rule and religion.'},
                                                {'id': 'c',
                                                 'text': 'C) The Pueblo Revolt was a significant '
                                                         'resistance against Spanish colonization '
                                                         'efforts.'},
                                                {'id': 'd',
                                                 'text': 'D) The Spanish were primarily interested '
                                                         'in establishing trade routes.'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_history_3_1_31',
                                    'prompt': 'Q1: In what year did Spanish settlers establish '
                                              'themselves at Santa Fe?',
                                    'choices': [{'id': 'a', 'text': 'A) 1598'},
                                                {'id': 'b', 'text': 'B) 1610'},
                                                {'id': 'c', 'text': 'C) 1680'},
                                                {'id': 'd', 'text': 'D) 1692'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_history_3_1_32',
                                    'prompt': 'Q2: What immediate outcome did the 1680 Pueblo '
                                              'Revolt produce for Spanish colonists, and in what '
                                              'year was Spanish control reestablished?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It caused about 50 Spanish deaths and '
                                                         'drove a few hundred settlers south, with '
                                                         'control restored in 1681.'},
                                                {'id': 'b',
                                                 'text': 'B) It caused roughly 300 Spanish deaths '
                                                         'and sent over one thousand settlers '
                                                         'south, with control restored in 1685.'},
                                                {'id': 'c',
                                                 'text': 'C) It caused over 400 Spanish deaths and '
                                                         'drove up to two thousand settlers south, '
                                                         'with control restored in 1692.'},
                                                {'id': 'd',
                                                 'text': 'D) It caused over 400 Pueblo deaths and '
                                                         'displaced native villages, with control '
                                                         'restored in 1700.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'requesta_history_3_1_33',
                                    'prompt': 'Q3: Which factor most plausibly made sustained '
                                              'coexistence unlikely after the initial blending of '
                                              'Pueblo spirituality with Catholic practice?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Clerical demands to erase traditional '
                                                         'rites and remove children from their '
                                                         'families, deepening resentment'},
                                                {'id': 'b',
                                                 'text': 'B) Economic frustration over scarce gold '
                                                         'and silver outweighed cultural tensions '
                                                         'in straining relations'},
                                                {'id': 'c',
                                                 'text': 'C) Ongoing droughts and raids led Pueblo '
                                                         'communities to lean on Spanish '
                                                         'protection, preserving cooperation'},
                                                {'id': 'd',
                                                 'text': 'D) Spanish branding of Pueblo resistance '
                                                         'as satanic hardened views before the '
                                                         'revolt, halting blending'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'QX5',
                                    'prompt': 'Choose Option B to show that you are reading '
                                              'carefully',
                                    'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                {'id': 'b', 'text': 'B) London'},
                                                {'id': 'c', 'text': 'C) Tokyo'},
                                                {'id': 'd', 'text': 'D) Rome'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_history_3_1_34',
                                    'prompt': 'Q4: How did labeling the 1680 Pueblo uprising as '
                                              'demonic influence likely aid Spanish objectives '
                                              'when they reclaimed control in 1692?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) By branding the uprising a holy '
                                                         'contest, leaders downplayed Pueblo '
                                                         'complaints and legitimated their '
                                                         'return.'},
                                                {'id': 'b',
                                                 'text': 'B) By delaying their return until '
                                                         'drought and raids subsided, leaders '
                                                         'addressed the roots of the unrest.'},
                                                {'id': 'c',
                                                 'text': 'C) By moderating missionary demands, '
                                                         'leaders accommodated Pueblo rituals to '
                                                         'ease tensions.'},
                                                {'id': 'd',
                                                 'text': 'D) By negotiating reforms with Pueblo '
                                                         'communities, leaders prioritized '
                                                         'compromise before reentry.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_history_3_1_35',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Franciscan conversion efforts '
                                                         'dominated Spanish policy and steadily '
                                                         'won over the Pueblo in the 1600s.'},
                                                {'id': 'b',
                                                 'text': 'B) Raids and drought in the 1670s pushed '
                                                         'the Spanish to abandon New Mexico until '
                                                         'the early eighteenth century.'},
                                                {'id': 'c',
                                                 'text': 'C) Spanish expansion into Pueblo lands '
                                                         'and forceful missionizing sparked the '
                                                         '1680 Pueblo Revolt, expelling the '
                                                         'Spanish until 1692.'},
                                                {'id': 'd',
                                                 'text': 'D) The founding of Santa Fe anchored '
                                                         "Spain's northern outpost as explorers "
                                                         'sought wealth and influence.'}],
                                    'correct_choice_id': 'c'}]}},
 'p8': {'id': 'history_3_2',
        'questions': {'baseline': [{'question_id': 'baseline_history_3_2_36',
                                    'prompt': 'Who established Quebec as a French fur-trading '
                                              'outpost in the early 1600s?',
                                    'choices': [{'id': 'a', 'text': 'A) Jacques Cartier'},
                                                {'id': 'b', 'text': 'B) Samuel de Champlain'},
                                                {'id': 'c', 'text': 'C) Claude Chauchetière'},
                                                {'id': 'd', 'text': 'D) Kateri Tekakwitha'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_history_3_2_37',
                                    'prompt': 'What was the primary reason the Algonquian '
                                              'tolerated the French presence in Canada?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They wanted to convert to '
                                                         'Catholicism.'},
                                                {'id': 'b',
                                                 'text': 'B) They needed firearms for their war '
                                                         'with the Iroquois.'},
                                                {'id': 'c',
                                                 'text': 'C) They were paid with beaver pelts.'},
                                                {'id': 'd',
                                                 'text': 'D) They wanted to trade with the '
                                                         'Spanish.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX1',
                                    'prompt': 'Which of the following is NOT an animal?',
                                    'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                {'id': 'b', 'text': 'B) Elephant'},
                                                {'id': 'c', 'text': 'C) Giraffe'},
                                                {'id': 'd', 'text': 'D) Computer'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_history_3_2_38',
                                    'prompt': 'What can be inferred about the French attitude '
                                              'towards Native peoples in New France?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The French saw them as equals and '
                                                         'allies.'},
                                                {'id': 'b',
                                                 'text': 'B) The French respected their autonomy '
                                                         'and culture.'},
                                                {'id': 'c',
                                                 'text': 'C) The French viewed them as inferior '
                                                         'and pressured them to convert.'},
                                                {'id': 'd',
                                                 'text': 'D) The French avoided interaction with '
                                                         'them.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_history_3_2_39',
                                    'prompt': 'Why might the Church leaders have initially balked '
                                              'at canonizing Kateri Tekakwitha?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They believed she was not pious '
                                                         'enough.'},
                                                {'id': 'b',
                                                 'text': 'B) They were unsure of the authenticity '
                                                         'of her conversion.'},
                                                {'id': 'c',
                                                 'text': 'C) They had a policy against canonizing '
                                                         'Native Americans.'},
                                                {'id': 'd',
                                                 'text': 'D) They were hesitant to elevate a '
                                                         "'savage' to sainthood."}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_history_3_2_40',
                                    'prompt': 'What is the main idea of the text regarding the '
                                              'French colonization of Canada?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The French were primarily focused on '
                                                         'religious conversion.'},
                                                {'id': 'b',
                                                 'text': 'B) The French successfully established a '
                                                         'large population in Canada by 1640.'},
                                                {'id': 'c',
                                                 'text': 'C) The French colonization was marked by '
                                                         'alliances and conflicts with Native '
                                                         'peoples, driven by economic and '
                                                         'religious motives.'},
                                                {'id': 'd',
                                                 'text': 'D) The French had no significant impact '
                                                         'on the native populations of Canada.'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_history_3_2_36',
                                    'prompt': 'Q1: In the early 1600s, how was Quebec initially '
                                              'established, and which people did the colonists '
                                              'rely on for survival?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) As an agricultural colony; the '
                                                         'Iroquois.'},
                                                {'id': 'b',
                                                 'text': 'B) As a fur-trading outpost; the '
                                                         'Algonquian.'},
                                                {'id': 'c',
                                                 'text': 'C) As a military fort; the Dutch.'},
                                                {'id': 'd',
                                                 'text': 'D) As a missionary base; the Jesuits.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_history_3_2_37',
                                    'prompt': 'Q2: In which decade did the first Jesuit priests '
                                              'arrive in Quebec?',
                                    'choices': [{'id': 'a', 'text': 'A) 1540s'},
                                                {'id': 'b', 'text': 'B) 1620s'},
                                                {'id': 'c', 'text': 'C) 1640s'},
                                                {'id': 'd', 'text': 'D) 1660s'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'requesta_history_3_2_38',
                                    'prompt': 'Q3: Given the French view of Canada and the small '
                                              'number of settlers by 1640, what colonial approach '
                                              'did France most likely adopt in Canada?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Building large agricultural '
                                                         'settlements to secure land and replace '
                                                         'Native communities'},
                                                {'id': 'b',
                                                 'text': 'B) Developing military strongholds to '
                                                         'subdue rivals and administer direct '
                                                         'control'},
                                                {'id': 'c',
                                                 'text': 'C) Emphasizing fur-trade posts and '
                                                         'alliances with local peoples over dense '
                                                         'towns'},
                                                {'id': 'd',
                                                 'text': 'D) Establishing missionary colonies as '
                                                         'the primary engine of growth and '
                                                         'conversion'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'QX4',
                                    'prompt': 'Which of the following is the ONLY option that is a '
                                              'number?',
                                    'choices': [{'id': 'a', 'text': 'A) Seven'},
                                                {'id': 'b', 'text': 'B) Chair'},
                                                {'id': 'c', 'text': 'C) Machine'},
                                                {'id': 'd', 'text': 'D) Sidewalk'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_history_3_2_39',
                                    'prompt': 'Q4: What can be inferred about the broader '
                                              'significance of the Beaver Wars given that the '
                                              'French and the Dutch supplied firearms to opposing '
                                              'Native groups?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They extended European trade rivalry '
                                                         'as rival powers armed Indigenous '
                                                         'allies.'},
                                                {'id': 'b',
                                                 'text': 'B) They reflected intertribal rivalries '
                                                         'largely detached from European '
                                                         'commerce.'},
                                                {'id': 'c',
                                                 'text': 'C) They resulted from French plans to '
                                                         'expand permanent settlement across '
                                                         'Canada.'},
                                                {'id': 'd',
                                                 'text': 'D) They were chiefly religious clashes '
                                                         'sparked by Catholic missionary '
                                                         'campaigns.'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_history_3_2_40',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Early French Canada was sparsely '
                                                         'settled, fur-trade focused, dependent on '
                                                         'Native allies, and marked by Jesuit '
                                                         'missions, conflicts, and inequality.'},
                                                {'id': 'b',
                                                 'text': 'B) French colonization quickly expanded '
                                                         'after Cartier, producing thriving '
                                                         'settlements and cooperative, equal '
                                                         'partnerships with Indigenous nations '
                                                         'across the region.'},
                                                {'id': 'c',
                                                 'text': 'C) Jesuit missions broadly transformed '
                                                         'Indigenous societies through widespread '
                                                         'conversions and enduring acceptance of '
                                                         'French religious and political '
                                                         'authority.'},
                                                {'id': 'd',
                                                 'text': 'D) The Beaver Wars arose chiefly from '
                                                         'Dutch arms trading and remained largely '
                                                         'separate from French commerce and '
                                                         'alliances around the Great Lakes.'}],
                                    'correct_choice_id': 'a'}]}},
 'p9': {'id': 'history_3_3',
        'questions': {'baseline': [{'question_id': 'baseline_history_3_3_41',
                                    'prompt': 'What economic activity did English migrants in '
                                              'Chesapeake Bay engage in to make money?',
                                    'choices': [{'id': 'a', 'text': 'A) Gold mining'},
                                                {'id': 'b', 'text': 'B) Fur trading'},
                                                {'id': 'c', 'text': 'C) Tobacco growing'},
                                                {'id': 'd', 'text': 'D) Fishing'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'baseline_history_3_3_42',
                                    'prompt': 'Which group of English settlers was primarily '
                                              'motivated by religious reasons to migrate to North '
                                              'America?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Unmarried young Englishmen'},
                                                {'id': 'b', 'text': 'B) Puritans'},
                                                {'id': 'c', 'text': 'C) Royalists'},
                                                {'id': 'd', 'text': 'D) Merchants'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX3',
                                    'prompt': 'Select Option B below',
                                    'choices': [{'id': 'a', 'text': 'A) Red'},
                                                {'id': 'b', 'text': 'B) Green'},
                                                {'id': 'c', 'text': 'C) Blue'},
                                                {'id': 'd', 'text': 'D) Yellow'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_history_3_3_43',
                                    'prompt': 'What might be a reason Puritans decided to '
                                              'establish towns focused on the church in New '
                                              'England?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They wanted to create economic '
                                                         'opportunities through agriculture.'},
                                                {'id': 'b',
                                                 'text': 'B) They sought to separate from the '
                                                         "Church of England's practices."},
                                                {'id': 'c',
                                                 'text': 'C) They were ordered by the English '
                                                         'monarchy to do so.'},
                                                {'id': 'd',
                                                 'text': 'D) They were primarily interested in '
                                                         'commercial ventures.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'baseline_history_3_3_44',
                                    'prompt': 'What can be inferred about the impact of the '
                                              'English Civil War on the colonies?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) It strengthened the administration of '
                                                         'the colonies.'},
                                                {'id': 'b',
                                                 'text': 'B) It had no impact on the colonial '
                                                         'development.'},
                                                {'id': 'c',
                                                 'text': 'C) It caused the colonies to unify under '
                                                         'a single government.'},
                                                {'id': 'd',
                                                 'text': 'D) It led to divergent cultural '
                                                         'developments in the colonies.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'baseline_history_3_3_45',
                                    'prompt': 'What is the main idea of the source text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) The English colonization was '
                                                         'primarily motivated by economic '
                                                         'factors.'},
                                                {'id': 'b',
                                                 'text': 'B) The Chesapeake and New England '
                                                         'colonies faced similar challenges.'},
                                                {'id': 'c',
                                                 'text': 'C) The differing motivations and '
                                                         'backgrounds of English colonists led to '
                                                         'distinct regional cultures in North '
                                                         'America.'},
                                                {'id': 'd',
                                                 'text': 'D) The English Civil War had little '
                                                         'impact on the colonies.'}],
                                    'correct_choice_id': 'c'}],
                      'requesta': [{'question_id': 'requesta_history_3_3_41',
                                    'prompt': 'Q1: What was the only sure means of making money in '
                                              'the Chesapeake colonies of Virginia and Maryland?',
                                    'choices': [{'id': 'a', 'text': 'A) Growing tobacco'},
                                                {'id': 'b', 'text': 'B) Harvesting timber'},
                                                {'id': 'c', 'text': 'C) Mining gold'},
                                                {'id': 'd', 'text': 'D) Trading furs'}],
                                    'correct_choice_id': 'a'},
                                   {'question_id': 'requesta_history_3_3_42',
                                    'prompt': 'Q2: Which description best fits the early English '
                                              'settlers in New England and their town life?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Adventurers intent on discovering '
                                                         'gold, establishing temporary camps '
                                                         'oriented to mineral extraction.'},
                                                {'id': 'b',
                                                 'text': 'B) Anglican loyalists promoting '
                                                         'conformity, arranging communities under '
                                                         'centralized church direction.'},
                                                {'id': 'c',
                                                 'text': 'C) Mostly single young men pursuing '
                                                         'tobacco profits on dispersed '
                                                         'plantations.'},
                                                {'id': 'd',
                                                 'text': 'D) Puritan families driven by religious '
                                                         'aims, building church-centered towns '
                                                         'with self-governing congregations.'}],
                                    'correct_choice_id': 'd'},
                                   {'question_id': 'requesta_history_3_3_43',
                                    'prompt': 'Q3: Given the contrasting migrant profiles to the '
                                              'Chesapeake and New England, which difference in '
                                              'community life is most plausible?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) Both regions developed similar town '
                                                         'structures and family patterns, '
                                                         "regardless of differences in migrants' "
                                                         'motives.'},
                                                {'id': 'b',
                                                 'text': 'B) Chesapeake settlements had higher '
                                                         'turnover and weaker church-centered town '
                                                         'life, while New England formed stable, '
                                                         'congregation-focused communities.'},
                                                {'id': 'c',
                                                 'text': "C) New England's religious migrants "
                                                         'dispersed into isolated farmsteads with '
                                                         'minimal parish influence, while the '
                                                         'Chesapeake clustered in tight village '
                                                         'parishes.'},
                                                {'id': 'd',
                                                 'text': 'D) Tobacco profits fostered permanent, '
                                                         'family-based communities in the '
                                                         "Chesapeake, while New England's climate "
                                                         'limited stable settlement.'}],
                                    'correct_choice_id': 'b'},
                                   {'question_id': 'QX2',
                                    'prompt': 'Select color from the following:',
                                    'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                {'id': 'b', 'text': 'B) Rabbit'},
                                                {'id': 'c', 'text': 'C) Yellow'},
                                                {'id': 'd', 'text': 'D) Cat'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'requesta_history_3_3_44',
                                    'prompt': 'Q4: What outcome is most likely for New England '
                                              'towns when each congregation governed itself and '
                                              "England's upheavals disrupted imperial supervision?",
                                    'choices': [{'id': 'a',
                                                 'text': 'A) They followed detailed directives '
                                                         'from London on church and town policy.'},
                                                {'id': 'b',
                                                 'text': 'B) They modeled their institutions on '
                                                         "the Chesapeake's planter-led governance "
                                                         'structures.'},
                                                {'id': 'c',
                                                 'text': 'C) They practiced broad community-level '
                                                         'decision-making in worship and town '
                                                         'affairs.'},
                                                {'id': 'd',
                                                 'text': 'D) They prioritized cash-crop '
                                                         'agriculture over congregational and '
                                                         'local municipal concerns.'}],
                                    'correct_choice_id': 'c'},
                                   {'question_id': 'requesta_history_3_3_45',
                                    'prompt': 'Q5: Which statement best summarizes the text?',
                                    'choices': [{'id': 'a',
                                                 'text': 'A) After failing to find gold, '
                                                         'Chesapeake settlers turned to tobacco, '
                                                         'drawing many unmarried, unemployed '
                                                         'English migrants seeking work, land, and '
                                                         'profit.'},
                                                {'id': 'b',
                                                 'text': "B) England's religious and political "
                                                         'conflicts fostered contrasting colonial '
                                                         'goals—profit-driven Chesapeake '
                                                         'settlements and faith-centered New '
                                                         'England towns—resulting in divergent '
                                                         'cultures under weak imperial oversight.'},
                                                {'id': 'c',
                                                 'text': "C) English promoters' promises of "
                                                         'American riches set a uniform economic '
                                                         'agenda across the colonies, guiding '
                                                         'settlement patterns and ensuring '
                                                         'consistent imperial control.'},
                                                {'id': 'd',
                                                 'text': 'D) Puritan families migrated to New '
                                                         'England to build church-centered towns '
                                                         'where each congregation governed itself, '
                                                         'and many later returned to England '
                                                         'during the Civil War.'}],
                                    'correct_choice_id': 'b'}]}},
 'p10': {'id': 'history_3_4',
         'questions': {'baseline': [{'question_id': 'baseline_history_3_4_46',
                                     'prompt': 'What was the primary purpose of the Royal African '
                                               'Company, chartered by the English crown in 1672?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) To explore new territories in '
                                                          'Africa'},
                                                 {'id': 'b',
                                                  'text': 'B) To establish trade routes for '
                                                          'English goods'},
                                                 {'id': 'c',
                                                  'text': 'C) To transport enslaved African people '
                                                          'to the English colonies'},
                                                 {'id': 'd',
                                                  'text': 'D) To govern English colonies in '
                                                          'Africa'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_history_3_4_47',
                                     'prompt': 'By the year 1700, approximately how many enslaved '
                                               'people were there on the English sugar island of '
                                               'Barbados?',
                                     'choices': [{'id': 'a', 'text': 'A) 10,000'},
                                                 {'id': 'b', 'text': 'B) 25,000'},
                                                 {'id': 'c', 'text': 'C) 50,000'},
                                                 {'id': 'd', 'text': 'D) 75,000'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_history_3_4_48',
                                     'prompt': 'What can be inferred about the nature of African '
                                               'slavery compared to New World slavery?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) African slavery was more brutal than '
                                                          'New World slavery'},
                                                 {'id': 'b',
                                                  'text': 'B) African slavery was typically a '
                                                          'lifelong and heritable condition'},
                                                 {'id': 'c',
                                                  'text': 'C) African slavery was often temporary '
                                                          'and not based on race'},
                                                 {'id': 'd',
                                                  'text': 'D) African slavery focused on large '
                                                          'plantation work'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_history_3_4_49',
                                     'prompt': 'Why might Africans have engaged in the slave trade '
                                               'with Europeans?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) They were forced by Europeans to '
                                                          'participate'},
                                                 {'id': 'b',
                                                  'text': 'B) They wanted to explore new lands'},
                                                 {'id': 'c',
                                                  'text': 'C) They wanted to form alliances with '
                                                          'European nations'},
                                                 {'id': 'd',
                                                  'text': 'D) They traded enslaved people for '
                                                          'European goods and power'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_history_3_4_50',
                                     'prompt': 'What is the main idea of the source text?',
                                     'choices': [{'id': 'a',
                                                  'text': "A) The English crown's role in "
                                                          'colonization'},
                                                 {'id': 'b',
                                                  'text': 'B) The cultural practices of African '
                                                          'societies'},
                                                 {'id': 'c',
                                                  'text': 'C) The development of the transatlantic '
                                                          'slave trade and its impact'},
                                                 {'id': 'd',
                                                  'text': 'D) The agricultural advancements in the '
                                                          'American colonies'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_history_3_4_46',
                                     'prompt': 'Q1: About how many Africans did the Royal African '
                                               'Company transport in the four decades after its '
                                               '1672 charter?',
                                     'choices': [{'id': 'a', 'text': 'A) 50,000'},
                                                 {'id': 'b', 'text': 'B) 325,800'},
                                                 {'id': 'c', 'text': 'C) 350,000'},
                                                 {'id': 'd', 'text': 'D) 4,000,000'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_history_3_4_47',
                                     'prompt': 'Q2: Which statement best describes how slavery '
                                               'practiced by Africans differed from New World '
                                               'chattel slavery?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Centered on plantation cash crops '
                                                          'like sugar and tobacco, imposed '
                                                          'lifetime servitude, made status '
                                                          'hereditary, and was organized by racial '
                                                          'categories.'},
                                                 {'id': 'b',
                                                  'text': 'B) Depended on racial classifications '
                                                          'enforced by colonial law, oriented to '
                                                          'plantation work, and made bondage '
                                                          'perpetual and inheritable.'},
                                                 {'id': 'c',
                                                  'text': 'C) Emphasized household and small‑farm '
                                                          'labor, was often temporary and '
                                                          'nonhereditary, and was not defined by '
                                                          'race.'},
                                                 {'id': 'd',
                                                  'text': 'D) Focused on supplying plantation '
                                                          'labor via European firms, with racial '
                                                          'status and lifetime terms fixed by '
                                                          'traders and colonial statutes.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX4',
                                     'prompt': 'Which of the following is the ONLY option that is '
                                               'a number?',
                                     'choices': [{'id': 'a', 'text': 'A) Seven'},
                                                 {'id': 'b', 'text': 'B) Chair'},
                                                 {'id': 'c', 'text': 'C) Machine'},
                                                 {'id': 'd', 'text': 'D) Sidewalk'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_history_3_4_48',
                                     'prompt': "Q3: What best explains the English colonies' shift "
                                               'from servant labor to legally codified African '
                                               'chattel slavery by the late seventeenth century?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) African customs favored lifelong, '
                                                          'race-based bondage, which colonists '
                                                          'adopted unchanged.'},
                                                 {'id': 'b',
                                                  'text': 'B) Familiarity with slavery in England '
                                                          'encouraged colonists to replicate it '
                                                          'overseas.'},
                                                 {'id': 'c',
                                                  'text': 'C) Labor-intensive sugar and tobacco '
                                                          'led planters to seek a permanent, '
                                                          'inheritable workforce.'},
                                                 {'id': 'd',
                                                  'text': "D) The Royal African Company's monopoly "
                                                          'required colonies to replace servants '
                                                          'with imported captives.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_history_3_4_49',
                                     'prompt': 'Q4: What outcome for West African societies can be '
                                               'inferred from the expansion of the Atlantic slave '
                                               'trade?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) A turn to plantation agriculture in '
                                                          'West Africa that decreased reliance on '
                                                          'raiding'},
                                                 {'id': 'b',
                                                  'text': 'B) Greater cohesion as commercial gains '
                                                          'reduced incentives for conflict among '
                                                          'neighboring groups'},
                                                 {'id': 'c',
                                                  'text': 'C) Intensified conflict through raiding '
                                                          'and elevated influence of leaders '
                                                          'profiting from captives'},
                                                 {'id': 'd',
                                                  'text': 'D) Reduced authority of local elites as '
                                                          'Europeans imposed direct control over '
                                                          'inland politics'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_history_3_4_50',
                                     'prompt': 'Q5: Which of the following best expresses the main '
                                               'idea of the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Enslaved Africans in the Americas, '
                                                          'including the Chesapeake, labored for '
                                                          'life on cash-crop plantations but '
                                                          'formed maroon communities and '
                                                          'maintained spiritual traditions such as '
                                                          'Vodun.'},
                                                 {'id': 'b',
                                                  'text': 'B) Slavery in Africa differed from New '
                                                          'World slavery because it was not '
                                                          'race-based, was often temporary, and '
                                                          'was tied to households or small farms '
                                                          'rather than plantations.'},
                                                 {'id': 'c',
                                                  'text': 'C) The Atlantic slave trade, driven by '
                                                          'cash-crop demand, entrenched chattel '
                                                          'slavery in English colonies, reshaped '
                                                          'West Africa, and brutalized captives, '
                                                          'as the enslaved resisted and preserved '
                                                          'culture.'},
                                                 {'id': 'd',
                                                  'text': 'D) The Royal African Company '
                                                          'monopolized English slave transport '
                                                          'over four decades, contributing to '
                                                          'large enslaved populations in places '
                                                          'like Barbados by 1700.'}],
                                     'correct_choice_id': 'c'}]}},
 'p11': {'id': 'lifespan_development_1_2',
         'questions': {'baseline': [{'question_id': 'baseline_lifespan_development_1_2_51',
                                     'prompt': 'What is resilience, according to the American '
                                               'Psychological Association?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The ability to avoid adversity'},
                                                 {'id': 'b',
                                                  'text': 'B) The process of adapting poorly in '
                                                          'the face of stress'},
                                                 {'id': 'c',
                                                  'text': 'C) The process of adapting well in the '
                                                          'face of adversity'},
                                                 {'id': 'd',
                                                  'text': 'D) The ability to learn a language at '
                                                          'any age'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_2_52',
                                     'prompt': 'In the 1970s case of Genie, which hemisphere of '
                                               'the brain was involved in her language processing?',
                                     'choices': [{'id': 'a', 'text': 'A) Left hemisphere'},
                                                 {'id': 'b', 'text': 'B) Right hemisphere'},
                                                 {'id': 'c', 'text': 'C) Both hemispheres equally'},
                                                 {'id': 'd', 'text': 'D) Neither hemisphere'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_2_53',
                                     'prompt': 'What can be inferred about the role of a critical '
                                               'period in language development?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Language development can occur at '
                                                          'any time without constraints.'},
                                                 {'id': 'b',
                                                  'text': 'B) A critical period is unnecessary for '
                                                          'typical language development.'},
                                                 {'id': 'c',
                                                  'text': 'C) Missing the critical period may lead '
                                                          'to atypical language processing.'},
                                                 {'id': 'd',
                                                  'text': 'D) Critical periods only exist for '
                                                          'physical abilities, not psychological '
                                                          'ones.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX3',
                                     'prompt': 'Select Option B below',
                                     'choices': [{'id': 'a', 'text': 'A) Red'},
                                                 {'id': 'b', 'text': 'B) Green'},
                                                 {'id': 'c', 'text': 'C) Blue'},
                                                 {'id': 'd', 'text': 'D) Yellow'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_2_54',
                                     'prompt': 'Based on the text, which factor is most likely to '
                                               'hinder the development of a particular ability?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Introduction of enriching '
                                                          'environments'},
                                                 {'id': 'b',
                                                  'text': 'B) Exposure to normative developmental '
                                                          'outcomes'},
                                                 {'id': 'c',
                                                  'text': 'C) Extreme deprivation during specific '
                                                          'developmental times'},
                                                 {'id': 'd',
                                                  'text': 'D) Typical environmental conditions'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_2_55',
                                     'prompt': 'What is the main idea of the source text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Developmental psychologists focus '
                                                          'solely on physical development.'},
                                                 {'id': 'b',
                                                  'text': 'B) Resilience is rare and difficult to '
                                                          'achieve in human development.'},
                                                 {'id': 'c',
                                                  'text': 'C) Developmental outcomes are '
                                                          'influenced by environmental conditions '
                                                          'and critical periods.'},
                                                 {'id': 'd',
                                                  'text': 'D) Language development is the only '
                                                          'skill affected by early experiences.'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_lifespan_development_1_2_51',
                                     'prompt': 'Q1: What level and timing of deprivation are '
                                               'typically required to severely limit developmental '
                                               'potential?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Brief periods of deprivation limited '
                                                          'to later adolescence.'},
                                                 {'id': 'b',
                                                  'text': 'B) Mild shortages of stimulation across '
                                                          'childhood and adolescence.'},
                                                 {'id': 'c',
                                                  'text': 'C) Moderate adversity occurring at '
                                                          'different developmental ages.'},
                                                 {'id': 'd',
                                                  'text': 'D) Severe lack of key experiences '
                                                          'during critical periods.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_lifespan_development_1_2_52',
                                     'prompt': 'Q2: What is a critical period in development?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) A developmental interval in which '
                                                          'added enrichment can accelerate '
                                                          'growth.'},
                                                 {'id': 'b',
                                                  'text': 'B) A developmental phase when growth '
                                                          'proceeds regardless of experience.'},
                                                 {'id': 'c',
                                                  'text': 'C) A developmental span when specific '
                                                          'experiences are required for '
                                                          'development.'},
                                                 {'id': 'd',
                                                  'text': 'D) A developmental stage marked by full '
                                                          'neural maturity and stability.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_lifespan_development_1_2_53',
                                     'prompt': "Q3: Considering critical periods and Genie's "
                                               'language profile, what is the most reasonable '
                                               'conclusion about beginning language intervention '
                                               'after early childhood?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It often produces near-typical '
                                                          'mastery because humans adapt well to '
                                                          'adversity.'},
                                                 {'id': 'b',
                                                  'text': 'B) Outcomes depend largely on '
                                                          'enrichment level, so the start time has '
                                                          'little bearing on eventual skill.'},
                                                 {'id': 'c',
                                                  'text': 'C) The brain may recruit noncanonical '
                                                          'areas, limiting how closely later '
                                                          'learners can approximate standard '
                                                          'patterns.'},
                                                 {'id': 'd',
                                                  'text': 'D) With extensive practice, functions '
                                                          'tend to shift back to the left '
                                                          'hemisphere and ordinary patterns '
                                                          'emerge.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX5',
                                     'prompt': 'Choose Option B to show that you are reading '
                                               'carefully',
                                     'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                 {'id': 'b', 'text': 'B) London'},
                                                 {'id': 'c', 'text': 'C) Tokyo'},
                                                 {'id': 'd', 'text': 'D) Rome'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_lifespan_development_1_2_54',
                                     'prompt': 'Q4: Two children grow up in suboptimal conditions. '
                                               'Child 1 has modest resources but daily '
                                               'conversation with caregivers. Child 2 receives '
                                               'attentive care but little spoken input until age '
                                               '13. Which outcome best reflects how human '
                                               'development balances adaptability with '
                                               'timing-sensitive requirements?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Child 1 may develop on track, while '
                                                          'Child 2 has lasting language deficits '
                                                          'from missing early input.'},
                                                 {'id': 'b',
                                                  'text': 'B) Both are likely to attain typical '
                                                          'language with support, since growth is '
                                                          'broadly adaptable.'},
                                                 {'id': 'c',
                                                  'text': 'C) Child 2 should recover fully with '
                                                          'therapy, whereas Child 1 risks delays '
                                                          'from limited enrichment.'},
                                                 {'id': 'd',
                                                  'text': 'D) Both are likely to show similarly '
                                                          'broad impairments, given the impact of '
                                                          'early hardship.'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_lifespan_development_1_2_55',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Early experiences strongly determine '
                                                          'development; deprivation in childhood '
                                                          'typically produces severe, broad '
                                                          'deficits across domains.'},
                                                 {'id': 'b',
                                                  'text': 'B) Humans are resilient, but certain '
                                                          'abilities depend on input during '
                                                          'critical periods; extreme early '
                                                          'deprivation can produce atypical '
                                                          'outcomes, as seen in Genie.'},
                                                 {'id': 'c',
                                                  'text': 'C) Most children develop typically '
                                                          'regardless of timing or environment, '
                                                          'showing that critical periods have '
                                                          'little effect on outcomes.'},
                                                 {'id': 'd',
                                                  'text': 'D) The Genie case shows language '
                                                          'shifting to the right hemisphere after '
                                                          'deprivation, suggesting that language '
                                                          'is uniquely governed by critical '
                                                          'periods.'}],
                                     'correct_choice_id': 'b'}]}},
 'p12': {'id': 'lifespan_development_1_3',
         'questions': {'baseline': [{'question_id': 'baseline_lifespan_development_1_3_56',
                                     'prompt': 'Which of the following is an example of a social '
                                               'tool that Vygotsky considers important for '
                                               'cognitive development?',
                                     'choices': [{'id': 'a', 'text': 'A) Natural instincts'},
                                                 {'id': 'b', 'text': 'B) Language'},
                                                 {'id': 'c', 'text': 'C) Genetic predispositions'},
                                                 {'id': 'd', 'text': 'D) Diet'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_3_57',
                                     'prompt': 'What concept introduced by Vygotsky refers to '
                                               'tasks that a learner can achieve with guidance but '
                                               'not yet independently?',
                                     'choices': [{'id': 'a', 'text': 'A) Cognitive dissonance'},
                                                 {'id': 'b',
                                                  'text': 'B) Zone of proximal development'},
                                                 {'id': 'c', 'text': 'C) Theory of mind'},
                                                 {'id': 'd', 'text': 'D) Cognitive scaffolding'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_3_58',
                                     'prompt': "Based on Vygotsky's theory, what can be inferred "
                                               'about the role of technology in learning?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It hinders the learning process by '
                                                          'making tasks too easy.'},
                                                 {'id': 'b',
                                                  'text': 'B) It replaces traditional learning '
                                                          'methods entirely.'},
                                                 {'id': 'c',
                                                  'text': 'C) It acts as a tool to enhance '
                                                          'cognitive capabilities.'},
                                                 {'id': 'd',
                                                  'text': 'D) It is irrelevant to cognitive '
                                                          'development.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_3_59',
                                     'prompt': "What might be a reason Vygotsky's theory "
                                               'emphasizes language as a critical tool for '
                                               'cognitive development?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Language is innate and does not '
                                                          'change.'},
                                                 {'id': 'b',
                                                  'text': 'B) Language allows for complex '
                                                          'problem-solving without social '
                                                          'interaction.'},
                                                 {'id': 'c',
                                                  'text': 'C) Language is a universal form of '
                                                          'communication that can be used without '
                                                          'cultural context.'},
                                                 {'id': 'd',
                                                  'text': 'D) Language helps organize thoughts and '
                                                          'facilitates communication of ideas.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_lifespan_development_1_3_60',
                                     'prompt': "What is the central theme of Vygotsky's "
                                               'sociocultural theory of cognitive development as '
                                               'discussed in the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Cognitive development is solely '
                                                          'reliant on inborn abilities.'},
                                                 {'id': 'b',
                                                  'text': 'B) Learning is best achieved through '
                                                          'individual effort without external '
                                                          'aid.'},
                                                 {'id': 'c',
                                                  'text': 'C) Social and cultural interactions '
                                                          'play a crucial role in cognitive '
                                                          'development.'},
                                                 {'id': 'd',
                                                  'text': 'D) Technological advancements are the '
                                                          'primary drivers of cognitive growth.'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_lifespan_development_1_3_56',
                                     'prompt': 'Q1: What chiefly shapes cognitive development in '
                                               "Vygotsky's sociocultural theory?",
                                     'choices': [{'id': 'a',
                                                  'text': 'A) A predetermined sequence of stages '
                                                          'shared by most learners.'},
                                                 {'id': 'b',
                                                  'text': 'B) Personal discovery through '
                                                          'individual exploration and '
                                                          'trial-and-error.'},
                                                 {'id': 'c',
                                                  'text': 'C) Predominantly biological maturation '
                                                          'of the individual over time.'},
                                                 {'id': 'd',
                                                  'text': 'D) Social and cultural context, with '
                                                          'language and guidance.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_lifespan_development_1_3_57',
                                     'prompt': 'Q2: What do the zone of proximal development and '
                                               'scaffolding suggest about how individuals can '
                                               'extend performance?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Achievement depends more on stages '
                                                          'of maturation than on context.'},
                                                 {'id': 'b',
                                                  'text': 'B) Language and tools let people solve '
                                                          'complex tasks with little guidance.'},
                                                 {'id': 'c',
                                                  'text': 'C) People can do harder tasks with '
                                                          'temporary guidance that fades.'},
                                                 {'id': 'd',
                                                  'text': 'D) Progress requires more and more '
                                                          'external help as skills improve.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_lifespan_development_1_3_58',
                                     'prompt': 'Q3: How would deliberate use of private speech, '
                                               'acronyms, and tools like calculators or '
                                               "autocorrect most likely affect students' work on "
                                               'complex assignments?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) allow learners to focus on '
                                                          'conceptual reasoning by offloading '
                                                          'routine processes'},
                                                 {'id': 'b',
                                                  'text': 'B) encourage dependence on aids and '
                                                          'limit independent thinking during '
                                                          'challenging tasks'},
                                                 {'id': 'c',
                                                  'text': 'C) function mainly as memorization aids '
                                                          'rather than supporting complex '
                                                          'reasoning in practice'},
                                                 {'id': 'd',
                                                  'text': 'D) lessen the need for scaffolding '
                                                          'because tools substitute for guided '
                                                          'support'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_lifespan_development_1_3_59',
                                     'prompt': 'Q4: To help learners operate beyond their present '
                                               'skill while avoiding dependence or discouragement, '
                                               'which instructional choice would be most '
                                               'effective?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Maintain detailed, step-by-step '
                                                          'guidance across tasks to minimize '
                                                          'errors and uncertainty.'},
                                                 {'id': 'b',
                                                  'text': 'B) Present complex tasks first, adding '
                                                          'supports later in response to repeated '
                                                          'failures.'},
                                                 {'id': 'c',
                                                  'text': 'C) Provide timely prompts for '
                                                          'near-ready skills, then fade them as '
                                                          'skills grow.'},
                                                 {'id': 'd',
                                                  'text': 'D) Withhold assistance to foster '
                                                          'independence from the outset, even on '
                                                          'challenging tasks.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX4',
                                     'prompt': 'Which of the following is the ONLY option that is '
                                               'a number?',
                                     'choices': [{'id': 'a', 'text': 'A) Seven'},
                                                 {'id': 'b', 'text': 'B) Chair'},
                                                 {'id': 'c', 'text': 'C) Machine'},
                                                 {'id': 'd', 'text': 'D) Sidewalk'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_lifespan_development_1_3_60',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Cognitive development is socially '
                                                          'mediated by language, technology, and '
                                                          'scaffolded guidance within the ZPD.'},
                                                 {'id': 'b',
                                                  'text': 'B) Instruction works best when '
                                                          'temporary supports, like training '
                                                          'wheels, are provided until independence '
                                                          'is reached.'},
                                                 {'id': 'c',
                                                  'text': 'C) Language primarily drives thought, '
                                                          'with private speech and mnemonics '
                                                          'fostering cognitive growth.'},
                                                 {'id': 'd',
                                                  'text': 'D) Technological tools lessen mental '
                                                          'load by automating mechanics so '
                                                          'learners can focus on higher-level '
                                                          'thinking.'}],
                                     'correct_choice_id': 'a'}]}},
 'p13': {'id': 'lifespan_development_1_4',
         'questions': {'baseline': [{'question_id': 'baseline_lifespan_development_1_4_61',
                                     'prompt': "What does the term 'cis-' denote in terms of "
                                               'gender identity?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It denotes gender non-conformity'},
                                                 {'id': 'b',
                                                  'text': 'B) It denotes a mismatch between gender '
                                                          'identity and sex assignment'},
                                                 {'id': 'c',
                                                  'text': 'C) It denotes conformity between gender '
                                                          'identity and sex assignment'},
                                                 {'id': 'd',
                                                  'text': 'D) It denotes a non-binary gender '
                                                          'identity'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_4_62',
                                     'prompt': 'Which organization provided insights regarding '
                                               'sex, gender, and sexual orientation as key '
                                               'components of human development?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) American Psychological Association'},
                                                 {'id': 'b',
                                                  'text': 'B) National Academies of Sciences, '
                                                          'Engineering, & Medicine'},
                                                 {'id': 'c',
                                                  'text': 'C) World Health Organization'},
                                                 {'id': 'd',
                                                  'text': 'D) Centers for Disease Control and '
                                                          'Prevention'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_4_63',
                                     'prompt': 'Based on the text, why might the practice of using '
                                               'sex and gender terms interchangeably be '
                                               'problematic?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It reflects the lack of scientific '
                                                          'research on the topic'},
                                                 {'id': 'b',
                                                  'text': 'B) It can lead to confusion and '
                                                          'misinterpretation of study results'},
                                                 {'id': 'c',
                                                  'text': 'C) It simplifies the complexity of '
                                                          'human behavior and identity'},
                                                 {'id': 'd',
                                                  'text': 'D) It supports outdated cultural '
                                                          'norms'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_lifespan_development_1_4_64',
                                     'prompt': 'What conclusion can be drawn about the '
                                               'relationship between cultural trends and gender '
                                               'associations?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Cultural trends have little impact '
                                                          'on gender associations'},
                                                 {'id': 'b',
                                                  'text': 'B) Gender associations are biologically '
                                                          'determined and unchangeable'},
                                                 {'id': 'c',
                                                  'text': 'C) Cultural trends can influence and '
                                                          'change traditional gender associations '
                                                          'over time'},
                                                 {'id': 'd',
                                                  'text': 'D) Gender associations are consistent '
                                                          'across different cultures'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_4_65',
                                     'prompt': 'What is the primary purpose of the source text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) To discuss the historical changes in '
                                                          'gender roles'},
                                                 {'id': 'b',
                                                  'text': 'B) To explore the challenges of '
                                                          'researching human development'},
                                                 {'id': 'c',
                                                  'text': 'C) To explain the distinctions and '
                                                          'relationships between sex, gender, and '
                                                          'sexual orientation in human '
                                                          'development'},
                                                 {'id': 'd',
                                                  'text': 'D) To criticize the use of gender '
                                                          'labels in scientific studies'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_lifespan_development_1_4_61',
                                     'prompt': 'Q1: Which statement correctly distinguishes sex '
                                               'from gender?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Sex is assigned at birth based on '
                                                          'biological traits (such as '
                                                          'chromosomes), while gender reflects '
                                                          'societal roles and behaviors.'},
                                                 {'id': 'b',
                                                  'text': 'B) Sex is based on patterns of sexual '
                                                          'attraction, while gender indicates '
                                                          'occupational and family roles in a '
                                                          'community.'},
                                                 {'id': 'c',
                                                  'text': 'C) Sex is determined by cultural '
                                                          'expectations and socialization, while '
                                                          'gender is set by chromosomes and '
                                                          'anatomy at birth.'},
                                                 {'id': 'd',
                                                  'text': 'D) Sex is identified by labels such as '
                                                          'woman, man, or nonbinary, while gender '
                                                          'refers to physical traits present at '
                                                          'birth.'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_lifespan_development_1_4_62',
                                     'prompt': 'Q2: What components make up sexual orientation?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Gender identity, sexual behavior, '
                                                          'and sexual attraction.'},
                                                 {'id': 'b',
                                                  'text': 'B) Romantic orientation, emotional '
                                                          'attraction, and sexual attraction.'},
                                                 {'id': 'c',
                                                  'text': 'C) Sex assigned at birth, gender roles, '
                                                          'and sexual attraction.'},
                                                 {'id': 'd',
                                                  'text': 'D) Sexual identity, sexual behavior, '
                                                          'and sexual attraction.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_lifespan_development_1_4_63',
                                     'prompt': 'Q3: What is a likely consequence when studies use '
                                               'sex and gender terms interchangeably in reporting '
                                               'developmental results?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Clarifies results by merging '
                                                          'categories for consistency across '
                                                          'studies.'},
                                                 {'id': 'b',
                                                  'text': 'B) Enhances cultural validity as social '
                                                          'norms evolve over time.'},
                                                 {'id': 'c',
                                                  'text': 'C) Invites misreading of outcomes by '
                                                          'blending distinct influences.'},
                                                 {'id': 'd',
                                                  'text': 'D) Reduces bias by avoiding labels that '
                                                          'participants may contest.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_lifespan_development_1_4_64',
                                     'prompt': 'Q4: What does the historical reversal of pink and '
                                               'blue associations imply about the nature of '
                                               'gender-linked characteristics?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) They are determined by chromosomal '
                                                          'patterns that remain stable across '
                                                          'generations.'},
                                                 {'id': 'b',
                                                  'text': 'B) They are fixed outcomes of prenatal '
                                                          'hormone exposure independent of '
                                                          'society.'},
                                                 {'id': 'c',
                                                  'text': 'C) They arise from social norms that '
                                                          'can change rather than innate biology.'},
                                                 {'id': 'd',
                                                  'text': 'D) They mirror common parental '
                                                          'practices, which assign stable meanings '
                                                          'to traits across time.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_lifespan_development_1_4_65',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Clarifies how sex, gender, gender '
                                                          'identity, and sexual orientation '
                                                          'differ, noting conflation and changing '
                                                          'norms complicate research.'},
                                                 {'id': 'b',
                                                  'text': 'B) Emphasizes that sexual orientation '
                                                          'comprises identity, behavior, and '
                                                          'attraction, which may not align, '
                                                          'including emotional versus sexual '
                                                          'attraction.'},
                                                 {'id': 'c',
                                                  'text': 'C) Focuses on cultural shifts in gender '
                                                          'norms, arguing that gender-linked '
                                                          'meanings change over time across '
                                                          'historical periods.'},
                                                 {'id': 'd',
                                                  'text': 'D) Highlights that psychology often '
                                                          'analyzes social and cultural subgroups '
                                                          'such as sex, race/ethnicity, religion, '
                                                          'and socioeconomic status.'}],
                                     'correct_choice_id': 'a'}]}},
 'p14': {'id': 'lifespan_development_1_5',
         'questions': {'baseline': [{'question_id': 'baseline_lifespan_development_1_5_66',
                                     'prompt': 'What is a common challenge faced by longitudinal '
                                               'studies due to participants dropping out?',
                                     'choices': [{'id': 'a', 'text': 'A) Cohort effects'},
                                                 {'id': 'b', 'text': 'B) Practice effects'},
                                                 {'id': 'c', 'text': 'C) Attrition'},
                                                 {'id': 'd', 'text': 'D) Generalization issues'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_5_67',
                                     'prompt': 'What type of research design involves studying the '
                                               'same group of participants over time?',
                                     'choices': [{'id': 'a', 'text': 'A) Cross-sectional design'},
                                                 {'id': 'b', 'text': 'B) Experimental design'},
                                                 {'id': 'c', 'text': 'C) Longitudinal design'},
                                                 {'id': 'd', 'text': 'D) Case study design'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_1_5_68',
                                     'prompt': 'Why might longitudinal studies be considered '
                                               'highly valuable despite their challenges?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) They are quick to conduct and '
                                                          'analyze.'},
                                                 {'id': 'b',
                                                  'text': 'B) They allow for observing changes '
                                                          'within individuals over time.'},
                                                 {'id': 'c',
                                                  'text': 'C) They require fewer participants than '
                                                          'other studies.'},
                                                 {'id': 'd',
                                                  'text': 'D) They exclusively focus on '
                                                          'health-related research.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_5_69',
                                     'prompt': 'Why might researchers be confident that findings '
                                               'from large longitudinal studies can be generalized '
                                               'to the larger population?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Because they include a diverse range '
                                                          'of topics.'},
                                                 {'id': 'b',
                                                  'text': 'B) Because they are typically funded by '
                                                          'reputable organizations.'},
                                                 {'id': 'c',
                                                  'text': 'C) Because the studies are conducted '
                                                          'over a short period.'},
                                                 {'id': 'd',
                                                  'text': 'D) Because they often involve tens of '
                                                          'thousands of participants.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX3',
                                     'prompt': 'Select Option B below',
                                     'choices': [{'id': 'a', 'text': 'A) Red'},
                                                 {'id': 'b', 'text': 'B) Green'},
                                                 {'id': 'c', 'text': 'C) Blue'},
                                                 {'id': 'd', 'text': 'D) Yellow'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_1_5_70',
                                     'prompt': 'What is the primary focus of the source text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The process of recruiting '
                                                          'participants for longitudinal studies.'},
                                                 {'id': 'b',
                                                  'text': 'B) The advantages of using longitudinal '
                                                          'studies in educational research.'},
                                                 {'id': 'c',
                                                  'text': 'C) The characteristics, uses, and '
                                                          'challenges of longitudinal research '
                                                          'design.'},
                                                 {'id': 'd',
                                                  'text': 'D) The role of the American Cancer '
                                                          'Society in promoting longitudinal '
                                                          'studies.'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_lifespan_development_1_5_66',
                                     'prompt': 'Q1: Which feature defines a longitudinal research '
                                               'design?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Comparing different age groups at a '
                                                          'single time point to infer trends.'},
                                                 {'id': 'b',
                                                  'text': 'B) Randomly assigning people to '
                                                          'conditions to test immediate '
                                                          'intervention effects.'},
                                                 {'id': 'c',
                                                  'text': 'C) Recruiting new samples at each '
                                                          'assessment to avoid attrition and '
                                                          'practice effects.'},
                                                 {'id': 'd',
                                                  'text': 'D) Repeatedly measuring the same '
                                                          'participants over time to track '
                                                          'change.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_lifespan_development_1_5_67',
                                     'prompt': 'Q2: Which issue is identified as the most serious '
                                               'challenge in longitudinal research, with its risk '
                                               'increasing as studies run longer?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Attrition of participants across '
                                                          'waves.'},
                                                 {'id': 'b',
                                                  'text': 'B) Cohort effects that limit '
                                                          'generalizability.'},
                                                 {'id': 'c',
                                                  'text': 'C) Delayed findings due to extended '
                                                          'timelines.'},
                                                 {'id': 'd',
                                                  'text': 'D) Practice effects from repeated '
                                                          'testing.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_lifespan_development_1_5_68',
                                     'prompt': 'Q3: Which aspect of a longitudinal design best '
                                               'explains its advantage in revealing developmental '
                                               'paths and pinpointing risk factors compared with '
                                               'designs that assess different people at one time?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It minimizes cohort effects by '
                                                          'focusing on a single cohort over time '
                                                          'and holding the broader context '
                                                          'constant.'},
                                                 {'id': 'b',
                                                  'text': 'B) It reassesses the same individuals, '
                                                          'showing within-person change and the '
                                                          'temporal ordering of predictors and '
                                                          'outcomes.'},
                                                 {'id': 'c',
                                                  'text': 'C) It recruits very large samples, '
                                                          'boosting statistical power and broad '
                                                          'generalizability across populations.'},
                                                 {'id': 'd',
                                                  'text': 'D) It uses the same instruments at each '
                                                          'wave to keep responses strictly '
                                                          'comparable across time.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'QX5',
                                     'prompt': 'Choose Option B to show that you are reading '
                                               'carefully',
                                     'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                 {'id': 'b', 'text': 'B) London'},
                                                 {'id': 'c', 'text': 'C) Tokyo'},
                                                 {'id': 'd', 'text': 'D) Rome'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_lifespan_development_1_5_69',
                                     'prompt': 'Q4: If many participants leave a long-term study '
                                               'and those who remain become accustomed to repeated '
                                               'measures, what is the most likely impact on the '
                                               "study's ability to draw conclusions about change "
                                               'over time?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It would bias results through '
                                                          'attrition and practice effects, '
                                                          'weakening validity and '
                                                          'generalizability.'},
                                                 {'id': 'b',
                                                  'text': 'B) It would improve precision because '
                                                          'repeated exposure makes answers more '
                                                          'consistent.'},
                                                 {'id': 'c',
                                                  'text': 'C) It would make results more '
                                                          'generalizable since the sample is '
                                                          'followed closely for years.'},
                                                 {'id': 'd',
                                                  'text': 'D) It would lessen cohort concerns '
                                                          'because the same individuals are '
                                                          'tracked.'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_lifespan_development_1_5_70',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Given practice effects and '
                                                          'attrition, longitudinal designs offer '
                                                          'limited value relative to quicker '
                                                          'cross-sectional studies and therefore '
                                                          'are rarely appropriate for studying '
                                                          'development or health.'},
                                                 {'id': 'b',
                                                  'text': 'B) Longitudinal research tracks the '
                                                          'same people over time to study change '
                                                          'and risk; despite time, attrition, and '
                                                          'cohort issues, it remains a highly '
                                                          'valid, valuable method.'},
                                                 {'id': 'c',
                                                  'text': 'C) Longitudinal studies are mainly '
                                                          'about assembling huge samples for broad '
                                                          'generalization, as in smoking research, '
                                                          'and present few concerns beyond '
                                                          'managing long timelines.'},
                                                 {'id': 'd',
                                                  'text': 'D) The central purpose of longitudinal '
                                                          'research is to identify cohort effects '
                                                          'that emerge over time, which largely '
                                                          'overshadow any benefits of tracking the '
                                                          'same individuals.'}],
                                     'correct_choice_id': 'b'}]}},
 'p15': {'id': 'lifespan_development_9_3',
         'questions': {'baseline': [{'question_id': 'baseline_lifespan_development_9_3_71',
                                     'prompt': 'What new ability characterizes adolescent thought '
                                               'according to the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The ability to think in simple '
                                                          'terms'},
                                                 {'id': 'b',
                                                  'text': 'B) The ability to think about concrete '
                                                          'operations'},
                                                 {'id': 'c',
                                                  'text': 'C) The ability to think about what is '
                                                          'possible'},
                                                 {'id': 'd',
                                                  'text': 'D) The ability to memorize facts'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_9_3_72',
                                     'prompt': 'According to the text, what is a hallmark of '
                                               'adolescent thinking when faced with situations '
                                               'like a dress code violation?',
                                     'choices': [{'id': 'a', 'text': 'A) Acceptance of authority'},
                                                 {'id': 'b', 'text': 'B) Unquestioning obedience'},
                                                 {'id': 'c',
                                                  'text': 'C) Seeing irony in the situation'},
                                                 {'id': 'd', 'text': 'D) Ignoring the situation'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX5',
                                     'prompt': 'Choose Option B to show that you are reading '
                                               'carefully',
                                     'choices': [{'id': 'a', 'text': 'A) Paris'},
                                                 {'id': 'b', 'text': 'B) London'},
                                                 {'id': 'c', 'text': 'C) Tokyo'},
                                                 {'id': 'd', 'text': 'D) Rome'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_lifespan_development_9_3_73',
                                     'prompt': 'Why might adolescents become frustrated with '
                                               'adults, based on the information in the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Because they are naturally '
                                                          'rebellious'},
                                                 {'id': 'b',
                                                  'text': 'B) Because adults often punish them '
                                                          'unfairly'},
                                                 {'id': 'c',
                                                  'text': 'C) Because they de-idealize adults due '
                                                          'to their ability to see multiple '
                                                          'perspectives and question rules'},
                                                 {'id': 'd',
                                                  'text': 'D) Because they want to be treated like '
                                                          'children'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_lifespan_development_9_3_74',
                                     'prompt': 'How might adolescents use their relativistic '
                                               'thinking in a classroom setting?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) By only listening to the teacher'},
                                                 {'id': 'b',
                                                  'text': 'B) By accepting all rules without '
                                                          'question'},
                                                 {'id': 'c',
                                                  'text': 'C) By focusing solely on memorizing '
                                                          'facts'},
                                                 {'id': 'd',
                                                  'text': 'D) By discussing with the instructor to '
                                                          'gain a better understanding of material '
                                                          'when multiple perspectives are '
                                                          'possible'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_lifespan_development_9_3_75',
                                     'prompt': 'What is the main idea of the source text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Adolescents lack the ability to '
                                                          'understand complex ideas'},
                                                 {'id': 'b',
                                                  'text': 'B) Adolescents should be taught to '
                                                          'think in absolutes'},
                                                 {'id': 'c',
                                                  'text': 'C) Adolescents develop new thinking '
                                                          'abilities that allow them to understand '
                                                          'abstract concepts, consider multiple '
                                                          'perspectives, and engage in '
                                                          'relativistic thinking'},
                                                 {'id': 'd',
                                                  'text': 'D) Adolescents are primarily focused on '
                                                          'the physical world'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_lifespan_development_9_3_71',
                                     'prompt': 'Q1: During adolescence, what becomes a focus of '
                                               'more sophisticated reasoning?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Absolute distinctions such as right '
                                                          'versus wrong'},
                                                 {'id': 'b',
                                                  'text': 'B) Concrete, observable behaviors like '
                                                          'sharing and taking turns'},
                                                 {'id': 'c',
                                                  'text': 'C) Nonphysical concepts such as justice '
                                                          'and equality'},
                                                 {'id': 'd',
                                                  'text': 'D) Single-factor explanations of events '
                                                          'and outcomes'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_lifespan_development_9_3_72',
                                     'prompt': 'Q2: What ability do adolescents gain that allows '
                                               'them to see that two opposing answers can both be '
                                               'valid depending on context?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Abstract reasoning about ideas'},
                                                 {'id': 'b',
                                                  'text': 'B) Appreciation of sarcasm in '
                                                          'discourse'},
                                                 {'id': 'c', 'text': 'C) Relativistic thinking'},
                                                 {'id': 'd',
                                                  'text': 'D) Thinking in multiple dimensions'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_lifespan_development_9_3_73',
                                     'prompt': "Q3: Given adolescents' growing capacity to think "
                                               'across multiple dimensions and detect irony, how '
                                               'are they likely to respond to school rules they '
                                               'view as arbitrary?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Accepting such directives as '
                                                          'reasonable compromises once they '
                                                          'consider multiple viewpoints'},
                                                 {'id': 'b',
                                                  'text': 'B) Aiming for clear right-or-wrong '
                                                          'judgments that make directives easier '
                                                          'to follow'},
                                                 {'id': 'c',
                                                  'text': 'C) Challenging or negotiating such '
                                                          'directives with the adults in charge'},
                                                 {'id': 'd',
                                                  'text': 'D) Using sarcasm to lighten the '
                                                          'situation and strengthen rapport with '
                                                          'rule-makers'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_lifespan_development_9_3_74',
                                     'prompt': 'Q4: How does the development of relativistic '
                                               "thinking most likely affect adolescents' judgments "
                                               'about issues like school rules or exam responses?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) They hesitate to choose, as context '
                                                          'can make both seem right.'},
                                                 {'id': 'b',
                                                  'text': 'B) They rely on adults to determine the '
                                                          'correct stance to reduce ambiguity.'},
                                                 {'id': 'c',
                                                  'text': 'C) They resolve questions faster '
                                                          'because higher-level reasoning points '
                                                          'to one best option.'},
                                                 {'id': 'd',
                                                  'text': 'D) They treat correctness as '
                                                          'independent of context, making '
                                                          'evaluation straightforward.'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_lifespan_development_9_3_75',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Adolescents develop abstract, '
                                                          'perspective-taking, relativistic '
                                                          'thinking, which yields nuanced '
                                                          'judgments and increased questioning of '
                                                          'authority.'},
                                                 {'id': 'b',
                                                  'text': 'B) Appreciating irony and sarcasm helps '
                                                          'adolescents communicate more '
                                                          'effectively and navigate social '
                                                          'situations.'},
                                                 {'id': 'c',
                                                  'text': 'C) Considering multiple viewpoints '
                                                          'leads adolescents to see truth as '
                                                          'subjective and to resolve disagreements '
                                                          'through discussion.'},
                                                 {'id': 'd',
                                                  'text': 'D) Greater skepticism toward rules in '
                                                          'adolescence often produces frustration '
                                                          'and conflict with authority figures.'}],
                                     'correct_choice_id': 'a'}]}},
 'p16': {'id': 'sociology_1_1',
         'questions': {'baseline': [{'question_id': 'baseline_sociology_1_1_76',
                                     'prompt': 'According to the U.S. Census Bureau 2020 data, how '
                                               'many fathers are raising their children alone?',
                                     'choices': [{'id': 'a', 'text': 'A) 1.5 million'},
                                                 {'id': 'b', 'text': 'B) 2.5 million'},
                                                 {'id': 'c', 'text': 'C) 3.5 million'},
                                                 {'id': 'd', 'text': 'D) 4.5 million'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_sociology_1_1_77',
                                     'prompt': 'What term did German sociologist Norbert Elias use '
                                               'to describe the process of analyzing individual '
                                               'behavior and the society that shapes it?',
                                     'choices': [{'id': 'a', 'text': 'A) Socialization'},
                                                 {'id': 'b', 'text': 'B) Figuration'},
                                                 {'id': 'c', 'text': 'C) Interactionism'},
                                                 {'id': 'd', 'text': 'D) Symbolism'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_1_1_78',
                                     'prompt': 'Why might sociologists be interested in the '
                                               'increasing number of expanded households?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) To understand the economic benefits '
                                                          'of larger households'},
                                                 {'id': 'b',
                                                  'text': 'B) To see how traditional family '
                                                          'structures are maintained'},
                                                 {'id': 'c',
                                                  'text': 'C) To study changes in social support '
                                                          'systems and family dynamics'},
                                                 {'id': 'd',
                                                  'text': 'D) To investigate the impact on '
                                                          'neighborhood development'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX2',
                                     'prompt': 'Select color from the following:',
                                     'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                 {'id': 'b', 'text': 'B) Rabbit'},
                                                 {'id': 'c', 'text': 'C) Yellow'},
                                                 {'id': 'd', 'text': 'D) Cat'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_sociology_1_1_79',
                                     'prompt': 'How could the concept of figuration apply to the '
                                               'study of religion in society?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) By reducing religion to individual '
                                                          'beliefs'},
                                                 {'id': 'b',
                                                  'text': 'B) By analyzing religious texts without '
                                                          'context'},
                                                 {'id': 'c',
                                                  'text': 'C) By ignoring the role of government '
                                                          'in religious practices'},
                                                 {'id': 'd',
                                                  'text': 'D) By considering both individual '
                                                          'religious practices and the social '
                                                          'context of religion'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_sociology_1_1_80',
                                     'prompt': 'What is the primary focus of the sociological '
                                               'perspective as described in the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The study of individual psychology'},
                                                 {'id': 'b',
                                                  'text': 'B) The analysis of economic systems'},
                                                 {'id': 'c',
                                                  'text': 'C) The examination of the relationship '
                                                          'between individuals and society'},
                                                 {'id': 'd',
                                                  'text': 'D) The exploration of historical '
                                                          'events'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_sociology_1_1_76',
                                     'prompt': 'Q1: Which sociologist labeled the process of '
                                               'analyzing individuals together with the society '
                                               'shaping them as "figuration"?',
                                     'choices': [{'id': 'a', 'text': 'A) Émile Durkheim'},
                                                 {'id': 'b', 'text': 'B) Norbert Elias'},
                                                 {'id': 'c', 'text': 'C) Karl Marx'},
                                                 {'id': 'd', 'text': 'D) Max Weber'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_1_1_77',
                                     'prompt': 'Q2: About how many single mothers and single '
                                               'fathers were raising children in the United States '
                                               'in 2020?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) 3.5 million mothers and 15 million '
                                                          'fathers'},
                                                 {'id': 'b',
                                                  'text': 'B) 10 million mothers and 7 million '
                                                          'fathers'},
                                                 {'id': 'c',
                                                  'text': 'C) 15 million mothers and 3.5 million '
                                                          'fathers'},
                                                 {'id': 'd',
                                                  'text': 'D) 20 million mothers and 1 million '
                                                          'fathers'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_sociology_1_1_78',
                                     'prompt': 'Q3: Which underlying influences best account for '
                                               'the growing variety of household types in the '
                                               'United States?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Changing views of marriage and '
                                                          'labor-market conditions'},
                                                 {'id': 'b',
                                                  'text': 'B) Expanding needs for education, '
                                                          'housing, and healthcare services'},
                                                 {'id': 'c',
                                                  'text': 'C) Increases in fertility rates and '
                                                          'extended life expectancy'},
                                                 {'id': 'd',
                                                  'text': 'D) Personal preferences that operate '
                                                          'largely without societal pressure'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_sociology_1_1_79',
                                     'prompt': 'Q4: Under a figurational view, what is the most '
                                               'likely outcome when a government revises policies '
                                               'that govern worship practices?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Both personal observance and '
                                                          'institutional routines change little, '
                                                          'as traditions tend to buffer outside '
                                                          'pressures.'},
                                                 {'id': 'b',
                                                  'text': 'B) Personal observance changes with new '
                                                          'rules, while organizational practices '
                                                          'largely persist without alteration.'},
                                                 {'id': 'c',
                                                  'text': 'C) Organizational practices adjust for '
                                                          "compliance, while congregants' habits "
                                                          'remain much as before.'},
                                                 {'id': 'd',
                                                  'text': 'D) Personal observance changes with new '
                                                          'rules, and over time organizations '
                                                          'adjust routines.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_sociology_1_1_80',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Sociology centers on contemporary '
                                                          'policy issues such as policing, '
                                                          'political realignments, and social '
                                                          "media's impact on communication and "
                                                          'community life.'},
                                                 {'id': 'b',
                                                  'text': 'B) Sociology examines how religious '
                                                          'institutions influence personal '
                                                          'practice and ritual within broader '
                                                          'cultural contexts and everyday life.'},
                                                 {'id': 'c',
                                                  'text': 'C) Sociology explores the '
                                                          'interdependence of individuals and '
                                                          'society by analyzing social facts and '
                                                          'patterns shaping behavior and '
                                                          'institutions.'},
                                                 {'id': 'd',
                                                  'text': 'D) Sociology mainly documents changes '
                                                          'in U.S. family forms and their effects '
                                                          'on children and social services.'}],
                                     'correct_choice_id': 'c'}]}},
 'p17': {'id': 'sociology_11_2',
         'questions': {'baseline': [{'question_id': 'baseline_sociology_11_2_81',
                                     'prompt': 'According to the functionalist perspective, what '
                                               'is one positive function of racism in society?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It promotes economic equality.'},
                                                 {'id': 'b',
                                                  'text': 'B) It strengthens bonds within in-group '
                                                          'members by excluding out-group '
                                                          'members.'},
                                                 {'id': 'c',
                                                  'text': 'C) It eliminates racial boundaries.'},
                                                 {'id': 'd',
                                                  'text': 'D) It prevents social changes.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_11_2_82',
                                     'prompt': 'What did Herbert Blumer suggest about racial '
                                               'prejudice?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It is inherent in human nature.'},
                                                 {'id': 'b',
                                                  'text': 'B) It is formed through interactions '
                                                          'between members of the subordinate '
                                                          'group.'},
                                                 {'id': 'c',
                                                  'text': 'C) It is formed through interactions '
                                                          'between members of the dominant group.'},
                                                 {'id': 'd',
                                                  'text': 'D) It has no relation to social '
                                                          'interactions.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_sociology_11_2_83',
                                     'prompt': 'What might be a reason why the functionalist '
                                               'perspective suggests racial inequalities have '
                                               'existed for a long time?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) They have been ignored by society.'},
                                                 {'id': 'b',
                                                  'text': 'B) They serve an important function for '
                                                          'the dominant group.'},
                                                 {'id': 'c',
                                                  'text': 'C) They are legally mandated.'},
                                                 {'id': 'd',
                                                  'text': 'D) They are a result of technological '
                                                          'advancements.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_sociology_11_2_84',
                                     'prompt': 'How might symbolic interactionism explain the '
                                               'formation of racial identities?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Through biological characteristics '
                                                          'fixed at birth.'},
                                                 {'id': 'b',
                                                  'text': 'B) Through direct mandates from legal '
                                                          'systems.'},
                                                 {'id': 'c',
                                                  'text': 'C) Through social interactions and '
                                                          'symbols.'},
                                                 {'id': 'd',
                                                  'text': 'D) Through geographical locations.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_sociology_11_2_85',
                                     'prompt': 'What is the primary focus of the source text '
                                               'regarding race and ethnicity?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) To argue for the elimination of '
                                                          'racial categories.'},
                                                 {'id': 'b',
                                                  'text': 'B) To discuss how race and ethnicity '
                                                          'impact economic systems.'},
                                                 {'id': 'c',
                                                  'text': 'C) To explore how different '
                                                          'sociological perspectives explain race '
                                                          'and ethnicity.'},
                                                 {'id': 'd',
                                                  'text': 'D) To provide a historical overview of '
                                                          'racial relations.'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_sociology_11_2_81',
                                     'prompt': 'Q1: When racial or ethnic inequalities disrupt '
                                               'social stability, what action does functionalism '
                                               'expect from institutions?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Divert public resources to uphold '
                                                          'racial boundaries.'},
                                                 {'id': 'b',
                                                  'text': 'B) Enforce social exclusion to bolster '
                                                          'in-group solidarity.'},
                                                 {'id': 'c',
                                                  'text': 'C) Implement reforms, including in '
                                                          'policing, to regain balance.'},
                                                 {'id': 'd',
                                                  'text': 'D) Rely on interactions to maintain the '
                                                          'status quo.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_sociology_11_2_82',
                                     'prompt': "Q2: According to Herbert Blumer's symbolic "
                                               'interactionism, what causes racial prejudice?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Direct encounters with minority '
                                                          'members that replace abstract images '
                                                          'with personal knowledge and reduce '
                                                          'bias.'},
                                                 {'id': 'b',
                                                  'text': 'B) Functional needs of the social '
                                                          'system that boost cohesion by excluding '
                                                          'outsiders and enforcing boundaries.'},
                                                 {'id': 'c',
                                                  'text': 'C) In-group contacts among dominants '
                                                          'that form generalized images of '
                                                          'out-groups and preserve the status '
                                                          'quo.'},
                                                 {'id': 'd',
                                                  'text': "D) Misclassification of one's own and "
                                                          "others' racial identities that occurs "
                                                          'through everyday labeling practices.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_sociology_11_2_83',
                                     'prompt': 'Q3: If prejudice stems from dominant-group '
                                               'interactions and abstract images of out-groups, '
                                               'which strategy would be most likely to diminish '
                                               'it?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Adopt colorblind messaging in '
                                                          'schools and reduce references to racial '
                                                          'categories.'},
                                                 {'id': 'b',
                                                  'text': "B) Emphasize inequality's integrative "
                                                          'functions and preserve existing group '
                                                          'boundaries.'},
                                                 {'id': 'c',
                                                  'text': 'C) Increase penalties for bias '
                                                          'incidents and expand monitoring to '
                                                          'deter offenses.'},
                                                 {'id': 'd',
                                                  'text': 'D) Promote sustained cooperative '
                                                          'contact across groups and diversify '
                                                          'accurate media portrayals.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX3',
                                     'prompt': 'Select Option B below',
                                     'choices': [{'id': 'a', 'text': 'A) Red'},
                                                 {'id': 'b', 'text': 'B) Green'},
                                                 {'id': 'c', 'text': 'C) Blue'},
                                                 {'id': 'd', 'text': 'D) Yellow'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_11_2_84',
                                     'prompt': 'Q4: From a functionalist perspective, why might '
                                               'initiatives to reduce racial inequality encounter '
                                               'pushback even if they promise broad social '
                                               'benefits?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Advantaged groups benefit from the '
                                                          'current hierarchy and are motivated to '
                                                          'keep it intact.'},
                                                 {'id': 'b',
                                                  'text': 'B) Identity concerns lead people to '
                                                          'resist reforms because they would alter '
                                                          'symbols they use for self-definition.'},
                                                 {'id': 'c',
                                                  'text': 'C) Policymakers resist since the '
                                                          'adjustments needed to reach a new '
                                                          'balance are overly disruptive.'},
                                                 {'id': 'd',
                                                  'text': 'D) Reducing boundaries would weaken '
                                                          'in-group cohesion without improving '
                                                          'overall efficiency.'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_sociology_11_2_85',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The text argues that racism '
                                                          'strengthens in-group bonds and is '
                                                          'managed by institutions to keep society '
                                                          'stable.'},
                                                 {'id': 'b',
                                                  'text': 'B) The text contrasts functionalist and '
                                                          'symbolic interactionist views of racial '
                                                          'inequality, emphasizing order, symbols, '
                                                          'and interaction-based prejudice.'},
                                                 {'id': 'c',
                                                  'text': 'C) The text claims that racial '
                                                          'categories are not biological and that '
                                                          'media images generate prejudice in '
                                                          'dominant groups.'},
                                                 {'id': 'd',
                                                  'text': 'D) The text concludes that racism '
                                                          'mainly benefits dominant groups by '
                                                          'justifying inequality and wasting '
                                                          'minority talent.'}],
                                     'correct_choice_id': 'b'}]}},
 'p18': {'id': 'sociology_3_1',
         'questions': {'baseline': [{'question_id': 'baseline_sociology_3_1_86',
                                     'prompt': 'What is an example of a cultural universal '
                                               'mentioned in the text?',
                                     'choices': [{'id': 'a', 'text': 'A) Eating with utensils'},
                                                 {'id': 'b', 'text': 'B) Use of language'},
                                                 {'id': 'c', 'text': 'C) Drinking coffee'},
                                                 {'id': 'd', 'text': 'D) Wearing European dress'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_3_1_87',
                                     'prompt': 'According to the text, what is cultural '
                                               'imperialism?',
                                     'choices': [{'id': 'a',
                                                  'text': "A) The appreciation of one's own "
                                                          'culture'},
                                                 {'id': 'b',
                                                  'text': "B) The imposition of one's own cultural "
                                                          'values on another culture'},
                                                 {'id': 'c',
                                                  'text': 'C) The belief that all cultures are '
                                                          'equal'},
                                                 {'id': 'd',
                                                  'text': 'D) The practice of respecting '
                                                          'indigenous cultures'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'QX3',
                                     'prompt': 'Select Option B below',
                                     'choices': [{'id': 'a', 'text': 'A) Red'},
                                                 {'id': 'b', 'text': 'B) Green'},
                                                 {'id': 'c', 'text': 'C) Blue'},
                                                 {'id': 'd', 'text': 'D) Yellow'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_3_1_88',
                                     'prompt': 'What can be inferred about ethnocentrism from the '
                                               'text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It encourages understanding and '
                                                          'acceptance of different cultures'},
                                                 {'id': 'b',
                                                  'text': 'B) It can lead to negative outcomes '
                                                          'such as conflict and stereotyping'},
                                                 {'id': 'c',
                                                  'text': 'C) It is a modern phenomenon that did '
                                                          'not exist in the past'},
                                                 {'id': 'd',
                                                  'text': 'D) It is primarily a positive force '
                                                          'within societies'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_3_1_89',
                                     'prompt': 'Based on the text, what is a potential consequence '
                                               'of international aid agencies introducing foreign '
                                               'agricultural methods?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Improved local agricultural '
                                                          'productivity'},
                                                 {'id': 'b',
                                                  'text': 'B) Loss of biodiversity and local '
                                                          'agricultural practices'},
                                                 {'id': 'c',
                                                  'text': 'C) Increased cultural diversity in the '
                                                          'region'},
                                                 {'id': 'd',
                                                  'text': 'D) Strengthening of indigenous cultural '
                                                          'practices'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_3_1_90',
                                     'prompt': 'What is the main idea of the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Cultural universals are more common '
                                                          'than cultural differences'},
                                                 {'id': 'b',
                                                  'text': 'B) Ethnocentrism is beneficial for '
                                                          'maintaining cultural identity'},
                                                 {'id': 'c',
                                                  'text': 'C) Cultural differences and '
                                                          'ethnocentrism can lead to cultural '
                                                          'imperialism'},
                                                 {'id': 'd',
                                                  'text': 'D) All cultures should adopt Western '
                                                          'cultural practices'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_sociology_3_1_86',
                                     'prompt': 'Q1: What does ethnocentrism mean?',
                                     'choices': [{'id': 'a',
                                                  'text': "A) Deliberately imposing one group's "
                                                          'values and practices on another.'},
                                                 {'id': 'b',
                                                  'text': "B) Expressing pride in one's community "
                                                          'to strengthen social bonds.'},
                                                 {'id': 'c',
                                                  'text': "C) Judging other cultures by one's "
                                                          'standards, deeming yours superior.'},
                                                 {'id': 'd',
                                                  'text': 'D) Recognizing common features shared '
                                                          'by societies, such as language.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_sociology_3_1_87',
                                     'prompt': 'Q2: What is cultural imperialism?',
                                     'choices': [{'id': 'a',
                                                  'text': "A) Assessing other cultures using one's "
                                                          'own cultural standards.'},
                                                 {'id': 'b',
                                                  'text': 'B) Common features present across all '
                                                          'societies.'},
                                                 {'id': 'c',
                                                  'text': "C) Deliberately imposing one group's "
                                                          'values on another society.'},
                                                 {'id': 'd',
                                                  'text': 'D) Fostering social cohesion through '
                                                          'pride in communal heritage.'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_sociology_3_1_88',
                                     'prompt': 'Q3: Given that many people judge other cultures by '
                                               'their own standards and this can produce '
                                               'misunderstanding, stereotyping, and conflict, '
                                               'which approach would most likely enhance effective '
                                               'cross-cultural interactions?',
                                     'choices': [{'id': 'a',
                                                  'text': "A) Emphasizing pride in one's heritage "
                                                          'while downplaying differences with '
                                                          'other groups'},
                                                 {'id': 'b',
                                                  'text': 'B) Establishing uniform behavioral '
                                                          'standards to align practices across '
                                                          'diverse societies'},
                                                 {'id': 'c',
                                                  'text': 'C) Minimizing contact with unfamiliar '
                                                          'groups to reduce clashes over customs '
                                                          'and beliefs'},
                                                 {'id': 'd',
                                                  'text': 'D) Promoting awareness of differing '
                                                          'customs and questioning assumptions '
                                                          'about unfamiliar practices'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX3',
                                     'prompt': 'Select Option B below',
                                     'choices': [{'id': 'a', 'text': 'A) Red'},
                                                 {'id': 'b', 'text': 'B) Green'},
                                                 {'id': 'c', 'text': 'C) Blue'},
                                                 {'id': 'd', 'text': 'D) Yellow'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_3_1_89',
                                     'prompt': 'Q4: Why might the introduction of foreign farming '
                                               'methods by aid groups and the expansion of timber '
                                               'companies into the Amazon both exemplify cultural '
                                               'imperialism?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Both arise because all cultures '
                                                          'share the same basic needs and '
                                                          'therefore benefit from uniform '
                                                          'solutions.'},
                                                 {'id': 'b',
                                                  'text': 'B) Both prioritize outside agendas that '
                                                          'displace region-specific knowledge and '
                                                          'erode indigenous lands and '
                                                          'livelihoods.'},
                                                 {'id': 'c',
                                                  'text': 'C) Both reflect the natural diffusion '
                                                          'of culture through voluntary exchange.'},
                                                 {'id': 'd',
                                                  'text': 'D) Both spread beneficial innovations '
                                                          'that raise productivity without '
                                                          'affecting local customs.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_3_1_90',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Cultural differences outweigh '
                                                          'universals, as seen in conversational '
                                                          'distance and eating and drinking '
                                                          'practices.'},
                                                 {'id': 'b',
                                                  'text': 'B) Ethnocentrism is a healthy '
                                                          'expression of pride that generally '
                                                          'strengthens societies and reduces '
                                                          'conflict.'},
                                                 {'id': 'c',
                                                  'text': "C) Imposing one culture's values on "
                                                          'another is mainly a feature of European '
                                                          'colonialism and has limited relevance '
                                                          'today.'},
                                                 {'id': 'd',
                                                  'text': 'D) Wide cultural variation is common, '
                                                          "and judging or imposing one culture's "
                                                          'norms (ethnocentrism, cultural '
                                                          'imperialism) causes harm.'}],
                                     'correct_choice_id': 'd'}]}},
 'p19': {'id': 'sociology_4_1',
         'questions': {'baseline': [{'question_id': 'baseline_sociology_4_1_91',
                                     'prompt': 'What new power source began appearing everywhere '
                                               'during the Industrial Revolution, replacing human '
                                               'and animal labor?',
                                     'choices': [{'id': 'a', 'text': 'A) Wind power'},
                                                 {'id': 'b', 'text': 'B) Steam power'},
                                                 {'id': 'c', 'text': 'C) Solar power'},
                                                 {'id': 'd', 'text': 'D) Hydroelectric power'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_4_1_92',
                                     'prompt': 'Which families became the new power players in '
                                               'business and government during the Industrial '
                                               'Revolution?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The Tudors and the Stuarts'},
                                                 {'id': 'b',
                                                  'text': 'B) The Rockefellers and the '
                                                          'Vanderbilts'},
                                                 {'id': 'c',
                                                  'text': 'C) The Medici and the Borgias'},
                                                 {'id': 'd',
                                                  'text': 'D) The Habsburgs and the Romanovs'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_4_1_93',
                                     'prompt': 'What can be inferred about the role of labor '
                                               'unions during the Industrial Revolution?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) They were supportive of business '
                                                          'owners.'},
                                                 {'id': 'b',
                                                  'text': 'B) They were formed to address concerns '
                                                          'over worker exploitation.'},
                                                 {'id': 'c',
                                                  'text': 'C) They were primarily interested in '
                                                          'technological advancements.'},
                                                 {'id': 'd',
                                                  'text': 'D) They were mainly focused on '
                                                          'agricultural productivity.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_4_1_94',
                                     'prompt': 'Why might the Industrial Revolution have led to a '
                                               'rise in urban centers?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) People wanted to leave the '
                                                          'countryside for better weather.'},
                                                 {'id': 'b',
                                                  'text': 'B) Urban centers provided more '
                                                          'educational opportunities.'},
                                                 {'id': 'c',
                                                  'text': 'C) The development of new technologies '
                                                          'required more space.'},
                                                 {'id': 'd',
                                                  'text': 'D) Factories offered jobs, attracting '
                                                          'workers from rural areas.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX2',
                                     'prompt': 'Select color from the following:',
                                     'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                 {'id': 'b', 'text': 'B) Rabbit'},
                                                 {'id': 'c', 'text': 'C) Yellow'},
                                                 {'id': 'd', 'text': 'D) Cat'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_sociology_4_1_95',
                                     'prompt': 'What is the main idea of the source text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The Industrial Revolution was '
                                                          'detrimental to society.'},
                                                 {'id': 'b',
                                                  'text': 'B) Technological inventions had little '
                                                          'impact on daily life.'},
                                                 {'id': 'c',
                                                  'text': 'C) The Industrial Revolution brought '
                                                          'about significant changes in '
                                                          'technology, society, and social '
                                                          'structure.'},
                                                 {'id': 'd',
                                                  'text': 'D) Agriculture remained the focus of '
                                                          'European societies during the '
                                                          'Industrial Revolution.'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_sociology_4_1_91',
                                     'prompt': 'Q1: Which change during the eighteenth-century '
                                               'Industrial Revolution most directly drove sharp '
                                               'gains in productivity and wider access to goods?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Expansion of steam-powered machinery '
                                                          'in factories and on farms.'},
                                                 {'id': 'b',
                                                  'text': 'B) Greater dependence on human and '
                                                          'animal power for production.'},
                                                 {'id': 'c',
                                                  'text': 'C) Growth of urban nightlife through '
                                                          'widespread gas lighting.'},
                                                 {'id': 'd',
                                                  'text': 'D) Mass migration to cities that '
                                                          'diversified populations.'}],
                                     'correct_choice_id': 'a'},
                                    {'question_id': 'requesta_sociology_4_1_92',
                                     'prompt': 'Q2: What circumstances in the Industrial '
                                               'Revolution spurred the emergence of sociology in '
                                               'the eighteenth and nineteenth centuries?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Advances in steam power and textile '
                                                          'production shifted inquiry toward '
                                                          'machinery rather than social '
                                                          'relations.'},
                                                 {'id': 'b',
                                                  'text': 'B) Expansion of aristocratic control '
                                                          'and renewed rural traditions directed '
                                                          'thinkers away from urban issues.'},
                                                 {'id': 'c',
                                                  'text': 'C) Increased schooling and medical care '
                                                          'persuaded scholars that major social '
                                                          'problems had declined.'},
                                                 {'id': 'd',
                                                  'text': 'D) Mass migration to cities and harsh '
                                                          'crowding, filth, and poverty prompted '
                                                          'study of person-society relations.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_sociology_4_1_93',
                                     'prompt': 'Q3: What does the birth of sociology during the '
                                               'Industrial Revolution most strongly indicate about '
                                               'how people sought to deal with the upheavals of '
                                               'urbanization?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Assuming that advances in machinery '
                                                          'would gradually remove the need to '
                                                          'study social issues'},
                                                 {'id': 'b',
                                                  'text': 'B) Creating a structured discipline to '
                                                          'analyze and address the disruptive '
                                                          'conditions of city life'},
                                                 {'id': 'c',
                                                  'text': 'C) Entrusting the wealthy '
                                                          'industrialists to restore order through '
                                                          'economic leadership alone'},
                                                 {'id': 'd',
                                                  'text': 'D) Relying on rural customs to guide '
                                                          'behavior in densely populated, diverse '
                                                          'communities'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_4_1_94',
                                     'prompt': 'Q4: What does the emergence of worker '
                                               'organizations and mandated workplace standards, '
                                               'alongside wider access to goods, schooling, and '
                                               'medical care, imply about early factory labor?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Employment in mills was generally '
                                                          'orderly and fair, lessening disputes '
                                                          'over treatment.'},
                                                 {'id': 'b',
                                                  'text': 'B) Mechanization quickly solved city '
                                                          'crowding and poverty by boosting pay.'},
                                                 {'id': 'c',
                                                  'text': 'C) The main impact was the erosion of '
                                                          'craft skills, not significant concerns '
                                                          'about treatment.'},
                                                 {'id': 'd',
                                                  'text': 'D) Work on the shop floor was often '
                                                          'harsh or risky, prompting collective '
                                                          'action and state oversight.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX3',
                                     'prompt': 'Select Option B below',
                                     'choices': [{'id': 'a', 'text': 'A) Red'},
                                                 {'id': 'b', 'text': 'B) Green'},
                                                 {'id': 'c', 'text': 'C) Blue'},
                                                 {'id': 'd', 'text': 'D) Yellow'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_4_1_95',
                                     'prompt': 'Q5: Which of the following best expresses the main '
                                               'idea of the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Industrial-era innovations reshaped '
                                                          'Europe, boosting output and '
                                                          'urbanization, shifting power, and '
                                                          'spurring social institutions and '
                                                          'ideas.'},
                                                 {'id': 'b',
                                                  'text': "B) Industrialization's urban problems "
                                                          'prompted governments to regulate '
                                                          'factories and protect workers.'},
                                                 {'id': 'c',
                                                  'text': 'C) Steam power and mechanization mainly '
                                                          'raised productivity and broadened '
                                                          'access to goods and services.'},
                                                 {'id': 'd',
                                                  'text': 'D) The rise of industrial capitalists '
                                                          'displaced the aristocracy and helped '
                                                          'give rise to sociology as a '
                                                          'discipline.'}],
                                     'correct_choice_id': 'a'}]}},
 'p20': {'id': 'sociology_5_2',
         'questions': {'baseline': [{'question_id': 'baseline_sociology_5_2_96',
                                     'prompt': 'What method do researchers use to study the impact '
                                               'of nature on human behavior?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Observing different cultures'},
                                                 {'id': 'b', 'text': 'B) Interviewing individuals'},
                                                 {'id': 'c', 'text': 'C) Studying twins'},
                                                 {'id': 'd',
                                                  'text': 'D) Analyzing historical records'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'baseline_sociology_5_2_97',
                                     'prompt': 'In what year were the twin girls mentioned in the '
                                               'study reunited?',
                                     'choices': [{'id': 'a', 'text': 'A) 1968'},
                                                 {'id': 'b', 'text': 'B) 1975'},
                                                 {'id': 'c', 'text': 'C) 1990'},
                                                 {'id': 'd', 'text': 'D) 2003'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_sociology_5_2_98',
                                     'prompt': 'What conclusion can be drawn about the role of '
                                               'genetics in behavior from the example of the '
                                               'reunited twins?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Genetics has no influence on '
                                                          'behavior.'},
                                                 {'id': 'b',
                                                  'text': 'B) Genetics plays a significant role in '
                                                          'shaping behavior.'},
                                                 {'id': 'c',
                                                  'text': 'C) Environment is the sole factor in '
                                                          'determining behavior.'},
                                                 {'id': 'd',
                                                  'text': 'D) Genetics only influences physical '
                                                          'appearance.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'baseline_sociology_5_2_99',
                                     'prompt': 'What might a conflict theorist suggest about the '
                                               'impact of socialization on individuals from '
                                               'different social classes?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Socialization creates equal '
                                                          'opportunities for all.'},
                                                 {'id': 'b',
                                                  'text': 'B) Socialization has no impact on '
                                                          'individuals from different classes.'},
                                                 {'id': 'c',
                                                  'text': 'C) Socialization helps individuals from '
                                                          'different classes understand each other '
                                                          'better.'},
                                                 {'id': 'd',
                                                  'text': 'D) Socialization reproduces inequality '
                                                          'by conveying different expectations and '
                                                          'norms.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX1',
                                     'prompt': 'Which of the following is NOT an animal?',
                                     'choices': [{'id': 'a', 'text': 'A) Dog'},
                                                 {'id': 'b', 'text': 'B) Elephant'},
                                                 {'id': 'c', 'text': 'C) Giraffe'},
                                                 {'id': 'd', 'text': 'D) Computer'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'baseline_sociology_5_2_100',
                                     'prompt': 'What is the main idea of the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Genetics is the sole factor '
                                                          'determining human behavior.'},
                                                 {'id': 'b',
                                                  'text': 'B) Socialization has no impact on human '
                                                          'development.'},
                                                 {'id': 'c',
                                                  'text': 'C) Both nature and nurture play '
                                                          'significant roles in shaping who we '
                                                          'are.'},
                                                 {'id': 'd',
                                                  'text': 'D) The study of twins is the best way '
                                                          'to understand human behavior.'}],
                                     'correct_choice_id': 'c'}],
                       'requesta': [{'question_id': 'requesta_sociology_5_2_96',
                                     'prompt': 'Q1: Which factors does sociology view as affecting '
                                               "people's lives as much as heredity?",
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Genetic predispositions established '
                                                          'before birth.'},
                                                 {'id': 'b',
                                                  'text': 'B) Hormonal differences that shape '
                                                          'temperament and behavior.'},
                                                 {'id': 'c',
                                                  'text': 'C) Innate interests and talents '
                                                          'determined by DNA.'},
                                                 {'id': 'd',
                                                  'text': 'D) Social influences such as race and '
                                                          'social class.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'requesta_sociology_5_2_97',
                                     'prompt': 'Q2: Which set of statements correctly '
                                               'distinguishes structural functionalist, conflict, '
                                               'and interactionist views of socialization?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Functionalist—maintains social order '
                                                          'and transmits culture; Conflict—reduces '
                                                          'inequality by setting common '
                                                          'expectations; Interactionist—examines '
                                                          'face-to-face symbols like gendered '
                                                          'color cues.'},
                                                 {'id': 'b',
                                                  'text': 'B) Functionalist—maintains social order '
                                                          'and transmits culture; '
                                                          'Conflict—reproduces inequality through '
                                                          'unequal expectations by social group; '
                                                          'Interactionist—examines face-to-face '
                                                          'symbols like gendered color cues.'},
                                                 {'id': 'c',
                                                  'text': 'C) Functionalist—reproduces inequality '
                                                          'by passing along class-specific norms; '
                                                          'Conflict—builds cohesion by teaching '
                                                          'shared values; Interactionist—focuses '
                                                          'on everyday symbolic exchanges such as '
                                                          'greetings.'},
                                                 {'id': 'd',
                                                  'text': 'D) Functionalist—maintains social order '
                                                          'and transmits culture; Conflict—treats '
                                                          'socialization as value-neutral, '
                                                          'reflecting shared norms; '
                                                          'Interactionist—emphasizes institutions '
                                                          'and mass media over face-to-face '
                                                          'symbolism.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_5_2_98',
                                     'prompt': 'Q3: Which conclusion best integrates the '
                                               'twin-study evidence with the sociological focus on '
                                               'race, class, and socialization?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) Biology accounts for most outcomes, '
                                                          'with socialization playing a minor '
                                                          'role.'},
                                                 {'id': 'b',
                                                  'text': 'B) Both inherited traits and social '
                                                          'contexts work together to shape '
                                                          'development.'},
                                                 {'id': 'c',
                                                  'text': 'C) Either biology or environment '
                                                          'typically overrides the other in '
                                                          'determining behavior.'},
                                                 {'id': 'd',
                                                  'text': 'D) Upbringing is the main driver, while '
                                                          'genes have little lasting impact.'}],
                                     'correct_choice_id': 'b'},
                                    {'question_id': 'requesta_sociology_5_2_99',
                                     'prompt': 'Q4: If institutions stopped sending distinct '
                                               'expectations based on gender, class, or race, what '
                                               'would the conflict perspective most likely predict '
                                               'for group differences in access to opportunities?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) The disparities would grow as '
                                                          'weakening cultural transmission '
                                                          'undermines cohesion.'},
                                                 {'id': 'b',
                                                  'text': 'B) The disparities would persist '
                                                          'because they are primarily biological.'},
                                                 {'id': 'c',
                                                  'text': 'C) The disparities would change shape '
                                                          'without lessening due to entrenched '
                                                          'role training.'},
                                                 {'id': 'd',
                                                  'text': 'D) The disparities would shrink as '
                                                          'fewer unequal messages are conveyed.'}],
                                     'correct_choice_id': 'd'},
                                    {'question_id': 'QX2',
                                     'prompt': 'Select color from the following:',
                                     'choices': [{'id': 'a', 'text': 'A) Deer'},
                                                 {'id': 'b', 'text': 'B) Rabbit'},
                                                 {'id': 'c', 'text': 'C) Yellow'},
                                                 {'id': 'd', 'text': 'D) Cat'}],
                                     'correct_choice_id': 'c'},
                                    {'question_id': 'requesta_sociology_5_2_100',
                                     'prompt': 'Q5: Which statement best summarizes the text?',
                                     'choices': [{'id': 'a',
                                                  'text': 'A) It claims sociologists downplay '
                                                          'biology and explain identity mainly by '
                                                          'race, class, and similar social '
                                                          'categories.'},
                                                 {'id': 'b',
                                                  'text': 'B) The passage argues that '
                                                          'socialization chiefly preserves '
                                                          'cultural continuity, aligning with a '
                                                          'structural functionalist view.'},
                                                 {'id': 'c',
                                                  'text': 'C) The text contrasts genetic and '
                                                          'social influences and highlights '
                                                          'sociological theories explaining how '
                                                          'socialization shapes behavior and '
                                                          'inequality.'},
                                                 {'id': 'd',
                                                  'text': 'D) Twin studies of separated identical '
                                                          'twins are used to argue that '
                                                          'temperament and behavior are mostly set '
                                                          'by genes.'}],
                                     'correct_choice_id': 'c'}]}}}

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
