'''I Rotoli dei Giudici attendono il tuo sigillo: assegna il grado corretto con `grade(score)`, usando soglie **decrescenti**: `A` per `score >= 90`, poi `B` `>= 80`, `C` `>= 70`, `D` `>= 60`, altrimenti `F`. Mantieni la firma e soddisfa i test.'''

def grade(score: int) -> str:
    
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    else:
        return 'F'