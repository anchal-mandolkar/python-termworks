import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cal_stat(data):
    avg_score=np.mean(data['score'])
    min_score=np.min(data['score'])
    max_score = np.max(data['score'])
    num_stud = len(data)
    return (avg_score,max_score,min_score,num_stud)

def create_visual(data):
    plt.figure(figsize=(8,6))
    plt.hist(data['score'],bins=10, color = 'pink')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Exam Score Distribution')
    plt.show()
    top_students=data[data['score']>=90]
    plt.figure(figsize=(8,6))
    plt.bar(top_students['name'],top_students['score'],color='green')
    plt.xlabel('Student Name')
    plt.ylabel('Score')
    plt.title('Top performing students')
    plt.xticks(rotation=45)
    plt.show()

def main():
    exam_data=pd.read_csv("exam_scores.csv")
    avg_score,max_score,min_score,num_students=cal_stat(exam_data)
    print("Average score: ",avg_score)
    print("Maximum score: ", max_score)
    print("Minimum score: ", min_score)
    print("Number of students: ", num_students)
    create_visual(exam_data)

if __name__=="__main__":
    main()