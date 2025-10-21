"""Repo rule and macro used for testing"""

def _test_repo_rule_impl(repository_ctx):
    repository_ctx.file(
        "BUILD",
        content = """
genrule(
    name = "foo",
    outs = ["rule_name.out"],
    cmd = "touch $@",
    visibility = ["//visibility:public"],
)
"""
    )

_test_repo_rule = repository_rule(
    implementation = _test_repo_rule_impl,
)

def my_custom_macro(name):
    _test_repo_rule(name = name)
