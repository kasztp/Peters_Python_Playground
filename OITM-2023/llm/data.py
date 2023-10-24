sentence_list = [
    "The cat sat on the windowsill and watched the birds outside.",
    "She opened the window to let in some fresh air.",
    "The windowpane was cracked and needed to be replaced.",
    "I could see the beautiful sunset through the window.",
    "He closed the curtains to block out the bright sunlight.",
    "The curtains swayed gently in the breeze.",
    "I love to sit by the fireplace and read a good book.",
    "The fire crackled and warmed the room.",
    "She roasted marshmallows over the campfire.",
    "The campfire provided much-needed warmth on a chilly night.",
    "The rain began to fall, and I hurriedly closed the umbrella.",
    "I forgot my umbrella, and I got soaked in the rain.",
    "She twirled her colorful umbrella as she walked in the rain.",
    "The umbrella shielded me from the downpour.",
    "We hiked to the top of the mountain and enjoyed the view.",
    "The mountain air was crisp and invigorating.",
    "The mountain trail was steep and challenging.",
    "We reached the mountain peak just before sunset.",
    "The beach was crowded with people enjoying the summer sun.",
    "I built a sandcastle with a moat at the beach.",
    "The waves crashed against the shore, creating a soothing sound.",
    "I collected seashells along the shoreline.",
    "The train sped down the tracks, heading for its destination.",
    "I waved goodbye to my friend as the train pulled away.",
    "The train station was bustling with travelers.",
    "The train conductor announced the next stop.",
    "The chef prepared a delicious meal using fresh ingredients.",
    "I savor every bite of the chef's special dish.",
    "The restaurant had a cozy atmosphere with dimmed lights.",
    "The aroma of the food filled the restaurant.",
    "The children played in the playground, laughing and running.",
    "The playground equipment included swings and slides.",
    "The playground was a popular spot for families.",
    "The playground was surrounded by lush green trees.",
    "The students eagerly listened to the teacher's instructions.",
    "I learned a lot from the teacher's informative lecture.",
    "The teacher encouraged class participation.",
    "The teacher's dedication to education was evident.",
    "The birds chirped in the trees as the sun rose.",
    "I woke up early to watch the sunrise.",
    "The sunrise painted the sky with shades of pink and orange.",
    "The sunrise signaled the start of a new day.",
    "The book was a thrilling mystery that kept me on the edge of my seat.",
    "I couldn't put the book down until I finished it.",
    "The book had a surprising plot twist that I didn't see coming.",
    "The book's ending left me wanting more.",
    "The flowers in the garden bloomed in vibrant colors.",
    "I spent hours tending to the garden and planting new flowers.",
    "The garden was a peaceful retreat from the hustle and bustle of the city.",
    "The garden's fragrance filled the air with sweetness.",
    "The musician played a beautiful melody on the piano.",
    "I was moved to tears by the musician's heartfelt performance.",
    "The piano's keys were polished to a shine.",
    "The piano's music echoed through the concert hall.",
    "The astronaut floated in space, admiring the stars and planets.",
    "I dream of becoming an astronaut and exploring the cosmos.",
    "The astronaut's spacesuit protected them from the harsh conditions of space.",
    "The astronaut's mission was to conduct experiments on the International Space Station.",
    "The detective examined the crime scene for clues.",
    "I enjoy reading detective novels and solving mysteries.",
    "The detective's sharp instincts led to the discovery of the culprit.",
    "The detective's dedication to solving cases was unwavering.",
    "The scientist conducted experiments in the laboratory.",
    "I have always been fascinated by the work of scientists.",
    "The scientist's research could revolutionize the field of medicine.",
    "The scientist's discoveries were published in prestigious scientific journals.",
    "The artist painted a masterpiece that captured the essence of nature.",
    "I admire the talent and creativity of artists.",
    "The artist's studio was filled with canvases and paintbrushes.",
    "The artist's work was displayed in galleries around the world.",
    "The storm raged outside, with thunder and lightning illuminating the sky.",
    "I stayed indoors and listened to the soothing sound of raindrops.",
    "The stormy weather made me appreciate the coziness of home.",
    "The storm eventually passed, leaving behind a sense of calm.",
    "The explorer ventured deep into the jungle, seeking adventure.",
    "I love reading about the adventures of brave explorers.",
    "The explorer encountered exotic wildlife and ancient ruins.",
    "The explorer's journey was documented in a bestselling book.",
    "The actor delivered a powerful monologue on the stage.",
    "I was moved by the actor's emotional performance.",
    "The actor's talent earned them critical acclaim.",
    "The actor's dedication to their craft was evident in every role.",
    "The beach was a tranquil place to relax and unwind.",
    "I could hear the gentle lapping of waves on the beach.",
    "The beach was scattered with seashells and pebbles.",
    "The beach was a perfect spot for a leisurely stroll.",
    "The inventor created a groundbreaking technology that changed the world.",
    "I'm fascinated by the stories of inventors and their inventions.",
    "The inventor's innovation revolutionized the way we live.",
    "The inventor's determination led to the success of their invention.",
    "The marathon runner trained tirelessly for the race.",
    "I admire the dedication and endurance of marathon runners.",
    "The marathon runner crossed the finish line to thunderous applause.",
    "The marathon runner's achievement was a testament to their hard work.",
    "The ocean waves crashed against the rocky shore.",
    "I find solace in listening to the rhythmic sound of ocean waves.",
    "The ocean was teeming with marine life and colorful coral reefs.",
    "The ocean's vastness reminded me of the endless possibilities in life.",
    "The detective followed a trail of clues that led to the suspect.",
    "I enjoy watching detective shows and trying to solve the cases.",
    "The detective's determination paid off when they solved the mystery.",
    "The detective's sharp mind was their greatest asset in solving crimes.",
    "The mountaineer scaled the towering peak of the mountain.",
    "I admire the courage and strength of mountaineers.",
    "The mountaineer reached the summit and planted their flag.",
    "The mountaineer's journey was filled with challenges and triumphs.",
    "The garden was a haven for butterflies and bees.",
    "I planted a variety of flowers to attract pollinators to the garden.",
    "The garden's beauty was enhanced by the presence of colorful butterflies.",
    "The garden's ecosystem was a delicate balance of plants and insects.",
    "The artist's brushstrokes brought the canvas to life.",
    "I visited the artist's gallery and was captivated by their work.",
    "The artist's creativity knew no bounds.",
    "The artist's studio was a place of inspiration and imagination.",
    "The musician's song touched the hearts of everyone in the audience.",
    "I have a deep appreciation for the talent of musicians.",
    "The musician's melodies were a source of comfort and joy.",
    "The musician's passion for music was evident in every note they played.",
    "The astronaut's journey into space was a lifelong dream.",
    "I watched in awe as the astronaut floated in zero gravity.",
    "The astronaut's mission was to conduct experiments on the International Space Station.",
    "The astronaut's dedication to exploration was truly inspiring.",
    "The detective's sharp instincts led to the discovery of crucial evidence.",
    "I enjoy solving puzzles and riddles, just like a detective.",
    "The detective's determination to solve the case was unwavering.",
    "The detective's thorough investigation uncovered the truth.",
    "The scientist's experiments in the laboratory yielded groundbreaking results.",
    "I have a deep respect for the scientific method and the work of scientists.",
    "The scientist's research had the potential to change the world.",
    "The scientist's discoveries were met with excitement and curiosity.",
    "The artist's palette was filled with a vibrant array of colors.",
    "I marveled at the artist's ability to capture emotion on canvas.",
    "The artist's work was displayed in prestigious art galleries.",
    "The artist's passion for art was evident in every brushstroke.",
    "The stormy weather made me appreciate the warmth of home.",
    "I cozied up by the fireplace with a good book during the storm.",
    "The storm eventually passed, leaving behind a sense of calm and serenity.",
    "The explorer's journey through the dense jungle was filled with excitement.",
    "I love reading about the adventures of intrepid explorers.",
    "The explorer discovered hidden treasures and documented their findings.",
    "The explorer's courage and curiosity were the driving forces behind their expeditions.",
    "The actor's performance on stage left a lasting impression on the audience.",
    "I was moved to tears by the actor's heartfelt portrayal of the character.",
    "The actor's dedication to their craft was evident in their commitment to the role.",
    "The actor's talent earned them critical acclaim and accolades."
]

def longest_substr_bing(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr


def longest_substr_copilot(data):
    """ Longest substring
    Get the longest equivalent substring from a set of strings.
    The name of the function should be `longest_substr`,
    it gets a `data` parameter, which is the collection of the strings.
    
    Return the longest substring.

    Example input
    ['csinos almás kitti', 'finom almás pite', 'édes-almás süti']

    Example output
    almás
    """
    for i in range(len(data[0])):
        for j in range(len(data[0]) - i + 1):
            if j > len(data[0]) - i:
                break
            if all(data[0][i:i+j] in s for s in data):
                return data[0][i:i+j]
    

print(longest_substr_bing(sentence_list))
print(longest_substr_copilot(sentence_list))
