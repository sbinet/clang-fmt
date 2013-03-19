clang-fmt
=========

``clang-fmt`` is a backport of ``clang-format`` from (the not yet
released) ``clang-3.3`` into the 3.2 environment.

## Installation

```sh
# usual hwaf dance
$ hwaf init some-dir
$ hwaf setup some-dir
$ cd some-dir

# real installation
$ hwaf pkg co git://github.com/sbinet/clang-fmt
$ hwaf configure
$ hwaf
```

## Example

```sh
$ cat > bar.cxx
namespace Ns {class bar{
int m_int    ; public:
bar ( ) ; void some_meth(const int & an_int ) ;};} //> namespace Ns

$ clang-fmt --style=Google bar.cxx
namespace Ns {
class bar {
  int m_int;
 public:
  bar();
  void some_meth(const int& an_int);
};
}  //> namespace Ns

```

