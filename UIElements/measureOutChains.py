from kivy.uix.widget                      import   Widget
from kivy.properties                      import   ObjectProperty, StringProperty

class MeasureOutChains(Widget):
    '''
    
    Provides a standard interface for measuring out a known length of both chains
    
    '''
    data              =  ObjectProperty(None) #set externally
    text              =  StringProperty("")
    
    def stop(self):
        self.data.quick_queue.put("!") 
        with self.data.gcode_queue.mutex:
            self.data.gcode_queue.queue.clear()
    
    def calibrateChainLengths(self, direction):
        cmdString = "B02 " + str(direction) + " "
        self.data.gcode_queue.put("B02 ")
    
    def next(self):
        self.data.gcode_queue.put("B15 ")
        self.carousel.load_next()