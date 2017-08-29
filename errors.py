
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
#This Module holds every Exception used in this library.
#===============================================================================

class PlagDetectorError(Exception): pass

class OutOfRangeError(PlagDetectorError): pass

class NoValidArgumentError(PlagDetectorError): pass

#Errors raised when nor valid, i.e. existing, normalizer
#or algorithm name is used.
class NoValidNameError(PlagDetectorError):

    def __init__(self, wrongName, availableNamesList):
        self.wrongName = str(wrongName)
        self.availableNames = str(availableNamesList)

    def __str__(self):
        print ("The used name " + self.wrongName + " is not defined.\n" \
             + "Following name ids are legal to use:\n" + self.availableNames)

class NoValidNormalizerNameError(NoValidNameError): pass
class NoValidAlgorithmNameError(NoValidNameError): pass

#Error raised when no identifier was set (used in PlagResult)
class NoIdentifierSetError(PlagDetectorError): pass

