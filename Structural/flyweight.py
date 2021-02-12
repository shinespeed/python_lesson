from typing import List


class BlockType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self):
        print(self.name)
        print(self.color)
        print(self.texture)
        print(self)


class BlockFactory:
    blockType: List[BlockType] = []

    @staticmethod
    def getBlockType(name, color, texture):
        type = BlockType(name, color, texture)
        if len(BlockFactory.blockType) == 0:
            BlockFactory.blockType.append(type)
        else:
            for block in BlockFactory.blockType:
                if block.__dict__ != type.__dict__:
                    BlockFactory.blockType.append(type)
        return type


class Block:
    def __init__(self, x, y, type: BlockType):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        print(self.y)
        print(self.x)
        self.type.draw()


class BlockList:
    blocks: List[Block] = []

    def addBlock(self, x, y, name: str, color: str, texture: str):
        type = BlockFactory.getBlockType(name, color, texture)
        block = Block(x, y, type)
        self.blocks.append(block)

    def draw(self):
        for block in self.blocks:
            block.draw()


if __name__ == "__main__":
    blockList = BlockList()
    blockList.addBlock(33, 56, "block", "red", "texture_block")
    blockList.addBlock(13, 15, "block", "red", "texture_block")
    blockList.addBlock(13, 15, "block", "green", "texture_block")
    blockList.addBlock(131, 151, "block", "green", "texture_block")

    print(BlockFactory.blockType)

    blockList.draw()