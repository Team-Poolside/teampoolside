# TEAM POOLSIDE WEBSITE

Contains the source code for <https://teampoolsi.de>

## Development

It's a django site.

Main page is located in `website`, shop is located in `store`

### Environment setup

---

#### Docker (preferred)

this site is containerized using docker. start the services using `docker-compose`:

```sh
$ docker-compose up -d --build
```

which will serve the site at `localhost:8000`

you can kill this by running

```sh
$ docker-compose down
```



to test the production environment, pass `-f docker-compose.prod.yml` to the above commands

(if you need to remove the data volumes too, pass `-v` to the down commands)

#### Conda

Provided for convenience is a conda environment file. Install it with

```sh
$ ./scripts/env/init
```

in the root of the project directory (you'll need a conda distribution installed).
Then you can activate it with

```sh
$ ./scripts/env/activate
```

if you add new packages to the virtual environment, update it with

```sh
$ ./scripts/env/update
```

I also recommend setting things up so that the conda env is automatically activated when you enter the project directory (though this is optional):

1. install `direnv` (`sudo apt install direnv` or similar)
2. add the following to `~/.bashrc` (or equivalent) after the `# >>> conda initialize` section:

    ```sh
    show_conda_env() {
        if [[ -n "$CONDA_DEFAULT_ENV" ]]; then
            echo "($(basename $CONDA_DEFAULT_ENV))"
        fi
    }

    export -f show_conda_env
    # use our own PS1 in place of conda's
    conda config --set changeps1 False
    PS1='$(show_conda_env) '$PS1

    # set up direnv
    eval "$(direnv hook bash)"
    ```

3. add the following to `~/.direnvrc`:

    ```sh
    layout_miniconda() {
        if [ -n "$1" ]; then
                local env_name="$1"
                source activate ${env_name}
        elif (grep -q name: environment.yml); then
                source activate \
                    `grep name: environment.yml | sed -e 's/name: //' | cut -d "" -f 2 | cut -d "" -f 2`
        else
                (>&2 echo No environment specified);
                exit 1;
        fi
    }
    ```

4. run `direnv allow .` in the repository directory

_Note: the above was adapted into a more readable format from [this article](https://medium.com/@manishdixit1986/auto-switch-conda-env-per-directory-using-conda-direnv-in-linux-13c912da6520).
