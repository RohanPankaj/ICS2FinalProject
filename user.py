from topic import topic
import applicationMap


class user(object):
    def __init__(self):
        self.topics = {}

    #N: add_topic
    # D: adds a topic to the task manager
    # I: new_topic (string) - the name of the new topic
    #R: N/A
    def add_topic(self, new_topic):
        self.topics[new_topic] = topic()

    #N: delete_topic
    # D: deletes topic from the task manager
    # I: old_topic (string) - the name of the old topic
    #R: N/A
    def delete_topic(self, old_topic):
        del self.topics[old_topic]

    #N: check_if_active_topic()
    # D: check if a topic already exists
    # I: topic (string) the name of the topic
    # R: False if the topic does not exist and true if the topic already exists
    def check_if_active_topic(self, topic):
        if topic not in applicationMap.m_user.topics:
            return False
        else:
            return True

    #N: print_all
    # D: prints all the topics and their corresponding tasks
    #I: N/A
    # R: prints all the topics and theor correcponding tasks
    def print_all(self):
        for topic in self.topics:
            print(topic)
            for key in self.topics.keys():
                for task in self.topics[key].task_list:
                    print(task[0])

    #N: prioitize
    # D: prioritizes all the tasks in their corresponding topics based on which tasks should be completed first
    # I: the name of the new topic
    #R: N/A
    def prioritize(self, topics_dictionary):
        for topic in topics_dictionary:
            print(topic)
            prioritized_tasks = []
            longest_duration = 0
            longest_duration_key = None
            for i in range(0, len(self.topics[topic].task_list)):
                for task in self.topics[topic].task_list:
                    if longest_duration <= task[1]:
                        prioritized_tasks.insert(0, (task[0], task[2]))
                        longest_duration = task[1]
                        self.topics[topic].task_list.remove(task)
            for task in prioritized_tasks:
                print(task)
