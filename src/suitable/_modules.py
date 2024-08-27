# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from __future__ import annotations

from typing import overload, Any, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import StrPath
    from suitable._module_types import (
        AptResults,
        AptKeyResults,
        AptRepositoryResults,
        AssembleResults,
        AsyncStatusResults,
        CommandResults,
        CopyResults,
        CronResults,
        Deb822RepositoryResults,
        DebconfResults,
        Dnf5Results,
        FileResults,
        FindResults,
        GatherFactsResults,
        GetUrlResults,
        GetentResults,
        GitResults,
        GroupResults,
        ImportPlaybookResults,
        ImportRoleResults,
        ImportTasksResults,
        IncludeResults,
        IncludeRoleResults,
        IncludeTasksResults,
        IncludeVarsResults,
        LineinfileResults,
        PackageFactsResults,
        PauseResults,
        PingResults,
        PipResults,
        RebootResults,
        ReplaceResults,
        RpmKeyResults,
        ServiceResults,
        ServiceFactsResults,
        ShellResults,
        SlurpResults,
        StatResults,
        SubversionResults,
        SystemdResults,
        SystemdServiceResults,
        SysvinitResults,
        TempfileResults,
        TemplateResults,
        UnarchiveResults,
        UriResults,
        UserResults,
        ValidateArgumentSpecResults,
        WaitForResults,
        WaitForConnectionResults,
        YumRepositoryResults,
    )
    from suitable.types import Incomplete
    from typing_extensions import Never as NotSupported


# HACK: Get Sphinx to display the default values we don't
#       know as `...` and also avoid mypy errors.
_Unknown: Any = type('...', (object,), {'__repr__': lambda s: '...'})()


class AnsibleModules:

    def apt(
        self,
        *,
        name: NotSupported = _Unknown,
        state: Literal[
            'absent',
            'build-dep',
            'latest',
            'present',
            'fixed',
        ] = 'present',
        update_cache: bool = _Unknown,
        update_cache_retries: int = 5,
        update_cache_retry_max_delay: int = 12,
        cache_valid_time: int = 0,
        purge: bool = False,
        default_release: str = _Unknown,
        install_recommends: bool = _Unknown,
        force: bool = False,
        clean: bool = False,
        allow_unauthenticated: bool = False,
        allow_downgrade: bool = False,
        allow_change_held_packages: bool = False,
        upgrade: Literal['dist', 'full', 'no', 'safe', 'yes'] = 'no',
        dpkg_options: str = 'force-confdef,force-confold',
        deb: StrPath = _Unknown,
        autoremove: bool = False,
        autoclean: bool = False,
        policy_rc_d: int = _Unknown,
        only_upgrade: bool = False,
        fail_on_autoremove: bool = False,
        force_apt_get: bool = False,
        lock_timeout: int = 60,
    ) -> AptResults:
        """
        Manages apt-packages.

        :param name:
            A list of package names, like `foo`, or package specifier with
            version, like `foo=1.0` or `foo>=1.0`. Name wildcards (fnmatch)
            like `apt*` and version wildcards like `foo=1.0*` are also
            supported.
        :param state:
            Indicates the desired package state. `latest` ensures that the
            latest version is installed. `build-dep` ensures the package build
            dependencies are installed. `fixed` attempt to correct a system
            with broken dependencies in place.
        :param update_cache:
            Run the equivalent of `apt-get update` before the operation. Can
            be run as part of the package installation or as a separate step.
            Default is not to update the cache.
        :param update_cache_retries:
            Amount of retries if the cache update fails. Also see
            `update_cache_retry_max_delay`.
            Requires ansible-core >= 2.10
        :param update_cache_retry_max_delay:
            Use an exponential backoff delay for each retry (see
            `update_cache_retries`) up to this max delay in seconds.
            Requires ansible-core >= 2.10
        :param cache_valid_time:
            Update the apt cache if it is older than the `cache_valid_time`.
            This option is set in seconds.
            As of Ansible 2.4, if explicitly set, this sets `update_cache=yes`.
        :param purge:
            Will force purging of configuration files if `state=absent` or
            `autoremove=yes`.
        :param default_release:
            Corresponds to the `-t` option for *apt* and sets pin priorities.
        :param install_recommends:
            Corresponds to the `--no-install-recommends` option for *apt*.
            `true` installs recommended packages.  `false` does not install
            recommended packages. By default, Ansible will use the same
            defaults as the operating system. Suggested packages are never
            installed.
        :param force:
            Corresponds to the `--force-yes` to *apt-get* and implies
            `allow_unauthenticated=yes` and `allow_downgrade=yes`.
            This option will disable checking both the packages' signatures
            and the certificates of the web servers they are downloaded from.
            This option *is not* the equivalent of passing the `-f` flag to
            *apt-get* on the command line.
            **This is a destructive operation with the potential to destroy
            your system, and it should almost never be used.** Please also see
            `man apt-get` for more information.
        :param clean:
            Run the equivalent of `apt-get clean` to clear out the local
            repository of retrieved package files. It removes everything but
            the lock file from /var/cache/apt/archives/ and
            /var/cache/apt/archives/partial/.
            Can be run as part of the package installation (clean runs before
            install) or as a separate step.
            Requires ansible-core >= 2.13
        :param allow_unauthenticated:
            Ignore if packages cannot be authenticated. This is useful for
            bootstrapping environments that manage their own apt-key setup.
            `allow_unauthenticated` is only supported with `state`:
            `install`/`present`.
        :param allow_downgrade:
            Corresponds to the `--allow-downgrades` option for *apt*.
            This option enables the named package and version to replace an
            already installed higher version of that package.
            Note that setting `allow_downgrade=true` can make this module
            behave in a non-idempotent way.
            (The task could end up with a set of packages that does not match
            the complete list of specified packages to install).
            `allow_downgrade` is only supported by `apt` and will be ignored
            if `aptitude` is detected or specified.
            Requires ansible-core >= 2.12
        :param allow_change_held_packages:
            Allows changing the version of a package which is on the apt hold
            list.
            Requires ansible-core >= 2.13
        :param upgrade:
            If yes or safe, performs an aptitude safe-upgrade.
            If full, performs an aptitude full-upgrade.
            If dist, performs an apt-get dist-upgrade.
            Note: This does not upgrade a specific package, use state=latest
            for that.
            Note: Since 2.4, apt-get is used as a fall-back if aptitude is not
            present.
        :param dpkg_options:
            Add dpkg options to apt command. Defaults to '-o
            "Dpkg::Options::=--force-confdef" -o
            "Dpkg::Options::=--force-confold"'.
            Options should be supplied as comma separated list.
        :param deb:
            Path to a .deb package on the remote machine.
            If :// in the path, ansible will attempt to download deb before
            installing. (Version added 2.1).
            Requires the `xz-utils` package to extract the control file of the
            deb package to install.
        :param autoremove:
            If `true`, remove unused dependency packages for all module states
            except `build-dep`. It can also be used as the only option.
            Previous to version 2.4, autoclean was also an alias for
            autoremove, now it is its own separate command. See documentation
            for further information.
        :param autoclean:
            If `true`, cleans the local repository of retrieved package files
            that can no longer be downloaded.
        :param policy_rc_d:
            Force the exit code of /usr/sbin/policy-rc.d.
            For example, if *policy_rc_d=101* the installed package will not
            trigger a service start.
            If /usr/sbin/policy-rc.d already exists, it is backed up and
            restored after the package installation.
            If `null`, the /usr/sbin/policy-rc.d isn't created/changed.
        :param only_upgrade:
            Only upgrade a package if it is already installed.
        :param fail_on_autoremove:
            Corresponds to the `--no-remove` option for `apt`.
            If `true`, it is ensured that no packages will be removed or the
            task will fail.
            `fail_on_autoremove` is only supported with `state` except
            `absent`.
            `fail_on_autoremove` is only supported by `apt` and will be
            ignored if `aptitude` is detected or specified.
            Requires ansible-core >= 2.11
        :param force_apt_get:
            Force usage of apt-get instead of aptitude.
        :param lock_timeout:
            How many seconds will this action wait to acquire a lock on the
            apt db.
            Sometimes there is a transitory lock and this will retry at least
            until timeout is hit.
            Requires ansible-core >= 2.12
        """
        raise AttributeError('apt')

    def apt_key(
        self,
        *,
        id: str = _Unknown,
        data: str = _Unknown,
        file: StrPath = _Unknown,
        keyring: StrPath = _Unknown,
        url: str = _Unknown,
        keyserver: str = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        validate_certs: bool = True,
    ) -> AptKeyResults:
        """
        Add or remove an apt key.

        :param id:
            The identifier of the key.
            Including this allows check mode to correctly report the changed
            state.
            If specifying a subkey's id be aware that apt-key does not
            understand how to remove keys via a subkey id.  Specify the
            primary key's id instead.
            This parameter is required when `state` is set to `absent`.
        :param data:
            The keyfile contents to add to the keyring.
        :param file:
            The path to a keyfile on the remote server to add to the keyring.
        :param keyring:
            The full path to specific keyring file in
            `/etc/apt/trusted.gpg.d/`.
        :param url:
            The URL to retrieve key from.
        :param keyserver:
            The keyserver to retrieve key from.
        :param state:
            Ensures that the key is present (added) or absent (revoked).
        :param validate_certs:
            If `false`, SSL certificates for the target url will not be
            validated. This should only be used on personally controlled sites
            using self-signed certificates.
        """
        raise AttributeError('apt_key')

    def apt_repository(
        self,
        *,
        repo: str,
        state: Literal['absent', 'present'] = 'present',
        mode: str = _Unknown,
        update_cache: bool = True,
        update_cache_retries: int = 5,
        update_cache_retry_max_delay: int = 12,
        validate_certs: bool = True,
        filename: str = _Unknown,
        codename: str = _Unknown,
        install_python_apt: bool = True,
    ) -> AptRepositoryResults:
        """
        Add and remove APT repositories.

        :param repo:
            A source string for the repository.
        :param state:
            A source string state.
        :param mode:
            The octal mode for newly created files in sources.list.d.
            Default is what system uses (probably 0644).
        :param update_cache:
            Run the equivalent of `apt-get update` when a change occurs.
            Cache updates are run after making changes.
        :param update_cache_retries:
            Amount of retries if the cache update fails. Also see
            `update_cache_retry_max_delay`.
            Requires ansible-core >= 2.10
        :param update_cache_retry_max_delay:
            Use an exponential backoff delay for each retry (see
            `update_cache_retries`) up to this max delay in seconds.
            Requires ansible-core >= 2.10
        :param validate_certs:
            If `false`, SSL certificates for the target repo will not be
            validated. This should only be used on personally controlled sites
            using self-signed certificates.
        :param filename:
            Sets the name of the source list file in sources.list.d. Defaults
            to a file name based on the repository source url. The .list
            extension will be automatically added.
        :param codename:
            Override the distribution codename to use for PPA repositories.
            Should usually only be set when working with a PPA on a non-Ubuntu
            target (for example, Debian or Mint).
        :param install_python_apt:
            Whether to automatically try to install the Python apt library or
            not, if it is not already installed. Without this library, the
            module does not work.
            Runs `apt-get install python-apt` for Python 2, and `apt-get
            install python3-apt` for Python 3.
            Only works with the system Python 2 or Python 3. If you are using
            a Python on the remote that is not the system Python, set
            `install_python_apt=false` and ensure that the Python apt library
            for your Python version is installed some other way.
        """
        raise AttributeError('apt_repository')

    def assemble(
        self,
        *,
        src: StrPath,
        dest: StrPath,
        backup: bool = False,
        delimiter: str = _Unknown,
        remote_src: bool = True,
        regexp: str = _Unknown,
        ignore_hidden: bool = False,
        validate: str = _Unknown,
    ) -> AssembleResults:
        """
        Assemble configuration files from fragments.

        :param src:
            An already existing directory full of source files.
        :param dest:
            A file to create using the concatenation of all of the source
            files.
        :param backup:
            Create a backup file (if `true`), including the timestamp
            information so you can get the original file back if you somehow
            clobbered it incorrectly.
        :param delimiter:
            A delimiter to separate the file contents.
        :param remote_src:
            If `false`, it will search for src at originating/master machine.
            If `true`, it will go to the remote/target machine for the src.
        :param regexp:
            Assemble files only if the given regular expression matches the
            filename.
            If not set, all files are assembled.
            Every `\\` (backslash) must be escaped as `\\\\` to comply to YAML
            syntax.
            Uses `Python regular expressions
            <https://docs.python.org/3/library/re.html>`__.
        :param ignore_hidden:
            A boolean that controls if files that start with a '.' will be
            included or not.
        :param validate:
            The validation command to run before copying into place.
            The path to the file to validate is passed in via '%s' which must
            be present as in the sshd example below.
            The command is passed securely so shell features like expansion
            and pipes won't work.
        """
        raise AttributeError('assemble')

    def async_status(
        self,
        *,
        jid: str,
        mode: Literal['cleanup', 'status'] = 'status',
    ) -> AsyncStatusResults:
        """
        Obtain status of asynchronous task.

        :param jid:
            Job or task identifier.
        :param mode:
            If `status`, obtain the status.
            If `cleanup`, clean up the async job cache (by default in
            `~/.ansible_async/`) for the specified job `jid`, without waiting
            for it to finish.
        """
        raise AttributeError('async_status')

    @overload
    def command(
        self,
        *,
        expand_argument_vars: bool = True,
        cmd: str = _Unknown,
        argv: NotSupported = _Unknown,
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        chdir: StrPath = _Unknown,
        stdin: str = _Unknown,
        stdin_add_newline: bool = True,
        strip_empty_ends: bool = True,
    ) -> CommandResults: ...

    @overload
    def command(self, arg: str, /) -> CommandResults: ...

    def command(self, *args: Any, **kwargs: Any) -> CommandResults:
        """
        Execute commands on targets.

        :param expand_argument_vars:
            Expands the arguments that are variables, for example `$HOME` will
            be expanded before being passed to the command to run.
            Set to `false` to disable expansion and treat the value as a
            literal argument.
            Requires ansible-core >= 2.16
        :param cmd:
            The command to run.
        :param argv:
            Passes the command as a list rather than a string.
            Use `argv` to avoid quoting values that would otherwise be
            interpreted incorrectly (for example "user name").
            Only the string (free form) or the list (argv) form can be
            provided, not both.  One or the other must be provided.
        :param creates:
            A filename or (since 2.0) glob pattern. If a matching file already
            exists, this step **will not** be run.
            This is checked before `removes` is checked.
        :param removes:
            A filename or (since 2.0) glob pattern. If a matching file exists,
            this step **will** be run.
            This is checked after `creates` is checked.
        :param chdir:
            Change into this directory before running the command.
        :param stdin:
            Set the stdin of the command directly to the specified value.
        :param stdin_add_newline:
            If set to `true`, append a newline to stdin data.
        :param strip_empty_ends:
            Strip empty lines from the end of stdout/stderr in result.
        """
        raise AttributeError('command')

    def copy(
        self,
        *,
        src: StrPath = _Unknown,
        content: str = _Unknown,
        dest: StrPath,
        backup: bool = False,
        force: bool = True,
        mode: str = _Unknown,
        directory_mode: str = _Unknown,
        remote_src: bool = False,
        follow: bool = False,
        local_follow: bool = True,
        checksum: str = _Unknown,
    ) -> CopyResults:
        """
        Copy files to remote locations.

        :param src:
            Local path to a file to copy to the remote server.
            This can be absolute or relative.
            If path is a directory, it is copied recursively. In this case, if
            path ends with "/", only inside contents of that directory are
            copied to destination. Otherwise, if it does not end with "/", the
            directory itself with all contents is copied. This behavior is
            similar to the `rsync` command line tool.
        :param content:
            When used instead of `src`, sets the contents of a file directly
            to the specified value.
            Works only when `dest` is a file. Creates the file if it does not
            exist.
            For advanced formatting or if `content` contains a variable, use
            the :meth:`ansible.builtin.template` module.
        :param dest:
            Remote absolute path where the file should be copied to.
            If `src` is a directory, this must be a directory too.
            If `dest` is a non-existent path and if either `dest` ends with
            "/" or `src` is a directory, `dest` is created.
            If `dest` is a relative path, the starting directory is determined
            by the remote host.
            If `src` and `dest` are files, the parent directory of `dest` is
            not created and the task fails if it does not already exist.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param force:
            Influence whether the remote file must always be replaced.
            If `true`, the remote file will be replaced when contents are
            different than the source.
            If `false`, the file will only be transferred if the destination
            does not exist.
        :param mode:
            The permissions of the destination file or directory.
            For those used to `/usr/bin/chmod` remember that modes are
            actually octal numbers. You must either add a leading zero so that
            Ansible's YAML parser knows it is an octal number (like `0644` or
            `01777`) or quote it (like `'644'` or `'1777'`) so Ansible
            receives a string and can do its own conversion from string into
            number. Giving Ansible a number without following one of these
            rules will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, `u+rwx` or `u=rw,g=r,o=r`).
            As of Ansible 2.3, the mode may also be the special string
            `preserve`.
            `preserve` means that the file will be given the same permissions
            as the source file.
            When doing a recursive copy, see also `directory_mode`.
            If `mode` is not specified and the destination file **does not**
            exist, the default `umask` on the system will be used when setting
            the mode for the newly created file.
            If `mode` is not specified and the destination file **does**
            exist, the mode of the existing file will be used.
            Specifying `mode` is the best way to ensure files are created with
            the correct permissions. See CVE-2020-1736 for further details.
        :param directory_mode:
            Set the access permissions of newly created directories to the
            given mode. Permissions on existing directories do not change.
            See `mode` for the syntax of accepted values.
            The target system's defaults determine permissions when this
            parameter is not set.
        :param remote_src:
            Influence whether `src` needs to be transferred or already is
            present remotely.
            If `false`, it will search for `src` on the controller node.
            If `true` it will search for `src` on the managed (remote) node.
            `remote_src` supports recursive copying as of version 2.8.
            `remote_src` only works with `mode=preserve` as of version 2.6.
            Auto-decryption of files does not work when `remote_src=yes`.
        :param follow:
            This flag indicates that filesystem links in the destination, if
            they exist, should be followed.
        :param local_follow:
            This flag indicates that filesystem links in the source tree, if
            they exist, should be followed.
        :param checksum:
            SHA1 checksum of the file being transferred.
            Used to validate that the copy of the file was successful.
            If this is not provided, ansible will use the local calculated
            checksum of the src file.
        """
        raise AttributeError('copy')

    def cron(
        self,
        *,
        name: str,
        user: str = _Unknown,
        job: str = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        cron_file: StrPath = _Unknown,
        backup: bool = False,
        minute: str = '*',
        hour: str = '*',
        day: str = '*',
        month: str = '*',
        weekday: str = '*',
        special_time: Literal[
            'annually',
            'daily',
            'hourly',
            'monthly',
            'reboot',
            'weekly',
            'yearly',
        ] = _Unknown,
        disabled: bool = False,
        env: bool = False,
        insertafter: str = _Unknown,
        insertbefore: str = _Unknown,
    ) -> CronResults:
        """
        Manage cron.d and crontab entries.

        :param name:
            Description of a crontab entry or, if env is set, the name of
            environment variable.
            This parameter is always required as of ansible-core 2.12.
        :param user:
            The specific user whose crontab should be modified.
            When unset, this parameter defaults to the current user.
        :param job:
            The command to execute or, if env is set, the value of environment
            variable.
            The command should not contain line breaks.
            Required if `state=present`.
        :param state:
            Whether to ensure the job or environment variable is present or
            absent.
        :param cron_file:
            If specified, uses this file instead of an individual user's
            crontab. The assumption is that this file is exclusively managed
            by the module, do not use if the file contains multiple entries,
            NEVER use for /etc/crontab.
            If this is a relative path, it is interpreted with respect to
            `/etc/cron.d`.
            Many linux distros expect (and some require) the filename portion
            to consist solely of upper- and lower-case letters, digits,
            underscores, and hyphens.
            Using this parameter requires you to specify the `user` as well,
            unless `state` is not `present`.
            Either this parameter or `name` is required.
        :param backup:
            If set, create a backup of the crontab before it is modified. The
            location of the backup is returned in the R`ignore:backup_file`
            variable by this module.
        :param minute:
            Minute when the job should run (`0-59`, `*`, `*/2`, and so on).
        :param hour:
            Hour when the job should run (`0-23`, `*`, `*/2`, and so on).
        :param day:
            Day of the month the job should run (`1-31`, `*`, `*/2`, and so
            on).
        :param month:
            Month of the year the job should run (`1-12`, `*`, `*/2`, and so
            on).
        :param weekday:
            Day of the week that the job should run (`0-6` for
            Sunday-Saturday, `*`, and so on).
        :param special_time:
            Special time specification nickname.
        :param disabled:
            If the job should be disabled (commented out) in the crontab.
            Only has effect if `state=present`.
        :param env:
            If set, manages a crontab's environment variable.
            New variables are added on top of crontab.
            `name` and `value` parameters are the name and the value of
            environment variable.
        :param insertafter:
            Used with `state=present` and `env`.
            If specified, the environment variable will be inserted after the
            declaration of specified environment variable.
        :param insertbefore:
            Used with `state=present` and `env`.
            If specified, the environment variable will be inserted before the
            declaration of specified environment variable.
        """
        raise AttributeError('cron')

    def deb822_repository(
        self,
        *,
        allow_downgrade_to_insecure: bool = _Unknown,
        allow_insecure: bool = _Unknown,
        allow_weak: bool = _Unknown,
        architectures: NotSupported = _Unknown,
        by_hash: bool = _Unknown,
        check_date: bool = _Unknown,
        check_valid_until: bool = _Unknown,
        components: NotSupported = _Unknown,
        date_max_future: int = _Unknown,
        enabled: bool = _Unknown,
        inrelease_path: str = _Unknown,
        languages: NotSupported = _Unknown,
        name: str,
        pdiffs: bool = _Unknown,
        signed_by: str = _Unknown,
        suites: NotSupported = _Unknown,
        targets: NotSupported = _Unknown,
        trusted: bool = _Unknown,
        types: NotSupported = _Unknown,
        uris: NotSupported = _Unknown,
        mode: str = '0644',
        state: Literal['absent', 'present'] = 'present',
    ) -> Deb822RepositoryResults:
        """
        Add and remove deb822 formatted repositories.

        .. note:: Requires ansible-core >= 2.15

        :param allow_downgrade_to_insecure:
            Allow downgrading a package that was previously authenticated but
            is no longer authenticated.
        :param allow_insecure:
            Allow insecure repositories.
        :param allow_weak:
            Allow repositories signed with a key using a weak digest algorithm.
        :param architectures:
            Architectures to search within repository.
        :param by_hash:
            Controls if APT should try to acquire indexes via a URI
            constructed from a hashsum of the expected file instead of using
            the well-known stable filename of the index.
        :param check_date:
            Controls if APT should consider the machine's time correct and
            hence perform time related checks, such as verifying that a
            Release file is not from the future.
        :param check_valid_until:
            Controls if APT should try to detect replay attacks.
        :param components:
            Components specify different sections of one distribution version
            present in a Suite.
        :param date_max_future:
            Controls how far from the future a repository may be.
        :param enabled:
            Tells APT whether the source is enabled or not.
        :param inrelease_path:
            Determines the path to the InRelease file, relative to the normal
            position of an InRelease file.
        :param languages:
            Defines which languages information such as translated package
            descriptions should be downloaded.
        :param name:
            Name of the repo. Specifically used for `X-Repolib-Name` and in
            naming the repository and signing key files.
        :param pdiffs:
            Controls if APT should try to use PDiffs to update old indexes
            instead of downloading the new indexes entirely.
        :param signed_by:
            Either a URL to a GPG key, absolute path to a keyring file, one or
            more fingerprints of keys either in the `trusted.gpg` keyring or
            in the keyrings in the `trusted.gpg.d/` directory, or an ASCII
            armored GPG public key block.
        :param suites:
            Suite can specify an exact path in relation to the UR*s* provided,
            in which case the Components: must be omitted and suite must end
            with a slash (`/`). Alternatively, it may take the form of a
            distribution version (e.g. a version codename like disco or
            artful). If the suite does not specify a path, at least one
            component must be present.
        :param targets:
            Defines which download targets apt will try to acquire from this
            source.
        :param trusted:
            Decides if a source is considered trusted or if warnings should be
            raised before e.g. packages are installed from this source.
        :param types:
            Which types of packages to look for from a given source; either
            binary `deb` or source code `deb-src`.
        :param uris:
            The URIs must specify the base of the Debian distribution archive,
            from which APT finds the information it needs.
        :param mode:
            The octal mode for newly created files in sources.list.d.
        :param state:
            A source string state.
        """
        raise AttributeError('deb822_repository')

    def debconf(
        self,
        *,
        name: str,
        question: str = _Unknown,
        vtype: Literal[
            'boolean',
            'error',
            'multiselect',
            'note',
            'password',
            'seen',
            'select',
            'string',
            'text',
            'title',
        ] = _Unknown,
        value: str = _Unknown,
        unseen: bool = False,
    ) -> DebconfResults:
        """
        Configure a .deb package.

        :param name:
            Name of package to configure.
        :param question:
            A debconf configuration setting.
        :param vtype:
            The type of the value supplied.
            It is highly recommended to add `no_log=True` to task while
            specifying `vtype=password`.
            `seen` was added in Ansible 2.2.
            After Ansible 2.17, user can specify `value` as a list, if `vtype`
            is set as `multiselect`.
        :param value:
            Value to set the configuration to.
            After Ansible 2.17, `value` is of type 'raw'.
        :param unseen:
            Do not set 'seen' flag when pre-seeding.
        """
        raise AttributeError('debconf')

    def dnf5(
        self,
        *,
        name: NotSupported = _Unknown,
        list: str = _Unknown,
        state: Literal[
            'absent',
            'present',
            'installed',
            'removed',
            'latest',
        ] = _Unknown,
        enablerepo: NotSupported = _Unknown,
        disablerepo: NotSupported = _Unknown,
        conf_file: str = _Unknown,
        disable_gpg_check: bool = False,
        installroot: str = '/',
        releasever: str = _Unknown,
        autoremove: bool = False,
        exclude: NotSupported = _Unknown,
        skip_broken: bool = False,
        update_cache: bool = False,
        update_only: bool = False,
        security: bool = False,
        bugfix: bool = False,
        enable_plugin: NotSupported = _Unknown,
        disable_plugin: NotSupported = _Unknown,
        disable_excludes: str = _Unknown,
        validate_certs: bool = True,
        sslverify: bool = True,
        allow_downgrade: bool = False,
        install_repoquery: bool = True,
        download_only: bool = False,
        lock_timeout: int = 30,
        install_weak_deps: bool = True,
        download_dir: str = _Unknown,
        allowerasing: bool = False,
        nobest: bool = _Unknown,
        best: bool = _Unknown,
        cacheonly: bool = False,
    ) -> Dnf5Results:
        """
        Manages packages with the *dnf5* package manager.

        .. note:: Requires ansible-core >= 2.15

        :param name:
            A package name or package specifier with version, like `name-1.0`.
            When using state=latest, this can be '*' which means run: dnf -y
            update. You can also pass a url or a local path to an rpm file. To
            operate on several packages this can accept a comma separated
            string of packages or a list of packages.
            Comparison operators for package version are valid here `>`, `<`,
            `>=`, `<=`. Example - `name >= 1.0`. Spaces around the operator
            are required.
            You can also pass an absolute path for a binary which is provided
            by the package to install. See examples for more information.
        :param list:
            Various (non-idempotent) commands for usage with
            `/usr/bin/ansible` and *not* playbooks. Use
            :meth:`ansible.builtin.package_facts` instead of the `list`
            argument as a best practice.
        :param state:
            Whether to install (`present`, `latest`), or remove (`absent`) a
            package.
            Default is `None`, however in effect the default action is
            `present` unless the `autoremove` option is enabled for this
            module, then `absent` is inferred.
        :param enablerepo:
            *Repoid* of repositories to enable for the install/update
            operation. These repos will not persist beyond the transaction.
            When specifying multiple repos, separate them with a ",".
        :param disablerepo:
            *Repoid* of repositories to disable for the install/update
            operation. These repos will not persist beyond the transaction.
            When specifying multiple repos, separate them with a ",".
        :param conf_file:
            The remote dnf configuration file to use for the transaction.
        :param disable_gpg_check:
            Whether to disable the GPG checking of signatures of packages
            being installed. Has an effect only if `state` is `present` or
            `latest`.
            This setting affects packages installed from a repository as well
            as "local" packages installed from the filesystem or a URL.
        :param installroot:
            Specifies an alternative installroot, relative to which all
            packages will be installed.
        :param releasever:
            Specifies an alternative release from which all packages will be
            installed.
        :param autoremove:
            If `true`, removes all "leaf" packages from the system that were
            originally installed as dependencies of user-installed packages
            but which are no longer required by any such package. Should be
            used alone or when `state` is `absent`.
        :param exclude:
            Package name(s) to exclude when state=present, or latest. This can
            be a list or a comma separated string.
        :param skip_broken:
            Skip all unavailable packages or packages with broken dependencies
            without raising an error. Equivalent to passing the --skip-broken
            option.
        :param update_cache:
            Force dnf to check if cache is out of date and redownload if
            needed. Has an effect only if `state` is `present` or `latest`.
        :param update_only:
            When using latest, only update installed packages. Do not install
            packages.
            Has an effect only if `state` is `latest`.
        :param security:
            If set to `true`, and `state=latest` then only installs updates
            that have been marked security related.
            Note that, similar to `dnf upgrade-minimal`, this filter applies
            to dependencies as well.
        :param bugfix:
            If set to `true`, and `state=latest` then only installs updates
            that have been marked bugfix related.
            Note that, similar to `dnf upgrade-minimal`, this filter applies
            to dependencies as well.
        :param enable_plugin:
            This is currently a no-op as dnf5 itself does not implement this
            feature.
            *Plugin* name to enable for the install/update operation. The
            enabled plugin will not persist beyond the transaction.
        :param disable_plugin:
            This is currently a no-op as dnf5 itself does not implement this
            feature.
            *Plugin* name to disable for the install/update operation. The
            disabled plugins will not persist beyond the transaction.
        :param disable_excludes:
            Disable the excludes defined in DNF config files.
            If set to `all`, disables all excludes.
            If set to `main`, disable excludes defined in [main] in dnf.conf.
            If set to `repoid`, disable excludes defined for given repo id.
        :param validate_certs:
            This is effectively a no-op in the dnf5 module as dnf5 itself
            handles downloading a https url as the source of the rpm, but is
            an accepted parameter for feature parity/compatibility with the
            :meth:`ansible.builtin.dnf` module.
        :param sslverify:
            Disables SSL validation of the repository server for this
            transaction.
            This should be set to `false` if one of the configured
            repositories is using an untrusted or self-signed certificate.
        :param allow_downgrade:
            Specify if the named package and version is allowed to downgrade a
            maybe already installed higher version of that package. Note that
            setting allow_downgrade=True can make this module behave in a
            non-idempotent way. The task could end up with a set of packages
            that does not match the complete list of specified packages to
            install (because dependencies between the downgraded package and
            others can cause changes to the packages which were in the earlier
            transaction).
        :param install_repoquery:
            This is effectively a no-op in DNF as it is not needed with DNF.
            This option is deprecated and will be removed in ansible-core 2.20.
        :param download_only:
            Only download the packages, do not install them.
        :param lock_timeout:
            This is currently a no-op as dnf5 does not provide an option to
            configure it.
            Amount of time to wait for the dnf lockfile to be freed.
        :param install_weak_deps:
            Will also install all packages linked by a weak dependency
            relation.
        :param download_dir:
            Specifies an alternate directory to store packages.
            Has an effect only if `download_only` is specified.
        :param allowerasing:
            If `true` it allows  erasing  of  installed  packages to resolve
            dependencies.
        :param nobest:
            This is the opposite of the `best` option kept for backwards
            compatibility.
            Since ansible-core 2.17 the default value is set by the operating
            system distribution.
        :param best:
            When set to `true`, either use a package with the highest version
            available or fail.
            When set to `false`, if the latest version cannot be installed go
            with the lower version.
            Default is set by the operating system distribution.
            Requires ansible-core >= 2.17
        :param cacheonly:
            Tells dnf to run entirely from system cache; does not download or
            update metadata.
        """
        raise AttributeError('dnf5')

    def file(
        self,
        *,
        path: StrPath,
        state: Literal[
            'absent',
            'directory',
            'file',
            'hard',
            'link',
            'touch',
        ] = _Unknown,
        src: StrPath = _Unknown,
        recurse: bool = False,
        force: bool = False,
        follow: bool = True,
        modification_time: str = _Unknown,
        modification_time_format: str = '%Y%m%d%H%M.%S',
        access_time: str = _Unknown,
        access_time_format: str = '%Y%m%d%H%M.%S',
    ) -> FileResults:
        """
        Manage files and file properties.

        :param path:
            Path to the file being managed.
        :param state:
            If `absent`, directories will be recursively deleted, and files or
            symlinks will be unlinked. In the case of a directory, if `diff`
            is declared, you will see the files and folders deleted listed
            under `path_contents`. Note that `absent` will not cause
            :meth:`ansible.builtin.file` to fail if the `path` does not exist
            as the state did not change.
            If `directory`, all intermediate subdirectories will be created if
            they do not exist. Since Ansible 1.7 they will be created with the
            supplied permissions.
            If `file`, with no other options, returns the current state of
            `path`.
            If `file`, even with other options (such as `mode`), the file will
            be modified if it exists but will NOT be created if it does not
            exist. Set to `touch` or use the :meth:`ansible.builtin.copy` or
            :meth:`ansible.builtin.template` module if you want to create the
            file if it does not exist.
            If `hard`, the hard link will be created or changed.
            If `link`, the symbolic link will be created or changed.
            If `touch` (new in 1.4), an empty file will be created if the file
            does not exist, while an existing file or directory will receive
            updated file access and modification times (similar to the way
            `touch` works from the command line).
            Default is the current state of the file if it exists, `directory`
            if `recurse=yes`, or `file` otherwise.
        :param src:
            Path of the file to link to.
            This applies only to `state=link` and `state=hard`.
            For `state=link`, this will also accept a non-existing path.
            Relative paths are relative to the file being created (`path`)
            which is how the Unix command `ln -s SRC DEST` treats relative
            paths.
        :param recurse:
            Recursively set the specified file attributes on directory
            contents.
            This applies only when `state` is set to `directory`.
        :param force:
            Force the creation of the symlinks in two cases: the source file
            does not exist (but will appear later); the destination exists and
            is a file (so, we need to unlink the `path` file and create a
            symlink to the `src` file in place of it).
        :param follow:
            This flag indicates that filesystem links, if they exist, should
            be followed.
            `follow=yes` and `state=link` can modify `src` when combined with
            parameters such as `mode`.
            Previous to Ansible 2.5, this was `false` by default.
            While creating a symlink with a non-existent destination, set
            `follow` to `false` to avoid a warning message related to
            permission issues. The warning message is added to notify the user
            that we can not set permissions to the non-existent destination.
        :param modification_time:
            This parameter indicates the time the file's modification time
            should be set to.
            Should be `preserve` when no modification is required,
            `YYYYMMDDHHMM.SS` when using default time format, or `now`.
            Default is None meaning that `preserve` is the default for
            `state=[file,directory,link,hard]` and `now` is default for
            `state=touch`.
        :param modification_time_format:
            When used with `modification_time`, indicates the time format that
            must be used.
            Based on default Python format (see time.strftime doc).
        :param access_time:
            This parameter indicates the time the file's access time should be
            set to.
            Should be `preserve` when no modification is required,
            `YYYYMMDDHHMM.SS` when using default time format, or `now`.
            Default is `None` meaning that `preserve` is the default for
            `state=[file,directory,link,hard]` and `now` is default for
            `state=touch`.
        :param access_time_format:
            When used with `access_time`, indicates the time format that must
            be used.
            Based on default Python format (see time.strftime doc).
        """
        raise AttributeError('file')

    def find(
        self,
        *,
        age: str = _Unknown,
        patterns: NotSupported = _Unknown,
        excludes: NotSupported = _Unknown,
        contains: str = _Unknown,
        read_whole_file: bool = False,
        paths: NotSupported,
        file_type: Literal['any', 'directory', 'file', 'link'] = 'file',
        recurse: bool = False,
        size: str = _Unknown,
        age_stamp: Literal['atime', 'ctime', 'mtime'] = 'mtime',
        hidden: bool = False,
        mode: str = _Unknown,
        exact_mode: bool = True,
        follow: bool = False,
        get_checksum: bool = False,
        use_regex: bool = False,
        depth: int = _Unknown,
        encoding: str = _Unknown,
    ) -> FindResults:
        """
        Return a list of files based on specific criteria.

        :param age:
            Select files whose age is equal to or greater than the specified
            time.
            Use a negative age to find files equal to or less than the
            specified time.
            You can choose seconds, minutes, hours, days, or weeks by
            specifying the first letter of any of those words (e.g., "1w").
        :param patterns:
            One or more (shell or regex) patterns, which type is controlled by
            `use_regex` option.
            The patterns restrict the list of files to be returned to those
            whose basenames match at least one of the patterns specified.
            Multiple patterns can be specified using a list.
            The pattern is matched against the file base name, excluding the
            directory.
            When using regexen, the pattern MUST match the ENTIRE file name,
            not just parts of it. So if you are looking to match all files
            ending in .default, you'd need to use `.*\\.default` as a regexp
            and not just `\\.default`.
            This parameter expects a list, which can be either comma separated
            or YAML. If any of the patterns contain a comma, make sure to put
            them in a list to avoid splitting the patterns in undesirable ways.
            Defaults to `*` when `use_regex=False`, or `.*` when
            `use_regex=True`.
        :param excludes:
            One or more (shell or regex) patterns, which type is controlled by
            `use_regex` option.
            Items whose basenames match an `excludes` pattern are culled from
            `patterns` matches. Multiple patterns can be specified using a
            list.
        :param contains:
            A regular expression or pattern which should be matched against
            the file content.
            If `read_whole_file` is `false` it matches against the beginning
            of the line (uses `re.match(\\`)). If `read_whole_file` is `true`,
            it searches anywhere for that pattern (uses `re.search(\\`)).
            Works only when `file_type` is `file`.
        :param read_whole_file:
            When doing a `contains` search, determines whether the whole file
            should be read into memory or if the regex should be applied to
            the file line-by-line.
            Setting this to `true` can have performance and memory
            implications for large files.
            This uses `re.search(\\`) instead of `re.match(\\`).
            Requires ansible-core >= 2.11
        :param paths:
            List of paths of directories to search. All paths must be fully
            qualified.
        :param file_type:
            Type of file to select.
            The 'link' and 'any' choices were added in Ansible 2.3.
        :param recurse:
            If target is a directory, recursively descend into the directory
            looking for files.
        :param size:
            Select files whose size is equal to or greater than the specified
            size.
            Use a negative size to find files equal to or less than the
            specified size.
            Unqualified values are in bytes but b, k, m, g, and t can be
            appended to specify bytes, kilobytes, megabytes, gigabytes, and
            terabytes, respectively.
            Size is not evaluated for directories.
        :param age_stamp:
            Choose the file property against which we compare age.
        :param hidden:
            Set this to `true` to include hidden files, otherwise they will be
            ignored.
        :param mode:
            Choose objects matching a specified permission. This value is
            restricted to modes that can be applied using the python
            `os.chmod` function.
            The mode can be provided as an octal such as `"0644"` or as
            symbolic such as `u=rw,g=r,o=r`.
            Requires ansible-core >= 2.16
        :param exact_mode:
            Restrict mode matching to exact matches only, and not as a minimum
            set of permissions to match.
            Requires ansible-core >= 2.16
        :param follow:
            Set this to `true` to follow symlinks in path for systems with
            python 2.6+.
        :param get_checksum:
            Set this to `true` to retrieve a file's SHA1 checksum.
        :param use_regex:
            If `false`, the patterns are file globs (shell).
            If `true`, they are python regexes.
        :param depth:
            Set the maximum number of levels to descend into.
            Setting recurse to `false` will override this value, which is
            effectively depth 1.
            Default is unlimited depth.
        :param encoding:
            When doing a `contains` search, determine the encoding of the
            files to be searched.
            Requires ansible-core >= 2.17
        """
        raise AttributeError('find')

    def gather_facts(
        self,
        *,
        parallel: bool = _Unknown,
    ) -> GatherFactsResults:
        """
        Gathers facts about remote hosts.

        :param parallel:
            A toggle that controls if the fact modules are executed in
            parallel or serially and in order. This can guarantee the merge
            order of module facts at the expense of performance.
            By default it will be true if more than one fact module is used.
            For low cost/delay fact modules parallelism overhead might end up
            meaning the whole process takes longer. Test your specific case to
            see if it is a speed improvement or not.
        """
        raise AttributeError('gather_facts')

    def get_url(
        self,
        *,
        ciphers: NotSupported = _Unknown,
        decompress: bool = True,
        url: str,
        dest: StrPath,
        tmp_dest: StrPath = _Unknown,
        force: bool = False,
        backup: bool = False,
        checksum: str = '',
        use_proxy: bool = True,
        validate_certs: bool = True,
        timeout: int = 10,
        headers: NotSupported = _Unknown,
        url_username: str = _Unknown,
        url_password: str = _Unknown,
        force_basic_auth: bool = False,
        client_cert: StrPath = _Unknown,
        client_key: StrPath = _Unknown,
        http_agent: str = 'ansible-httpget',
        unredirected_headers: NotSupported = _Unknown,
        use_gssapi: bool = False,
        use_netrc: bool = True,
    ) -> GetUrlResults:
        """
        Downloads files from HTTP, HTTPS, or FTP to node.

        :param ciphers:
            SSL/TLS Ciphers to use for the request.
            When a list is provided, all ciphers are joined in order with `:`.
            See the `OpenSSL Cipher List Format
            <https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html#CIPHER-LIST-FORMAT>`__
            for more details.
            The available ciphers is dependent on the Python and
            OpenSSL/LibreSSL versions.
            Requires ansible-core >= 2.14
        :param decompress:
            Whether to attempt to decompress gzip content-encoded responses.
            Requires ansible-core >= 2.14
        :param url:
            HTTP, HTTPS, or FTP URL in the form
            (http|https|ftp)://[user[:pass]]@host.domain[:port]/path.
        :param dest:
            Absolute path of where to download the file to.
            If `dest` is a directory, either the server provided filename or,
            if none provided, the base name of the URL on the remote server
            will be used. If a directory, `force` has no effect.
            If `dest` is a directory, the file will always be downloaded
            (regardless of the `force` and `checksum` option), but replaced
            only if the contents changed.
        :param tmp_dest:
            Absolute path of where temporary file is downloaded to.
            When run on Ansible 2.5 or greater, path defaults to ansible's
            remote_tmp setting.
            When run on Ansible prior to 2.5, it defaults to `TMPDIR`, `TEMP`
            or `TMP` env variables or a platform specific value.
            `tempfile.tempdir
            <https://docs.python.org/3/library/tempfile.html#tempfile.tempdir>`__.

        :param force:
            If `true` and `dest` is not a directory, will download the file
            every time and replace the file if the contents change. If
            `false`, the file will only be downloaded if the destination does
            not exist. Generally should be `true` only for small local files.
            Prior to 0.6, this module behaved as if `true` was the default.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param checksum:
            If a checksum is passed to this parameter, the digest of the
            destination file will be calculated after it is downloaded to
            ensure its integrity and verify that the transfer completed
            successfully. Format: <algorithm>:<checksum|url>, e.g.
            checksum="sha256:D98291AC[...]B6DC7B97",
            checksum="sha256:http://example.com/path/sha256sum.txt".
            If you worry about portability, only the sha1 algorithm is
            available on all platforms and python versions.
            The Python ``hashlib`` module is responsible for providing the
            available algorithms. The choices vary based on Python version and
            OpenSSL version.
            On systems running in FIPS compliant mode, the ``md5`` algorithm
            may be unavailable.
            Additionally, if a checksum is passed to this parameter, and the
            file exist under the `dest` location, the `destination_checksum`
            would be calculated, and if checksum equals
            `destination_checksum`, the file download would be skipped (unless
            `force` is `true`). If the checksum does not equal
            `destination_checksum`, the destination file is deleted.
        :param use_proxy:
            if `false`, it will not use a proxy, even if one is defined in an
            environment variable on the target hosts.
        :param validate_certs:
            If `false`, SSL certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param timeout:
            Timeout in seconds for URL request.
        :param headers:
            Add custom HTTP headers to a request in hash/dict format.
            The hash/dict format was added in Ansible 2.6.
            Previous versions used a `"key:value,key:value"` string format.
            The `"key:value,key:value"` string format is deprecated and has
            been removed in version 2.10.
        :param url_username:
            The username for use in HTTP basic authentication.
            This parameter can be used without `url_password` for sites that
            allow empty passwords.
            Since version 2.8 you can also use the `username` alias for this
            option.
        :param url_password:
            The password for use in HTTP basic authentication.
            If the `url_username` parameter is not specified, the
            `url_password` parameter will not be used.
            Since version 2.8 you can also use the `password` alias for this
            option.
        :param force_basic_auth:
            Force the sending of the Basic authentication header upon initial
            request.
            httplib2, the library used by the uri module only sends
            authentication information when a webservice responds to an
            initial request with a 401 status. Since some basic auth services
            do not properly send a 401, logins will fail.
        :param client_cert:
            PEM formatted certificate chain file to be used for SSL client
            authentication.
            This file can also include the key as well, and if the key is
            included, `client_key` is not required.
        :param client_key:
            PEM formatted file that contains your private key to be used for
            SSL client authentication.
            If `client_cert` contains both the certificate and key, this
            option is not required.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
        :param unredirected_headers:
            A list of header names that will not be sent on subsequent
            redirected requests. This list is case insensitive. By default all
            headers will be redirected. In some cases it may be beneficial to
            list headers such as `Authorization` here to avoid potential
            credential exposure.
            Requires ansible-core >= 2.12
        :param use_gssapi:
            Use GSSAPI to perform the authentication, typically this is for
            Kerberos or Kerberos through Negotiate authentication.
            Requires the Python library `gssapi
            <https://github.com/pythongssapi/python-gssapi>`__ to be installed.
            Credentials for GSSAPI can be specified with
            `url_username`/`url_password` or with the GSSAPI env var
            `KRB5CCNAME` that specified a custom Kerberos credential cache.
            NTLM authentication is *not* supported even if the GSSAPI mech for
            NTLM has been installed.
            Requires ansible-core >= 2.11
        :param use_netrc:
            Determining whether to use credentials from ``~/.netrc`` file.
            By default .netrc is used with Basic authentication headers.
            When set to False, .netrc credentials are ignored.
            Requires ansible-core >= 2.14
        """  # noqa: E501
        raise AttributeError('get_url')

    def getent(
        self,
        *,
        database: str,
        key: str = _Unknown,
        service: str = _Unknown,
        split: str = _Unknown,
        fail_key: bool = True,
    ) -> GetentResults:
        """
        A wrapper to the unix getent utility.

        :param database:
            The name of a getent database supported by the target system
            (passwd, group, hosts, etc).
        :param key:
            Key from which to return values from the specified database,
            otherwise the full contents are returned.
        :param service:
            Override all databases with the specified service.
            The underlying system must support the service flag which is not
            always available.
            Requires ansible-core >= 2.9
        :param split:
            Character used to split the database values into lists/arrays such
            as `:` or `\\t`, otherwise it will try to pick one depending on
            the database.
        :param fail_key:
            If a supplied key is missing this will make the task fail if
            `true`.
        """
        raise AttributeError('getent')

    def git(
        self,
        *,
        repo: str,
        dest: StrPath,
        version: str = 'HEAD',
        accept_hostkey: bool = False,
        accept_newhostkey: bool = False,
        ssh_opts: str = _Unknown,
        key_file: StrPath = _Unknown,
        reference: str = _Unknown,
        remote: str = 'origin',
        refspec: str = _Unknown,
        force: bool = False,
        depth: int = _Unknown,
        clone: bool = True,
        update: bool = True,
        executable: StrPath = _Unknown,
        bare: bool = False,
        umask: str = _Unknown,
        recursive: bool = True,
        single_branch: bool = False,
        track_submodules: bool = False,
        verify_commit: bool = False,
        archive: StrPath = _Unknown,
        archive_prefix: str = _Unknown,
        separate_git_dir: StrPath = _Unknown,
        gpg_allowlist: NotSupported = _Unknown,
    ) -> GitResults:
        """
        Deploy software (or files) from git checkouts.

        :param repo:
            git, SSH, or HTTP(S) protocol address of the git repository.
        :param dest:
            The path of where the repository should be checked out. This is
            equivalent to `git clone [repo_url] [directory]`. The repository
            named in `repo` is not appended to this path and the destination
            directory must be empty. This parameter is required, unless
            `clone` is set to `false`.
        :param version:
            What version of the repository to check out. This can be the
            literal string `HEAD`, a branch name, a tag name. It can also be a
            *SHA-1* hash, in which case `refspec` needs to be specified if the
            given revision is not already available.
        :param accept_hostkey:
            Will ensure or not that "-o StrictHostKeyChecking=no" is present
            as an ssh option.
            Be aware that this disables a protection against MITM attacks.
            Those using OpenSSH >= 7.5 might want to set `ssh_opts` to
            `StrictHostKeyChecking=accept-new` instead, it does not remove the
            MITM issue but it does restrict it to the first attempt.
        :param accept_newhostkey:
            As of OpenSSH 7.5, "-o StrictHostKeyChecking=accept-new" can be
            used which is safer and will only accepts host keys which are not
            present or are the same. if `true`, ensure that "-o
            StrictHostKeyChecking=accept-new" is present as an ssh option.
            Requires ansible-core >= 2.12
        :param ssh_opts:
            Options git will pass to ssh when used as protocol, it works via
            `git`'s `GIT_SSH`/`GIT_SSH_COMMAND` environment variables.
            For older versions it appends `GIT_SSH_OPTS` (specific to this
            module) to the variables above or via a wrapper script.
            Other options can add to this list, like `key_file` and
            `accept_hostkey`.
            An example value could be "-o StrictHostKeyChecking=no" (although
            this particular option is better set by `accept_hostkey`).
            The module ensures that 'BatchMode=yes' is always present to avoid
            prompts.
        :param key_file:
            Specify an optional private key file path, on the target host, to
            use for the checkout.
            This ensures 'IdentitiesOnly=yes' is present in `ssh_opts`.
        :param reference:
            Reference repository (see "git clone --reference ...").
        :param remote:
            Name of the remote.
        :param refspec:
            Add an additional refspec to be fetched. If version is set to a
            *SHA-1* not reachable from any branch or tag, this option may be
            necessary to specify the ref containing the *SHA-1*. Uses the same
            syntax as the `git fetch` command. An example value could be
            "refs/meta/config".
        :param force:
            If `true`, any modified files in the working repository will be
            discarded.  Prior to 0.7, this was always `true` and could not be
            disabled.  Prior to 1.9, the default was `true`.
        :param depth:
            Create a shallow clone with a history truncated to the specified
            number or revisions. The minimum possible value is `1`, otherwise
            ignored. Needs *git>=1.9.1* to work correctly.
        :param clone:
            If `false`, do not clone the repository even if it does not exist
            locally.
        :param update:
            If `false`, do not retrieve new revisions from the origin
            repository.
            Operations like archive will work on the existing (old) repository
            and might not respond to changes to the options version or remote.
        :param executable:
            Path to git executable to use. If not supplied, the normal
            mechanism for resolving binary paths will be used.
        :param bare:
            If `true`, repository will be created as a bare repo, otherwise it
            will be a standard repo with a workspace.
        :param umask:
            The umask to set before doing any checkouts, or any other
            repository maintenance.
        :param recursive:
            If `false`, repository will be cloned without the `--recursive`
            option, skipping sub-modules.
        :param single_branch:
            Clone only the history leading to the tip of the specified
            revision.
            Requires ansible-core >= 2.11
        :param track_submodules:
            If `true`, submodules will track the latest commit on their master
            branch (or other branch specified in .gitmodules).  If `false`,
            submodules will be kept at the revision specified by the main
            project. This is equivalent to specifying the `--remote` flag to
            git submodule update.
        :param verify_commit:
            If `true`, when cloning or checking out a `version` verify the
            signature of a GPG signed commit. This requires git version>=2.1.0
            to be installed. The commit MUST be signed and the public key MUST
            be present in the GPG keyring.
        :param archive:
            Specify archive file path with extension. If specified, creates an
            archive file of the specified format containing the tree structure
            for the source tree. Allowed archive formats ["zip", "tar.gz",
            "tar", "tgz"].
            This will clone and perform git archive from local directory as
            not all git servers support git archive.
        :param archive_prefix:
            Specify a prefix to add to each file path in archive. Requires
            `archive` to be specified.
            Requires ansible-core >= 2.10
        :param separate_git_dir:
            The path to place the cloned repository. If specified, Git
            repository can be separated from working tree.
        :param gpg_allowlist:
            A list of trusted GPG fingerprints to compare to the fingerprint
            of the GPG-signed commit.
            Only used when `verify_commit=yes`.
            Use of this feature requires Git 2.6+ due to its reliance on git's
            `--raw` flag to `verify-commit` and `verify-tag`.
            Alias `gpg_allowlist` is added in version 2.17.
            Alias `gpg_whitelist` is deprecated and will be removed in version
            2.21.
            Requires ansible-core >= 2.9
        """
        raise AttributeError('git')

    def group(
        self,
        *,
        name: str,
        gid: int = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        force: bool = False,
        system: bool = False,
        local: bool = False,
        non_unique: bool = False,
    ) -> GroupResults:
        """
        Add or remove groups.

        :param name:
            Name of the group to manage.
        :param gid:
            Optional *GID* to set for the group.
        :param state:
            Whether the group should be present or not on the remote host.
        :param force:
            Whether to delete a group even if it is the primary group of a
            user.
            Only applicable on platforms which implement a --force flag on the
            group deletion command.
            Requires ansible-core >= 2.15
        :param system:
            If `True`, indicates that the group created is a system group.
        :param local:
            Forces the use of "local" command alternatives on platforms that
            implement it.
            This is useful in environments that use centralized authentication
            when you want to manipulate the local groups. (for example, it
            uses `lgroupadd` instead of `groupadd`).
            This requires that these commands exist on the targeted host,
            otherwise it will be a fatal error.
        :param non_unique:
            This option allows to change the group ID to a non-unique value.
            Requires `gid`.
            Not supported on macOS or BusyBox distributions.
        """
        raise AttributeError('group')

    def import_playbook(self, arg: str, /) -> ImportPlaybookResults:
        """
        Import a playbook.
        """
        raise AttributeError('import_playbook')

    def import_role(
        self,
        *,
        name: str,
        tasks_from: str = 'main',
        vars_from: str = 'main',
        defaults_from: str = 'main',
        allow_duplicates: bool = True,
        handlers_from: str = 'main',
        rolespec_validate: bool = True,
        public: bool = True,
    ) -> ImportRoleResults:
        """
        Import a role into a play.

        :param name:
            The name of the role to be executed.
        :param tasks_from:
            File to load from a role's `tasks/` directory.
        :param vars_from:
            File to load from a role's `vars/` directory.
        :param defaults_from:
            File to load from a role's `defaults/` directory.
        :param allow_duplicates:
            Overrides the role's metadata setting to allow using a role more
            than once with the same parameters.
        :param handlers_from:
            File to load from a role's `handlers/` directory.
        :param rolespec_validate:
            Perform role argument spec validation if an argument spec is
            defined.
            Requires ansible-core >= 2.11
        :param public:
            This option dictates whether the role's `vars` and `defaults` are
            exposed to the play.
            Variables are exposed to the play at playbook parsing time, and
            available to earlier roles and tasks as well unlike `include_role`.
            The default depends on the configuration option
            :ref:`default_private_role_vars`.
            Requires ansible-core >= 2.17
        """
        raise AttributeError('import_role')

    @overload
    def import_tasks(
        self,
        *,
        file: str = _Unknown,
    ) -> ImportTasksResults: ...

    @overload
    def import_tasks(self, arg: str, /) -> ImportTasksResults: ...

    def import_tasks(self, *args: Any, **kwargs: Any) -> ImportTasksResults:
        """
        Import a task list.

        :param file:
            Specifies the name of the file that lists tasks to add to the
            current playbook.
        """
        raise AttributeError('import_tasks')

    def include(self, arg: str, /) -> IncludeResults:
        """
        Include a play or task list.
        """
        raise AttributeError('include')

    def include_role(
        self,
        *,
        apply: str = _Unknown,
        name: str,
        tasks_from: str = 'main',
        vars_from: str = 'main',
        defaults_from: str = 'main',
        allow_duplicates: bool = True,
        public: bool = False,
        handlers_from: str = 'main',
        rolespec_validate: bool = True,
    ) -> IncludeRoleResults:
        """
        Load and execute a role.

        :param apply:
            Accepts a hash of task keywords (for example `tags`, `become`)
            that will be applied to all tasks within the included role.
        :param name:
            The name of the role to be executed.
        :param tasks_from:
            File to load from a role's `tasks/` directory.
        :param vars_from:
            File to load from a role's `vars/` directory.
        :param defaults_from:
            File to load from a role's `defaults/` directory.
        :param allow_duplicates:
            Overrides the role's metadata setting to allow using a role more
            than once with the same parameters.
        :param public:
            This option dictates whether the role's `vars` and `defaults` are
            exposed to the play. If set to `true` the variables will be
            available to tasks following the `include_role` task. This
            functionality differs from standard variable exposure for roles
            listed under the `roles` header or
            :meth:`ansible.builtin.import_role` as they are exposed to the
            play at playbook parsing time, and available to earlier roles and
            tasks as well.
        :param handlers_from:
            File to load from a role's `handlers/` directory.
        :param rolespec_validate:
            Perform role argument spec validation if an argument spec is
            defined.
            Requires ansible-core >= 2.11
        """
        raise AttributeError('include_role')

    @overload
    def include_tasks(
        self,
        *,
        file: str = _Unknown,
        apply: str = _Unknown,
    ) -> IncludeTasksResults: ...

    @overload
    def include_tasks(self, arg: str, /) -> IncludeTasksResults: ...

    def include_tasks(self, *args: Any, **kwargs: Any) -> IncludeTasksResults:
        """
        Dynamically include a task list.

        :param file:
            Specifies the name of the file that lists tasks to add to the
            current playbook.
        :param apply:
            Accepts a hash of task keywords (for example `tags`, `become`)
            that will be applied to the tasks within the include.
        """
        raise AttributeError('include_tasks')

    @overload
    def include_vars(
        self,
        *,
        file: StrPath = _Unknown,
        dir: StrPath = _Unknown,
        name: str = _Unknown,
        depth: int = 0,
        files_matching: str = _Unknown,
        ignore_files: NotSupported = _Unknown,
        extensions: NotSupported = _Unknown,
        ignore_unknown_extensions: bool = False,
        hash_behaviour: Literal['replace', 'merge'] = _Unknown,
    ) -> IncludeVarsResults: ...

    @overload
    def include_vars(self, arg: str, /) -> IncludeVarsResults: ...

    def include_vars(self, *args: Any, **kwargs: Any) -> IncludeVarsResults:
        """
        Load variables from files, dynamically within a task.

        :param file:
            The file name from which variables should be loaded.
            If the path is relative, it will look for the file in vars/
            subdirectory of a role or relative to playbook.
        :param dir:
            The directory name from which the variables should be loaded.
            If the path is relative and the task is inside a role, it will
            look inside the role's vars/ subdirectory.
            If the path is relative and not inside a role, it will be parsed
            relative to the playbook.
        :param name:
            The name of a variable into which assign the included vars.
            If omitted (null) they will be made top level vars.
        :param depth:
            When using `dir`, this module will, by default, recursively go
            through each sub directory and load up the variables. By
            explicitly setting the depth, this module will only go as deep as
            the depth.
        :param files_matching:
            Limit the files that are loaded within any directory to this
            regular expression.
        :param ignore_files:
            List of file names to ignore.
        :param extensions:
            List of file extensions to read when using `dir`.
        :param ignore_unknown_extensions:
            Ignore unknown file extensions within the directory.
            This allows users to specify a directory containing vars files
            that are intermingled with non-vars files extension types (e.g. a
            directory with a README in it and vars files).
        :param hash_behaviour:
            If set to `merge`, merges existing hash variables instead of
            overwriting them.
            If omitted (`null`), the behavior falls back to the global
            `hash_behaviour` configuration.
            This option is self-contained and does not apply to individual
            files in `dir`. You can use a loop to apply `hash_behaviour` per
            file.
            Requires ansible-core >= 2.12
        """
        raise AttributeError('include_vars')

    def lineinfile(
        self,
        *,
        path: StrPath,
        regexp: str = _Unknown,
        search_string: str = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        line: str = _Unknown,
        backrefs: bool = False,
        insertafter: str = 'EOF',
        insertbefore: str = _Unknown,
        create: bool = False,
        backup: bool = False,
        firstmatch: bool = False,
    ) -> LineinfileResults:
        """
        Manage lines in text files.

        :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as `dest`,
            `destfile` and `name`.
        :param regexp:
            The regular expression to look for in every line of the file.
            For `state=present`, the pattern to replace if found. Only the
            last line found will be replaced.
            For `state=absent`, the pattern of the line(s) to remove.
            If the regular expression is not matched, the line will be added
            to the file in keeping with `insertbefore` or `insertafter`
            settings.
            When modifying a line the regexp should typically match both the
            initial state of the line as well as its state after replacement
            by `line` to ensure idempotence.
            Uses Python regular expressions. See `reference
            <https://docs.python.org/3/library/re.html>`__.
        :param search_string:
            The literal string to look for in every line of the file. This
            does not have to match the entire line.
            For `state=present`, the line to replace if the string is found in
            the file. Only the last line found will be replaced.
            For `state=absent`, the line(s) to remove if the string is in the
            line.
            If the literal expression is not matched, the line will be added
            to the file in keeping with `insertbefore` or `insertafter`
            settings.
            Mutually exclusive with `backrefs` and `regexp`.
            Requires ansible-core >= 2.11
        :param state:
            Whether the line should be there or not.
        :param line:
            The line to insert/replace into the file.
            Required for `state=present`.
            If `backrefs` is set, may contain backreferences that will get
            expanded with the `regexp` capture groups if the regexp matches.
        :param backrefs:
            Used with `state=present`.
            If set, `line` can contain backreferences (both positional and
            named) that will get populated if the `regexp` matches.
            This parameter changes the operation of the module slightly;
            `insertbefore` and `insertafter` will be ignored, and if the
            `regexp` does not match anywhere in the file, the file will be
            left unchanged.
            If the `regexp` does match, the last matching line will be
            replaced by the expanded line parameter.
            Mutually exclusive with `search_string`.
        :param insertafter:
            Used with `state=present`.
            If specified, the line will be inserted after the last match of
            specified regular expression.
            If the first match is required, use(firstmatch=yes).
            A special value is available; `EOF` for inserting the line at the
            end of the file.
            If specified regular expression has no matches, EOF will be used
            instead.
            If `insertbefore` is set, default value `EOF` will be ignored.
            If regular expressions are passed to both `regexp` and
            `insertafter`, `insertafter` is only honored if no match for
            `regexp` is found.
            May not be used with `backrefs` or `insertbefore`.
        :param insertbefore:
            Used with `state=present`.
            If specified, the line will be inserted before the last match of
            specified regular expression.
            If the first match is required, use `firstmatch=yes`.
            A value is available; `BOF` for inserting the line at the
            beginning of the file.
            If specified regular expression has no matches, the line will be
            inserted at the end of the file.
            If regular expressions are passed to both `regexp` and
            `insertbefore`, `insertbefore` is only honored if no match for
            `regexp` is found.
            May not be used with `backrefs` or `insertafter`.
        :param create:
            Used with `state=present`.
            If specified, the file will be created if it does not already
            exist.
            By default it will fail if the file is missing.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param firstmatch:
            Used with `insertafter` or `insertbefore`.
            If set, `insertafter` and `insertbefore` will work with the first
            line that matches the given regular expression.
        """
        raise AttributeError('lineinfile')

    def package_facts(
        self,
        *,
        manager: NotSupported = _Unknown,
        strategy: Literal['first', 'all'] = 'first',
    ) -> PackageFactsResults:
        """
        Package information as facts.

        :param manager:
            The package manager used by the system so we can query the package
            information.
            Since 2.8 this is a list and can support multiple package managers
            per system.
            The 'portage' and 'pkg' options were added in version 2.8.
            The 'apk' option was added in version 2.11.
            The 'pkg_info' option was added in version 2.13.
        :param strategy:
            This option controls how the module queries the package managers
            on the system. `first` means it will return only information for
            the first supported package manager available. `all` will return
            information for all supported and available package managers on
            the system.
        """
        raise AttributeError('package_facts')

    def pause(
        self,
        *,
        minutes: str = _Unknown,
        seconds: str = _Unknown,
        prompt: str = _Unknown,
        echo: bool = True,
    ) -> PauseResults:
        """
        Pause playbook execution.

        :param minutes:
            A positive number of minutes to pause for.
        :param seconds:
            A positive number of seconds to pause for.
        :param prompt:
            Optional text to use for the prompt message.
            User input is only returned if `seconds=None` and `minutes=None`,
            otherwise this is just a custom message before playbook execution
            is paused.
        :param echo:
            Controls whether or not keyboard input is shown when typing.
            Only has effect if `seconds=None` and `minutes=None`.
        """
        raise AttributeError('pause')

    def ping(
        self,
        *,
        data: str = 'pong',
    ) -> PingResults:
        """
        Try to connect to host, verify a usable python and return `pong` on
        success.

        :param data:
            Data to return for the R`ping` return value.
            If this parameter is set to `crash`, the module will cause an
            exception.
        """
        raise AttributeError('ping')

    def pip(
        self,
        *,
        name: NotSupported = _Unknown,
        version: str = _Unknown,
        requirements: str = _Unknown,
        virtualenv: StrPath = _Unknown,
        virtualenv_site_packages: bool = False,
        virtualenv_command: StrPath = 'virtualenv',
        virtualenv_python: str = _Unknown,
        state: Literal[
            'absent',
            'forcereinstall',
            'latest',
            'present',
        ] = 'present',
        extra_args: str = _Unknown,
        editable: bool = False,
        chdir: StrPath = _Unknown,
        executable: StrPath = _Unknown,
        umask: str = _Unknown,
        break_system_packages: bool = False,
    ) -> PipResults:
        """
        Manages Python library dependencies.

        :param name:
            The name of a Python library to install or the
            url(bzr+,hg+,git+,svn+) of the remote package.
            This can be a list (since 2.2) and contain version specifiers
            (since 2.7).
        :param version:
            The version number to install of the Python library specified in
            the `name` parameter.
        :param requirements:
            The path to a pip requirements file, which should be local to the
            remote system. File can be specified as a relative path if using
            the chdir option.
        :param virtualenv:
            An optional path to a *virtualenv* directory to install into. It
            cannot be specified together with the 'executable' parameter
            (added in 2.1). If the virtualenv does not exist, it will be
            created before installing packages. The optional
            virtualenv_site_packages, virtualenv_command, and
            virtualenv_python options affect the creation of the virtualenv.
        :param virtualenv_site_packages:
            Whether the virtual environment will inherit packages from the
            global site-packages directory.  Note that if this setting is
            changed on an already existing virtual environment it will not
            have any effect, the environment must be deleted and newly created.
        :param virtualenv_command:
            The command or a pathname to the command to create the virtual
            environment with. For example `pyvenv`, `virtualenv`,
            `virtualenv2`, `~/bin/virtualenv`, `/usr/local/bin/virtualenv`.
        :param virtualenv_python:
            The Python executable used for creating the virtual environment.
            For example `python3.12`, `python2.7`. When not specified, the
            Python version used to run the ansible module is used. This
            parameter should not be used when `virtualenv_command` is using
            `pyvenv` or the `-m venv` module.
        :param state:
            The state of module.
            The 'forcereinstall' option is only available in Ansible 2.1 and
            above.
        :param extra_args:
            Extra arguments passed to pip.
        :param editable:
            Pass the editable flag.
        :param chdir:
            cd into this directory before running the command.
        :param executable:
            The explicit executable or pathname for the pip executable, if
            different from the Ansible Python interpreter. For example
            `pip3.3`, if there are both Python 2.7 and 3.3 installations in
            the system and you want to run pip for the Python 3.3 installation.
            Mutually exclusive with `virtualenv` (added in 2.1).
            Does not affect the Ansible Python interpreter.
            The setuptools package must be installed for both the Ansible
            Python interpreter and for the version of Python specified by this
            option.
        :param umask:
            The system umask to apply before installing the pip package. This
            is useful, for example, when installing on systems that have a
            very restrictive umask by default (e.g., "0077") and you want to
            pip install packages which are to be used by all users. Note that
            this requires you to specify desired umask mode as an octal
            string, (e.g., "0022").
        :param break_system_packages:
            Allow pip to modify an externally-managed Python installation as
            defined by PEP 668.
            This is typically required when installing packages outside a
            virtual environment on modern systems.
            Requires ansible-core >= 2.17
        """
        raise AttributeError('pip')

    def reboot(
        self,
        *,
        pre_reboot_delay: int = 0,
        post_reboot_delay: int = 0,
        reboot_timeout: int = 600,
        connect_timeout: int = _Unknown,
        test_command: str = 'whoami',
        msg: str = _Unknown,
        search_paths: NotSupported = _Unknown,
        boot_time_command: str = _Unknown,
        reboot_command: str = _Unknown,
    ) -> RebootResults:
        """
        Reboot a machine.

        :param pre_reboot_delay:
            Seconds to wait before reboot. Passed as a parameter to the reboot
            command.
            On Linux, macOS and OpenBSD, this is converted to minutes and
            rounded down. If less than 60, it will be set to 0.
            On Solaris and FreeBSD, this will be seconds.
        :param post_reboot_delay:
            Seconds to wait after the reboot command was successful before
            attempting to validate the system rebooted successfully.
            This is useful if you want wait for something to settle despite
            your connection already working.
        :param reboot_timeout:
            Maximum seconds to wait for machine to reboot and respond to a
            test command.
            This timeout is evaluated separately for both reboot verification
            and test command success so the maximum execution time for the
            module is twice this amount.
        :param connect_timeout:
            Maximum seconds to wait for a successful connection to the managed
            hosts before trying again.
            If unspecified, the default setting for the underlying connection
            plugin is used.
        :param test_command:
            Command to run on the rebooted host and expect success from to
            determine the machine is ready for further tasks.
        :param msg:
            Message to display to users before reboot.
        :param search_paths:
            Paths to search on the remote machine for the `shutdown` command.
            *Only* these paths will be searched for the `shutdown` command.
            `PATH` is ignored in the remote node when searching for the
            `shutdown` command.
        :param boot_time_command:
            Command to run that returns a unique string indicating the last
            time the system was booted.
            Setting this to a command that has different output each time it
            is run will cause the task to fail.
            Requires ansible-core >= 2.10
        :param reboot_command:
            Command to run that reboots the system, including any parameters
            passed to the command.
            Can be an absolute path to the command or just the command name.
            If an absolute path to the command is not given, `search_paths` on
            the target system will be searched to find the absolute path.
            This will cause `pre_reboot_delay`, `post_reboot_delay`, and `msg`
            to be ignored.
            Requires ansible-core >= 2.11
        """
        raise AttributeError('reboot')

    def replace(
        self,
        *,
        path: StrPath,
        regexp: str,
        replace: str = '',
        after: str = _Unknown,
        before: str = _Unknown,
        backup: bool = False,
        others: str = _Unknown,
        encoding: str = 'utf-8',
    ) -> ReplaceResults:
        """
        Replace all instances of a particular string in a file using a
        back-referenced regular expression.

        :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as `dest`,
            `destfile` and `name`.
        :param regexp:
            The regular expression to look for in the contents of the file.
            Uses Python regular expressions; see `reference
            <https://docs.python.org/3/library/re.html>`__.
            Uses MULTILINE mode, which means `^` and `$` match the beginning
            and end of the file, as well as the beginning and end respectively
            of *each line* of the file.
            Does not use DOTALL, which means the `.` special character matches
            any character *except newlines*. A common mistake is to assume
            that a negated character set like `[^#]` will also not match
            newlines.
            In order to exclude newlines, they must be added to the set like
            `[^#\\n]`.
            Note that, as of Ansible 2.0, short form tasks should have any
            escape sequences backslash-escaped in order to prevent them being
            parsed as string literal escapes. See the examples.
        :param replace:
            The string to replace regexp matches.
            May contain backreferences that will get expanded with the regexp
            capture groups if the regexp matches.
            If not set, matches are removed entirely.
            Backreferences can be used ambiguously like `\\1`, or explicitly
            like `\\g<1>`.
        :param after:
            If specified, only content after this match will be
            replaced/removed.
            Can be used in combination with `before`.
            Uses Python regular expressions; see `reference
            <https://docs.python.org/3/library/re.html>`__.
            Uses DOTALL, which means the `.` special character *can match
            newlines*.
            Does not use MULTILINE, so `^` and `$` will only match the
            beginning and end of the file.
        :param before:
            If specified, only content before this match will be
            replaced/removed.
            Can be used in combination with `after`.
            Uses Python regular expressions; see `reference
            <https://docs.python.org/3/library/re.html>`__.
            Uses DOTALL, which means the `.` special character *can match
            newlines*.
            Does not use MULTILINE, so `^` and `$` will only match the
            beginning and end of the file.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param others:
            All arguments accepted by the :meth:`ansible.builtin.file` module
            also work here.
        :param encoding:
            The character encoding for reading and writing the file.
        """
        raise AttributeError('replace')

    def rpm_key(
        self,
        *,
        key: str,
        state: Literal['absent', 'present'] = 'present',
        validate_certs: bool = True,
        fingerprint: str = _Unknown,
    ) -> RpmKeyResults:
        """
        Adds or removes a gpg key from the rpm db.

        :param key:
            Key that will be modified. Can be a url, a file on the managed
            node, or a keyid if the key already exists in the database.
        :param state:
            If the key will be imported or removed from the rpm db.
        :param validate_certs:
            If `false` and the `key` is a url starting with `https`, SSL
            certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param fingerprint:
            The long-form fingerprint of the key being imported.
            This will be used to verify the specified key.
            Requires ansible-core >= 2.9
        """
        raise AttributeError('rpm_key')

    def service(
        self,
        *,
        name: str,
        state: Literal[
            'reloaded',
            'restarted',
            'started',
            'stopped',
        ] = _Unknown,
        sleep: int = _Unknown,
        pattern: str = _Unknown,
        enabled: bool = _Unknown,
        runlevel: str = 'default',
        arguments: str = '',
        use: str = 'auto',
    ) -> ServiceResults:
        """
        Manage services.

        :param name:
            Name of the service.
        :param state:
            `started`/`stopped` are idempotent actions that will not run
            commands unless necessary.
            `restarted` will always bounce the service.
            `reloaded` will always reload.
            **At least one of state and enabled are required.**.
            Note that reloaded will start the service if it is not already
            started, even if your chosen init system wouldn't normally.
        :param sleep:
            If the service is being `restarted` then sleep this many seconds
            between the stop and start command.
            This helps to work around badly-behaving init scripts that exit
            immediately after signaling a process to stop.
            Not all service managers support sleep, i.e when using systemd
            this setting will be ignored.
        :param pattern:
            If the service does not respond to the status command, name a
            substring to look for as would be found in the output of the *ps*
            command as a stand-in for a status result.
            If the string is found, the service will be assumed to be started.
            While using remote hosts with systemd this setting will be ignored.
        :param enabled:
            Whether the service should start on boot.
            **At least one of state and enabled are required.**.
        :param runlevel:
            For OpenRC init scripts (e.g. Gentoo) only.
            The runlevel that this service belongs to.
            While using remote hosts with systemd this setting will be ignored.
        :param arguments:
            Additional arguments provided on the command line.
            While using remote hosts with systemd this setting will be ignored.
        :param use:
            The service module actually uses system specific modules, normally
            through auto detection, this setting can force a specific module.
            Normally it uses the value of the 'ansible_service_mgr' fact and
            falls back to the old 'service' module when none matching is found.
            The 'old service module' still uses autodetection and in no way
            does it correspond to the `service` command.
        """
        raise AttributeError('service')

    def service_facts(self) -> ServiceFactsResults:
        """
        Return service state information as fact data.
        """
        raise AttributeError('service_facts')

    @overload
    def shell(
        self,
        *,
        cmd: str = _Unknown,
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        chdir: StrPath = _Unknown,
        executable: StrPath = _Unknown,
        stdin: str = _Unknown,
        stdin_add_newline: bool = True,
    ) -> ShellResults: ...

    @overload
    def shell(self, arg: str, /) -> ShellResults: ...

    def shell(self, *args: Any, **kwargs: Any) -> ShellResults:
        """
        Execute shell commands on targets.

        :param cmd:
            The command to run followed by optional arguments.
        :param creates:
            A filename, when it already exists, this step will **not** be run.
        :param removes:
            A filename, when it does not exist, this step will **not** be run.
        :param chdir:
            Change into this directory before running the command.
        :param executable:
            Change the shell used to execute the command.
            This expects an absolute path to the executable.
        :param stdin:
            Set the stdin of the command directly to the specified value.
        :param stdin_add_newline:
            Whether to append a newline to stdin data.
        """
        raise AttributeError('shell')

    def slurp(
        self,
        *,
        src: StrPath,
    ) -> SlurpResults:
        """
        Slurps a file from remote nodes.

        :param src:
            The file on the remote system to fetch. This *must* be a file, not
            a directory.
        """
        raise AttributeError('slurp')

    def stat(
        self,
        *,
        path: StrPath,
        follow: bool = False,
        get_checksum: bool = True,
        checksum_algorithm: Literal[
            'md5',
            'sha1',
            'sha224',
            'sha256',
            'sha384',
            'sha512',
        ] = 'sha1',
        get_mime: bool = True,
        get_attributes: bool = True,
    ) -> StatResults:
        """
        Retrieve file or file system status.

        :param path:
            The full path of the file/object to get the facts of.
        :param follow:
            Whether to follow symlinks.
        :param get_checksum:
            Whether to return a checksum of the file.
        :param checksum_algorithm:
            Algorithm to determine checksum of file.
            Will throw an error if the host is unable to use specified
            algorithm.
            The remote host has to support the hashing method specified, `md5`
            can be unavailable if the host is FIPS-140 compliant.
        :param get_mime:
            Use file magic and return data about the nature of the file. this
            uses the 'file' utility found on most Linux/Unix systems.
            This will add both R`stat.mimetype` and R`stat.charset` fields to
            the return, if possible.
            In Ansible 2.3 this option changed from `mime` to `get_mime` and
            the default changed to `true`.
        :param get_attributes:
            Get file attributes using lsattr tool if present.
        """
        raise AttributeError('stat')

    def subversion(
        self,
        *,
        repo: str,
        dest: StrPath = _Unknown,
        revision: str = 'HEAD',
        force: bool = False,
        in_place: bool = False,
        username: str = _Unknown,
        password: str = _Unknown,
        executable: StrPath = _Unknown,
        checkout: bool = True,
        update: bool = True,
        export: bool = False,
        switch: bool = True,
        validate_certs: bool = False,
    ) -> SubversionResults:
        """
        Deploys a subversion repository.

        :param repo:
            The subversion URL to the repository.
        :param dest:
            Absolute path where the repository should be deployed.
            The destination directory must be specified unless `checkout=no`,
            `update=no`, and `export=no`.
        :param revision:
            Specific revision to checkout.
        :param force:
            If `true`, modified files will be discarded. If `false`, module
            will fail if it encounters modified files. Prior to 1.9 the
            default was `true`.
        :param in_place:
            If the directory exists, then the working copy will be checked-out
            over-the-top using svn checkout --force; if force is specified
            then existing files with different content are reverted.
        :param username:
            `--username` parameter passed to svn.
        :param password:
            `--password` parameter passed to svn when svn is less than version
            1.10.0. This is not secure and the password will be leaked to argv.
            `--password-from-stdin` parameter when svn is greater or equal to
            version 1.10.0.
        :param executable:
            Path to svn executable to use. If not supplied, the normal
            mechanism for resolving binary paths will be used.
        :param checkout:
            If `false`, do not check out the repository if it does not exist
            locally.
        :param update:
            If `false`, do not retrieve new revisions from the origin
            repository.
        :param export:
            If `true`, do export instead of checkout/update.
        :param switch:
            If `false`, do not call svn switch before update.
        :param validate_certs:
            If `false`, passes the `--trust-server-cert` flag to svn.
            If `true`, does not pass the flag.
            Requires ansible-core >= 2.11
        """
        raise AttributeError('subversion')

    def systemd(
        self,
        *,
        name: str = _Unknown,
        state: Literal[
            'reloaded',
            'restarted',
            'started',
            'stopped',
        ] = _Unknown,
        enabled: bool = _Unknown,
        force: bool = _Unknown,
        masked: bool = _Unknown,
        daemon_reload: bool = False,
        daemon_reexec: bool = False,
        scope: Literal['system', 'user', 'global'] = 'system',
        no_block: bool = False,
    ) -> SystemdResults:
        """
        Manage systemd units.

        :param name:
            Name of the unit. This parameter takes the name of exactly one
            unit to work with.
            When no extension is given, it is implied to a `.service` as
            systemd.
            When using in a chroot environment you always need to specify the
            name of the unit with the extension. For example, `crond.service`.
        :param state:
            `started`/`stopped` are idempotent actions that will not run
            commands unless necessary. `restarted` will always bounce the
            unit. `reloaded` will always reload and if the service is not
            running at the moment of the reload, it is started.
            If set, requires `name`.
        :param enabled:
            Whether the unit should start on boot. **At least one of state and
            enabled are required.**.
            If set, requires `name`.
        :param force:
            Whether to override existing symlinks.
        :param masked:
            Whether the unit should be masked or not. A masked unit is
            impossible to start.
            If set, requires `name`.
        :param daemon_reload:
            Run daemon-reload before doing any other operations, to make sure
            systemd has read any changes.
            When set to `true`, runs daemon-reload even if the module does not
            start or stop anything.
        :param daemon_reexec:
            Run daemon_reexec command before doing any other operations, the
            systemd manager will serialize the manager state.
        :param scope:
            Run systemctl within a given service manager scope, either as the
            default system scope `system`, the current user's scope `user`, or
            the scope of all users `global`.
            For systemd to work with 'user', the executing user must have its
            own instance of dbus started and accessible (systemd requirement).
            The user dbus process is normally started during normal login, but
            not during the run of Ansible tasks. Otherwise you will probably
            get a 'Failed to connect to bus: no such file or directory' error.
            The user must have access, normally given via setting the
            `XDG_RUNTIME_DIR` variable, see the example below.
        :param no_block:
            Do not synchronously wait for the requested operation to finish.
            Enqueued job will continue without Ansible blocking on its
            completion.
        """
        raise AttributeError('systemd')

    def systemd_service(
        self,
        *,
        name: str = _Unknown,
        state: Literal[
            'reloaded',
            'restarted',
            'started',
            'stopped',
        ] = _Unknown,
        enabled: bool = _Unknown,
        force: bool = _Unknown,
        masked: bool = _Unknown,
        daemon_reload: bool = False,
        daemon_reexec: bool = False,
        scope: Literal['system', 'user', 'global'] = 'system',
        no_block: bool = False,
    ) -> SystemdServiceResults:
        """
        Manage systemd units.

        :param name:
            Name of the unit. This parameter takes the name of exactly one
            unit to work with.
            When no extension is given, it is implied to a `.service` as
            systemd.
            When using in a chroot environment you always need to specify the
            name of the unit with the extension. For example, `crond.service`.
        :param state:
            `started`/`stopped` are idempotent actions that will not run
            commands unless necessary. `restarted` will always bounce the
            unit. `reloaded` will always reload and if the service is not
            running at the moment of the reload, it is started.
            If set, requires `name`.
        :param enabled:
            Whether the unit should start on boot. **At least one of state and
            enabled are required.**.
            If set, requires `name`.
        :param force:
            Whether to override existing symlinks.
        :param masked:
            Whether the unit should be masked or not. A masked unit is
            impossible to start.
            If set, requires `name`.
        :param daemon_reload:
            Run daemon-reload before doing any other operations, to make sure
            systemd has read any changes.
            When set to `true`, runs daemon-reload even if the module does not
            start or stop anything.
        :param daemon_reexec:
            Run daemon_reexec command before doing any other operations, the
            systemd manager will serialize the manager state.
        :param scope:
            Run systemctl within a given service manager scope, either as the
            default system scope `system`, the current user's scope `user`, or
            the scope of all users `global`.
            For systemd to work with 'user', the executing user must have its
            own instance of dbus started and accessible (systemd requirement).
            The user dbus process is normally started during normal login, but
            not during the run of Ansible tasks. Otherwise you will probably
            get a 'Failed to connect to bus: no such file or directory' error.
            The user must have access, normally given via setting the
            `XDG_RUNTIME_DIR` variable, see the example below.
        :param no_block:
            Do not synchronously wait for the requested operation to finish.
            Enqueued job will continue without Ansible blocking on its
            completion.
        """
        raise AttributeError('systemd_service')

    def sysvinit(
        self,
        *,
        name: str,
        state: Literal[
            'started',
            'stopped',
            'restarted',
            'reloaded',
        ] = _Unknown,
        enabled: bool = _Unknown,
        sleep: int = 1,
        pattern: str = _Unknown,
        runlevels: NotSupported = _Unknown,
        arguments: str = _Unknown,
        daemonize: bool = False,
    ) -> SysvinitResults:
        """
        Manage SysV services.

        :param name:
            Name of the service.
        :param state:
            `started`/`stopped` are idempotent actions that will not run
            commands unless necessary. Not all init scripts support
            `restarted` nor `reloaded` natively, so these will both trigger a
            stop and start as needed.
        :param enabled:
            Whether the service should start on boot. **At least one of state
            and enabled are required.**.
        :param sleep:
            If the service is being `restarted` or `reloaded` then sleep this
            many seconds between the stop and start command. This helps to
            workaround badly behaving services.
        :param pattern:
            A substring to look for as would be found in the output of the
            *ps* command as a stand-in for a status result.
            If the string is found, the service will be assumed to be running.
            This option is mainly for use with init scripts that don't support
            the 'status' option.
        :param runlevels:
            The runlevels this script should be enabled/disabled from.
            Use this to override the defaults set by the package or init
            script itself.
        :param arguments:
            Additional arguments provided on the command line that some init
            scripts accept.
        :param daemonize:
            Have the module daemonize as the service itself might not do so
            properly.
            This is useful with badly written init scripts or daemons, which
            commonly manifests as the task hanging as it is still holding the
            tty or the service dying when the task is over as the connection
            closes the session.
        """
        raise AttributeError('sysvinit')

    def tempfile(
        self,
        *,
        state: Literal['directory', 'file'] = 'file',
        path: StrPath = _Unknown,
        prefix: str = 'ansible.',
        suffix: str = '',
    ) -> TempfileResults:
        """
        Creates temporary files and directories.

        :param state:
            Whether to create file or directory.
        :param path:
            Location where temporary file or directory should be created.
            If path is not specified, the default system temporary directory
            will be used.
        :param prefix:
            Prefix of file/directory name created by module.
        :param suffix:
            Suffix of file/directory name created by module.
        """
        raise AttributeError('tempfile')

    def template(
        self,
        *,
        follow: bool = False,
    ) -> TemplateResults:
        """
        Template a file out to a target host.

        :param follow:
            Determine whether symbolic links should be followed.
            When set to `true` symbolic links will be followed, if they exist.
            When set to `false` symbolic links will not be followed.
            Previous to Ansible 2.4, this was hardcoded as `true`.
        """
        raise AttributeError('template')

    def unarchive(
        self,
        *,
        src: StrPath,
        dest: StrPath,
        copy: bool = True,
        creates: StrPath = _Unknown,
        io_buffer_size: int = 65536,
        list_files: bool = False,
        exclude: NotSupported = _Unknown,
        include: NotSupported = _Unknown,
        keep_newer: bool = False,
        extra_opts: NotSupported = _Unknown,
        remote_src: bool = False,
        validate_certs: bool = True,
    ) -> UnarchiveResults:
        """
        Unpacks an archive after (optionally) copying it from the local
        machine.

        :param src:
            If `remote_src=no` (default), local path to archive file to copy
            to the target server; can be absolute or relative. If
            `remote_src=yes`, path on the target server to existing archive
            file to unpack.
            If `remote_src=yes` and `src` contains `://`, the remote machine
            will download the file from the URL first. (version_added 2.0).
            This is only for simple cases, for full download support use the
            :meth:`ansible.builtin.get_url` module.
        :param dest:
            Remote absolute path where the archive should be unpacked.
            The given path must exist. Base directory is not created by this
            module.
        :param copy:
            If true, the file is copied from local controller to the managed
            (remote) node, otherwise, the plugin will look for src archive on
            the managed machine.
            This option has been deprecated in favor of `remote_src`.
            This option is mutually exclusive with `remote_src`.
        :param creates:
            If the specified absolute path (file or directory) already exists,
            this step will **not** be run.
            The specified absolute path (file or directory) must be below the
            base path given with `dest`.
        :param io_buffer_size:
            Size of the volatile memory buffer that is used for extracting
            files from the archive in bytes.
            Requires ansible-core >= 2.12
        :param list_files:
            If set to True, return the list of files that are contained in the
            tarball.
        :param exclude:
            List the directory and file entries that you would like to exclude
            from the unarchive action.
            Mutually exclusive with `include`.
        :param include:
            List of directory and file entries that you would like to extract
            from the archive. If `include` is not empty, only files listed
            here will be extracted.
            Mutually exclusive with `exclude`.
            Requires ansible-core >= 2.11
        :param keep_newer:
            Do not replace existing files that are newer than files from the
            archive.
        :param extra_opts:
            Specify additional options by passing in an array.
            Each space-separated command-line option should be a new element
            of the array. See examples.
            Command-line options with multiple elements must use multiple
            lines in the array, one for each element.
        :param remote_src:
            Set to `true` to indicate the archived file is already on the
            remote system and not local to the Ansible controller.
            This option is mutually exclusive with `copy`.
        :param validate_certs:
            This only applies if using a https URL as the source of the file.
            This should only set to `false` used on personally controlled
            sites using self-signed certificate.
            Prior to 2.2 the code worked as if this was set to `true`.
        """
        raise AttributeError('unarchive')

    def uri(
        self,
        *,
        ciphers: NotSupported = _Unknown,
        decompress: bool = True,
        url: str,
        dest: StrPath = _Unknown,
        url_username: str = _Unknown,
        url_password: str = _Unknown,
        body: str = _Unknown,
        body_format: Literal[
            'form-urlencoded',
            'json',
            'raw',
            'form-multipart',
        ] = 'raw',
        method: str = 'GET',
        return_content: bool = False,
        force_basic_auth: bool = False,
        follow_redirects: Literal[
            'all',
            'none',
            'safe',
            'urllib2',
            'no',
            'yes',
        ] = 'safe',
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        status_code: NotSupported = _Unknown,
        timeout: int = 30,
        headers: NotSupported = _Unknown,
        validate_certs: bool = True,
        client_cert: StrPath = _Unknown,
        client_key: StrPath = _Unknown,
        ca_path: StrPath = _Unknown,
        src: StrPath = _Unknown,
        remote_src: bool = False,
        force: bool = False,
        use_proxy: bool = True,
        unix_socket: StrPath = _Unknown,
        http_agent: str = 'ansible-httpget',
        unredirected_headers: NotSupported = _Unknown,
        use_gssapi: bool = False,
        use_netrc: bool = True,
    ) -> UriResults:
        """
        Interacts with webservices.

        :param ciphers:
            SSL/TLS Ciphers to use for the request.
            When a list is provided, all ciphers are joined in order with `:`.
            See the `OpenSSL Cipher List Format
            <https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html#CIPHER-LIST-FORMAT>`__
            for more details.
            The available ciphers is dependent on the Python and
            OpenSSL/LibreSSL versions.
            Requires ansible-core >= 2.14
        :param decompress:
            Whether to attempt to decompress gzip content-encoded responses.
            Requires ansible-core >= 2.14
        :param url:
            HTTP or HTTPS URL in the form
            (http|https)://host.domain[:port]/path.
        :param dest:
            A path of where to download the file to (if desired). If `dest` is
            a directory, the basename of the file on the remote server will be
            used.
        :param url_username:
            A username for the module to use for Digest, Basic or WSSE
            authentication.
        :param url_password:
            A password for the module to use for Digest, Basic or WSSE
            authentication.
        :param body:
            The body of the http request/response to the web service. If
            `body_format` is set to `json` it will take an already formatted
            JSON string or convert a data structure into JSON.
            If `body_format` is set to `form-urlencoded` it will convert a
            dictionary or list of tuples into an
            'application/x-www-form-urlencoded' string. (Added in v2.7).
            If `body_format` is set to `form-multipart` it will convert a
            dictionary into 'multipart/form-multipart' body. (Added in v2.10).
        :param body_format:
            The serialization format of the body. When set to `json`,
            `form-multipart`, or `form-urlencoded`, encodes the body argument,
            if needed, and automatically sets the Content-Type header
            accordingly.
            As of v2.3 it is possible to override the `Content-Type` header,
            when set to `json` or `form-urlencoded` via the `headers` option.
            The 'Content-Type' header cannot be overridden when using
            `form-multipart`.
            `form-urlencoded` was added in v2.7.
            `form-multipart` was added in v2.10.
        :param method:
            The HTTP method of the request or response.
            In more recent versions we do not restrict the method at the
            module level anymore but it still must be a valid method accepted
            by the service handling the request.
        :param return_content:
            Whether or not to return the body of the response as a "content"
            key in the dictionary result no matter it succeeded or failed.
            Independently of this option, if the reported Content-type is
            "application/json", then the JSON is always loaded into a key
            called R`ignore:json` in the dictionary results.
        :param force_basic_auth:
            Force the sending of the Basic authentication header upon initial
            request.
            When this setting is `false`, this module will first try an
            unauthenticated request, and when the server replies with an `HTTP
            401` error, it will submit the Basic authentication header.
            When this setting is `true`, this module will immediately send a
            Basic authentication header on the first request.
            Use this setting in any of the following scenarios:.
            You know the webservice endpoint always requires HTTP Basic
            authentication, and you want to speed up your requests by
            eliminating the first roundtrip.
            The web service does not properly send an HTTP 401 error to your
            client, so Ansible's HTTP library will not properly respond with
            HTTP credentials, and logins will fail.
            The webservice bans or rate-limits clients that cause any HTTP 401
            errors.
        :param follow_redirects:
            Whether or not the URI module should follow redirects.
        :param creates:
            A filename, when it already exists, this step will not be run.
        :param removes:
            A filename, when it does not exist, this step will not be run.
        :param status_code:
            A list of valid, numeric, HTTP status codes that signifies success
            of the request.
        :param timeout:
            The socket level timeout in seconds.
        :param headers:
            Add custom HTTP headers to a request in the format of a YAML hash.
            As of Ansible 2.3 supplying `Content-Type` here will override the
            header generated by supplying `json` or `form-urlencoded` for
            `body_format`.
        :param validate_certs:
            If `false`, SSL certificates will not be validated.
            This should only set to `false` used on personally controlled
            sites using self-signed certificates.
            Prior to 1.9.2 the code defaulted to `false`.
        :param client_cert:
            PEM formatted certificate chain file to be used for SSL client
            authentication.
            This file can also include the key as well, and if the key is
            included, `client_key` is not required.
        :param client_key:
            PEM formatted file that contains your private key to be used for
            SSL client authentication.
            If `client_cert` contains both the certificate and key, this
            option is not required.
        :param ca_path:
            PEM formatted file that contains a CA certificate to be used for
            validation.
            Requires ansible-core >= 2.11
        :param src:
            Path to file to be submitted to the remote server.
            Cannot be used with `body`.
            Should be used with `force_basic_auth` to ensure success when the
            remote end sends a 401.
        :param remote_src:
            If `false`, the module will search for the `src` on the controller
            node.
            If `true`, the module will search for the `src` on the managed
            (remote) node.
        :param force:
            If `true` do not get a cached copy.
        :param use_proxy:
            If `false`, it will not use a proxy, even if one is defined in an
            environment variable on the target hosts.
        :param unix_socket:
            Path to Unix domain socket to use for connection.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
        :param unredirected_headers:
            A list of header names that will not be sent on subsequent
            redirected requests. This list is case insensitive. By default all
            headers will be redirected. In some cases it may be beneficial to
            list headers such as `Authorization` here to avoid potential
            credential exposure.
            Requires ansible-core >= 2.12
        :param use_gssapi:
            Use GSSAPI to perform the authentication, typically this is for
            Kerberos or Kerberos through Negotiate authentication.
            Requires the Python library `gssapi
            <https://github.com/pythongssapi/python-gssapi>`__ to be installed.
            Credentials for GSSAPI can be specified with
            `url_username`/`url_password` or with the GSSAPI env var
            `KRB5CCNAME` that specified a custom Kerberos credential cache.
            NTLM authentication is **not** supported even if the GSSAPI mech
            for NTLM has been installed.
            Requires ansible-core >= 2.11
        :param use_netrc:
            Determining whether to use credentials from ``~/.netrc`` file.
            By default .netrc is used with Basic authentication headers.
            When set to False, .netrc credentials are ignored.
            Requires ansible-core >= 2.14
        """  # noqa: E501
        raise AttributeError('uri')

    def user(
        self,
        *,
        name: str,
        uid: int = _Unknown,
        comment: str = _Unknown,
        hidden: bool = _Unknown,
        non_unique: bool = False,
        seuser: str = _Unknown,
        group: str = _Unknown,
        groups: NotSupported = _Unknown,
        append: bool = False,
        shell: str = _Unknown,
        home: StrPath = _Unknown,
        skeleton: str = _Unknown,
        password: str = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        create_home: bool = True,
        move_home: bool = False,
        system: bool = False,
        force: bool = False,
        remove: bool = False,
        login_class: str = _Unknown,
        generate_ssh_key: bool = False,
        ssh_key_bits: int = _Unknown,
        ssh_key_type: str = 'rsa',
        ssh_key_file: StrPath = _Unknown,
        ssh_key_comment: str = _Unknown,
        ssh_key_passphrase: str = _Unknown,
        update_password: Literal['always', 'on_create'] = 'always',
        expires: Incomplete = _Unknown,
        password_lock: bool = _Unknown,
        local: bool = False,
        profile: str = _Unknown,
        authorization: str = _Unknown,
        role: str = _Unknown,
        password_expire_max: int = _Unknown,
        password_expire_min: int = _Unknown,
        password_expire_warn: int = _Unknown,
        umask: str = _Unknown,
    ) -> UserResults:
        """
        Manage user accounts.

        :param name:
            Name of the user to create, remove or modify.
        :param uid:
            Optionally sets the *UID* of the user.
        :param comment:
            Optionally sets the description (aka *GECOS*) of user account.
            On macOS, this defaults to the `name` option.
        :param hidden:
            macOS only, optionally hide the user from the login window and
            system preferences.
            The default will be `true` if the `system` option is used.
        :param non_unique:
            Optionally when used with the -u option, this option allows to
            change the user ID to a non-unique value.
        :param seuser:
            Optionally sets the seuser type (user_u) on selinux enabled
            systems.
        :param group:
            Optionally sets the user's primary group (takes a group name).
            On macOS, this defaults to `'staff'`.
        :param groups:
            A list of supplementary groups which the user is also a member of.
            By default, the user is removed from all other groups. Configure
            `append` to modify this.
            When set to an empty string `''`, the user is removed from all
            groups except the primary group.
            Before Ansible 2.3, the only input format allowed was a comma
            separated string.
        :param append:
            If `true`, add the user to the groups specified in `groups`.
            If `false`, user will only be added to the groups specified in
            `groups`, removing them from all other groups.
        :param shell:
            Optionally set the user's shell.
            On macOS, before Ansible 2.5, the default shell for non-system
            users was `/usr/bin/false`. Since Ansible 2.5, the default shell
            for non-system users on macOS is `/bin/bash`.
            On other operating systems, the default shell is determined by the
            underlying tool invoked by this module. See Notes for a per
            platform list of invoked tools.
        :param home:
            Optionally set the user's home directory.
        :param skeleton:
            Optionally set a home skeleton directory.
            Requires `create_home` option!.
        :param password:
            If provided, set the user's password to the provided encrypted
            hash (Linux) or plain text password (macOS).
            **Linux/Unix/POSIX:** Enter the hashed password as the value.
            See `FAQ entry
            <https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module>`__
            for details on various ways to generate the hash of a password.
            To create an account with a locked/disabled password on Linux
            systems, set this to `'!'` or `'*'`.
            To create an account with a locked/disabled password on OpenBSD,
            set this to `'*************'`.
            **OS X/macOS:** Enter the cleartext password as the value. Be sure
            to take relevant security precautions.
            On macOS, the password specified in the `password` option will
            always be set, regardless of whether the user account already
            exists or not.
            When the password is passed as an argument, the `user` module will
            always return changed to `true` for macOS systems. Since macOS no
            longer provides access to the hashed passwords directly.
        :param state:
            Whether the account should exist or not, taking action if the
            state is different from what is stated.
            See this `FAQ entry
            <https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#running-on-macos-as-a-target>`__
            for additional requirements when removing users on macOS systems.
        :param create_home:
            Unless set to `false`, a home directory will be made for the user
            when the account is created or if the home directory does not
            exist.
            Changed from `createhome` to `create_home` in Ansible 2.5.
        :param move_home:
            If set to `true` when used with `home`, attempt to move the user's
            old home directory to the specified directory if it isn't there
            already and the old home exists.
        :param system:
            When creating an account `state=present`, setting this to `true`
            makes the user a system account.
            This setting cannot be changed on existing users.
        :param force:
            This only affects `state=absent`, it forces removal of the user
            and associated directories on supported platforms.
            The behavior is the same as `userdel --force`, check the man page
            for `userdel` on your system for details and support.
            When used with `generate_ssh_key=yes` this forces an existing key
            to be overwritten.
        :param remove:
            This only affects `state=absent`, it attempts to remove
            directories associated with the user.
            The behavior is the same as `userdel --remove`, check the man page
            for details and support.
        :param login_class:
            Optionally sets the user's login class, a feature of most BSD OSs.
        :param generate_ssh_key:
            Whether to generate a SSH key for the user in question.
            This will **not** overwrite an existing SSH key unless used with
            `force=yes`.
        :param ssh_key_bits:
            Optionally specify number of bits in SSH key to create.
            The default value depends on ssh-keygen.
        :param ssh_key_type:
            Optionally specify the type of SSH key to generate.
            Available SSH key types will depend on implementation present on
            target host.
        :param ssh_key_file:
            Optionally specify the SSH key filename.
            If this is a relative filename then it will be relative to the
            user's home directory.
            This parameter defaults to `.ssh/id_rsa`.
        :param ssh_key_comment:
            Optionally define the comment for the SSH key.
        :param ssh_key_passphrase:
            Set a passphrase for the SSH key.
            If no passphrase is provided, the SSH key will default to having
            no passphrase.
        :param update_password:
            `always` will update passwords if they differ.
            `on_create` will only set the password for newly created users.
        :param expires:
            An expiry time for the user in epoch, it will be ignored on
            platforms that do not support this.
            Currently supported on GNU/Linux, FreeBSD, and DragonFlyBSD.
            Since Ansible 2.6 you can remove the expiry time by specifying a
            negative value. Currently supported on GNU/Linux and FreeBSD.
        :param password_lock:
            Lock the password (`usermod -L`, `usermod -U`, `pw lock`).
            Implementation differs by platform. This option does not always
            mean the user cannot login using other methods.
            This option does not disable the user, only lock the password.
            This must be set to `False` in order to unlock a currently locked
            password. The absence of this parameter will not unlock a password.
            Currently supported on Linux, FreeBSD, DragonFlyBSD, NetBSD,
            OpenBSD.
        :param local:
            Forces the use of "local" command alternatives on platforms that
            implement it.
            This is useful in environments that use centralized authentication
            when you want to manipulate the local users (in other words, it
            uses `luseradd` instead of `useradd`).
            This will check `/etc/passwd` for an existing account before
            invoking commands. If the local account database exists somewhere
            other than `/etc/passwd`, this setting will not work properly.
            This requires that the above commands as well as `/etc/passwd`
            must exist on the target host, otherwise it will be a fatal error.
        :param profile:
            Sets the profile of the user.
            Can set multiple profiles using comma separation.
            To delete all the profiles, use `profile=''`.
            Currently supported on Illumos/Solaris. Does nothing when used
            with other platforms.
        :param authorization:
            Sets the authorization of the user.
            Can set multiple authorizations using comma separation.
            To delete all authorizations, use `authorization=''`.
            Currently supported on Illumos/Solaris. Does nothing when used
            with other platforms.
        :param role:
            Sets the role of the user.
            Can set multiple roles using comma separation.
            To delete all roles, use `role=''`.
            Currently supported on Illumos/Solaris. Does nothing when used
            with other platforms.
        :param password_expire_max:
            Maximum number of days between password change.
            Supported on Linux only.
            Requires ansible-core >= 2.11
        :param password_expire_min:
            Minimum number of days between password change.
            Supported on Linux only.
            Requires ansible-core >= 2.11
        :param password_expire_warn:
            Number of days of warning before password expires.
            Supported on Linux only.
            Requires ansible-core >= 2.16
        :param umask:
            Sets the umask of the user.
            Currently supported on Linux. Does nothing when used with other
            platforms.
            Requires `local` is omitted or `False`.
            Requires ansible-core >= 2.12
        """  # noqa: E501
        raise AttributeError('user')

    def validate_argument_spec(
        self,
        *,
        argument_spec: str,
        provided_arguments: str = _Unknown,
    ) -> ValidateArgumentSpecResults:
        """
        Validate role argument specs.

        .. note:: Requires ansible-core >= 2.11

        :param argument_spec:
            A dictionary like AnsibleModule argument_spec. See `argument spec
            definition,argument_spec`.
        :param provided_arguments:
            A dictionary of the arguments that will be validated according to
            argument_spec.
        """
        raise AttributeError('validate_argument_spec')

    def wait_for(
        self,
        *,
        host: str = '127.0.0.1',
        timeout: int = 300,
        connect_timeout: int = 5,
        delay: int = 0,
        port: int = _Unknown,
        active_connection_states: NotSupported = _Unknown,
        state: Literal[
            'absent',
            'drained',
            'present',
            'started',
            'stopped',
        ] = 'started',
        path: StrPath = _Unknown,
        search_regex: str = _Unknown,
        exclude_hosts: NotSupported = _Unknown,
        sleep: int = 1,
        msg: str = _Unknown,
    ) -> WaitForResults:
        """
        Waits for a condition before continuing.

        :param host:
            A resolvable hostname or IP address to wait for.
        :param timeout:
            Maximum number of seconds to wait for, when used with another
            condition it will force an error.
            When used without other conditions it is equivalent of just
            sleeping.
        :param connect_timeout:
            Maximum number of seconds to wait for a connection to happen
            before closing and retrying.
        :param delay:
            Number of seconds to wait before starting to poll.
        :param port:
            Port number to poll.
            `path` and `port` are mutually exclusive parameters.
        :param active_connection_states:
            The list of TCP connection states which are counted as active
            connections.
        :param state:
            Either `present`, `started`, or `stopped`, `absent`, or `drained`.
            When checking a port `started` will ensure the port is open,
            `stopped` will check that it is closed, `drained` will check for
            active connections.
            When checking for a file or a search string `present` or `started`
            will ensure that the file or string is present before continuing,
            `absent` will check that file is absent or removed.
        :param path:
            Path to a file on the filesystem that must exist before continuing.
            `path` and `port` are mutually exclusive parameters.
        :param search_regex:
            Can be used to match a string in either a file or a socket
            connection.
            Defaults to a multiline regex.
        :param exclude_hosts:
            List of hosts or IPs to ignore when looking for active TCP
            connections for `drained` state.
        :param sleep:
            Number of seconds to sleep between checks.
            Before Ansible 2.3 this was hardcoded to 1 second.
        :param msg:
            This overrides the normal error message from a failure to meet the
            required conditions.
        """
        raise AttributeError('wait_for')

    def wait_for_connection(
        self,
        *,
        connect_timeout: int = 5,
        delay: int = 0,
        sleep: int = 1,
        timeout: int = 600,
    ) -> WaitForConnectionResults:
        """
        Waits until remote system is reachable/usable.

        :param connect_timeout:
            Maximum number of seconds to wait for a connection to happen
            before closing and retrying.
        :param delay:
            Number of seconds to wait before starting to poll.
        :param sleep:
            Number of seconds to sleep between checks.
        :param timeout:
            Maximum number of seconds to wait for.
        """
        raise AttributeError('wait_for_connection')

    def yum_repository(
        self,
        *,
        async_: bool = _Unknown,
        bandwidth: str = _Unknown,
        baseurl: NotSupported = _Unknown,
        cost: str = _Unknown,
        deltarpm_metadata_percentage: str = _Unknown,
        deltarpm_percentage: str = _Unknown,
        description: str = _Unknown,
        enabled: bool = _Unknown,
        enablegroups: bool = _Unknown,
        exclude: NotSupported = _Unknown,
        failovermethod: Literal['roundrobin', 'priority'] = _Unknown,
        file: str = _Unknown,
        gpgcakey: str = _Unknown,
        gpgcheck: bool = _Unknown,
        gpgkey: NotSupported = _Unknown,
        module_hotfixes: bool = _Unknown,
        http_caching: Literal['all', 'packages', 'none'] = _Unknown,
        include: str = _Unknown,
        includepkgs: NotSupported = _Unknown,
        ip_resolve: Literal['4', '6', 'IPv4', 'IPv6', 'whatever'] = _Unknown,
        keepalive: bool = _Unknown,
        keepcache: Literal['0', '1'] = _Unknown,
        metadata_expire: str = _Unknown,
        metadata_expire_filter: Literal[
            'never',
            'read-only:past',
            'read-only:present',
            'read-only:future',
        ] = _Unknown,
        metalink: str = _Unknown,
        mirrorlist: str = _Unknown,
        mirrorlist_expire: str = _Unknown,
        name: str,
        password: str = _Unknown,
        priority: str = _Unknown,
        protect: bool = _Unknown,
        proxy: str = _Unknown,
        proxy_password: str = _Unknown,
        proxy_username: str = _Unknown,
        repo_gpgcheck: bool = _Unknown,
        reposdir: StrPath = '/etc/yum.repos.d',
        retries: str = _Unknown,
        s3_enabled: bool = _Unknown,
        skip_if_unavailable: bool = _Unknown,
        ssl_check_cert_permissions: bool = _Unknown,
        sslcacert: str = _Unknown,
        sslclientcert: str = _Unknown,
        sslclientkey: str = _Unknown,
        sslverify: bool = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        throttle: str = _Unknown,
        timeout: str = _Unknown,
        ui_repoid_vars: str = _Unknown,
        username: str = _Unknown,
    ) -> YumRepositoryResults:
        """
        Add or remove YUM repositories.

        :param async:
            If set to `true` Yum will download packages and metadata from this
            repo in parallel, if possible.
            In ansible-core 2.11, 2.12, and 2.13 the default value is `true`.
            This option has been deprecated in RHEL 8. If you're using one of
            the versions listed above, you can set this option to None to
            avoid passing an unknown configuration option.
        :param bandwidth:
            Maximum available network bandwidth in bytes/second. Used with the
            `throttle` option.
            If `throttle` is a percentage and bandwidth is `0` then bandwidth
            throttling will be disabled. If `throttle` is expressed as a data
            rate (bytes/sec) then this option is ignored. Default is `0` (no
            bandwidth throttling).
        :param baseurl:
            URL to the directory where the yum repository's 'repodata'
            directory lives.
            It can also be a list of multiple URLs.
            This, the `metalink` or `mirrorlist` parameters are required if
            `state` is set to `present`.
        :param cost:
            Relative cost of accessing this repository. Useful for weighing
            one repo's packages as greater/less than any other.
        :param deltarpm_metadata_percentage:
            When the relative size of deltarpm metadata vs pkgs is larger than
            this, deltarpm metadata is not downloaded from the repo. Note that
            you can give values over `100`, so `200` means that the metadata
            is required to be half the size of the packages. Use `0` to turn
            off this check, and always download metadata.
        :param deltarpm_percentage:
            When the relative size of delta vs pkg is larger than this, delta
            is not used. Use `0` to turn off delta rpm processing. Local
            repositories (with file://`baseurl`) have delta rpms turned off by
            default.
        :param description:
            A human-readable string describing the repository. This option
            corresponds to the "name" property in the repo file.
            This parameter is only required if `state` is set to `present`.
        :param enabled:
            This tells yum whether or not use this repository.
            Yum default value is `true`.
        :param enablegroups:
            Determines whether yum will allow the use of package groups for
            this repository.
            Yum default value is `true`.
        :param exclude:
            List of packages to exclude from updates or installs. This should
            be a space separated list. Shell globs using wildcards (for
            example `*` and `?`) are allowed.
            The list can also be a regular YAML array.
        :param failovermethod:
            `roundrobin` randomly selects a URL out of the list of URLs to
            start with and proceeds through each of them as it encounters a
            failure contacting the host.
            `priority` starts from the first `baseurl` listed and reads
            through them sequentially.
        :param file:
            File name without the `.repo` extension to save the repo in.
            Defaults to the value of `name`.
        :param gpgcakey:
            A URL pointing to the ASCII-armored CA key file for the repository.
        :param gpgcheck:
            Tells yum whether or not it should perform a GPG signature check
            on packages.
            No default setting. If the value is not set, the system setting
            from `/etc/yum.conf` or system default of `false` will be used.
        :param gpgkey:
            A URL pointing to the ASCII-armored GPG key file for the
            repository.
            It can also be a list of multiple URLs.
        :param module_hotfixes:
            Disable module RPM filtering and make all RPMs from the repository
            available. The default is `None`.
            Requires ansible-core >= 2.11
        :param http_caching:
            Determines how upstream HTTP caches are instructed to handle any
            HTTP downloads that Yum does.
            `all` means that all HTTP downloads should be cached.
            `packages` means that only RPM package downloads should be cached
            (but not repository metadata downloads).
            `none` means that no HTTP downloads should be cached.
        :param include:
            Include external configuration file. Both, local path and URL is
            supported. Configuration file will be inserted at the position of
            the `include=` line. Included files may contain further include
            lines. Yum will abort with an error if an inclusion loop is
            detected.
        :param includepkgs:
            List of packages you want to only use from a repository. This
            should be a space separated list. Shell globs using wildcards (for
            example `*` and `?`) are allowed. Substitution variables (for
            example `$releasever`) are honored here.
            The list can also be a regular YAML array.
        :param ip_resolve:
            Determines how yum resolves host names.
            `4` or `IPv4` - resolve to IPv4 addresses only.
            `6` or `IPv6` - resolve to IPv6 addresses only.
        :param keepalive:
            This tells yum whether or not HTTP/1.1 keepalive should be used
            with this repository. This can improve transfer speeds by using
            one connection when downloading multiple files from a repository.
        :param keepcache:
            Either `1` or `0`. Determines whether or not yum keeps the cache
            of headers and packages after successful installation.
            This parameter is deprecated and will be removed in version 2.20.
        :param metadata_expire:
            Time (in seconds) after which the metadata will expire.
            Default value is 6 hours.
        :param metadata_expire_filter:
            Filter the `metadata_expire` time, allowing a trade of speed for
            accuracy if a command doesn't require it. Each yum command can
            specify that it requires a certain level of timeliness quality
            from the remote repos. from "I'm about to install/upgrade, so this
            better be current" to "Anything that's available is good enough".
            `never` - Nothing is filtered, always obey `metadata_expire`.
            `read-only:past` - Commands that only care about past information
            are filtered from metadata expiring. Eg. `yum history` info (if
            history needs to lookup anything about a previous transaction,
            then by definition the remote package was available in the past).
            `read-only:present` - Commands that are balanced between past and
            future. Eg. `yum list yum`.
            `read-only:future` - Commands that are likely to result in running
            other commands which will require the latest metadata. Eg. `yum
            check-update`.
            Note that this option does not override "yum clean expire-cache".
        :param metalink:
            Specifies a URL to a metalink file for the repomd.xml, a list of
            mirrors for the entire repository are generated by converting the
            mirrors for the repomd.xml file to a `baseurl`.
            This, the `baseurl` or `mirrorlist` parameters are required if
            `state` is set to `present`.
        :param mirrorlist:
            Specifies a URL to a file containing a list of baseurls.
            This, the `baseurl` or `metalink` parameters are required if
            `state` is set to `present`.
        :param mirrorlist_expire:
            Time (in seconds) after which the mirrorlist locally cached will
            expire.
            Default value is 6 hours.
        :param name:
            Unique repository ID. This option builds the section name of the
            repository in the repo file.
            This parameter is only required if `state` is set to `present` or
            `absent`.
        :param password:
            Password to use with the username for basic authentication.
        :param priority:
            Enforce ordered protection of repositories. The value is an
            integer from 1 to 99.
            This option only works if the YUM Priorities plugin is installed.
        :param protect:
            Protect packages from updates from other repositories.
        :param proxy:
            URL to the proxy server that yum should use. Set to `_none_` to
            disable the global proxy setting.
        :param proxy_password:
            Password for this proxy.
        :param proxy_username:
            Username to use for proxy.
        :param repo_gpgcheck:
            This tells yum whether or not it should perform a GPG signature
            check on the repodata from this repository.
        :param reposdir:
            Directory where the `.repo` files will be stored.
        :param retries:
            Set the number of times any attempt to retrieve a file should
            retry before returning an error. Setting this to `0` makes yum try
            forever.
        :param s3_enabled:
            Enables support for S3 repositories.
            This option only works if the YUM S3 plugin is installed.
        :param skip_if_unavailable:
            If set to `true` yum will continue running if this repository
            cannot be contacted for any reason. This should be set carefully
            as all repos are consulted for any given command.
        :param ssl_check_cert_permissions:
            Whether yum should check the permissions on the paths for the
            certificates on the repository (both remote and local).
            If we can't read any of the files then yum will force
            `skip_if_unavailable` to be `true`. This is most useful for
            non-root processes which use yum on repos that have client cert
            files which are readable only by root.
        :param sslcacert:
            Path to the directory containing the databases of the certificate
            authorities yum should use to verify SSL certificates.
        :param sslclientcert:
            Path to the SSL client certificate yum should use to connect to
            repos/remote sites.
        :param sslclientkey:
            Path to the SSL client key yum should use to connect to
            repos/remote sites.
        :param sslverify:
            Defines whether yum should verify SSL certificates/hosts at all.
        :param state:
            State of the repo file.
        :param throttle:
            Enable bandwidth throttling for downloads.
            This option can be expressed as a absolute data rate in bytes/sec.
            An SI prefix (k, M or G) may be appended to the bandwidth value.
        :param timeout:
            Number of seconds to wait for a connection before timing out.
        :param ui_repoid_vars:
            When a repository id is displayed, append these yum variables to
            the string if they are used in the `baseurl`/etc. Variables are
            appended in the order listed (and found).
        :param username:
            Username to use for basic authentication to a repo or really any
            url.
        """
        raise AttributeError('yum_repository')
