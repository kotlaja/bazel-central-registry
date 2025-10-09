load("@io_bazel_rules_go//go:def.bzl", "go_binary")
load("@bazel_gazelle//:def.bzl", "gazelle")
load("@rules_python//python:py_binary.bzl", "py_binary")
load("@rules_java//java:defs.bzl", "java_binary")
load("@rules_shell//shell:sh_library.bzl", "sh_library")

# Go
gazelle(name = "gazelle")
go_binary(
    name = "go_bin",
    srcs = ["test.go"],
    deps = [
        "@org_golang_x_net//context",
    ]
)

# Python
py_binary(
    name = "py_bin",
    srcs = ["py_bin.py"],
    deps = [
        "@my_python_deps//numpy",
    ],
    toolchains = [
        "@rules_python//python:current_py_toolchain",
    ]
)

# Maven
java_binary(
    name = "px_deps_bin",
    main_class = "org.antlr.v4.Tool",
    runtime_deps = [
        "@px_deps//:org_antlr_antlr4",
    ],
)

sh_library(name='sh_lib')