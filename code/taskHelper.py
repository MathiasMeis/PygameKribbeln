from difficulty import Difficulty
from task import Task 
from Tasks.task_anyColor_anyAnotherColor import Task_anyColor_anyAnotherColor
from Tasks.task_anyColor import Task_anyColor
from Tasks.task_atLeast_ColorX import Task_atLeast_ColorX
from Tasks.task_ColorX_and_ColorY import Task_ColorX_and_ColorY
from Tasks.task_ColorX_greater_allOtherColors import Task_ColorX_greater_allOtherColors
from Tasks.task_ColorX_greater_ColorY import Task_ColorX_greater_ColorY
from Tasks.task_ColorX import Task_ColorX
from Tasks.task_ColorXY_equal import Task_ColorXY_equal
from Tasks.task_ColorXYZ_equal import Task_ColorXYZ_equal
from Tasks.task_Kribbeln import Task_Kribbeln
from Tasks.task_numberOfColors import Task_numberOfColors
import random

class TaskHelper:
    easyTasks : list[Task]
    mediumTasks : list[Task]
    hardTasks : list[Task]

    def setUpEasyTasks():
        TaskHelper.easyTasks : list[Task] = []
        TaskHelper.easyTasks.append(Task_ColorX(0))
        TaskHelper.easyTasks.append(Task_ColorX(1))
        TaskHelper.easyTasks.append(Task_ColorX(2))
        TaskHelper.easyTasks.append(Task_ColorX_and_ColorY(0,0))
        TaskHelper.easyTasks.append(Task_ColorX_and_ColorY(1,0))
        TaskHelper.easyTasks.append(Task_ColorX_and_ColorY(1,1))
        TaskHelper.easyTasks.append(Task_atLeast_ColorX(2))
        TaskHelper.easyTasks.append(Task_anyColor(2, True))

    def setUpMediumTasks():
        TaskHelper.mediumTasks : list[Task] = []
        TaskHelper.mediumTasks.append(Task_ColorX(3))
        TaskHelper.mediumTasks.append(Task_ColorX_and_ColorY(2,0))
        TaskHelper.mediumTasks.append(Task_ColorX_and_ColorY(2,1))
        TaskHelper.mediumTasks.append(Task_atLeast_ColorX(3))
        TaskHelper.mediumTasks.append(Task_anyColor(3, True))
        TaskHelper.mediumTasks.append(Task_anyColor(3, False))
        TaskHelper.mediumTasks.append(Task_anyColor(2, False))
        TaskHelper.mediumTasks.append(Task_numberOfColors(2))
        TaskHelper.mediumTasks.append(Task_numberOfColors(3))
        TaskHelper.mediumTasks.append(Task_anyColor_anyAnotherColor(2,2))
        TaskHelper.mediumTasks.append(Task_anyColor_anyAnotherColor(3,2))

    def setUpHardTasks():
        TaskHelper.hardTasks : list[Task] = []
        TaskHelper.hardTasks.append(Task_anyColor(4, True))
        TaskHelper.hardTasks.append(Task_anyColor(5, True))
        TaskHelper.hardTasks.append(Task_ColorXY_equal(True))
        TaskHelper.hardTasks.append(Task_ColorXY_equal(False))
        TaskHelper.hardTasks.append(Task_ColorXYZ_equal(True))
        TaskHelper.hardTasks.append(Task_ColorXYZ_equal(False))
        TaskHelper.hardTasks.append(Task_ColorX_greater_ColorY())
        TaskHelper.hardTasks.append(Task_ColorX_greater_allOtherColors())

    def getTaskFromList(tasks : list):
        index : int = random.randint(0, len(tasks) - 1)
        return tasks[index]

    def getDefaultTasks() -> list[Task]:
        TaskHelper.setUpEasyTasks()
        TaskHelper.setUpMediumTasks()
        TaskHelper.setUpHardTasks()
        tasks : list = []
        tasks.append(TaskHelper.getTaskFromList(TaskHelper.easyTasks))
        tasks.append(TaskHelper.getTaskFromList(TaskHelper.easyTasks))
        tasks.append(Task_Kribbeln())
        tasks.append(TaskHelper.getTaskFromList(TaskHelper.mediumTasks))
        tasks.append(TaskHelper.getTaskFromList(TaskHelper.mediumTasks))
        tasks.append(Task_Kribbeln())
        tasks.append(TaskHelper.getTaskFromList(TaskHelper.hardTasks))
        tasks.append(TaskHelper.getTaskFromList(TaskHelper.hardTasks))
        tasks.append(Task_Kribbeln())
        tasks.append(Task_Kribbeln())
        return tasks

    def isKribbelnTask(task : Task) -> bool:
        if (isinstance(task, Task_Kribbeln)):
            return True
        else:
            return False
        
    def setKribbelnMinumum(minimum : int):
        Task_Kribbeln.minimumPoints = minimum

    def getTestTask() -> Task:
        return Task_ColorX(2)