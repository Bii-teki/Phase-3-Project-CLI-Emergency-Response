import fire
  
class Square(object):
  
    def square(self, number):
        return number*number
  
fire.Fire(Square)