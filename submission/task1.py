id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(
        choices=[
            'Hat',
            'Pants',
            'Shirt',
            'Apple',
            'Banana',
            'Pots',
            'Towels',
            'Ford',
            'Chevy',
            'Hammer',
            'Wrench'
         ]
    )
    description = factory.Faker('sentence', nb_words=4)
    price = FuzzyDecimal(low=0.5,high=2000.0, precision=2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )