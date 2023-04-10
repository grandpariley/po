from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem


def default_variables():
    return {
        "0": Variable(DiscreteDomain([0, 1, 2, 3, 4, 5], 0), []),
        "1": Variable(DiscreteDomain([0, 1, 2, 3, 4, 5], 0), []),
        "2": Variable(DiscreteDomain([0, 1, 2, 3, 4, 5], 0), []),
    }


def default_consistent_problem():
    return Problem(
        default_variables(),
        [
            Constraint(("0", "1"), lambda v: v["0"].get_value() != v["1"].get_value()),
            Constraint(tuple(["2"]), lambda v: v["2"].get_value() > 0),
        ],
        [lambda v: v["0"].get_value(), lambda v: v["1"].get_value(), lambda v: v["2"].get_value()]
    )


def default_consistent_problem_set_values():
    problem = default_consistent_problem()
    problem.set_value("0", 2)
    problem.set_value("1", 1)
    problem.set_value("2", 2)
    return problem


def default_inconsistent_problem():
    return Problem(
        default_variables(),
        [
            Constraint(("0", "2"), lambda v: False),
        ],
        [lambda v: v["0"].get_value(), lambda v: v["1"].get_value(), lambda v: v["2"].get_value()]
    )


def default_inconsistent_problem_set_values():
    problem = default_inconsistent_problem()
    problem.set_value("0", 2)
    problem.set_value("1", 1)
    problem.set_value("2", 2)
    return problem


def default_multi_objective_problem():
    return Problem(
        default_variables(),
        [
            Constraint(("0", "2"), lambda v: v["0"] == v["1"]),
            Constraint(tuple(["1"]), lambda v: v["0"] == "1"),
            Constraint(tuple(["2"]), lambda v: v["0"] > 0)
        ],
        [lambda v: sum([v[var].get_value() for var in v]), lambda v: -sum(v[var].get_value() for var in v)]
    )


def default_multi_objective_problem_set_values():
    problem = default_multi_objective_problem()
    problem.set_value("0", 2)
    problem.set_value("1", 1)
    problem.set_value("2", 2)
    return problem


def get_test_data():
    return {
        "0": {},
        "1": {},
        "2": {}
    }
