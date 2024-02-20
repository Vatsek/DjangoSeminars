from django import forms


class RandomGames(forms.Form):
    games = [['Coin', 'Бросить монету'],['Dice', 'Бросить игральную кость'],['Random_num','Сгенерировать случайное число']]
    game = forms.ChoiceField(choices=games, label='Выберите игру')
    count = forms.IntegerField(min_value=1, max_value=64, label='Введите кол-во попыток')
