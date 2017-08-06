
# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006 Otto-von-Guericke-Universität Magdeburg
#
# This file is part of ECAssignmentBox.
#
# ECAssignmentBox is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# ECAssignmentBox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ECAssignmentBox; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

#===============================================================================
#Author: Christian Dervaric
#
#Description:
#This module contains the class PlagResult. PlagResult is an object holding
#informations about the result of the plagiarism tests called from PlagChecker.
#===============================================================================

from errors import NoValidArgumentError, OutOfRangeError, NoIdentifierSetError



class PlagResult(object):
    """Class for the result of the comparison of two texts for plagiarism.
	"""

    def __init__(self, id1 = None , id2 = None):
        """Initializes the PlagResult object."""
        self.tiles = []
        self.similarity = 0.0
        self.id1 = id1
        self.id2 = id2
        self.id1StringLength = 0
        self.id2StringLength = 0
        self.algName = ""
        self.normName = ""
        self.suspectedPlagiarism = False

#===============================================================================
#   GETTER AND SETTER
#===============================================================================
    def setTiles(self, tiles):
        """Set tiles found in the Test for plagiarism."""
        if type(tiles) != type([]):
            raise NoValidArgumentError
        else:
            self.tiles = tiles

    def getTiles(self):
        rf_tiles = self.tiles
        rf_tiles=sorted(rf_tiles, key=lambda x: x[0])
        # print enumerate(rf_tiles)
        rf = []
        i = 0
        for tile in rf_tiles:
            # print i
            # print tile[0]
            if i == 0:
                rf.append(tile)
                i = i + 1
                continue
            if rf[i - 1][0] == tile[0]:
                continue
            else:
                rf.append(tile)
                i = i + 1
        return rf
    # def getRefineTiles(self):
    #     rf_tiles = self.tiles
    #     # print enumerate(rf_tiles)
    #     rf = []
    #     i=0
    #     for  tile in rf_tiles:
    #         # print i
    #         # print tile[0]
    #         if i == 0:
    #             rf.append(tile)
    #             i=i+1
    #             continue
    #         if rf[i - 1][0] == tile[0]:
    #             continue
    #         else:
    #             rf.append(tile)
    #             i=i+1

        #return rf
    def setSimilarity(self, similarity):
        """Set similarity calculated in the Test for plagiarism."""
        if not (0 <= similarity <= 1):
            raise OutOfRangeError
        else:
            self.similarity = similarity

    def getSimilarity(self):
        """Get similarity calculated in the Test for plagiarism."""
        return self.similarity

    def setIdentifier(self, id1, id2):
        """Set identifier for each compared text."""
        self.id1 = id1
        self.id2 = id2

    def getIdentifier(self):
        """Get the identifier for the compared texts."""
        if self.id1 == None or self.id2 == None:
            raise NoIdentifierSetError
        return [self.id1, self.id2]

    def containsIdentifier(self, id):
        """Checks if the given identifier is one of the identifier of this result."""
        return id==self.id1 or id==self.id2

    def setIdStringLength(self, id1StringLength, id2StringLength):
        """Set the string length of the identifier strings. Important for Visualization."""
        self.id1StringLength = id1StringLength
        self.id2StringLength = id2StringLength

    def getIdStringLength(self):
        """Get the string length of the identifier strings as a List[id1strlength, id2strlenght].
            Important for Visualization.
        """
        return [self.id1StringLength, self.id2StringLength]

    def setSuspectedPlagiarism(self, value):
        """set boolean value: True means there is plagiarism suspicion other False"""
        if type(value) != type(True):
            raise NoValidArgumentError
        self.suspectedPlagiarism = value

    def isSuspectPlagiarism(self):
        """Returns boolean value indicating if there is plagiarism suspcicion."""
        return self.suspectedPlagiarism

    def setAlgorithmName(self, algName):
        """Sets the algorithm id used for the comparison."""
        self.algName = algName

    def getAlgorithmName(self):
        """Gets the algorithm id used for the comparison."""
        return self.algName

    def setNormalizerName(self, normName):
        """Sets the normalizer id used for the comparison."""
        self.normName = normName

    def getNormalizerName(self):
        """Gets the normalizer id used for the comparison."""
        return self.normName

#===============================================================================
#    Comparison
#===============================================================================
    def __eq__(self, other):
        """Method to compare if this object is equal to another one:  this == other"""
        if other == None:
            return False
        elif (set(self.getIdentifier()) == set(other.getIdentifier())
            and self.getSimilarity() == other.getSimilarity()
            and set(self.getTiles()) == set(other.getTiles())
            and set(self.getIdStringLength()) == set(other.getIdStringLength())):
            return True

        return False

    def __ne__(self, other):
        """Method to compare if this object ist NOT equal with another object: this != other"""
        return not self.__eq__(other)

#===============================================================================
#    String Representation
#===============================================================================
    def __str__(self):
        """Returns the informal string representation of this PlagResult object."""
        return ('PlagResult:\n'
                + ' Identifier: ' + str(self.getIdentifier()) + '\n'
                + ' Similarity: ' + str(self.getSimilarity()) + '\n'
                + ' Tiles: ' + str(self.getTiles()) + '\n'
                + ' supected Plagiarism: ' + str(self.isSuspectPlagiarism()) + '\n')

    def __repr__(self):
        """Returns the form string representation of this PlagResult object."""
        return "%s %s %s %s" %(str(self.getIdentifier()), str(self.getSimilarity()),
                str(self.getTiles()), str(self.isSuspectPlagiarism()))
