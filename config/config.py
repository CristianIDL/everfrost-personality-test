QUESTIONS = {
    "artist-scientist": "Artistic or scientific?", 
    "planner-spontaneous": "Planner or spontaneous?",
    "library-gym": "Library or gym?",
    "wolf-pack-lone-wolf": "Wolf pack or lone wolf?",
    "volunteer-leader": "Volunteer or leader?",
    "optimist-realist": "Optimist or realist?",
    "anxious-calm": "Anxious or calm?",
}

'''
CONSTANTS structure:
    question: [lower_bound, upper_bound]

bounds:
    -1 to -0.2: First option
    -0.2 to 0.2: Balanced   
    0.2 to 1: Second option
'''

# TARGET PERSONALITY PROFILES
# Astrofusioners usually are scientific, planners, leaders, realists and balanced
ASTROFUSIONER = {
    "artist-scientist": [0.2, 1],
    "planner-spontaneous": [-1, -0.2],
    "library-gym": [-0.2, 0.2],
    "wolf-pack-lone-wolf": [-0.2, 0.2],
    "volunteer-leader": [0.2, 1],
    "optimist-realist": [0.2, 1],
    "anxious-calm": [-0.2, 0.2]
}

# Essentromancers are usually spontaneous, gym-goers, extroverts, optimists and emotional.
ESSENTROMANCER = {
    "artist-scientist": [-0.2, 0.2],
    "planner-spontaneous": [0.2, 1],
    "library-gym": [0.2, 1],
    "wolf-pack-lone-wolf": [-1, -0.2],
    "volunteer-leader": [-0.2, 0.2],
    "optimist-realist": [-1, -0.2],
    "anxious-calm": [-1, -0.2]
}

# Intergraphs are usually artistic, library-goers, lone wolves, volunteers, calmed and.
INTERGRAPH = {
    "artist-scientist": [-1, -0.2],
    "planner-spontaneous": [-0.2, 0.2],
    "library-gym": [-1, -0.2],
    "wolf-pack-lone-wolf": [0.2, 1],
    "volunteer-leader": [-1, -0.2],
    "optimist-realist": [-0.2, 0.2],
    "anxious-calm": [0.2, 1]
}

# Mapping of answers to personality types:
# 1: Artist: Intergraph;     Scientist: Astrofusioner; Balance: Essentromancer
# 2: Planner: Astrofusioner; Spontaneous: Essentromancer; Balance: Intergraph
# 3: Library: Intergraph;    Gym: Essentromancer; Balance: Astrofusioner
# 4: Wolf pack: Essentromancer; Lone wolf: Intergraph; Balance: Astrofusioner
# 5: Volunteer: Intergraph; Leader: Astrofusioner; Balance: Essentromancer
# 6: Optimist: Essentromancer; Realist: Astrofusioner; Balance: Intergraph
# 7: Anxious: Essentromancer; Calm: Intergraph; Balance: Astrofusioner

# Personality type scoring interval mappings. Number indicates the question number.