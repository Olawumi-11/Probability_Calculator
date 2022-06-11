#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to get random n number of hats from contents
def draw(self,amount):
    draw_list = []
    if amount >= len(self.contents):
        return self.contents
    for i in range(amount):
        name=self.contents.pop(random.ranndrange(len(self.contents)))
        draw_list.append(name)
    return draw_list

# importing the modules needed
import copy
import random

class Hat:
    def prob_lem(self,**all_item):
        self.contents=[]
        for key,value in all_item.items():
            for y in range(value):
                self.contents.append(key)

#function to get the probability

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count=0
    for x in range(num_experiments):
        copyhat = copy.deepcopy(hat)
        temp_list = copyhat.draw(num_balls_drawn)
        success=True
        for key,value in expected_balls.items():
            if temp_list.count(key) < value:
                success=False
                break
            if success:
                final_count+=1
        return final_count/num_experiments

