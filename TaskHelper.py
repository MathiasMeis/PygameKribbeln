import Difficulty
import random
import Task 
import Tasks.Task_anyColor
import Tasks.Task_ColorX
import Tasks.Task_Kribbeln
#import all tasks

class TaskHelper:
    easyTasks : list = []
    mediumTasks : list
    hardTasks : list

    def getRandomTask(dif) -> Task: #evtl überflüssig, ggfs einfacher wenn andere modis dazukommen
        print()

    def getRandomEasyTask() -> Task:
        return TaskHelper.easyTasks[random.randint(0, len(TaskHelper.easyTasks))]

    def getRandomMediumTask() -> Task:
        return TaskHelper.mediumTasks[random.randint(0, len(TaskHelper.mediumTasks))]

    def getRandomHardTask() -> Task:
        return TaskHelper.hardTasks[random.randint(0, len(TaskHelper.hardTasks))]

    def getDefaultTasks() -> list:
        tasks : list = []
        tasks.append(TaskHelper.getRandomEasyTask())
        tasks.append(TaskHelper.getRandomEasyTask())
        tasks.append(Tasks.Task_Kribbeln())
        tasks.append(TaskHelper.getRandomMediumTask())
        tasks.append(TaskHelper.getRandomMediumTask())
        tasks.append(Tasks.Task_Kribbeln())
        tasks.append(TaskHelper.getRandomHardTask())
        tasks.append(TaskHelper.getRandomHardTask())
        tasks.append(Tasks.Task_Kribbeln())
        tasks.append(Tasks.Task_Kribbeln())

