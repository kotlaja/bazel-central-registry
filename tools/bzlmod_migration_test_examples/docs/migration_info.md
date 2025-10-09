# Migration info
Command for local testing:
```
bazel build --enable_bzlmod --noenable_workspace //...
```
## Direct dependencies:
* rules_java
* bazel_gazelle
* io_bazel_rules_go
* my_python_deps
* rules_python
* org_golang_x_net
* px_deps
## Migration of `rules_java`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository rules_java instantiated at:
  /DEFAULT.WORKSPACE.SUFFIX:39:6: in <toplevel>
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "rules_java",
  urls = [
    "https://github.com/bazelbuild/rules_java/releases/download/7.6.1/rules_java-7.6.1.tar.gz"
  ],
  sha256 = "f8ae9ed3887df02f40de9f4f7ac3873e6dd7a471f9cddf63952538b94b59aeb3",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found perfect name match in BCR: `rules_java`

It has been introduced as a Bazel module:

	bazel_dep(name = "rules_java", version = "8.15.2")
## Migration of `bazel_gazelle`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository bazel_gazelle instantiated at:
  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:17:13: in <toplevel>
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "bazel_gazelle",
  urls = [
    "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.37.0/bazel-gazelle-v0.37.0.tar.gz",
    "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.37.0/bazel-gazelle-v0.37.0.tar.gz"
  ],
  integrity = "sha256-12v3pg/YsFBEQJDfooN6Tq+YKeEWVhjuNdzspcvfWNU=",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found partially name matches in BCR: `gazelle`

It has been introduced as a Bazel module:

	bazel_dep(name = "gazelle", version = "0.45.0", repo_name = "bazel_gazelle")
## Migration of `io_bazel_rules_go`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository io_bazel_rules_go instantiated at:
  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:8:13: in <toplevel>
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "io_bazel_rules_go",
  urls = [
    "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.48.0/rules_go-v0.48.0.zip",
    "https://github.com/bazelbuild/rules_go/releases/download/v0.48.0/rules_go-v0.48.0.zip"
  ],
  integrity = "sha256-M6zErg9wUC20uJPJ/B3Xqb+ZjCPn/yxFF3QdQEmpdvg=",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found partially name matches in BCR: `rules_go`

It has been introduced as a Bazel module:

	bazel_dep(name = "rules_go", version = "0.57.0", repo_name = "io_bazel_rules_go")
## Migration of `rules_python`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository rules_python instantiated at:
  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:44:13: in <toplevel>
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "rules_python",
  url = "https://github.com/bazelbuild/rules_python/releases/download/1.4.0/rules_python-1.4.0.tar.gz",
  integrity = "sha256-qDdnnxOC8mlowe5vg5x9r5B5qlMSgGmh8oFd7KpjcwQ=",
  strip_prefix = "rules_python-1.4.0",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found perfect name match in BCR: `rules_python`

Found partially name matches in BCR: `rules_python_gazelle_plugin`

It has been introduced as a Bazel module:

	bazel_dep(name = "rules_python", version = "1.6.1")
## Migration of `my_python_deps`
It has been introduced as a python extension:

```
pip.parse(
    hub_name = "my_python_deps",
    requirements_lock = "//:requirements_lock.txt",
    python_version = "3.11",
)
use_repo(pip, "my_python_deps")

python = use_extension("@rules_python//python/extensions:python.bzl", "python")
python.defaults(python_version = "3.11")
python.toolchain(python_version = "3.11")
```
## Migration of `rules_python`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository rules_python instantiated at:
  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:44:13: in <toplevel>
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "rules_python",
  url = "https://github.com/bazelbuild/rules_python/releases/download/1.4.0/rules_python-1.4.0.tar.gz",
  integrity = "sha256-qDdnnxOC8mlowe5vg5x9r5B5qlMSgGmh8oFd7KpjcwQ=",
  strip_prefix = "rules_python-1.4.0",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found perfect name match in BCR: `rules_python`

Found partially name matches in BCR: `rules_python_gazelle_plugin`

This module has already been added inside the MODULE.bazel file
## Migration of `org_golang_x_net`:
It has been introduced as a go module with the help of `go.mod`:

```
go_deps.from_file(go_mod = "//:go.mod")
go_sdk.from_file(go_mod = "//:go.mod")
```
Additionally, `gazelle_override` was used for the initial directives:

```
go_deps.gazelle_override(
    path = "golang.org/x/net",
    directives = [
        "gazelle:proto disable",
         "gazelle:go_naming_convention import",
    ],
)
```
## Migration of `rules_jvm_external`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository rules_jvm_external instantiated at:
  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:72:13: in <toplevel>
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "rules_jvm_external",
  urls = [
    "https://github.com/bazelbuild/rules_jvm_external/archive/refs/tags/4.3.tar.gz"
  ],
  sha256 = "23fe83890a77ac1a3ee143e2306ec12da4a845285b14ea13cb0df1b1e23658fe",
  strip_prefix = "rules_jvm_external-4.3",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found perfect name match in BCR: `rules_jvm_external`

It has been introduced as a Bazel module:

	bazel_dep(name = "rules_jvm_external", version = "6.8")
## Migration of `org.antlr` (px_deps):
It has been introduced as a maven artifact:

```
maven.artifact(
    name = "px_deps",
    group = "org.antlr",
    artifact = "antlr4",
    version = "4.11.1"
)
```
## Migration of `rules_shell`:

<details>
<summary>Click here to see where and how the repo was declared in the WORKSPACE file</summary>

#### Location
```python
Repository rules_shell instantiated at:
  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:105:13: in <toplevel>
Repository rule http_archive defined at:
  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>

```

#### Definition
```python
load("@@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
  name = "rules_shell",
  url = "https://github.com/bazelbuild/rules_shell/releases/download/v0.4.0/rules_shell-v0.4.0.tar.gz",
  sha256 = "3e114424a5c7e4fd43e0133cc6ecdfe54e45ae8affa14fadd839f29901424043",
  strip_prefix = "rules_shell-0.4.0",
)
```
**Tip**: URLs usually show which version was used.
</details>

___
Found perfect name match in BCR: `rules_shell`

It has been introduced as a Bazel module:

	bazel_dep(name = "rules_shell", version = "0.6.1")
