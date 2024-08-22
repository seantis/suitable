"""
This is an auto-generated file. Please don't manually edit.

Instead call `scripts/generate_module_hints.py`
"""


class AnsibleModules:

    def apt(self, *args, **kwargs):
        """
        Manages apt-packages.

         :param name:
            A list of package names, like `foo`, or package specifier with
            version, like `foo=1.0`. Name wildcards (fnmatch) like `apt*` and
            version wildcards like `foo=1.0*` are also supported.
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
            *update_cache_retry_max_delay*.
            Minimum Ansible version: 2.10
         :param update_cache_retry_max_delay:
            Use an exponential backoff delay for each retry (see
            *update_cache_retries*) up to this max delay in seconds.
            Minimum Ansible version: 2.10
         :param cache_valid_time:
            Update the apt cache if its older than the *cache_valid_time*.
            This option is set in seconds.
            As of Ansible 2.4, if explicitly set, this sets *update_cache=yes*.
         :param purge:
            Will force purging of configuration files if the module state is
            set to *absent*.
         :param default_release:
            Corresponds to the `-t` option for *apt* and sets pin priorities.
         :param install_recommends:
            Corresponds to the `--no-install-recommends` option for *apt*.
            `True` installs recommended packages.  `False` does not install
            recommended packages. By default, Ansible will use the same
            defaults as the operating system. Suggested packages are never
            installed.
         :param force:
            Corresponds to the `--force-yes` to *apt-get* and implies
            `allow_unauthenticated: yes`.
            This option will disable checking both the packages' signatures
            and the certificates of the web servers they are downloaded from.
            This option *is not* the equivalent of passing the `-f` flag to
            *apt-get* on the command line.
            **This is a destructive operation with the potential to destroy
            your system, and it should almost never be used.** Please also see
            `man apt-get` for more information.
         :param allow_unauthenticated:
            Ignore if packages cannot be authenticated. This is useful for
            bootstrapping environments that manage their own apt-key setup.
            `allow_unauthenticated` is only supported with state:
            *install*/I(present).
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
            If `True`, remove unused dependency packages for all module states
            except *build-dep*. It can also be used as the only option.
            Previous to version 2.4, autoclean was also an alias for
            autoremove, now it is its own separate command. See documentation
            for further information.
         :param autoclean:
            If `True`, cleans the local repository of retrieved package files
            that can no longer be downloaded.
         :param policy_rc_d:
            Force the exit code of /usr/sbin/policy-rc.d.
            For example, if *policy_rc_d=101* the installed package will not
            trigger a service start.
            If /usr/sbin/policy-rc.d already exist, it is backed up and
            restored after the package installation.
            If `null`, the /usr/sbin/policy-rc.d isn't created/changed.
         :param only_upgrade:
            Only upgrade a package if it is already installed.
         :param force_apt_get:
            Force usage of apt-get instead of aptitude.
        """
        raise AttributeError('apt')

    def apt_key(self, *args, **kwargs):
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
            If `False`, SSL certificates for the target url will not be
            validated. This should only be used on personally controlled sites
            using self-signed certificates.
        """
        raise AttributeError('apt_key')

    def apt_repository(self, *args, **kwargs):
        """
        Add and remove APT repositories.

         :param repo:
            A source string for the repository.
         :param state:
            A source string state.
         :param mode:
            The octal mode for newly created files in sources.list.d.
         :param update_cache:
            Run the equivalent of `apt-get update` when a change occurs.
            Cache updates are run after making changes.
         :param update_cache_retries:
            Amount of retries if the cache update fails. Also see
            *update_cache_retry_max_delay*.
            Minimum Ansible version: 2.10
         :param update_cache_retry_max_delay:
            Use an exponential backoff delay for each retry (see
            *update_cache_retries*) up to this max delay in seconds.
            Minimum Ansible version: 2.10
         :param validate_certs:
            If `False`, SSL certificates for the target repo will not be
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
        """
        raise AttributeError('apt_repository')

    def assemble(self, *args, **kwargs):
        """
        Assemble configuration files from fragments.

         :param src:
            An already existing directory full of source files.
         :param dest:
            A file to create using the concatenation of all of the source
            files.
         :param backup:
            Create a backup file (if `True`), including the timestamp
            information so you can get the original file back if you somehow
            clobbered it incorrectly.
         :param delimiter:
            A delimiter to separate the file contents.
         :param remote_src:
            If `False`, it will search for src at originating/master machine.
            If `True`, it will go to the remote/target machine for the src.
         :param regexp:
            Assemble files only if `regex` matches the filename.
            If not set, all files are assembled.
            Every "\\" (backslash) must be escaped as "\\\\" to comply to YAML
            syntax.
            Uses `Python regular expressions`__.
         :param ignore_hidden:
            A boolean that controls if files that start with a '.' will be
            included or not.
         :param validate:
            The validation command to run before copying into place.
            The path to the file to validate is passed in via '%s' which must
            be present as in the sshd example below.
            The command is passed securely so shell features like expansion
            and pipes won't work.
        __ http://docs.python.org/2/library/re.html

        """
        raise AttributeError('assemble')

    def async_status(self, *args, **kwargs):
        """
        Obtain status of asynchronous task.

         :param jid:
            Job or task identifier.
         :param mode:
            If `status`, obtain the status.
            If `cleanup`, clean up the async job cache (by default in
            `~/.ansible_async/`) for the specified job *jid*.
        """
        raise AttributeError('async_status')

    def command(self, *args, **kwargs):
        """
        Execute commands on targets.

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
            This is checked before *removes* is checked.
         :param removes:
            A filename or (since 2.0) glob pattern. If a matching file exists,
            this step **will** be run.
            This is checked after *creates* is checked.
         :param chdir:
            Change into this directory before running the command.
         :param warn:
            Enable or disable task warnings.
         :param stdin:
            Set the stdin of the command directly to the specified value.
         :param stdin_add_newline:
            If set to `True`, append a newline to stdin data.
         :param strip_empty_ends:
            Strip empty lines from the end of stdout/stderr in result.
        """
        raise AttributeError('command')

    def copy(self, *args, **kwargs):
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
            If *dest* is a relative path, the starting directory is determined
            by the remote host.
            If `src` and `dest` are files, the parent directory of `dest` is
            not created and the task fails if it does not already exist.
         :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
         :param force:
            Influence whether the remote file must always be replaced.
            If `True`, the remote file will be replaced when contents are
            different than the source.
            If `False`, the file will only be transferred if the destination
            does not exist.
            Alias `thirsty` has been deprecated and will be removed in 2.13.
         :param mode:
            The permissions of the destination file or directory.
            For those used to `/usr/bin/chmod` remember that modes are
            actually octal numbers. You must either add a leading zero so that
            Ansible's YAML parser knows it is an octal number (like `0644` or
            `01777`)or quote it (like `'644'` or `'1777'`) so Ansible receives
            a string and can do its own conversion from string into number.
            Giving Ansible a number without following one of these rules will
            end up with a decimal number which will have unexpected results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, `u+rwx` or `u=rw,g=r,o=r`).
            As of Ansible 2.3, the mode may also be the special string
            `preserve`.
            `preserve` means that the file will be given the same permissions
            as the source file.
            When doing a recursive copy, see also `directory_mode`.
         :param directory_mode:
            When doing a recursive copy set the mode for the directories.
            If this is not set we will use the system defaults.
            The mode is only set on directories which are newly created, and
            will not affect those that already existed.
         :param remote_src:
            Influence whether `src` needs to be transferred or already is
            present remotely.
            If `False`, it will search for `src` at originating/master machine.
            If `True` it will go to the remote/target machine for the `src`.
            `remote_src` supports recursive copying as of version 2.8.
            `remote_src` only works with `mode=preserve` as of version 2.6.
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

    def cron(self, *args, **kwargs):
        """
        Manage cron.d and crontab entries.

         :param name:
            Description of a crontab entry or, if env is set, the name of
            environment variable.
            Required if *state=absent*.
            Note that if name is not set and *state=present*, then a new
            crontab entry will always be created, regardless of existing ones.
            This parameter will always be required in future releases.
         :param user:
            The specific user whose crontab should be modified.
            When unset, this parameter defaults to the current user.
         :param job:
            The command to execute or, if env is set, the value of environment
            variable.
            The command should not contain line breaks.
            Required if *state=present*.
         :param state:
            Whether to ensure the job or environment variable is present or
            absent.
         :param cron_file:
            If specified, uses this file instead of an individual user's
            crontab.
            If this is a relative path, it is interpreted with respect to
            */etc/cron.d*.
            If it is absolute, it will typically be `/etc/crontab`.
            Many linux distros expect (and some require) the filename portion
            to consist solely of upper- and lower-case letters, digits,
            underscores, and hyphens.
            To use the *cron_file* parameter you must specify the *user* as
            well.
         :param backup:
            If set, create a backup of the crontab before it is modified. The
            location of the backup is returned in the `backup_file` variable
            by this module.
         :param minute:
            Minute when the job should run (C(0-59), `*`, `*/2`, and so on).
         :param hour:
            Hour when the job should run (C(0-23), `*`, `*/2`, and so on).
         :param day:
            Day of the month the job should run (C(1-31), `*`, `*/2`, and so
            on).
         :param month:
            Month of the year the job should run (C(1-12), `*`, `*/2`, and so
            on).
         :param weekday:
            Day of the week that the job should run (C(0-6) for
            Sunday-Saturday, `*`, and so on).
         :param reboot:
            If the job should be run at reboot. This option is deprecated.
            Users should use *special_time*.
         :param special_time:
            Special time specification nickname.
         :param disabled:
            If the job should be disabled (commented out) in the crontab.
            Only has effect if *state=present*.
         :param env:
            If set, manages a crontab's environment variable.
            New variables are added on top of crontab.
            *name* and *value* parameters are the name and the value of
            environment variable.
         :param insertafter:
            Used with *state=present* and *env*.
            If specified, the environment variable will be inserted after the
            declaration of specified environment variable.
         :param insertbefore:
            Used with *state=present* and *env*.
            If specified, the environment variable will be inserted before the
            declaration of specified environment variable.
        """
        raise AttributeError('cron')

    def debconf(self, *args, **kwargs):
        """
        Configure a .deb package.

         :param name:
            Name of package to configure.
         :param question:
            A debconf configuration setting.
         :param vtype:
            The type of the value supplied.
            It is highly recommended to add *no_log=True* to task while
            specifying *vtype=password*.
            `seen` was added in Ansible 2.2.
         :param value:
            Value to set the configuration to.
         :param unseen:
            Do not set 'seen' flag when pre-seeding.
        """
        raise AttributeError('debconf')

    def dnf5(self, *args, **kwargs):
        """
        Manages packages with the *dnf5* package manager.

        Minimum Ansible version: 2.15

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
            Whether to install (V(present), `latest`), or remove (V(absent)) a
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
            Minimum Ansible version: 2.17
         :param cacheonly:
            Tells dnf to run entirely from system cache; does not download or
            update metadata.
        """
        raise AttributeError('dnf5')

    def file(self, *args, **kwargs):
        """
        Manage files and file properties.

         :param path:
            Path to the file being managed.
         :param state:
            If `absent`, directories will be recursively deleted, and files or
            symlinks will be unlinked. In the case of a directory, if `diff`
            is declared, you will see the files and folders deleted listed
            under `path_contents`. Note that `absent` will not cause `file` to
            fail if the `path` does not exist as the state did not change.
            If `directory`, all intermediate subdirectories will be created if
            they do not exist. Since Ansible 1.7 they will be created with the
            supplied permissions.
            If `file`, without any other options this works mostly as a 'stat'
            and will return the current state of `path`. Even with other
            options (i.e `mode`), the file will be modified but will NOT be
            created if it does not exist; see the `touch` value or the
            :meth:`ansible.builtin.copy` or :meth:`ansible.builtin.template`
            module if you want that behavior.
            If `hard`, the hard link will be created or changed.
            If `link`, the symbolic link will be created or changed.
            If `touch` (new in 1.4), an empty file will be created if the
            `path` does not exist, while an existing file or directory will
            receive updated file access and modification times (similar to the
            way `touch` works from the command line).
         :param src:
            Path of the file to link to.
            This applies only to `state=link` and `state=hard`.
            For `state=link`, this will also accept a non-existing path.
            Relative paths are relative to the file being created (C(path))
            which is how the Unix command `ln -s SRC DEST` treats relative
            paths.
         :param recurse:
            Recursively set the specified file attributes on directory
            contents.
            This applies only when `state` is set to `directory`.
         :param force:
            Force the creation of the symlinks in two cases: the source file
            does not exist (but will appear later); the destination exists and
            is a file (so, we need to unlink the `path` file and create
            symlink to the `src` file in place of it).
.
         :param follow:
            This flag indicates that filesystem links, if they exist, should
            be followed.
            Previous to Ansible 2.5, this was `False` by default.
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

    def find(self, *args, **kwargs):
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
            ending in .default, you'd need to use '.*\\.default' as a regexp
            and not just '\\.default'.
            This parameter expects a list, which can be either comma separated
            or YAML. If any of the patterns contain a comma, make sure to put
            them in a list to avoid splitting the patterns in undesirable ways.
            Defaults to '*' when `use_regex=False`, or '.*' when
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
            Set this to `True` to include hidden files, otherwise they will be
            ignored.
         :param follow:
            Set this to `True` to follow symlinks in path for systems with
            python 2.6+.
         :param get_checksum:
            Set this to `True` to retrieve a file's SHA1 checksum.
         :param use_regex:
            If `False`, the patterns are file globs (shell).
            If `True`, they are python regexes.
         :param depth:
            Set the maximum number of levels to descend into.
            Setting recurse to `False` will override this value, which is
            effectively depth 1.
            Default is unlimited depth.
        """
        raise AttributeError('find')

    def gather_facts(self, *args, **kwargs):
        """
        Gathers facts about remote hosts.

         :param parallel:
            A toggle that controls if the fact modules are executed in
            parallel or serially and in order. This can guarantee the merge
            order of module facts at the expense of performance.
            By default it will be true if more than one fact module is used.
        """
        raise AttributeError('gather_facts')

    def get_url(self, *args, **kwargs):
        """
        Downloads files from HTTP, HTTPS, or FTP to node.

         :param url:
            HTTP, HTTPS, or FTP URL in the form
            (http|https|ftp)://[user[:pass]]@host.domain[:port]/path.
         :param dest:
            Absolute path of where to download the file to.
            If `dest` is a directory, either the server provided filename or,
            if none provided, the base name of the URL on the remote server
            will be used. If a directory, `force` has no effect.
            If `dest` is a directory, the file will always be downloaded
            (regardless of the `force` option), but replaced only if the
            contents changed..
         :param tmp_dest:
            Absolute path of where temporary file is downloaded to.
            When run on Ansible 2.5 or greater, path defaults to ansible's
            remote_tmp setting.
            When run on Ansible prior to 2.5, it defaults to `TMPDIR`, `TEMP`
            or `TMP` env variables or a platform specific value.
            `here__.
         :param force:
            If `True` and `dest` is not a directory, will download the file
            every time and replace the file if the contents change. If
            `False`, the file will only be downloaded if the destination does
            not exist. Generally should be `True` only for small local files.
            Prior to 0.6, this module behaved as if `True` was the default.
            Alias `thirsty` has been deprecated and will be removed in 2.13.
         :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
         :param sha256sum:
            If a SHA-256 checksum is passed to this parameter, the digest of
            the destination file will be calculated after it is downloaded to
            ensure its integrity and verify that the transfer completed
            successfully. This option is deprecated and will be removed in
            version 2.14. Use option `checksum` instead.
         :param checksum:
            If a checksum is passed to this parameter, the digest of the
            destination file will be calculated after it is downloaded to
            ensure its integrity and verify that the transfer completed
            successfully. Format: <algorithm>:<checksum|url>, e.g.
            checksum="sha256:D98291AC[...]B6DC7B97",
            checksum="sha256:http://example.com/path/sha256sum.txt".
            If you worry about portability, only the sha1 algorithm is
            available on all platforms and python versions.
            The third party hashlib library can be installed for access to
            additional algorithms.
            Additionally, if a checksum is passed to this parameter, and the
            file exist under the `dest` location, the *destination_checksum*
            would be calculated, and if checksum equals
            *destination_checksum*, the file download would be skipped (unless
            `force` is true). If the checksum does not equal
            *destination_checksum*, the destination file is deleted.
         :param use_proxy:
            if `False`, it will not use a proxy, even if one is defined in an
            environment variable on the target hosts.
         :param validate_certs:
            If `False`, SSL certificates will not be validated.
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
            Since version 2.8 you can also use the 'password' alias for this
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
        __ https://docs.python.org/2/library/tempfile.html#tempfile.tempdir

        """
        raise AttributeError('get_url')

    def git(self, *args, **kwargs):
        """
        Deploy software (or files) from git checkouts.

         :param repo:
            git, SSH, or HTTP(S) protocol address of the git repository.
         :param dest:
            The path of where the repository should be checked out. This
            parameter is required, unless `clone` is set to `False`.
         :param version:
            What version of the repository to check out.  This can be the
            literal string `HEAD`, a branch name, a tag name. It can also be a
            *SHA-1* hash, in which case *refspec* needs to be specified if the
            given revision is not already available.
         :param accept_hostkey:
            If `True`, ensure that "-o StrictHostKeyChecking=no" is present as
            an ssh option.
         :param ssh_opts:
            Creates a wrapper script and exports the path as GIT_SSH which git
            then automatically uses to override ssh arguments. An example
            value could be "-o StrictHostKeyChecking=no" (although this
            particular option is better set via `accept_hostkey`).
         :param key_file:
            Specify an optional private key file path, on the target host, to
            use for the checkout.
         :param reference:
            Reference repository (see "git clone --reference ...").
         :param remote:
            Name of the remote.
         :param refspec:
            Add an additional refspec to be fetched. If version is set to a
            *SHA-1* not reachable from any branch or tag, this option may be
            necessary to specify the ref containing the *SHA-1*. Uses the same
            syntax as the 'git fetch' command. An example value could be
            "refs/meta/config".
         :param force:
            If `True`, any modified files in the working repository will be
            discarded.  Prior to 0.7, this was always 'yes' and could not be
            disabled.  Prior to 1.9, the default was `yes`.
         :param depth:
            Create a shallow clone with a history truncated to the specified
            number or revisions. The minimum possible value is `1`, otherwise
            ignored. Needs *git>=1.9.1* to work correctly.
         :param clone:
            If `False`, do not clone the repository even if it does not exist
            locally.
         :param update:
            If `False`, do not retrieve new revisions from the origin
            repository.
            Operations like archive will work on the existing (old) repository
            and might not respond to changes to the options version or remote.
         :param executable:
            Path to git executable to use. If not supplied, the normal
            mechanism for resolving binary paths will be used.
         :param bare:
            If `True`, repository will be created as a bare repo, otherwise it
            will be a standard repo with a workspace.
         :param umask:
            The umask to set before doing any checkouts, or any other
            repository maintenance.
         :param recursive:
            If `False`, repository will be cloned without the --recursive
            option, skipping sub-modules.
         :param track_submodules:
            If `True`, submodules will track the latest commit on their master
            branch (or other branch specified in .gitmodules).  If `False`,
            submodules will be kept at the revision specified by the main
            project. This is equivalent to specifying the --remote flag to git
            submodule update.
         :param verify_commit:
            If `True`, when cloning or checking out a *version* verify the
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
            *archive* to be specified.
            Minimum Ansible version: 2.10
         :param separate_git_dir:
            The path to place the cloned repository. If specified, Git
            repository can be separated from working tree.
         :param gpg_whitelist:
            A list of trusted GPG fingerprints to compare to the fingerprint
            of the GPG-signed commit.
            Only used when *verify_commit=yes*.
            Use of this feature requires Git 2.6+ due to its reliance on git's
            `--raw` flag to `verify-commit` and `verify-tag`.
            Minimum Ansible version: 2.9
        """
        raise AttributeError('git')

    def group(self, *args, **kwargs):
        """
        Add or remove groups.

         :param name:
            Name of the group to manage.
         :param gid:
            Optional *GID* to set for the group.
         :param state:
            Whether the group should be present or not on the remote host.
         :param system:
            If *True*, indicates that the group created is a system group.
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

    def import_playbook(self, *args, **kwargs):
        """
        Import a playbook.
        """
        raise AttributeError('import_playbook')

    def import_role(self, *args, **kwargs):
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
        """
        raise AttributeError('import_role')

    def import_tasks(self, *args, **kwargs):
        """
        Import a task list.
        """
        raise AttributeError('import_tasks')

    def include(self, *args, **kwargs):
        """
        Include a play or task list.
        """
        raise AttributeError('include')

    def include_role(self, *args, **kwargs):
        """
        Load and execute a role.

         :param apply:
            Accepts a hash of task keywords (e.g. `tags`, `become`) that will
            be applied to all tasks within the included role.
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
            exposed to the playbook. If set to `True` the variables will be
            available to tasks following the `include_role` task. This
            functionality differs from standard variable exposure for roles
            listed under the `roles` header or `import_role` as they are
            exposed at playbook parsing time, and available to earlier roles
            and tasks as well.
         :param handlers_from:
            File to load from a role's `handlers/` directory.
        """
        raise AttributeError('include_role')

    def include_tasks(self, *args, **kwargs):
        """
        Dynamically include a task list.

         :param file:
            The name of the imported file is specified directly without any
            other option.
            Unlike :meth:`ansible.builtin.import_tasks`, most keywords,
            including loop, with_items, and conditionals, apply to this
            statement.
            The do until loop is not supported on
            :meth:`ansible.builtin.include_tasks`.
         :param apply:
            Accepts a hash of task keywords (e.g. `tags`, `become`) that will
            be applied to the tasks within the include.
        """
        raise AttributeError('include_tasks')

    def include_vars(self, *args, **kwargs):
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
        """
        raise AttributeError('include_vars')

    def lineinfile(self, *args, **kwargs):
        """
        Manage lines in text files.

         :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as *dest*,
            *destfile* and *name*.
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
            Uses Python regular expressions. See `here__.
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
         :param others:
            All arguments accepted by the :meth:`ansible.builtin.file` module
            also work here.
        __ https://docs.python.org/3/library/re.html

        """
        raise AttributeError('lineinfile')

    def package_facts(self, *args, **kwargs):
        """
        Package information as facts.

         :param manager:
            The package manager used by the system so we can query the package
            information.
            Since 2.8 this is a list and can support multiple package managers
            per system.
            The 'portage' and 'pkg' options were added in version 2.8.
         :param strategy:
            This option controls how the module queries the package managers
            on the system. `first` means it will return only information for
            the first supported package manager available. `all` will return
            information for all supported and available package managers on
            the system.
        """
        raise AttributeError('package_facts')

    def pause(self, *args, **kwargs):
        """
        Pause playbook execution.

         :param minutes:
            A positive number of minutes to pause for.
         :param seconds:
            A positive number of seconds to pause for.
         :param prompt:
            Optional text to use for the prompt message.
         :param echo:
            Controls whether or not keyboard input is shown when typing.
            Has no effect if 'seconds' or 'minutes' is set.
        """
        raise AttributeError('pause')

    def ping(self, *args, **kwargs):
        """
        Try to connect to host, verify a usable python and return `pong` on
        success.

         :param data:
            Data to return for the `ping` return value.
            If this parameter is set to `crash`, the module will cause an
            exception.
        """
        raise AttributeError('ping')

    def pip(self, *args, **kwargs):
        """
        Manages Python library dependencies.

         :param name:
            The name of a Python library to install or the
            url(bzr+,hg+,git+,svn+) of the remote package.
            This can be a list (since 2.2) and contain version specifiers
            (since 2.7).
         :param version:
            The version number to install of the Python library specified in
            the *name* parameter.
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
            For example `python3.5`, `python2.7`. When not specified, the
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
            Mutually exclusive with *virtualenv* (added in 2.1).
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
        """
        raise AttributeError('pip')

    def reboot(self, *args, **kwargs):
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
            Minimum Ansible version: 2.10
        """
        raise AttributeError('reboot')

    def replace(self, *args, **kwargs):
        """
        Replace all instances of a particular string in a file using a
        back-referenced regular expression.

         :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as *dest*,
            *destfile* and *name*.
         :param regexp:
            The regular expression to look for in the contents of the file.
            Uses Python regular expressions; see `here__.
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
            Uses Python regular expressions; see `here__.
            Uses DOTALL, which means the `.` special character *can match
            newlines*.
         :param before:
            If specified, only content before this match will be
            replaced/removed.
            Can be used in combination with `after`.
            Uses Python regular expressions; see `here__.
            Uses DOTALL, which means the `.` special character *can match
            newlines*.
         :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
         :param others:
            All arguments accepted by the :meth:`ansible.builtin.file` module
            also work here.
         :param encoding:
            The character encoding for reading and writing the file.
        __ http://docs.python.org/2/library/re.html
        __ http://docs.python.org/2/library/re.html
        __ http://docs.python.org/2/library/re.html

        """
        raise AttributeError('replace')

    def rpm_key(self, *args, **kwargs):
        """
        Adds or removes a gpg key from the rpm db.

         :param key:
            Key that will be modified. Can be a url, a file on the managed
            node, or a keyid if the key already exists in the database.
         :param state:
            If the key will be imported or removed from the rpm db.
         :param validate_certs:
            If `False` and the `key` is a url starting with https, SSL
            certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
         :param fingerprint:
            The long-form fingerprint of the key being imported.
            This will be used to verify the specified key.
            Minimum Ansible version: 2.9
        """
        raise AttributeError('rpm_key')

    def service(self, *args, **kwargs):
        """
        Manage services.

         :param name:
            Name of the service.
         :param state:
            `started`/C(stopped) are idempotent actions that will not run
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
        """
        raise AttributeError('service')

    def service_facts(self, *args, **kwargs):
        """
        Return service state information as fact data.
        """
        raise AttributeError('service_facts')

    def shell(self, *args, **kwargs):
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
         :param warn:
            Whether to enable task warnings.
         :param stdin:
            Set the stdin of the command directly to the specified value.
         :param stdin_add_newline:
            Whether to append a newline to stdin data.
        """
        raise AttributeError('shell')

    def slurp(self, *args, **kwargs):
        """
        Slurps a file from remote nodes.

         :param src:
            The file on the remote system to fetch. This *must* be a file, not
            a directory.
        """
        raise AttributeError('slurp')

    def stat(self, *args, **kwargs):
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
            This will add both `mime_type` and 'charset' fields to the return,
            if possible.
            In Ansible 2.3 this option changed from 'mime' to 'get_mime' and
            the default changed to 'Yes'.
         :param get_attributes:
            Get file attributes using lsattr tool if present.
        """
        raise AttributeError('stat')

    def subversion(self, *args, **kwargs):
        """
        Deploys a subversion repository.

         :param repo:
            The subversion URL to the repository.
         :param dest:
            Absolute path where the repository should be deployed.
         :param revision:
            Specific revision to checkout.
         :param force:
            If `True`, modified files will be discarded. If `False`, module
            will fail if it encounters modified files. Prior to 1.9 the
            default was `True`.
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
            If `False`, do not check out the repository if it does not exist
            locally.
         :param update:
            If `False`, do not retrieve new revisions from the origin
            repository.
         :param export:
            If `True`, do export instead of checkout/update.
         :param switch:
            If `False`, do not call svn switch before update.
        """
        raise AttributeError('subversion')

    def systemd(self, *args, **kwargs):
        """
        Manage services.

         :param name:
            Name of the service. This parameter takes the name of exactly one
            service to work with.
            When using in a chroot environment you always need to specify the
            full name i.e. (crond.service).
         :param state:
            `started`/C(stopped) are idempotent actions that will not run
            commands unless necessary. `restarted` will always bounce the
            service. `reloaded` will always reload.
         :param enabled:
            Whether the service should start on boot. **At least one of state
            and enabled are required.**.
         :param force:
            Whether to override existing symlinks.
         :param masked:
            Whether the unit should be masked or not, a masked unit is
            impossible to start.
         :param daemon_reload:
            Run daemon-reload before doing any other operations, to make sure
            systemd has read any changes.
            When set to `True`, runs daemon-reload even if the module does not
            start or stop anything.
         :param daemon_reexec:
            Run daemon_reexec command before doing any other operations, the
            systemd manager will serialize the manager state.
         :param user:
            (deprecated) run ``systemctl`` talking to the service manager of
            the calling user, rather than the service manager of the system.
            This option is deprecated and will eventually be removed in 2.11.
            The ``scope`` option should be used instead.
            The default value is `false`.
         :param scope:
            Run systemctl within a given service manager scope, either as the
            default system scope `system`, the current user's scope `user`, or
            the scope of all users `global`.
            For systemd to work with 'user', the executing user must have its
            own instance of dbus started (systemd requirement). The user dbus
            process is normally started during normal login, but not during
            the run of Ansible tasks. Otherwise you will probably get a
            'Failed to connect to bus: no such file or directory' error.
         :param no_block:
            Do not synchronously wait for the requested operation to finish.
            Enqueued job will continue without Ansible blocking on its
            completion.
        """
        raise AttributeError('systemd')

    def systemd_service(self, *args, **kwargs):
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
            `started`/V(stopped) are idempotent actions that will not run
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

    def sysvinit(self, *args, **kwargs):
        """
        Manage SysV services.

         :param name:
            Name of the service.
         :param state:
            `started`/C(stopped) are idempotent actions that will not run
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

    def tempfile(self, *args, **kwargs):
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

    def uri(self, *args, **kwargs):
        """
        Interacts with webservices.

         :param url:
            HTTP or HTTPS URL in the form
            (http|https)://host.domain[:port]/path.
         :param dest:
            A path of where to download the file to (if desired). If *dest* is
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
            `body_format` is set to 'json' it will take an already formatted
            JSON string or convert a data structure into JSON.
            If `body_format` is set to 'form-urlencoded' it will convert a
            dictionary or list of tuples into an
            'application/x-www-form-urlencoded' string. (Added in v2.7).
            If `body_format` is set to 'form-multipart' it will convert a
            dictionary into 'multipart/form-multipart' body. (Added in v2.10).
         :param body_format:
            The serialization format of the body. When set to `json`,
            `form-multipart`, or `form-urlencoded`, encodes the body argument,
            if needed, and automatically sets the Content-Type header
            accordingly.
            As of `2.3` it is possible to override the `Content-Type` header,
            when set to `json` or `form-urlencoded` via the *headers* option.
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
            called `json` in the dictionary results.
         :param force_basic_auth:
            Force the sending of the Basic authentication header upon initial
            request.
            The library used by the uri module only sends authentication
            information when a webservice responds to an initial request with
            a 401 status. Since some basic auth services do not properly send
            a 401, logins will fail.
         :param follow_redirects:
            Whether or not the URI module should follow redirects. `all` will
            follow all redirects. `safe` will follow only "safe" redirects,
            where "safe" means that the client is only doing a GET or HEAD on
            the URI to which it is being redirected. `none` will not follow
            any redirects. Note that `True` and `False` choices are accepted
            for backwards compatibility, where `True` is the equivalent of
            `all` and `False` is the equivalent of `safe`. `True` and `False`
            are deprecated and will be removed in some future version of
            Ansible.
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
            As of `2.3` supplying `Content-Type` here will override the header
            generated by supplying `json` or `form-urlencoded` for
            *body_format*.
         :param validate_certs:
            If `False`, SSL certificates will not be validated.
            This should only set to `False` used on personally controlled
            sites using self-signed certificates.
            Prior to 1.9.2 the code defaulted to `False`.
         :param client_cert:
            PEM formatted certificate chain file to be used for SSL client
            authentication.
            This file can also include the key as well, and if the key is
            included, *client_key* is not required.
         :param client_key:
            PEM formatted file that contains your private key to be used for
            SSL client authentication.
            If *client_cert* contains both the certificate and key, this
            option is not required.
         :param src:
            Path to file to be submitted to the remote server.
            Cannot be used with *body*.
         :param remote_src:
            If `False`, the module will search for src on originating/master
            machine.
            If `True` the module will use the `src` path on the remote/target
            machine.
         :param force:
            If `True` do not get a cached copy.
            Alias `thirsty` has been deprecated and will be removed in 2.13.
         :param use_proxy:
            If `False`, it will not use a proxy, even if one is defined in an
            environment variable on the target hosts.
         :param unix_socket:
            Path to Unix domain socket to use for connection.
         :param http_agent:
            Header to identify as, generally appears in web server logs.
        """
        raise AttributeError('uri')

    def user(self, *args, **kwargs):
        """
        Manage user accounts.

         :param name:
            Name of the user to create, remove or modify.
         :param uid:
            Optionally sets the *UID* of the user.
         :param comment:
            Optionally sets the description (aka *GECOS*) of user account.
         :param hidden:
            macOS only, optionally hide the user from the login window and
            system preferences.
            The default will be `True` if the *system* option is used.
         :param non_unique:
            Optionally when used with the -u option, this option allows to
            change the user ID to a non-unique value.
         :param seuser:
            Optionally sets the seuser type (user_u) on selinux enabled
            systems.
         :param group:
            Optionally sets the user's primary group (takes a group name).
         :param groups:
            List of groups user will be added to. When set to an empty string
            `''`, the user is removed from all groups except the primary group.
            Before Ansible 2.3, the only input format allowed was a comma
            separated string.
         :param append:
            If `True`, add the user to the groups specified in `groups`.
            If `False`, user will only be added to the groups specified in
            `groups`, removing them from all other groups.
         :param shell:
            Optionally set the user's shell.
            On macOS, before Ansible 2.5, the default shell for non-system
            users was `/usr/bin/false`. Since Ansible 2.5, the default shell
            for non-system users on macOS is `/bin/bash`.
            On other operating systems, the default shell is determined by the
            underlying tool being used. See Notes for details.
         :param home:
            Optionally set the user's home directory.
         :param skeleton:
            Optionally set a home skeleton directory.
            Requires `create_home` option!.
         :param password:
            Optionally set the user's password to this crypted value.
            On macOS systems, this value has to be cleartext. Beware of
            security issues.
            To create a disabled account on Linux systems, set this to `'!'`
            or `'*'`.
            To create a disabled account on OpenBSD, set this to
            `'*************'`.
            See `here__ for details on various ways to generate these password
            values.
         :param state:
            Whether the account should exist or not, taking action if the
            state is different from what is stated.
         :param create_home:
            Unless set to `False`, a home directory will be made for the user
            when the account is created or if the home directory does not
            exist.
            Changed from `createhome` to `create_home` in Ansible 2.5.
         :param move_home:
            If set to `True` when used with `home: `, attempt to move the
            user's old home directory to the specified directory if it isn't
            there already and the old home exists.
         :param system:
            When creating an account `state=present`, setting this to `True`
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
         :param ssh_key_type:
            Optionally specify the type of SSH key to generate.
            Available SSH key types will depend on implementation present on
            target host.
         :param ssh_key_file:
            Optionally specify the SSH key filename.
            If this is a relative filename then it will be relative to the
            user's home directory.
            This parameter defaults to *.ssh/id_rsa*.
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
            Lock the password (C(usermod -L), `usermod -U`, `pw lock`).
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
            Does nothing when used with other platforms.
            Can set multiple profiles using comma separation.
            To delete all the profiles, use `profile=''`.
            Currently supported on Illumos/Solaris.
         :param authorization:
            Sets the authorization of the user.
            Does nothing when used with other platforms.
            Can set multiple authorizations using comma separation.
            To delete all authorizations, use `authorization=''`.
            Currently supported on Illumos/Solaris.
         :param role:
            Sets the role of the user.
            Does nothing when used with other platforms.
            Can set multiple roles using comma separation.
            To delete all roles, use `role=''`.
            Currently supported on Illumos/Solaris.
        __ https://docs.ansible.com/ansible/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module

        """  # noqa: E501
        raise AttributeError('user')

    def validate_argument_spec(self, *args, **kwargs):
        """
        Validate role argument specs.

        Minimum Ansible version: 2.11

         :param argument_spec:
            A dictionary like AnsibleModule argument_spec. See `argument spec
            definition,argument_spec`.
         :param provided_arguments:
            A dictionary of the arguments that will be validated according to
            argument_spec.
        """
        raise AttributeError('validate_argument_spec')

    def wait_for(self, *args, **kwargs):
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

    def wait_for_connection(self, *args, **kwargs):
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

    def yum_repository(self, *args, **kwargs):
        """
        Add or remove YUM repositories.

         :param async:
            If set to `True` Yum will download packages and metadata from this
            repo in parallel, if possible.
         :param bandwidth:
            Maximum available network bandwidth in bytes/second. Used with the
            *throttle* option.
            If *throttle* is a percentage and bandwidth is `0` then bandwidth
            throttling will be disabled. If *throttle* is expressed as a data
            rate (bytes/sec) then this option is ignored. Default is `0` (no
            bandwidth throttling).
         :param baseurl:
            URL to the directory where the yum repository's 'repodata'
            directory lives.
            It can also be a list of multiple URLs.
            This, the *metalink* or *mirrorlist* parameters are required if
            *state* is set to `present`.
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
            repositories (with file:// *baseurl*) have delta rpms turned off
            by default.
         :param description:
            A human readable string describing the repository. This option
            corresponds to the "name" property in the repo file.
            This parameter is only required if *state* is set to `present`.
         :param enabled:
            This tells yum whether or not use this repository.
         :param enablegroups:
            Determines whether yum will allow the use of package groups for
            this repository.
         :param exclude:
            List of packages to exclude from updates or installs. This should
            be a space separated list. Shell globs using wildcards (eg. `*`
            and `?`) are allowed.
            The list can also be a regular YAML array.
         :param failovermethod:
            `roundrobin` randomly selects a URL out of the list of URLs to
            start with and proceeds through each of them as it encounters a
            failure contacting the host.
            `priority` starts from the first *baseurl* listed and reads
            through them sequentially.
         :param file:
            File name without the `.repo` extension to save the repo in.
            Defaults to the value of *name*.
         :param gpgcakey:
            A URL pointing to the ASCII-armored CA key file for the repository.
         :param gpgcheck:
            Tells yum whether or not it should perform a GPG signature check
            on packages.
            No default setting. If the value is not set, the system setting
            from `/etc/yum.conf` or system default of `False` will be used.
         :param gpgkey:
            A URL pointing to the ASCII-armored GPG key file for the
            repository.
            It can also be a list of multiple URLs.
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
            the *include=* line. Included files may contain further include
            lines. Yum will abort with an error if an inclusion loop is
            detected.
         :param includepkgs:
            List of packages you want to only use from a repository. This
            should be a space separated list. Shell globs using wildcards (eg.
            `*` and `?`) are allowed. Substitution variables (e.g.
            `$releasever`) are honored here.
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
         :param metadata_expire:
            Time (in seconds) after which the metadata will expire.
            Default value is 6 hours.
         :param metadata_expire_filter:
            Filter the *metadata_expire* time, allowing a trade of speed for
            accuracy if a command doesn't require it. Each yum command can
            specify that it requires a certain level of timeliness quality
            from the remote repos. from "I'm about to install/upgrade, so this
            better be current" to "Anything that's available is good enough".
            `never` - Nothing is filtered, always obey *metadata_expire*.
            `read-only:past` - Commands that only care about past information
            are filtered from metadata expiring. Eg. *yum history* info (if
            history needs to lookup anything about a previous transaction,
            then by definition the remote package was available in the past).
            `read-only:present` - Commands that are balanced between past and
            future. Eg. *yum list yum*.
            `read-only:future` - Commands that are likely to result in running
            other commands which will require the latest metadata. Eg. *yum
            check-update*.
            Note that this option does not override "yum clean expire-cache".
         :param metalink:
            Specifies a URL to a metalink file for the repomd.xml, a list of
            mirrors for the entire repository are generated by converting the
            mirrors for the repomd.xml file to a *baseurl*.
            This, the *baseurl* or *mirrorlist* parameters are required if
            *state* is set to `present`.
         :param mirrorlist:
            Specifies a URL to a file containing a list of baseurls.
            This, the *baseurl* or *metalink* parameters are required if
            *state* is set to `present`.
         :param mirrorlist_expire:
            Time (in seconds) after which the mirrorlist locally cached will
            expire.
            Default value is 6 hours.
         :param name:
            Unique repository ID. This option builds the section name of the
            repository in the repo file.
            This parameter is only required if *state* is set to `present` or
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
            If set to `True` yum will continue running if this repository
            cannot be contacted for any reason. This should be set carefully
            as all repos are consulted for any given command.
         :param ssl_check_cert_permissions:
            Whether yum should check the permissions on the paths for the
            certificates on the repository (both remote and local).
            If we can't read any of the files then yum will force
            *skip_if_unavailable* to be `True`. This is most useful for
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
            the string if they are used in the *baseurl*/etc. Variables are
            appended in the order listed (and found).
         :param username:
            Username to use for basic authentication to a repo or really any
            url.
        """
        raise AttributeError('yum_repository')
