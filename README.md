## Quality Assurance Command Line Interface (CLI)

This program allows individual phases of our Quality Assurance process to be executed.

### Dependencies

This program has been targeted to be ran with `Python3`. The following dependencies are required to extend or execute program commands. To install program dependencies please execute the following commands. However, please note that installing packages via the console can be problematic so probably better done via your chosen IDE. Please see the references section below for more information on package dependencies.

```bash
# install local dependencies
$ pip install -r requirements.txt --user
# or view local dependencies
$ cat requirements.txt
```

### Usage

Please run the following command to display which options are made available by this program.

```bash
$ python -m project --help
```

### Execution

Please use the following commands to execute each phase of Quality Assurance locally or on build.

Run all project specific *unit tests* with *code coverage*, and Junit XML formatted reports.

```bash
$ python -m project [--path /path/to/directory] --unittest
```

Enable project specific *code style* inspections and reporting

```bash
$ python -m project [--path /path/to/directory] --codestyle
```

Enable *debug* for logging to console

```bash
$ python -m project [...] --debug
```

### Configuration

Please note that the configuration files contained within [data/config](data/config) are used when a project is validated against our Quality Assurance expectations. During build the configuration files are copied over to the project under test to guarantee that the reports we require are generated correctly. The following configuration files contain all the default properties required during build.

- [data/config/.noserc](data/config/.noserc)
- [data/config/.coveragerc](data/config/.coveragerc)
- [data/styles/google.rc](data/styles/google.rc)

Important: The following environment variable needs to be set when using this program. The variable contents the location of this program.

```bash
export QA_EXEC_BASE="/path/to/quality-assurance-cli"
```

### Extending this Program

The following sections describe what you may need to know if you need to extend this programs functionality. This variable will also need to be present during build.

#### Development

Please `source` the following script to support use. It should help with setting up your development environment, so is convenient if your extending this program's functionality.

```bash
# setup a development environment
$ source ./bin/export-dev.env
```

#### Test

While in development you may need to confirm that functionality meets test and style guide expectations. To do this please execute the following commands.

Runs all the *unit tests* for this program.

```bash
$ python -m nose -v project.tests
```

Runs a single *unit test* for this program.

```bash
$ python -m nose -v --tests project.tests.test_options
$ python -m nose -v --tests project.tests.test_process
$ python -m nose -v --tests project.tests.test_project
```

To enable code coverage reports you will probably need to update the (.noserc)[.noserc] and/or (.coveragerc)[.coveragerc] to provide support. Once you are happy with the configuration you can run `nose` with the following options.

```bash
$ python -m nose -v --config /path/to/.noserc project.tests
```

Please run the following command to generate *code style* reports. These are presently validated against Google's Style Guide. If you need to ignore a file, or files, add the following argument to this command.

- `--ignore=` allows to you to specify file which should be ignored, e.g., `__main__.py`

```bash
$ python -m pylint --rcfile data/styles/google.rc project
```

#### Documentation

While in development you may need to automatically generate documentation which describes the program's interface, behaviour and dependencies. Please execute the following commands to generate this documentation.

```bash
£ use this command to add more sections to the documentation
$ cd docs; sphinx-apidoc -f -o source ../project; cd -
# documentation is found under doc/build/html/index.html
# please note, the warnings generated as part of the build process can sometimes be ignored ;)
$ cd docs; sphinx-build -M html source build; cd -
```

Please execute the following commands to erase previous documentation files.

```bash
# handy if generation errors occur
# please note: make (GCC) is not installed on the desktop
$ rm -rf doc/build/html
```

#### References

- https://docs.pylint.org/en/latest
- https://nose.readthedocs.io/en/latest
- https://nose.readthedocs.io/en/latest/usage.html
- https://coverage.readthedocs.io/en/latest/config.html
- https://docs.pylint.org/en/latest/run.html
- https://github.com/vinitkumar/googlecl

### Author

Bug reports, pull requests and feature requests are welcomed.

-
-
