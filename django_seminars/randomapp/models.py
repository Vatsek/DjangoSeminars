from django.db import models


class Coin(models.Model):
    side = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_last_n_flip(n):
        flips = Coin.objects.order_by('-timestamp')[:n]
        result = {'орёл': 0, 'решка': 0}
        for flip in flips:
            if flip.side == 'орёл':
                result['орёл'] += 1
            else:
                result['решка'] += 1
        return result