#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order,along with the answer key

import random
import os
#the quizdata.keys are states and values are their capitals.
capitals={'北京市':'北京','上海市':'上海','天津市':'天津','重庆市':'重庆','黑龙江省':'哈尔滨','吉林省':'长春','辽宁省':'沈阳','内蒙古自治区':'呼和浩特','河北省':'石家庄','新疆维吾尔自治区':'乌鲁木齐','甘肃省':'兰州','青海省':'西宁','陕西省':'西安','宁夏回族自治区':'银川','河南省':'郑州','山东省':'济南','山西省':'太原','安徽省':'合肥','湖南省':'长沙','湖北省':'武汉','江苏省':'南京','四川省':'成都','贵州省':'贵阳','云南省':'昆明','广西壮族自治区':'南宁','西藏自治区':'拉萨','浙江省':'杭州','江西省':'南昌','广东省':'广州','福建省':'福州','台湾省':'台北','海南省':'海口','香港特别行政区':'香港','澳门特别行政区':'澳门'
}
#generate 48 quiz files.
for quizNum in range(25):
    
    #create the quiz and answer key files.
    quizFile=open('capitalsquiz%s.txt' % (quizNum+1),'w')
    answerKeyFile=open('capitalsquiz_answer%s.txt' % (quizNum+1),'w')
    
    #write out the header of the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriond:\n\n')
    quizFile.write((' ' *20)+'全国省会名称测验(表%s)'% (quizNum+1))
    quizFile.write('\n\n')
    
    #shuffle the the order of the states
    states=list(capitals.keys())
    random.shuffle(states)
    
    #loop through all 34 states,making a question for each
    for questionNum in range(34):
        
        #get right and wrong answer
        correctAnswer=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)
        
        #write the questions and options to the quiz file
        quizFile.write('%s. what is the capital of %s?\n'%(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
            
        quizFile.write('\n')
        
            #write the answer key to a files
        answerKeyFile.write('%s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))

    
        
        
       
        
