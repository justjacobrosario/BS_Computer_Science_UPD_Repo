class Bank:
    #                  v abstract
    def __init__(self, vault: Vault):  # dependency injection
        self.vault = vault
        # self.vault = CombinationVault("...") # <-- concrete dependency
