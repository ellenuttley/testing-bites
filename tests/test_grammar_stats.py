from lib.grammar_stats import *

def test_grammer_stats_functional():
    grammar_stats = GrammarStats()
    assert(grammar_stats)

def test_grammer_stats_check_return_bool():
    grammar_stats = GrammarStats()
    assert type(grammar_stats.check('text')) == bool

def test_grammer_stats_check_true_if_valid():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Text.') == True

def test_grammar_stats_check_false_if_invalid():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Text') == False

def test_grammar_stats_percentage_good_returns_int():
    grammar_stats = GrammarStats()
    grammar_stats.check('Text')
    assert type(grammar_stats.percentage_good()) == int

def test_grammar_stats_percentage_good_accurate():
    grammar_stats = GrammarStats()
    grammar_stats.check('Text')
    grammar_stats.check('Text.')
    assert grammar_stats.percentage_good() == 50
