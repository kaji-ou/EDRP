# What to implement
- task list
  - task has start node, goal node, deadline
- task creator
  - density of tasks
  - influence hours
  - random
- list of what tasks were assigned
- GUI of task list

# Implementation Ideas
- task list
  - a queue or list whose elements are taple(start_node, goal_node, deadline)
- task creator
  - density of tasks
  - influence hours
  - random
    - The addition of tasks is not necessarily limited to one per step
    - First is to create a whole task list at the start of the episode
      - at the beginning of the episode, create a list of tasks that the agent can observe and a list of tasks that should be assigned in the future
      - The latter list has information about when and what tasks are to be added to the former list
          - The latter list is an array　or list of time limit size
          - Ex list(list(taple(start_node, goal_node, deadline)))
    - Second is to create tasks for each step

- list of what tasks were assigned
  - an array or list whose size is the same as the number of drones and whose elements are taple(start_node, goal_node, deadline)
- GUI of task list

