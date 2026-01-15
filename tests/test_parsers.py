# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

@pytest.mark.parametrize(
        "FASTA_parser, passfail", 
        [
        (FastaParser("data/test.fa"), "pass"), 
        (FastaParser("tests/bad.fa"), "fail"), 
        (FastaParser("tests/blank.fa"), "fail"),
        ]
    )
def test_FastaParser(FASTA_parser, passfail):
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    if passfail == "pass":
        records = list(FASTA_parser)
        assert records is not None
        assert len(records) > 0
    
        header, sequence = records[0]
        assert isinstance(header, str)
        assert len(header) > 0
        assert isinstance(sequence, str)
        assert len(sequence) > 0
    else:
        with pytest.raises((ValueError, AssertionError)):
            records = list(FASTA_parser)
            assert records is not None
            assert len(records) > 0
            
            header, sequence = records[0]
            assert isinstance(header, str)
            assert len(header) > 0
            assert isinstance(sequence, str)
            assert len(sequence) > 0

@pytest.mark.parametrize(
        "FASTA_format, passfail", 
        [
            (FastaParser("data/test.fa"), "pass"), 
            (FastaParser("data/test.fq"), "fail"),
            ]
    )
def test_FastaFormat(FASTA_format, passfail):
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    if passfail == "pass":
        records = list(FASTA_format)
        assert records[0][0] is not None
    else:
        with pytest.raises((ValueError, AssertionError)):
            records = list(FASTA_format)
            assert records[0][0] is not None

@pytest.mark.parametrize(
        "FASTQ_parser, passfail", 
        [
        (FastqParser("data/test.fq"), "pass"), 
        (FastqParser("tests/bad.fq"), "fail"), 
        (FastqParser("tests/blank.fq"), "fail"),
        ]
    )
def test_FastqParser(FASTQ_parser, passfail):
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    if passfail == "pass":
        records = list(FASTQ_parser)
        assert records is not None
        assert len(records) > 0

        header, sequence, quality = records[0]
        assert isinstance(header, str)
        assert len(header) > 0
        assert isinstance(sequence, str)
        assert len(sequence) > 0
        assert isinstance(quality, str)
        assert len(quality) > 0

        assert len(sequence) == len(quality)
    else:
        with pytest.raises((ValueError, AssertionError)):
            records = list(FASTQ_parser)
            assert records is not None
            assert len(records) > 0

            header, sequence, quality = records[0]
            assert isinstance(header, str)
            assert len(header) > 0
            assert isinstance(sequence, str)
            assert len(sequence) > 0
            assert isinstance(quality, str)
            assert len(quality) > 0

            assert len(sequence) == len(quality)

@pytest.mark.parametrize(
        "FASTQ_format, passfail", 
        [
            (FastqParser("data/test.fa"), "fail"), 
            (FastqParser("data/test.fq"), "pass"),
            ]
    )
def test_FastqFormat(FASTQ_format, passfail):
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    
    if passfail == "pass":
        records = list(FASTQ_format)
        assert records[0][0] is not None
    else:
        with pytest.raises((ValueError, AssertionError)):
            records = list(FASTQ_format)
            assert records[0][0] is not None