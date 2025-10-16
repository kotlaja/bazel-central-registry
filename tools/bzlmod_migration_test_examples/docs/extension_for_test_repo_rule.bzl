load("//:test_repo_rule.bzl", "test_repo_rule")
# -- load statements -- #

def _extension_for_test_repo_rule_impl(ctx):
  _test_repo_rule(
    name = "macro_rule",
  )
# -- repo definitions -- #

extension_for_test_repo_rule = module_extension(implementation = _extension_for_test_repo_rule_impl)
