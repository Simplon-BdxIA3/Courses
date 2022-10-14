# Day 2: Boolean and methods

## TD 1

### EXO1

Display the game answers with this syntax :
use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
```

output:
```bash
> question 0 - yes
> question 1 - yes
> question 2 - no
> question 3 - yes
```

### EXO2
Display the game answers with this syntax if the answer is yes :
Use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
```
output:
```bash
> question 0 - yes
> question 1 - yes
> question 3 - yes
```

### EXO 3
Display the number of yes in game answers :
use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
```

output:
```bash
> 3
```

### EXO 4 Annexe

Display the vegetables and its associated color
Use:
```bash
vegetables = ["Carotte", "Poireau", "Courgette"]
colors = ["Orange", "Blanche", "Verte"]
```

output:
```bash
Le légume nommé Carotte est de couleur Orange
Le légume nommé Poireau est de couleur Blanche
Le légume nommé Courgette est de couleur Verte
```

### EXO 4

Display the matching between Game answers and Pauline's answers
Use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
pauline_answers = [ "yes",  "yes", "no", "no" ]
```

output:
```bash
Game | Pauline
yes | yes
yes | yes
no | no
yes | no
```

### EXO 5

Display the matching between Game answers and Pauline's answers
just if Game answer and Pauline's answer are the same.
Use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
pauline_answers = [ "yes",  "yes", "no", "no" ]
```

output:
```bash
Game | Pauline
yes | yes
yes | yes
no | no
```

### EXO 6

Display the number of matchings between Game answers and Pauline's answers
Use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
pauline_answers = [ "yes",  "yes", "no", "no" ]
```

output:
```bash
3
```

### EXO 7

Display the number of matchings between Game answers and Pauline's answers
but you must use this structure
Use:
```bash
game_answers = [ "yes",  "yes", "no", "yes" ]
pauline_answers = [ "yes",  "yes", "no", "no" ]

def evaluate_matching_between(game_answers, student_answers):

  # ???

  matching

print(evaluate_matching_between(game_answers, pauline_answers))
```

output:
```bash
3
```
