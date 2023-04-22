class SysStack:
    def __init__(self):
        '''
        This is a stack to control the flow of the whole program. By implementing this,
        a back function is no longer necessary.
        The function name at the end of the call stack will always be the name of the
        function to be called!
        '''
        self.stack = []

    def add(self, func_name):
        self.stack.append(func_name)

    def remove(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def see_stack(self):
        return self.stack       # for debugging

    def control(self, func_name):
        '''
        This method receives function name and checks is the function is already in the stack.
        If yes, pop all function names after it. If no, add it to the end.
        '''
        if func_name in self.stack:
            while(self.peek() != func_name):
                self.remove()
        else:
            self.add(func_name)