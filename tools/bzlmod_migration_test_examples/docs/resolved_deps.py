resolved = [
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository io_bazel_rules_go instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:24:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_go",
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.48.0/rules_go-v0.48.0.zip",
                    "https://github.com/bazelbuild/rules_go/releases/download/v0.48.0/rules_go-v0.48.0.zip"
               ],
               "integrity": "sha256-M6zErg9wUC20uJPJ/B3Xqb+ZjCPn/yxFF3QdQEmpdvg="
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.48.0/rules_go-v0.48.0.zip",
                              "https://github.com/bazelbuild/rules_go/releases/download/v0.48.0/rules_go-v0.48.0.zip"
                         ],
                         "sha256": "",
                         "integrity": "sha256-M6zErg9wUC20uJPJ/B3Xqb+ZjCPn/yxFF3QdQEmpdvg=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "io_bazel_rules_go"
                    },
                    "output_tree_hash": "e10092760ab420659655a16e23306a287501b46c7bb650eaac9e8ab581377a16"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_gazelle instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:33:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle",
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.37.0/bazel-gazelle-v0.37.0.tar.gz",
                    "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.37.0/bazel-gazelle-v0.37.0.tar.gz"
               ],
               "integrity": "sha256-12v3pg/YsFBEQJDfooN6Tq+YKeEWVhjuNdzspcvfWNU="
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.37.0/bazel-gazelle-v0.37.0.tar.gz",
                              "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.37.0/bazel-gazelle-v0.37.0.tar.gz"
                         ],
                         "sha256": "",
                         "integrity": "sha256-12v3pg/YsFBEQJDfooN6Tq+YKeEWVhjuNdzspcvfWNU=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_gazelle"
                    },
                    "output_tree_hash": "00e93f33d43bce4dc8c10271e1e2f306b2d3391e1df6b5d14b0d5cc26e1d407c"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_python instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:60:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python",
               "url": "https://github.com/bazelbuild/rules_python/releases/download/1.0.0/rules_python-1.0.0.tar.gz",
               "sha256": "4f7e2aa1eb9aa722d96498f5ef514f426c1f55161c3c9ae628c857a7128ceb07",
               "strip_prefix": "rules_python-1.0.0"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_python/releases/download/1.0.0/rules_python-1.0.0.tar.gz",
                         "urls": [],
                         "sha256": "4f7e2aa1eb9aa722d96498f5ef514f426c1f55161c3c9ae628c857a7128ceb07",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_python-1.0.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_python"
                    },
                    "output_tree_hash": "85131bf036ba70d6924aa5936c73dc26d7d04e5229ffde2acf2a3af832853c9a"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:internal_config_repo.bzl%internal_config_repo",
          "definition_information": "Repository rules_python_internal instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:33:10: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule internal_config_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/internal_config_repo.bzl:108:39: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python_internal",
               "generator_name": "rules_python_internal",
               "generator_function": "py_repositories",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:internal_config_repo.bzl%internal_config_repo",
                    "attributes": {
                         "name": "rules_python_internal",
                         "generator_name": "rules_python_internal",
                         "generator_function": "py_repositories",
                         "generator_location": None
                    },
                    "output_tree_hash": "ffdec66b8b1e449fdc8b40bddcaf5d49bd385780897d6486833127a21203f617"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:45:22: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/repositories.bzl:51:12: in go_rules_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/repositories.bzl:295:18: in _maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib",
               "generator_name": "bazel_skylib",
               "generator_function": "go_rules_dependencies",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.6.1/bazel-skylib-1.6.1.tar.gz",
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.6.1/bazel-skylib-1.6.1.tar.gz"
               ],
               "sha256": "9f38886a40548c6e96c106b752f242130ee11aaa068a56ba7e56f4511f33e4f2",
               "strip_prefix": ""
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.6.1/bazel-skylib-1.6.1.tar.gz",
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.6.1/bazel-skylib-1.6.1.tar.gz"
                         ],
                         "sha256": "9f38886a40548c6e96c106b752f242130ee11aaa068a56ba7e56f4511f33e4f2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_skylib"
                    },
                    "output_tree_hash": "fae930d1d51ea9a75f1f3ab3edc23892f9095ffb78b1f598b5db7563053b899d"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:6:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc",
               "urls": [
                    "https://github.com/bazelbuild/rules_cc/releases/download/0.1.5/rules_cc-0.1.5.tar.gz"
               ],
               "sha256": "b8b918a85f9144c01f6cfe0f45e4f2838c7413961a8ff23bc0c6cdf8bb07a3b6",
               "strip_prefix": "rules_cc-0.1.5"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_cc/releases/download/0.1.5/rules_cc-0.1.5.tar.gz"
                         ],
                         "sha256": "b8b918a85f9144c01f6cfe0f45e4f2838c7413961a8ff23bc0c6cdf8bb07a3b6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_cc-0.1.5",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cc"
                    },
                    "output_tree_hash": "fd71c837eb8b0ab01fcd166d4306fa55acda17d2ac9641f21de1743bcad104b8"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private/pypi:pip_repository.bzl%pip_repository",
          "definition_information": "Repository my_python_deps instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:71:10: in <toplevel>\nRepository rule pip_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/pip_repository.bzl:223:33: in <toplevel>\n",
          "original_attributes": {
               "name": "my_python_deps",
               "requirements_lock": "//:requirements_lock.txt"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private/pypi:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "my_python_deps",
                         "requirements_lock": "//:requirements_lock.txt"
                    },
                    "output_tree_hash": "d05dfaf77021d6ab15adf9d6b5799d9637cec090e2b5510217bff749a30e51f4"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_jvm_external instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:91:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_jvm_external",
               "url": "https://github.com/bazelbuild/rules_jvm_external/archive/4.5.zip",
               "sha256": "b17d7388feb9bfa7f2fa09031b32707df529f26c91ab9e5d909eb1676badd9a6",
               "strip_prefix": "rules_jvm_external-4.5"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_jvm_external/archive/4.5.zip",
                         "urls": [],
                         "sha256": "b17d7388feb9bfa7f2fa09031b32707df529f26c91ab9e5d909eb1676badd9a6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_jvm_external-4.5",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_jvm_external"
                    },
                    "output_tree_hash": "528bdc67a3f162074bf5b2fb4eb594250bb850d2262e1eff1036393ca2ef6cee"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_jvm_external//:coursier.bzl%pinned_coursier_fetch",
          "definition_information": "Repository rules_jvm_external_deps instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:99:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_jvm_external/repositories.bzl:23:18: in rules_jvm_external_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_jvm_external/private/rules/maven_install.bzl:137:30: in maven_install\nRepository rule pinned_coursier_fetch defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_jvm_external/coursier.bzl:1261:40: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_jvm_external_deps",
               "generator_name": "rules_jvm_external_deps",
               "generator_function": "rules_jvm_external_deps",
               "generator_location": None,
               "repositories": [
                    "{ \"repo_url\": \"https://repo1.maven.org/maven2\" }",
                    "{ \"repo_url\": \"https://maven.google.com\" }"
               ],
               "artifacts": [
                    "{ \"group\": \"com.google.auth\", \"artifact\": \"google-auth-library-credentials\", \"version\": \"0.22.0\" }",
                    "{ \"group\": \"com.google.auth\", \"artifact\": \"google-auth-library-oauth2-http\", \"version\": \"0.22.0\" }",
                    "{ \"group\": \"com.google.cloud\", \"artifact\": \"google-cloud-core\", \"version\": \"1.93.10\" }",
                    "{ \"group\": \"com.google.cloud\", \"artifact\": \"google-cloud-storage\", \"version\": \"1.113.4\" }",
                    "{ \"group\": \"com.google.code.gson\", \"artifact\": \"gson\", \"version\": \"2.9.0\" }",
                    "{ \"group\": \"org.apache.maven\", \"artifact\": \"maven-artifact\", \"version\": \"3.8.6\" }",
                    "{ \"group\": \"software.amazon.awssdk\", \"artifact\": \"s3\", \"version\": \"2.17.183\" }"
               ],
               "fetch_sources": False,
               "fetch_javadoc": False,
               "generate_compat_repositories": False,
               "maven_install_json": "@@rules_jvm_external//:rules_jvm_external_deps_install.json",
               "override_targets": {},
               "strict_visibility": True,
               "strict_visibility_value": [
                    "//visibility:private"
               ],
               "jetify": False,
               "jetify_include_list": [
                    "*"
               ],
               "additional_netrc_lines": [],
               "use_credentials_from_home_netrc_file": False,
               "fail_if_repin_required": True,
               "use_starlark_android_rules": False,
               "aar_import_bzl_label": "@build_bazel_rules_android//android:rules.bzl",
               "duplicate_version_warning": "warn"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_jvm_external//:coursier.bzl%pinned_coursier_fetch",
                    "attributes": {
                         "name": "rules_jvm_external_deps",
                         "generator_name": "rules_jvm_external_deps",
                         "generator_function": "rules_jvm_external_deps",
                         "generator_location": None,
                         "repositories": [
                              "{ \"repo_url\": \"https://repo1.maven.org/maven2\" }",
                              "{ \"repo_url\": \"https://maven.google.com\" }"
                         ],
                         "artifacts": [
                              "{ \"group\": \"com.google.auth\", \"artifact\": \"google-auth-library-credentials\", \"version\": \"0.22.0\" }",
                              "{ \"group\": \"com.google.auth\", \"artifact\": \"google-auth-library-oauth2-http\", \"version\": \"0.22.0\" }",
                              "{ \"group\": \"com.google.cloud\", \"artifact\": \"google-cloud-core\", \"version\": \"1.93.10\" }",
                              "{ \"group\": \"com.google.cloud\", \"artifact\": \"google-cloud-storage\", \"version\": \"1.113.4\" }",
                              "{ \"group\": \"com.google.code.gson\", \"artifact\": \"gson\", \"version\": \"2.9.0\" }",
                              "{ \"group\": \"org.apache.maven\", \"artifact\": \"maven-artifact\", \"version\": \"3.8.6\" }",
                              "{ \"group\": \"software.amazon.awssdk\", \"artifact\": \"s3\", \"version\": \"2.17.183\" }"
                         ],
                         "fetch_sources": False,
                         "fetch_javadoc": False,
                         "generate_compat_repositories": False,
                         "maven_install_json": "@@rules_jvm_external//:rules_jvm_external_deps_install.json",
                         "override_targets": {},
                         "strict_visibility": True,
                         "strict_visibility_value": [
                              "//visibility:private"
                         ],
                         "jetify": False,
                         "jetify_include_list": [
                              "*"
                         ],
                         "additional_netrc_lines": [],
                         "use_credentials_from_home_netrc_file": False,
                         "fail_if_repin_required": True,
                         "use_starlark_android_rules": False,
                         "aar_import_bzl_label": "@build_bazel_rules_android//android:rules.bzl",
                         "duplicate_version_warning": "warn"
                    },
                    "output_tree_hash": "96ce09b29a4e2fdf712d15fac81484720435eb3c480dd9cf2f2a624e69a301b7"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository rules_java_builtin instantiated at:\n  /DEFAULT.WORKSPACE:12:36: in <toplevel>\nRepository rule local_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java_builtin",
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/rules_java"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "rules_java_builtin",
                         "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/rules_java"
                    },
                    "output_tree_hash": "1ca569c961d1b83e6e2919e062955f682718aa999453062d166332b728ac03c3"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository internal_platforms_do_not_use instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:153:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule local_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "internal_platforms_do_not_use",
               "generator_name": "internal_platforms_do_not_use",
               "generator_function": "maybe",
               "generator_location": None,
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/platforms"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "internal_platforms_do_not_use",
                         "generator_name": "internal_platforms_do_not_use",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/platforms"
                    },
                    "output_tree_hash": "2c5a81204fc3389153b58f72597bfa776024257949d3110df00c8a1ac5b8a961"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_gazelle//internal:is_bazel_module.bzl%is_bazel_module",
          "definition_information": "Repository bazel_gazelle_is_bazel_module instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:47:21: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/deps.bzl:92:20: in gazelle_dependencies\nRepository rule is_bazel_module defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/internal/is_bazel_module.bzl:30:34: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_is_bazel_module",
               "generator_name": "bazel_gazelle_is_bazel_module",
               "generator_function": "gazelle_dependencies",
               "generator_location": None,
               "is_bazel_module": False
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_gazelle//internal:is_bazel_module.bzl%is_bazel_module",
                    "attributes": {
                         "name": "bazel_gazelle_is_bazel_module",
                         "generator_name": "bazel_gazelle_is_bazel_module",
                         "generator_function": "gazelle_dependencies",
                         "generator_location": None,
                         "is_bazel_module": False
                    },
                    "output_tree_hash": "dda7e5d5aa9d766c3d9c95f78a31564192edad9cc7e5448bcaeb039f33b87c8f"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_java instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:39:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java",
               "generator_name": "rules_java",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_java/releases/download/7.6.1/rules_java-7.6.1.tar.gz"
               ],
               "sha256": "f8ae9ed3887df02f40de9f4f7ac3873e6dd7a471f9cddf63952538b94b59aeb3"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_java/releases/download/7.6.1/rules_java-7.6.1.tar.gz"
                         ],
                         "sha256": "f8ae9ed3887df02f40de9f4f7ac3873e6dd7a471f9cddf63952538b94b59aeb3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_java"
                    },
                    "output_tree_hash": "409cd75d3f9f0685a28e3085e19bf79e19ba3b26c7eb73e8319d756ee1981a3a"
               }
          ]
     },
     {
          "original_rule_class": "@@io_bazel_rules_go//go/private:nogo.bzl%go_register_nogo",
          "definition_information": "Repository io_bazel_rules_nogo instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:45:22: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/repositories.bzl:282:12: in go_rules_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/repositories.bzl:295:18: in _maybe\nRepository rule go_register_nogo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/nogo.bzl:54:35: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_nogo",
               "generator_name": "io_bazel_rules_nogo",
               "generator_function": "go_rules_dependencies",
               "generator_location": None,
               "nogo": "@io_bazel_rules_go//:default_nogo"
          },
          "repositories": [
               {
                    "rule_class": "@@io_bazel_rules_go//go/private:nogo.bzl%go_register_nogo",
                    "attributes": {
                         "name": "io_bazel_rules_nogo",
                         "generator_name": "io_bazel_rules_nogo",
                         "generator_function": "go_rules_dependencies",
                         "generator_location": None,
                         "nogo": "@io_bazel_rules_go//:default_nogo"
                    },
                    "output_tree_hash": "b414d771116ea38248c456980d0530fe9f067be3b2788ab130fe8d828a181379"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_shell instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:14:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_shell",
               "url": "https://github.com/bazelbuild/rules_shell/releases/download/v0.4.0/rules_shell-v0.4.0.tar.gz",
               "sha256": "3e114424a5c7e4fd43e0133cc6ecdfe54e45ae8affa14fadd839f29901424043",
               "strip_prefix": "rules_shell-0.4.0"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_shell/releases/download/v0.4.0/rules_shell-v0.4.0.tar.gz",
                         "urls": [],
                         "sha256": "3e114424a5c7e4fd43e0133cc6ecdfe54e45ae8affa14fadd839f29901424043",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_shell-0.4.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_shell"
                    },
                    "output_tree_hash": "fa5d60b448608536b6d898c19421fcbc6b64754e59148764ee44d662f04864ef"
               }
          ]
     },
     {
          "original_rule_class": "@@io_bazel_rules_go//go/private:polyfill_bazel_features.bzl%polyfill_bazel_features",
          "definition_information": "Repository io_bazel_rules_go_bazel_features instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:45:22: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/repositories.bzl:288:11: in go_rules_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/repositories.bzl:295:18: in _maybe\nRepository rule polyfill_bazel_features defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/polyfill_bazel_features.bzl:38:42: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_go_bazel_features",
               "generator_name": "io_bazel_rules_go_bazel_features",
               "generator_function": "go_rules_dependencies",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@io_bazel_rules_go//go/private:polyfill_bazel_features.bzl%polyfill_bazel_features",
                    "attributes": {
                         "name": "io_bazel_rules_go_bazel_features",
                         "generator_name": "io_bazel_rules_go_bazel_features",
                         "generator_function": "go_rules_dependencies",
                         "generator_location": None
                    },
                    "output_tree_hash": "d2aedf1dbc666769a8f1876777f10eaeeda4289edf0895a2a42938d6a7a6443d"
               }
          ]
     },
     {
          "original_rule_class": "@@internal_platforms_do_not_use//host:extension.bzl%host_platform_repo",
          "definition_information": "Repository host_platform instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:165:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule host_platform_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/internal_platforms_do_not_use/host/extension.bzl:51:37: in <toplevel>\n",
          "original_attributes": {
               "name": "host_platform",
               "generator_name": "host_platform",
               "generator_function": "maybe",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@internal_platforms_do_not_use//host:extension.bzl%host_platform_repo",
                    "attributes": {
                         "name": "host_platform",
                         "generator_name": "host_platform",
                         "generator_function": "maybe",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bb7732a410e479305fb8602fbfbe14a04e932eed9f8384852c03def646e87d5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository platforms instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:147:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule local_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "platforms",
               "generator_name": "platforms",
               "generator_function": "maybe",
               "generator_location": None,
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/platforms"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "platforms",
                         "generator_name": "platforms",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/f2a59e3870432ed89c73c37a0498bd05/platforms"
                    },
                    "output_tree_hash": "2c5a81204fc3389153b58f72597bfa776024257949d3110df00c8a1ac5b8a961"
               }
          ]
     },
     {
          "original_rule_class": "//:macro_module_extension.bzl%_test_repo_rule",
          "definition_information": "Repository my_custom_repo instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:114:16: in <toplevel>\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/macro_module_extension.bzl:21:20: in my_custom_macro\nRepository rule _test_repo_rule defined at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/macro_module_extension.bzl:16:34: in <toplevel>\n",
          "original_attributes": {
               "name": "my_custom_repo",
               "generator_name": "my_custom_repo",
               "generator_function": "my_custom_macro",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "//:macro_module_extension.bzl%_test_repo_rule",
                    "attributes": {
                         "name": "my_custom_repo",
                         "generator_name": "my_custom_repo",
                         "generator_function": "my_custom_macro",
                         "generator_location": None
                    },
                    "output_tree_hash": "baae4f277b35b485b4f928e28b689461ec0bea6b8d56d1e8a462b1b707831525"
               }
          ]
     },
     {
          "original_rule_class": "@@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository go_sdk_toolchains instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:46:23: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:725:28: in go_register_toolchains\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:319:19: in go_download_sdk\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:307:27: in _go_toolchains\nRepository rule go_multiple_toolchains defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:294:41: in <toplevel>\n",
          "original_attributes": {
               "name": "go_sdk_toolchains",
               "generator_name": "go_sdk_toolchains",
               "generator_function": "go_register_toolchains",
               "generator_location": None,
               "prefixes": [
                    ""
               ],
               "sdk_repos": [
                    "go_sdk"
               ],
               "sdk_types": [
                    "remote"
               ],
               "sdk_versions": [
                    "1.23.1"
               ],
               "geese": [
                    ""
               ],
               "goarchs": [
                    ""
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "go_sdk_toolchains",
                         "generator_name": "go_sdk_toolchains",
                         "generator_function": "go_register_toolchains",
                         "generator_location": None,
                         "prefixes": [
                              ""
                         ],
                         "sdk_repos": [
                              "go_sdk"
                         ],
                         "sdk_types": [
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.23.1"
                         ],
                         "geese": [
                              ""
                         ],
                         "goarchs": [
                              ""
                         ]
                    },
                    "output_tree_hash": "a3f341b234543b81645f525d8c43c3f4930225c4f53424ecf8ea63017bcbf278"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d0587a4ecc9323d5cf65314b2d284b520ffb5ee1d3231cc6601efa13dadcc0f4"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "45b3b36d22d3e614745e7a5e838351c32fe0eabb09a4a197bac0f4d416a950ce"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0a170bf4f31e6c4621aeb4d4ce4b75b808be2f3a63cb55dc8172c27707d299ab"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_macos_toolchain_config_repo",
               "generator_name": "remote_jdk8_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_macos_toolchain_config_repo",
                         "generator_name": "remote_jdk8_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "e0d82dc2dbe8ec49d859811afe4973ec36226875a39ac7fc8419e91e7e9c89fb"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "3272b586976beea589d09ea8029fd5d714da40127c8850e3480991c2440c5825"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "244e11245106a8495ac4744a90023b87008e3e553766ba11d47a9fe5b4bb408d"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "30b78e0951c37c2d7ae1318f83045ff42ef261dbb93c5b4fd3ba963e12cf68d6"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "86b129d9c464a9b08f97eca7d8bc5bdb3676b581f8aac044451dbdfaa49e69d3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c237bd9668de9b6437c452c020ea5bc717ff80b1a5ffd581adfdc7d4a6c5fe03"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f0f07fe0f645f2dc7b8c9953c7962627e1c7425cc52f543729dbff16cd20e461"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c9c795851cffbf2a808bfc7cccea597c3b3fef46cfefa084f7e9de7e90b65447"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
               "generator_name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4d721d8b0731cfb50f963f8b55c7bef9f572de0e2f251f07a12c722ef1acbb2f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_windows_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_windows_toolchain_config_repo",
               "generator_name": "remote_jdk8_windows_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_windows_toolchain_config_repo",
                         "generator_name": "remote_jdk8_windows_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8d0b08c18f215c185d64efe72054a5ffef36325906c34ebf1d3c710d4ba5c685"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb33021f243382d2fb849ec204c5c8be5083c37e081df71d34a84324687cf001"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:187:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bf5ba89669bcdf4526f821bc9f1f9f49409ae9c61c4e8f21c9f17e06c475127"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0eb17f6d969bc665a21e55d29eb51e88a067159ee62cf5094b17658a07d3accb"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository python_3_11_toolchains instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:80:27: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/python_register_toolchains.bzl:180:20: in python_register_toolchains\nRepository rule toolchains_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/toolchains_repo.bzl:113:34: in <toplevel>\n",
          "original_attributes": {
               "name": "python_3_11_toolchains",
               "generator_name": "python_3_11_toolchains",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "platforms": [
                    "aarch64-apple-darwin",
                    "aarch64-unknown-linux-gnu",
                    "ppc64le-unknown-linux-gnu",
                    "s390x-unknown-linux-gnu",
                    "x86_64-apple-darwin",
                    "x86_64-pc-windows-msvc",
                    "x86_64-unknown-linux-gnu",
                    "x86_64-unknown-linux-musl"
               ],
               "python_version": "3.11.10",
               "set_python_version_constraint": False,
               "user_repository_name": "python_3_11"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "python_3_11_toolchains",
                         "generator_name": "python_3_11_toolchains",
                         "generator_function": "python_register_toolchains",
                         "generator_location": None,
                         "platforms": [
                              "aarch64-apple-darwin",
                              "aarch64-unknown-linux-gnu",
                              "ppc64le-unknown-linux-gnu",
                              "s390x-unknown-linux-gnu",
                              "x86_64-apple-darwin",
                              "x86_64-pc-windows-msvc",
                              "x86_64-unknown-linux-gnu",
                              "x86_64-unknown-linux-musl"
                         ],
                         "python_version": "3.11.10",
                         "set_python_version_constraint": False,
                         "user_repository_name": "python_3_11"
                    },
                    "output_tree_hash": "618c6e5d2759a00381476f84d6d7d772edaecc4e23d18d638397f05050ef8371"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b169b01ac1a169d7eb5e3525454c3e408e9127993ac0f578dc2c5ad183fd4e3e"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_win_toolchain_config_repo",
               "generator_name": "remotejdk21_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_win_toolchain_config_repo",
                         "generator_name": "remotejdk21_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "87012328b07a779503deec0ef47132a0de50efd69afe7df87619bcc07b1dc4ed"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "41aa7b3317f8d9001746e908454760bf544ffaa058abe22f40711246608022ba"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "ca1d067909669aa58188026a7da06d43bdec74a3ba5c122af8a4c3660acd8d8f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bef508c068dd47d605f62c53ab0628f1f7f5101fdcc8ada09b2067b36c47931f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "170c3c9a35e502555dc9f04b345e064880acbf7df935f673154011356f4aad34"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_macos_toolchain_config_repo",
               "generator_name": "remotejdk21_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_macos_toolchain_config_repo",
                         "generator_name": "remotejdk21_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "434446eddb7f6a3dcc7a2a5330ed9ab26579c5142c19866b197475a695fbb32f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7886e497d586c3f3c8225685281b0940e9aa699af208dc98de3db8839e197be3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "6ba1870e09fccfdcd423f4169b966a73f8e9deaff859ec6fb3b626ed61ebd8b5"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk21_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk21_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9bbdbb329eeba27bc482582360abc6e3351d9a9a07ee11cba3a0026c90223e85"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "ee548ad054c9b75286ff3cd19792e433a2d1236378d3a0d8076fca0bb1a88e05"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b6a178fc0ca08a4473490f1c5d0f9f633db0ca0f2834c69dd08ce8290cf9ca86"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk21_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk21_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "706d910cc6809ea7f77fa4f938a4f019dd90d9dad927fb804a14b04321300a36"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_s390x_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_s390x_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f1e3f0b4884e21863a7c19a3a12a8995ed4162e02bd07cbb61b42799fc2d7359"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "fdc8ae00f2436bfc46b2f54c84f2bd84122787ede232a4d61ffc284bfe6f61ec"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:181:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/cpp/cc_configure.bzl:148:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/cpp/cc_configure.bzl:47:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "f95f3d84ac75b4a4d9817af803f1d998a755bd9c20c700c79fa82cb159e98cfc"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:85:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/local_java_repository.bzl:335:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/local_java_repository.bzl:290:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
               "java_home": "",
               "version": ""
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
                         "java_home": "",
                         "version": ""
                    },
                    "output_tree_hash": "7f6ef4ff2fc865665ea008a6be05f793fc7fa910a2673ec7f17c0595ba53d7e0"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:pythons_hub.bzl%hub_repo",
          "definition_information": "Repository pythons_hub instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:37:10: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule hub_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pythons_hub.bzl:145:27: in <toplevel>\n",
          "original_attributes": {
               "name": "pythons_hub",
               "generator_name": "pythons_hub",
               "generator_function": "py_repositories",
               "generator_location": None,
               "default_python_version": "",
               "minor_mapping": {
                    "3.8": "3.8.20",
                    "3.9": "3.9.20",
                    "3.10": "3.10.15",
                    "3.11": "3.11.10",
                    "3.12": "3.12.7",
                    "3.13": "3.13.0"
               },
               "python_versions": [
                    "3.10.11",
                    "3.10.12",
                    "3.10.13",
                    "3.10.14",
                    "3.10.15",
                    "3.10.2",
                    "3.10.4",
                    "3.10.6",
                    "3.10.8",
                    "3.10.9",
                    "3.11.1",
                    "3.11.10",
                    "3.11.3",
                    "3.11.4",
                    "3.11.5",
                    "3.11.6",
                    "3.11.7",
                    "3.11.8",
                    "3.11.9",
                    "3.12.0",
                    "3.12.1",
                    "3.12.2",
                    "3.12.3",
                    "3.12.4",
                    "3.12.7",
                    "3.13.0",
                    "3.8.10",
                    "3.8.12",
                    "3.8.13",
                    "3.8.15",
                    "3.8.16",
                    "3.8.17",
                    "3.8.18",
                    "3.8.19",
                    "3.8.20",
                    "3.9.10",
                    "3.9.12",
                    "3.9.13",
                    "3.9.15",
                    "3.9.16",
                    "3.9.17",
                    "3.9.18",
                    "3.9.19",
                    "3.9.20"
               ],
               "toolchain_prefixes": [],
               "toolchain_python_versions": [],
               "toolchain_set_python_version_constraints": [],
               "toolchain_user_repository_names": []
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:pythons_hub.bzl%hub_repo",
                    "attributes": {
                         "name": "pythons_hub",
                         "generator_name": "pythons_hub",
                         "generator_function": "py_repositories",
                         "generator_location": None,
                         "default_python_version": "",
                         "minor_mapping": {
                              "3.8": "3.8.20",
                              "3.9": "3.9.20",
                              "3.10": "3.10.15",
                              "3.11": "3.11.10",
                              "3.12": "3.12.7",
                              "3.13": "3.13.0"
                         },
                         "python_versions": [
                              "3.10.11",
                              "3.10.12",
                              "3.10.13",
                              "3.10.14",
                              "3.10.15",
                              "3.10.2",
                              "3.10.4",
                              "3.10.6",
                              "3.10.8",
                              "3.10.9",
                              "3.11.1",
                              "3.11.10",
                              "3.11.3",
                              "3.11.4",
                              "3.11.5",
                              "3.11.6",
                              "3.11.7",
                              "3.11.8",
                              "3.11.9",
                              "3.12.0",
                              "3.12.1",
                              "3.12.2",
                              "3.12.3",
                              "3.12.4",
                              "3.12.7",
                              "3.13.0",
                              "3.8.10",
                              "3.8.12",
                              "3.8.13",
                              "3.8.15",
                              "3.8.16",
                              "3.8.17",
                              "3.8.18",
                              "3.8.19",
                              "3.8.20",
                              "3.9.10",
                              "3.9.12",
                              "3.9.13",
                              "3.9.15",
                              "3.9.16",
                              "3.9.17",
                              "3.9.18",
                              "3.9.19",
                              "3.9.20"
                         ],
                         "toolchain_prefixes": [],
                         "toolchain_python_versions": [],
                         "toolchain_set_python_version_constraints": [],
                         "toolchain_user_repository_names": []
                    },
                    "output_tree_hash": "3e1eecbeb0db3172f8cb417f5d6ec0bf512abdd8465f8ea38e09c8e36c322e26"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__build instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__build",
               "generator_name": "pypi__build",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e2/03/f3c8ba0a6b6e30d7d18c40faab90807c9bb5e9a1e3b2fe2008af624a9c97/build-1.2.1-py3-none-any.whl",
               "sha256": "75e10f767a433d9a86e50d83f418e83efc18ede923ee5ff7df93b6cb0306c5d4",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e2/03/f3c8ba0a6b6e30d7d18c40faab90807c9bb5e9a1e3b2fe2008af624a9c97/build-1.2.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "75e10f767a433d9a86e50d83f418e83efc18ede923ee5ff7df93b6cb0306c5d4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__build"
                    },
                    "output_tree_hash": "1de76c0746001064ed9284733db8f6be4f750074a1ed434b504165c55279e706"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__click instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__click",
               "generator_name": "pypi__click",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl",
               "sha256": "ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl",
                         "urls": [],
                         "sha256": "ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__click"
                    },
                    "output_tree_hash": "29128cbfc3292665939bcfebb4d6471abb579f9a6c22f8880a18bc3c46ad460e"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__colorama instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__colorama",
               "generator_name": "pypi__colorama",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
               "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__colorama"
                    },
                    "output_tree_hash": "8553250f797cc56d5f4fdca6496f70020fe6c221c8ff463fa6af4166b3a5daa7"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__importlib_metadata instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__importlib_metadata",
               "generator_name": "pypi__importlib_metadata",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/2d/0a/679461c511447ffaf176567d5c496d1de27cbe34a87df6677d7171b2fbd4/importlib_metadata-7.1.0-py3-none-any.whl",
               "sha256": "30962b96c0c223483ed6cc7280e7f0199feb01a0e40cfae4d4450fc6fab1f570",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/2d/0a/679461c511447ffaf176567d5c496d1de27cbe34a87df6677d7171b2fbd4/importlib_metadata-7.1.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "30962b96c0c223483ed6cc7280e7f0199feb01a0e40cfae4d4450fc6fab1f570",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__importlib_metadata"
                    },
                    "output_tree_hash": "d73c6382792304ed27a5bfc7f50006341094f8a3b501d3c441b0dbf8159e95e2"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__installer instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__installer",
               "generator_name": "pypi__installer",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
               "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__installer"
                    },
                    "output_tree_hash": "8d48d8e9c356d812c9c19b05b78232d70d096a6244dd51bfb70126dfafdc1ca2"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__more_itertools instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__more_itertools",
               "generator_name": "pypi__more_itertools",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/50/e2/8e10e465ee3987bb7c9ab69efb91d867d93959095f4807db102d07995d94/more_itertools-10.2.0-py3-none-any.whl",
               "sha256": "686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/50/e2/8e10e465ee3987bb7c9ab69efb91d867d93959095f4807db102d07995d94/more_itertools-10.2.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__more_itertools"
                    },
                    "output_tree_hash": "25e8396b111bcd583ad1ed62e2091efbeab377b16892b9db961fc28a42fb9040"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__packaging instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__packaging",
               "generator_name": "pypi__packaging",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/49/df/1fceb2f8900f8639e278b056416d49134fb8d84c5942ffaa01ad34782422/packaging-24.0-py3-none-any.whl",
               "sha256": "2ddfb553fdf02fb784c234c7ba6ccc288296ceabec964ad2eae3777778130bc5",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/49/df/1fceb2f8900f8639e278b056416d49134fb8d84c5942ffaa01ad34782422/packaging-24.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "2ddfb553fdf02fb784c234c7ba6ccc288296ceabec964ad2eae3777778130bc5",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__packaging"
                    },
                    "output_tree_hash": "93fc79b774d75cc535a6ae1c4247dad82ccdbb928f146f44a29f844482fef0f0"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pep517 instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pep517",
               "generator_name": "pypi__pep517",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/25/6e/ca4a5434eb0e502210f591b97537d322546e4833dcb4d470a48c375c5540/pep517-0.13.1-py3-none-any.whl",
               "sha256": "31b206f67165b3536dd577c5c3f1518e8fbaf38cbc57efff8369a392feff1721",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/25/6e/ca4a5434eb0e502210f591b97537d322546e4833dcb4d470a48c375c5540/pep517-0.13.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "31b206f67165b3536dd577c5c3f1518e8fbaf38cbc57efff8369a392feff1721",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pep517"
                    },
                    "output_tree_hash": "4a85e94f8a475c209abe3e6c50b8a704a0767dfc9a7c35cb92c4d928e5043220"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:374:21: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:59:14: in java_tools_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools_linux",
               "generator_name": "remote_java_tools_linux",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v13.6.1/java_tools_linux-v13.6.1.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_13.6.1/java_tools_linux-v13.6.1.zip"
               ],
               "sha256": "0d3fcae7ae40d0a25f17c3adc30a3674f526953c55871189e2efe3463fce3496"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v13.6.1/java_tools_linux-v13.6.1.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_13.6.1/java_tools_linux-v13.6.1.zip"
                         ],
                         "sha256": "0d3fcae7ae40d0a25f17c3adc30a3674f526953c55871189e2efe3463fce3496",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools_linux"
                    },
                    "output_tree_hash": "2e657f5f39af7598f7e4ddc202212df1f3b2e108c69d9c022c0422bb2835e10c"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip",
               "generator_name": "pypi__pip",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl",
               "sha256": "ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip"
                    },
                    "output_tree_hash": "65834a59e24df778029cdbc66cf87c1f5fa08aaf452ba0e9d72ee8bfdeeb4495"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip_tools instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip_tools",
               "generator_name": "pypi__pip_tools",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/0d/dc/38f4ce065e92c66f058ea7a368a9c5de4e702272b479c0992059f7693941/pip_tools-7.4.1-py3-none-any.whl",
               "sha256": "4c690e5fbae2f21e87843e89c26191f0d9454f362d8acdbd695716493ec8b3a9",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/0d/dc/38f4ce065e92c66f058ea7a368a9c5de4e702272b479c0992059f7693941/pip_tools-7.4.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "4c690e5fbae2f21e87843e89c26191f0d9454f362d8acdbd695716493ec8b3a9",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip_tools"
                    },
                    "output_tree_hash": "238237c8e35ff9bdfe5268b8949bef8f0d18ba96d341af92509bcca127472dff"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pyproject_hooks instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pyproject_hooks",
               "generator_name": "pypi__pyproject_hooks",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ae/f3/431b9d5fe7d14af7a32340792ef43b8a714e7726f1d7b69cc4e8e7a3f1d7/pyproject_hooks-1.1.0-py3-none-any.whl",
               "sha256": "7ceeefe9aec63a1064c18d939bdc3adf2d8aa1988a510afec15151578b232aa2",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ae/f3/431b9d5fe7d14af7a32340792ef43b8a714e7726f1d7b69cc4e8e7a3f1d7/pyproject_hooks-1.1.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "7ceeefe9aec63a1064c18d939bdc3adf2d8aa1988a510afec15151578b232aa2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pyproject_hooks"
                    },
                    "output_tree_hash": "4b1b18654eee6f774f4c8e95ccc0b693621666f2315c099373b589664b8a7cc2"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:374:21: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:59:14: in java_tools_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools",
               "generator_name": "remote_java_tools",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v13.6.1/java_tools-v13.6.1.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_13.6.1/java_tools-v13.6.1.zip"
               ],
               "sha256": "74c978eab040ad4ec38ce0d0970ac813cc2c6f4f6f4f121c0414719487edc991"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v13.6.1/java_tools-v13.6.1.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_13.6.1/java_tools-v13.6.1.zip"
                         ],
                         "sha256": "74c978eab040ad4ec38ce0d0970ac813cc2c6f4f6f4f121c0414719487edc991",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools"
                    },
                    "output_tree_hash": "ab225bdec90ae84ae3eae100bc622620656ca5b176170aed4ee1fe374cd48462"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__setuptools instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__setuptools",
               "generator_name": "pypi__setuptools",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/de/88/70c5767a0e43eb4451c2200f07d042a4bcd7639276003a9c54a68cfcc1f8/setuptools-70.0.0-py3-none-any.whl",
               "sha256": "54faa7f2e8d2d11bcd2c07bed282eef1046b5c080d1c32add737d7b5817b1ad4",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/de/88/70c5767a0e43eb4451c2200f07d042a4bcd7639276003a9c54a68cfcc1f8/setuptools-70.0.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "54faa7f2e8d2d11bcd2c07bed282eef1046b5c080d1c32add737d7b5817b1ad4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__setuptools"
                    },
                    "output_tree_hash": "74a6ccfbc86dec1c2a0542212953c77f558ee1485e6b86a994af12ca7f2cb079"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository local_config_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:181:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/cpp/cc_configure.bzl:149:16: in cc_configure\nRepository rule cc_autoconf defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/cpp/cc_configure.bzl:109:30: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc",
               "generator_name": "local_config_cc",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "local_config_cc",
                         "generator_name": "local_config_cc",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "aca1fa29fd29de0e338712d2fc5c54c33001ba7dc1f690b79e237c7ebb6613b7"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:61:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto",
               "generator_name": "rules_proto",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_proto/archive/refs/tags/5.3.0-21.7.tar.gz"
               ],
               "sha256": "dc3fb206a2cb3441b485eb1e423165b231235a1ea9b031b4433cf7bc1fa460dd",
               "strip_prefix": "rules_proto-5.3.0-21.7"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_proto/archive/refs/tags/5.3.0-21.7.tar.gz"
                         ],
                         "sha256": "dc3fb206a2cb3441b485eb1e423165b231235a1ea9b031b4433cf7bc1fa460dd",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto-5.3.0-21.7",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_proto"
                    },
                    "output_tree_hash": "608368d66cb0c59f3804f830d280d6aff5f1ec309d624864b521b3c1157349a4"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__tomli instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__tomli",
               "generator_name": "pypi__tomli",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
               "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__tomli"
                    },
                    "output_tree_hash": "0616aa3668e641c885e2abfa459ceaccb2c9411a8ea1b520b5dc236108f754df"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
          "definition_information": "Repository local_config_xcode instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:184:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/osx/xcode_configure.bzl:312:19: in xcode_configure\nRepository rule xcode_autoconf defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/osx/xcode_configure.bzl:297:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_xcode",
               "generator_name": "local_config_xcode",
               "generator_function": "xcode_configure",
               "generator_location": None,
               "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
                    "attributes": {
                         "name": "local_config_xcode",
                         "generator_name": "local_config_xcode",
                         "generator_function": "xcode_configure",
                         "generator_location": None,
                         "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
                    },
                    "output_tree_hash": "ec026961157bb71cf68d1b568815ad68147ed16f318161bc0da40f6f3d7d79fd"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__wheel instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__wheel",
               "generator_name": "pypi__wheel",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/7d/cd/d7460c9a869b16c3dd4e1e403cce337df165368c71d6af229a74699622ce/wheel-0.43.0-py3-none-any.whl",
               "sha256": "55c570405f142630c6b9f72fe09d9b67cf1477fcf543ae5b8dcb1f5b7377da81",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/7d/cd/d7460c9a869b16c3dd4e1e403cce337df165368c71d6af229a74699622ce/wheel-0.43.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "55c570405f142630c6b9f72fe09d9b67cf1477fcf543ae5b8dcb1f5b7377da81",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__wheel"
                    },
                    "output_tree_hash": "9a7b85a57f83e7fdfda26cbd06b9c2dcf16405dea2608d3b3b43e7d03486d5ee"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__zipp instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:68:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/py_repositories.bzl:72:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__zipp",
               "generator_name": "pypi__zipp",
               "generator_function": "py_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/da/55/a03fd7240714916507e1fcf7ae355bd9d9ed2e6db492595f1a67f61681be/zipp-3.18.2-py3-none-any.whl",
               "sha256": "dce197b859eb796242b0622af1b8beb0a722d52aa2f57133ead08edd5bf5374e",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/da/55/a03fd7240714916507e1fcf7ae355bd9d9ed2e6db492595f1a67f61681be/zipp-3.18.2-py3-none-any.whl",
                         "urls": [],
                         "sha256": "dce197b859eb796242b0622af1b8beb0a722d52aa2f57133ead08edd5bf5374e",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__zipp"
                    },
                    "output_tree_hash": "8d354499ffeef2ddfc8412947e7f230ad2dbcd1f419906fe50ae32997b8328f6"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:python_repository.bzl%python_repository",
          "definition_information": "Repository python_3_11_x86_64-unknown-linux-gnu instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:80:27: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/python_register_toolchains.bzl:133:26: in python_register_toolchains\nRepository rule python_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/python_repository.bzl:267:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python_3_11_x86_64-unknown-linux-gnu",
               "generator_name": "python_3_11_x86_64-unknown-linux-gnu",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "patches": [],
               "platform": "x86_64-unknown-linux-gnu",
               "python_version": "3.11.10",
               "release_filename": "20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz",
               "sha256": "8b50a442b04724a24c1eebb65a36a0c0e833d35374dbdf9c9470d8a97b164cd9",
               "strip_prefix": "python",
               "urls": [
                    "https://github.com/indygreg/python-build-standalone/releases/download/20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:python_repository.bzl%python_repository",
                    "attributes": {
                         "auth_patterns": {},
                         "coverage_tool": "",
                         "distutils": None,
                         "distutils_content": "",
                         "ignore_root_user_error": False,
                         "name": "python_3_11_x86_64-unknown-linux-gnu",
                         "netrc": "",
                         "patch_strip": 1,
                         "patches": [],
                         "platform": "x86_64-unknown-linux-gnu",
                         "python_version": "3.11.10",
                         "release_filename": "20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz",
                         "sha256": "8b50a442b04724a24c1eebb65a36a0c0e833d35374dbdf9c9470d8a97b164cd9",
                         "strip_prefix": "python",
                         "urls": [
                              "https://github.com/indygreg/python-build-standalone/releases/download/20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz"
                         ]
                    },
                    "output_tree_hash": "764ea18d4fbb6d3e7de11a40d1bf529c4437d7d8130e9715c469ce13974e58b3"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:52:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux",
               "generator_name": "remotejdk11_linux",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "urls": [
                    "https://cdn.azul.com/zulu/bin/zulu11.72.19-ca-jdk11.0.23-linux_x64.tar.gz",
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.72.19-ca-jdk11.0.23-linux_x64.tar.gz"
               ],
               "sha256": "0a4d1bfc7a96a7f9f5329b72b9801b3c53366417b4753f1b658fa240204c7347",
               "strip_prefix": "zulu11.72.19-ca-jdk11.0.23-linux_x64",
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 11,\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 11,\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://cdn.azul.com/zulu/bin/zulu11.72.19-ca-jdk11.0.23-linux_x64.tar.gz",
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.72.19-ca-jdk11.0.23-linux_x64.tar.gz"
                         ],
                         "sha256": "0a4d1bfc7a96a7f9f5329b72b9801b3c53366417b4753f1b658fa240204c7347",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.72.19-ca-jdk11.0.23-linux_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 11,\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 11,\n)\n",
                         "workspace_file_content": "",
                         "name": "remotejdk11_linux"
                    },
                    "output_tree_hash": "fbe42375c17e4b8e582dbc3233a8e77c619fc2d5b17a447435134bdfa18d630b"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_cockroachdb_cockroach instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:118:13: in <toplevel>\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_cockroachdb_cockroach",
               "url": "https://github.com/cockroachdb/cockroach/archive/v22.1.6.tar.gz",
               "sha256": "6c3568ef244ce6b874694eeeecb83ed4f5d5dff6cf037c952ecde76828a6c502",
               "strip_prefix": "cockroach-22.1.6"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/cockroachdb/cockroach/archive/v22.1.6.tar.gz",
                         "urls": [],
                         "sha256": "6c3568ef244ce6b874694eeeecb83ed4f5d5dff6cf037c952ecde76828a6c502",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "cockroach-22.1.6",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_cockroachdb_cockroach"
                    },
                    "output_tree_hash": "3352288104bb68fc680f3b0f90336b0025dcbbee66e4336d6561ed5ab34d6e09"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk21_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/utils.bzl:259:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_java_builtin/toolchains/remote_java_repository.bzl:52:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_tools/tools/build_defs/repo/http.bzl:400:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux",
               "generator_name": "remotejdk21_linux",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "urls": [
                    "https://cdn.azul.com/zulu/bin/zulu21.34.19-ca-jdk21.0.3-linux_x64.tar.gz",
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu21.34.19-ca-jdk21.0.3-linux_x64.tar.gz"
               ],
               "sha256": "ca763d1308a6bcc768382f160733a08e591d5f595a7dd9e51b60d27d54828dcc",
               "strip_prefix": "zulu21.34.19-ca-jdk21.0.3-linux_x64",
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 21,\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 21,\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://cdn.azul.com/zulu/bin/zulu21.34.19-ca-jdk21.0.3-linux_x64.tar.gz",
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu21.34.19-ca-jdk21.0.3-linux_x64.tar.gz"
                         ],
                         "sha256": "ca763d1308a6bcc768382f160733a08e591d5f595a7dd9e51b60d27d54828dcc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu21.34.19-ca-jdk21.0.3-linux_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [],
                         "remote_module_file_integrity": "",
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 21,\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = 21,\n)\n",
                         "workspace_file_content": "",
                         "name": "remotejdk21_linux"
                    },
                    "output_tree_hash": "2880f6f2c21ab8ed6b483d504a01ee70c7beadf20191404b735829b18b55784d"
               }
          ]
     },
     {
          "original_rule_class": "@@io_bazel_rules_go//go/private:sdk.bzl%go_download_sdk_rule",
          "definition_information": "Repository go_sdk instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:46:23: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:725:28: in go_register_toolchains\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:318:25: in go_download_sdk\nRepository rule go_download_sdk_rule defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/io_bazel_rules_go/go/private/sdk.bzl:136:39: in <toplevel>\n",
          "original_attributes": {
               "name": "go_sdk",
               "generator_name": "go_sdk",
               "generator_function": "go_register_toolchains",
               "generator_location": None,
               "version": "1.23.1"
          },
          "repositories": [
               {
                    "rule_class": "@@io_bazel_rules_go//go/private:sdk.bzl%go_download_sdk_rule",
                    "attributes": {
                         "name": "go_sdk",
                         "generator_name": "go_sdk",
                         "generator_function": "go_register_toolchains",
                         "generator_location": None,
                         "version": "1.23.1"
                    },
                    "output_tree_hash": "7dd5213e55f329a474a568caf94d903e5a0b2fa6333009404f850f4151b50dc6"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_jvm_external//:coursier.bzl%coursier_fetch",
          "definition_information": "Repository px_deps instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:104:14: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_jvm_external/private/rules/maven_install.bzl:107:19: in maven_install\nRepository rule coursier_fetch defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_jvm_external/coursier.bzl:1306:33: in <toplevel>\n",
          "original_attributes": {
               "name": "px_deps",
               "generator_name": "px_deps",
               "generator_function": "maven_install",
               "generator_location": None,
               "repositories": [
                    "{ \"repo_url\": \"https://repo1.maven.org/maven2\" }"
               ],
               "artifacts": [
                    "{ \"group\": \"org.antlr\", \"artifact\": \"antlr4\", \"version\": \"4.11.1\" }"
               ],
               "fail_on_missing_checksum": True,
               "fetch_sources": False,
               "fetch_javadoc": False,
               "use_unsafe_shared_cache": False,
               "use_credentials_from_home_netrc_file": False,
               "excluded_artifacts": [],
               "generate_compat_repositories": False,
               "version_conflict_policy": "default",
               "override_targets": {},
               "strict_visibility": False,
               "strict_visibility_value": [
                    "//visibility:private"
               ],
               "resolve_timeout": 600,
               "jetify": False,
               "jetify_include_list": [
                    "*"
               ],
               "use_starlark_android_rules": False,
               "aar_import_bzl_label": "@build_bazel_rules_android//android:rules.bzl",
               "duplicate_version_warning": "warn"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_jvm_external//:coursier.bzl%coursier_fetch",
                    "attributes": {
                         "name": "px_deps",
                         "generator_name": "px_deps",
                         "generator_function": "maven_install",
                         "generator_location": None,
                         "repositories": [
                              "{ \"repo_url\": \"https://repo1.maven.org/maven2\" }"
                         ],
                         "artifacts": [
                              "{ \"group\": \"org.antlr\", \"artifact\": \"antlr4\", \"version\": \"4.11.1\" }"
                         ],
                         "fail_on_missing_checksum": True,
                         "fetch_sources": False,
                         "fetch_javadoc": False,
                         "use_unsafe_shared_cache": False,
                         "use_credentials_from_home_netrc_file": False,
                         "excluded_artifacts": [],
                         "generate_compat_repositories": False,
                         "version_conflict_policy": "default",
                         "override_targets": {},
                         "strict_visibility": False,
                         "strict_visibility_value": [
                              "//visibility:private"
                         ],
                         "resolve_timeout": 600,
                         "jetify": False,
                         "jetify_include_list": [
                              "*"
                         ],
                         "use_starlark_android_rules": False,
                         "aar_import_bzl_label": "@build_bazel_rules_android//android:rules.bzl",
                         "duplicate_version_warning": "warn"
                    },
                    "output_tree_hash": "59a0d9f727977cb5ce3bf19dcf28f91d004729ea8b234819a4a43945b86e4472"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private/pypi:whl_library.bzl%whl_library",
          "definition_information": "Repository my_python_deps_numpy instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:77:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/my_python_deps/requirements.bzl:86:20: in install_deps\nRepository rule whl_library defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/rules_python/python/private/pypi/whl_library.bzl:457:30: in <toplevel>\n",
          "original_attributes": {
               "name": "my_python_deps_numpy",
               "generator_name": "my_python_deps_numpy",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "my_python_deps",
               "repo_prefix": "my_python_deps_",
               "requirement": "numpy==1.26.4",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "quiet": True,
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private/pypi:whl_library.bzl%whl_library",
                    "attributes": {
                         "name": "my_python_deps_numpy",
                         "generator_name": "my_python_deps_numpy",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "my_python_deps",
                         "repo_prefix": "my_python_deps_",
                         "requirement": "numpy==1.26.4",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "quiet": True,
                         "timeout": 600
                    },
                    "output_tree_hash": "e8425743a0795e29a675098caca3c470753d205dc83b12f531faabd7b30bbb43"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_gazelle//internal:go_repository_cache.bzl%go_repository_cache",
          "definition_information": "Repository bazel_gazelle_go_repository_cache instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:47:21: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/deps.bzl:76:28: in gazelle_dependencies\nRepository rule go_repository_cache defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/internal/go_repository_cache.bzl:77:38: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_go_repository_cache",
               "generator_name": "bazel_gazelle_go_repository_cache",
               "generator_function": "gazelle_dependencies",
               "generator_location": None,
               "go_sdk_info": {
                    "go_sdk": "host"
               },
               "go_env": {}
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_gazelle//internal:go_repository_cache.bzl%go_repository_cache",
                    "attributes": {
                         "name": "bazel_gazelle_go_repository_cache",
                         "generator_name": "bazel_gazelle_go_repository_cache",
                         "generator_function": "gazelle_dependencies",
                         "generator_location": None,
                         "go_sdk_info": {
                              "go_sdk": "host"
                         },
                         "go_env": {}
                    },
                    "output_tree_hash": "be3c38168cf914014d392ca995f43f467b04bc2f9270f50e7b51acf86973ce4c"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_gazelle//internal:go_repository_tools.bzl%go_repository_tools",
          "definition_information": "Repository bazel_gazelle_go_repository_tools instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:47:21: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/deps.bzl:82:24: in gazelle_dependencies\nRepository rule go_repository_tools defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/internal/go_repository_tools.bzl:117:38: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_go_repository_tools",
               "generator_name": "bazel_gazelle_go_repository_tools",
               "generator_function": "gazelle_dependencies",
               "generator_location": None,
               "go_cache": "@@bazel_gazelle_go_repository_cache//:go.env"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_gazelle//internal:go_repository_tools.bzl%go_repository_tools",
                    "attributes": {
                         "name": "bazel_gazelle_go_repository_tools",
                         "generator_name": "bazel_gazelle_go_repository_tools",
                         "generator_function": "gazelle_dependencies",
                         "generator_location": None,
                         "go_cache": "@@bazel_gazelle_go_repository_cache//:go.env"
                    },
                    "output_tree_hash": "4d617d946d0b5ede134351ab917c10a967d580c659f201388c34c8e6c611fbea"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_gazelle//internal:go_repository_config.bzl%go_repository_config",
          "definition_information": "Repository bazel_gazelle_go_repository_config instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:47:21: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/deps.bzl:87:25: in gazelle_dependencies\nRepository rule go_repository_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/internal/go_repository_config.bzl:69:39: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_go_repository_config",
               "generator_name": "bazel_gazelle_go_repository_config",
               "generator_function": "gazelle_dependencies",
               "generator_location": None,
               "config": "//:WORKSPACE"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_gazelle//internal:go_repository_config.bzl%go_repository_config",
                    "attributes": {
                         "name": "bazel_gazelle_go_repository_config",
                         "generator_name": "bazel_gazelle_go_repository_config",
                         "generator_function": "gazelle_dependencies",
                         "generator_location": None,
                         "config": "//:WORKSPACE"
                    },
                    "output_tree_hash": "70b5de78ec59d4fbc1f271d85b7bec8bddf81369b7f752dcb7452e2f1eab53d2"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository org_golang_x_net instantiated at:\n  /usr/local/google/home/kotlaja/migration_tool/bazel-central-registry/tools/bzlmod_migration_test_examples/docs/WORKSPACE:49:14: in <toplevel>\nRepository rule go_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/2582b7ac5cec30526d328691d305d4e4/external/bazel_gazelle/internal/go_repository.bzl:379:32: in <toplevel>\n",
          "original_attributes": {
               "name": "org_golang_x_net",
               "importpath": "golang.org/x/net",
               "version": "v0.0.0-20190311183353-d8887717615a",
               "sum": "h1:oWX7TPOiFAMXLq8o0ikBYfCJVlRHBcsciT5bXOrH628=",
               "build_naming_convention": "import",
               "build_file_proto_mode": "disable"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "org_golang_x_net",
                         "importpath": "golang.org/x/net",
                         "version": "v0.0.0-20190311183353-d8887717615a",
                         "sum": "h1:oWX7TPOiFAMXLq8o0ikBYfCJVlRHBcsciT5bXOrH628=",
                         "build_naming_convention": "import",
                         "build_file_proto_mode": "disable"
                    },
                    "output_tree_hash": "4600d64097ac8924caa9f59b315354cbf06bfacb87f1ed82e8aca675752a35b2"
               }
          ]
     }
]