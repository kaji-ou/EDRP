

class TaskManager():
    @classmethod
    def assign_task(cls, agent_num, current_tasklist, assigned_tasklist):
        for i in range(agent_num):
            if len(assigned_tasklist[i])==0 and len(current_tasklist)>0 :
                task = current_tasklist.pop(0)
                assigned_tasklist[i] = task
        return current_tasklist, assigned_tasklist