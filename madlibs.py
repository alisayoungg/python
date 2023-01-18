adj = input("Adjective: ")
adj1 = input("Adjective: ")
verb = input("Verb: ")
noun = input("Noun: ")
noun1 = input("Noun: ")


madlib = "Sometimes I feel like I am so {adj} and it makes me \
feel {adj1}. In order to stop feeling like a {noun}, I need to {verb} \
because otherwise I am a {noun1}.".format(adj=adj, adj1=adj1, noun=noun, verb=verb, noun1=noun1)

print("Therapy")
print(madlib)