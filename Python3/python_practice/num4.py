def work_status(task,worker,day):
    rest_task = task
    for k in range(day):
        if rest_task > 0:
            rest_task = rest_task-worker
        elif rest_task <= 0:
            print("task end")
    if rest_task > 0:
        print('more workers')

work_status(100,11,10)
work_status(100,1,10)
work_status(100,9,10)
work_status(100,10,10)

