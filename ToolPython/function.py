class functions:
    def substring_after(self,s, substring):
        return s.partition(substring)[2]

    def substring_before(self,s, substring):
        return s.partition(substring)[0]
