import click

def sheetTemplate4Col(result):
    Ravenclaw = result['Ravenclaw'];
    Slytherin = result['Slytherin'];
    Gryffindor = result['Gryffindor'];
    Hufflepuff = result['Hufflepuff'];
    click.echo(
        f"        ┃{Ravenclaw['index']:^13}┃{Slytherin['index']:^13}┃{Gryffindor['index']:^13}┃{Hufflepuff['index']:^13}\n"+
        f"┏━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━┓\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Count ┃{Ravenclaw['count']:^13}┃{Slytherin['count']:^13}┃{Gryffindor['count']:^13}┃{Hufflepuff['count']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Mean  ┃{Ravenclaw['mean']:^13}┃{Slytherin['mean']:^13}┃{Gryffindor['mean']:^13}┃{Hufflepuff['mean']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Std   ┃{Ravenclaw['std']:^13}┃{Slytherin['std']:^13}┃{Gryffindor['std']:^13}┃{Hufflepuff['std']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Min   ┃{Ravenclaw['min']:^13}┃{Slytherin['min']:^13}┃{Gryffindor['min']:^13}┃{Hufflepuff['min']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ 25%   ┃{Ravenclaw['25%']:^13}┃{Slytherin['25%']:^13}┃{Gryffindor['25%']:^13}┃{Hufflepuff['25%']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ 50%   ┃{Ravenclaw['50%']:^13}┃{Slytherin['50%']:^13}┃{Gryffindor['50%']:^13}┃{Hufflepuff['50%']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ 75%   ┃{Ravenclaw['75%']:^13}┃{Slytherin['75%']:^13}┃{Gryffindor['75%']:^13}┃{Hufflepuff['75%']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Max   ┃{Ravenclaw['max']:^13}┃{Slytherin['max']:^13}┃{Gryffindor['max']:^13}┃{Hufflepuff['max']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃\n"

    )

def sheetTemplate13Col(result):
    Arithmancy = result['Arithmancy'];
    Astronomy = result['Astronomy'];
    Herbology = result['Herbology'];
    DATDA = result['DATDA'];
    Divination = result['Divination'];
    MuggleStudies = result['MuggleStudies'];
    AncientRunes = result['Ancient Runes'];
    MagicHistory = result['Magic History'];
    Transfigurati = result['Transfigurati'];
    Potions = result['Potions'];
    CareCreature = result['Care Creature'];
    print(type(result['Care Creature']["std"]));
    Charms = result['Charms'];
    Flying = result['Flying'];
    click.echo(
        f"        ┃{Arithmancy['index']:^13}┃{Astronomy['index']:^13}┃{Herbology['index']:^13}┃{DATDA['index']:^13}┃{Divination['index']:^13}┃{MuggleStudies['index']:^13}"+
        f"┃{AncientRunes['index']:^13}┃{MagicHistory['index']:^13}┃{Transfigurati['index']:^13}┃{Potions['index']:^13}┃{CareCreature['index']:^13}┃{Charms['index']:^13}┃{Flying['index']:^13}\n"+
        f"┏━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━┓\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Count ┃{Arithmancy['count']:^13}┃{Astronomy['count']:^13}┃{Herbology['count']:^13}┃{DATDA['count']:^13}┃{Divination['count']:^13}┃{MuggleStudies['count']:^13}"+
        f"┃{AncientRunes['count']:^13}┃{MagicHistory['count']:^13}┃{Transfigurati['count']:^13}┃{Potions['count']:^13}┃{CareCreature['count']:^13}┃{Charms['count']:^13}┃{Flying['count']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Mean  ┃{Arithmancy['mean']:^13}┃{Astronomy['mean']:^13}┃{Herbology['mean']:^13}┃{DATDA['mean']:^13}┃{Divination['mean']:^13}┃{MuggleStudies['mean']:^13}"+
        f"┃{AncientRunes['mean']:^13}┃{MagicHistory['mean']:^13}┃{Transfigurati['mean']:^13}┃{Potions['mean']:^13}┃{CareCreature['mean']:^13}┃{Charms['mean']:^13}┃{Flying['mean']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Std   ┃{Arithmancy['std']:^13}┃{Astronomy['std']:^13}┃{Herbology['std']:^13}┃{DATDA['std']:^13}┃{Divination['std']:^13}┃{MuggleStudies['std']:^13}"+
        f"┃{AncientRunes['std']:^13}┃{MagicHistory['std']:^13}┃{Transfigurati['std']:^13}┃{Potions['std']:^13}┃{CareCreature['std']:^13}┃{Charms['std']:^13}┃{Flying['std']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Min   ┃{Arithmancy['min']:^13}┃{Astronomy['min']:^13}┃{Herbology['min']:^13}┃{DATDA['min']:^13}┃{Divination['min']:^13}┃{MuggleStudies['min']:^13}"+
        f"┃{AncientRunes['min']:^13}┃{MagicHistory['min']:^13}┃{Transfigurati['min']:^13}┃{Potions['min']:^13}┃{CareCreature['min']:^13}┃{Charms['min']:^13}┃{Flying['min']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ 25%   ┃{Arithmancy['25%']:^13}┃{Astronomy['25%']:^13}┃{Herbology['25%']:^13}┃{DATDA['25%']:^13}┃{Divination['25%']:^13}┃{MuggleStudies['25%']:^13}"+
        f"┃{AncientRunes['25%']:^13}┃{MagicHistory['25%']:^13}┃{Transfigurati['25%']:^13}┃{Potions['25%']:^13}┃{CareCreature['25%']:^13}┃{Charms['25%']:^13}┃{Flying['25%']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ 50%   ┃{Arithmancy['50%']:^13}┃{Astronomy['50%']:^13}┃{Herbology['50%']:^13}┃{DATDA['50%']:^13}┃{Divination['50%']:^13}┃{MuggleStudies['50%']:^13}"+
        f"┃{AncientRunes['50%']:^13}┃{MagicHistory['50%']:^13}┃{Transfigurati['50%']:^13}┃{Potions['50%']:^13}┃{CareCreature['50%']:^13}┃{Charms['50%']:^13}┃{Flying['50%']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ 75%   ┃{Arithmancy['75%']:^13}┃{Astronomy['75%']:^13}┃{Herbology['75%']:^13}┃{DATDA['75%']:^13}┃{Divination['75%']:^13}┃{MuggleStudies['75%']:^13}"+
        f"┃{AncientRunes['75%']:^13}┃{MagicHistory['75%']:^13}┃{Transfigurati['75%']:^13}┃{Potions['75%']:^13}┃{CareCreature['75%']:^13}┃{Charms['75%']:^13}┃{Flying['75%']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┣━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━\n" +
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n" +
        f"┃ Max   ┃{Arithmancy['max']:^13}┃{Astronomy['max']:^13}┃{Herbology['max']:^13}┃{DATDA['max']:^13}┃{Divination['max']:^13}┃{MuggleStudies['max']:^13}"+
        f"┃{AncientRunes['max']:^13}┃{MagicHistory['max']:^13}┃{Transfigurati['max']:^13}┃{Potions['max']:^13}┃{CareCreature['max']:^13}┃{Charms['max']:^13}┃{Flying['max']:^13}┃\n"+
        f"┃       ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃             ┃\n"

    )
    