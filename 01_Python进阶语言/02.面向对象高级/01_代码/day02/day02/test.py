
class nan:
    def your_sex(self):
        pass

class Xiaoming(nan):
    def sex(self):
        return '男'

class Xiaohao(nan):
    def sex(self):
        return '男'

class nvn:
    def sex(self):
        pass
class Xiaobai(nvn):
    def sex(self):
        return '女'

class Xiaofeng(nvn):
    def sex(self):
        return '女'

def how_sex(man):
    if man.sex() == '男':
        print('他是男')
    else:
        print('她是女')



if __name__ == '__main__':
    n1 = Xiaoming()
    n2 = Xiaohao()
    n3 = Xiaobai()
    n4 = Xiaofeng()
    how_sex(n1)
    how_sex(n2)
    how_sex(n3)
    how_sex(n4)







