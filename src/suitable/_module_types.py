# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from __future__ import annotations

from suitable.runner_results import RunnerResults
from suitable.types import Incomplete
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import type_check_only
else:
    def type_check_only(f):
        return f


@type_check_only
class AptResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def cache_updated(self, server: str | None = None) -> bool:
        """
        if the cache was updated or not.

        Returned when: success, in some cases
        """
        return self.acquire(server, 'cache_updated')

    def cache_update_time(self, server: str | None = None) -> int:
        """
        time of the last cache update (0 if unknown).

        Returned when: success, in some cases
        """
        return self.acquire(server, 'cache_update_time')

    def stdout(self, server: str | None = None) -> str:
        """
        output from apt.

        Returned when: success, when needed
        """
        return self.acquire(server, 'stdout')

    def stderr(self, server: str | None = None) -> str:
        """
        error output from apt.

        Returned when: success, when needed
        """
        return self.acquire(server, 'stderr')


@type_check_only
class AptKeyResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def after(self, server: str | None = None) -> list[Incomplete]:
        """
        List of apt key ids or fingerprints after any modification.

        Returned when: on change
        """
        return self.acquire(server, 'after')

    def before(self, server: str | None = None) -> list[Incomplete]:
        """
        List of apt key ids or fingprints before any modifications.

        Returned when: always
        """
        return self.acquire(server, 'before')

    def fp(self, server: str | None = None) -> str:
        """
        Fingerprint of the key to import.

        Returned when: always
        """
        return self.acquire(server, 'fp')

    def id(self, server: str | None = None) -> str:
        """
        key id from source.

        Returned when: always
        """
        return self.acquire(server, 'id')

    def key_id(self, server: str | None = None) -> str:
        """
        calculated key id, it should be same as 'id', but can be different.

        Returned when: always
        """
        return self.acquire(server, 'key_id')

    def short_id(self, server: str | None = None) -> str:
        """
        calculated short key id.

        Returned when: always
        """
        return self.acquire(server, 'short_id')


@type_check_only
class AptRepositoryResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def repo(self, server: str | None = None) -> str:
        """
        A source string for the repository.

        Returned when: always
        """
        return self.acquire(server, 'repo')

    def sources_added(self, server: str | None = None) -> list[Incomplete]:
        """
        List of sources added.

        Returned when: success, sources were added

        .. note:: Requires ansible-core >= 2.15
        """
        return self.acquire(server, 'sources_added')

    def sources_removed(self, server: str | None = None) -> list[Incomplete]:
        """
        List of sources removed.

        Returned when: success, sources were removed

        .. note:: Requires ansible-core >= 2.15
        """
        return self.acquire(server, 'sources_removed')


@type_check_only
class AssembleResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class AsyncStatusResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ansible_job_id(self, server: str | None = None) -> str:
        """
        The asynchronous job id.

        Returned when: success
        """
        return self.acquire(server, 'ansible_job_id')

    def finished(self, server: str | None = None) -> int:
        """
        Whether the asynchronous job has finished (`1`) or not (`0`).

        Returned when: always
        """
        return self.acquire(server, 'finished')

    def started(self, server: str | None = None) -> int:
        """
        Whether the asynchronous job has started (`1`) or not (`0`).

        Returned when: always
        """
        return self.acquire(server, 'started')

    def stdout(self, server: str | None = None) -> str:
        """
        Any output returned by async_wrapper.

        Returned when: always
        """
        return self.acquire(server, 'stdout')

    def stderr(self, server: str | None = None) -> str:
        """
        Any errors returned by async_wrapper.

        Returned when: always
        """
        return self.acquire(server, 'stderr')

    def erased(self, server: str | None = None) -> str:
        """
        Path to erased job file.

        Returned when: file is erased
        """
        return self.acquire(server, 'erased')


@type_check_only
class CommandResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> bool:
        """
        changed.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def start(self, server: str | None = None) -> str:
        """
        The command execution start time.

        Returned when: always
        """
        return self.acquire(server, 'start')

    def end(self, server: str | None = None) -> str:
        """
        The command execution end time.

        Returned when: always
        """
        return self.acquire(server, 'end')

    def delta(self, server: str | None = None) -> str:
        """
        The command execution delta time.

        Returned when: always
        """
        return self.acquire(server, 'delta')

    def stdout(self, server: str | None = None) -> str:
        """
        The command standard output.

        Returned when: always
        """
        return self.acquire(server, 'stdout')

    def stderr(self, server: str | None = None) -> str:
        """
        The command standard error.

        Returned when: always
        """
        return self.acquire(server, 'stderr')

    def cmd(self, server: str | None = None) -> list[Incomplete]:
        """
        The command executed by the task.

        Returned when: always
        """
        return self.acquire(server, 'cmd')

    def rc(self, server: str | None = None) -> int:
        """
        The command return code (0 means success).

        Returned when: always
        """
        return self.acquire(server, 'rc')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The command standard output split in lines.

        Returned when: always
        """
        return self.acquire(server, 'stdout_lines')

    def stderr_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The command standard error split in lines.

        Returned when: always
        """
        return self.acquire(server, 'stderr_lines')


@type_check_only
class CopyResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def dest(self, server: str | None = None) -> str:
        """
        Destination file/path.

        Returned when: success
        """
        return self.acquire(server, 'dest')

    def src(self, server: str | None = None) -> str:
        """
        Source file used for the copy on the target machine.

        Returned when: changed
        """
        return self.acquire(server, 'src')

    def md5sum(self, server: str | None = None) -> str:
        """
        MD5 checksum of the file after running copy.

        Returned when: supported
        """
        return self.acquire(server, 'md5sum')

    def checksum(self, server: str | None = None) -> str:
        """
        SHA1 checksum of the file after running copy.

        Returned when: success
        """
        return self.acquire(server, 'checksum')

    def backup_file(self, server: str | None = None) -> str:
        """
        Name of backup file created.

        Returned when: changed and if backup=yes
        """
        return self.acquire(server, 'backup_file')

    def gid(self, server: str | None = None) -> int:
        """
        Group id of the file, after execution.

        Returned when: success
        """
        return self.acquire(server, 'gid')

    def group(self, server: str | None = None) -> str:
        """
        Group of the file, after execution.

        Returned when: success
        """
        return self.acquire(server, 'group')

    def owner(self, server: str | None = None) -> str:
        """
        Owner of the file, after execution.

        Returned when: success
        """
        return self.acquire(server, 'owner')

    def uid(self, server: str | None = None) -> int:
        """
        Owner id of the file, after execution.

        Returned when: success
        """
        return self.acquire(server, 'uid')

    def mode(self, server: str | None = None) -> str:
        """
        Permissions of the target, after execution.

        Returned when: success
        """
        return self.acquire(server, 'mode')

    def size(self, server: str | None = None) -> int:
        """
        Size of the target, after execution.

        Returned when: success
        """
        return self.acquire(server, 'size')

    def state(self, server: str | None = None) -> str:
        """
        State of the target, after execution.

        Returned when: success
        """
        return self.acquire(server, 'state')


@type_check_only
class CronResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class Deb822RepositoryResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def repo(self, server: str | None = None) -> str:
        """
        A source string for the repository.

        Returned when: always
        """
        return self.acquire(server, 'repo')

    def dest(self, server: str | None = None) -> str:
        """
        Path to the repository file.

        Returned when: always
        """
        return self.acquire(server, 'dest')

    def key_filename(self, server: str | None = None) -> str:
        """
        Path to the signed_by key file.

        Returned when: always
        """
        return self.acquire(server, 'key_filename')


@type_check_only
class DebconfResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class Dnf5Results(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> str:
        """
        Additional information about the result.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def results(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of the dnf transaction results.

        Returned when: success
        """
        return self.acquire(server, 'results')

    def failures(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of the dnf transaction failures.

        Returned when: failure
        """
        return self.acquire(server, 'failures')

    def rc(self, server: str | None = None) -> int:
        """
        For compatibility, 0 for success, 1 for failure.

        Returned when: always
        """
        return self.acquire(server, 'rc')


@type_check_only
class FileResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def dest(self, server: str | None = None) -> str:
        """
        Destination file/path, equal to the value passed to `path`.

        Returned when: `state=touch`, `state=hard`, `state=link`
        """
        return self.acquire(server, 'dest')

    def path(self, server: str | None = None) -> str:
        """
        Destination file/path, equal to the value passed to `path`.

        Returned when: `state=absent`, `state=directory`, `state=file`
        """
        return self.acquire(server, 'path')


@type_check_only
class FindResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def files(self, server: str | None = None) -> list[Incomplete]:
        """
        All matches found with the specified criteria (see stat module for
        full output of each dictionary).

        Returned when: success
        """
        return self.acquire(server, 'files')

    def matched(self, server: str | None = None) -> int:
        """
        Number of matches.

        Returned when: success
        """
        return self.acquire(server, 'matched')

    def examined(self, server: str | None = None) -> int:
        """
        Number of filesystem objects looked at.

        Returned when: success
        """
        return self.acquire(server, 'examined')

    def skipped_paths(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        skipped paths and reasons they were skipped.

        Returned when: success

        .. note:: Requires ansible-core >= 2.12
        """
        return self.acquire(server, 'skipped_paths')


@type_check_only
class GatherFactsResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    depends on the fact module called.

    """


@type_check_only
class GetUrlResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def backup_file(self, server: str | None = None) -> str:
        """
        name of backup file created after download.

        Returned when: changed and if backup=yes
        """
        return self.acquire(server, 'backup_file')

    def checksum_dest(self, server: str | None = None) -> str:
        """
        sha1 checksum of the file after copy.

        Returned when: success
        """
        return self.acquire(server, 'checksum_dest')

    def checksum_src(self, server: str | None = None) -> str:
        """
        sha1 checksum of the file.

        Returned when: success
        """
        return self.acquire(server, 'checksum_src')

    def dest(self, server: str | None = None) -> str:
        """
        destination file/path.

        Returned when: success
        """
        return self.acquire(server, 'dest')

    def elapsed(self, server: str | None = None) -> int:
        """
        The number of seconds that elapsed while performing the download.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')

    def gid(self, server: str | None = None) -> int:
        """
        group id of the file.

        Returned when: success
        """
        return self.acquire(server, 'gid')

    def group(self, server: str | None = None) -> str:
        """
        group of the file.

        Returned when: success
        """
        return self.acquire(server, 'group')

    def md5sum(self, server: str | None = None) -> str:
        """
        md5 checksum of the file after download.

        Returned when: supported
        """
        return self.acquire(server, 'md5sum')

    def mode(self, server: str | None = None) -> str:
        """
        permissions of the target.

        Returned when: success
        """
        return self.acquire(server, 'mode')

    def msg(self, server: str | None = None) -> str:
        """
        the HTTP message from the request.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def owner(self, server: str | None = None) -> str:
        """
        owner of the file.

        Returned when: success
        """
        return self.acquire(server, 'owner')

    def secontext(self, server: str | None = None) -> str:
        """
        the SELinux security context of the file.

        Returned when: success
        """
        return self.acquire(server, 'secontext')

    def size(self, server: str | None = None) -> int:
        """
        size of the target.

        Returned when: success
        """
        return self.acquire(server, 'size')

    def src(self, server: str | None = None) -> str:
        """
        source file used after download.

        Returned when: always
        """
        return self.acquire(server, 'src')

    def state(self, server: str | None = None) -> str:
        """
        state of the target.

        Returned when: success
        """
        return self.acquire(server, 'state')

    def status_code(self, server: str | None = None) -> int:
        """
        the HTTP status code from the request.

        Returned when: always
        """
        return self.acquire(server, 'status_code')

    def uid(self, server: str | None = None) -> int:
        """
        owner id of the file, after execution.

        Returned when: success
        """
        return self.acquire(server, 'uid')

    def url(self, server: str | None = None) -> str:
        """
        the actual URL used for the request.

        Returned when: always
        """
        return self.acquire(server, 'url')


@type_check_only
class GetentResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ansible_facts(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        Facts to add to ansible_facts.

        Returned when: always
        """
        return self.acquire(server, 'ansible_facts')


@type_check_only
class GitResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def after(self, server: str | None = None) -> str:
        """
        Last commit revision of the repository retrieved during the update.

        Returned when: success
        """
        return self.acquire(server, 'after')

    def before(self, server: str | None = None) -> str:
        """
        Commit revision before the repository was updated, "null" for new
        repository.

        Returned when: success
        """
        return self.acquire(server, 'before')

    def remote_url_changed(self, server: str | None = None) -> bool:
        """
        Contains True or False whether or not the remote URL was changed.

        Returned when: success
        """
        return self.acquire(server, 'remote_url_changed')

    def warnings(self, server: str | None = None) -> str:
        """
        List of warnings if requested features were not available due to a too
        old git version.

        Returned when: error
        """
        return self.acquire(server, 'warnings')

    def git_dir_now(self, server: str | None = None) -> str:
        """
        Contains the new path of .git directory if it is changed.

        Returned when: success
        """
        return self.acquire(server, 'git_dir_now')

    def git_dir_before(self, server: str | None = None) -> str:
        """
        Contains the original path of .git directory if it is changed.

        Returned when: success
        """
        return self.acquire(server, 'git_dir_before')


@type_check_only
class GroupResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def gid(self, server: str | None = None) -> int:
        """
        Group ID of the group.

        Returned when: `state` is `present`
        """
        return self.acquire(server, 'gid')

    def name(self, server: str | None = None) -> str:
        """
        Group name.

        Returned when: always
        """
        return self.acquire(server, 'name')

    def state(self, server: str | None = None) -> str:
        """
        Whether the group is present or not.

        Returned when: always
        """
        return self.acquire(server, 'state')

    def system(self, server: str | None = None) -> bool:
        """
        Whether the group is a system group or not.

        Returned when: `state` is `present`
        """
        return self.acquire(server, 'system')


@type_check_only
class ImportPlaybookResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    This module does not return anything except plays to execute.

    """


@type_check_only
class ImportRoleResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    This module does not return anything except tasks to execute.

    """


@type_check_only
class ImportTasksResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    This module does not return anything except tasks to execute.

    """


@type_check_only
class IncludeResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    This module does not return anything except plays or tasks to execute.

    """


@type_check_only
class IncludeRoleResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    This module does not return anything except tasks to execute.

    """


@type_check_only
class IncludeTasksResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    This module does not return anything except tasks to execute.

    """


@type_check_only
class IncludeVarsResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ansible_facts(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        Variables that were included and their values.

        Returned when: success
        """
        return self.acquire(server, 'ansible_facts')

    def ansible_included_var_files(
        self,
        server: str | None = None
    ) -> list[Incomplete]:
        """
        A list of files that were successfully included.

        Returned when: success
        """
        return self.acquire(server, 'ansible_included_var_files')


@type_check_only
class LineinfileResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class PackageFactsResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ansible_facts(self, server: str | None = None) -> complex:
        """
        Facts to add to ansible_facts.

        Returned when: always
        """
        return self.acquire(server, 'ansible_facts')


@type_check_only
class PauseResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def user_input(self, server: str | None = None) -> str:
        """
        User input from interactive console.

        Returned when: if no waiting time set
        """
        return self.acquire(server, 'user_input')

    def start(self, server: str | None = None) -> str:
        """
        Time when started pausing.

        Returned when: always
        """
        return self.acquire(server, 'start')

    def stop(self, server: str | None = None) -> str:
        """
        Time when ended pausing.

        Returned when: always
        """
        return self.acquire(server, 'stop')

    def delta(self, server: str | None = None) -> str:
        """
        Time paused in seconds.

        Returned when: always
        """
        return self.acquire(server, 'delta')

    def stdout(self, server: str | None = None) -> str:
        """
        Output of pause module.

        Returned when: always
        """
        return self.acquire(server, 'stdout')

    def echo(self, server: str | None = None) -> bool:
        """
        Value of echo setting.

        Returned when: always
        """
        return self.acquire(server, 'echo')


@type_check_only
class PingResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ping(self, server: str | None = None) -> str:
        """
        Value provided with the `data` parameter.

        Returned when: success
        """
        return self.acquire(server, 'ping')


@type_check_only
class PipResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def cmd(self, server: str | None = None) -> str:
        """
        pip command used by the module.

        Returned when: success
        """
        return self.acquire(server, 'cmd')

    def name(self, server: str | None = None) -> list[Incomplete]:
        """
        list of python modules targeted by pip.

        Returned when: success
        """
        return self.acquire(server, 'name')

    def requirements(self, server: str | None = None) -> str:
        """
        Path to the requirements file.

        Returned when: success, if a requirements file was provided
        """
        return self.acquire(server, 'requirements')

    def version(self, server: str | None = None) -> str:
        """
        Version of the package specified in 'name'.

        Returned when: success, if a name and version were provided
        """
        return self.acquire(server, 'version')

    def virtualenv(self, server: str | None = None) -> str:
        """
        Path to the virtualenv.

        Returned when: success, if a virtualenv path was provided
        """
        return self.acquire(server, 'virtualenv')


@type_check_only
class RebootResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def rebooted(self, server: str | None = None) -> bool:
        """
        true if the machine was rebooted.

        Returned when: always
        """
        return self.acquire(server, 'rebooted')

    def elapsed(self, server: str | None = None) -> int:
        """
        The number of seconds that elapsed waiting for the system to be
        rebooted.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')


@type_check_only
class ReplaceResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class RpmKeyResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class ServiceResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class ServiceFactsResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ansible_facts(self, server: str | None = None) -> complex:
        """
        Facts to add to ansible_facts about the services on the system.

        Returned when: always
        """
        return self.acquire(server, 'ansible_facts')


@type_check_only
class ShellResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> bool:
        """
        changed.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def start(self, server: str | None = None) -> str:
        """
        The command execution start time.

        Returned when: always
        """
        return self.acquire(server, 'start')

    def end(self, server: str | None = None) -> str:
        """
        The command execution end time.

        Returned when: always
        """
        return self.acquire(server, 'end')

    def delta(self, server: str | None = None) -> str:
        """
        The command execution delta time.

        Returned when: always
        """
        return self.acquire(server, 'delta')

    def stdout(self, server: str | None = None) -> str:
        """
        The command standard output.

        Returned when: always
        """
        return self.acquire(server, 'stdout')

    def stderr(self, server: str | None = None) -> str:
        """
        The command standard error.

        Returned when: always
        """
        return self.acquire(server, 'stderr')

    def cmd(self, server: str | None = None) -> str:
        """
        The command executed by the task.

        Returned when: always
        """
        return self.acquire(server, 'cmd')

    def rc(self, server: str | None = None) -> int:
        """
        The command return code (0 means success).

        Returned when: always
        """
        return self.acquire(server, 'rc')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The command standard output split in lines.

        Returned when: always
        """
        return self.acquire(server, 'stdout_lines')

    def stderr_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The command standard error split in lines.

        Returned when: always
        """
        return self.acquire(server, 'stderr_lines')


@type_check_only
class SlurpResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def content(self, server: str | None = None) -> str:
        """
        Encoded file content.

        Returned when: success
        """
        return self.acquire(server, 'content')

    def encoding(self, server: str | None = None) -> str:
        """
        Type of encoding used for file.

        Returned when: success
        """
        return self.acquire(server, 'encoding')

    def source(self, server: str | None = None) -> str:
        """
        Actual path of file slurped.

        Returned when: success
        """
        return self.acquire(server, 'source')


@type_check_only
class StatResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def stat(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        Dictionary containing all the stat data, some platforms might add
        additional fields.

        Returned when: success
        """
        return self.acquire(server, 'stat')


@type_check_only
class SubversionResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


@type_check_only
class SystemdResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def status(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        A dictionary with the key=value pairs returned from `systemctl show`.

        Returned when: success
        """
        return self.acquire(server, 'status')


@type_check_only
class SystemdServiceResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def status(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        A dictionary with the key=value pairs returned from `systemctl show`.

        Returned when: success
        """
        return self.acquire(server, 'status')


@type_check_only
class SysvinitResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def results(self, server: str | None = None) -> complex:
        """
        results from actions taken.

        Returned when: always
        """
        return self.acquire(server, 'results')


@type_check_only
class TempfileResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def path(self, server: str | None = None) -> str:
        """
        Path to created file or directory.

        Returned when: success
        """
        return self.acquire(server, 'path')


@type_check_only
class TemplateResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def dest(self, server: str | None = None) -> str:
        """
        Destination file/path, equal to the value passed to *dest*.

        Returned when: success
        """
        return self.acquire(server, 'dest')

    def checksum(self, server: str | None = None) -> str:
        """
        SHA1 checksum of the rendered file.

        Returned when: always
        """
        return self.acquire(server, 'checksum')

    def uid(self, server: str | None = None) -> int:
        """
        Numeric id representing the file owner.

        Returned when: success
        """
        return self.acquire(server, 'uid')

    def gid(self, server: str | None = None) -> int:
        """
        Numeric id representing the group of the owner.

        Returned when: success
        """
        return self.acquire(server, 'gid')

    def owner(self, server: str | None = None) -> str:
        """
        User name of owner.

        Returned when: success
        """
        return self.acquire(server, 'owner')

    def group(self, server: str | None = None) -> str:
        """
        Group name of owner.

        Returned when: success
        """
        return self.acquire(server, 'group')

    def md5sum(self, server: str | None = None) -> str:
        """
        MD5 checksum of the rendered file.

        Returned when: changed
        """
        return self.acquire(server, 'md5sum')

    def mode(self, server: str | None = None) -> str:
        """
        Unix permissions of the file in octal representation as a string.

        Returned when: success
        """
        return self.acquire(server, 'mode')

    def size(self, server: str | None = None) -> int:
        """
        Size of the rendered file in bytes.

        Returned when: success
        """
        return self.acquire(server, 'size')

    def src(self, server: str | None = None) -> str:
        """
        Source file used for the copy on the target machine.

        Returned when: changed
        """
        return self.acquire(server, 'src')


@type_check_only
class UnarchiveResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def dest(self, server: str | None = None) -> str:
        """
        Path to the destination directory.

        Returned when: always
        """
        return self.acquire(server, 'dest')

    def files(self, server: str | None = None) -> list[Incomplete]:
        """
        List of all the files in the archive.

        Returned when: `list_files` is `True`
        """
        return self.acquire(server, 'files')

    def gid(self, server: str | None = None) -> int:
        """
        Numerical ID of the group that owns the destination directory.

        Returned when: always
        """
        return self.acquire(server, 'gid')

    def group(self, server: str | None = None) -> str:
        """
        Name of the group that owns the destination directory.

        Returned when: always
        """
        return self.acquire(server, 'group')

    def handler(self, server: str | None = None) -> str:
        """
        Archive software handler used to extract and decompress the archive.

        Returned when: always
        """
        return self.acquire(server, 'handler')

    def mode(self, server: str | None = None) -> str:
        """
        String that represents the octal permissions of the destination
        directory.

        Returned when: always
        """
        return self.acquire(server, 'mode')

    def owner(self, server: str | None = None) -> str:
        """
        Name of the user that owns the destination directory.

        Returned when: always
        """
        return self.acquire(server, 'owner')

    def size(self, server: str | None = None) -> int:
        """
        The size of destination directory in bytes. Does not include the size
        of files or subdirectories contained within.

        Returned when: always
        """
        return self.acquire(server, 'size')

    def src(self, server: str | None = None) -> str:
        """
        The source archive's path.

        If `src` was a remote web URL, or from the local ansible controller,
        this shows the temporary location where the download was stored.

        Returned when: always
        """
        return self.acquire(server, 'src')

    def state(self, server: str | None = None) -> str:
        """
        State of the destination. Effectively always "directory".

        Returned when: always
        """
        return self.acquire(server, 'state')

    def uid(self, server: str | None = None) -> int:
        """
        Numerical ID of the user that owns the destination directory.

        Returned when: always
        """
        return self.acquire(server, 'uid')


@type_check_only
class UriResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def content(self, server: str | None = None) -> str:
        """
        The response body content.

        Returned when: status not in status_code or return_content is true
        """
        return self.acquire(server, 'content')

    def cookies(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        The cookie values placed in cookie jar.

        Returned when: on success
        """
        return self.acquire(server, 'cookies')

    def cookies_string(self, server: str | None = None) -> str:
        """
        The value for future request Cookie headers.

        Returned when: on success
        """
        return self.acquire(server, 'cookies_string')

    def elapsed(self, server: str | None = None) -> int:
        """
        The number of seconds that elapsed while performing the download.

        Returned when: on success
        """
        return self.acquire(server, 'elapsed')

    def msg(self, server: str | None = None) -> str:
        """
        The HTTP message from the request.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def path(self, server: str | None = None) -> str:
        """
        destination file/path.

        Returned when: dest is defined
        """
        return self.acquire(server, 'path')

    def redirected(self, server: str | None = None) -> bool:
        """
        Whether the request was redirected.

        Returned when: on success
        """
        return self.acquire(server, 'redirected')

    def status(self, server: str | None = None) -> int:
        """
        The HTTP status code from the request.

        Returned when: always
        """
        return self.acquire(server, 'status')

    def url(self, server: str | None = None) -> str:
        """
        The actual URL used for the request.

        Returned when: always
        """
        return self.acquire(server, 'url')


@type_check_only
class UserResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def append(self, server: str | None = None) -> bool:
        """
        Whether or not to append the user to groups.

        Returned when: `state` is `present` and the user exists
        """
        return self.acquire(server, 'append')

    def comment(self, server: str | None = None) -> str:
        """
        Comment section from passwd file, usually the user name.

        Returned when: user exists
        """
        return self.acquire(server, 'comment')

    def create_home(self, server: str | None = None) -> bool:
        """
        Whether or not to create the home directory.

        Returned when: user does not exist and not check mode
        """
        return self.acquire(server, 'create_home')

    def force(self, server: str | None = None) -> bool:
        """
        Whether or not a user account was forcibly deleted.

        Returned when: `state` is `absent` and user exists
        """
        return self.acquire(server, 'force')

    def group(self, server: str | None = None) -> int:
        """
        Primary user group ID.

        Returned when: user exists
        """
        return self.acquire(server, 'group')

    def groups(self, server: str | None = None) -> str:
        """
        List of groups of which the user is a member.

        Returned when: `groups` is not empty and `state` is `present`
        """
        return self.acquire(server, 'groups')

    def home(self, server: str | None = None) -> str:
        """
        Path to user's home directory.

        Returned when: `state` is `present`
        """
        return self.acquire(server, 'home')

    def move_home(self, server: str | None = None) -> bool:
        """
        Whether or not to move an existing home directory.

        Returned when: `state` is `present` and user exists
        """
        return self.acquire(server, 'move_home')

    def name(self, server: str | None = None) -> str:
        """
        User account name.

        Returned when: always
        """
        return self.acquire(server, 'name')

    def password(self, server: str | None = None) -> str:
        """
        Masked value of the password.

        Returned when: `state` is `present` and `password` is not empty
        """
        return self.acquire(server, 'password')

    def remove(self, server: str | None = None) -> bool:
        """
        Whether or not to remove the user account.

        Returned when: `state` is `absent` and user exists
        """
        return self.acquire(server, 'remove')

    def shell(self, server: str | None = None) -> str:
        """
        User login shell.

        Returned when: `state` is `present`
        """
        return self.acquire(server, 'shell')

    def ssh_fingerprint(self, server: str | None = None) -> str:
        """
        Fingerprint of generated SSH key.

        Returned when: `generate_ssh_key` is `True`
        """
        return self.acquire(server, 'ssh_fingerprint')

    def ssh_key_file(self, server: str | None = None) -> str:
        """
        Path to generated SSH private key file.

        Returned when: `generate_ssh_key` is `True`
        """
        return self.acquire(server, 'ssh_key_file')

    def ssh_public_key(self, server: str | None = None) -> str:
        """
        Generated SSH public key file.

        Returned when: `generate_ssh_key` is `True`
        """
        return self.acquire(server, 'ssh_public_key')

    def stderr(self, server: str | None = None) -> str:
        """
        Standard error from running commands.

        Returned when: stderr is returned by a command that is run
        """
        return self.acquire(server, 'stderr')

    def stdout(self, server: str | None = None) -> str:
        """
        Standard output from running commands.

        Returned when: standard output is returned by the command that is run
        """
        return self.acquire(server, 'stdout')

    def system(self, server: str | None = None) -> bool:
        """
        Whether or not the account is a system account.

        Returned when: `system` is passed to the module and the account does
        not exist
        """
        return self.acquire(server, 'system')

    def uid(self, server: str | None = None) -> int:
        """
        User ID of the user account.

        Returned when: `uid` is passed to the module
        """
        return self.acquire(server, 'uid')


@type_check_only
class ValidateArgumentSpecResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def argument_errors(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of arg validation errors.

        Returned when: failure
        """
        return self.acquire(server, 'argument_errors')

    def argument_spec_data(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        A dict of the data from the 'argument_spec' arg.

        Returned when: failure
        """
        return self.acquire(server, 'argument_spec_data')

    def validate_args_context(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        A dict of info about where validate_args_spec was used.

        Returned when: always
        """
        return self.acquire(server, 'validate_args_context')


@type_check_only
class WaitForResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def elapsed(self, server: str | None = None) -> int:
        """
        The number of seconds that elapsed while waiting.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')

    def match_groups(self, server: str | None = None) -> list[Incomplete]:
        """
        Tuple containing all the subgroups of the match as returned by
        `re.Match.groups
        <https://docs.python.org/3/library/re.html#re.Match.groups>`__.

        Returned when: always
        """
        return self.acquire(server, 'match_groups')

    def match_groupdict(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        Dictionary containing all the named subgroups of the match, keyed by
        the subgroup name, as returned by `re.Match.groupdict
        <https://docs.python.org/3/library/re.html#re.Match.groupdict>`__.

        Returned when: always
        """
        return self.acquire(server, 'match_groupdict')


@type_check_only
class WaitForConnectionResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def elapsed(self, server: str | None = None) -> float:
        """
        The number of seconds that elapsed waiting for the connection to
        appear.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')


@type_check_only
class YumRepositoryResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def repo(self, server: str | None = None) -> str:
        """
        repository name.

        Returned when: success
        """
        return self.acquire(server, 'repo')

    def state(self, server: str | None = None) -> str:
        """
        state of the target, after execution.

        Returned when: success
        """
        return self.acquire(server, 'state')
