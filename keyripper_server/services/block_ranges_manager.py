from keyripper_server.infra import log
from keyripper_server.apis import Firebase


class BlockRanges:

    def __init__(
            self,
            address: int
        ) -> None:
        self.address = address
        self.firebase = Firebase()
    
    def block_builder(self):
        connection = self.firebase.firebase_connection("root")
        
        return
    
    def block_provider(self):
        return

    def block_validator(self):
        return


if __name__ == "__main__":
    block_ranges = BlockRanges(
        address=30
    )

    block_ranges.block_builder()
