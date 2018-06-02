#!/usr/bin/env python2
# coding: utf-8

from collections import namedtuple

BlockIDLen = 47


class BlockBaseError(Exception):
    pass


class BlockIDError(BlockBaseError):
    pass


class BlockID(namedtuple('_BlockID', 'type block_group_id block_index drive_id pg_seq')):

    @classmethod
    def parse(cls, block_id):

        if len(block_id) != BlockIDLen:
            raise BlockIDError('Block id length should be {0}, but is {1}: {2}'.format(
                BlockIDLen, len(block_id), block_id))

        return BlockID(block_id[0], block_id[1:17], block_id[17:21], block_id[21:37], block_id[-10:])

    def __str__(self):
        return self.type + self.block_group_id + self.block_index + self.drive_id + self.pg_seq