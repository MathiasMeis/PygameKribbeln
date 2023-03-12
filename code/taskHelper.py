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

    def getTaskFromList(tasks : list[Task]):
        index : int = random.randint(0, len(tasks) - 1)
        return tasks[index]

    def getDefaultTasks() -> list[Task]:
        TaskHelper.setUpEasyTasks()
        TaskHelper.setUpMediumTasks()
        TaskHelper.setUpHardTasks()
        tasks : list[Task] = []
        helper : list[Task] = TaskHelper.getTasks(2,TaskHelper.easyTasks)
        tasks.append(helper[0])
        tasks.append(helper[1])
        tasks.append(Task_Kribbeln())
        helper : list[Task] = TaskHelper.getTasks(2,TaskHelper.mediumTasks)
        tasks.append(helper[0])
        tasks.append(helper[1])
        tasks.append(Task_Kribbeln())
        helper : list[Task] = TaskHelper.getTasks(2,TaskHelper.hardTasks)
        tasks.append(helper[0])
        tasks.append(helper[1])
        tasks.append(Task_Kribbeln())
        tasks.append(Task_Kribbeln())
        return tasks

    def getTasks(numberOfTasks, listOfTasks : list[Task]) -> list:
        remainingTasks : list = listOfTasks
        tasks : list = []
        index : int 
        for i in range(numberOfTasks):
            index = random.randint(0, len(remainingTasks)-1)
            tasks.append(remainingTasks[index])
            remainingTasks.remove(remainingTasks[index])

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
    

    def getEveryTask(): #only for testing
        allTasks : list[Task] = []
        allTasks.append(Task_ColorX(0))
        allTasks.append(Task_ColorX(1))
        allTasks.append(Task_ColorX(2))
        allTasks.append(Task_ColorX_and_ColorY(0,0))
        allTasks.append(Task_ColorX_and_ColorY(1,0))
        allTasks.append(Task_ColorX_and_ColorY(1,1))
        allTasks.append(Task_atLeast_ColorX(2))
        allTasks.append(Task_anyColor(2, True))
        allTasks.append(Task_ColorX(3))
        allTasks.append(Task_ColorX_and_ColorY(2,0))
        allTasks.append(Task_ColorX_and_ColorY(2,1))
        allTasks.append(Task_atLeast_ColorX(3))
        allTasks.append(Task_anyColor(3, True))
        allTasks.append(Task_anyColor(3, False))
        allTasks.append(Task_anyColor(2, False))
        allTasks.append(Task_numberOfColors(2))
        allTasks.append(Task_numberOfColors(3))
        allTasks.append(Task_anyColor_anyAnotherColor(2,2))
        allTasks.append(Task_anyColor_anyAnotherColor(3,2))
        allTasks.append(Task_anyColor(4, True))
        allTasks.append(Task_anyColor(5, True))
        allTasks.append(Task_ColorXY_equal(True))
        allTasks.append(Task_ColorXY_equal(False))
        allTasks.append(Task_ColorXYZ_equal(True))
        allTasks.append(Task_ColorXYZ_equal(False))
        allTasks.append(Task_ColorX_greater_ColorY())
        allTasks.append(Task_ColorX_greater_allOtherColors())
        return allTasks
