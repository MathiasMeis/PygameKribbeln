import Player
import Task

#hier werden die aufgaben gesetzt. 2xeasy + kribbeln1 + 2xmedium + kribbeln2 + 2xhard + kribbeln3+4
# ui stuff dafür könnte auch in ne andere klasse ausgelagert werden, wenns zu viel wird
# ui sollte beim würfeln als overlay realisiert werden, könnte über hide() und show() getooglet werden
# punkte können hier oder beim spieler selbst hinterlegt werden. letzteres könnte sinniger sein, wenn man die spielerreihenfolge variabel nach punkten macht
# bzw ab 2tem kribbeln nach punkten schauen
class ScoreBoard:
    players : list
    tasks : list
