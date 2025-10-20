"""Repo rule and macro used for testing"""

def _test_repo_rule_impl(repository_ctx):
    repository_ctx.file(
        "BUILD",
        content = """
genrule(
    name = "macro_extension",
    outs = ["rule_name.out"],
    cmd = "touch $@",
    visibility = ["//visibility:public"],
)
"""
    )

_test_repo_rule = repository_rule(
    implementation = _test_repo_rule_impl,
)

def macro_module_extension(name):
    _test_repo_rule(name = name)
