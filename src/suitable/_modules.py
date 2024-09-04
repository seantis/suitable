# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from __future__ import annotations

from typing import overload, Any, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import StrPath
    from collections.abc import Mapping, Sequence
    from suitable._module_types import (
        AddHostResults,
        AptResults,
        AptKeyResults,
        AptRepositoryResults,
        AssembleResults,
        AssertResults,
        AsyncStatusResults,
        BlockinfileResults,
        CommandResults,
        CopyResults,
        CronResults,
        Deb822RepositoryResults,
        DebconfResults,
        DebugResults,
        DnfResults,
        Dnf5Results,
        DpkgSelectionsResults,
        ExpectResults,
        FailResults,
        FetchResults,
        FileResults,
        FindResults,
        GatherFactsResults,
        GetUrlResults,
        GetentResults,
        GitResults,
        GroupResults,
        GroupByResults,
        HostnameResults,
        ImportPlaybookResults,
        ImportRoleResults,
        ImportTasksResults,
        IncludeResults,
        IncludeRoleResults,
        IncludeTasksResults,
        IncludeVarsResults,
        IptablesResults,
        KnownHostsResults,
        LineinfileResults,
        MetaResults,
        PackageResults,
        PackageFactsResults,
        PauseResults,
        PingResults,
        PipResults,
        RawResults,
        RebootResults,
        ReplaceResults,
        RpmKeyResults,
        ScriptResults,
        ServiceResults,
        ServiceFactsResults,
        SetFactResults,
        SetStatsResults,
        SetupResults,
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
        YumResults,
        YumRepositoryResults,
        CliBackupResults,
        CliCommandResults,
        CliConfigResults,
        CliRestoreResults,
        GrpcConfigResults,
        GrpcGetResults,
        NetGetResults,
        NetPingResults,
        NetPutResults,
        NetconfConfigResults,
        NetconfGetResults,
        NetconfRpcResults,
        NetworkResourceResults,
        RestconfConfigResults,
        RestconfGetResults,
        TelnetResults,
        AclResults,
        AtResults,
        AuthorizedKeyResults,
        FirewalldResults,
        FirewalldInfoResults,
        MountResults,
        PatchResults,
        RhelFactsResults,
        RhelRpmOstreeResults,
        RpmOstreeUpgradeResults,
        SebooleanResults,
        SelinuxResults,
        SynchronizeResults,
        SysctlResults,
        CliParseResults,
        FactDiffResults,
        UpdateFactResults,
        ValidateResults,
        WinAclResults,
        WinAclInheritanceResults,
        WinCertificateStoreResults,
        WinCommandResults,
        WinCopyResults,
        WinDnsClientResults,
        WinDomainResults,
        WinDomainControllerResults,
        WinDomainMembershipResults,
        WinDscResults,
        WinEnvironmentResults,
        WinFeatureResults,
        WinFileResults,
        WinFindResults,
        WinGetUrlResults,
        WinGroupResults,
        WinGroupMembershipResults,
        WinHostnameResults,
        WinOptionalFeatureResults,
        WinOwnerResults,
        WinPackageResults,
        WinPathResults,
        WinPingResults,
        WinPowershellResults,
        WinRebootResults,
        WinRegStatResults,
        WinRegeditResults,
        WinServiceResults,
        WinServiceInfoResults,
        WinShareResults,
        WinShellResults,
        WinStatResults,
        WinTempfileResults,
        WinTemplateResults,
        WinUpdatesResults,
        WinUriResults,
        WinUserResults,
        WinUserRightResults,
        WinWaitForResults,
        WinWhoamiResults,
    )
    from suitable.types import Incomplete


# HACK: Get Sphinx to display the default values we don't
#       know as `...` and also avoid mypy errors.
_Unknown: Any = type('...', (object,), {'__repr__': lambda s: '...'})()


class AnsibleModules:

    #
    # ansible.builtin start
    #

    def add_host(
        self,
        *,
        name: str,
        groups: Sequence[str] = _Unknown,
    ) -> AddHostResults:
        """
        Add a host (and alternatively a group) to the ansible-playbook
        in-memory inventory.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.add_host_module>`

        :param name:
            The hostname/ip of the host to add to the inventory, can include a
            colon and a port number.
        :param groups:
            The groups to add the hostname to.
        """  # noqa: E501
        raise AttributeError('add_host')

    def apt(
        self,
        *,
        name: Sequence[str] = _Unknown,
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.apt_module>`

        :param name:
            A list of package names, like ``foo``, or package specifier with
            version, like ``foo=1.0`` or ``foo>=1.0``. Name wildcards
            (fnmatch) like ``apt*`` and version wildcards like ``foo=1.0*``
            are also supported.
        :param state:
            Indicates the desired package state. ``latest`` ensures that the
            latest version is installed. ``build-dep`` ensures the package
            build dependencies are installed. ``fixed`` attempt to correct a
            system with broken dependencies in place.
        :param update_cache:
            Run the equivalent of ``apt-get update`` before the operation. Can
            be run as part of the package installation or as a separate step.
            Default is not to update the cache.
        :param update_cache_retries:
            Amount of retries if the cache update fails. Also see
            ``update_cache_retry_max_delay``.
        :param update_cache_retry_max_delay:
            Use an exponential backoff delay for each retry (see
            ``update_cache_retries``) up to this max delay in seconds.
        :param cache_valid_time:
            Update the apt cache if it is older than the ``cache_valid_time``.
            This option is set in seconds.
            As of Ansible 2.4, if explicitly set, this sets
            ``update_cache=yes``.
        :param purge:
            Will force purging of configuration files if ``state=absent`` or
            ``autoremove=yes``.
        :param default_release:
            Corresponds to the ``-t`` option for *apt* and sets pin priorities.
        :param install_recommends:
            Corresponds to the ``--no-install-recommends`` option for *apt*.
            ``true`` installs recommended packages. ``false`` does not install
            recommended packages. By default, Ansible will use the same
            defaults as the operating system. Suggested packages are never
            installed.
        :param force:
            Corresponds to the ``--force-yes`` to *apt-get* and implies
            ``allow_unauthenticated=yes`` and ``allow_downgrade=yes``.
            This option will disable checking both the packages' signatures
            and the certificates of the web servers they are downloaded from.
            This option *is not* the equivalent of passing the ``-f`` flag to
            *apt-get* on the command line.
            **This is a destructive operation with the potential to destroy
            your system, and it should almost never be used.** Please also see
            ``man apt-get`` for more information.
        :param clean:
            Run the equivalent of ``apt-get clean`` to clear out the local
            repository of retrieved package files. It removes everything but
            the lock file from /var/cache/apt/archives/ and
            /var/cache/apt/archives/partial/.
            Can be run as part of the package installation (clean runs before
            install) or as a separate step.
        :param allow_unauthenticated:
            Ignore if packages cannot be authenticated. This is useful for
            bootstrapping environments that manage their own apt-key setup.
            ``allow_unauthenticated`` is only supported with ``state``:
            ``install``/``present``.
        :param allow_downgrade:
            Corresponds to the ``--allow-downgrades`` option for *apt*.
            This option enables the named package and version to replace an
            already installed higher version of that package.
            Note that setting ``allow_downgrade=true`` can make this module
            behave in a non-idempotent way.
            (The task could end up with a set of packages that does not match
            the complete list of specified packages to install).
            ``allow_downgrade`` is only supported by ``apt`` and will be
            ignored if ``aptitude`` is detected or specified.
        :param allow_change_held_packages:
            Allows changing the version of a package which is on the apt hold
            list.
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
            Requires the ``xz-utils`` package to extract the control file of
            the deb package to install.
        :param autoremove:
            If ``true``, remove unused dependency packages for all module
            states except ``build-dep``. It can also be used as the only
            option.
            Previous to version 2.4, autoclean was also an alias for
            autoremove, now it is its own separate command. See documentation
            for further information.
        :param autoclean:
            If ``true``, cleans the local repository of retrieved package
            files that can no longer be downloaded.
        :param policy_rc_d:
            Force the exit code of /usr/sbin/policy-rc.d.
            For example, if *policy_rc_d=101* the installed package will not
            trigger a service start.
            If /usr/sbin/policy-rc.d already exists, it is backed up and
            restored after the package installation.
            If ``null``, the /usr/sbin/policy-rc.d isn't created/changed.
        :param only_upgrade:
            Only upgrade a package if it is already installed.
        :param fail_on_autoremove:
            Corresponds to the ``--no-remove`` option for ``apt``.
            If ``true``, it is ensured that no packages will be removed or the
            task will fail.
            ``fail_on_autoremove`` is only supported with ``state`` except
            ``absent``.
            ``fail_on_autoremove`` is only supported by ``apt`` and will be
            ignored if ``aptitude`` is detected or specified.
        :param force_apt_get:
            Force usage of apt-get instead of aptitude.
        :param lock_timeout:
            How many seconds will this action wait to acquire a lock on the
            apt db.
            Sometimes there is a transitory lock and this will retry at least
            until timeout is hit.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.apt_key_module>`

        :param id:
            The identifier of the key.
            Including this allows check mode to correctly report the changed
            state.
            If specifying a subkey's id be aware that apt-key does not
            understand how to remove keys via a subkey id. Specify the primary
            key's id instead.
            This parameter is required when ``state`` is set to ``absent``.
        :param data:
            The keyfile contents to add to the keyring.
        :param file:
            The path to a keyfile on the remote server to add to the keyring.
        :param keyring:
            The full path to specific keyring file in
            ``/etc/apt/trusted.gpg.d/``.
        :param url:
            The URL to retrieve key from.
        :param keyserver:
            The keyserver to retrieve key from.
        :param state:
            Ensures that the key is present (added) or absent (revoked).
        :param validate_certs:
            If ``false``, SSL certificates for the target url will not be
            validated. This should only be used on personally controlled sites
            using self-signed certificates.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.apt_repository_module>`

        :param repo:
            A source string for the repository.
        :param state:
            A source string state.
        :param mode:
            The octal mode for newly created files in sources.list.d.
            Default is what system uses (probably 0644).
        :param update_cache:
            Run the equivalent of ``apt-get update`` when a change occurs.
            Cache updates are run after making changes.
        :param update_cache_retries:
            Amount of retries if the cache update fails. Also see
            ``update_cache_retry_max_delay``.
        :param update_cache_retry_max_delay:
            Use an exponential backoff delay for each retry (see
            ``update_cache_retries``) up to this max delay in seconds.
        :param validate_certs:
            If ``false``, SSL certificates for the target repo will not be
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
            Runs ``apt-get install python-apt`` for Python 2, and
            ``apt-get install python3-apt`` for Python 3.
            Only works with the system Python 2 or Python 3. If you are using
            a Python on the remote that is not the system Python, set
            ``install_python_apt=false`` and ensure that the Python apt
            library for your Python version is installed some other way.
        """  # noqa: E501
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
        decrypt: bool = True,
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
    ) -> AssembleResults:
        """
        Assemble configuration files from fragments.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.assemble_module>`

        :param src:
            An already existing directory full of source files.
        :param dest:
            A file to create using the concatenation of all of the source
            files.
        :param backup:
            Create a backup file (if ``true``), including the timestamp
            information so you can get the original file back if you somehow
            clobbered it incorrectly.
        :param delimiter:
            A delimiter to separate the file contents.
        :param remote_src:
            If ``false``, it will search for src at originating/master machine.
            If ``true``, it will go to the remote/target machine for the src.
        :param regexp:
            Assemble files only if the given regular expression matches the
            filename.
            If not set, all files are assembled.
            Every ``\\`` (backslash) must be escaped as ``\\\\`` to comply to
            YAML syntax.
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
        :param decrypt:
            This option controls the auto-decryption of source files using
            vault.
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        """  # noqa: E501
        raise AttributeError('assemble')

    def assert_(
        self,
        *,
        that: Sequence[str],
        fail_msg: str = _Unknown,
        success_msg: str = _Unknown,
        quiet: bool = False,
    ) -> AssertResults:
        """
        Asserts given expressions are true.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.assert_module>`

        :param that:
            A list of string expressions of the same form that can be passed
            to the 'when' statement.
        :param fail_msg:
            The customized message used for a failing assertion.
            This argument was called 'msg' before Ansible 2.7, now it is
            renamed to 'fail_msg' with alias 'msg'.
        :param success_msg:
            The customized message used for a successful assertion.
        :param quiet:
            Set this to ``true`` to avoid verbose output.
        """  # noqa: E501
        raise AttributeError('assert')

    def async_status(
        self,
        *,
        jid: str,
        mode: Literal['cleanup', 'status'] = 'status',
    ) -> AsyncStatusResults:
        """
        Obtain status of asynchronous task.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.async_status_module>`

        .. warning::
            The documentation is referring to the module from
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.async_status_module>`,
            there are however other collections with the same module name, so
            depending on your environment you may be getting one of those
            instead.

            Conflicting collections:

            * :ref:`ansible.windows <ansible_collections.ansible.windows.async_status_module>`

        :param jid:
            Job or task identifier.
        :param mode:
            If ``status``, obtain the status.
            If ``cleanup``, clean up the async job cache (by default in
            ``~/.ansible_async/``) for the specified job ``jid``, without
            waiting for it to finish.
        """  # noqa: E501
        raise AttributeError('async_status')

    def blockinfile(
        self,
        *,
        path: StrPath,
        state: Literal['absent', 'present'] = 'present',
        marker: str = _Unknown,
        block: str = '',
        insertafter: str = 'EOF',
        insertbefore: str = _Unknown,
        create: bool = False,
        backup: bool = False,
        marker_begin: str = 'BEGIN',
        marker_end: str = 'END',
        append_newline: bool = False,
        prepend_newline: bool = False,
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
        validate: str = _Unknown,
    ) -> BlockinfileResults:
        """
        Insert/update/remove a text block surrounded by marker lines.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.blockinfile_module>`

        :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as ``dest``,
            ``destfile`` and ``name``.
        :param state:
            Whether the block should be there or not.
        :param marker:
            The marker line template.
            ``{mark}`` will be replaced with the values in ``marker_begin``
            (default="BEGIN") and ``marker_end`` (default="END").
            Using a custom marker without the ``{mark}`` variable may result
            in the block being repeatedly inserted on subsequent playbook runs.
            Multi-line markers are not supported and will result in the block
            being repeatedly inserted on subsequent playbook runs.
            A newline is automatically appended by the module to
            ``marker_begin`` and ``marker_end``.
        :param block:
            The text to insert inside the marker lines.
            If it is missing or an empty string, the block will be removed as
            if ``state`` were specified to ``absent``.
        :param insertafter:
            If specified and no begin/ending ``marker`` lines are found, the
            block will be inserted after the last match of specified regular
            expression.
            A special value is available; ``EOF`` for inserting the block at
            the end of the file.
            If specified regular expression has no matches, ``EOF`` will be
            used instead.
            The presence of the multiline flag (?m) in the regular expression
            controls whether the match is done line by line or with multiple
            lines. This behaviour was added in ansible-core 2.14.
        :param insertbefore:
            If specified and no begin/ending ``marker`` lines are found, the
            block will be inserted before the last match of specified regular
            expression.
            A special value is available; ``BOF`` for inserting the block at
            the beginning of the file.
            If specified regular expression has no matches, the block will be
            inserted at the end of the file.
            The presence of the multiline flag (?m) in the regular expression
            controls whether the match is done line by line or with multiple
            lines. This behaviour was added in ansible-core 2.14.
        :param create:
            Create a new file if it does not exist.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param marker_begin:
            This will be inserted at ``{mark}`` in the opening ansible block
            ``marker``.
        :param marker_end:
            This will be inserted at ``{mark}`` in the closing ansible block
            ``marker``.
        :param append_newline:
            Append a blank line to the inserted block, if this does not appear
            at the end of the file.
            Note that this attribute is not considered when ``state`` is set
            to ``absent``.
            Requires ansible-core >= 2.16
        :param prepend_newline:
            Prepend a blank line to the inserted block, if this does not
            appear at the beginning of the file.
            Note that this attribute is not considered when ``state`` is set
            to ``absent``.
            Requires ansible-core >= 2.16
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        :param validate:
            The validation command to run before copying the updated file into
            the final destination.
            A temporary file path is used to validate, passed in through '%s'
            which must be present as in the examples below.
            Also, the command is passed securely so shell features such as
            expansion and pipes will not work.
            For an example on how to handle more complex validation than what
            this option provides, see ``handling complex validation``.
        """  # noqa: E501
        raise AttributeError('blockinfile')

    @overload
    def command(
        self,
        *,
        expand_argument_vars: bool = True,
        cmd: str = _Unknown,
        argv: Sequence[str] = _Unknown,
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.command_module>`

        .. warning::
            The documentation is referring to the module from
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.command_module>`,
            there are however other collections with the same module name, so
            depending on your environment you may be getting one of those
            instead.

            Conflicting collections:

            * :ref:`community.ciscosmb <ansible_collections.community.ciscosmb.command_module>`
            * :ref:`community.routeros <ansible_collections.community.routeros.command_module>`

        :param expand_argument_vars:
            Expands the arguments that are variables, for example ``$HOME``
            will be expanded before being passed to the command to run.
            Set to ``false`` to disable expansion and treat the value as a
            literal argument.
            Requires ansible-core >= 2.16
        :param cmd:
            The command to run.
        :param argv:
            Passes the command as a list rather than a string.
            Use ``argv`` to avoid quoting values that would otherwise be
            interpreted incorrectly (for example "user name").
            Only the string (free form) or the list (argv) form can be
            provided, not both. One or the other must be provided.
        :param creates:
            A filename or (since 2.0) glob pattern. If a matching file already
            exists, this step **will not** be run.
            This is checked before ``removes`` is checked.
        :param removes:
            A filename or (since 2.0) glob pattern. If a matching file exists,
            this step **will** be run.
            This is checked after ``creates`` is checked.
        :param chdir:
            Change into this directory before running the command.
        :param stdin:
            Set the stdin of the command directly to the specified value.
        :param stdin_add_newline:
            If set to ``true``, append a newline to stdin data.
        :param strip_empty_ends:
            Strip empty lines from the end of stdout/stderr in result.
        """  # noqa: E501
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
        decrypt: bool = True,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
        validate: str = _Unknown,
    ) -> CopyResults:
        """
        Copy files to remote locations.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.copy_module>`

        :param src:
            Local path to a file to copy to the remote server.
            This can be absolute or relative.
            If path is a directory, it is copied recursively. In this case, if
            path ends with "/", only inside contents of that directory are
            copied to destination. Otherwise, if it does not end with "/", the
            directory itself with all contents is copied. This behavior is
            similar to the ``rsync`` command line tool.
        :param content:
            When used instead of ``src``, sets the contents of a file directly
            to the specified value.
            Works only when ``dest`` is a file. Creates the file if it does
            not exist.
            For advanced formatting or if ``content`` contains a variable, use
            the :meth:`template` method.
        :param dest:
            Remote absolute path where the file should be copied to.
            If ``src`` is a directory, this must be a directory too.
            If ``dest`` is a non-existent path and if either ``dest`` ends
            with "/" or ``src`` is a directory, ``dest`` is created.
            If ``dest`` is a relative path, the starting directory is
            determined by the remote host.
            If ``src`` and ``dest`` are files, the parent directory of
            ``dest`` is not created and the task fails if it does not already
            exist.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param force:
            Influence whether the remote file must always be replaced.
            If ``true``, the remote file will be replaced when contents are
            different than the source.
            If ``false``, the file will only be transferred if the destination
            does not exist.
        :param mode:
            The permissions of the destination file or directory.
            For those used to ``/usr/bin/chmod`` remember that modes are
            actually octal numbers. You must either add a leading zero so that
            Ansible's YAML parser knows it is an octal number (like ``0644``
            or ``01777``) or quote it (like ``'644'`` or ``'1777'``) so
            Ansible receives a string and can do its own conversion from
            string into number. Giving Ansible a number without following one
            of these rules will end up with a decimal number which will have
            unexpected results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            As of Ansible 2.3, the mode may also be the special string
            ``preserve``.
            ``preserve`` means that the file will be given the same
            permissions as the source file.
            When doing a recursive copy, see also ``directory_mode``.
            If ``mode`` is not specified and the destination file **does not**
            exist, the default ``umask`` on the system will be used when
            setting the mode for the newly created file.
            If ``mode`` is not specified and the destination file **does**
            exist, the mode of the existing file will be used.
            Specifying ``mode`` is the best way to ensure files are created
            with the correct permissions. See CVE-2020-1736 for further
            details.
        :param directory_mode:
            Set the access permissions of newly created directories to the
            given mode. Permissions on existing directories do not change.
            See ``mode`` for the syntax of accepted values.
            The target system's defaults determine permissions when this
            parameter is not set.
        :param remote_src:
            Influence whether ``src`` needs to be transferred or already is
            present remotely.
            If ``false``, it will search for ``src`` on the controller node.
            If ``true`` it will search for ``src`` on the managed (remote)
            node.
            ``remote_src`` supports recursive copying as of version 2.8.
            ``remote_src`` only works with ``mode=preserve`` as of version 2.6.
            Auto-decryption of files does not work when ``remote_src=yes``.
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
        :param decrypt:
            This option controls the auto-decryption of source files using
            vault.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        :param validate:
            The validation command to run before copying the updated file into
            the final destination.
            A temporary file path is used to validate, passed in through '%s'
            which must be present as in the examples below.
            Also, the command is passed securely so shell features such as
            expansion and pipes will not work.
            For an example on how to handle more complex validation than what
            this option provides, see ``handling complex validation``.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.cron_module>`

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
            Required if ``state=present``.
        :param state:
            Whether to ensure the job or environment variable is present or
            absent.
        :param cron_file:
            If specified, uses this file instead of an individual user's
            crontab. The assumption is that this file is exclusively managed
            by the module, do not use if the file contains multiple entries,
            NEVER use for /etc/crontab.
            If this is a relative path, it is interpreted with respect to
            ``/etc/cron.d``.
            Many linux distros expect (and some require) the filename portion
            to consist solely of upper- and lower-case letters, digits,
            underscores, and hyphens.
            Using this parameter requires you to specify the ``user`` as well,
            unless ``state`` is not ``present``.
            Either this parameter or ``name`` is required.
        :param backup:
            If set, create a backup of the crontab before it is modified. The
            location of the backup is returned in the ``ignore:backup_file``
            variable by this module.
        :param minute:
            Minute when the job should run (``0-59``, ``*``, ``*/2``, and so
            on).
        :param hour:
            Hour when the job should run (``0-23``, ``*``, ``*/2``, and so on).
        :param day:
            Day of the month the job should run (``1-31``, ``*``, ``*/2``, and
            so on).
        :param month:
            Month of the year the job should run (``1-12``, ``*``, ``*/2``,
            and so on).
        :param weekday:
            Day of the week that the job should run (``0-6`` for
            Sunday-Saturday, ``*``, and so on).
        :param special_time:
            Special time specification nickname.
        :param disabled:
            If the job should be disabled (commented out) in the crontab.
            Only has effect if ``state=present``.
        :param env:
            If set, manages a crontab's environment variable.
            New variables are added on top of crontab.
            ``name`` and ``value`` parameters are the name and the value of
            environment variable.
        :param insertafter:
            Used with ``state=present`` and ``env``.
            If specified, the environment variable will be inserted after the
            declaration of specified environment variable.
        :param insertbefore:
            Used with ``state=present`` and ``env``.
            If specified, the environment variable will be inserted before the
            declaration of specified environment variable.
        """  # noqa: E501
        raise AttributeError('cron')

    def deb822_repository(
        self,
        *,
        allow_downgrade_to_insecure: bool = _Unknown,
        allow_insecure: bool = _Unknown,
        allow_weak: bool = _Unknown,
        architectures: Sequence[str] = _Unknown,
        by_hash: bool = _Unknown,
        check_date: bool = _Unknown,
        check_valid_until: bool = _Unknown,
        components: Sequence[str] = _Unknown,
        date_max_future: int = _Unknown,
        enabled: bool = _Unknown,
        inrelease_path: str = _Unknown,
        languages: Sequence[str] = _Unknown,
        name: str,
        pdiffs: bool = _Unknown,
        signed_by: str = _Unknown,
        suites: Sequence[str] = _Unknown,
        targets: Sequence[str] = _Unknown,
        trusted: bool = _Unknown,
        types: Sequence[str] = _Unknown,
        uris: Sequence[str] = _Unknown,
        mode: str = '0644',
        state: Literal['absent', 'present'] = 'present',
    ) -> Deb822RepositoryResults:
        """
        Add and remove deb822 formatted repositories.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.deb822_repository_module>`

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
            Name of the repo. Specifically used for ``X-Repolib-Name`` and in
            naming the repository and signing key files.
        :param pdiffs:
            Controls if APT should try to use PDiffs to update old indexes
            instead of downloading the new indexes entirely.
        :param signed_by:
            Either a URL to a GPG key, absolute path to a keyring file, one or
            more fingerprints of keys either in the ``trusted.gpg`` keyring or
            in the keyrings in the ``trusted.gpg.d/`` directory, or an ASCII
            armored GPG public key block.
        :param suites:
            Suite can specify an exact path in relation to the UR*s* provided,
            in which case the Components: must be omitted and suite must end
            with a slash (``/``). Alternatively, it may take the form of a
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
            binary ``deb`` or source code ``deb-src``.
        :param uris:
            The URIs must specify the base of the Debian distribution archive,
            from which APT finds the information it needs.
        :param mode:
            The octal mode for newly created files in sources.list.d.
        :param state:
            A source string state.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.debconf_module>`

        :param name:
            Name of package to configure.
        :param question:
            A debconf configuration setting.
        :param vtype:
            The type of the value supplied.
            It is highly recommended to add ``no_log=True`` to task while
            specifying ``vtype=password``.
            ``seen`` was added in Ansible 2.2.
            After Ansible 2.17, user can specify ``value`` as a list, if
            ``vtype`` is set as ``multiselect``.
        :param value:
            Value to set the configuration to.
            After Ansible 2.17, ``value`` is of type 'raw'.
        :param unseen:
            Do not set 'seen' flag when pre-seeding.
        """  # noqa: E501
        raise AttributeError('debconf')

    def debug(
        self,
        *,
        msg: str = _Unknown,
        var: str = _Unknown,
        verbosity: int = 0,
    ) -> DebugResults:
        """
        Print statements during execution.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.debug_module>`

        :param msg:
            The customized message that is printed. If omitted, prints a
            generic message.
        :param var:
            A variable name to debug.
            Mutually exclusive with the ``msg`` option.
            Be aware that this option already runs in Jinja2 context and has
            an implicit ``{{ }}`` wrapping, so you should not be using Jinja2
            delimiters unless you are looking for double interpolation.
        :param verbosity:
            A number that controls when the debug is run, if you set to 3 it
            will only run debug when -vvv or above.
        """  # noqa: E501
        raise AttributeError('debug')

    def dnf(
        self,
        *,
        use_backend: Literal[
            'auto',
            'yum',
            'dnf',
            'yum4',
            'dnf4',
            'dnf5',
        ] = 'auto',
        name: Sequence[str] = _Unknown,
        list: str = _Unknown,
        state: Literal[
            'absent',
            'present',
            'installed',
            'removed',
            'latest',
        ] = _Unknown,
        enablerepo: Sequence[str] = _Unknown,
        disablerepo: Sequence[str] = _Unknown,
        conf_file: str = _Unknown,
        disable_gpg_check: bool = False,
        installroot: str = '/',
        releasever: str = _Unknown,
        autoremove: bool = False,
        exclude: Sequence[str] = _Unknown,
        skip_broken: bool = False,
        update_cache: bool = False,
        update_only: bool = False,
        security: bool = False,
        bugfix: bool = False,
        enable_plugin: Sequence[str] = _Unknown,
        disable_plugin: Sequence[str] = _Unknown,
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
    ) -> DnfResults:
        """
        Manages packages with the *dnf* package manager.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.dnf_module>`

        :param use_backend:
            Backend module to use.
            Requires ansible-core >= 2.15
        :param name:
            A package name or package specifier with version, like
            ``name-1.0``. When using state=latest, this can be '*' which means
            run: dnf -y update. You can also pass a url or a local path to an
            rpm file. To operate on several packages this can accept a comma
            separated string of packages or a list of packages.
            Comparison operators for package version are valid here ``>``,
            ``<``, ``>=``, ``<=``. Example - ``name >= 1.0``. Spaces around
            the operator are required.
            You can also pass an absolute path for a binary which is provided
            by the package to install. See examples for more information.
        :param list:
            Various (non-idempotent) commands for usage with
            ``/usr/bin/ansible`` and *not* playbooks. Use
            :meth:`package_facts` instead of the ``list`` argument as a best
            practice.
        :param state:
            Whether to install (``present``, ``latest``), or remove
            (``absent``) a package.
            Default is ``None``, however in effect the default action is
            ``present`` unless the ``autoremove`` option is enabled for this
            module, then ``absent`` is inferred.
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
            being installed. Has an effect only if ``state`` is ``present`` or
            ``latest``.
            This setting affects packages installed from a repository as well
            as "local" packages installed from the filesystem or a URL.
        :param installroot:
            Specifies an alternative installroot, relative to which all
            packages will be installed.
        :param releasever:
            Specifies an alternative release from which all packages will be
            installed.
        :param autoremove:
            If ``true``, removes all "leaf" packages from the system that were
            originally installed as dependencies of user-installed packages
            but which are no longer required by any such package. Should be
            used alone or when ``state`` is ``absent``.
        :param exclude:
            Package name(s) to exclude when state=present, or latest. This can
            be a list or a comma separated string.
        :param skip_broken:
            Skip all unavailable packages or packages with broken dependencies
            without raising an error. Equivalent to passing the --skip-broken
            option.
        :param update_cache:
            Force dnf to check if cache is out of date and redownload if
            needed. Has an effect only if ``state`` is ``present`` or
            ``latest``.
        :param update_only:
            When using latest, only update installed packages. Do not install
            packages.
            Has an effect only if ``state`` is ``latest``.
        :param security:
            If set to ``true``, and ``state=latest`` then only installs
            updates that have been marked security related.
            Note that, similar to ``dnf upgrade-minimal``, this filter applies
            to dependencies as well.
        :param bugfix:
            If set to ``true``, and ``state=latest`` then only installs
            updates that have been marked bugfix related.
            Note that, similar to ``dnf upgrade-minimal``, this filter applies
            to dependencies as well.
        :param enable_plugin:
            *Plugin* name to enable for the install/update operation. The
            enabled plugin will not persist beyond the transaction.
        :param disable_plugin:
            *Plugin* name to disable for the install/update operation. The
            disabled plugins will not persist beyond the transaction.
        :param disable_excludes:
            Disable the excludes defined in DNF config files.
            If set to ``all``, disables all excludes.
            If set to ``main``, disable excludes defined in [main] in dnf.conf.
            If set to ``repoid``, disable excludes defined for given repo id.
        :param validate_certs:
            This only applies if using a https url as the source of the rpm.
            e.g. for localinstall. If set to ``false``, the SSL certificates
            will not be validated.
            This should only set to ``false`` used on personally controlled
            sites using self-signed certificates as it avoids verifying the
            source site.
        :param sslverify:
            Disables SSL validation of the repository server for this
            transaction.
            This should be set to ``false`` if one of the configured
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
            Amount of time to wait for the dnf lockfile to be freed.
        :param install_weak_deps:
            Will also install all packages linked by a weak dependency
            relation.
        :param download_dir:
            Specifies an alternate directory to store packages.
            Has an effect only if ``download_only`` is specified.
        :param allowerasing:
            If ``true`` it allows erasing of installed packages to resolve
            dependencies.
        :param nobest:
            This is the opposite of the ``best`` option kept for backwards
            compatibility.
            Since ansible-core 2.17 the default value is set by the operating
            system distribution.
        :param best:
            When set to ``true``, either use a package with the highest
            version available or fail.
            When set to ``false``, if the latest version cannot be installed
            go with the lower version.
            Default is set by the operating system distribution.
            Requires ansible-core >= 2.17
        :param cacheonly:
            Tells dnf to run entirely from system cache; does not download or
            update metadata.
        """  # noqa: E501
        raise AttributeError('dnf')

    def dnf5(
        self,
        *,
        name: Sequence[str] = _Unknown,
        list: str = _Unknown,
        state: Literal[
            'absent',
            'present',
            'installed',
            'removed',
            'latest',
        ] = _Unknown,
        enablerepo: Sequence[str] = _Unknown,
        disablerepo: Sequence[str] = _Unknown,
        conf_file: str = _Unknown,
        disable_gpg_check: bool = False,
        installroot: str = '/',
        releasever: str = _Unknown,
        autoremove: bool = False,
        exclude: Sequence[str] = _Unknown,
        skip_broken: bool = False,
        update_cache: bool = False,
        update_only: bool = False,
        security: bool = False,
        bugfix: bool = False,
        enable_plugin: Sequence[str] = _Unknown,
        disable_plugin: Sequence[str] = _Unknown,
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.dnf5_module>`

        .. note:: Requires ansible-core >= 2.15

        :param name:
            A package name or package specifier with version, like
            ``name-1.0``. When using state=latest, this can be '*' which means
            run: dnf -y update. You can also pass a url or a local path to an
            rpm file. To operate on several packages this can accept a comma
            separated string of packages or a list of packages.
            Comparison operators for package version are valid here ``>``,
            ``<``, ``>=``, ``<=``. Example - ``name >= 1.0``. Spaces around
            the operator are required.
            You can also pass an absolute path for a binary which is provided
            by the package to install. See examples for more information.
        :param list:
            Various (non-idempotent) commands for usage with
            ``/usr/bin/ansible`` and *not* playbooks. Use
            :meth:`package_facts` instead of the ``list`` argument as a best
            practice.
        :param state:
            Whether to install (``present``, ``latest``), or remove
            (``absent``) a package.
            Default is ``None``, however in effect the default action is
            ``present`` unless the ``autoremove`` option is enabled for this
            module, then ``absent`` is inferred.
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
            being installed. Has an effect only if ``state`` is ``present`` or
            ``latest``.
            This setting affects packages installed from a repository as well
            as "local" packages installed from the filesystem or a URL.
        :param installroot:
            Specifies an alternative installroot, relative to which all
            packages will be installed.
        :param releasever:
            Specifies an alternative release from which all packages will be
            installed.
        :param autoremove:
            If ``true``, removes all "leaf" packages from the system that were
            originally installed as dependencies of user-installed packages
            but which are no longer required by any such package. Should be
            used alone or when ``state`` is ``absent``.
        :param exclude:
            Package name(s) to exclude when state=present, or latest. This can
            be a list or a comma separated string.
        :param skip_broken:
            Skip all unavailable packages or packages with broken dependencies
            without raising an error. Equivalent to passing the --skip-broken
            option.
        :param update_cache:
            Force dnf to check if cache is out of date and redownload if
            needed. Has an effect only if ``state`` is ``present`` or
            ``latest``.
        :param update_only:
            When using latest, only update installed packages. Do not install
            packages.
            Has an effect only if ``state`` is ``latest``.
        :param security:
            If set to ``true``, and ``state=latest`` then only installs
            updates that have been marked security related.
            Note that, similar to ``dnf upgrade-minimal``, this filter applies
            to dependencies as well.
        :param bugfix:
            If set to ``true``, and ``state=latest`` then only installs
            updates that have been marked bugfix related.
            Note that, similar to ``dnf upgrade-minimal``, this filter applies
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
            If set to ``all``, disables all excludes.
            If set to ``main``, disable excludes defined in [main] in dnf.conf.
            If set to ``repoid``, disable excludes defined for given repo id.
        :param validate_certs:
            This is effectively a no-op in the dnf5 module as dnf5 itself
            handles downloading a https url as the source of the rpm, but is
            an accepted parameter for feature parity/compatibility with the
            :meth:`dnf` method.
        :param sslverify:
            Disables SSL validation of the repository server for this
            transaction.
            This should be set to ``false`` if one of the configured
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
            Has an effect only if ``download_only`` is specified.
        :param allowerasing:
            If ``true`` it allows erasing of installed packages to resolve
            dependencies.
        :param nobest:
            This is the opposite of the ``best`` option kept for backwards
            compatibility.
            Since ansible-core 2.17 the default value is set by the operating
            system distribution.
        :param best:
            When set to ``true``, either use a package with the highest
            version available or fail.
            When set to ``false``, if the latest version cannot be installed
            go with the lower version.
            Default is set by the operating system distribution.
            Requires ansible-core >= 2.17
        :param cacheonly:
            Tells dnf to run entirely from system cache; does not download or
            update metadata.
        """  # noqa: E501
        raise AttributeError('dnf5')

    def dpkg_selections(
        self,
        *,
        name: str,
        selection: Literal[
            'install',
            'hold',
            'deinstall',
            'purge',
        ],
    ) -> DpkgSelectionsResults:
        """
        Dpkg package selection selections.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.dpkg_selections_module>`

        :param name:
            Name of the package.
        :param selection:
            The selection state to set the package to.
        """  # noqa: E501
        raise AttributeError('dpkg_selections')

    def expect(
        self,
        *,
        command: str,
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        chdir: StrPath = _Unknown,
        responses: Mapping[str, Incomplete],
        timeout: int | str = 30,
        echo: bool = False,
    ) -> ExpectResults:
        """
        Executes a command and responds to prompts.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.expect_module>`

        :param command:
            The command module takes command to run.
        :param creates:
            A filename, when it already exists, this step will **not** be run.
        :param removes:
            A filename, when it does not exist, this step will **not** be run.
        :param chdir:
            Change into this directory before running the command.
        :param responses:
            Mapping of prompt regular expressions and corresponding answer(s).
            Each key in ``responses`` is a Python regex
            `regular-expression-syntax <https://docs.python.org/3/library/re.html#regular-expression-syntax>`__.
            The value of each key is a string or list of strings. If the value
            is a string and the prompt is encountered multiple times, the
            answer will be repeated. Provide the value as a list to give
            different answers for successive matches.
        :param timeout:
            Amount of time in seconds to wait for the expected strings. Use
            ``null`` to disable timeout.
        :param echo:
            Whether or not to echo out your response strings.
        """  # noqa: E501
        raise AttributeError('expect')

    def fail(
        self,
        *,
        msg: str = _Unknown,
    ) -> FailResults:
        """
        Fail with custom message.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.fail_module>`

        :param msg:
            The customized message used for failing execution.
            If omitted, fail will simply bail out with a generic message.
        """  # noqa: E501
        raise AttributeError('fail')

    def fetch(
        self,
        *,
        src: str,
        dest: str,
        fail_on_missing: bool = True,
        validate_checksum: bool = True,
        flat: bool = False,
    ) -> FetchResults:
        """
        Fetch files from remote nodes.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.fetch_module>`

        :param src:
            The file on the remote system to fetch.
            This *must* be a file, not a directory.
            Recursive fetching may be supported in a later release.
        :param dest:
            A directory to save the file into.
            For example, if the ``dest`` directory is ``/backup`` a ``src``
            file named ``/etc/profile`` on host ``host.example.com``, would be
            saved into ``/backup/host.example.com/etc/profile``. The host name
            is based on the inventory name.
        :param fail_on_missing:
            When set to ``true``, the task will fail if the remote file cannot
            be read for any reason.
            Prior to Ansible 2.5, setting this would only fail if the source
            file was missing.
            The default was changed to ``true`` in Ansible 2.5.
        :param validate_checksum:
            Verify that the source and destination checksums match after the
            files are fetched.
        :param flat:
            Allows you to override the default behavior of appending
            hostname/path/to/file to the destination.
            If ``dest`` ends with '/', it will use the basename of the source
            file, similar to the copy module.
            This can be useful if working with a single host, or if retrieving
            files that are uniquely named per host.
            If using multiple hosts with the same filename, the file will be
            overwritten for each host.
        """  # noqa: E501
        raise AttributeError('fetch')

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
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
    ) -> FileResults:
        """
        Manage files and file properties.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.file_module>`

        :param path:
            Path to the file being managed.
        :param state:
            If ``absent``, directories will be recursively deleted, and files
            or symlinks will be unlinked. In the case of a directory, if
            ``diff`` is declared, you will see the files and folders deleted
            listed under ``path_contents``. Note that ``absent`` will not
            cause :meth:`file` to fail if the ``path`` does not exist as the
            state did not change.
            If ``directory``, all intermediate subdirectories will be created
            if they do not exist. Since Ansible 1.7 they will be created with
            the supplied permissions.
            If ``file``, with no other options, returns the current state of
            ``path``.
            If ``file``, even with other options (such as ``mode``), the file
            will be modified if it exists but will NOT be created if it does
            not exist. Set to ``touch`` or use the :meth:`copy` or
            :meth:`template` method if you want to create the file if it does
            not exist.
            If ``hard``, the hard link will be created or changed.
            If ``link``, the symbolic link will be created or changed.
            If ``touch`` (new in 1.4), an empty file will be created if the
            file does not exist, while an existing file or directory will
            receive updated file access and modification times (similar to the
            way ``touch`` works from the command line).
            Default is the current state of the file if it exists,
            ``directory`` if ``recurse=yes``, or ``file`` otherwise.
        :param src:
            Path of the file to link to.
            This applies only to ``state=link`` and ``state=hard``.
            For ``state=link``, this will also accept a non-existing path.
            Relative paths are relative to the file being created (``path``)
            which is how the Unix command ``ln -s SRC DEST`` treats relative
            paths.
        :param recurse:
            Recursively set the specified file attributes on directory
            contents.
            This applies only when ``state`` is set to ``directory``.
        :param force:
            Force the creation of the symlinks in two cases: the source file
            does not exist (but will appear later); the destination exists and
            is a file (so, we need to unlink the ``path`` file and create a
            symlink to the ``src`` file in place of it).
        :param follow:
            This flag indicates that filesystem links, if they exist, should
            be followed.
            ``follow=yes`` and ``state=link`` can modify ``src`` when combined
            with parameters such as ``mode``.
            Previous to Ansible 2.5, this was ``false`` by default.
            While creating a symlink with a non-existent destination, set
            ``follow`` to ``false`` to avoid a warning message related to
            permission issues. The warning message is added to notify the user
            that we can not set permissions to the non-existent destination.
        :param modification_time:
            This parameter indicates the time the file's modification time
            should be set to.
            Should be ``preserve`` when no modification is required,
            ``YYYYMMDDHHMM.SS`` when using default time format, or ``now``.
            Default is None meaning that ``preserve`` is the default for
            ``state=[file,directory,link,hard]`` and ``now`` is default for
            ``state=touch``.
        :param modification_time_format:
            When used with ``modification_time``, indicates the time format
            that must be used.
            Based on default Python format (see time.strftime doc).
        :param access_time:
            This parameter indicates the time the file's access time should be
            set to.
            Should be ``preserve`` when no modification is required,
            ``YYYYMMDDHHMM.SS`` when using default time format, or ``now``.
            Default is ``None`` meaning that ``preserve`` is the default for
            ``state=[file,directory,link,hard]`` and ``now`` is default for
            ``state=touch``.
        :param access_time_format:
            When used with ``access_time``, indicates the time format that
            must be used.
            Based on default Python format (see time.strftime doc).
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        """  # noqa: E501
        raise AttributeError('file')

    def find(
        self,
        *,
        age: str = _Unknown,
        patterns: Sequence[str] = _Unknown,
        excludes: Sequence[str] = _Unknown,
        contains: str = _Unknown,
        read_whole_file: bool = False,
        paths: Sequence[str],
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.find_module>`

        :param age:
            Select files whose age is equal to or greater than the specified
            time.
            Use a negative age to find files equal to or less than the
            specified time.
            You can choose seconds, minutes, hours, days, or weeks by
            specifying the first letter of any of those words (e.g., "1w").
        :param patterns:
            One or more (shell or regex) patterns, which type is controlled by
            ``use_regex`` option.
            The patterns restrict the list of files to be returned to those
            whose basenames match at least one of the patterns specified.
            Multiple patterns can be specified using a list.
            The pattern is matched against the file base name, excluding the
            directory.
            When using regexen, the pattern MUST match the ENTIRE file name,
            not just parts of it. So if you are looking to match all files
            ending in .default, you'd need to use ``.*\\.default`` as a regexp
            and not just ``\\.default``.
            This parameter expects a list, which can be either comma separated
            or YAML. If any of the patterns contain a comma, make sure to put
            them in a list to avoid splitting the patterns in undesirable ways.
            Defaults to ``*`` when ``use_regex=False``, or ``.*`` when
            ``use_regex=True``.
        :param excludes:
            One or more (shell or regex) patterns, which type is controlled by
            ``use_regex`` option.
            Items whose basenames match an ``excludes`` pattern are culled
            from ``patterns`` matches. Multiple patterns can be specified
            using a list.
        :param contains:
            A regular expression or pattern which should be matched against
            the file content.
            If ``read_whole_file`` is ``false`` it matches against the
            beginning of the line (uses ``re.match(\\``)). If
            ``read_whole_file`` is ``true``, it searches anywhere for that
            pattern (uses ``re.search(\\``)).
            Works only when ``file_type`` is ``file``.
        :param read_whole_file:
            When doing a ``contains`` search, determines whether the whole
            file should be read into memory or if the regex should be applied
            to the file line-by-line.
            Setting this to ``true`` can have performance and memory
            implications for large files.
            This uses ``re.search(\\``) instead of ``re.match(\\``).
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
            Set this to ``true`` to include hidden files, otherwise they will
            be ignored.
        :param mode:
            Choose objects matching a specified permission. This value is
            restricted to modes that can be applied using the python
            ``os.chmod`` function.
            The mode can be provided as an octal such as ``"0644"`` or as
            symbolic such as ``u=rw,g=r,o=r``.
            Requires ansible-core >= 2.16
        :param exact_mode:
            Restrict mode matching to exact matches only, and not as a minimum
            set of permissions to match.
            Requires ansible-core >= 2.16
        :param follow:
            Set this to ``true`` to follow symlinks in path for systems with
            python 2.6+.
        :param get_checksum:
            Set this to ``true`` to retrieve a file's SHA1 checksum.
        :param use_regex:
            If ``false``, the patterns are file globs (shell).
            If ``true``, they are python regexes.
        :param depth:
            Set the maximum number of levels to descend into.
            Setting recurse to ``false`` will override this value, which is
            effectively depth 1.
            Default is unlimited depth.
        :param encoding:
            When doing a ``contains`` search, determine the encoding of the
            files to be searched.
            Requires ansible-core >= 2.17
        """  # noqa: E501
        raise AttributeError('find')

    def gather_facts(
        self,
        *,
        parallel: bool = _Unknown,
    ) -> GatherFactsResults:
        """
        Gathers facts about remote hosts.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.gather_facts_module>`

        :param parallel:
            A toggle that controls if the fact modules are executed in
            parallel or serially and in order. This can guarantee the merge
            order of module facts at the expense of performance.
            By default it will be true if more than one fact module is used.
            For low cost/delay fact modules parallelism overhead might end up
            meaning the whole process takes longer. Test your specific case to
            see if it is a speed improvement or not.
        """  # noqa: E501
        raise AttributeError('gather_facts')

    def get_url(
        self,
        *,
        ciphers: Sequence[str] = _Unknown,
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
        headers: Mapping[str, Incomplete] = _Unknown,
        url_username: str = _Unknown,
        url_password: str = _Unknown,
        force_basic_auth: bool = False,
        client_cert: StrPath = _Unknown,
        client_key: StrPath = _Unknown,
        http_agent: str = 'ansible-httpget',
        unredirected_headers: Sequence[str] = _Unknown,
        use_gssapi: bool = False,
        use_netrc: bool = True,
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
    ) -> GetUrlResults:
        """
        Downloads files from HTTP, HTTPS, or FTP to node.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.get_url_module>`

        :param ciphers:
            SSL/TLS Ciphers to use for the request.
            When a list is provided, all ciphers are joined in order with
            ``:``.
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
            If ``dest`` is a directory, either the server provided filename
            or, if none provided, the base name of the URL on the remote
            server will be used. If a directory, ``force`` has no effect.
            If ``dest`` is a directory, the file will always be downloaded
            (regardless of the ``force`` and ``checksum`` option), but
            replaced only if the contents changed.
        :param tmp_dest:
            Absolute path of where temporary file is downloaded to.
            When run on Ansible 2.5 or greater, path defaults to ansible's
            remote_tmp setting.
            When run on Ansible prior to 2.5, it defaults to ``TMPDIR``,
            ``TEMP`` or ``TMP`` env variables or a platform specific value.
            `tempfile.tempdir <https://docs.python.org/3/library/tempfile.html#tempfile.tempdir>`__.
        :param force:
            If ``true`` and ``dest`` is not a directory, will download the
            file every time and replace the file if the contents change. If
            ``false``, the file will only be downloaded if the destination
            does not exist. Generally should be ``true`` only for small local
            files.
            Prior to 0.6, this module behaved as if ``true`` was the default.
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
            file exist under the ``dest`` location, the
            ``destination_checksum`` would be calculated, and if checksum
            equals ``destination_checksum``, the file download would be
            skipped (unless ``force`` is ``true``). If the checksum does not
            equal ``destination_checksum``, the destination file is deleted.
        :param use_proxy:
            if ``false``, it will not use a proxy, even if one is defined in
            an environment variable on the target hosts.
        :param validate_certs:
            If ``false``, SSL certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param timeout:
            Timeout in seconds for URL request.
        :param headers:
            Add custom HTTP headers to a request in hash/dict format.
            The hash/dict format was added in Ansible 2.6.
            Previous versions used a ``"key:value,key:value"`` string format.
            The ``"key:value,key:value"`` string format is deprecated and has
            been removed in version 2.10.
        :param url_username:
            The username for use in HTTP basic authentication.
            This parameter can be used without ``url_password`` for sites that
            allow empty passwords.
            Since version 2.8 you can also use the ``username`` alias for this
            option.
        :param url_password:
            The password for use in HTTP basic authentication.
            If the ``url_username`` parameter is not specified, the
            ``url_password`` parameter will not be used.
            Since version 2.8 you can also use the ``password`` alias for this
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
            included, ``client_key`` is not required.
        :param client_key:
            PEM formatted file that contains your private key to be used for
            SSL client authentication.
            If ``client_cert`` contains both the certificate and key, this
            option is not required.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
        :param unredirected_headers:
            A list of header names that will not be sent on subsequent
            redirected requests. This list is case insensitive. By default all
            headers will be redirected. In some cases it may be beneficial to
            list headers such as ``Authorization`` here to avoid potential
            credential exposure.
        :param use_gssapi:
            Use GSSAPI to perform the authentication, typically this is for
            Kerberos or Kerberos through Negotiate authentication.
            Requires the Python library `gssapi
            <https://github.com/pythongssapi/python-gssapi>`__ to be installed.
            Credentials for GSSAPI can be specified with
            ``url_username``/``url_password`` or with the GSSAPI env var
            ``KRB5CCNAME`` that specified a custom Kerberos credential cache.
            NTLM authentication is *not* supported even if the GSSAPI mech for
            NTLM has been installed.
        :param use_netrc:
            Determining whether to use credentials from ``~/.netrc`` file.
            By default .netrc is used with Basic authentication headers.
            When set to False, .netrc credentials are ignored.
            Requires ansible-core >= 2.14
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.getent_module>`

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
        :param split:
            Character used to split the database values into lists/arrays such
            as ``:`` or ``\\t``, otherwise it will try to pick one depending
            on the database.
        :param fail_key:
            If a supplied key is missing this will make the task fail if
            ``true``.
        """  # noqa: E501
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
        gpg_allowlist: Sequence[str] = _Unknown,
    ) -> GitResults:
        """
        Deploy software (or files) from git checkouts.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.git_module>`

        :param repo:
            git, SSH, or HTT``S`` protocol address of the git repository.
        :param dest:
            The path of where the repository should be checked out. This is
            equivalent to ``git clone [repo_url] [directory]``. The repository
            named in ``repo`` is not appended to this path and the destination
            directory must be empty. This parameter is required, unless
            ``clone`` is set to ``false``.
        :param version:
            What version of the repository to check out. This can be the
            literal string ``HEAD``, a branch name, a tag name. It can also be
            a *SHA-1* hash, in which case ``refspec`` needs to be specified if
            the given revision is not already available.
        :param accept_hostkey:
            Will ensure or not that "-o StrictHostKeyChecking=no" is present
            as an ssh option.
            Be aware that this disables a protection against MITM attacks.
            Those using OpenSSH >= 7.5 might want to set ``ssh_opts`` to
            ``StrictHostKeyChecking=accept-new`` instead, it does not remove
            the MITM issue but it does restrict it to the first attempt.
        :param accept_newhostkey:
            As of OpenSSH 7.5, "-o StrictHostKeyChecking=accept-new" can be
            used which is safer and will only accepts host keys which are not
            present or are the same. if ``true``, ensure that "-o
            StrictHostKeyChecking=accept-new" is present as an ssh option.
        :param ssh_opts:
            Options git will pass to ssh when used as protocol, it works via
            ``git``'s ``GIT_SSH``/``GIT_SSH_COMMAND`` environment variables.
            For older versions it appends ``GIT_SSH_OPTS`` (specific to this
            module) to the variables above or via a wrapper script.
            Other options can add to this list, like ``key_file`` and
            ``accept_hostkey``.
            An example value could be "-o StrictHostKeyChecking=no" (although
            this particular option is better set by ``accept_hostkey``).
            The module ensures that 'BatchMode=yes' is always present to avoid
            prompts.
        :param key_file:
            Specify an optional private key file path, on the target host, to
            use for the checkout.
            This ensures 'IdentitiesOnly=yes' is present in ``ssh_opts``.
        :param reference:
            Reference repository (see "git clone --reference ...").
        :param remote:
            Name of the remote.
        :param refspec:
            Add an additional refspec to be fetched. If version is set to a
            *SHA-1* not reachable from any branch or tag, this option may be
            necessary to specify the ref containing the *SHA-1*. Uses the same
            syntax as the ``git fetch`` command. An example value could be
            "refs/meta/config".
        :param force:
            If ``true``, any modified files in the working repository will be
            discarded. Prior to 0.7, this was always ``true`` and could not be
            disabled. Prior to 1.9, the default was ``true``.
        :param depth:
            Create a shallow clone with a history truncated to the specified
            number or revisions. The minimum possible value is ``1``,
            otherwise ignored. Needs *git>=1.9.1* to work correctly.
        :param clone:
            If ``false``, do not clone the repository even if it does not
            exist locally.
        :param update:
            If ``false``, do not retrieve new revisions from the origin
            repository.
            Operations like archive will work on the existing (old) repository
            and might not respond to changes to the options version or remote.
        :param executable:
            Path to git executable to use. If not supplied, the normal
            mechanism for resolving binary paths will be used.
        :param bare:
            If ``true``, repository will be created as a bare repo, otherwise
            it will be a standard repo with a workspace.
        :param umask:
            The umask to set before doing any checkouts, or any other
            repository maintenance.
        :param recursive:
            If ``false``, repository will be cloned without the
            ``--recursive`` option, skipping sub-modules.
        :param single_branch:
            Clone only the history leading to the tip of the specified
            revision.
        :param track_submodules:
            If ``true``, submodules will track the latest commit on their
            master branch (or other branch specified in .gitmodules). If
            ``false``, submodules will be kept at the revision specified by
            the main project. This is equivalent to specifying the
            ``--remote`` flag to git submodule update.
        :param verify_commit:
            If ``true``, when cloning or checking out a ``version`` verify the
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
            ``archive`` to be specified.
        :param separate_git_dir:
            The path to place the cloned repository. If specified, Git
            repository can be separated from working tree.
        :param gpg_allowlist:
            A list of trusted GPG fingerprints to compare to the fingerprint
            of the GPG-signed commit.
            Only used when ``verify_commit=yes``.
            Use of this feature requires Git 2.6+ due to its reliance on git's
            ``--raw`` flag to ``verify-commit`` and ``verify-tag``.
            Alias ``gpg_allowlist`` is added in version 2.17.
            Alias ``gpg_whitelist`` is deprecated and will be removed in
            version 2.21.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.group_module>`

        .. warning::
            The documentation is referring to the module from
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.group_module>`,
            there are however other collections with the same module name, so
            depending on your environment you may be getting one of those
            instead.

            Conflicting collections:

            * :ref:`awx.awx <ansible_collections.awx.awx.group_module>`
            * :ref:`microsoft.ad <ansible_collections.microsoft.ad.group_module>`

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
            If ``True``, indicates that the group created is a system group.
        :param local:
            Forces the use of "local" command alternatives on platforms that
            implement it.
            This is useful in environments that use centralized authentication
            when you want to manipulate the local groups. (for example, it
            uses ``lgroupadd`` instead of ``groupadd``).
            This requires that these commands exist on the targeted host,
            otherwise it will be a fatal error.
        :param non_unique:
            This option allows to change the group ID to a non-unique value.
            Requires ``gid``.
            Not supported on macOS or BusyBox distributions.
        """  # noqa: E501
        raise AttributeError('group')

    def group_by(
        self,
        *,
        key: str,
        parents: Sequence[str] = _Unknown,
    ) -> GroupByResults:
        """
        Create Ansible groups based on facts.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.group_by_module>`

        :param key:
            The variables whose values will be used as groups.
        :param parents:
            The list of the parent groups.
        """  # noqa: E501
        raise AttributeError('group_by')

    def hostname(
        self,
        *,
        name: str,
        use: Literal[
            'alpine',
            'debian',
            'freebsd',
            'generic',
            'macos',
            'macosx',
            'darwin',
            'openbsd',
            'openrc',
            'redhat',
            'sles',
            'solaris',
            'systemd',
        ] = _Unknown,
    ) -> HostnameResults:
        """
        Manage hostname.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.hostname_module>`

        :param name:
            Name of the host.
            If the value is a fully qualified domain name that does not
            resolve from the given host, this will cause the module to hang
            for a few seconds while waiting for the name resolution attempt to
            timeout.
        :param use:
            Which strategy to use to update the hostname.
            If not set we try to autodetect, but this can be problematic,
            particularly with containers as they can present misleading
            information.
            Note that 'systemd' should be specified for RHEL/EL/CentOS 7+.
            Older distributions should use 'redhat'.
        """  # noqa: E501
        raise AttributeError('hostname')

    def import_playbook(self, arg: str, /) -> ImportPlaybookResults:
        """
        Import a playbook.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.import_playbook_module>`
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.import_role_module>`

        :param name:
            The name of the role to be executed.
        :param tasks_from:
            File to load from a role's ``tasks/`` directory.
        :param vars_from:
            File to load from a role's ``vars/`` directory.
        :param defaults_from:
            File to load from a role's ``defaults/`` directory.
        :param allow_duplicates:
            Overrides the role's metadata setting to allow using a role more
            than once with the same parameters.
        :param handlers_from:
            File to load from a role's ``handlers/`` directory.
        :param rolespec_validate:
            Perform role argument spec validation if an argument spec is
            defined.
        :param public:
            This option dictates whether the role's ``vars`` and ``defaults``
            are exposed to the play.
            Variables are exposed to the play at playbook parsing time, and
            available to earlier roles and tasks as well unlike
            ``include_role``.
            The default depends on the configuration option
            `default_private_role_vars`.
            Requires ansible-core >= 2.17
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.import_tasks_module>`

        :param file:
            Specifies the name of the file that lists tasks to add to the
            current playbook.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.include_role_module>`

        :param apply:
            Accepts a hash of task keywords (for example ``tags``, ``become``)
            that will be applied to all tasks within the included role.
        :param name:
            The name of the role to be executed.
        :param tasks_from:
            File to load from a role's ``tasks/`` directory.
        :param vars_from:
            File to load from a role's ``vars/`` directory.
        :param defaults_from:
            File to load from a role's ``defaults/`` directory.
        :param allow_duplicates:
            Overrides the role's metadata setting to allow using a role more
            than once with the same parameters.
        :param public:
            This option dictates whether the role's ``vars`` and ``defaults``
            are exposed to the play. If set to ``true`` the variables will be
            available to tasks following the ``include_role`` task. This
            functionality differs from standard variable exposure for roles
            listed under the ``roles`` header or :meth:`import_role` as they
            are exposed to the play at playbook parsing time, and available to
            earlier roles and tasks as well.
        :param handlers_from:
            File to load from a role's ``handlers/`` directory.
        :param rolespec_validate:
            Perform role argument spec validation if an argument spec is
            defined.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.include_tasks_module>`

        :param file:
            Specifies the name of the file that lists tasks to add to the
            current playbook.
        :param apply:
            Accepts a hash of task keywords (for example ``tags``, ``become``)
            that will be applied to the tasks within the include.
        """  # noqa: E501
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
        ignore_files: Sequence[str] = _Unknown,
        extensions: Sequence[str] = _Unknown,
        ignore_unknown_extensions: bool = False,
        hash_behaviour: Literal['replace', 'merge'] = _Unknown,
    ) -> IncludeVarsResults: ...

    @overload
    def include_vars(self, arg: str, /) -> IncludeVarsResults: ...

    def include_vars(self, *args: Any, **kwargs: Any) -> IncludeVarsResults:
        """
        Load variables from files, dynamically within a task.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.include_vars_module>`

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
            When using ``dir``, this module will, by default, recursively go
            through each sub directory and load up the variables. By
            explicitly setting the depth, this module will only go as deep as
            the depth.
        :param files_matching:
            Limit the files that are loaded within any directory to this
            regular expression.
        :param ignore_files:
            List of file names to ignore.
        :param extensions:
            List of file extensions to read when using ``dir``.
        :param ignore_unknown_extensions:
            Ignore unknown file extensions within the directory.
            This allows users to specify a directory containing vars files
            that are intermingled with non-vars files extension types (e.g. a
            directory with a README in it and vars files).
        :param hash_behaviour:
            If set to ``merge``, merges existing hash variables instead of
            overwriting them.
            If omitted (``null``), the behavior falls back to the global
            ``hash_behaviour`` configuration.
            This option is self-contained and does not apply to individual
            files in ``dir``. You can use a loop to apply ``hash_behaviour``
            per file.
        """  # noqa: E501
        raise AttributeError('include_vars')

    def iptables(
        self,
        *,
        table: Literal[
            'filter',
            'nat',
            'mangle',
            'raw',
            'security',
        ] = 'filter',
        state: Literal['absent', 'present'] = 'present',
        action: Literal['append', 'insert'] = 'append',
        rule_num: str = _Unknown,
        ip_version: Literal['ipv4', 'ipv6'] = 'ipv4',
        chain: str = _Unknown,
        protocol: str = _Unknown,
        source: str = _Unknown,
        destination: str = _Unknown,
        tcp_flags: Mapping[str, Incomplete] = _Unknown,
        match: Sequence[str] = _Unknown,
        jump: str = _Unknown,
        gateway: str = _Unknown,
        log_prefix: str = _Unknown,
        log_level: Literal[
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            'emerg',
            'alert',
            'crit',
            'error',
            'warning',
            'notice',
            'info',
            'debug',
        ] = _Unknown,
        goto: str = _Unknown,
        in_interface: str = _Unknown,
        out_interface: str = _Unknown,
        fragment: str = _Unknown,
        set_counters: str = _Unknown,
        source_port: str = _Unknown,
        destination_port: str = _Unknown,
        destination_ports: Sequence[str] = _Unknown,
        to_ports: str = _Unknown,
        to_destination: str = _Unknown,
        to_source: str = _Unknown,
        syn: Literal['ignore', 'match', 'negate'] = 'ignore',
        set_dscp_mark: str = _Unknown,
        set_dscp_mark_class: str = _Unknown,
        comment: str = _Unknown,
        ctstate: Sequence[str] = _Unknown,
        src_range: str = _Unknown,
        dst_range: str = _Unknown,
        match_set: str = _Unknown,
        match_set_flags: Literal[
            'src',
            'dst',
            'src,dst',
            'dst,src',
            'dst,dst',
            'src,src',
        ] = _Unknown,
        limit: str = _Unknown,
        limit_burst: str = _Unknown,
        uid_owner: str = _Unknown,
        gid_owner: str = _Unknown,
        reject_with: str = _Unknown,
        icmp_type: str = _Unknown,
        flush: bool = False,
        policy: Literal['ACCEPT', 'DROP', 'QUEUE', 'RETURN'] = _Unknown,
        wait: str = _Unknown,
        chain_management: bool = False,
        numeric: bool = False,
    ) -> IptablesResults:
        """
        Modify iptables rules.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.iptables_module>`

        :param table:
            This option specifies the packet matching table on which the
            command should operate.
            If the kernel is configured with automatic module loading, an
            attempt will be made to load the appropriate module for that table
            if it is not already there.
        :param state:
            Whether the rule should be absent or present.
        :param action:
            Whether the rule should be appended at the bottom or inserted at
            the top.
            If the rule already exists the chain will not be modified.
        :param rule_num:
            Insert the rule as the given rule number.
            This works only with ``action=insert``.
        :param ip_version:
            Which version of the IP protocol this rule should apply to.
        :param chain:
            Specify the iptables chain to modify.
            This could be a user-defined chain or one of the standard iptables
            chains, like ``INPUT``, ``FORWARD``, ``OUTPUT``, ``PREROUTING``,
            ``POSTROUTING``, ``SECMARK`` or ``CONNSECMARK``.
        :param protocol:
            The protocol of the rule or of the packet to check.
            The specified protocol can be one of ``tcp``, ``udp``,
            ``udplite``, ``icmp``, ``ipv6-icmp`` or ``icmpv6``, ``esp``,
            ``ah``, ``sctp`` or the special keyword ``all``, or it can be a
            numeric value, representing one of these protocols or a different
            one.
            A protocol name from ``/etc/protocols`` is also allowed.
            A ``!`` argument before the protocol inverts the test.
            The number zero is equivalent to all.
            ``all`` will match with all protocols and is taken as default when
            this option is omitted.
        :param source:
            Source specification.
            Address can be either a network name, a hostname, a network IP
            address (with /mask), or a plain IP address.
            Hostnames will be resolved once only, before the rule is submitted
            to the kernel. Please note that specifying any name to be resolved
            with a remote query such as DNS is a really bad idea.
            The mask can be either a network mask or a plain number,
            specifying the number of 1's at the left side of the network mask.
            Thus, a mask of 24 is equivalent to 255.255.255.0. A ``!``
            argument before the address specification inverts the sense of the
            address.
        :param destination:
            Destination specification.
            Address can be either a network name, a hostname, a network IP
            address (with /mask), or a plain IP address.
            Hostnames will be resolved once only, before the rule is submitted
            to the kernel. Please note that specifying any name to be resolved
            with a remote query such as DNS is a really bad idea.
            The mask can be either a network mask or a plain number,
            specifying the number of 1's at the left side of the network mask.
            Thus, a mask of 24 is equivalent to 255.255.255.0. A ``!``
            argument before the address specification inverts the sense of the
            address.
        :param tcp_flags:
            TCP flags specification.
            ``tcp_flags`` expects a dict with the two keys ``flags`` and
            ``flags_set``.
        :param match:
            Specifies a match to use, that is, an extension module that tests
            for a specific property.
            The set of matches makes up the condition under which a target is
            invoked.
            Matches are evaluated first to last if specified as an array and
            work in short-circuit fashion, i.e. if one extension yields false,
            the evaluation will stop.
        :param jump:
            This specifies the target of the rule; i.e., what to do if the
            packet matches it.
            The target can be a user-defined chain (other than the one this
            rule is in), one of the special builtin targets that decide the
            fate of the packet immediately, or an extension (see EXTENSIONS
            below).
            If this option is omitted in a rule (and the goto parameter is not
            used), then matching the rule will have no effect on the packet's
            fate, but the counters on the rule will be incremented.
        :param gateway:
            This specifies the IP address of the host to send the cloned
            packets.
            This option is only valid when ``jump`` is set to ``TEE``.
        :param log_prefix:
            Specifies a log text for the rule. Only makes sense with a LOG
            jump.
        :param log_level:
            Logging level according to the syslogd-defined priorities.
            The value can be strings or numbers from 1-8.
            This parameter is only applicable if ``jump`` is set to ``LOG``.
        :param goto:
            This specifies that the processing should continue in a
            user-specified chain.
            Unlike the jump argument return will not continue processing in
            this chain but instead in the chain that called us via jump.
        :param in_interface:
            Name of an interface via which a packet was received (only for
            packets entering the ``INPUT``, ``FORWARD`` and ``PREROUTING``
            chains).
            When the ``!`` argument is used before the interface name, the
            sense is inverted.
            If the interface name ends in a ``+``, then any interface which
            begins with this name will match.
            If this option is omitted, any interface name will match.
        :param out_interface:
            Name of an interface via which a packet is going to be sent (for
            packets entering the ``FORWARD``, ``OUTPUT`` and ``POSTROUTING``
            chains).
            When the ``!`` argument is used before the interface name, the
            sense is inverted.
            If the interface name ends in a ``+``, then any interface which
            begins with this name will match.
            If this option is omitted, any interface name will match.
        :param fragment:
            This means that the rule only refers to second and further
            fragments of fragmented packets.
            Since there is no way to tell the source or destination ports of
            such a packet (or ICMP type), such a packet will not match any
            rules which specify them.
            When the "!" argument precedes the fragment argument, the rule
            will only match head fragments, or unfragmented packets.
        :param set_counters:
            This enables the administrator to initialize the packet and byte
            counters of a rule (during ``INSERT``, ``APPEND``, ``REPLACE``
            operations).
        :param source_port:
            Source port or port range specification.
            This can either be a service name or a port number.
            An inclusive range can also be specified, using the format
            ``first:last``.
            If the first port is omitted, ``0`` is assumed; if the last is
            omitted, ``65535`` is assumed.
            If the first port is greater than the second one they will be
            swapped.
        :param destination_port:
            Destination port or port range specification. This can either be a
            service name or a port number. An inclusive range can also be
            specified, using the format first:last. If the first port is
            omitted, '0' is assumed; if the last is omitted, '65535' is
            assumed. If the first port is greater than the second one they
            will be swapped. This is only valid if the rule also specifies one
            of the following protocols: tcp, udp, dccp or sctp.
        :param destination_ports:
            This specifies multiple destination port numbers or port ranges to
            match in the multiport module.
            It can only be used in conjunction with the protocols tcp, udp,
            udplite, dccp and sctp.
        :param to_ports:
            This specifies a destination port or range of ports to use,
            without this, the destination port is never altered.
            This is only valid if the rule also specifies one of the protocol
            ``tcp``, ``udp``, ``dccp`` or ``sctp``.
        :param to_destination:
            This specifies a destination address to use with ``DNAT``.
            Without this, the destination address is never altered.
        :param to_source:
            This specifies a source address to use with ``SNAT``.
            Without this, the source address is never altered.
        :param syn:
            This allows matching packets that have the SYN bit set and the ACK
            and RST bits unset.
            When negated, this matches all packets with the RST or the ACK
            bits set.
        :param set_dscp_mark:
            This allows specifying a DSCP mark to be added to packets. It
            takes either an integer or hex value.
            If the parameter is set, ``jump`` is set to ``DSCP``.
            Mutually exclusive with ``set_dscp_mark_class``.
        :param set_dscp_mark_class:
            This allows specifying a predefined DiffServ class which will be
            translated to the corresponding DSCP mark.
            If the parameter is set, ``jump`` is set to ``DSCP``.
            Mutually exclusive with ``set_dscp_mark``.
        :param comment:
            This specifies a comment that will be added to the rule.
        :param ctstate:
            A list of the connection states to match in the conntrack module.
            Possible values are ``INVALID``, ``NEW``, ``ESTABLISHED``,
            ``RELATED``, ``UNTRACKED``, ``SNAT``, ``DNAT``.
        :param src_range:
            Specifies the source IP range to match the iprange module.
        :param dst_range:
            Specifies the destination IP range to match in the iprange module.
        :param match_set:
            Specifies a set name that can be defined by ipset.
            Must be used together with the ``match_set_flags`` parameter.
            When the ``!`` argument is prepended then it inverts the rule.
            Uses the iptables set extension.
        :param match_set_flags:
            Specifies the necessary flags for the match_set parameter.
            Must be used together with the ``match_set`` parameter.
            Uses the iptables set extension.
            Choices ``dst,dst`` and ``src,src`` added in version 2.17.
        :param limit:
            Specifies the maximum average number of matches to allow per
            second.
            The number can specify units explicitly, using ``/second``,
            ``/minute``, ``/hour`` or ``/day``, or parts of them (so
            ``5/second`` is the same as ``5/s``).
        :param limit_burst:
            Specifies the maximum burst before the above limit kicks in.
        :param uid_owner:
            Specifies the UID or username to use in the match by owner rule.
            From Ansible 2.6 when the ``!`` argument is prepended then the it
            inverts the rule to apply instead to all users except that one
            specified.
        :param gid_owner:
            Specifies the GID or group to use in the match by owner rule.
        :param reject_with:
            Specifies the error packet type to return while rejecting. It
            implies "jump: REJECT".
        :param icmp_type:
            This allows specification of the ICMP type, which can be a numeric
            ICMP type, type/code pair, or one of the ICMP type names shown by
            the command 'iptables -p icmp -h'.
        :param flush:
            Flushes the specified table and chain of all rules.
            If no chain is specified then the entire table is purged.
            Ignores all other parameters.
        :param policy:
            Set the policy for the chain to the given target.
            Only built-in chains can have policies.
            This parameter requires the ``chain`` parameter.
            If you specify this parameter, all other parameters will be
            ignored.
            This parameter is used to set the default policy for the given
            ``chain``. Do not confuse this with ``jump`` parameter.
        :param wait:
            Wait N seconds for the xtables lock to prevent multiple instances
            of the program from running concurrently.
        :param chain_management:
            If ``true`` and ``state`` is ``present``, the chain will be
            created if needed.
            If ``true`` and ``state`` is ``absent``, the chain will be deleted
            if the only other parameter passed are ``chain`` and optionally
            ``table``.
        :param numeric:
            This parameter controls the running of the list -action of
            iptables, which is used internally by the module.
            Does not affect the actual functionality. Use this if iptables
            hang when creating a chain or altering policy.
            If ``true``, then iptables skips the DNS-lookup of the IP
            addresses in a chain when it uses the list -action.
            Listing is used internally for example when setting a policy or
            creating a chain.
            Requires ansible-core >= 2.15
        """  # noqa: E501
        raise AttributeError('iptables')

    def known_hosts(
        self,
        *,
        name: str,
        key: str = _Unknown,
        path: StrPath = '~/.ssh/known_hosts',
        hash_host: bool = False,
        state: Literal['absent', 'present'] = 'present',
    ) -> KnownHostsResults:
        """
        Add or remove a host from the ``known_hosts`` file.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.known_hosts_module>`

        :param name:
            The host to add or remove (must match a host specified in key). It
            will be converted to lowercase so that ssh-keygen can find it.
            Must match with <hostname> or <ip> present in key attribute.
            For custom SSH port, ``name`` needs to specify port as well. See
            example section.
        :param key:
            The SSH public host key, as a string.
            Required if ``state=present``, optional when ``state=absent``, in
            which case all keys for the host are removed.
            The key must be in the right format for SSH (see sshd(8), section
            "SSH_KNOWN_HOSTS FILE FORMAT").
            Specifically, the key should not match the format that is found in
            an SSH pubkey file, but should rather have the hostname prepended
            to a line that includes the pubkey, the same way that it would
            appear in the known_hosts file. The value prepended to the line
            must also match the value of the name parameter.
            Should be of format ``<hostname[,IP]> ssh-rsa <pubkey>``.
            For custom SSH port, ``key`` needs to specify port as well. See
            example section.
        :param path:
            The known_hosts file to edit.
            The known_hosts file will be created if needed. The rest of the
            path must exist prior to running the module.
        :param hash_host:
            Hash the hostname in the known_hosts file.
        :param state:
            ``present`` to add the host key.
            ``absent`` to remove it.
        """  # noqa: E501
        raise AttributeError('known_hosts')

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
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
        validate: str = _Unknown,
    ) -> LineinfileResults:
        """
        Manage lines in text files.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.lineinfile_module>`

        :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as ``dest``,
            ``destfile`` and ``name``.
        :param regexp:
            The regular expression to look for in every line of the file.
            For ``state=present``, the pattern to replace if found. Only the
            last line found will be replaced.
            For ``state=absent``, the pattern of the line(s) to remove.
            If the regular expression is not matched, the line will be added
            to the file in keeping with ``insertbefore`` or ``insertafter``
            settings.
            When modifying a line the regexp should typically match both the
            initial state of the line as well as its state after replacement
            by ``line`` to ensure idempotence.
            Uses Python regular expressions. See
            `reference <https://docs.python.org/3/library/re.html>`__.
        :param search_string:
            The literal string to look for in every line of the file. This
            does not have to match the entire line.
            For ``state=present``, the line to replace if the string is found
            in the file. Only the last line found will be replaced.
            For ``state=absent``, the line(s) to remove if the string is in
            the line.
            If the literal expression is not matched, the line will be added
            to the file in keeping with ``insertbefore`` or ``insertafter``
            settings.
            Mutually exclusive with ``backrefs`` and ``regexp``.
        :param state:
            Whether the line should be there or not.
        :param line:
            The line to insert/replace into the file.
            Required for ``state=present``.
            If ``backrefs`` is set, may contain backreferences that will get
            expanded with the ``regexp`` capture groups if the regexp matches.
        :param backrefs:
            Used with ``state=present``.
            If set, ``line`` can contain backreferences (both positional and
            named) that will get populated if the ``regexp`` matches.
            This parameter changes the operation of the module slightly;
            ``insertbefore`` and ``insertafter`` will be ignored, and if the
            ``regexp`` does not match anywhere in the file, the file will be
            left unchanged.
            If the ``regexp`` does match, the last matching line will be
            replaced by the expanded line parameter.
            Mutually exclusive with ``search_string``.
        :param insertafter:
            Used with ``state=present``.
            If specified, the line will be inserted after the last match of
            specified regular expression.
            If the first match is required, use(firstmatch=yes).
            A special value is available; ``EOF`` for inserting the line at
            the end of the file.
            If specified regular expression has no matches, EOF will be used
            instead.
            If ``insertbefore`` is set, default value ``EOF`` will be ignored.
            If regular expressions are passed to both ``regexp`` and
            ``insertafter``, ``insertafter`` is only honored if no match for
            ``regexp`` is found.
            May not be used with ``backrefs`` or ``insertbefore``.
        :param insertbefore:
            Used with ``state=present``.
            If specified, the line will be inserted before the last match of
            specified regular expression.
            If the first match is required, use ``firstmatch=yes``.
            A value is available; ``BOF`` for inserting the line at the
            beginning of the file.
            If specified regular expression has no matches, the line will be
            inserted at the end of the file.
            If regular expressions are passed to both ``regexp`` and
            ``insertbefore``, ``insertbefore`` is only honored if no match for
            ``regexp`` is found.
            May not be used with ``backrefs`` or ``insertafter``.
        :param create:
            Used with ``state=present``.
            If specified, the file will be created if it does not already
            exist.
            By default it will fail if the file is missing.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param firstmatch:
            Used with ``insertafter`` or ``insertbefore``.
            If set, ``insertafter`` and ``insertbefore`` will work with the
            first line that matches the given regular expression.
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        :param validate:
            The validation command to run before copying the updated file into
            the final destination.
            A temporary file path is used to validate, passed in through '%s'
            which must be present as in the examples below.
            Also, the command is passed securely so shell features such as
            expansion and pipes will not work.
            For an example on how to handle more complex validation than what
            this option provides, see ``handling complex validation``.
        """  # noqa: E501
        raise AttributeError('lineinfile')

    def meta(self, arg: str, /) -> MetaResults:
        """
        Execute Ansible 'actions'.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.meta_module>`
        """  # noqa: E501
        raise AttributeError('meta')

    def package(
        self,
        *,
        name: str,
        state: str,
        use: str = 'auto',
    ) -> PackageResults:
        """
        Generic OS package manager.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.package_module>`

        :param name:
            Package name, or package specifier with version.
            Syntax varies with package manager. For example ``name-1.0`` or
            ``name=1.0``.
            Package names also vary with package manager; this module will not
            "translate" them per distribution. For example ``libyaml-dev``,
            ``libyaml-devel``.
            To operate on several packages this can accept a comma separated
            string of packages or a list of packages, depending on the
            underlying package manager.
        :param state:
            Whether to install (``present``), or remove (``absent``) a package.
            You can use other states like ``latest`` ONLY if they are
            supported by the underlying package module(s) executed.
        :param use:
            The required package manager module to use (``dnf``, ``apt``, and
            so on). The default ``auto`` will use existing facts or try to
            auto-detect it.
            You should only use this field if the automatic selection is not
            working for some reason.
            Since version 2.17 you can use the ``ansible_package_use``
            variable to override the automatic detection, but this option
            still takes precedence.
        """  # noqa: E501
        raise AttributeError('package')

    def package_facts(
        self,
        *,
        manager: Sequence[str] = _Unknown,
        strategy: Literal['first', 'all'] = 'first',
    ) -> PackageFactsResults:
        """
        Package information as facts.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.package_facts_module>`

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
            on the system. ``first`` means it will return only information for
            the first supported package manager available. ``all`` will return
            information for all supported and available package managers on
            the system.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.pause_module>`

        :param minutes:
            A positive number of minutes to pause for.
        :param seconds:
            A positive number of seconds to pause for.
        :param prompt:
            Optional text to use for the prompt message.
            User input is only returned if ``seconds=None`` and
            ``minutes=None``, otherwise this is just a custom message before
            playbook execution is paused.
        :param echo:
            Controls whether or not keyboard input is shown when typing.
            Only has effect if ``seconds=None`` and ``minutes=None``.
        """  # noqa: E501
        raise AttributeError('pause')

    def ping(
        self,
        *,
        data: str = 'pong',
    ) -> PingResults:
        """
        Try to connect to host, verify a usable python and return ``pong`` on
        success.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.ping_module>`

        :param data:
            Data to return for the ``ping`` return value.
            If this parameter is set to ``crash``, the module will cause an
            exception.
        """  # noqa: E501
        raise AttributeError('ping')

    def pip(
        self,
        *,
        name: Sequence[str] = _Unknown,
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.pip_module>`

        :param name:
            The name of a Python library to install or the
            url(bzr+,hg+,git+,svn+) of the remote package.
            This can be a list (since 2.2) and contain version specifiers
            (since 2.7).
        :param version:
            The version number to install of the Python library specified in
            the ``name`` parameter.
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
            global site-packages directory. Note that if this setting is
            changed on an already existing virtual environment it will not
            have any effect, the environment must be deleted and newly created.
        :param virtualenv_command:
            The command or a pathname to the command to create the virtual
            environment with. For example ``pyvenv``, ``virtualenv``,
            ``virtualenv2``, ``~/bin/virtualenv``,
            ``/usr/local/bin/virtualenv``.
        :param virtualenv_python:
            The Python executable used for creating the virtual environment.
            For example ``python3.12``, ``python2.7``. When not specified, the
            Python version used to run the ansible module is used. This
            parameter should not be used when ``virtualenv_command`` is using
            ``pyvenv`` or the ``-m venv`` module.
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
            ``pip3.3``, if there are both Python 2.7 and 3.3 installations in
            the system and you want to run pip for the Python 3.3 installation.
            Mutually exclusive with ``virtualenv`` (added in 2.1).
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
        """  # noqa: E501
        raise AttributeError('pip')

    @overload
    def raw(
        self,
        *,
        executable: str = _Unknown,
    ) -> RawResults: ...

    @overload
    def raw(self, arg: str, /) -> RawResults: ...

    def raw(self, *args: Any, **kwargs: Any) -> RawResults:
        """
        Executes a low-down and dirty command.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.raw_module>`

        :param executable:
            Change the shell used to execute the command. Should be an
            absolute path to the executable.
            When using privilege escalation (``become``) a default shell will
            be assigned if one is not provided as privilege escalation
            requires a shell.
        """  # noqa: E501
        raise AttributeError('raw')

    def reboot(
        self,
        *,
        pre_reboot_delay: int = 0,
        post_reboot_delay: int = 0,
        reboot_timeout: int = 600,
        connect_timeout: int = _Unknown,
        test_command: str = 'whoami',
        msg: str = _Unknown,
        search_paths: Sequence[str] = _Unknown,
        boot_time_command: str = _Unknown,
        reboot_command: str = _Unknown,
    ) -> RebootResults:
        """
        Reboot a machine.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.reboot_module>`

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
            Paths to search on the remote machine for the ``shutdown`` command.
            *Only* these paths will be searched for the ``shutdown`` command.
            ``PATH`` is ignored in the remote node when searching for the
            ``shutdown`` command.
        :param boot_time_command:
            Command to run that returns a unique string indicating the last
            time the system was booted.
            Setting this to a command that has different output each time it
            is run will cause the task to fail.
        :param reboot_command:
            Command to run that reboots the system, including any parameters
            passed to the command.
            Can be an absolute path to the command or just the command name.
            If an absolute path to the command is not given, ``search_paths``
            on the target system will be searched to find the absolute path.
            This will cause ``pre_reboot_delay``, ``post_reboot_delay``, and
            ``msg`` to be ignored.
        """  # noqa: E501
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
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
        validate: str = _Unknown,
    ) -> ReplaceResults:
        """
        Replace all instances of a particular string in a file using a
        back-referenced regular expression.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.replace_module>`

        :param path:
            The file to modify.
            Before Ansible 2.3 this option was only usable as ``dest``,
            ``destfile`` and ``name``.
        :param regexp:
            The regular expression to look for in the contents of the file.
            Uses Python regular expressions; see
            `reference <https://docs.python.org/3/library/re.html>`__.
            Uses MULTILINE mode, which means ``^`` and ``$`` match the
            beginning and end of the file, as well as the beginning and end
            respectively of *each line* of the file.
            Does not use DOTALL, which means the ``.`` special character
            matches any character *except newlines*. A common mistake is to
            assume that a negated character set like ``[^#]`` will also not
            match newlines.
            In order to exclude newlines, they must be added to the set like
            ``[^#\\n]``.
            Note that, as of Ansible 2.0, short form tasks should have any
            escape sequences backslash-escaped in order to prevent them being
            parsed as string literal escapes. See the examples.
        :param replace:
            The string to replace regexp matches.
            May contain backreferences that will get expanded with the regexp
            capture groups if the regexp matches.
            If not set, matches are removed entirely.
            Backreferences can be used ambiguously like ``\\1``, or explicitly
            like ``\\g<1>``.
        :param after:
            If specified, only content after this match will be
            replaced/removed.
            Can be used in combination with ``before``.
            Uses Python regular expressions; see
            `reference <https://docs.python.org/3/library/re.html>`__.
            Uses DOTALL, which means the ``.`` special character *can match
            newlines*.
            Does not use MULTILINE, so ``^`` and ``$`` will only match the
            beginning and end of the file.
        :param before:
            If specified, only content before this match will be
            replaced/removed.
            Can be used in combination with ``after``.
            Uses Python regular expressions; see
            `reference <https://docs.python.org/3/library/re.html>`__.
            Uses DOTALL, which means the ``.`` special character *can match
            newlines*.
            Does not use MULTILINE, so ``^`` and ``$`` will only match the
            beginning and end of the file.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param others:
            All arguments accepted by the :meth:`file` method also work here.
        :param encoding:
            The character encoding for reading and writing the file.
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        :param validate:
            The validation command to run before copying the updated file into
            the final destination.
            A temporary file path is used to validate, passed in through '%s'
            which must be present as in the examples below.
            Also, the command is passed securely so shell features such as
            expansion and pipes will not work.
            For an example on how to handle more complex validation than what
            this option provides, see ``handling complex validation``.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.rpm_key_module>`

        :param key:
            Key that will be modified. Can be a url, a file on the managed
            node, or a keyid if the key already exists in the database.
        :param state:
            If the key will be imported or removed from the rpm db.
        :param validate_certs:
            If ``false`` and the ``key`` is a url starting with ``https``, SSL
            certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param fingerprint:
            The long-form fingerprint of the key being imported.
            This will be used to verify the specified key.
        """  # noqa: E501
        raise AttributeError('rpm_key')

    @overload
    def script(
        self,
        *,
        cmd: str = _Unknown,
        creates: str = _Unknown,
        removes: str = _Unknown,
        chdir: str = _Unknown,
        executable: str = _Unknown,
        decrypt: bool = True,
    ) -> ScriptResults: ...

    @overload
    def script(self, arg: str, /) -> ScriptResults: ...

    def script(self, *args: Any, **kwargs: Any) -> ScriptResults:
        """
        Runs a local script on a remote node after transferring it.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.script_module>`

        :param cmd:
            Path to the local script to run followed by optional arguments.
        :param creates:
            A filename on the remote node, when it already exists, this step
            will **not** be run.
        :param removes:
            A filename on the remote node, when it does not exist, this step
            will **not** be run.
        :param chdir:
            Change into this directory on the remote node before running the
            script.
        :param executable:
            Name or path of an executable to invoke the script with.
        :param decrypt:
            This option controls the auto-decryption of source files using
            vault.
        """  # noqa: E501
        raise AttributeError('script')

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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.service_module>`

        :param name:
            Name of the service.
        :param state:
            ``started``/``stopped`` are idempotent actions that will not run
            commands unless necessary.
            ``restarted`` will always bounce the service.
            ``reloaded`` will always reload.
            **At least one of state and enabled are required.**.
            Note that reloaded will start the service if it is not already
            started, even if your chosen init system wouldn't normally.
        :param sleep:
            If the service is being ``restarted`` then sleep this many seconds
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
            does it correspond to the ``service`` command.
        """  # noqa: E501
        raise AttributeError('service')

    def service_facts(self) -> ServiceFactsResults:
        """
        Return service state information as fact data.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.service_facts_module>`
        """  # noqa: E501
        raise AttributeError('service_facts')

    def set_fact(
        self,
        *,
        key_value: str,
        cacheable: bool = False,
    ) -> SetFactResults:
        """
        Set host variable(s) and fact(s).

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.set_fact_module>`

        :param key_value:
            The :meth:`set_fact` method takes ``key=value`` pairs or
            ``key: value`` (YAML notation) as variables to set in the playbook
            scope. The 'key' is the resulting variable name and the value is,
            of course, the value of said variable.
            You can create multiple variables at once, by supplying multiple
            pairs, but do NOT mix notations.
        :param cacheable:
            This boolean converts the variable into an actual 'fact' which
            will also be added to the fact cache. It does not enable fact
            caching across runs, it just means it will work with it if already
            enabled.
            Normally this module creates 'host level variables' and has much
            higher precedence, this option changes the nature and precedence
            (by 7 steps) of the variable created.
            `variable-precedence-where-should-i-put-a-variable <https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable>`__.
            This actually creates 2 copies of the variable, a normal
            'set_fact' host variable with high precedence and a lower
            'ansible_fact' one that is available for persistence via the facts
            cache plugin. This creates a possibly confusing interaction with
            ``meta: clear_facts`` as it will remove the 'ansible_fact' but not
            the host variable.
        """  # noqa: E501
        raise AttributeError('set_fact')

    def set_stats(
        self,
        *,
        data: Mapping[str, Incomplete],
        per_host: bool = False,
        aggregate: bool = True,
    ) -> SetStatsResults:
        """
        Define and display stats for the current ansible run.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.set_stats_module>`

        :param data:
            A dictionary of which each key represents a stat (or variable) you
            want to keep track of.
        :param per_host:
            whether the stats are per host or for all hosts in the run.
        :param aggregate:
            Whether the provided value is aggregated to the existing stat
            ``true`` or will replace it ``false``.
        """  # noqa: E501
        raise AttributeError('set_stats')

    def setup(
        self,
        *,
        gather_subset: Sequence[str] = _Unknown,
        gather_timeout: int = 10,
        filter: Sequence[str] = _Unknown,
        fact_path: StrPath = '/etc/ansible/facts.d',
    ) -> SetupResults:
        """
        Gathers facts about remote hosts.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.setup_module>`

        .. warning::
            The documentation is referring to the module from
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.setup_module>`,
            there are however other collections with the same module name, so
            depending on your environment you may be getting one of those
            instead.

            Conflicting collections:

            * :ref:`ansible.windows <ansible_collections.ansible.windows.setup_module>`

        :param gather_subset:
            If supplied, restrict the additional facts collected to the given
            subset. Possible values: ``all``, ``all_ipv4_addresses``,
            ``all_ipv6_addresses``, ``apparmor``, ``architecture``, ``caps``,
            ``chroot``,``cmdline``, ``date_time``, ``default_ipv4``,
            ``default_ipv6``, ``devices``, ``distribution``,
            ``distribution_major_version``, ``distribution_release``,
            ``distribution_version``, ``dns``, ``effective_group_ids``,
            ``effective_user_id``, ``env``, ``facter``, ``fips``,
            ``hardware``, ``interfaces``, ``is_chroot``, ``iscsi``,
            ``kernel``, ``local``, ``lsb``, ``machine``, ``machine_id``,
            ``mounts``, ``network``, ``ohai``, ``os_family``, ``pkg_mgr``,
            ``platform``, ``processor``, ``processor_cores``,
            ``processor_count``, ``python``, ``python_version``,
            ``real_user_id``, ``selinux``, ``service_mgr``,
            ``ssh_host_key_dsa_public``, ``ssh_host_key_ecdsa_public``,
            ``ssh_host_key_ed25519_public``, ``ssh_host_key_rsa_public``,
            ``ssh_host_pub_keys``, ``ssh_pub_keys``, ``system``,
            ``system_capabilities``, ``system_capabilities_enforced``,
            ``user``, ``user_dir``, ``user_gecos``, ``user_gid``, ``user_id``,
            ``user_shell``, ``user_uid``, ``virtual``,
            ``virtualization_role``, ``virtualization_type``. Can specify a
            list of values to specify a larger subset. Values can also be used
            with an initial ``!`` to specify that that specific subset should
            not be collected. For instance:
            ``!hardware,!network,!virtual,!ohai,!facter``. If ``!all`` is
            specified then only the min subset is collected. To avoid
            collecting even the min subset, specify ``!all,!min``. To collect
            only specific facts, use ``!all,!min``, and specify the particular
            fact subsets. Use the filter parameter if you do not want to
            display some collected facts.
        :param gather_timeout:
            Set the default timeout in seconds for individual fact gathering.
        :param filter:
            If supplied, only return facts that match one of the shell-style
            (fnmatch) pattern. An empty list basically means 'no filter'. As
            of Ansible 2.11, the type has changed from string to list and the
            default has became an empty list. A simple string is still
            accepted and works as a single pattern. The behaviour prior to
            Ansible 2.11 remains.
        :param fact_path:
            Path used for local ansible facts (``*.fact``) - files in this dir
            will be run (if executable) and their results be added to
            ``ansible_local`` facts. If a file is not executable it is read
            instead. File/results format can be JSON or INI-format. The
            default ``fact_path`` can be specified in ``ansible.cfg`` for when
            setup is automatically called as part of ``gather_facts``. NOTE -
            For windows clients, the results will be added to a variable named
            after the local file (without extension suffix), rather than
            ``ansible_local``.
            Since Ansible 2.1, Windows hosts can use ``fact_path``. Make sure
            that this path exists on the target host. Files in this path MUST
            be PowerShell scripts ``.ps1`` which outputs an object. This
            object will be formatted by Ansible as json so the script should
            be outputting a raw hashtable, array, or other primitive object.
        """  # noqa: E501
        raise AttributeError('setup')

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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.shell_module>`

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
        """  # noqa: E501
        raise AttributeError('shell')

    def slurp(
        self,
        *,
        src: StrPath,
    ) -> SlurpResults:
        """
        Slurps a file from remote nodes.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.slurp_module>`

        .. warning::
            The documentation is referring to the module from
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.slurp_module>`,
            there are however other collections with the same module name, so
            depending on your environment you may be getting one of those
            instead.

            Conflicting collections:

            * :ref:`ansible.windows <ansible_collections.ansible.windows.slurp_module>`

        :param src:
            The file on the remote system to fetch. This *must* be a file, not
            a directory.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.stat_module>`

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
            The remote host has to support the hashing method specified,
            ``md5`` can be unavailable if the host is FIPS-140 compliant.
        :param get_mime:
            Use file magic and return data about the nature of the file. this
            uses the 'file' utility found on most Linux/Unix systems.
            This will add both ``stat.mimetype`` and ``stat.charset`` fields
            to the return, if possible.
            In Ansible 2.3 this option changed from ``mime`` to ``get_mime``
            and the default changed to ``true``.
        :param get_attributes:
            Get file attributes using lsattr tool if present.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.subversion_module>`

        :param repo:
            The subversion URL to the repository.
        :param dest:
            Absolute path where the repository should be deployed.
            The destination directory must be specified unless
            ``checkout=no``, ``update=no``, and ``export=no``.
        :param revision:
            Specific revision to checkout.
        :param force:
            If ``true``, modified files will be discarded. If ``false``,
            module will fail if it encounters modified files. Prior to 1.9 the
            default was ``true``.
        :param in_place:
            If the directory exists, then the working copy will be checked-out
            over-the-top using svn checkout --force; if force is specified
            then existing files with different content are reverted.
        :param username:
            ``--username`` parameter passed to svn.
        :param password:
            ``--password`` parameter passed to svn when svn is less than
            version 1.10.0. This is not secure and the password will be leaked
            to argv.
            ``--password-from-stdin`` parameter when svn is greater or equal
            to version 1.10.0.
        :param executable:
            Path to svn executable to use. If not supplied, the normal
            mechanism for resolving binary paths will be used.
        :param checkout:
            If ``false``, do not check out the repository if it does not exist
            locally.
        :param update:
            If ``false``, do not retrieve new revisions from the origin
            repository.
        :param export:
            If ``true``, do export instead of checkout/update.
        :param switch:
            If ``false``, do not call svn switch before update.
        :param validate_certs:
            If ``false``, passes the ``--trust-server-cert`` flag to svn.
            If ``true``, does not pass the flag.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.systemd_module>`

        :param name:
            Name of the unit. This parameter takes the name of exactly one
            unit to work with.
            When no extension is given, it is implied to a ``.service`` as
            systemd.
            When using in a chroot environment you always need to specify the
            name of the unit with the extension. For example,
            ``crond.service``.
        :param state:
            ``started``/``stopped`` are idempotent actions that will not run
            commands unless necessary. ``restarted`` will always bounce the
            unit. ``reloaded`` will always reload and if the service is not
            running at the moment of the reload, it is started.
            If set, requires ``name``.
        :param enabled:
            Whether the unit should start on boot. **At least one of state and
            enabled are required.**.
            If set, requires ``name``.
        :param force:
            Whether to override existing symlinks.
        :param masked:
            Whether the unit should be masked or not. A masked unit is
            impossible to start.
            If set, requires ``name``.
        :param daemon_reload:
            Run daemon-reload before doing any other operations, to make sure
            systemd has read any changes.
            When set to ``true``, runs daemon-reload even if the module does
            not start or stop anything.
        :param daemon_reexec:
            Run daemon_reexec command before doing any other operations, the
            systemd manager will serialize the manager state.
        :param scope:
            Run systemctl within a given service manager scope, either as the
            default system scope ``system``, the current user's scope
            ``user``, or the scope of all users ``global``.
            For systemd to work with 'user', the executing user must have its
            own instance of dbus started and accessible (systemd requirement).
            The user dbus process is normally started during normal login, but
            not during the run of Ansible tasks. Otherwise you will probably
            get a 'Failed to connect to bus: no such file or directory' error.
            The user must have access, normally given via setting the
            ``XDG_RUNTIME_DIR`` variable, see the example below.
        :param no_block:
            Do not synchronously wait for the requested operation to finish.
            Enqueued job will continue without Ansible blocking on its
            completion.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.systemd_service_module>`

        :param name:
            Name of the unit. This parameter takes the name of exactly one
            unit to work with.
            When no extension is given, it is implied to a ``.service`` as
            systemd.
            When using in a chroot environment you always need to specify the
            name of the unit with the extension. For example,
            ``crond.service``.
        :param state:
            ``started``/``stopped`` are idempotent actions that will not run
            commands unless necessary. ``restarted`` will always bounce the
            unit. ``reloaded`` will always reload and if the service is not
            running at the moment of the reload, it is started.
            If set, requires ``name``.
        :param enabled:
            Whether the unit should start on boot. **At least one of state and
            enabled are required.**.
            If set, requires ``name``.
        :param force:
            Whether to override existing symlinks.
        :param masked:
            Whether the unit should be masked or not. A masked unit is
            impossible to start.
            If set, requires ``name``.
        :param daemon_reload:
            Run daemon-reload before doing any other operations, to make sure
            systemd has read any changes.
            When set to ``true``, runs daemon-reload even if the module does
            not start or stop anything.
        :param daemon_reexec:
            Run daemon_reexec command before doing any other operations, the
            systemd manager will serialize the manager state.
        :param scope:
            Run systemctl within a given service manager scope, either as the
            default system scope ``system``, the current user's scope
            ``user``, or the scope of all users ``global``.
            For systemd to work with 'user', the executing user must have its
            own instance of dbus started and accessible (systemd requirement).
            The user dbus process is normally started during normal login, but
            not during the run of Ansible tasks. Otherwise you will probably
            get a 'Failed to connect to bus: no such file or directory' error.
            The user must have access, normally given via setting the
            ``XDG_RUNTIME_DIR`` variable, see the example below.
        :param no_block:
            Do not synchronously wait for the requested operation to finish.
            Enqueued job will continue without Ansible blocking on its
            completion.
        """  # noqa: E501
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
        runlevels: Sequence[str] = _Unknown,
        arguments: str = _Unknown,
        daemonize: bool = False,
    ) -> SysvinitResults:
        """
        Manage SysV services.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.sysvinit_module>`

        :param name:
            Name of the service.
        :param state:
            ``started``/``stopped`` are idempotent actions that will not run
            commands unless necessary. Not all init scripts support
            ``restarted`` nor ``reloaded`` natively, so these will both
            trigger a stop and start as needed.
        :param enabled:
            Whether the service should start on boot. **At least one of state
            and enabled are required.**.
        :param sleep:
            If the service is being ``restarted`` or ``reloaded`` then sleep
            this many seconds between the stop and start command. This helps
            to workaround badly behaving services.
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
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.tempfile_module>`

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
        """  # noqa: E501
        raise AttributeError('tempfile')

    def template(
        self,
        *,
        follow: bool = False,
        backup: bool = False,
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
        src: StrPath,
        dest: StrPath,
        newline_sequence: Literal['\\n', '\\r', '\\r\\n'] = '\\n',
        block_start_string: str = '{%',
        block_end_string: str = '%}',
        variable_start_string: str = '{{',
        variable_end_string: str = '}}',
        comment_start_string: str = _Unknown,
        comment_end_string: str = _Unknown,
        trim_blocks: bool = True,
        lstrip_blocks: bool = False,
        force: bool = True,
        output_encoding: str = 'utf-8',
        validate: str = _Unknown,
    ) -> TemplateResults:
        """
        Template a file out to a target host.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.template_module>`

        :param follow:
            Determine whether symbolic links should be followed.
            When set to ``true`` symbolic links will be followed, if they
            exist.
            When set to ``false`` symbolic links will not be followed.
            Previous to Ansible 2.4, this was hardcoded as ``true``.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        :param src:
            Path of a Jinja2 formatted template on the Ansible controller.
            This can be a relative or an absolute path.
            The file must be encoded with ``utf-8`` but ``output_encoding``
            can be used to control the encoding of the output template.
        :param dest:
            Location to render the template to on the remote machine.
        :param newline_sequence:
            Specify the newline sequence to use for templating files.
        :param block_start_string:
            The string marking the beginning of a block.
        :param block_end_string:
            The string marking the end of a block.
        :param variable_start_string:
            The string marking the beginning of a print statement.
        :param variable_end_string:
            The string marking the end of a print statement.
        :param comment_start_string:
            The string marking the beginning of a comment statement.
        :param comment_end_string:
            The string marking the end of a comment statement.
        :param trim_blocks:
            Determine when newlines should be removed from blocks.
            When set to ``True`` the first newline after a block is removed
            (block, not variable tag!).
        :param lstrip_blocks:
            Determine when leading spaces and tabs should be stripped.
            When set to ``True`` leading spaces and tabs are stripped from the
            start of a line to a block.
        :param force:
            Determine when the file is being transferred if the destination
            already exists.
            When set to ``True``, replace the remote file when contents are
            different than the source.
            When set to ``False``, the file will only be transferred if the
            destination does not exist.
        :param output_encoding:
            Overrides the encoding used to write the template file defined by
            ``dest``.
            It defaults to ``utf-8``, but any encoding supported by python can
            be used.
            The source template file must always be encoded using ``utf-8``,
            for homogeneity.
        :param validate:
            The validation command to run before copying the updated file into
            the final destination.
            A temporary file path is used to validate, passed in through '%s'
            which must be present as in the examples below.
            Also, the command is passed securely so shell features such as
            expansion and pipes will not work.
            For an example on how to handle more complex validation than what
            this option provides, see ``handling complex validation``.
        """  # noqa: E501
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
        exclude: Sequence[str] = _Unknown,
        include: Sequence[str] = _Unknown,
        keep_newer: bool = False,
        extra_opts: Sequence[str] = _Unknown,
        remote_src: bool = False,
        validate_certs: bool = True,
        decrypt: bool = True,
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
    ) -> UnarchiveResults:
        """
        Unpacks an archive after (optionally) copying it from the local
        machine.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.unarchive_module>`

        :param src:
            If ``remote_src=no`` (default), local path to archive file to copy
            to the target server; can be absolute or relative. If
            ``remote_src=yes``, path on the target server to existing archive
            file to unpack.
            If ``remote_src=yes`` and ``src`` contains ``://``, the remote
            machine will download the file from the URL first. (version_added
            2.0). This is only for simple cases, for full download support use
            the :meth:`get_url` method.
        :param dest:
            Remote absolute path where the archive should be unpacked.
            The given path must exist. Base directory is not created by this
            module.
        :param copy:
            If true, the file is copied from local controller to the managed
            (remote) node, otherwise, the plugin will look for src archive on
            the managed machine.
            This option has been deprecated in favor of ``remote_src``.
            This option is mutually exclusive with ``remote_src``.
        :param creates:
            If the specified absolute path (file or directory) already exists,
            this step will **not** be run.
            The specified absolute path (file or directory) must be below the
            base path given with ``dest``.
        :param io_buffer_size:
            Size of the volatile memory buffer that is used for extracting
            files from the archive in bytes.
        :param list_files:
            If set to True, return the list of files that are contained in the
            tarball.
        :param exclude:
            List the directory and file entries that you would like to exclude
            from the unarchive action.
            Mutually exclusive with ``include``.
        :param include:
            List of directory and file entries that you would like to extract
            from the archive. If ``include`` is not empty, only files listed
            here will be extracted.
            Mutually exclusive with ``exclude``.
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
            Set to ``true`` to indicate the archived file is already on the
            remote system and not local to the Ansible controller.
            This option is mutually exclusive with ``copy``.
        :param validate_certs:
            This only applies if using a https URL as the source of the file.
            This should only set to ``false`` used on personally controlled
            sites using self-signed certificate.
            Prior to 2.2 the code worked as if this was set to ``true``.
        :param decrypt:
            This option controls the auto-decryption of source files using
            vault.
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        """  # noqa: E501
        raise AttributeError('unarchive')

    def uri(
        self,
        *,
        ciphers: Sequence[str] = _Unknown,
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
        status_code: Sequence[int] = _Unknown,
        timeout: int = 30,
        headers: Mapping[str, Incomplete] = _Unknown,
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
        unredirected_headers: Sequence[str] = _Unknown,
        use_gssapi: bool = False,
        use_netrc: bool = True,
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
    ) -> UriResults:
        """
        Interacts with webservices.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.uri_module>`

        :param ciphers:
            SSL/TLS Ciphers to use for the request.
            When a list is provided, all ciphers are joined in order with
            ``:``.
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
            A path of where to download the file to (if desired). If ``dest``
            is a directory, the basename of the file on the remote server will
            be used.
        :param url_username:
            A username for the module to use for Digest, Basic or WSSE
            authentication.
        :param url_password:
            A password for the module to use for Digest, Basic or WSSE
            authentication.
        :param body:
            The body of the http request/response to the web service. If
            ``body_format`` is set to ``json`` it will take an already
            formatted JSON string or convert a data structure into JSON.
            If ``body_format`` is set to ``form-urlencoded`` it will convert a
            dictionary or list of tuples into an
            'application/x-www-form-urlencoded' string. (Added in v2.7).
            If ``body_format`` is set to ``form-multipart`` it will convert a
            dictionary into 'multipart/form-multipart' body. (Added in v2.10).
        :param body_format:
            The serialization format of the body. When set to ``json``,
            ``form-multipart``, or ``form-urlencoded``, encodes the body
            argument, if needed, and automatically sets the Content-Type
            header accordingly.
            As of v2.3 it is possible to override the ``Content-Type`` header,
            when set to ``json`` or ``form-urlencoded`` via the ``headers``
            option.
            The 'Content-Type' header cannot be overridden when using
            ``form-multipart``.
            ``form-urlencoded`` was added in v2.7.
            ``form-multipart`` was added in v2.10.
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
            called ``ignore:json`` in the dictionary results.
        :param force_basic_auth:
            Force the sending of the Basic authentication header upon initial
            request.
            When this setting is ``false``, this module will first try an
            unauthenticated request, and when the server replies with an
            ``HTTP 401`` error, it will submit the Basic authentication header.
            When this setting is ``true``, this module will immediately send a
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
            As of Ansible 2.3 supplying ``Content-Type`` here will override
            the header generated by supplying ``json`` or ``form-urlencoded``
            for ``body_format``.
        :param validate_certs:
            If ``false``, SSL certificates will not be validated.
            This should only set to ``false`` used on personally controlled
            sites using self-signed certificates.
            Prior to 1.9.2 the code defaulted to ``false``.
        :param client_cert:
            PEM formatted certificate chain file to be used for SSL client
            authentication.
            This file can also include the key as well, and if the key is
            included, ``client_key`` is not required.
        :param client_key:
            PEM formatted file that contains your private key to be used for
            SSL client authentication.
            If ``client_cert`` contains both the certificate and key, this
            option is not required.
        :param ca_path:
            PEM formatted file that contains a CA certificate to be used for
            validation.
        :param src:
            Path to file to be submitted to the remote server.
            Cannot be used with ``body``.
            Should be used with ``force_basic_auth`` to ensure success when
            the remote end sends a 401.
        :param remote_src:
            If ``false``, the module will search for the ``src`` on the
            controller node.
            If ``true``, the module will search for the ``src`` on the managed
            (remote) node.
        :param force:
            If ``true`` do not get a cached copy.
        :param use_proxy:
            If ``false``, it will not use a proxy, even if one is defined in
            an environment variable on the target hosts.
        :param unix_socket:
            Path to Unix domain socket to use for connection.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
        :param unredirected_headers:
            A list of header names that will not be sent on subsequent
            redirected requests. This list is case insensitive. By default all
            headers will be redirected. In some cases it may be beneficial to
            list headers such as ``Authorization`` here to avoid potential
            credential exposure.
        :param use_gssapi:
            Use GSSAPI to perform the authentication, typically this is for
            Kerberos or Kerberos through Negotiate authentication.
            Requires the Python library `gssapi
            <https://github.com/pythongssapi/python-gssapi>`__ to be installed.
            Credentials for GSSAPI can be specified with
            ``url_username``/``url_password`` or with the GSSAPI env var
            ``KRB5CCNAME`` that specified a custom Kerberos credential cache.
            NTLM authentication is **not** supported even if the GSSAPI mech
            for NTLM has been installed.
        :param use_netrc:
            Determining whether to use credentials from ``~/.netrc`` file.
            By default .netrc is used with Basic authentication headers.
            When set to False, .netrc credentials are ignored.
            Requires ansible-core >= 2.14
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
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
        groups: Sequence[str] = _Unknown,
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
        expires: float = _Unknown,
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.user_module>`

        .. warning::
            The documentation is referring to the module from
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.user_module>`,
            there are however other collections with the same module name, so
            depending on your environment you may be getting one of those
            instead.

            Conflicting collections:

            * :ref:`awx.awx <ansible_collections.awx.awx.user_module>`
            * :ref:`cisco.dnac <ansible_collections.cisco.dnac.user_module>`
            * :ref:`ieisystem.inmanage <ansible_collections.ieisystem.inmanage.user_module>`
            * :ref:`inspur.ispim <ansible_collections.inspur.ispim.user_module>`
            * :ref:`inspur.sm <ansible_collections.inspur.sm.user_module>`
            * :ref:`kaytus.ksmanage <ansible_collections.kaytus.ksmanage.user_module>`
            * :ref:`lowlydba.sqlserver <ansible_collections.lowlydba.sqlserver.user_module>`
            * :ref:`microsoft.ad <ansible_collections.microsoft.ad.user_module>`
            * :ref:`sensu.sensu_go <ansible_collections.sensu.sensu_go.user_module>`
            * :ref:`theforeman.foreman <ansible_collections.theforeman.foreman.user_module>`
            * :ref:`vultr.cloud <ansible_collections.vultr.cloud.user_module>`

        :param name:
            Name of the user to create, remove or modify.
        :param uid:
            Optionally sets the *UID* of the user.
        :param comment:
            Optionally sets the description (aka *GECOS*) of user account.
            On macOS, this defaults to the ``name`` option.
        :param hidden:
            macOS only, optionally hide the user from the login window and
            system preferences.
            The default will be ``true`` if the ``system`` option is used.
        :param non_unique:
            Optionally when used with the -u option, this option allows to
            change the user ID to a non-unique value.
        :param seuser:
            Optionally sets the seuser type (user_u) on selinux enabled
            systems.
        :param group:
            Optionally sets the user's primary group (takes a group name).
            On macOS, this defaults to ``'staff'``.
        :param groups:
            A list of supplementary groups which the user is also a member of.
            By default, the user is removed from all other groups. Configure
            ``append`` to modify this.
            When set to an empty string ``''``, the user is removed from all
            groups except the primary group.
            Before Ansible 2.3, the only input format allowed was a comma
            separated string.
        :param append:
            If ``true``, add the user to the groups specified in ``groups``.
            If ``false``, user will only be added to the groups specified in
            ``groups``, removing them from all other groups.
        :param shell:
            Optionally set the user's shell.
            On macOS, before Ansible 2.5, the default shell for non-system
            users was ``/usr/bin/false``. Since Ansible 2.5, the default shell
            for non-system users on macOS is ``/bin/bash``.
            On other operating systems, the default shell is determined by the
            underlying tool invoked by this module. See Notes for a per
            platform list of invoked tools.
        :param home:
            Optionally set the user's home directory.
        :param skeleton:
            Optionally set a home skeleton directory.
            Requires ``create_home`` option!.
        :param password:
            If provided, set the user's password to the provided encrypted
            hash (Linux) or plain text password (macOS).
            **Linux/Unix/POSIX:** Enter the hashed password as the value.
            See `FAQ entry
            <https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module>`__
            for details on various ways to generate the hash of a password.
            To create an account with a locked/disabled password on Linux
            systems, set this to ``'!'`` or ``'*'``.
            To create an account with a locked/disabled password on OpenBSD,
            set this to ``'*************'``.
            **OS X/macOS:** Enter the cleartext password as the value. Be sure
            to take relevant security precautions.
            On macOS, the password specified in the ``password`` option will
            always be set, regardless of whether the user account already
            exists or not.
            When the password is passed as an argument, the ``user`` module
            will always return changed to ``true`` for macOS systems. Since
            macOS no longer provides access to the hashed passwords directly.
        :param state:
            Whether the account should exist or not, taking action if the
            state is different from what is stated.
            See this `FAQ entry
            <https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#running-on-macos-as-a-target>`__
            for additional requirements when removing users on macOS systems.
        :param create_home:
            Unless set to ``false``, a home directory will be made for the
            user when the account is created or if the home directory does not
            exist.
            Changed from ``createhome`` to ``create_home`` in Ansible 2.5.
        :param move_home:
            If set to ``true`` when used with ``home``, attempt to move the
            user's old home directory to the specified directory if it isn't
            there already and the old home exists.
        :param system:
            When creating an account ``state=present``, setting this to
            ``true`` makes the user a system account.
            This setting cannot be changed on existing users.
        :param force:
            This only affects ``state=absent``, it forces removal of the user
            and associated directories on supported platforms.
            The behavior is the same as ``userdel --force``, check the man
            page for ``userdel`` on your system for details and support.
            When used with ``generate_ssh_key=yes`` this forces an existing
            key to be overwritten.
        :param remove:
            This only affects ``state=absent``, it attempts to remove
            directories associated with the user.
            The behavior is the same as ``userdel --remove``, check the man
            page for details and support.
        :param login_class:
            Optionally sets the user's login class, a feature of most BSD OSs.
        :param generate_ssh_key:
            Whether to generate a SSH key for the user in question.
            This will **not** overwrite an existing SSH key unless used with
            ``force=yes``.
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
            This parameter defaults to ``.ssh/id_rsa``.
        :param ssh_key_comment:
            Optionally define the comment for the SSH key.
        :param ssh_key_passphrase:
            Set a passphrase for the SSH key.
            If no passphrase is provided, the SSH key will default to having
            no passphrase.
        :param update_password:
            ``always`` will update passwords if they differ.
            ``on_create`` will only set the password for newly created users.
        :param expires:
            An expiry time for the user in epoch, it will be ignored on
            platforms that do not support this.
            Currently supported on GNU/Linux, FreeBSD, and DragonFlyBSD.
            Since Ansible 2.6 you can remove the expiry time by specifying a
            negative value. Currently supported on GNU/Linux and FreeBSD.
        :param password_lock:
            Lock the password (``usermod -L``, ``usermod -U``, ``pw lock``).
            Implementation differs by platform. This option does not always
            mean the user cannot login using other methods.
            This option does not disable the user, only lock the password.
            This must be set to ``False`` in order to unlock a currently
            locked password. The absence of this parameter will not unlock a
            password.
            Currently supported on Linux, FreeBSD, DragonFlyBSD, NetBSD,
            OpenBSD.
        :param local:
            Forces the use of "local" command alternatives on platforms that
            implement it.
            This is useful in environments that use centralized authentication
            when you want to manipulate the local users (in other words, it
            uses ``luseradd`` instead of ``useradd``).
            This will check ``/etc/passwd`` for an existing account before
            invoking commands. If the local account database exists somewhere
            other than ``/etc/passwd``, this setting will not work properly.
            This requires that the above commands as well as ``/etc/passwd``
            must exist on the target host, otherwise it will be a fatal error.
        :param profile:
            Sets the profile of the user.
            Can set multiple profiles using comma separation.
            To delete all the profiles, use ``profile=''``.
            Currently supported on Illumos/Solaris. Does nothing when used
            with other platforms.
        :param authorization:
            Sets the authorization of the user.
            Can set multiple authorizations using comma separation.
            To delete all authorizations, use ``authorization=''``.
            Currently supported on Illumos/Solaris. Does nothing when used
            with other platforms.
        :param role:
            Sets the role of the user.
            Can set multiple roles using comma separation.
            To delete all roles, use ``role=''``.
            Currently supported on Illumos/Solaris. Does nothing when used
            with other platforms.
        :param password_expire_max:
            Maximum number of days between password change.
            Supported on Linux only.
        :param password_expire_min:
            Minimum number of days between password change.
            Supported on Linux only.
        :param password_expire_warn:
            Number of days of warning before password expires.
            Supported on Linux only.
            Requires ansible-core >= 2.16
        :param umask:
            Sets the umask of the user.
            Currently supported on Linux. Does nothing when used with other
            platforms.
            Requires ``local`` is omitted or ``False``.
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.validate_argument_spec_module>`

        :param argument_spec:
            A dictionary like AnsibleModule argument_spec. See
            ``argument spec definition``.
        :param provided_arguments:
            A dictionary of the arguments that will be validated according to
            argument_spec.
        """  # noqa: E501
        raise AttributeError('validate_argument_spec')

    def wait_for(
        self,
        *,
        host: str = '127.0.0.1',
        timeout: int = 300,
        connect_timeout: int = 5,
        delay: int = 0,
        port: int = _Unknown,
        active_connection_states: Sequence[str] = _Unknown,
        state: Literal[
            'absent',
            'drained',
            'present',
            'started',
            'stopped',
        ] = 'started',
        path: StrPath = _Unknown,
        search_regex: str = _Unknown,
        exclude_hosts: Sequence[str] = _Unknown,
        sleep: int = 1,
        msg: str = _Unknown,
    ) -> WaitForResults:
        """
        Waits for a condition before continuing.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.wait_for_module>`

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
            ``path`` and ``port`` are mutually exclusive parameters.
        :param active_connection_states:
            The list of TCP connection states which are counted as active
            connections.
        :param state:
            Either ``present``, ``started``, or ``stopped``, ``absent``, or
            ``drained``.
            When checking a port ``started`` will ensure the port is open,
            ``stopped`` will check that it is closed, ``drained`` will check
            for active connections.
            When checking for a file or a search string ``present`` or
            ``started`` will ensure that the file or string is present before
            continuing, ``absent`` will check that file is absent or removed.
        :param path:
            Path to a file on the filesystem that must exist before continuing.
            ``path`` and ``port`` are mutually exclusive parameters.
        :param search_regex:
            Can be used to match a string in either a file or a socket
            connection.
            Defaults to a multiline regex.
        :param exclude_hosts:
            List of hosts or IPs to ignore when looking for active TCP
            connections for ``drained`` state.
        :param sleep:
            Number of seconds to sleep between checks.
            Before Ansible 2.3 this was hardcoded to 1 second.
        :param msg:
            This overrides the normal error message from a failure to meet the
            required conditions.
        """  # noqa: E501
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

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.wait_for_connection_module>`

        :param connect_timeout:
            Maximum number of seconds to wait for a connection to happen
            before closing and retrying.
        :param delay:
            Number of seconds to wait before starting to poll.
        :param sleep:
            Number of seconds to sleep between checks.
        :param timeout:
            Maximum number of seconds to wait for.
        """  # noqa: E501
        raise AttributeError('wait_for_connection')

    def yum(
        self,
        *,
        use_backend: Literal['auto', 'yum', 'yum4', 'dnf'] = 'auto',
        name: Sequence[str] = _Unknown,
        exclude: str = _Unknown,
        list: str = _Unknown,
        state: Literal[
            'absent',
            'installed',
            'latest',
            'present',
            'removed',
        ] = _Unknown,
        enablerepo: str = _Unknown,
        disablerepo: str = _Unknown,
        conf_file: str = _Unknown,
        disable_gpg_check: bool = False,
        skip_broken: bool = False,
        update_cache: bool = False,
        validate_certs: bool = True,
        update_only: bool = False,
        installroot: str = '/',
        security: bool = False,
        bugfix: str = 'no',
        allow_downgrade: bool = False,
        enable_plugin: str = _Unknown,
        disable_plugin: str = _Unknown,
        releasever: str = _Unknown,
        autoremove: bool = False,
        disable_excludes: str = _Unknown,
        download_only: bool = False,
        lock_timeout: int = 30,
        install_weak_deps: bool = True,
        download_dir: str = _Unknown,
        install_repoquery: bool = True,
    ) -> YumResults:
        """
        Manages packages with the *yum* package manager.

        :param use_backend:
            This module supports ``yum`` (as it always has), this is known as
            ``yum3``/``YUM3``/``yum-deprecated`` by upstream yum developers.
            As of Ansible 2.7+, this module also supports ``YUM4``, which is
            the "new yum" and it has an ``dnf`` backend.
            By default, this module will select the backend based on the
            ``ansible_pkg_mgr`` fact.
        :param name:
            A package name or package specifier with version, like
            ``name-1.0``.
            If a previous version is specified, the task also needs to turn
            ``allow_downgrade`` on. See the ``allow_downgrade`` documentation
            for caveats with downgrading packages.
            When using state=latest, this can be ``'*'`` which means run
            ``yum -y update``.
            You can also pass a url or a local path to a rpm file (using
            state=present). To operate on several packages this can accept a
            comma separated string of packages or (as of 2.0) a list of
            packages.
        :param exclude:
            Package name(s) to exclude when state=present, or latest.
        :param list:
            Package name to run the equivalent of yum list --show-duplicates
            <package> against. In addition to listing packages, use can also
            list the following: ``installed``, ``updates``, ``available`` and
            ``repos``.
            This parameter is mutually exclusive with ``name``.
        :param state:
            Whether to install (``present`` or ``installed``, ``latest``), or
            remove (``absent`` or ``removed``) a package.
            ``present`` and ``installed`` will simply ensure that a desired
            package is installed.
            ``latest`` will update the specified package if it's not of the
            latest available version.
            ``absent`` and ``removed`` will remove the specified package.
            Default is ``None``, however in effect the default action is
            ``present`` unless the ``autoremove`` option is enabled for this
            module, then ``absent`` is inferred.
        :param enablerepo:
            *Repoid* of repositories to enable for the install/update
            operation. These repos will not persist beyond the transaction.
            When specifying multiple repos, separate them with a ``","``.
            As of Ansible 2.7, this can alternatively be a list instead of
            ``","`` separated string.
        :param disablerepo:
            *Repoid* of repositories to disable for the install/update
            operation. These repos will not persist beyond the transaction.
            When specifying multiple repos, separate them with a ``","``.
            As of Ansible 2.7, this can alternatively be a list instead of
            ``","`` separated string.
        :param conf_file:
            The remote yum configuration file to use for the transaction.
        :param disable_gpg_check:
            Whether to disable the GPG checking of signatures of packages
            being installed. Has an effect only if state is *present* or
            *latest*.
        :param skip_broken:
            Skip packages with broken dependencies(devsolve) and are causing
            problems.
        :param update_cache:
            Force yum to check if cache is out of date and redownload if
            needed. Has an effect only if state is *present* or *latest*.
        :param validate_certs:
            This only applies if using a https url as the source of the rpm.
            e.g. for localinstall. If set to ``False``, the SSL certificates
            will not be validated.
            This should only set to ``False`` used on personally controlled
            sites using self-signed certificates as it avoids verifying the
            source site.
            Prior to 2.1 the code worked as if this was set to ``True``.
        :param update_only:
            When using latest, only update installed packages. Do not install
            packages.
            Has an effect only if state is *latest*.
        :param installroot:
            Specifies an alternative installroot, relative to which all
            packages will be installed.
        :param security:
            If set to ``True``, and ``state=latest`` then only installs
            updates that have been marked security related.
        :param bugfix:
            If set to ``True``, and ``state=latest`` then only installs
            updates that have been marked bugfix related.
        :param allow_downgrade:
            Specify if the named package and version is allowed to downgrade a
            maybe already installed higher version of that package. Note that
            setting allow_downgrade=True can make this module behave in a
            non-idempotent way. The task could end up with a set of packages
            that does not match the complete list of specified packages to
            install (because dependencies between the downgraded package and
            others can cause changes to the packages which were in the earlier
            transaction).
        :param enable_plugin:
            *Plugin* name to enable for the install/update operation. The
            enabled plugin will not persist beyond the transaction.
        :param disable_plugin:
            *Plugin* name to disable for the install/update operation. The
            disabled plugins will not persist beyond the transaction.
        :param releasever:
            Specifies an alternative release from which all packages will be
            installed.
        :param autoremove:
            If ``True``, removes all "leaf" packages from the system that were
            originally installed as dependencies of user-installed packages
            but which are no longer required by any such package. Should be
            used alone or when state is *absent*.
            NOTE: This feature requires yum >= 3.4.3 (RHEL/CentOS 7+).
        :param disable_excludes:
            Disable the excludes defined in YUM config files.
            If set to ``all``, disables all excludes.
            If set to ``main``, disable excludes defined in [main] in yum.conf.
            If set to ``repoid``, disable excludes defined for given repo id.
        :param download_only:
            Only download the packages, do not install them.
        :param lock_timeout:
            Amount of time to wait for the yum lockfile to be freed.
        :param install_weak_deps:
            Will also install all packages linked by a weak dependency
            relation.
            NOTE: This feature requires yum >= 4 (RHEL/CentOS 8+).
        :param download_dir:
            Specifies an alternate directory to store packages.
            Has an effect only if *download_only* is specified.
        :param install_repoquery:
            If repoquery is not available, install yum-utils. If the system is
            registered to RHN or an RHN Satellite, repoquery allows for
            querying all channels assigned to the system. It is also required
            to use the 'list' parameter.
            NOTE: This will run and be logged as a separate yum transation
            which takes place before any other installation or removal.
            NOTE: This will use the system's default enabled repositories
            without regard for disablerepo/enablerepo given to the module.
        """
        raise AttributeError('yum')

    def yum_repository(
        self,
        *,
        async_: bool = _Unknown,
        bandwidth: str = _Unknown,
        baseurl: Sequence[str] = _Unknown,
        cost: str = _Unknown,
        deltarpm_metadata_percentage: str = _Unknown,
        deltarpm_percentage: str = _Unknown,
        description: str = _Unknown,
        enabled: bool = _Unknown,
        enablegroups: bool = _Unknown,
        exclude: Sequence[str] = _Unknown,
        failovermethod: Literal['roundrobin', 'priority'] = _Unknown,
        file: str = _Unknown,
        gpgcakey: str = _Unknown,
        gpgcheck: bool = _Unknown,
        gpgkey: Sequence[str] = _Unknown,
        module_hotfixes: bool = _Unknown,
        http_caching: Literal['all', 'packages', 'none'] = _Unknown,
        include: str = _Unknown,
        includepkgs: Sequence[str] = _Unknown,
        ip_resolve: Literal[
            '4',
            '6',
            'IPv4',
            'IPv6',
            'whatever',
        ] = _Unknown,
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
        mode: str = _Unknown,
        owner: str = _Unknown,
        group: str = _Unknown,
        seuser: str = _Unknown,
        serole: str = _Unknown,
        setype: str = _Unknown,
        selevel: str = _Unknown,
        unsafe_writes: bool = False,
        attributes: str = _Unknown,
    ) -> YumRepositoryResults:
        """
        Add or remove YUM repositories.

        .. seealso::
            :ref:`ansible.builtin <ansible_collections.ansible.builtin.yum_repository_module>`

        :param async:
            If set to ``true`` Yum will download packages and metadata from
            this repo in parallel, if possible.
            In ansible-core 2.11, 2.12, and 2.13 the default value is ``true``.
            This option has been deprecated in RHEL 8. If you're using one of
            the versions listed above, you can set this option to None to
            avoid passing an unknown configuration option.
        :param bandwidth:
            Maximum available network bandwidth in bytes/second. Used with the
            ``throttle`` option.
            If ``throttle`` is a percentage and bandwidth is ``0`` then
            bandwidth throttling will be disabled. If ``throttle`` is
            expressed as a data rate (bytes/sec) then this option is ignored.
            Default is ``0`` (no bandwidth throttling).
        :param baseurl:
            URL to the directory where the yum repository's 'repodata'
            directory lives.
            It can also be a list of multiple URLs.
            This, the ``metalink`` or ``mirrorlist`` parameters are required
            if ``state`` is set to ``present``.
        :param cost:
            Relative cost of accessing this repository. Useful for weighing
            one repo's packages as greater/less than any other.
        :param deltarpm_metadata_percentage:
            When the relative size of deltarpm metadata vs pkgs is larger than
            this, deltarpm metadata is not downloaded from the repo. Note that
            you can give values over ``100``, so ``200`` means that the
            metadata is required to be half the size of the packages. Use
            ``0`` to turn off this check, and always download metadata.
        :param deltarpm_percentage:
            When the relative size of delta vs pkg is larger than this, delta
            is not used. Use ``0`` to turn off delta rpm processing. Local
            repositories (with file://``baseurl``) have delta rpms turned off
            by default.
        :param description:
            A human-readable string describing the repository. This option
            corresponds to the "name" property in the repo file.
            This parameter is only required if ``state`` is set to ``present``.
        :param enabled:
            This tells yum whether or not use this repository.
            Yum default value is ``true``.
        :param enablegroups:
            Determines whether yum will allow the use of package groups for
            this repository.
            Yum default value is ``true``.
        :param exclude:
            List of packages to exclude from updates or installs. This should
            be a space separated list. Shell globs using wildcards (for
            example ``*`` and ``?``) are allowed.
            The list can also be a regular YAML array.
        :param failovermethod:
            ``roundrobin`` randomly selects a URL out of the list of URLs to
            start with and proceeds through each of them as it encounters a
            failure contacting the host.
            ``priority`` starts from the first ``baseurl`` listed and reads
            through them sequentially.
        :param file:
            File name without the ``.repo`` extension to save the repo in.
            Defaults to the value of ``name``.
        :param gpgcakey:
            A URL pointing to the ASCII-armored CA key file for the repository.
        :param gpgcheck:
            Tells yum whether or not it should perform a GPG signature check
            on packages.
            No default setting. If the value is not set, the system setting
            from ``/etc/yum.conf`` or system default of ``false`` will be used.
        :param gpgkey:
            A URL pointing to the ASCII-armored GPG key file for the
            repository.
            It can also be a list of multiple URLs.
        :param module_hotfixes:
            Disable module RPM filtering and make all RPMs from the repository
            available. The default is ``None``.
        :param http_caching:
            Determines how upstream HTTP caches are instructed to handle any
            HTTP downloads that Yum does.
            ``all`` means that all HTTP downloads should be cached.
            ``packages`` means that only RPM package downloads should be
            cached (but not repository metadata downloads).
            ``none`` means that no HTTP downloads should be cached.
        :param include:
            Include external configuration file. Both, local path and URL is
            supported. Configuration file will be inserted at the position of
            the ``include=`` line. Included files may contain further include
            lines. Yum will abort with an error if an inclusion loop is
            detected.
        :param includepkgs:
            List of packages you want to only use from a repository. This
            should be a space separated list. Shell globs using wildcards (for
            example ``*`` and ``?``) are allowed. Substitution variables (for
            example ``$releasever``) are honored here.
            The list can also be a regular YAML array.
        :param ip_resolve:
            Determines how yum resolves host names.
            ``4`` or ``IPv4`` - resolve to IPv4 addresses only.
            ``6`` or ``IPv6`` - resolve to IPv6 addresses only.
        :param keepalive:
            This tells yum whether or not HTTP/1.1 keepalive should be used
            with this repository. This can improve transfer speeds by using
            one connection when downloading multiple files from a repository.
        :param keepcache:
            Either ``1`` or ``0``. Determines whether or not yum keeps the
            cache of headers and packages after successful installation.
            This parameter is deprecated and will be removed in version 2.20.
        :param metadata_expire:
            Time (in seconds) after which the metadata will expire.
            Default value is 6 hours.
        :param metadata_expire_filter:
            Filter the ``metadata_expire`` time, allowing a trade of speed for
            accuracy if a command doesn't require it. Each yum command can
            specify that it requires a certain level of timeliness quality
            from the remote repos. from "I'm about to install/upgrade, so this
            better be current" to "Anything that's available is good enough".
            ``never`` - Nothing is filtered, always obey ``metadata_expire``.
            ``read-only:past`` - Commands that only care about past
            information are filtered from metadata expiring. Eg.
            ``yum history`` info (if history needs to lookup anything about a
            previous transaction, then by definition the remote package was
            available in the past).
            ``read-only:present`` - Commands that are balanced between past
            and future. Eg. ``yum list yum``.
            ``read-only:future`` - Commands that are likely to result in
            running other commands which will require the latest metadata. Eg.
            ``yum check-update``.
            Note that this option does not override "yum clean expire-cache".
        :param metalink:
            Specifies a URL to a metalink file for the repomd.xml, a list of
            mirrors for the entire repository are generated by converting the
            mirrors for the repomd.xml file to a ``baseurl``.
            This, the ``baseurl`` or ``mirrorlist`` parameters are required if
            ``state`` is set to ``present``.
        :param mirrorlist:
            Specifies a URL to a file containing a list of baseurls.
            This, the ``baseurl`` or ``metalink`` parameters are required if
            ``state`` is set to ``present``.
        :param mirrorlist_expire:
            Time (in seconds) after which the mirrorlist locally cached will
            expire.
            Default value is 6 hours.
        :param name:
            Unique repository ID. This option builds the section name of the
            repository in the repo file.
            This parameter is only required if ``state`` is set to ``present``
            or ``absent``.
        :param password:
            Password to use with the username for basic authentication.
        :param priority:
            Enforce ordered protection of repositories. The value is an
            integer from 1 to 99.
            This option only works if the YUM Priorities plugin is installed.
        :param protect:
            Protect packages from updates from other repositories.
        :param proxy:
            URL to the proxy server that yum should use. Set to ``_none_`` to
            disable the global proxy setting.
        :param proxy_password:
            Password for this proxy.
        :param proxy_username:
            Username to use for proxy.
        :param repo_gpgcheck:
            This tells yum whether or not it should perform a GPG signature
            check on the repodata from this repository.
        :param reposdir:
            Directory where the ``.repo`` files will be stored.
        :param retries:
            Set the number of times any attempt to retrieve a file should
            retry before returning an error. Setting this to ``0`` makes yum
            try forever.
        :param s3_enabled:
            Enables support for S3 repositories.
            This option only works if the YUM S3 plugin is installed.
        :param skip_if_unavailable:
            If set to ``true`` yum will continue running if this repository
            cannot be contacted for any reason. This should be set carefully
            as all repos are consulted for any given command.
        :param ssl_check_cert_permissions:
            Whether yum should check the permissions on the paths for the
            certificates on the repository (both remote and local).
            If we can't read any of the files then yum will force
            ``skip_if_unavailable`` to be ``true``. This is most useful for
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
            the string if they are used in the ``baseurl``/etc. Variables are
            appended in the order listed (and found).
        :param username:
            Username to use for basic authentication to a repo or really any
            url.
        :param mode:
            The permissions the resulting filesystem object should have.
            For those used to */usr/bin/chmod* remember that modes are
            actually octal numbers. You must give Ansible enough information
            to parse them correctly. For consistent results, quote octal
            numbers (for example, ``'644'`` or ``'1777'``) so Ansible receives
            a string and can do its own conversion from string into number.
            Adding a leading zero (for example, ``0755``) works sometimes, but
            can fail in loops and some other circumstances.
            Giving Ansible a number without following either of these rules
            will end up with a decimal number which will have unexpected
            results.
            As of Ansible 1.8, the mode may be specified as a symbolic mode
            (for example, ``u+rwx`` or ``u=rw,g=r,o=r``).
            If ``mode`` is not specified and the destination filesystem object
            **does not** exist, the default ``umask`` on the system will be
            used when setting the mode for the newly created filesystem object.
            If ``mode`` is not specified and the destination filesystem object
            **does** exist, the mode of the existing filesystem object will be
            used.
            Specifying ``mode`` is the best way to ensure filesystem objects
            are created with the correct permissions. See CVE-2020-1736 for
            further details.
        :param owner:
            Name of the user that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current user unless you are
            root, in which case it can preserve the previous ownership.
            Specifying a numeric username will be assumed to be a user ID and
            not a username. Avoid numeric usernames to avoid this confusion.
        :param group:
            Name of the group that should own the filesystem object, as would
            be fed to *chown*.
            When left unspecified, it uses the current group of the current
            user unless you are root, in which case it can preserve the
            previous ownership.
        :param seuser:
            The user part of the SELinux filesystem object context.
            By default it uses the ``system`` policy, where applicable.
            When set to ``_default``, it will use the ``user`` portion of the
            policy if available.
        :param serole:
            The role part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``role`` portion of the
            policy if available.
        :param setype:
            The type part of the SELinux filesystem object context.
            When set to ``_default``, it will use the ``type`` portion of the
            policy if available.
        :param selevel:
            The level part of the SELinux filesystem object context.
            This is the MLS/MCS attribute, sometimes known as the ``range``.
            When set to ``_default``, it will use the ``level`` portion of the
            policy if available.
        :param unsafe_writes:
            Influence when to use atomic operation to prevent data corruption
            or inconsistent reads from the target filesystem object.
            By default this module uses atomic operations to prevent data
            corruption or inconsistent reads from the target filesystem
            objects, but sometimes systems are configured or just broken in
            ways that prevent this. One example is docker mounted filesystem
            objects, which cannot be updated atomically from inside the
            container and can only be written in an unsafe manner.
            This option allows Ansible to fall back to unsafe methods of
            updating filesystem objects when atomic operations fail (however,
            it doesn't force Ansible to perform unsafe writes).
            IMPORTANT! Unsafe writes are subject to race conditions and can
            lead to data corruption.
        :param attributes:
            The attributes the resulting filesystem object should have.
            To get supported flags look at the man page for *chattr* on the
            target system.
            This string should contain the attributes in the same order as the
            one displayed by *lsattr*.
            The ``=`` operator is assumed as default, otherwise ``+`` or ``-``
            operators need to be included in the string.
        """  # noqa: E501
        raise AttributeError('yum_repository')

    #
    # ansible.builtin end
    # ansible.netcommon start
    #

    def cli_backup(
        self,
        *,
        defaults: bool = False,
        filename: str = _Unknown,
        dir_path: StrPath = _Unknown,
    ) -> CliBackupResults:
        """
        Back up device configuration from network devices over network_cli.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.cli_backup_module>`

        :param defaults:
            The *defaults* argument will influence how the running-config is
            collected from the device. When the value is set to true, the
            command used to collect the running-config is append with the all
            keyword. When the value is set to false, the command is issued
            without the all keyword.
        :param filename:
            The filename to be used to store the backup configuration. If the
            filename is not given it will be generated based on the hostname,
            current time and date in format defined by
            <hostname>_config.<current-date>@<current-time>.
        :param dir_path:
            This option provides the path ending with directory name in which
            the backup configuration file will be stored. If the directory
            does not exist it will be first created and the filename is either
            the value of ``filename`` or default filename as described in
            ``filename`` options description. If the path value is not given
            in that case a *backup* directory will be created in the current
            working directory and backup configuration will be copied in
            ``filename`` within *backup* directory.
        """  # noqa: E501
        raise AttributeError('cli_backup')

    def cli_command(
        self,
        *,
        command: str,
        prompt: Sequence[str] = _Unknown,
        answer: Sequence[str] = _Unknown,
        sendonly: bool = False,
        newline: bool = True,
        check_all: bool = False,
    ) -> CliCommandResults:
        """
        Run a cli command on cli-based network devices.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.cli_command_module>`

        :param command:
            The command to send to the remote network device. The resulting
            output from the command is returned, unless *sendonly* is set.
        :param prompt:
            A single regex pattern or a sequence of patterns to evaluate the
            expected prompt from *command*.
        :param answer:
            The answer to reply with if *prompt* is matched. The value can be
            a single answer or a list of answer for multiple prompts. In case
            the command execution results in multiple prompts the sequence of
            the prompt and excepted answer should be in same order.
        :param sendonly:
            The boolean value, that when set to true will send *command* to
            the device but not wait for a result.
        :param newline:
            The boolean value, that when set to false will send *answer* to
            the device without a trailing newline.
        :param check_all:
            By default if any one of the prompts mentioned in ``prompt``
            option is matched it won't check for other prompts. This boolean
            flag, that when set to *True* will check for all the prompts
            mentioned in ``prompt`` option in the given order. If the option
            is set to *True* all the prompts should be received from remote
            host if not it will result in timeout.
        """  # noqa: E501
        raise AttributeError('cli_command')

    def cli_config(
        self,
        *,
        config: str = _Unknown,
        commit: bool = _Unknown,
        replace: str = _Unknown,
        backup: bool = False,
        rollback: int = _Unknown,
        commit_comment: str = _Unknown,
        defaults: bool = False,
        multiline_delimiter: str = _Unknown,
        diff_replace: Literal['line', 'block', 'config'] = _Unknown,
        diff_match: Literal['line', 'strict', 'exact', 'none'] = _Unknown,
        diff_ignore_lines: Sequence[str] = _Unknown,
        backup_options: Mapping[str, Incomplete] = _Unknown,
    ) -> CliConfigResults:
        """
        Push text based configuration to network devices over network_cli.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.cli_config_module>`

        :param config:
            The config to be pushed to the network device. This argument is
            mutually exclusive with ``rollback`` and either one of the option
            should be given as input. To ensure idempotency and correct diff
            the configuration lines should be similar to how they appear if
            present in the running configuration on device including the
            indentation.
        :param commit:
            The ``commit`` argument instructs the module to push the
            configuration to the device. This is mapped to module check mode.
        :param replace:
            If the ``replace`` argument is set to ``True``, it will replace
            the entire running-config of the device with the ``config``
            argument value. For devices that support replacing running
            configuration from file on device like NXOS/JUNOS, the ``replace``
            argument takes path to the file on the device that will be used
            for replacing the entire running-config. The value of ``config``
            option should be *None* for such devices. Nexus 9K devices only
            support replace. Use *net_put* or *nxos_file_copy* in case of NXOS
            module to copy the flat file to remote device and then use set the
            fullpath to this argument.
        :param backup:
            This argument will cause the module to create a full backup of the
            current running config from the remote device before any changes
            are made. If the ``backup_options`` value is not given, the backup
            file is written to the ``backup`` folder in the playbook root
            directory or role root directory, if playbook is part of an
            ansible role. If the directory does not exist, it is created.
        :param rollback:
            The ``rollback`` argument instructs the module to rollback the
            current configuration to the identifier specified in the argument.
            If the specified rollback identifier does not exist on the remote
            device, the module will fail. To rollback to the most recent
            commit, set the ``rollback`` argument to 0. This option is
            mutually exclusive with ``config``.
        :param commit_comment:
            The ``commit_comment`` argument specifies a text string to be used
            when committing the configuration. If the ``commit`` argument is
            set to False, this argument is silently ignored. This argument is
            only valid for the platforms that support commit operation with
            comment.
        :param defaults:
            The *defaults* argument will influence how the running-config is
            collected from the device. When the value is set to true, the
            command used to collect the running-config is append with the all
            keyword. When the value is set to false, the command is issued
            without the all keyword.
        :param multiline_delimiter:
            This argument is used when pushing a multiline configuration
            element to the device. It specifies the character to use as the
            delimiting character. This only applies to the configuration
            action.
        :param diff_replace:
            Instructs the module on the way to perform the configuration on
            the device. If the ``diff_replace`` argument is set to *line* then
            the modified lines are pushed to the device in configuration mode.
            If the argument is set to *block* then the entire command block is
            pushed to the device in configuration mode if any line is not
            correct. Note that this parameter will be ignored if the platform
            has onbox diff support.
        :param diff_match:
            Instructs the module on the way to perform the matching of the set
            of commands against the current device config. If ``diff_match``
            is set to *line*, commands are matched line by line. If
            ``diff_match`` is set to *strict*, command lines are matched with
            respect to position. If ``diff_match`` is set to *exact*, command
            lines must be an equal match. Finally, if ``diff_match`` is set to
            *none*, the module will not attempt to compare the source
            configuration with the running configuration on the remote device.
            Note that this parameter will be ignored if the platform has onbox
            diff support.
        :param diff_ignore_lines:
            Use this argument to specify one or more lines that should be
            ignored during the diff. This is used for lines in the
            configuration that are automatically updated by the system. This
            argument takes a list of regular expressions or exact line
            matches. Note that this parameter will be ignored if the platform
            has onbox diff support.
        :param backup_options:
            This is a dict object containing configurable options related to
            backup file path. The value of this option is read only when
            ``backup`` is set to *True*, if ``backup`` is set to *False* this
            option will be silently ignored.
        """  # noqa: E501
        raise AttributeError('cli_config')

    def cli_restore(
        self,
        *,
        filename: str = _Unknown,
        path: str = _Unknown,
    ) -> CliRestoreResults:
        """
        Restore device configuration to network devices over network_cli.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.cli_restore_module>`

        .. note:: Requires ansible >= 6.1.0

        :param filename:
            Filename of the backup file, present in the appliance where the
            restore operation is to be performed. Check appliance for the
            configuration backup file name.
        :param path:
            The location in the target appliance where the file containing the
            backup exists. The path and the filename together create the input
            to the config replace command,.
            For an IOSXE appliance the path pattern is flash://<filename>.
        """  # noqa: E501
        raise AttributeError('cli_restore')

    def grpc_config(
        self,
        *,
        config: str = _Unknown,
        state: str = _Unknown,
        backup: bool = False,
        backup_options: Mapping[str, Incomplete] = _Unknown,
    ) -> GrpcConfigResults:
        """
        Fetch configuration/state data from gRPC enabled target hosts.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.grpc_config_module>`

        :param config:
            This option specifies the string which acts as a filter to
            restrict the portions of the data to be retrieved from the target
            host device. If this option is not specified the entire
            configuration or state data is returned in response provided it is
            supported by target host.
        :param state:
            action to be performed.
        :param backup:
            This argument will cause the module to create a full backup of the
            current ``running-config`` from the remote device before any
            changes are made. If the ``backup_options`` value is not given,
            the backup file is written to the ``backup`` folder in the
            playbook root directory or role root directory, if playbook is
            part of an ansible role. If the directory does not exist, it is
            created.
        :param backup_options:
            This is a dict object containing configurable options related to
            backup file path. The value of this option is read only when
            ``backup`` is set to *True*, if ``backup`` is set to *False* this
            option will be silently ignored.
        """  # noqa: E501
        raise AttributeError('grpc_config')

    def grpc_get(
        self,
        *,
        section: str = _Unknown,
        command: str = _Unknown,
        display: str = _Unknown,
        data_type: str = _Unknown,
    ) -> GrpcGetResults:
        """
        Fetch configuration/state data from gRPC enabled target hosts.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.grpc_get_module>`

        :param section:
            This option specifies the string which acts as a filter to
            restrict the portions of the data to be retrieved from the target
            host device. If this option is not specified the entire
            configuration or state data is returned in response provided it is
            supported by target host.
        :param command:
            The option specifies the command to be executed on the target host
            and return the response in result. This option is supported if the
            gRPC target host supports executing CLI command over the gRPC
            connection.
        :param display:
            Encoding scheme to use when serializing output from the device.
            The encoding scheme value depends on the capability of the gRPC
            server running on the target host. The values can be *json*,
            *text* etc.
        :param data_type:
            The type of data that should be fetched from the target host. The
            value depends on the capability of the gRPC server running on
            target host. The values can be *config*, *oper* etc. based on what
            is supported by the gRPC server. By default it will return both
            configuration and operational state data in response.
        """  # noqa: E501
        raise AttributeError('grpc_get')

    def net_get(
        self,
        *,
        src: str,
        protocol: Literal['scp', 'sftp'] = 'scp',
        dest: str = _Unknown,
    ) -> NetGetResults:
        """
        Copy a file from a network device to Ansible Controller.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.net_get_module>`

        :param src:
            Specifies the source file. The path to the source file can either
            be the full path on the network device or a relative path as per
            path supported by destination network device.
        :param protocol:
            Protocol used to transfer file.
        :param dest:
            Specifies the destination file. The path to the destination file
            can either be the full path on the Ansible control host or a
            relative path from the playbook or role root directory.
        """  # noqa: E501
        raise AttributeError('net_get')

    def net_ping(
        self,
        *,
        count: int | str = 5,
        dest: str,
        source: str = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        vrf: str = 'default',
    ) -> NetPingResults:
        """
        Tests reachability using ping from a network device.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.net_ping_module>`

        :param count:
            Number of packets to send.
        :param dest:
            The IP Address or hostname (resolvable by switch) of the remote
            node.
        :param source:
            The source IP Address.
        :param state:
            Determines if the expected result is success or fail.
        :param vrf:
            The VRF to use for forwarding.
        """  # noqa: E501
        raise AttributeError('net_ping')

    def net_put(
        self,
        *,
        src: str,
        protocol: Literal['scp', 'sftp'] = 'scp',
        dest: str = _Unknown,
        mode: Literal['binary', 'text'] = 'binary',
    ) -> NetPutResults:
        """
        Copy a file from Ansible Controller to a network device.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.net_put_module>`

        :param src:
            Specifies the source file. The path to the source file can either
            be the full path on the Ansible control host or a relative path
            from the playbook or role root directory.
        :param protocol:
            Protocol used to transfer file.
        :param dest:
            Specifies the destination file. The path to destination file can
            either be the full path or relative path as supported by
            network_os.
        :param mode:
            Set the file transfer mode. If mode is set to *text* then *src*
            file will go through Jinja2 template engine to replace any vars if
            present in the src file. If mode is set to *binary* then file will
            be copied as it is to destination device.
        """  # noqa: E501
        raise AttributeError('net_put')

    def netconf_config(
        self,
        *,
        content: str = _Unknown,
        target: Literal['auto', 'candidate', 'running'] = 'auto',
        source_datastore: str = _Unknown,
        format: Literal['xml', 'text', 'json'] = _Unknown,
        lock: Literal['never', 'always', 'if-supported'] = 'always',
        default_operation: Literal['merge', 'replace', 'none'] = _Unknown,
        confirm: int = 0,
        confirm_commit: bool = False,
        error_option: Literal[
            'stop-on-error',
            'continue-on-error',
            'rollback-on-error',
        ] = 'stop-on-error',
        save: bool = False,
        backup: bool = False,
        delete: bool = False,
        commit: bool = True,
        validate: bool = False,
        backup_options: Mapping[str, Incomplete] = _Unknown,
        get_filter: str = _Unknown,
    ) -> NetconfConfigResults:
        """
        netconf device configuration.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.netconf_config_module>`

        :param content:
            The configuration data as defined by the device's data models, the
            value can be either in xml string format or text format or python
            dictionary representation of JSON format.
            In case of json string format it will be converted to the
            corresponding xml string using xmltodict library before pushing
            onto the remote host.
            In case the value of this option isn *text* format the format
            should be supported by remote Netconf server.
            If the value of ``content`` option is in *xml* format in that case
            the xml value should have *config* as root tag.
        :param target:
            Name of the configuration datastore to be edited. - auto, uses
            candidate and fallback to running - candidate, edit <candidate/>
            datastore and then commit - running, edit <running/> datastore
            directly.
        :param source_datastore:
            Name of the configuration datastore to use as the source to copy
            the configuration to the datastore mentioned by ``target`` option.
            The values can be either *running*, *candidate*, *startup* or a
            remote URL.
        :param format:
            The format of the configuration provided as value of ``content``.
            In case of json string format it will be converted to the
            corresponding xml string using xmltodict library before pushing
            onto the remote host.
            In case of *text* format of the configuration should be supported
            by remote Netconf server.
            If the value of ``format`` options is not given it tries to guess
            the data format of ``content`` option as one of *xml* or *json* or
            *text*.
            If the data format is not identified it is set to *xml* by default.
        :param lock:
            Instructs the module to explicitly lock the datastore specified as
            ``target``. By setting the option value *always* is will
            explicitly lock the datastore mentioned in ``target`` option. It
            the value is *never* it will not lock the ``target`` datastore.
            The value *if-supported* lock the ``target`` datastore only if it
            is supported by the remote Netconf server.
        :param default_operation:
            The default operation for <edit-config> rpc, valid values are
            *merge*, *replace* and *none*. If the default value is merge, the
            configuration data in the ``content`` option is merged at the
            corresponding level in the ``target`` datastore. If the value is
            replace the data in the ``content`` option completely replaces the
            configuration in the ``target`` datastore. If the value is none
            the ``target`` datastore is unaffected by the configuration in the
            config option, unless and until the incoming configuration data
            uses the ``operation`` operation to request a different operation.
        :param confirm:
            This argument will configure a timeout value for the commit to be
            confirmed before it is automatically rolled back. If the
            ``confirm_commit`` argument is set to False, this argument is
            silently ignored. If the value of this argument is set to 0, the
            commit is confirmed immediately. The remote host MUST support
            :candidate and :confirmed-commit capability for this option to .
        :param confirm_commit:
            This argument will execute commit operation on remote device. It
            can be used to confirm a previous commit.
        :param error_option:
            This option controls the netconf server action after an error
            occurs while editing the configuration.
            If *error_option=stop-on-error*, abort the config edit on first
            error.
            If *error_option=continue-on-error*, continue to process
            configuration data on error. The error is recorded and negative
            response is generated if any errors occur.
            If *error_option=rollback-on-error*, rollback to the original
            configuration if any error occurs. This requires the remote
            Netconf server to support the *error_option=rollback-on-error*
            capability.
        :param save:
            The ``save`` argument instructs the module to save the
            configuration in ``target`` datastore to the startup-config if
            changed and if :startup capability is supported by Netconf server.
        :param backup:
            This argument will cause the module to create a full backup of the
            current ``running-config`` from the remote device before any
            changes are made. If the ``backup_options`` value is not given,
            the backup file is written to the ``backup`` folder in the
            playbook root directory or role root directory, if playbook is
            part of an ansible role. If the directory does not exist, it is
            created.
        :param delete:
            It instructs the module to delete the configuration from value
            mentioned in ``target`` datastore.
        :param commit:
            This boolean flag controls if the configuration changes should be
            committed or not after editing the candidate datastore. This
            option is supported only if remote Netconf server supports
            :candidate capability. If the value is set to *False* commit won't
            be issued after edit-config operation and user needs to handle
            commit or discard-changes explicitly.
        :param validate:
            This boolean flag if set validates the content of datastore given
            in ``target`` option. For this option to work remote Netconf
            server should support :validate capability.
        :param backup_options:
            This is a dict object containing configurable options related to
            backup file path. The value of this option is read only when
            ``backup`` is set to *True*, if ``backup`` is set to *False* this
            option will be silently ignored.
        :param get_filter:
            This argument specifies the XML string which acts as a filter to
            restrict the portions of the data retrieved from the remote device
            when comparing the before and after state of the device following
            calls to edit_config. When not specified, the entire configuration
            or state data is returned for comparison depending on the value of
            ``source`` option. The ``get_filter`` value can be either XML
            string or XPath or JSON string or native python dictionary, if the
            filter is in XPath format the NETCONF server running on remote
            host should support xpath capability else it will result in an
            error.
        """  # noqa: E501
        raise AttributeError('netconf_config')

    def netconf_get(
        self,
        *,
        source: Literal['running', 'candidate', 'startup'] = _Unknown,
        filter: str = _Unknown,
        display: Literal['json', 'pretty', 'xml', 'native'] = _Unknown,
        lock: Literal['never', 'always', 'if-supported'] = 'never',
    ) -> NetconfGetResults:
        """
        Fetch configuration/state data from NETCONF enabled network devices.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.netconf_get_module>`

        :param source:
            This argument specifies the datastore from which configuration
            data should be fetched. Valid values are *running*, *candidate*
            and *startup*. If the ``source`` value is not set both
            configuration and state information are returned in response from
            running datastore.
        :param filter:
            This argument specifies the string which acts as a filter to
            restrict the portions of the data to be are retrieved from the
            remote device. If this option is not specified entire
            configuration or state data is returned in result depending on the
            value of ``source`` option. The ``filter`` value can be either XML
            string or XPath or JSON string or native python dictionary, if the
            filter is in XPath format the NETCONF server running on remote
            host should support xpath capability else it will result in an
            error. If the filter is in JSON format the xmltodict library
            should be installed on the control node for JSON to XML conversion.
        :param display:
            Encoding scheme to use when serializing output from the device.
            The option *json* will serialize the output as JSON data. If the
            option value is *json* it requires jxmlease to be installed on
            control node. The option *pretty* is similar to received XML
            response but is using human readable format (spaces, new lines).
            The option value *xml* is similar to received XML response but
            removes all XML namespaces.
        :param lock:
            Instructs the module to explicitly lock the datastore specified as
            ``source``. If no *source* is defined, the *running* datastore
            will be locked. By setting the option value *always* is will
            explicitly lock the datastore mentioned in ``source`` option. By
            setting the option value *never* it will not lock the ``source``
            datastore. The value *if-supported* allows better interworking
            with NETCONF servers, which do not support the (un)lock operation
            for all supported datastores.
        """  # noqa: E501
        raise AttributeError('netconf_get')

    def netconf_rpc(
        self,
        *,
        rpc: str,
        xmlns: str = _Unknown,
        content: str = _Unknown,
        display: Literal['json', 'pretty', 'xml'] = _Unknown,
    ) -> NetconfRpcResults:
        """
        Execute operations on NETCONF enabled network devices.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.netconf_rpc_module>`

        :param rpc:
            This argument specifies the request (name of the operation) to be
            executed on the remote NETCONF enabled device.
        :param xmlns:
            NETCONF operations not defined in rfc6241 typically require the
            appropriate XML namespace to be set. In the case the *request*
            option is not already provided in XML format, the namespace can be
            defined by the *xmlns* option.
        :param content:
            This argument specifies the optional request content (all RPC
            attributes). The *content* value can either be provided as XML
            formatted string or as dictionary.
        :param display:
            Encoding scheme to use when serializing output from the device.
            The option *json* will serialize the output as JSON data. If the
            option value is *json* it requires jxmlease to be installed on
            control node. The option *pretty* is similar to received XML
            response but is using human readable format (spaces, new lines).
            The option value *xml* is similar to received XML response but
            removes all XML namespaces.
        """  # noqa: E501
        raise AttributeError('netconf_rpc')

    def network_resource(
        self,
        *,
        os_name: str = _Unknown,
        name: str = _Unknown,
        config: str = _Unknown,
        running_config: str = _Unknown,
        state: str = _Unknown,
    ) -> NetworkResourceResults:
        """
        Manage resource modules.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.network_resource_module>`

        :param os_name:
            The name of the os to manage the resource modules.
            The name should be fully qualified collection name format, that is
            *<namespace>.<collection-name>.<plugin-name>*.
            If value of this option is not set the os value will be read from
            *ansible_network_os* variable.
            If value of both *os_name* and *ansible_network_os* is not set it
            will result in error.
        :param name:
            The name of the resource module to manage.
            The resource module should be supported for given *os_name*, if
            not supported it will result in error.
        :param config:
            The resource module configuration. For details on the type and
            structure of this option refer the individual resource module
            platform documentation.
        :param running_config:
            This option is used only with state *parsed*.
            The value of this option should be the output received from the
            host device by executing the cli command to get the resource
            configuration on host.
            The state *parsed* reads the configuration from ``running_config``
            option and transforms it into Ansible structured data as per the
            resource module's argspec and the value is then returned in the
            *parsed* key within the result.
        :param state:
            The state the configuration should be left in.
            For supported values refer the individual resource module platform
            documentation.
        """  # noqa: E501
        raise AttributeError('network_resource')

    def restconf_config(
        self,
        *,
        path: str,
        content: str = _Unknown,
        method: Literal['post', 'put', 'patch', 'delete'] = 'post',
        format: Literal['json', 'xml'] = 'json',
    ) -> RestconfConfigResults:
        """
        Handles create, update, read and delete of configuration data on
        RESTCONF enabled devices.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.restconf_config_module>`

        :param path:
            URI being used to execute API calls.
        :param content:
            The configuration data in format as specififed in ``format``
            option. Required unless ``method`` is *delete*.
        :param method:
            The RESTCONF method to manage the configuration change on device.
            The value *post* is used to create a data resource or invoke an
            operation resource, *put* is used to replace the target data
            resource, *patch* is used to modify the target resource, and
            *delete* is used to delete the target resource.
        :param format:
            The format of the configuration provided as value of ``content``.
            Accepted values are *xml* and *json* and the given configuration
            format should be supported by remote RESTCONF server.
        """  # noqa: E501
        raise AttributeError('restconf_config')

    def restconf_get(
        self,
        *,
        path: str,
        content: Literal['config', 'nonconfig', 'all'] = _Unknown,
        output: Literal['json', 'xml'] = 'json',
    ) -> RestconfGetResults:
        """
        Fetch configuration/state data from RESTCONF enabled devices.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.restconf_get_module>`

        :param path:
            URI being used to execute API calls.
        :param content:
            The ``content`` is a query parameter that controls how descendant
            nodes of the requested data nodes in ``path`` will be processed in
            the reply. If value is *config* return only configuration
            descendant data nodes of value in ``path``. If value is
            *nonconfig* return only non-configuration descendant data nodes of
            value in ``path``. If value is *all* return all descendant data
            nodes of value in ``path``.
        :param output:
            The output of response received.
        """  # noqa: E501
        raise AttributeError('restconf_get')

    def telnet(
        self,
        *,
        command: Sequence[str],
        host: str = 'remote_addr',
        user: str = 'remote_user',
        password: str = _Unknown,
        port: int = 23,
        timeout: int = 120,
        prompts: Sequence[str] = _Unknown,
        login_prompt: str = _Unknown,
        password_prompt: str = _Unknown,
        pause: int = 1,
        send_newline: bool = False,
        crlf: bool = False,
    ) -> TelnetResults:
        """
        Executes a low-down and dirty telnet command.

        .. seealso::
            :ref:`ansible.netcommon <ansible_collections.ansible.netcommon.telnet_module>`

        :param command:
            List of commands to be executed in the telnet session.
        :param host:
            The host/target on which to execute the command.
        :param user:
            The user for login.
        :param password:
            The password for login.
        :param port:
            Remote port to use.
        :param timeout:
            timeout for remote operations.
        :param prompts:
            List of prompts expected before sending next command.
        :param login_prompt:
            Login or username prompt to expect.
        :param password_prompt:
            Login or username prompt to expect.
        :param pause:
            Seconds to pause between each command issued.
        :param send_newline:
            Sends a newline character upon successful connection to start the
            terminal session.
        :param crlf:
            Sends a CRLF (Carrage Return) instead of just a LF (Line Feed).
        """  # noqa: E501
        raise AttributeError('telnet')

    #
    # ansible.netcommon end
    # ansible.posix start
    #

    def acl(
        self,
        *,
        path: StrPath,
        state: Literal['absent', 'present', 'query'] = 'query',
        follow: bool = True,
        default: bool = False,
        entity: str = '',
        etype: Literal['group', 'mask', 'other', 'user'] = _Unknown,
        permissions: str = _Unknown,
        entry: str = _Unknown,
        recursive: bool = False,
        use_nfsv4_acls: bool = False,
        recalculate_mask: Literal['default', 'mask', 'no_mask'] = 'default',
    ) -> AclResults:
        """
        Set and retrieve file ACL information.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.acl_module>`

        :param path:
            The full path of the file or object.
        :param state:
            Define whether the ACL should be present or not.
            The ``query`` state gets the current ACL without changing it, for
            use in ``register`` operations.
        :param follow:
            Whether to follow symlinks on the path if a symlink is encountered.
        :param default:
            If the target is a directory, setting this to ``true`` will make
            it the default ACL for entities created inside the directory.
            Setting ``default`` to ``true`` causes an error if the path is a
            file.
        :param entity:
            The actual user or group that the ACL applies to when matching
            entity types user or group are selected.
        :param etype:
            The entity type of the ACL to apply, see ``setfacl`` documentation
            for more info.
        :param permissions:
            The permissions to apply/remove can be any combination of ``r``,
            ``w``, ``x``.
            (read, write and execute respectively), and ``X`` (execute
            permission if the file is a directory or already has execute
            permission for some user).
        :param entry:
            DEPRECATED.
            The ACL to set or remove.
            This must always be quoted in the form of
            ``<etype>:<qualifier>:<perms>``.
            The qualifier may be empty for some types, but the type and perms
            are always required.
            ``-`` can be used as placeholder when you do not care about
            permissions.
            This is now superseded by entity, type and permissions fields.
        :param recursive:
            Recursively sets the specified ACL.
            Incompatible with ``state=query``.
            Alias ``recurse`` added in version 1.3.0.
        :param use_nfsv4_acls:
            Use NFSv4 ACLs instead of POSIX ACLs.
        :param recalculate_mask:
            Select if and when to recalculate the effective right masks of the
            files.
            See ``setfacl`` documentation for more info.
            Incompatible with ``state=query``.
        """
        raise AttributeError('acl')

    def at(
        self,
        *,
        command: str = _Unknown,
        script_file: str = _Unknown,
        count: int = _Unknown,
        units: Literal['minutes', 'hours', 'days', 'weeks'] = _Unknown,
        state: Literal['absent', 'present'] = 'present',
        unique: bool = False,
    ) -> AtResults:
        """
        Schedule the execution of a command or script file via the at command.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.at_module>`

        :param command:
            A command to be executed in the future.
        :param script_file:
            An existing script file to be executed in the future.
        :param count:
            The count of units in the future to execute the command or script
            file.
        :param units:
            The type of units in the future to execute the command or script
            file.
        :param state:
            The state dictates if the command or script file should be
            evaluated as present(added) or absent(deleted).
        :param unique:
            If a matching job is present a new job will not be added.
        """
        raise AttributeError('at')

    def authorized_key(
        self,
        *,
        user: str,
        key: str,
        path: StrPath = _Unknown,
        manage_dir: bool = True,
        state: Literal['absent', 'present'] = 'present',
        key_options: str = _Unknown,
        exclusive: bool = False,
        validate_certs: bool = True,
        comment: str = _Unknown,
        follow: bool = False,
    ) -> AuthorizedKeyResults:
        """
        Adds or removes an SSH authorized key.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.authorized_key_module>`

        :param user:
            The username on the remote host whose authorized_keys file will be
            modified.
        :param key:
            The SSH public key(s), as a string or (since Ansible 1.9) url
            (https://github.com/username.keys).
        :param path:
            Alternate path to the authorized_keys file.
            When unset, this value defaults to *~/.ssh/authorized_keys*.
        :param manage_dir:
            Whether this module should manage the directory of the authorized
            key file.
            If set to ``true``, the module will create the directory, as well
            as set the owner and permissions of an existing directory.
            Be sure to set ``manage_dir=false`` if you are using an alternate
            directory for authorized_keys, as set with ``path``, since you
            could lock yourself out of SSH access.
            See the example below.
        :param state:
            Whether the given key (with the given key_options) should or
            should not be in the file.
        :param key_options:
            A string of ssh key options to be prepended to the key in the
            authorized_keys file.
        :param exclusive:
            Whether to remove all other non-specified keys from the
            authorized_keys file.
            Multiple keys can be specified in a single ``key`` string value by
            separating them by newlines.
            This option is not loop aware, so if you use ``with_`` , it will
            be exclusive per iteration of the loop.
            If you want multiple keys in the file you need to pass them all to
            ``key`` in a single batch as mentioned above.
        :param validate_certs:
            This only applies if using a https url as the source of the keys.
            If set to ``false``, the SSL certificates will not be validated.
            This should only set to ``false`` used on personally controlled
            sites using self-signed certificates as it avoids verifying the
            source site.
            Prior to 2.1 the code worked as if this was set to ``true``.
        :param comment:
            Change the comment on the public key.
            Rewriting the comment is useful in cases such as fetching it from
            GitHub or GitLab.
            If no comment is specified, the existing comment will be kept.
        :param follow:
            Follow path symlink instead of replacing it.
        """  # noqa: E501
        raise AttributeError('authorized_key')

    def firewalld(
        self,
        *,
        service: str = _Unknown,
        protocol: str = _Unknown,
        port: str = _Unknown,
        port_forward: Sequence[Mapping[str, Incomplete]] = _Unknown,
        rich_rule: str = _Unknown,
        source: str = _Unknown,
        interface: str = _Unknown,
        icmp_block: str = _Unknown,
        icmp_block_inversion: str = _Unknown,
        zone: str = _Unknown,
        permanent: bool = _Unknown,
        immediate: bool = False,
        state: Literal[
            'absent',
            'disabled',
            'enabled',
            'present',
        ],
        timeout: int = 0,
        masquerade: str = _Unknown,
        offline: bool = _Unknown,
        target: Literal[
            'default',
            'ACCEPT',
            'DROP',
            '%%REJECT%%',
        ] = _Unknown,
    ) -> FirewalldResults:
        """
        Manage arbitrary ports/services with firewalld.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.firewalld_module>`

        :param service:
            Name of a service to add/remove to/from firewalld.
            The service must be listed in output of firewall-cmd
            --get-services.
        :param protocol:
            Name of a protocol to add/remove to/from firewalld.
        :param port:
            Name of a port or port range to add/remove to/from firewalld.
            Must be in the form PORT/PROTOCOL or PORT-PORT/PROTOCOL for port
            ranges.
        :param port_forward:
            Port and protocol to forward using firewalld.
        :param rich_rule:
            Rich rule to add/remove to/from firewalld.
            See `Syntax for firewalld rich language rules
            <https://firewalld.org/documentation/man-pages/firewalld.richlanguage.html>`__.
        :param source:
            The source/network you would like to add/remove to/from firewalld.
        :param interface:
            The interface you would like to add/remove to/from a zone in
            firewalld.
        :param icmp_block:
            The ICMP block you would like to add/remove to/from a zone in
            firewalld.
        :param icmp_block_inversion:
            Enable/Disable inversion of ICMP blocks for a zone in firewalld.
        :param zone:
            The firewalld zone to add/remove to/from.
            Note that the default zone can be configured per system but
            ``public`` is default from upstream.
            Available choices can be extended based on per-system configs,
            listed here are "out of the box" defaults.
            Possible values include ``block``, ``dmz``, ``drop``,
            ``external``, ``home``, ``internal``, ``public``, ``trusted``,
            ``work``.
        :param permanent:
            Should this configuration be in the running firewalld
            configuration or persist across reboots.
            As of Ansible 2.3, permanent operations can operate on firewalld
            configs when it is not running (requires firewalld >= 0.3.9).
            Note that if this is ``false``, immediate is assumed ``true``.
        :param immediate:
            Should this configuration be applied immediately, if set as
            permanent.
        :param state:
            Enable or disable a setting.
            For ports: Should this port accept (enabled) or reject (disabled)
            connections.
            The states ``present`` and ``absent`` can only be used in zone
            level operations (i.e. when no other parameters but zone and state
            are set).
        :param timeout:
            The amount of time in seconds the rule should be in effect for
            when non-permanent.
        :param masquerade:
            The masquerade setting you would like to enable/disable to/from
            zones within firewalld.
        :param offline:
            Whether to run this module even when firewalld is offline.
        :param target:
            firewalld Zone target.
            If state is set to ``absent``, this will reset the target to
            default.
        """  # noqa: E501
        raise AttributeError('firewalld')

    def firewalld_info(
        self,
        *,
        active_zones: bool = False,
        zones: Sequence[str] = _Unknown,
    ) -> FirewalldInfoResults:
        """
        Gather information about firewalld.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.firewalld_info_module>`

        :param active_zones:
            Gather information about active zones.
        :param zones:
            Gather information about specific zones.
            If only works if ``active_zones`` is set to ``false``.
        """  # noqa: E501
        raise AttributeError('firewalld_info')

    def mount(
        self,
        *,
        path: StrPath,
        src: StrPath = _Unknown,
        fstype: str = _Unknown,
        opts: str = _Unknown,
        dump: str = '0',
        passno: str = '0',
        state: Literal[
            'absent',
            'absent_from_fstab',
            'mounted',
            'present',
            'unmounted',
            'remounted',
            'ephemeral',
        ],
        fstab: str = _Unknown,
        boot: bool = True,
        backup: bool = False,
    ) -> MountResults:
        """
        Control active and configured mount points.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.mount_module>`

        :param path:
            Path to the mount point (e.g. ``/mnt/files``).
            Before Ansible 2.3 this option was only usable as *dest*,
            *destfile* and *name*.
        :param src:
            Device (or NFS volume, or something else) to be mounted on *path*.
            Required when *state* set to ``present``, ``mounted`` or
            ``ephemeral``.
        :param fstype:
            Filesystem type.
            Required when *state* is ``present``, ``mounted`` or ``ephemeral``.
        :param opts:
            Mount options (see fstab(5), or vfstab(4) on Solaris).
        :param dump:
            Dump (see fstab(5)).
            Note that if set to ``null`` and *state* set to ``present``, it
            will cease to work and duplicate entries will be made with
            subsequent runs.
            Has no effect on Solaris systems or when used with ``ephemeral``.
        :param passno:
            Passno (see fstab(5)).
            Note that if set to ``null`` and *state* set to ``present``, it
            will cease to work and duplicate entries will be made with
            subsequent runs.
            Deprecated on Solaris systems. Has no effect when used with
            ``ephemeral``.
        :param state:
            If ``mounted``, the device will be actively mounted and
            appropriately configured in *fstab*. If the mount point is not
            present, the mount point will be created.
            If ``unmounted``, the device will be unmounted without changing
            *fstab*.
            ``present`` only specifies that the device is to be configured in
            *fstab* and does not trigger or require a mount.
            ``ephemeral`` only specifies that the device is to be mounted,
            without changing *fstab*. If it is already mounted, a remount will
            be triggered. This will always return changed=True. If the mount
            point *path* has already a device mounted on, and its source is
            different than *src*, the module will fail to avoid unexpected
            unmount or mount point override. If the mount point is not
            present, the mount point will be created. The *fstab* is
            completely ignored. This option is added in version 1.5.0.
            ``absent`` specifies that the device mount's entry will be removed
            from *fstab* and will also unmount the device and remove the mount
            point.
            ``remounted`` specifies that the device will be remounted for when
            you want to force a refresh on the mount itself (added in 2.9).
            This will always return changed=true. If *opts* is set, the
            options will be applied to the remount, but will not change
            *fstab*. Additionally, if *opts* is set, and the remount command
            fails, the module will error to prevent unexpected mount changes.
            Try using ``mounted`` instead to work around this issue.
            ``remounted`` expects the mount point to be present in the
            *fstab*. To remount a mount point not registered in *fstab*, use
            ``ephemeral`` instead, especially with BSD nodes.
            ``absent_from_fstab`` specifies that the device mount's entry will
            be removed from *fstab*. This option does not unmount it or delete
            the mountpoint.
        :param fstab:
            File to use instead of ``/etc/fstab``.
            You should not use this option unless you really know what you are
            doing.
            This might be useful if you need to configure mountpoints in a
            chroot environment.
            OpenBSD does not allow specifying alternate fstab files with mount
            so do not use this on OpenBSD with any state that operates on the
            live filesystem.
            This parameter defaults to /etc/fstab or /etc/vfstab on Solaris.
            This parameter is ignored when *state* is set to ``ephemeral``.
        :param boot:
            Determines if the filesystem should be mounted on boot.
            Only applies to Solaris and Linux systems.
            For Solaris systems, ``true`` will set ``True`` as the value of
            mount at boot in */etc/vfstab*.
            For Linux, FreeBSD, NetBSD and OpenBSD systems, ``false`` will add
            ``noauto`` to mount options in */etc/fstab*.
            To avoid mount option conflicts, if ``noauto`` specified in
            ``opts``, mount module will ignore ``boot``.
            This parameter is ignored when *state* is set to ``ephemeral``.
        :param backup:
            Create a backup file including the timestamp information so you
            can get the original file back if you somehow clobbered it
            incorrectly.
        """  # noqa: E501
        raise AttributeError('mount')

    def patch(
        self,
        *,
        basedir: StrPath = _Unknown,
        dest: StrPath = _Unknown,
        src: StrPath,
        state: Literal['absent', 'present'] = 'present',
        remote_src: bool = False,
        strip: int = 0,
        backup: bool = False,
        binary: bool = False,
        ignore_whitespace: bool = False,
    ) -> PatchResults:
        """
        Apply patch files using the GNU patch tool.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.patch_module>`

        :param basedir:
            Path of a base directory in which the patch file will be applied.
            May be omitted when ``dest`` option is specified, otherwise
            required.
        :param dest:
            Path of the file on the remote machine to be patched.
            The names of the files to be patched are usually taken from the
            patch file, but if there's just one file to be patched it can
            specified with this option.
        :param src:
            Path of the patch file as accepted by the GNU patch tool. If
            ``remote_src`` is ``false``, the patch source file is looked up
            from the module's *files* directory.
        :param state:
            Whether the patch should be applied or reverted.
        :param remote_src:
            If ``false``, it will search for src at originating/controller
            machine, if ``true`` it will go to the remote/target machine for
            the ``src``.
        :param strip:
            Number that indicates the smallest prefix containing leading
            slashes that will be stripped from each file name found in the
            patch file.
            For more information see the strip parameter of the GNU patch tool.
        :param backup:
            Passes ``--backup --version-control=numbered`` to patch, producing
            numbered backup copies.
        :param binary:
            Setting to ``true`` will disable patch's heuristic for
            transforming CRLF line endings into LF.
            Line endings of src and dest must match.
            If set to ``false``, ``patch`` will replace CRLF in ``src`` files
            on POSIX.
        :param ignore_whitespace:
            Setting to ``true`` will ignore white space changes between patch
            and input.
        """  # noqa: E501
        raise AttributeError('patch')

    def rhel_facts(self, arg: str, /) -> RhelFactsResults:
        """
        Facts module to set or override RHEL specific facts.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.rhel_facts_module>`
        """  # noqa: E501
        raise AttributeError('rhel_facts')

    def rhel_rpm_ostree(
        self,
        *,
        name: Sequence[str] = _Unknown,
        state: Literal[
            'absent',
            'installed',
            'latest',
            'present',
            'removed',
        ] = _Unknown,
    ) -> RhelRpmOstreeResults:
        """
        Ensure packages exist in a RHEL for Edge rpm-ostree based system.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.rhel_rpm_ostree_module>`

        :param name:
            A package name or package specifier with version, like
            ``name-1.0``.
            Comparison operators for package version are valid here ``>``,
            ``<``, ``>=``, ``<=``. Example - ``name>=1.0``.
            If a previous version is specified, the task also needs to turn
            ``allow_downgrade`` on. See the ``allow_downgrade`` documentation
            for caveats with downgrading packages.
            When using state=latest, this can be ``'*'`` which means run
            ``yum -y update``.
            You can also pass a url or a local path to a rpm file (using
            state=present). To operate on several packages this can accept a
            comma separated string of packages or (as of 2.0) a list of
            packages.
        :param state:
            Whether to install (``present`` or ``installed``, ``latest``), or
            remove (``absent`` or ``removed``) a package.
            ``present`` and ``installed`` will simply ensure that a desired
            package is installed.
            ``latest`` will update the specified package if it's not of the
            latest available version.
            ``absent`` and ``removed`` will remove the specified package.
            Default is ``None``, however in effect the default action is
            ``present`` unless the ``autoremove`` option is enabled for this
            module, then ``absent`` is inferred.
        """  # noqa: E501
        raise AttributeError('rhel_rpm_ostree')

    def rpm_ostree_upgrade(
        self,
        *,
        os: str = '',
        cache_only: bool = False,
        allow_downgrade: bool = False,
        peer: bool = False,
    ) -> RpmOstreeUpgradeResults:
        """
        Manage rpm-ostree upgrade transactions.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.rpm_ostree_upgrade_module>`

        :param os:
            The OSNAME upon which to operate.
        :param cache_only:
            Perform the transaction using only pre-cached data, do not
            download.
        :param allow_downgrade:
            Allow for the upgrade to be a chronologically older tree.
        :param peer:
            Force peer-to-peer connection instead of using a system message
            bus.
        """  # noqa: E501
        raise AttributeError('rpm_ostree_upgrade')

    def seboolean(
        self,
        *,
        name: str,
        persistent: bool = False,
        state: bool,
        ignore_selinux_state: bool = False,
    ) -> SebooleanResults:
        """
        Toggles SELinux booleans.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.seboolean_module>`

        :param name:
            Name of the boolean to configure.
        :param persistent:
            Set to ``true`` if the boolean setting should survive a reboot.
        :param state:
            Desired boolean value.
        :param ignore_selinux_state:
            Useful for scenarios (chrooted environment) that you can't get the
            real SELinux state.
        """  # noqa: E501
        raise AttributeError('seboolean')

    def selinux(
        self,
        *,
        policy: str = _Unknown,
        state: Literal[
            'disabled',
            'enforcing',
            'permissive',
        ],
        update_kernel_param: bool = False,
        configfile: str = '/etc/selinux/config',
    ) -> SelinuxResults:
        """
        Change policy and state of SELinux.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.selinux_module>`

        :param policy:
            The name of the SELinux policy to use (e.g. ``targeted``) will be
            required if *state* is not ``disabled``.
        :param state:
            The SELinux mode.
        :param update_kernel_param:
            If set to *true*, will update also the kernel boot parameters when
            disabling/enabling SELinux.
            The ``grubby`` tool must be present on the target system for this
            to work.
        :param configfile:
            The path to the SELinux configuration file, if non-standard.
        """  # noqa: E501
        raise AttributeError('selinux')

    def synchronize(
        self,
        *,
        src: str,
        dest: str,
        dest_port: int = _Unknown,
        mode: Literal['pull', 'push'] = 'push',
        archive: bool = True,
        checksum: bool = False,
        compress: bool = True,
        existing_only: bool = False,
        delete: bool = False,
        dirs: bool = False,
        recursive: bool = _Unknown,
        links: bool = _Unknown,
        copy_links: bool = False,
        perms: bool = _Unknown,
        times: bool = _Unknown,
        owner: bool = _Unknown,
        group: bool = _Unknown,
        rsync_path: str = _Unknown,
        rsync_timeout: int = 0,
        set_remote_user: bool = True,
        use_ssh_args: bool = False,
        ssh_connection_multiplexing: bool = False,
        rsync_opts: Sequence[str] = _Unknown,
        partial: bool = False,
        verify_host: bool = False,
        private_key: StrPath = _Unknown,
        link_dest: Sequence[str] = _Unknown,
        delay_updates: bool = True,
    ) -> SynchronizeResults:
        """
        A wrapper around rsync to make common tasks in your playbooks quick
        and easy.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.synchronize_module>`

        :param src:
            Path on the source host that will be synchronized to the
            destination.
            The path can be absolute or relative.
        :param dest:
            Path on the destination host that will be synchronized from the
            source.
            The path can be absolute or relative.
        :param dest_port:
            Port number for ssh on the destination host.
            Prior to Ansible 2.0, the ansible_ssh_port inventory var took
            precedence over this value.
            This parameter defaults to the value of ``ansible_port``, the
            ``remote_port`` config setting or the value from ssh client
            configuration if none of the former have been set.
        :param mode:
            Specify the direction of the synchronization.
            In push mode the localhost or delegate is the source.
            In pull mode the remote host in context is the source.
        :param archive:
            Mirrors the rsync archive flag, enables recursive, links, perms,
            times, owner, group flags and -D.
        :param checksum:
            Skip based on checksum, rather than mod-time & size; Note that
            that "archive" option is still enabled by default - the "checksum"
            option will not disable it.
        :param compress:
            Compress file data during the transfer.
            In most cases, leave this enabled unless it causes problems.
        :param existing_only:
            Skip creating new files on receiver.
        :param delete:
            Delete files in *dest* that do not exist (after transfer, not
            before) in the *src* path.
            This option requires *recursive=true*.
            This option ignores excluded files and behaves like the rsync opt
            ``--delete-after``.
        :param dirs:
            Transfer directories without recursing.
        :param recursive:
            Recurse into directories.
            This parameter defaults to the value of the archive option.
        :param links:
            Copy symlinks as symlinks.
            This parameter defaults to the value of the archive option.
        :param copy_links:
            Copy symlinks as the item that they point to (the referent) is
            copied, rather than the symlink.
        :param perms:
            Preserve permissions.
            This parameter defaults to the value of the archive option.
        :param times:
            Preserve modification times.
            This parameter defaults to the value of the archive option.
        :param owner:
            Preserve owner (super user only).
            This parameter defaults to the value of the archive option.
        :param group:
            Preserve group.
            This parameter defaults to the value of the archive option.
        :param rsync_path:
            Specify the rsync command to run on the remote host. See
            ``--rsync-path`` on the rsync man page.
            To specify the rsync command to run on the local host, you need to
            set this your task var ``ansible_rsync_path``.
        :param rsync_timeout:
            Specify a ``--timeout`` for the rsync command in seconds.
        :param set_remote_user:
            Put user@ for the remote paths.
            If you have a custom ssh config to define the remote user for a
            host that does not match the inventory user, you should set this
            parameter to ``false``.
        :param use_ssh_args:
            In Ansible 2.10 and lower, it uses the ssh_args specified in
            ``ansible.cfg``.
            In Ansible 2.11 and onwards, when set to ``true``, it uses all SSH
            connection configurations like ``ansible_ssh_args``,
            ``ansible_ssh_common_args``, and ``ansible_ssh_extra_args``.
        :param ssh_connection_multiplexing:
            SSH connection multiplexing for rsync is disabled by default to
            prevent misconfigured ControlSockets from resulting in failed SSH
            connections. This is accomplished by setting the SSH
            ``ControlSocket`` to ``none``.
            Set this option to ``true`` to allow multiplexing and reduce SSH
            connection overhead.
            Note that simply setting this option to ``true`` is not enough;
            You must also configure SSH connection multiplexing in your SSH
            client config by setting values for ``ControlMaster``,
            ``ControlPersist`` and ``ControlPath``.
        :param rsync_opts:
            Specify additional rsync options by passing in an array.
            Note that an empty string in ``rsync_opts`` will end up transfer
            the current working directory.
        :param partial:
            Tells rsync to keep the partial file which should make a
            subsequent transfer of the rest of the file much faster.
        :param verify_host:
            Verify destination host key.
        :param private_key:
            Specify the private key to use for SSH-based rsync connections
            (e.g. ``~/.ssh/id_rsa``).
        :param link_dest:
            Add a destination to hard link against during the rsync.
        :param delay_updates:
            This option puts the temporary file from each updated file into a
            holding directory until the end of the transfer, at which time all
            the files are renamed into place in rapid succession.
        """  # noqa: E501
        raise AttributeError('synchronize')

    def sysctl(
        self,
        *,
        name: str,
        value: str = _Unknown,
        state: Literal['present', 'absent'] = 'present',
        ignoreerrors: bool = False,
        reload: bool = True,
        sysctl_file: StrPath = '/etc/sysctl.conf',
        sysctl_set: bool = False,
    ) -> SysctlResults:
        """
        Manage entries in sysctl.conf.

        .. seealso::
            :ref:`ansible.posix <ansible_collections.ansible.posix.sysctl_module>`

        :param name:
            The dot-separated path (also known as *key*) specifying the sysctl
            variable.
        :param value:
            Desired value of the sysctl key.
        :param state:
            Whether the entry should be present or absent in the sysctl file.
        :param ignoreerrors:
            Use this option to ignore errors about unknown keys.
        :param reload:
            If ``true``, performs a */sbin/sysctl -p* if the ``sysctl_file``
            is updated. If ``false``, does not reload *sysctl* even if the
            ``sysctl_file`` is updated.
        :param sysctl_file:
            Specifies the absolute path to ``sysctl.conf``, if not
            ``/etc/sysctl.conf``.
        :param sysctl_set:
            Verify token value with the sysctl command and set with -w if
            necessary.
        """  # noqa: E501
        raise AttributeError('sysctl')

    #
    # ansible.posix end
    # ansible.utils start
    #

    def cli_parse(
        self,
        *,
        command: str = _Unknown,
        text: str = _Unknown,
        parser: Mapping[str, Incomplete],
        set_fact: str = _Unknown,
    ) -> CliParseResults:
        """
        Parse cli output or text using a variety of parsers.

        .. seealso::
            :ref:`ansible.utils <ansible_collections.ansible.utils.cli_parse_module>`

        :param command:
            The command to run on the host.
        :param text:
            Text to be parsed.
        :param parser:
            Parser specific parameters.
        :param set_fact:
            Set the resulting parsed data as a fact.
        """  # noqa: E501
        raise AttributeError('cli_parse')

    def fact_diff(
        self,
        *,
        before: str,
        after: str,
        plugin: Mapping[str, Incomplete] = _Unknown,
    ) -> FactDiffResults:
        """
        Find the difference between currently set facts.

        .. seealso::
            :ref:`ansible.utils <ansible_collections.ansible.utils.fact_diff_module>`

        :param before:
            The first fact to be used in the comparison.
        :param after:
            The second fact to be used in the comparison.
        :param plugin:
            Configure and specify the diff plugin to use.
        """  # noqa: E501
        raise AttributeError('fact_diff')

    def update_fact(
        self,
        *,
        updates: Sequence[Mapping[str, Incomplete]],
    ) -> UpdateFactResults:
        """
        Update currently set facts.

        .. seealso::
            :ref:`ansible.utils <ansible_collections.ansible.utils.update_fact_module>`

        :param updates:
            A list of dictionaries, each a desired update to make.
        """  # noqa: E501
        raise AttributeError('update_fact')

    def validate(
        self,
        *,
        data: str,
        engine: str = 'ansible.utils.jsonschema',
        criteria: str,
    ) -> ValidateResults:
        """
        Validate data with provided criteria.

        .. seealso::
            :ref:`ansible.utils <ansible_collections.ansible.utils.validate_module>`

        :param data:
            Data that will be validated against *criteria*. For the type of
            data refer to the documentation of individual validate plugins.
        :param engine:
            The name of the validate plugin to use. The engine value should
            follow the fully qualified collection name format, that is
            <org-name>.<collection-name>.<validate-plugin-name>.
        :param criteria:
            The criteria used for validation of *data*. For the type of
            criteria refer to the documentation of individual validate plugins.
        """  # noqa: E501
        raise AttributeError('validate')

    #
    # ansible.utils end
    # ansible.windows start
    #

    def win_acl(
        self,
        *,
        path: str,
        user: str,
        state: Literal['absent', 'present'] = 'present',
        type: Literal['allow', 'deny'],
        rights: str,
        inherit: Literal['ContainerInherit', 'ObjectInherit'] = _Unknown,
        propagation: Literal[
            'InheritOnly',
            'None',
            'NoPropagateInherit',
        ] = 'None',
        follow: bool = False,
    ) -> WinAclResults:
        """
        Set file/directory/registry/certificate permissions for a system user
        or group.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_acl_module>`

        :param path:
            The path to the file or directory.
        :param user:
            User or Group to add specified rights to act on src file/folder or
            registry key.
        :param state:
            Specify whether to add ``present`` or remove ``absent`` the
            specified access rule.
        :param type:
            Specify whether to allow or deny the rights specified.
        :param rights:
            The rights/permissions that are to be allowed/denied for the
            specified user or group for the item at ``path``.
            If ``path`` is a file or directory, rights can be any right under
            MSDN FileSystemRights
            `reference <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.filesystemrights.aspx>`__.
            If ``path`` is a registry key, rights can be any right under MSDN
            RegistryRights
            `reference <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.registryrights.aspx>`__.
            If *path* is a certificate key, rights can be ``Read`` and/or
            ``FullControl``. (Added in 2.2.0).
        :param inherit:
            Inherit flags on the ACL rules.
            Can be specified as a comma separated list, e.g.
            ``ContainerInherit``, ``ObjectInherit``.
            For more information on the choices see MSDN InheritanceFlags
            enumeration at
            `reference <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.inheritanceflags.aspx>`__.
            Defaults to ``ContainerInherit, ObjectInherit`` for Directories.
        :param propagation:
            Propagation flag on the ACL rules.
            For more information on the choices see MSDN PropagationFlags
            enumeration at
            `reference <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.propagationflags.aspx>`__.
        :param follow:
            Follow the symlinks and junctions to apply the ACLs to the target
            instead of the link.
        """  # noqa: E501
        raise AttributeError('win_acl')

    def win_acl_inheritance(
        self,
        *,
        path: str,
        state: Literal['absent', 'present'] = 'absent',
        reorganize: bool = False,
    ) -> WinAclInheritanceResults:
        """
        Change ACL inheritance.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_acl_inheritance_module>`

        :param path:
            Path to be used for changing inheritance.
            Support for registry keys have been added in
            ``ansible.windows>=1.11.0``.
        :param state:
            Specify whether to enable *present* or disable *absent* ACL
            inheritance.
        :param reorganize:
            For ``state=absent``, indicates if the inherited ACE's should be
            copied from the parent. This is necessary (in combination with
            removal) for a simple ACL instead of using multiple ACE deny
            entries.
            For ``state=present``, indicates if the inherited ACE's should be
            deduplicated compared to the parent. This removes complexity of
            the ACL structure.
        """  # noqa: E501
        raise AttributeError('win_acl_inheritance')

    def win_certificate_store(
        self,
        *,
        state: Literal['absent', 'exported', 'present'] = 'present',
        path: StrPath = _Unknown,
        thumbprint: str = _Unknown,
        store_name: str = 'My',
        store_location: str = 'LocalMachine',
        store_type: Literal['system', 'service'] = 'system',
        password: str = _Unknown,
        key_exportable: bool = True,
        key_storage: Literal['default', 'machine', 'user'] = 'default',
        file_type: Literal['der', 'pem', 'pkcs12'] = 'der',
    ) -> WinCertificateStoreResults:
        """
        Manages the certificate store.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_certificate_store_module>`

        :param state:
            If ``present``, will ensure that the certificate at *path* is
            imported into the certificate store specified.
            If ``absent``, will ensure that the certificate specified by
            *thumbprint* or the thumbprint of the cert at *path* is removed
            from the store specified.
            If ``exported``, will ensure the file at *path* is a certificate
            specified by *thumbprint*.
            When exporting a certificate, if *path* is a directory then the
            module will fail, otherwise the file will be replaced if needed.
        :param path:
            The path to a certificate file.
            This is required when *state* is ``present`` or ``exported``.
            When *state* is ``absent`` and *thumbprint* is not specified, the
            thumbprint is derived from the certificate at this path.
        :param thumbprint:
            The thumbprint as a hex string to either export or remove.
            See the examples for how to specify the thumbprint.
        :param store_name:
            The store name to use when importing a certificate or searching
            for a certificate.
            ``AddressBook``: The X.509 certificate store for other users.
            ``AuthRoot``: The X.509 certificate store for third-party
            certificate authorities (CAs).
            ``CertificateAuthority``: The X.509 certificate store for
            intermediate certificate authorities (CAs).
            ``Disallowed``: The X.509 certificate store for revoked
            certificates.
            ``My``: The X.509 certificate store for personal certificates.
            ``Root``: The X.509 certificate store for trusted root certificate
            authorities (CAs).
            ``TrustedPeople``: The X.509 certificate store for directly
            trusted people and resources.
            ``TrustedPublisher``: The X.509 certificate store for directly
            trusted publishers.
        :param store_location:
            The store location to use when importing a certificate or
            searching for a certificate.
            Can be set to ``CurrentUser`` or ``LocalMachine`` when
            ``store_type=system``.
            Defaults to ``LocalMachine`` when ``store_type=system``.
            Must be set to any service name when ``store_type=service``.
        :param store_type:
            The store type to manage.
            Use ``system`` to manage locations in the system store,
            ``LocalMachine`` and ``CurrentUser``.
            Use ``service`` to manage the store of a service account specified
            by *store_location*.
        :param password:
            The password of the pkcs12 certificate key.
            This is used when reading a pkcs12 certificate file or the
            password to set when ``state=exported`` and ``file_type=pkcs12``.
            If the pkcs12 file has no password set or no password should be
            set on the exported file, do not set this option.
        :param key_exportable:
            Whether to allow the private key to be exported.
            If ``false``, then this module and other process will only be able
            to export the certificate and the private key cannot be exported.
            Used when ``state=present`` only.
        :param key_storage:
            Specifies where Windows will store the private key when it is
            imported.
            When set to ``default``, the default option as set by Windows is
            used, typically ``user``.
            When set to ``machine``, the key is stored in a path accessible by
            various users.
            When set to ``user``, the key is stored in a path only accessible
            by the current user.
            Used when ``state=present`` only and cannot be changed once
            imported.
            See
            `reference <https://msdn.microsoft.com/en-us/library/system.security.cryptography.x509certificates.x509keystorageflags.aspx>`__
            for more details.
        :param file_type:
            The file type to export the certificate as when ``state=exported``.
            ``der`` is a binary ASN.1 encoded file.
            ``pem`` is a base64 encoded file of a der file in the OpenSSL form.
            ``pkcs12`` (also known as pfx) is a binary container that contains
            both the certificate and private key unlike the other options.
            When ``pkcs12`` is set and the private key is not exportable or
            accessible by the current user, it will throw an exception.
        """  # noqa: E501
        raise AttributeError('win_certificate_store')

    def win_command(
        self,
        *,
        _raw_params: str = _Unknown,
        cmd: str = _Unknown,
        argv: Sequence[str] = _Unknown,
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        chdir: StrPath = _Unknown,
        stdin: str = _Unknown,
        output_encoding_override: str = _Unknown,
    ) -> WinCommandResults:
        """
        Executes a command on a remote Windows node.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_command_module>`

        :param _raw_params:
            The ``win_command`` module takes a free form command to run.
            This is mutually exclusive with the ``cmd`` and ``argv`` options.
            There is no parameter actually named '_raw_params'. See the
            examples!.
        :param cmd:
            The command and arguments to run.
            This is mutually exclusive with the ``_raw_params`` and ``argv``
            options.
        :param argv:
            A list that contains the executable and arguments to run.
            The module will attempt to quote the arguments specified based on
            the `Win32 C command-line argument rules
            <https://docs.microsoft.com/en-us/cpp/c-language/parsing-c-command-line-arguments>`__.
            Not all applications use the same quoting rules so the escaping
            may not work, for those scenarios use ``cmd`` instead.
        :param creates:
            A path or path filter pattern; when the referenced path exists on
            the target host, the task will be skipped.
        :param removes:
            A path or path filter pattern; when the referenced path **does
            not** exist on the target host, the task will be skipped.
        :param chdir:
            Set the specified path as the current working directory before
            executing a command.
        :param stdin:
            Set the stdin of the command directly to the specified value.
        :param output_encoding_override:
            This option overrides the encoding of stdout/stderr output.
            You can use this option when you need to run a command which
            ignore the console's codepage.
            You should only need to use this option in very rare circumstances.
            This value can be any valid encoding ``Name`` based on the output
            of ``[System.Text.Encoding]::GetEncodings(``). See
            `reference <https://docs.microsoft.com/dotnet/api/system.text.encoding.getencodings>`__.
        """  # noqa: E501
        raise AttributeError('win_command')

    def win_copy(
        self,
        *,
        content: str = _Unknown,
        decrypt: bool = True,
        dest: StrPath,
        backup: bool = False,
        force: bool = True,
        local_follow: bool = True,
        remote_src: bool = False,
        src: StrPath = _Unknown,
    ) -> WinCopyResults:
        """
        Copies files to remote locations on windows hosts.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_copy_module>`

        :param content:
            When used instead of ``src``, sets the contents of a file directly
            to the specified value.
            This is for simple values, for anything complex or with formatting
            please switch to the :meth:`win_template` method.
        :param decrypt:
            This option controls the autodecryption of source files using
            vault.
        :param dest:
            Remote absolute path where the file should be copied to.
            If ``src`` is a directory, this must be a directory too.
            Use \\ for path separators or \\\\ when in "double quotes".
            If ``dest`` ends with \\ then source or the contents of source
            will be copied to the directory without renaming.
            If ``dest`` is a nonexistent path, it will only be created if
            ``dest`` ends with "/" or "\\", or ``src`` is a directory.
            If ``src`` and ``dest`` are files and if the parent directory of
            ``dest`` doesn't exist, then the task will fail.
        :param backup:
            Determine whether a backup should be created.
            When set to ``true``, create a backup file including the timestamp
            information so you can get the original file back if you somehow
            clobbered it incorrectly.
            No backup is taken when ``remote_src=False`` and multiple files
            are being copied.
        :param force:
            If set to ``true``, the file will only be transferred if the
            content is different than destination.
            If set to ``false``, the file will only be transferred if the
            destination does not exist.
            If set to ``false``, no checksuming of the content is performed
            which can help improve performance on larger files.
        :param local_follow:
            This flag indicates that filesystem links in the source tree, if
            they exist, should be followed.
        :param remote_src:
            If ``false``, it will search for src at originating/controller
            machine.
            If ``true``, it will go to the remote/target machine for the src.
        :param src:
            Local path to a file to copy to the remote server; can be absolute
            or relative.
            If path is a directory, it is copied (including the source folder
            name) recursively to ``dest``.
            If path is a directory and ends with "/", only the inside contents
            of that directory are copied to the destination. Otherwise, if it
            does not end with "/", the directory itself with all contents is
            copied.
            If path is a file and dest ends with "\\", the file is copied to
            the folder with the same filename.
            Required unless using ``content``.
        """  # noqa: E501
        raise AttributeError('win_copy')

    def win_dns_client(
        self,
        *,
        adapter_names: Sequence[str],
        dns_servers: Sequence[str],
    ) -> WinDnsClientResults:
        """
        Configures DNS lookup on Windows hosts.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_dns_client_module>`

        :param adapter_names:
            Adapter name or list of adapter names for which to manage DNS
            settings ('*' is supported as a wildcard value).
            The adapter name used is the connection caption in the Network
            Control Panel or the InterfaceAlias of
            ``Get-DnsClientServerAddress``.
        :param dns_servers:
            Single or ordered list of DNS servers (IPv4 and IPv6 addresses) to
            configure for lookup.
            An empty list will configure the adapter to use the DHCP-assigned
            values on connections where DHCP is enabled, or disable DNS lookup
            on statically-configured connections.
            IPv6 DNS servers can only be set on Windows Server 2012 or newer,
            older hosts can only set IPv4 addresses.
        """  # noqa: E501
        raise AttributeError('win_dns_client')

    def win_domain(
        self,
        *,
        dns_domain_name: str,
        domain_netbios_name: str = _Unknown,
        safe_mode_password: str,
        database_path: StrPath = _Unknown,
        log_path: StrPath = _Unknown,
        sysvol_path: StrPath = _Unknown,
        create_dns_delegation: bool = _Unknown,
        domain_mode: Literal[
            'Win2003',
            'Win2008',
            'Win2008R2',
            'Win2012',
            'Win2012R2',
            'WinThreshold',
        ] = _Unknown,
        forest_mode: Literal[
            'Win2003',
            'Win2008',
            'Win2008R2',
            'Win2012',
            'Win2012R2',
            'WinThreshold',
        ] = _Unknown,
        install_dns: bool = True,
    ) -> WinDomainResults:
        """
        Ensures the existence of a Windows domain.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_domain_module>`

        :param dns_domain_name:
            The DNS name of the domain which should exist and be reachable or
            reside on the target Windows host.
        :param domain_netbios_name:
            The NetBIOS name for the root domain in the new forest.
            For NetBIOS names to be valid for use with this parameter they
            must be single label names of 15 characters or less, if not it
            will fail.
            If this parameter is not set, then the default is automatically
            computed from the value of the *domain_name* parameter.
        :param safe_mode_password:
            Safe mode password for the domain controller.
        :param database_path:
            The path to a directory on a fixed disk of the Windows host where
            the domain database will be created.
            If not set then the default path is ``%SYSTEMROOT%\\NTDS``.
        :param log_path:
            Specifies the fully qualified, non-UNC path to a directory on a
            fixed disk of the local computer where the log file for this
            operation is written.
            If not set then the default path is ``%SYSTEMROOT%\\NTDS``.
        :param sysvol_path:
            The path to a directory on a fixed disk of the Windows host where
            the Sysvol file will be created.
            If not set then the default path is ``%SYSTEMROOT%\\SYSVOL``.
        :param create_dns_delegation:
            Whether to create a DNS delegation that references the new DNS
            server that you install along with the domain controller.
            Valid for Active Directory-integrated DNS only.
            The default is computed automatically based on the environment.
        :param domain_mode:
            Specifies the domain functional level of the first domain in the
            creation of a new forest.
            The domain functional level cannot be lower than the forest
            functional level, but it can be higher.
            The default is automatically computed and set.
        :param forest_mode:
            Specifies the forest functional level for the new forest.
            The default forest functional level in Windows Server is typically
            the same as the version you are running.
        :param install_dns:
            Whether to install the DNS service when creating the domain
            controller.
        """  # noqa: E501
        raise AttributeError('win_domain')

    def win_domain_controller(
        self,
        *,
        dns_domain_name: str = _Unknown,
        domain_admin_user: str,
        domain_admin_password: str,
        safe_mode_password: str = _Unknown,
        local_admin_password: str = _Unknown,
        read_only: bool = False,
        site_name: str = _Unknown,
        state: Literal[
            'domain_controller',
            'member_server',
        ],
        database_path: StrPath = _Unknown,
        domain_log_path: StrPath = _Unknown,
        sysvol_path: StrPath = _Unknown,
        install_media_path: StrPath = _Unknown,
        install_dns: bool = _Unknown,
        log_path: str = _Unknown,
    ) -> WinDomainControllerResults:
        """
        Manage domain controller/member server state for a Windows host.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_domain_controller_module>`

        :param dns_domain_name:
            When ``state`` is ``domain_controller``, the DNS name of the
            domain for which the targeted Windows host should be a DC.
        :param domain_admin_user:
            Username of a domain admin for the target domain (necessary to
            promote or demote a domain controller).
        :param domain_admin_password:
            Password for the specified ``domain_admin_user``.
        :param safe_mode_password:
            Safe mode password for the domain controller (required when
            ``state`` is ``domain_controller``).
        :param local_admin_password:
            Password to be assigned to the local ``Administrator`` user
            (required when ``state`` is ``member_server``).
        :param read_only:
            Whether to install the domain controller as a read only replica
            for an existing domain.
        :param site_name:
            Specifies the name of an existing site where you can place the new
            domain controller.
            This option is required when *read_only* is ``true``.
        :param state:
            Whether the target host should be a domain controller or a member
            server.
        :param database_path:
            The path to a directory on a fixed disk of the Windows host where
            the domain database will be created..
            If not set then the default path is ``%SYSTEMROOT%\\NTDS``.
        :param domain_log_path:
            Specified the fully qualified, non-UNC path to a directory on a
            fixed disk of the local computer that will contain the domain log
            files.
        :param sysvol_path:
            The path to a directory on a fixed disk of the Windows host where
            the Sysvol folder will be created.
            If not set then the default path is ``%SYSTEMROOT%\\SYSVOL``.
        :param install_media_path:
            The path to a directory on a fixed disk of the Windows host where
            the Install From Media ``IFC`` data will be used.
            See the `Install using IFM guide
            <https://social.technet.microsoft.com/wiki/contents/articles/8630.active-directory-step-by-step-guide-to-install-an-additional-domain-controller-using-ifm.aspx>`__
            for more information.
        :param install_dns:
            Whether to install the DNS service when creating the domain
            controller.
            If not specified then the ``-InstallDns`` option is not supplied
            to ``Install-ADDSDomainController`` command, see
            `reference <https://docs.microsoft.com/en-us/powershell/module/addsdeployment/install-addsdomaincontroller>`__.
        :param log_path:
            The path to log any debug information when running the module.
            This option is deprecated and should not be used, it will be
            removed on the major release after ``2022-07-01``.
            This does not relate to the ``-LogPath`` paramter of the install
            controller cmdlet.
        """  # noqa: E501
        raise AttributeError('win_domain_controller')

    def win_domain_membership(
        self,
        *,
        dns_domain_name: str = _Unknown,
        domain_admin_user: str,
        domain_admin_password: str = _Unknown,
        hostname: str = _Unknown,
        domain_ou_path: str = _Unknown,
        state: Literal['domain', 'workgroup'] = _Unknown,
        workgroup_name: str = _Unknown,
    ) -> WinDomainMembershipResults:
        """
        Manage domain/workgroup membership for a Windows host.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_domain_membership_module>`

        :param dns_domain_name:
            When ``state`` is ``domain``, the DNS name of the domain to which
            the targeted Windows host should be joined.
        :param domain_admin_user:
            Username of a domain admin for the target domain (required to join
            or leave the domain).
        :param domain_admin_password:
            Password for the specified ``domain_admin_user``.
        :param hostname:
            The desired hostname for the Windows host.
        :param domain_ou_path:
            The desired OU path for adding the computer object.
            This is only used when adding the target host to a domain, if it
            is already a member then it is ignored.
        :param state:
            Whether the target host should be a member of a domain or
            workgroup.
        :param workgroup_name:
            When ``state`` is ``workgroup``, the name of the workgroup that
            the Windows host should be in.
        """  # noqa: E501
        raise AttributeError('win_domain_membership')

    @overload
    def win_dsc(
        self,
        *,
        resource_name: str,
        module_version: str = 'latest',
    ) -> WinDscResults: ...

    @overload
    def win_dsc(self, arg: str, /) -> WinDscResults: ...

    def win_dsc(self, *args: Any, **kwargs: Any) -> WinDscResults:
        """
        Invokes a PowerShell DSC configuration.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_dsc_module>`

        :param resource_name:
            The name of the DSC Resource to use.
            Must be accessible to PowerShell using any of the default paths.
        :param module_version:
            Can be used to configure the exact version of the DSC resource to
            be invoked.
            Useful if the target node has multiple versions installed of the
            module containing the DSC resource.
            If not specified, the module will follow standard PowerShell
            convention and use the highest version available.
        """  # noqa: E501
        raise AttributeError('win_dsc')

    def win_environment(
        self,
        *,
        state: Literal['absent', 'present'] = _Unknown,
        name: str = _Unknown,
        value: str = _Unknown,
        variables: Mapping[str, Incomplete] = _Unknown,
        level: Literal['machine', 'process', 'user'],
    ) -> WinEnvironmentResults:
        """
        Modify environment variables on windows hosts.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_environment_module>`

        :param state:
            Set to ``present`` to ensure environment variable is set.
            Set to ``absent`` to ensure it is removed.
            When using *variables*, do not set this option.
        :param name:
            The name of the environment variable. Required when *state=absent*.
        :param value:
            The value to store in the environment variable.
            Must be set when *state=present* and cannot be an empty string.
            Should be omitted for *state=absent* and *variables*.
        :param variables:
            A dictionary where multiple environment variables can be defined
            at once.
            Not valid when *state* is set. Variables with a value will be set
            (``present``) and variables with an empty value will be unset
            (``absent``).
            *level* applies to all vars defined this way.
        :param level:
            The level at which to set the environment variable.
            Use ``machine`` to set for all users.
            Use ``user`` to set for the current user that ansible is connected
            as.
            Use ``process`` to set for the current process. Probably not that
            useful.
        """  # noqa: E501
        raise AttributeError('win_environment')

    def win_feature(
        self,
        *,
        name: Sequence[str],
        state: Literal['absent', 'present'] = 'present',
        include_sub_features: bool = False,
        include_management_tools: bool = False,
        source: str = _Unknown,
    ) -> WinFeatureResults:
        """
        Installs and uninstalls Windows Features on Windows Server.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_feature_module>`

        :param name:
            Names of roles or features to install as a single feature or a
            comma-separated list of features.
            To list all available features use the PowerShell command
            ``Get-WindowsFeature``.
        :param state:
            State of the features or roles on the system.
        :param include_sub_features:
            Adds all subfeatures of the specified feature.
        :param include_management_tools:
            Adds the corresponding management tools to the specified feature.
            Not supported in Windows 2008 R2 and will be ignored.
        :param source:
            Specify a source to install the feature from.
            Not supported in Windows 2008 R2 and will be ignored.
            Can either be ``{driveletter}:\\sources\\sxs`` or
            ``\\{IP}\\share\\sources\\sxs``.
        """  # noqa: E501
        raise AttributeError('win_feature')

    def win_file(
        self,
        *,
        path: StrPath,
        state: Literal[
            'absent',
            'directory',
            'file',
            'touch',
        ] = _Unknown,
    ) -> WinFileResults:
        """
        Creates, touches or removes files or directories.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_file_module>`

        :param path:
            Path to the file being managed.
        :param state:
            If ``directory``, all immediate subdirectories will be created if
            they do not exist.
            If ``file``, the file will NOT be created if it does not exist,
            see the :meth:`win_copy` or :meth:`win_template` method if you
            want that behavior.
            If ``absent``, directories will be recursively deleted, and files
            will be removed.
            If ``touch``, an empty file will be created if the ``path`` does
            not exist, while an existing file or directory will receive
            updated file access and modification times (similar to the way
            ``touch`` works from the command line).
        """  # noqa: E501
        raise AttributeError('win_file')

    def win_find(
        self,
        *,
        age: str = _Unknown,
        age_stamp: Literal['atime', 'ctime', 'mtime'] = 'mtime',
        checksum_algorithm: Literal[
            'md5',
            'sha1',
            'sha256',
            'sha384',
            'sha512',
        ] = 'sha1',
        depth: int = _Unknown,
        file_type: Literal['directory', 'file'] = 'file',
        follow: bool = False,
        get_checksum: bool = True,
        hidden: bool = False,
        paths: Sequence[str],
        patterns: Sequence[str] = _Unknown,
        recurse: bool = False,
        size: str = _Unknown,
        use_regex: bool = False,
    ) -> WinFindResults:
        """
        Return a list of files based on specific criteria.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_find_module>`

        :param age:
            Select files or folders whose age is equal to or greater than the
            specified time.
            Use a negative age to find files equal to or less than the
            specified time.
            You can choose seconds, minutes, hours, days or weeks by
            specifying the first letter of an of those words (e.g., "2s",
            "10d", 1w").
        :param age_stamp:
            Choose the file property against which we compare ``age``.
            The default attribute we compare with is the last modification
            time.
        :param checksum_algorithm:
            Algorithm to determine the checksum of a file.
            Will throw an error if the host is unable to use specified
            algorithm.
        :param depth:
            Set the maximum number of levels to descend into.
            Setting recurse to ``false`` will override this value, which is
            effectively depth 1.
            Default depth is unlimited.
        :param file_type:
            Type of file to search for.
        :param follow:
            Set this to ``true`` to follow symlinks in the path.
            This needs to be used in conjunction with ``recurse``.
        :param get_checksum:
            Whether to return a checksum of the file in the return info
            (default sha1), use ``checksum_algorithm`` to change from the
            default.
        :param hidden:
            Set this to include hidden files or folders.
        :param paths:
            List of paths of directories to search for files or folders in.
            This can be supplied as a single path or a list of paths.
        :param patterns:
            One or more (powershell or regex) patterns to compare filenames
            with.
            The type of pattern matching is controlled by ``use_regex`` option.
            The patterns restrict the list of files or folders to be returned
            based on the filenames.
            For a file to be matched it only has to match with one pattern in
            a list provided.
        :param recurse:
            Will recursively descend into the directory looking for files or
            folders.
        :param size:
            Select files or folders whose size is equal to or greater than the
            specified size.
            Use a negative value to find files equal to or less than the
            specified size.
            You can specify the size with a suffix of the byte type i.e. kilo
            = k, mega = m...
            Size is not evaluated for symbolic links.
        :param use_regex:
            Will set patterns to run as a regex check if set to ``true``.
        """  # noqa: E501
        raise AttributeError('win_find')

    def win_get_url(
        self,
        *,
        url: str,
        dest: StrPath,
        force: bool = True,
        checksum: str = _Unknown,
        checksum_algorithm: Literal[
            'md5',
            'sha1',
            'sha256',
            'sha384',
            'sha512',
        ] = 'sha1',
        checksum_url: str = _Unknown,
        url_method: str = _Unknown,
        url_timeout: int = 30,
        follow_redirects: Literal['all', 'none', 'safe'] = 'safe',
        headers: Mapping[str, Incomplete] = _Unknown,
        http_agent: str = 'ansible-httpget',
        maximum_redirection: int = 50,
        validate_certs: bool = True,
        client_cert: str = _Unknown,
        client_cert_password: str = _Unknown,
        force_basic_auth: bool = False,
        url_username: str = _Unknown,
        url_password: str = _Unknown,
        use_default_credential: bool = False,
        use_proxy: bool = True,
        proxy_url: str = _Unknown,
        proxy_username: str = _Unknown,
        proxy_password: str = _Unknown,
        proxy_use_default_credential: bool = False,
    ) -> WinGetUrlResults:
        """
        Downloads file from HTTP, HTTPS, or FTP to node.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_get_url_module>`

        :param url:
            The full URL of a file to download.
        :param dest:
            The location to save the file at the URL.
            Be sure to include a filename and extension as appropriate.
        :param force:
            If ``true``, will download the file every time and replace the
            file if the contents change. If ``false``, will only download the
            file if it does not exist or the remote file has been modified
            more recently than the local file.
            This works by sending an http HEAD request to retrieve last
            modified time of the requested resource, so for this to work, the
            remote web server must support HEAD requests.
        :param checksum:
            If a *checksum* is passed to this parameter, the digest of the
            destination file will be calculated after it is downloaded to
            ensure its integrity and verify that the transfer completed
            successfully.
            This option cannot be set with *checksum_url*.
        :param checksum_algorithm:
            Specifies the hashing algorithm used when calculating the checksum
            of the remote and destination file.
        :param checksum_url:
            Specifies a URL that contains the checksum values for the resource
            at *url*.
            Like ``checksum``, this is used to verify the integrity of the
            remote transfer.
            This option cannot be set with *checksum*.
        :param url_method:
            The HTTP Method of the request.
        :param url_timeout:
            Specifies how long the request can be pending before it times out
            (in seconds).
            Set to ``0`` to specify an infinite timeout.
        :param follow_redirects:
            Whether or the module should follow redirects.
            ``all`` will follow all redirect.
            ``none`` will not follow any redirect.
            ``safe`` will follow only "safe" redirects, where "safe" means
            that the client is only doing a ``GET`` or ``HEAD`` on the URI to
            which it is being redirected.
            When following a redirected URL, the ``Authorization`` header and
            any credentials set will be dropped and not redirected.
        :param headers:
            Extra headers to set on the request.
            This should be a dictionary where the key is the header name and
            the value is the value for that header.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
            This is set to the ``User-Agent`` header on a HTTP request.
        :param maximum_redirection:
            Specify how many times the module will redirect a connection to an
            alternative URI before the connection fails.
            If set to ``0`` or *follow_redirects* is set to ``none``, or
            ``safe`` when not doing a ``GET`` or ``HEAD`` it prevents all
            redirection.
        :param validate_certs:
            If ``False``, SSL certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param client_cert:
            The path to the client certificate (.pfx) that is used for X509
            authentication. This path can either be the path to the ``pfx`` on
            the filesystem or the PowerShell certificate path
            ``Cert:\\CurrentUser\\My\\<thumbprint>``.
            The WinRM connection must be authenticated with ``CredSSP`` or
            ``become`` is used on the task if the certificate file is not
            password protected.
            Other authentication types can set *client_cert_password* when the
            cert is password protected.
        :param client_cert_password:
            The password for *client_cert* if the cert is password protected.
        :param force_basic_auth:
            By default the authentication header is only sent when a
            webservice responses to an initial request with a 401 status.
            Since some basic auth services do not properly send a 401, logins
            will fail.
            This option forces the sending of the Basic authentication header
            upon the original request.
        :param url_username:
            The username to use for authentication.
        :param url_password:
            The password for *url_username*.
        :param use_default_credential:
            Uses the current user's credentials when authenticating with a
            server protected with ``NTLM``, ``Kerberos``, or ``Negotiate``
            authentication.
            Sites that use ``Basic`` auth will still require explicit
            credentials through the *url_username* and *url_password* options.
            The module will only have access to the user's credentials if
            using ``become`` with a password, you are connecting with SSH
            using a password, or connecting with WinRM using ``CredSSP`` or
            ``Kerberos with delegation``.
            If not using ``become`` or a different auth method to the ones
            stated above, there will be no default credentials available and
            no authentication will occur.
        :param use_proxy:
            If ``False``, it will not use the proxy defined in IE for the
            current user.
        :param proxy_url:
            An explicit proxy to use for the request.
            By default, the request will use the IE defined proxy unless
            *use_proxy* is set to ``False``.
        :param proxy_username:
            The username to use for proxy authentication.
        :param proxy_password:
            The password for *proxy_username*.
        :param proxy_use_default_credential:
            Uses the current user's credentials when authenticating with a
            proxy host protected with ``NTLM``, ``Kerberos``, or ``Negotiate``
            authentication.
            Proxies that use ``Basic`` auth will still require explicit
            credentials through the *proxy_username* and *proxy_password*
            options.
            The module will only have access to the user's credentials if
            using ``become`` with a password, you are connecting with SSH
            using a password, or connecting with WinRM using ``CredSSP`` or
            ``Kerberos with delegation``.
            If not using ``become`` or a different auth method to the ones
            stated above, there will be no default credentials available and
            no proxy authentication will occur.
        """  # noqa: E501
        raise AttributeError('win_get_url')

    def win_group(
        self,
        *,
        name: str,
        description: str = _Unknown,
        state: Literal['absent', 'present'] = 'present',
    ) -> WinGroupResults:
        """
        Add and remove local groups.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_group_module>`

        :param name:
            Name of the group.
        :param description:
            Description of the group.
        :param state:
            Create or remove the group.
        """  # noqa: E501
        raise AttributeError('win_group')

    def win_group_membership(
        self,
        *,
        name: str,
        members: Sequence[str],
        state: Literal['absent', 'present', 'pure'] = 'present',
    ) -> WinGroupMembershipResults:
        """
        Manage Windows local group membership.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_group_membership_module>`

        :param name:
            Name of the local group to manage membership on.
        :param members:
            A list of members to ensure are present/absent from the group.
            Accepts local users as .\\username, and SERVERNAME\\username.
            Accepts domain users and groups as DOMAIN\\username and
            username@DOMAIN.
            Accepts service users as NT AUTHORITY\\username.
            Accepts all local, domain and service user types as username,
            favoring domain lookups when in a domain.
        :param state:
            Desired state of the members in the group.
            When ``state`` is ``pure``, only the members specified will exist,
            and all other existing members not specified are removed.
        """  # noqa: E501
        raise AttributeError('win_group_membership')

    def win_hostname(
        self,
        *,
        name: str,
    ) -> WinHostnameResults:
        """
        Manages local Windows computer name.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_hostname_module>`

        :param name:
            The hostname to set for the computer.
        """  # noqa: E501
        raise AttributeError('win_hostname')

    def win_optional_feature(
        self,
        *,
        name: Sequence[str],
        state: Literal['absent', 'present'] = 'present',
        include_parent: bool = False,
        source: str = _Unknown,
    ) -> WinOptionalFeatureResults:
        """
        Manage optional Windows features.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_optional_feature_module>`

        :param name:
            The name(s) of the feature to install.
            This relates to ``FeatureName`` in the Powershell cmdlet.
            To list all available features use the PowerShell command
            ``Get-WindowsOptionalFeature``.
        :param state:
            Whether to ensure the feature is absent or present on the system.
        :param include_parent:
            Whether to enable the parent feature and the parent's dependencies.
        :param source:
            Specify a source to install the feature from.
            Can either be ``{driveletter}:\\sources\\sxs`` or
            ``\\{IP}\\share\\sources\\sxs``.
        """  # noqa: E501
        raise AttributeError('win_optional_feature')

    def win_owner(
        self,
        *,
        path: StrPath,
        user: str,
        recurse: bool = False,
    ) -> WinOwnerResults:
        """
        Set owner.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_owner_module>`

        :param path:
            Path to be used for changing owner.
        :param user:
            Name to be used for changing owner.
        :param recurse:
            Indicates if the owner should be changed recursively.
        """  # noqa: E501
        raise AttributeError('win_owner')

    def win_package(
        self,
        *,
        arguments: str = _Unknown,
        chdir: StrPath = _Unknown,
        creates_path: StrPath = _Unknown,
        creates_service: str = _Unknown,
        creates_version: str = _Unknown,
        expected_return_code: Sequence[int] = _Unknown,
        log_path: StrPath = _Unknown,
        path: str = _Unknown,
        product_id: str = _Unknown,
        provider: Literal[
            'auto',
            'msi',
            'msix',
            'msp',
            'registry',
        ] = 'auto',
        state: Literal['absent', 'present'] = 'present',
        wait_for_children: bool = False,
        url_method: str = _Unknown,
        follow_redirects: Literal['all', 'none', 'safe'] = 'safe',
        headers: Mapping[str, Incomplete] = _Unknown,
        http_agent: str = 'ansible-httpget',
        maximum_redirection: int = 50,
        url_timeout: int = 30,
        validate_certs: bool = True,
        client_cert: str = _Unknown,
        client_cert_password: str = _Unknown,
        force_basic_auth: bool = False,
        url_username: str = _Unknown,
        url_password: str = _Unknown,
        use_default_credential: bool = False,
        use_proxy: bool = True,
        proxy_url: str = _Unknown,
        proxy_username: str = _Unknown,
        proxy_password: str = _Unknown,
        proxy_use_default_credential: bool = False,
    ) -> WinPackageResults:
        """
        Installs/uninstalls an installable package.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_package_module>`

        :param arguments:
            Any arguments the installer needs to either install or uninstall
            the package.
            If the package is an MSI do not supply the ``/qn``, ``/log`` or
            ``/norestart`` arguments.
            This is only used for the ``msi``, ``msp``, and ``registry``
            providers.
            Can be a list of arguments and the module will escape the
            arguments as necessary, it is recommended to use a string when
            dealing with MSI packages due to the unique escaping issues with
            msiexec.
            When using a list of arguments each item in the list is considered
            to be a single argument. As such, if an argument in the list
            contains a space then Ansible will quote this to ensure that this
            is seen by Windows as a single argument. Should this behaviour not
            be what is required, the argument should be split into two
            separate list items. See the examples section for more detail.
        :param chdir:
            Set the specified path as the current working directory before
            installing or uninstalling a package.
            This is only used for the ``msi``, ``msp``, and ``registry``
            providers.
        :param creates_path:
            Will check the existence of the path specified and use the result
            to determine whether the package is already installed.
            You can use this in conjunction with ``product_id`` and other
            ``creates_*``.
        :param creates_service:
            Will check the existing of the service specified and use the
            result to determine whether the package is already installed.
            You can use this in conjunction with ``product_id`` and other
            ``creates_*``.
        :param creates_version:
            Will check the file version property of the file at
            ``creates_path`` and use the result to determine whether the
            package is already installed.
            ``creates_path`` MUST be set and is a file.
            You can use this in conjunction with ``product_id`` and other
            ``creates_*``.
        :param expected_return_code:
            One or more return codes from the package installation that
            indicates success.
            The return codes are read as a signed integer, any values greater
            than 2147483647 need to be represented as the signed equivalent,
            i.e. ``4294967295`` is ``-1``.
            To convert a unsigned number to the signed equivalent you can run
            "[Int32]("0x{0:X}" -f ([UInt32]3221225477))".
            A return code of ``3010`` usually means that a reboot is required,
            the ``reboot_required`` return value is set if the return code is
            ``3010``.
            This is only used for the ``msi``, ``msp``, and ``registry``
            providers.
        :param log_path:
            Specifies the path to a log file that is persisted after a package
            is installed or uninstalled.
            This is only used for the ``msi`` or ``msp`` provider.
            When omitted, a temporary log file is used instead for those
            providers.
            This is only valid for MSI files, use ``arguments`` for the
            ``registry`` provider.
        :param path:
            Location of the package to be installed or uninstalled.
            This package can either be on the local file system, network share
            or a url.
            When ``state=present``, ``product_id`` is not set and the path is
            a URL, this file will always be downloaded to a temporary
            directory for idempotency checks, otherwise the file will only be
            downloaded if the package has not been installed based on the
            ``product_id`` checks.
            If ``state=present`` then this value MUST be set.
            If ``state=absent`` then this value does not need to be set if
            ``product_id`` is.
        :param product_id:
            The product id of the installed packaged.
            This is used for checking whether the product is already installed
            and getting the uninstall information if ``state=absent``.
            For msi packages, this is the ``ProductCode`` (GUID) of the
            package. This can be found under the same registry paths as the
            ``registry`` provider.
            For msp packages, this is the ``PatchCode`` (GUID) of the package
            which can found under the ``Details -> Revision number`` of the
            file's properties.
            For msix packages, this is the ``Name`` or ``PackageFullName`` of
            the package found under the ``Get-AppxPackage`` cmdlet.
            For registry (exe) packages, this is the registry key name under
            the registry paths specified in *provider*.
            This value is ignored if ``path`` is set to a local accesible file
            path and the package is not an ``exe``.
            This SHOULD be set when the package is an ``exe``, or the path is
            a url or a network share and credential delegation is not being
            used. The ``creates_*`` options can be used instead but is not
            recommended.
        :param provider:
            Set the package provider to use when searching for a package.
            The ``auto`` provider will select the proper provider if *path*
            otherwise it scans all the other providers based on the
            *product_id*.
            The ``msi`` provider scans for MSI packages installed on a machine
            wide and current user context based on the ``ProductCode`` of the
            MSI.
            The ``msix`` provider is used to install ``.appx``, ``.msix``,
            ``.appxbundle``, or ``.msixbundle`` packages. These packages are
            only installed or removed on the current use. The host must be set
            to allow sideloaded apps or in developer mode. See the examples
            for how to enable this. If a package is already installed but
            ``path`` points to an updated package, this will be installed over
            the top of the existing one.
            The ``msp`` provider scans for all MSP patches installed on a
            machine wide and current user context based on the ``PatchCode``
            of the MSP. A ``msp`` will be applied or removed on all ``msi``
            products that it applies to and is installed. If the patch is
            obsoleted or superseded then no action will be taken.
            The ``registry`` provider is used for traditional ``exe``
            installers and uses the following registry path to determine if a
            product was installed;
            ``HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall``,
            ``HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall``,
            ``HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall``,
            and
            ``HKCU:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall``.
        :param state:
            Whether to install or uninstall the package.
            The module uses *product_id* to determine whether the package is
            installed or not.
            For all providers but ``auto``, the *path* can be used for
            idempotency checks if it is locally accesible filesystem path.
        :param wait_for_children:
            The module will wait for the process it spawns to finish but any
            processes spawned in that child process as ignored.
            Set to ``true`` to wait for all descendent processes to finish
            before the module returns.
            This is useful if the install/uninstaller is just a wrapper which
            then calls the actual installer as its own child process. When
            this option is ``true`` then the module will wait for both
            processes to finish before returning.
            This should not be required for most installers and setting to
            ``true`` could result in the module not returning until the
            process it is waiting for has been stopped manually.
            Requires Windows Server 2012 or Windows 8 or newer to use.
        :param url_method:
            The HTTP Method of the request.
        :param follow_redirects:
            Whether or the module should follow redirects.
            ``all`` will follow all redirect.
            ``none`` will not follow any redirect.
            ``safe`` will follow only "safe" redirects, where "safe" means
            that the client is only doing a ``GET`` or ``HEAD`` on the URI to
            which it is being redirected.
            When following a redirected URL, the ``Authorization`` header and
            any credentials set will be dropped and not redirected.
        :param headers:
            Extra headers to set on the request.
            This should be a dictionary where the key is the header name and
            the value is the value for that header.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
            This is set to the ``User-Agent`` header on a HTTP request.
        :param maximum_redirection:
            Specify how many times the module will redirect a connection to an
            alternative URI before the connection fails.
            If set to ``0`` or *follow_redirects* is set to ``none``, or
            ``safe`` when not doing a ``GET`` or ``HEAD`` it prevents all
            redirection.
        :param url_timeout:
            Specifies how long the request can be pending before it times out
            (in seconds).
            Set to ``0`` to specify an infinite timeout.
        :param validate_certs:
            If ``False``, SSL certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param client_cert:
            The path to the client certificate (.pfx) that is used for X509
            authentication. This path can either be the path to the ``pfx`` on
            the filesystem or the PowerShell certificate path
            ``Cert:\\CurrentUser\\My\\<thumbprint>``.
            The WinRM connection must be authenticated with ``CredSSP`` or
            ``become`` is used on the task if the certificate file is not
            password protected.
            Other authentication types can set *client_cert_password* when the
            cert is password protected.
        :param client_cert_password:
            The password for *client_cert* if the cert is password protected.
        :param force_basic_auth:
            By default the authentication header is only sent when a
            webservice responses to an initial request with a 401 status.
            Since some basic auth services do not properly send a 401, logins
            will fail.
            This option forces the sending of the Basic authentication header
            upon the original request.
        :param url_username:
            The username to use for authentication.
        :param url_password:
            The password for *url_username*.
        :param use_default_credential:
            Uses the current user's credentials when authenticating with a
            server protected with ``NTLM``, ``Kerberos``, or ``Negotiate``
            authentication.
            Sites that use ``Basic`` auth will still require explicit
            credentials through the *url_username* and *url_password* options.
            The module will only have access to the user's credentials if
            using ``become`` with a password, you are connecting with SSH
            using a password, or connecting with WinRM using ``CredSSP`` or
            ``Kerberos with delegation``.
            If not using ``become`` or a different auth method to the ones
            stated above, there will be no default credentials available and
            no authentication will occur.
        :param use_proxy:
            If ``False``, it will not use the proxy defined in IE for the
            current user.
        :param proxy_url:
            An explicit proxy to use for the request.
            By default, the request will use the IE defined proxy unless
            *use_proxy* is set to ``False``.
        :param proxy_username:
            The username to use for proxy authentication.
        :param proxy_password:
            The password for *proxy_username*.
        :param proxy_use_default_credential:
            Uses the current user's credentials when authenticating with a
            proxy host protected with ``NTLM``, ``Kerberos``, or ``Negotiate``
            authentication.
            Proxies that use ``Basic`` auth will still require explicit
            credentials through the *proxy_username* and *proxy_password*
            options.
            The module will only have access to the user's credentials if
            using ``become`` with a password, you are connecting with SSH
            using a password, or connecting with WinRM using ``CredSSP`` or
            ``Kerberos with delegation``.
            If not using ``become`` or a different auth method to the ones
            stated above, there will be no default credentials available and
            no proxy authentication will occur.
        """  # noqa: E501
        raise AttributeError('win_package')

    def win_path(
        self,
        *,
        name: str = 'PATH',
        elements: Sequence[str],
        state: Literal['absent', 'present'] = 'present',
        scope: Literal['machine', 'user'] = 'machine',
    ) -> WinPathResults:
        """
        Manage Windows path environment variables.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_path_module>`

        :param name:
            Target path environment variable name.
        :param elements:
            A single path element, or a list of path elements (ie,
            directories) to add or remove.
            When multiple elements are included in the list (and ``state`` is
            ``present``), the elements are guaranteed to appear in the same
            relative order in the resultant path value.
            Variable expansions (eg, ``%VARNAME%``) are allowed, and are
            stored unexpanded in the target path element.
            Any existing path elements not mentioned in ``elements`` are
            always preserved in their current order.
            New path elements are appended to the path, and existing path
            elements may be moved closer to the end to satisfy the requested
            ordering.
            Paths are compared in a case-insensitive fashion, and trailing
            backslashes are ignored for comparison purposes. However, note
            that trailing backslashes in YAML require quotes.
        :param state:
            Whether the path elements specified in ``elements`` should be
            present or absent.
        :param scope:
            The level at which the environment variable specified by ``name``
            should be managed (either for the current user or global machine
            scope).
        """  # noqa: E501
        raise AttributeError('win_path')

    def win_ping(
        self,
        *,
        data: str = 'pong',
    ) -> WinPingResults:
        """
        A windows version of the classic ping module.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_ping_module>`

        :param data:
            Alternate data to return instead of 'pong'.
            If this parameter is set to ``crash``, the module will cause an
            exception.
        """  # noqa: E501
        raise AttributeError('win_ping')

    def win_powershell(
        self,
        *,
        arguments: Sequence[str] = _Unknown,
        chdir: str = _Unknown,
        creates: str = _Unknown,
        depth: int = 2,
        error_action: Literal[
            'silently_continue',
            'continue',
            'stop',
        ] = 'continue',
        executable: str = _Unknown,
        parameters: Mapping[str, Incomplete] = _Unknown,
        removes: str = _Unknown,
        script: str,
        sensitive_parameters: Sequence[Mapping[str, Incomplete]] = _Unknown,
    ) -> WinPowershellResults:
        """
        Run PowerShell scripts.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_powershell_module>`

        :param arguments:
            A list of arguments to pass to *executable* when running a script
            in another PowerShell process.
            These are not arguments to pass to *script*, use *parameters* for
            that purpose.
        :param chdir:
            The PowerShell location to set when starting the script.
            This can be a location in any of the PowerShell providers.
            The default location is dependent on many factors, if relative
            paths are used then set this option.
        :param creates:
            A path or path filter pattern; when the referenced path exists on
            the target host, the task will be skipped.
        :param depth:
            How deep the return values are serialized for ``result``,
            ``output``, and ``information[x].message_data``.
            This also controls the depth of the diff output set by
            ``$Ansible.Diff``.
            Setting this to a higher value can dramatically increase the
            amount of data that needs to be returned.
        :param error_action:
            The ``$ErrorActionPreference`` to set before executing *script*.
            ``silently_continue`` will ignore any errors and exceptions raised.
            ``continue`` is the default behaviour in PowerShell, errors are
            present in the *error* return value but only terminating
            exceptions will stop the script from continuing and set it as
            failed.
            ``stop`` will treat errors like exceptions, will stop the script
            and set it as failed.
        :param executable:
            A custom PowerShell executable to run the script in.
            When not defined the script will run in the current module
            PowerShell interpreter.
            Both the remote PowerShell and the one specified by *executable*
            must be running on PowerShell v5.1 or newer.
            Setting this value may change the values returned in the
            ``output`` return value depending on the underlying .NET type.
        :param parameters:
            Parameters to pass into the script as key value pairs.
            The key corresponds to the parameter name and the value is the
            value for that parameter.
        :param removes:
            A path or path filter pattern; when the referenced path **does
            not** exist on the target host, the task will be skipped.
        :param script:
            The PowerShell script to run.
        :param sensitive_parameters:
            Parameters to pass into the script as a SecureString or
            PSCredential.
            Each sensitive value will be marked with ``no_log`` to ensure they
            are not exposed in the module invocation args logs.
            The *value* suboption can be used to create a SecureString value
            while *username* and *password* can be used to create a
            PSCredential value.
        """  # noqa: E501
        raise AttributeError('win_powershell')

    def win_reboot(
        self,
        *,
        pre_reboot_delay: int | float = 2,
        post_reboot_delay: int | float = 0,
        reboot_timeout: int | float = 600,
        connect_timeout: int | float = 5,
        test_command: str = _Unknown,
        msg: str = _Unknown,
        boot_time_command: str = _Unknown,
    ) -> WinRebootResults:
        """
        Reboot a windows machine.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_reboot_module>`

        :param pre_reboot_delay:
            Seconds to wait before reboot. Passed as a parameter to the reboot
            command.
            The minimum version is ``2`` seconds and cannot be set lower.
        :param post_reboot_delay:
            Seconds to wait after the reboot command was successful before
            attempting to validate the system rebooted successfully.
            This is useful if you want wait for something to settle despite
            your connection already working.
        :param reboot_timeout:
            Maximum seconds to wait for machine to re-appear on the network
            and respond to a test command.
            This timeout is evaluated separately for both reboot verification
            and test command success so maximum clock time is actually twice
            this value.
        :param connect_timeout:
            Maximum seconds to wait for a single successful TCP connection to
            the WinRM endpoint before trying again.
        :param test_command:
            Command to expect success for to determine the machine is ready
            for management.
            By default this test command is a custom one to detect when the
            Windows Logon screen is up and ready to accept credentials. Using
            a custom command will replace this behaviour and just run the
            command specified.
        :param msg:
            Message to display to users.
        :param boot_time_command:
            Command to run that returns a unique string indicating the last
            time the system was booted.
            Setting this to a command that has different output each time it
            is run will cause the task to fail.
        """  # noqa: E501
        raise AttributeError('win_reboot')

    def win_reg_stat(
        self,
        *,
        path: str,
        name: str = _Unknown,
    ) -> WinRegStatResults:
        """
        Get information about Windows registry keys.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_reg_stat_module>`

        :param path:
            The full registry key path including the hive to search for.
        :param name:
            The registry property name to get information for, the return json
            will not include the sub_keys and properties entries for the *key*
            specified.
            Set to an empty string to target the registry key's ``(Default``)
            property value.
        """  # noqa: E501
        raise AttributeError('win_reg_stat')

    def win_regedit(
        self,
        *,
        path: str,
        name: str = _Unknown,
        data: str = _Unknown,
        type: Literal[
            'none',
            'binary',
            'dword',
            'expandstring',
            'multistring',
            'string',
            'qword',
        ] = 'string',
        state: Literal['absent', 'present'] = 'present',
        delete_key: bool = True,
        hive: StrPath = _Unknown,
    ) -> WinRegeditResults:
        """
        Add, change, or remove registry keys and values.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_regedit_module>`

        :param path:
            Name of the registry path.
            Should be in one of the following registry hives: HKCC, HKCR,
            HKCU, HKLM, HKU.
        :param name:
            Name of the registry entry in the above ``path`` parameters.
            If not provided, or empty then the '(Default)' property for the
            key will be used.
        :param data:
            Value of the registry entry ``name`` in ``path``.
            If not specified then the value for the property will be null for
            the corresponding ``type``.
            Binary and None data should be expressed in a yaml byte array or
            as comma separated hex values.
            An easy way to generate this is to run ``regedit.exe`` and use the
            *export* option to save the registry values to a file.
            In the exported file, binary value will look like
            ``hex:be,ef,be,ef``, the ``hex:`` prefix is optional.
            DWORD and QWORD values should either be represented as a decimal
            number or a hex value.
            Multistring values should be passed in as a list.
            See the examples for more details on how to format this data.
        :param type:
            The registry value data type.
        :param state:
            The state of the registry entry.
        :param delete_key:
            When ``state`` is 'absent' then this will delete the entire key.
            If ``false`` then it will only clear out the '(Default)' property
            for that key.
        :param hive:
            A path to a hive key like C:\\Users\\Default\\NTUSER.DAT to load
            in the registry.
            This hive is loaded under the HKLM:\\ANSIBLE key which can then be
            used in *name* like any other path.
            This can be used to load the default user profile registry hive or
            any other hive saved as a file.
            Using this function requires the user to have the
            ``SeRestorePrivilege`` and ``SeBackupPrivilege`` privileges
            enabled.
        """  # noqa: E501
        raise AttributeError('win_regedit')

    def win_service(
        self,
        *,
        dependencies: Sequence[str] = _Unknown,
        dependency_action: Literal['add', 'remove', 'set'] = 'set',
        desktop_interact: bool = False,
        description: str = _Unknown,
        display_name: str = _Unknown,
        error_control: Literal[
            'critical',
            'ignore',
            'normal',
            'severe',
        ] = _Unknown,
        failure_actions: Sequence[Mapping[str, Incomplete]] = _Unknown,
        failure_actions_on_non_crash_failure: bool = _Unknown,
        failure_command: str = _Unknown,
        failure_reboot_msg: str = _Unknown,
        failure_reset_period_sec: str = _Unknown,
        force_dependent_services: bool = False,
        load_order_group: str = _Unknown,
        name: str,
        path: str = _Unknown,
        password: str = _Unknown,
        pre_shutdown_timeout_ms: str = _Unknown,
        required_privileges: Sequence[str] = _Unknown,
        service_type: Literal[
            'user_own_process',
            'user_share_process',
            'win32_own_process',
            'win32_share_process',
        ] = _Unknown,
        sid_info: Literal[
            'none',
            'restricted',
            'unrestricted',
        ] = _Unknown,
        start_mode: Literal[
            'auto',
            'delayed',
            'disabled',
            'manual',
        ] = _Unknown,
        state: Literal[
            'absent',
            'paused',
            'started',
            'stopped',
            'restarted',
        ] = _Unknown,
        update_password: Literal['always', 'on_create'] = _Unknown,
        username: str = _Unknown,
    ) -> WinServiceResults:
        """
        Manage and query Windows services.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_service_module>`

        :param dependencies:
            A list of service dependencies to set for this particular service.
            This should be a list of service names and not the display name of
            the service.
            This works by ``dependency_action`` to either add/remove or set
            the services in this list.
        :param dependency_action:
            Used in conjunction with ``dependency`` to either add the
            dependencies to the existing service dependencies.
            Remove the dependencies to the existing dependencies.
            Set the dependencies to only the values in the list replacing the
            existing dependencies.
        :param desktop_interact:
            Whether to allow the service user to interact with the desktop.
            This can only be set to ``true`` when using the ``LocalSystem``
            username.
            This can only be set to ``true`` when the *service_type* is
            ``win32_own_process`` or ``win32_share_process``.
        :param description:
            The description to set for the service.
        :param display_name:
            The display name to set for the service.
        :param error_control:
            The severity of the error and action token if the service fails to
            start.
            A new service defaults to ``normal``.
            ``critical`` will log the error and restart the system with the
            last-known good configuration. If the startup fails on reboot then
            the system will fail to operate.
            ``ignore`` ignores the error.
            ``normal`` logs the error in the event log but continues.
            ``severe`` is like ``critical`` but a failure on the last-known
            good configuration reboot startup will be ignored.
        :param failure_actions:
            A list of failure actions the service controller should take on
            each failure of a service.
            The service manager will run the actions from first to last
            defined until the service starts. If *failure_reset_period_sec*
            has been exceeded then the failure actions will restart from the
            beginning.
            If all actions have been performed the the service manager will
            repeat the last service defined.
            The existing actions will be replaced with the list defined in the
            task if there is a mismatch with any of them.
            Set to an empty list to delete all failure actions on a service
            otherwise an omitted or null value preserves the existing actions
            on the service.
        :param failure_actions_on_non_crash_failure:
            Controls whether failure actions will be performed on non crash
            failures or not.
        :param failure_command:
            The command to run for a ``run_command`` failure action.
            Set to an empty string to remove the command.
        :param failure_reboot_msg:
            The message to be broadcast to users logged on the host for a
            ``reboot`` failure action.
            Set to an empty string to remove the message.
        :param failure_reset_period_sec:
            The time in seconds after which the failure action list resets
            back to the start of the list if there are no failures.
            To set this value, *failure_actions* must have at least 1 action
            present.
            Specify ``'0xFFFFFFFF'`` to set an infinite reset period.
        :param force_dependent_services:
            If ``true``, stopping or restarting a service with dependent
            services will force the dependent services to stop or restart also.
            If ``false``, stopping or restarting a service with dependent
            services may fail.
        :param load_order_group:
            The name of the load ordering group of which this service is a
            member.
            Specify an empty string to remove the existing load order group of
            a service.
        :param name:
            Name of the service.
            If only the name parameter is specified, the module will report on
            whether the service exists or not without making any changes.
        :param path:
            The path to the executable to set for the service.
        :param password:
            The password to set the service to start as.
            This and the ``username`` argument should be supplied together
            when using a local or domain account.
            If omitted then the password will continue to use the existing
            value password set.
            If specifying ``LocalSystem``, ``NetworkService``,
            ``LocalService``, the ``NT SERVICE``, or a gMSA this field can be
            omitted as those accounts have no password.
        :param pre_shutdown_timeout_ms:
            The time in which the service manager waits after sending a
            preshutdown notification to the service until it proceeds to
            continue with the other shutdown actions.
        :param required_privileges:
            A list of privileges the service must have when starting up.
            When set the service will only have the privileges specified on
            its access token.
            The *username* of the service must already have the privileges
            assigned.
            The existing privileges will be replace with the list defined in
            the task if there is a mismatch with any of them.
            Set to an empty list to remove all required privileges, otherwise
            an omitted or null value will keep the existing privileges.
            See `privilege text constants
            <https://docs.microsoft.com/en-us/windows/win32/secauthz/privilege-constants>`__
            for a list of privilege constants that can be used.
        :param service_type:
            The type of service.
            The default type of a new service is ``win32_own_process``.
            *desktop_interact* can only be set if the service type is
            ``win32_own_process`` or ``win32_share_process``.
        :param sid_info:
            Used to define the behaviour of the service's access token groups.
            ``none`` will not add any groups to the token.
            ``restricted`` will add the ``NT SERVICE\\<service name>`` SID to
            the access token's groups and restricted groups.
            ``unrestricted`` will add the ``NT SERVICE\\<service name>`` SID
            to the access token's groups.
        :param start_mode:
            Set the startup type for the service.
            A newly created service will default to ``auto``.
        :param state:
            The desired state of the service.
            ``started``/``stopped``/``absent``/``paused`` are idempotent
            actions that will not run commands unless necessary.
            ``restarted`` will always bounce the service.
            Only services that support the paused state can be paused, you can
            check the return value ``can_pause_and_continue``.
            You can only pause a service that is already started.
            A newly created service will default to ``stopped``.
        :param update_password:
            When set to ``always`` and *password* is set, the module will
            always report a change and set the password.
            Set to ``on_create`` to only set the password if the module needs
            to create the service.
            If *username* was specified and the service changed to that
            username then *password* will also be changed if specified.
            The current default is ``on_create`` but this behaviour may change
            in the future, it is best to be explicit here.
        :param username:
            The username to set the service to start as.
            Can also be set to ``LocalSystem`` or ``SYSTEM`` to use the SYSTEM
            account.
            A newly created service will default to ``LocalSystem``.
            If using a custom user account, it must have the
            ``SeServiceLogonRight`` granted to be able to start up. You can
            use the :meth:`win_user_right` method to grant this user right for
            you.
            Set to ``NT SERVICE\\service name`` to run as the NT SERVICE
            account for that service.
            This can also be a gMSA in the form ``DOMAIN\\gMSA$``.
        """  # noqa: E501
        raise AttributeError('win_service')

    def win_service_info(
        self,
        *,
        name: str = _Unknown,
    ) -> WinServiceInfoResults:
        """
        Gather information about Windows services.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_service_info_module>`

        :param name:
            If specified, this is used to match the ``name`` or
            ``display_name`` of the Windows service to get the info for.
            Can be a wildcard to match multiple services but the wildcard will
            only be matched on the ``name`` of the service and not
            ``display_name``.
            If omitted then all services will returned.
        """  # noqa: E501
        raise AttributeError('win_service_info')

    def win_share(
        self,
        *,
        name: str,
        path: StrPath,
        state: Literal['absent', 'present'] = 'present',
        description: str = _Unknown,
        list: bool = False,
        read: str = _Unknown,
        change: str = _Unknown,
        full: str = _Unknown,
        deny: str = _Unknown,
        caching_mode: Literal[
            'BranchCache',
            'Documents',
            'Manual',
            'None',
            'Programs',
            'Unknown',
        ] = 'Manual',
        scope_name: str = _Unknown,
        encrypt: bool = False,
        rule_action: Literal['set', 'add'] = 'set',
    ) -> WinShareResults:
        """
        Manage Windows shares.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_share_module>`

        :param name:
            Share name.
        :param path:
            Share directory.
        :param state:
            Specify whether to add ``present`` or remove ``absent`` the
            specified share.
        :param description:
            Share description.
        :param list:
            Specify whether to allow or deny file listing, in case user has no
            permission on share. Also known as Access-Based Enumeration.
        :param read:
            Specify user list that should get read access on share, separated
            by comma.
        :param change:
            Specify user list that should get read and write access on share,
            separated by comma.
        :param full:
            Specify user list that should get full access on share, separated
            by comma.
        :param deny:
            Specify user list that should get no access, regardless of implied
            access on share, separated by comma.
        :param caching_mode:
            Set the CachingMode for this share.
        :param scope_name:
            Specifies the scope name of the share. For use with Windows Server
            failover cluster file server resources.
            When defined, *path* must be located on a cluster shared
            volume/disk.
        :param encrypt:
            Sets whether to encrypt the traffic to the share or not.
        :param rule_action:
            Whether to add or set (replace) access control entries.
        """  # noqa: E501
        raise AttributeError('win_share')

    @overload
    def win_shell(
        self,
        *,
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        chdir: StrPath = _Unknown,
        executable: StrPath = _Unknown,
        stdin: str = _Unknown,
        no_profile: bool = False,
        output_encoding_override: str = _Unknown,
    ) -> WinShellResults: ...

    @overload
    def win_shell(self, arg: str, /) -> WinShellResults: ...

    def win_shell(self, *args: Any, **kwargs: Any) -> WinShellResults:
        """
        Execute shell commands on target hosts.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_shell_module>`

        :param creates:
            A path or path filter pattern; when the referenced path exists on
            the target host, the task will be skipped.
        :param removes:
            A path or path filter pattern; when the referenced path **does
            not** exist on the target host, the task will be skipped.
        :param chdir:
            Set the specified path as the current working directory before
            executing a command.
        :param executable:
            Change the shell used to execute the command (eg, ``cmd``).
            The target shell must accept a ``/c`` parameter followed by the
            raw command line to be executed.
        :param stdin:
            Set the stdin of the command directly to the specified value.
        :param no_profile:
            Do not load the user profile before running a command. This is
            only valid when using PowerShell as the executable.
        :param output_encoding_override:
            This option overrides the encoding of stdout/stderr output.
            You can use this option when you need to run a command which
            ignore the console's codepage.
            You should only need to use this option in very rare circumstances.
            This value can be any valid encoding ``Name`` based on the output
            of ``[System.Text.Encoding]::GetEncodings(``). See
            `reference <https://docs.microsoft.com/dotnet/api/system.text.encoding.getencodings>`__.
        """  # noqa: E501
        raise AttributeError('win_shell')

    def win_stat(
        self,
        *,
        path: StrPath,
        get_checksum: bool = True,
        get_size: bool = True,
        checksum_algorithm: Literal[
            'md5',
            'sha1',
            'sha256',
            'sha384',
            'sha512',
        ] = 'sha1',
        follow: bool = False,
    ) -> WinStatResults:
        """
        Get information about Windows files.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_stat_module>`

        :param path:
            The full path of the file/object to get the facts of; both forward
            and back slashes are accepted.
        :param get_checksum:
            Whether to return a checksum of the file (default sha1).
        :param get_size:
            Whether to return the size of a file or directory.
        :param checksum_algorithm:
            Algorithm to determine checksum of file.
            Will throw an error if the host is unable to use specified
            algorithm.
        :param follow:
            Whether to follow symlinks or junction points.
            In the case of ``path`` pointing to another link, then that will
            be followed until no more links are found.
        """  # noqa: E501
        raise AttributeError('win_stat')

    def win_tempfile(
        self,
        *,
        state: Literal['directory', 'file'] = 'file',
        path: StrPath = '%TEMP%',
        prefix: str = 'ansible.',
        suffix: str = _Unknown,
    ) -> WinTempfileResults:
        """
        Creates temporary files and directories.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_tempfile_module>`

        :param state:
            Whether to create file or directory.
        :param path:
            Location where temporary file or directory should be created.
            If path is not specified default system temporary directory
            (%TEMP%) will be used.
        :param prefix:
            Prefix of file/directory name created by module.
        :param suffix:
            Suffix of file/directory name created by module.
        """  # noqa: E501
        raise AttributeError('win_tempfile')

    def win_template(
        self,
        *,
        backup: bool = False,
        block_end_string: str = '%}',
        block_start_string: str = '{%',
        dest: StrPath,
        force: bool = True,
        lstrip_blocks: bool = False,
        newline_sequence: Literal['\\n', '\\r', '\\r\\n'] = '\\r\\n',
        output_encoding: str = 'utf-8',
        src: StrPath,
        trim_blocks: bool = True,
        variable_end_string: str = '}}',
        variable_start_string: str = '{{',
    ) -> WinTemplateResults:
        """
        Template a file out to a remote server.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_template_module>`

        :param backup:
            Determine whether a backup should be created.
            When set to ``true``, create a backup file including the timestamp
            information so you can get the original file back if you somehow
            clobbered it incorrectly.
        :param block_end_string:
            The string marking the end of a block.
        :param block_start_string:
            The string marking the beginning of a block.
        :param dest:
            Location to render the template to on the remote machine.
        :param force:
            Determine when the file is being transferred if the destination
            already exists.
            When set to ``true``, replace the remote file when contents are
            different than the source.
            When set to ``false``, the file will only be transferred if the
            destination does not exist.
        :param lstrip_blocks:
            Determine when leading spaces and tabs should be stripped.
            When set to ``true`` leading spaces and tabs are stripped from the
            start of a line to a block.
            This functionality requires Jinja 2.7 or newer.
        :param newline_sequence:
            Specify the newline sequence to use for templating files.
        :param output_encoding:
            Overrides the encoding used to write the template file defined by
            ``dest``.
            It defaults to ``utf-8``, but any encoding supported by python can
            be used.
            The source template file must always be encoded using ``utf-8``,
            for homogeneity.
        :param src:
            Path of a Jinja2 formatted template on the Ansible controller.
            This can be a relative or an absolute path.
            The file must be encoded with ``utf-8`` but *output_encoding* can
            be used to control the encoding of the output template.
        :param trim_blocks:
            Determine when newlines should be removed from blocks.
            When set to ``true`` the first newline after a block is removed
            (block, not variable tag!).
        :param variable_end_string:
            The string marking the end of a print statement.
        :param variable_start_string:
            The string marking the beginning of a print statement.
        """  # noqa: E501
        raise AttributeError('win_template')

    def win_updates(
        self,
        *,
        accept_list: Sequence[str] = _Unknown,
        category_names: Sequence[str] = _Unknown,
        skip_optional: bool = False,
        reboot: bool = False,
        reboot_timeout: int = 1200,
        server_selection: Literal[
            'default',
            'managed_server',
            'windows_update',
        ] = 'default',
        state: Literal[
            'installed',
            'searched',
            'downloaded',
        ] = 'installed',
        log_path: StrPath = _Unknown,
        reject_list: Sequence[str] = _Unknown,
        _operation: Literal['start', 'cancel', 'poll'] = 'start',
        _operation_options: Mapping[str, Incomplete] = _Unknown,
    ) -> WinUpdatesResults:
        """
        Download and install Windows updates.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_updates_module>`

        :param accept_list:
            A list of update titles or KB numbers that can be used to specify
            which updates are to be searched or installed.
            If an available update does not match one of the entries, then it
            is skipped and not installed.
            Each entry can either be the KB article or Update title as a regex
            according to the PowerShell regex rules.
            The accept list is only validated on updates that were found based
            on *category_names*. It will not force the module to install an
            update if it was not in the category specified.
        :param category_names:
            A scalar or list of categories to install updates from. To get the
            list of categories, run the module with ``state=searched``. The
            category must be the full category string, but is case insensitive.
            Some possible categories are Application, Connectors, Critical
            Updates, Definition Updates, Developer Kits, Feature Packs,
            Guidance, Security Updates, Service Packs, Tools, Update Rollups,
            Updates, and Upgrades.
            Since ``v1.7.0`` the value ``*`` will match all categories.
        :param skip_optional:
            Skip optional updates where the update has BrowseOnly set by
            Microsoft.
            Microsoft documents show that BrowseOnly means that the update
            should not be installed automatically and appear as optional
            updates.
        :param reboot:
            Ansible will automatically reboot the remote host if it is
            required and continue to install updates after the reboot.
            This can be used instead of using a :meth:`win_reboot` task after
            this one and ensures all updates for that category is installed in
            one go.
            Async does not work when ``reboot=true``.
        :param reboot_timeout:
            The time in seconds to wait until the host is back online from a
            reboot.
            This is only used if ``reboot=true`` and a reboot is required.
        :param server_selection:
            Defines the Windows Update source catalog.
            ``default`` Use the default search source. For many systems
            default is set to the Microsoft Windows Update catalog. Systems
            participating in Windows Server Update Services (WSUS) or similar
            corporate update server environments may default to those managed
            update sources instead of the Windows Update catalog.
            ``managed_server`` Use a managed server catalog. For environments
            utilizing Windows Server Update Services (WSUS) or similar
            corporate update servers, this option selects the defined
            corporate update source.
            ``windows_update`` Use the Microsoft Windows Update catalog.
        :param state:
            Controls whether found updates are downloaded or installed or
            listed.
            This module also supports Ansible check mode, which has the same
            effect as setting state=searched.
        :param log_path:
            If set, ``win_updates`` will append update progress to the
            specified file. The directory must already exist.
        :param reject_list:
            A list of update titles or KB numbers that can be used to specify
            which updates are to be excluded from installation.
            If an available update does match one of the entries, then it is
            skipped and not installed.
            Each entry can either be the KB article or Update title as a regex
            according to the PowerShell regex rules.
        :param _operation:
            Internal use only.
        :param _operation_options:
            Internal use only.
        """  # noqa: E501
        raise AttributeError('win_updates')

    def win_uri(
        self,
        *,
        url: str,
        content_type: str = _Unknown,
        body: str = _Unknown,
        dest: StrPath = _Unknown,
        creates: StrPath = _Unknown,
        removes: StrPath = _Unknown,
        return_content: bool = False,
        status_code: Sequence[int] = _Unknown,
        url_method: str = 'GET',
        url_timeout: int = 30,
        follow_redirects: Literal['all', 'none', 'safe'] = 'safe',
        headers: Mapping[str, Incomplete] = _Unknown,
        http_agent: str = 'ansible-httpget',
        maximum_redirection: int = 50,
        validate_certs: bool = True,
        client_cert: str = _Unknown,
        client_cert_password: str = _Unknown,
        force_basic_auth: bool = False,
        url_username: str = _Unknown,
        url_password: str = _Unknown,
        use_default_credential: bool = False,
        use_proxy: bool = True,
        proxy_url: str = _Unknown,
        proxy_username: str = _Unknown,
        proxy_password: str = _Unknown,
        proxy_use_default_credential: bool = False,
    ) -> WinUriResults:
        """
        Interacts with webservices.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_uri_module>`

        :param url:
            Supports FTP, HTTP or HTTPS URLs in the form of
            (ftp|http|https)://host.domain:port/path.
        :param content_type:
            Sets the "Content-Type" header.
        :param body:
            The body of the HTTP request/response to the web service.
        :param dest:
            Output the response body to a file.
        :param creates:
            A filename, when it already exists, this step will be skipped.
        :param removes:
            A filename, when it does not exist, this step will be skipped.
        :param return_content:
            Whether or not to return the body of the response as a "content"
            key in the dictionary result. If the reported Content-type is
            "application/json", then the JSON is additionally loaded into a
            key called ``json`` in the dictionary results.
        :param status_code:
            A valid, numeric, HTTP status code that signifies success of the
            request.
            Can also be comma separated list of status codes.
        :param url_method:
            The HTTP Method of the request.
        :param url_timeout:
            Specifies how long the request can be pending before it times out
            (in seconds).
            Set to ``0`` to specify an infinite timeout.
        :param follow_redirects:
            Whether or the module should follow redirects.
            ``all`` will follow all redirect.
            ``none`` will not follow any redirect.
            ``safe`` will follow only "safe" redirects, where "safe" means
            that the client is only doing a ``GET`` or ``HEAD`` on the URI to
            which it is being redirected.
            When following a redirected URL, the ``Authorization`` header and
            any credentials set will be dropped and not redirected.
        :param headers:
            Extra headers to set on the request.
            This should be a dictionary where the key is the header name and
            the value is the value for that header.
        :param http_agent:
            Header to identify as, generally appears in web server logs.
            This is set to the ``User-Agent`` header on a HTTP request.
        :param maximum_redirection:
            Specify how many times the module will redirect a connection to an
            alternative URI before the connection fails.
            If set to ``0`` or *follow_redirects* is set to ``none``, or
            ``safe`` when not doing a ``GET`` or ``HEAD`` it prevents all
            redirection.
        :param validate_certs:
            If ``False``, SSL certificates will not be validated.
            This should only be used on personally controlled sites using
            self-signed certificates.
        :param client_cert:
            The path to the client certificate (.pfx) that is used for X509
            authentication. This path can either be the path to the ``pfx`` on
            the filesystem or the PowerShell certificate path
            ``Cert:\\CurrentUser\\My\\<thumbprint>``.
            The WinRM connection must be authenticated with ``CredSSP`` or
            ``become`` is used on the task if the certificate file is not
            password protected.
            Other authentication types can set *client_cert_password* when the
            cert is password protected.
        :param client_cert_password:
            The password for *client_cert* if the cert is password protected.
        :param force_basic_auth:
            By default the authentication header is only sent when a
            webservice responses to an initial request with a 401 status.
            Since some basic auth services do not properly send a 401, logins
            will fail.
            This option forces the sending of the Basic authentication header
            upon the original request.
        :param url_username:
            The username to use for authentication.
        :param url_password:
            The password for *url_username*.
        :param use_default_credential:
            Uses the current user's credentials when authenticating with a
            server protected with ``NTLM``, ``Kerberos``, or ``Negotiate``
            authentication.
            Sites that use ``Basic`` auth will still require explicit
            credentials through the *url_username* and *url_password* options.
            The module will only have access to the user's credentials if
            using ``become`` with a password, you are connecting with SSH
            using a password, or connecting with WinRM using ``CredSSP`` or
            ``Kerberos with delegation``.
            If not using ``become`` or a different auth method to the ones
            stated above, there will be no default credentials available and
            no authentication will occur.
        :param use_proxy:
            If ``False``, it will not use the proxy defined in IE for the
            current user.
        :param proxy_url:
            An explicit proxy to use for the request.
            By default, the request will use the IE defined proxy unless
            *use_proxy* is set to ``False``.
        :param proxy_username:
            The username to use for proxy authentication.
        :param proxy_password:
            The password for *proxy_username*.
        :param proxy_use_default_credential:
            Uses the current user's credentials when authenticating with a
            proxy host protected with ``NTLM``, ``Kerberos``, or ``Negotiate``
            authentication.
            Proxies that use ``Basic`` auth will still require explicit
            credentials through the *proxy_username* and *proxy_password*
            options.
            The module will only have access to the user's credentials if
            using ``become`` with a password, you are connecting with SSH
            using a password, or connecting with WinRM using ``CredSSP`` or
            ``Kerberos with delegation``.
            If not using ``become`` or a different auth method to the ones
            stated above, there will be no default credentials available and
            no proxy authentication will occur.
        """  # noqa: E501
        raise AttributeError('win_uri')

    def win_user(
        self,
        *,
        account_disabled: bool = _Unknown,
        account_expires: str = _Unknown,
        account_locked: bool = _Unknown,
        description: str = _Unknown,
        fullname: str = _Unknown,
        groups: Sequence[str] = _Unknown,
        groups_action: Literal['add', 'replace', 'remove'] = 'replace',
        home_directory: str = _Unknown,
        login_script: str = _Unknown,
        name: str,
        password: str = _Unknown,
        password_expired: bool = _Unknown,
        password_never_expires: bool = _Unknown,
        profile: str = _Unknown,
        state: Literal['absent', 'present', 'query'] = 'present',
        update_password: Literal['always', 'on_create'] = 'always',
        user_cannot_change_password: bool = _Unknown,
    ) -> WinUserResults:
        """
        Manages local Windows user accounts.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_user_module>`

        :param account_disabled:
            ``true`` will disable the user account.
            ``false`` will clear the disabled flag.
        :param account_expires:
            Set the account expiration date for the user.
            This value should be in the format ``%Y-%m-%d`` or
            ``%Y-%m-%dT%H:%M:%S%z``. The timezone can be omitted in the long
            format and will default to UTC. The format of ``%z`` is ``±HHMM``,
            ``±HH:MM``, or ``Z`` for UTC.
            Set the value to ``never`` to remove the account expiration date.
        :param account_locked:
            Only ``false`` can be set and it will unlock the user account if
            locked.
        :param description:
            Description of the user.
        :param fullname:
            Full name of the user.
        :param groups:
            Adds or removes the user from this comma-separated list of groups,
            depending on the value of *groups_action*.
            When *groups_action* is ``replace`` and *groups* is set to the
            empty string ('groups='), the user is removed from all groups.
            Since ``ansible.windows v1.5.0`` it is possible to specify a group
            using it's security identifier.
        :param groups_action:
            If ``add``, the user is added to each group in *groups* where not
            already a member.
            If ``replace``, the user is added as a member of each group in
            *groups* and removed from any other groups.
            If ``remove``, the user is removed from each group in *groups*.
        :param home_directory:
            The designated home directory of the user.
        :param login_script:
            The login script of the user.
        :param name:
            Name of the user to create, remove or modify.
        :param password:
            Optionally set the user's password to this (plain text) value.
        :param password_expired:
            ``true`` will require the user to change their password at next
            login.
            ``false`` will clear the expired password flag.
        :param password_never_expires:
            ``true`` will set the password to never expire.
            ``false`` will allow the password to expire.
        :param profile:
            The profile path of the user.
        :param state:
            When ``absent``, removes the user account if it exists.
            When ``present``, creates or updates the user account.
            When ``query``, retrieves the user account details without making
            any changes.
        :param update_password:
            ``always`` will update passwords if they differ.
            ``on_create`` will only set the password for newly created users.
        :param user_cannot_change_password:
            ``true`` will prevent the user from changing their password.
            ``false`` will allow the user to change their password.
        """  # noqa: E501
        raise AttributeError('win_user')

    def win_user_right(
        self,
        *,
        name: str,
        users: Sequence[str],
        action: Literal['add', 'remove', 'set'] = 'set',
    ) -> WinUserRightResults:
        """
        Manage Windows User Rights.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_user_right_module>`

        :param name:
            The name of the User Right as shown by the ``Constant Name`` value
            from
            `reference <https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment>`__.
            The module will return an error if the right is invalid.
        :param users:
            A list of users or groups to add/remove on the User Right.
            These can be in the form DOMAIN\\user-group, user-group@DOMAIN.COM
            for domain users/groups.
            For local users/groups it can be in the form user-group,
            .\\user-group, SERVERNAME\\user-group where SERVERNAME is the name
            of the remote server.
            It is highly recommended to use the ``.\\`` or ``SERVERNAME\\``
            prefix to avoid any ambiguity with domain account names or errors
            trying to lookup an account on a domain controller.
            You can also add special local accounts like SYSTEM and others.
            Can be set to an empty list with *action=set* to remove all
            accounts from the right.
        :param action:
            ``add`` will add the users/groups to the existing right.
            ``remove`` will remove the users/groups from the existing right.
            ``set`` will replace the users/groups of the existing right.
        """  # noqa: E501
        raise AttributeError('win_user_right')

    def win_wait_for(
        self,
        *,
        connect_timeout: int = 5,
        delay: int = _Unknown,
        exclude_hosts: Sequence[str] = _Unknown,
        host: str = '127.0.0.1',
        path: StrPath = _Unknown,
        port: int = _Unknown,
        regex: str = _Unknown,
        sleep: int = 1,
        state: Literal[
            'absent',
            'drained',
            'present',
            'started',
            'stopped',
        ] = 'started',
        timeout: int = 300,
    ) -> WinWaitForResults:
        """
        Waits for a condition before continuing.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_wait_for_module>`

        :param connect_timeout:
            The maximum number of seconds to wait for a connection to happen
            before closing and retrying.
        :param delay:
            The number of seconds to wait before starting to poll.
        :param exclude_hosts:
            The list of hosts or IPs to ignore when looking for active TCP
            connections when ``state=drained``.
        :param host:
            A resolvable hostname or IP address to wait for.
            If ``state=drained`` then it will only check for connections on
            the IP specified, you can use '0.0.0.0' to use all host IPs.
        :param path:
            The path to a file on the filesystem to check.
            If ``state`` is present or started then it will wait until the
            file exists.
            If ``state`` is absent then it will wait until the file does not
            exist.
        :param port:
            The port number to poll on ``host``.
        :param regex:
            Can be used to match a string in a file.
            If ``state`` is present or started then it will wait until the
            regex matches.
            If ``state`` is absent then it will wait until the regex does not
            match.
            Defaults to a multiline regex.
        :param sleep:
            Number of seconds to sleep between checks.
        :param state:
            When checking a port, ``started`` will ensure the port is open,
            ``stopped`` will check that is it closed and ``drained`` will
            check for active connections.
            When checking for a file or a search string ``present`` or
            ``started`` will ensure that the file or string is present,
            ``absent`` will check that the file or search string is absent or
            removed.
        :param timeout:
            The maximum number of seconds to wait for.
        """  # noqa: E501
        raise AttributeError('win_wait_for')

    def win_whoami(self) -> WinWhoamiResults:
        """
        Get information about the current user and process.

        .. seealso::
            :ref:`ansible.windows <ansible_collections.ansible.windows.win_whoami_module>`
        """  # noqa: E501
        raise AttributeError('win_whoami')
