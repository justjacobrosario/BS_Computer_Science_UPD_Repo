class LabGroup:
    def __init__(self, members: set[str]):  # What can go wrong with this?
        if len(members) not in {1, 2}:
            raise ValueError(f'Members must be between 1 and 2 (inclusive)')
 
        self._members = members             # What can go wrong with this?
 
    def add_member(self, member: str):
        if member in self.members:
            raise ValueError('Member is already in group')
 
        if len(self.members) == 2:
            raise ValueError('Group must have at most two members')
 
        self._members.add(member)
 
    @property
    def members(self):
        return self._members                # What can go wrong with this?