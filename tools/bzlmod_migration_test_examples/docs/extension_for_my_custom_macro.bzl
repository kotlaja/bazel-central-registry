load("//:macro_module_extension.bzl", "my_custom_macro")
# -- load statements -- #

def _extension_for_my_custom_macro_impl(ctx):
  my_custom_macro(
    name = "my_custom_repo",
  )
# -- repo definitions -- #

extension_for_my_custom_macro = module_extension(implementation = _extension_for_my_custom_macro_impl)
