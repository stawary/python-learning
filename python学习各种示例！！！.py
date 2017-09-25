#1、字符串拼接：
#str1 = input('请输入一个人的名字：')
#str2 = input('请输入一个国家的名字：')
#print("世界这么大，{}想去{}看看。".format(str1,str2))

#请输入一个人的名字：涂修建
#请输入一个国家的名字：法国
#世界这么大，涂修建想去法国看看。


#2、整数序列求和
#n = input("请输入整数N:")
#sum = 0
#for i in range(int(n)):
    #sum += i+1
#print('1到N求和结果：',sum)


#3、九九乘法表
#for i in range(1,10):
    #for j in range(1,i+1):
        #print('{}*{}={:2}'.format(j,i,i*j),end='')
    #print('')
#1*1= 1
#1*2= 22*2= 4
#1*3= 32*3= 63*3= 9
#1*4= 42*4= 83*4=124*4=16
#1*5= 52*5=103*5=154*5=205*5=25
#1*6= 62*6=123*6=184*6=245*6=306*6=36
#1*7= 72*7=143*7=214*7=285*7=356*7=427*7=49
#1*8= 82*8=163*8=244*8=325*8=406*8=487*8=568*8=64
#1*9= 92*9=183*9=274*9=365*9=456*9=547*9=638*9=729*9=81


#4、阶乘计算 .计算1+2！+3！+…+10！
#sum,tmp = 0,1
#for i in range(1,4):
    #tmp*=i
    #sum+=tmp #sum=sum+tmp
#print('运算结果是：{}'.format(sum))


#5、健康食谱输出。列出5种不同的食材，输出所有可能组成的菜式名称。即排列组合。。
#diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
#for x in range(0,5):
 #   for y in range(0,5):
  #      if not(x==y):
  #          print('{}{}'.format(diet[x],diet[y]))

#6、绘制红色五角星  没成功，在pycharm试试
#from turtle import *
#fillcolor('red')
#begin_fill()
#while Ture:
 #   forward(200)
  #  right(144)
   # if abs(pos())<1:
    #    break
#end_fill()


#7、太阳花绘制 成功！
#from turtle import *
#color('red','yellow')
#begin_fill()
#while True:
 #   forward(200)
  #  left(170)
   # if abs(pos())<1:
   #     break
#end_fill()
#done()

#8、彩色螺旋线绘制
import turtle
import time
turtle.pensize(2)
turtle.bgcolor('black')
colors=['red','yellow','purple','blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
turtle.tracer(True)
    
