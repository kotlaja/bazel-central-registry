load("//:macro_module_extension.bzl", "macro_module_extension")
# -- load statements -- #

def _extension_for_macro_module_extension_impl(ctx):
  macro_module_extension(
    name = "macro_extension",
  )
# -- repo definitions -- #

extension_for_macro_module_extension = module_extension(implementation = _extension_for_macro_module_extension_impl)
