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


#
# ansible.builtin start
#


@type_check_only
class AddHostResults(RunnerResults):
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
class AssertResults(RunnerResults):
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
        Whether the asynchronous job has finished (``1``) or not (``0``).

        Returned when: always
        """
        return self.acquire(server, 'finished')

    def started(self, server: str | None = None) -> int:
        """
        Whether the asynchronous job has started (``1``) or not (``0``).

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
class BlockinfileResults(RunnerResults):
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
class DebugResults(RunnerResults):
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
class DnfResults(RunnerResults):
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
class DpkgSelectionsResults(RunnerResults):
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
class ExpectResults(RunnerResults):
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
class FailResults(RunnerResults):
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
class FetchResults(RunnerResults):
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
        Destination file/path, equal to the value passed to ``path``.

        Returned when: ``state=touch``, ``state=hard``, ``state=link``
        """
        return self.acquire(server, 'dest')

    def path(self, server: str | None = None) -> str:
        """
        Destination file/path, equal to the value passed to ``path``.

        Returned when: ``state=absent``, ``state=directory``, ``state=file``
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

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

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

        Returned when: ``state`` is ``present``
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

        Returned when: ``state`` is ``present``
        """
        return self.acquire(server, 'system')


@type_check_only
class GroupByResults(RunnerResults):
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
class HostnameResults(RunnerResults):
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
class ImportPlaybookResults(RunnerResults):
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
class ImportRoleResults(RunnerResults):
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
class ImportTasksResults(RunnerResults):
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
class IncludeResults(RunnerResults):
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
class IncludeRoleResults(RunnerResults):
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
class IncludeTasksResults(RunnerResults):
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
class IptablesResults(RunnerResults):
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
class KnownHostsResults(RunnerResults):
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
class MetaResults(RunnerResults):
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
class PackageResults(RunnerResults):
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

    def ansible_facts(self, server: str | None = None) -> Incomplete:
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
        Value provided with the ``data`` parameter.

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
class RawResults(RunnerResults):
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
class ScriptResults(RunnerResults):
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

    def ansible_facts(self, server: str | None = None) -> Incomplete:
        """
        Facts to add to ansible_facts about the services on the system.

        Returned when: always
        """
        return self.acquire(server, 'ansible_facts')


@type_check_only
class SetFactResults(RunnerResults):
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
class SetStatsResults(RunnerResults):
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
class SetupResults(RunnerResults):
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
        A dictionary with the key=value pairs returned from ``systemctl show``.

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
        A dictionary with the key=value pairs returned from ``systemctl show``.

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

    def results(self, server: str | None = None) -> Incomplete:
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

        Returned when: ``list_files`` is ``True``
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

        If ``src`` was a remote web URL, or from the local ansible controller,
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

        Returned when: ``state`` is ``present`` and the user exists
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

        Returned when: ``state`` is ``absent`` and user exists
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

        Returned when: ``groups`` is not empty and ``state`` is ``present``
        """
        return self.acquire(server, 'groups')

    def home(self, server: str | None = None) -> str:
        """
        Path to user's home directory.

        Returned when: ``state`` is ``present``
        """
        return self.acquire(server, 'home')

    def move_home(self, server: str | None = None) -> bool:
        """
        Whether or not to move an existing home directory.

        Returned when: ``state`` is ``present`` and user exists
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

        Returned when: ``state`` is ``present`` and ``password`` is not empty
        """
        return self.acquire(server, 'password')

    def remove(self, server: str | None = None) -> bool:
        """
        Whether or not to remove the user account.

        Returned when: ``state`` is ``absent`` and user exists
        """
        return self.acquire(server, 'remove')

    def shell(self, server: str | None = None) -> str:
        """
        User login shell.

        Returned when: ``state`` is ``present``
        """
        return self.acquire(server, 'shell')

    def ssh_fingerprint(self, server: str | None = None) -> str:
        """
        Fingerprint of generated SSH key.

        Returned when: ``generate_ssh_key`` is ``True``
        """
        return self.acquire(server, 'ssh_fingerprint')

    def ssh_key_file(self, server: str | None = None) -> str:
        """
        Path to generated SSH private key file.

        Returned when: ``generate_ssh_key`` is ``True``
        """
        return self.acquire(server, 'ssh_key_file')

    def ssh_public_key(self, server: str | None = None) -> str:
        """
        Generated SSH public key file.

        Returned when: ``generate_ssh_key`` is ``True``
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

        Returned when: ``system`` is passed to the module and the account does
        not exist
        """
        return self.acquire(server, 'system')

    def uid(self, server: str | None = None) -> int:
        """
        User ID of the user account.

        Returned when: ``uid`` is passed to the module
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
        `re.Match.groups <https://docs.python.org/3/library/re.html#re.Match.groups>`__.

        Returned when: always
        """  # noqa: E501
        return self.acquire(server, 'match_groups')

    def match_groupdict(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        Dictionary containing all the named subgroups of the match, keyed by
        the subgroup name, as returned by
        `re.Match.groupdict <https://docs.python.org/3/library/re.html#re.Match.groupdict>`__.

        Returned when: always
        """  # noqa: E501
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
class YumResults(RunnerResults):
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


#
# ansible.builtin end
# ansible.netcommon start
#


@type_check_only
class CliBackupResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def backup_path(self, server: str | None = None) -> str:
        """
        The full path to the backup file.

        Returned when: always
        """
        return self.acquire(server, 'backup_path')


@type_check_only
class CliCommandResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def stdout(self, server: str | None = None) -> str:
        """
        The response from the command.

        Returned when: sendonly is false
        """
        return self.acquire(server, 'stdout')

    def json(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        A dictionary representing a JSON-formatted response.

        Returned when: the device response is valid JSON
        """
        return self.acquire(server, 'json')


@type_check_only
class CliConfigResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def diff(self, server: str | None = None) -> str:
        """
        The diff generated on the device when the commands were applied.

        Returned when: *supports_onbox_diff=True* in the platform's cliconf
        plugin
        """
        return self.acquire(server, 'diff')

    def commands(self, server: str | None = None) -> list[Incomplete]:
        """
        The set of commands that will be pushed to the remote device.

        Returned when: *supports_generated_diff=True* and
        *supports_onbox_diff=False* in the platform's cliconf plugin
        """
        return self.acquire(server, 'commands')

    def backup_path(self, server: str | None = None) -> str:
        """
        The full path to the backup file.

        Returned when: backup is yes
        """
        return self.acquire(server, 'backup_path')


@type_check_only
class CliRestoreResults(RunnerResults):
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
class GrpcConfigResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def stdout(self, server: str | None = None) -> str:
        """
        The raw string containing response object received from the gRPC
        server.

        Returned when: error mesage, when failure happens. empty , when the
        operation is successful
        """
        return self.acquire(server, 'stdout')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The value of stdout split into a list.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout_lines')

    def backup_path(self, server: str | None = None) -> str:
        """
        The full path to the backup file.

        Returned when: backup is yes
        """
        return self.acquire(server, 'backup_path')

    def diff(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        If --diff option in enabled while running, the before and after
        configuration change are returned as part of before and after key.

        Returned when: diff is enabled
        """
        return self.acquire(server, 'diff')


@type_check_only
class GrpcGetResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def stdout(self, server: str | None = None) -> str:
        """
        The raw string containing configuration or state data received from
        the gRPC server.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The value of stdout split into a list.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout_lines')

    def output(self, server: str | None = None) -> list[Incomplete]:
        """
        A dictionary representing a JSON-formatted response, if the response
        is a valid json string.

        Returned when: the device response is valid JSON
        """
        return self.acquire(server, 'output')


@type_check_only
class NetGetResults(RunnerResults):
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
class NetPingResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def commands(self, server: str | None = None) -> list[Incomplete]:
        """
        Show the command sent.

        Returned when: always
        """
        return self.acquire(server, 'commands')

    def packet_loss(self, server: str | None = None) -> str:
        """
        Percentage of packets lost.

        Returned when: always
        """
        return self.acquire(server, 'packet_loss')

    def packets_rx(self, server: str | None = None) -> int:
        """
        Packets successfully received.

        Returned when: always
        """
        return self.acquire(server, 'packets_rx')

    def packets_tx(self, server: str | None = None) -> int:
        """
        Packets successfully transmitted.

        Returned when: always
        """
        return self.acquire(server, 'packets_tx')

    def rtt(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        Show RTT stats.

        Returned when: always
        """
        return self.acquire(server, 'rtt')


@type_check_only
class NetPutResults(RunnerResults):
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
class NetconfConfigResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def server_capabilities(
        self,
        server: str | None = None
    ) -> list[Incomplete]:
        """
        list of capabilities of the server.

        Returned when: success
        """
        return self.acquire(server, 'server_capabilities')

    def backup_path(self, server: str | None = None) -> str:
        """
        The full path to the backup file.

        Returned when: backup is yes
        """
        return self.acquire(server, 'backup_path')

    def diff(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        If --diff option in enabled while running, the before and after
        configuration change are returned as part of before and after key.

        Returned when: diff is enabled
        """
        return self.acquire(server, 'diff')


@type_check_only
class NetconfGetResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def stdout(self, server: str | None = None) -> str:
        """
        The raw XML string containing configuration or state data received
        from the underlying ncclient library.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The value of stdout split into a list.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout_lines')

    def output(self, server: str | None = None) -> Incomplete:
        """
        Based on the value of display option will return either the set of
        transformed XML to JSON format from the RPC response with type dict or
        pretty XML string response (human-readable) or response with namespace
        removed from XML string.

        Returned when: If the display format is selected as *json* it is
        returned as dict type and the conversion is done using jxmlease python
        library. If the display format is selected as *native* it is returned
        as dict type and the conversion is done using xmltodict python
        library. If the display format is xml or pretty it is returned as a
        string apart from low-level errors (such as action plugin).
        """
        return self.acquire(server, 'output')


@type_check_only
class NetconfRpcResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def stdout(self, server: str | None = None) -> str:
        """
        The raw XML string containing configuration or state data received
        from the underlying ncclient library.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The value of stdout split into a list.

        Returned when: always apart from low-level errors (such as action
        plugin)
        """
        return self.acquire(server, 'stdout_lines')

    def output(self, server: str | None = None) -> Incomplete:
        """
        Based on the value of display option will return either the set of
        transformed XML to JSON format from the RPC response with type dict or
        pretty XML string response (human-readable) or response with namespace
        removed from XML string.

        Returned when: the display format is selected as JSON it is returned
        as dict type, if the display format is xml or pretty pretty it is
        returned as a string apart from low-level errors (such as action
        plugin).
        """
        return self.acquire(server, 'output')


@type_check_only
class NetworkResourceResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def modules(self, server: str | None = None) -> list[Incomplete]:
        """
        List of resource modules supported for given OS.

        Returned when: only *os_name* or *ansible_network_os* is set
        """
        return self.acquire(server, 'modules')

    def before(self, server: str | None = None) -> list[Incomplete]:
        """
        The configuration as structured data prior to module invocation.

        Returned when: *state* and/or *config* option is set
        """
        return self.acquire(server, 'before')

    def after(self, server: str | None = None) -> list[Incomplete]:
        """
        The configuration as structured data after module completion.

        Returned when: changed and  when *state* and/or *config* option is set
        """
        return self.acquire(server, 'after')

    def commands(self, server: str | None = None) -> list[Incomplete]:
        """
        The set of commands pushed to the remote device.

        Returned when: *state* and/or *config* option is set
        """
        return self.acquire(server, 'commands')


@type_check_only
class RestconfConfigResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def candidate(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        The configuration sent to the device.

        Returned when: the method is not delete
        """
        return self.acquire(server, 'candidate')

    def running(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        The current running configuration on the device.

        Returned when: the method is not delete
        """
        return self.acquire(server, 'running')


@type_check_only
class RestconfGetResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def response(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        A dictionary representing a JSON-formatted response.

        Returned when: the device response is valid JSON
        """
        return self.acquire(server, 'response')


@type_check_only
class TelnetResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def output(self, server: str | None = None) -> list[Incomplete]:
        """
        output of each command is an element in this list.

        Returned when: always
        """
        return self.acquire(server, 'output')


#
# ansible.netcommon end
# ansible.posix start
#


@type_check_only
class AclResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def acl(self, server: str | None = None) -> list[Incomplete]:
        """
        Current ACL on provided path (after changes, if any).

        Returned when: success
        """
        return self.acquire(server, 'acl')


@type_check_only
class AtResults(RunnerResults):
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
class AuthorizedKeyResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def exclusive(self, server: str | None = None) -> bool:
        """
        If the key has been forced to be exclusive or not.

        Returned when: success
        """
        return self.acquire(server, 'exclusive')

    def key(self, server: str | None = None) -> str:
        """
        The key that the module was running against.

        Returned when: success
        """
        return self.acquire(server, 'key')

    def key_option(self, server: str | None = None) -> str:
        """
        Key options related to the key.

        Returned when: success
        """
        return self.acquire(server, 'key_option')

    def keyfile(self, server: str | None = None) -> str:
        """
        Path for authorized key file.

        Returned when: success
        """
        return self.acquire(server, 'keyfile')

    def manage_dir(self, server: str | None = None) -> bool:
        """
        Whether this module managed the directory of the authorized key file.

        Returned when: success
        """
        return self.acquire(server, 'manage_dir')

    def path(self, server: str | None = None) -> str:
        """
        Alternate path to the authorized_keys file.

        Returned when: success
        """
        return self.acquire(server, 'path')

    def state(self, server: str | None = None) -> str:
        """
        Whether the given key (with the given key_options) should or should
        not be in the file.

        Returned when: success
        """
        return self.acquire(server, 'state')

    def unique(self, server: str | None = None) -> bool:
        """
        Whether the key is unique.

        Returned when: success
        """
        return self.acquire(server, 'unique')

    def user(self, server: str | None = None) -> str:
        """
        The username on the remote host whose authorized_keys file will be
        modified.

        Returned when: success
        """
        return self.acquire(server, 'user')

    def validate_certs(self, server: str | None = None) -> bool:
        """
        This only applies if using a https url as the source of the keys. If
        set to ``false``, the SSL certificates will not be validated.

        Returned when: success
        """
        return self.acquire(server, 'validate_certs')


@type_check_only
class FirewalldResults(RunnerResults):
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
class FirewalldInfoResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def active_zones(self, server: str | None = None) -> bool:
        """
        Gather active zones only if turn it ``true``.

        Returned when: success
        """
        return self.acquire(server, 'active_zones')

    def collected_zones(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of collected zones.

        Returned when: success
        """
        return self.acquire(server, 'collected_zones')

    def undefined_zones(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of undefined zones in ``zones`` option.

        ``undefined_zones`` will be ignored for gathering process.

        Returned when: success
        """
        return self.acquire(server, 'undefined_zones')

    def firewalld_info(self, server: str | None = None) -> Incomplete:
        """
        Returns various information about firewalld configuration.

        Returned when: success
        """
        return self.acquire(server, 'firewalld_info')


@type_check_only
class MountResults(RunnerResults):
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
class PatchResults(RunnerResults):
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
class RhelFactsResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ansible_facts(self, server: str | None = None) -> Incomplete:
        """
        Relevant Ansible Facts.

        Returned when: needed
        """
        return self.acquire(server, 'ansible_facts')


@type_check_only
class RhelRpmOstreeResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> str:
        """
        status of rpm transaction.

        Returned when: always
        """
        return self.acquire(server, 'msg')


@type_check_only
class RpmOstreeUpgradeResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> str:
        """
        The command standard output.

        Returned when: always
        """
        return self.acquire(server, 'msg')


@type_check_only
class SebooleanResults(RunnerResults):
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
class SelinuxResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> str:
        """
        Messages that describe changes that were made.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def configfile(self, server: str | None = None) -> str:
        """
        Path to SELinux configuration file.

        Returned when: always
        """
        return self.acquire(server, 'configfile')

    def policy(self, server: str | None = None) -> str:
        """
        Name of the SELinux policy.

        Returned when: always
        """
        return self.acquire(server, 'policy')

    def state(self, server: str | None = None) -> str:
        """
        SELinux mode.

        Returned when: always
        """
        return self.acquire(server, 'state')

    def reboot_required(self, server: str | None = None) -> bool:
        """
        Whether or not an reboot is required for the changes to take effect.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class SynchronizeResults(RunnerResults):
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
class SysctlResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    The return values for this module were not documented when these types
    were auto-generated, this could mean there are no return values.

    """


#
# ansible.posix end
# ansible.utils start
#


@type_check_only
class CliParseResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def parsed(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        The structured data resulting from the parsing of the text.

        Returned when: always
        """
        return self.acquire(server, 'parsed')

    def stdout(self, server: str | None = None) -> str:
        """
        The output from the command run.

        Returned when: provided a command
        """
        return self.acquire(server, 'stdout')

    def stdout_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The output of the command run split into lines.

        Returned when: provided a command
        """
        return self.acquire(server, 'stdout_lines')


@type_check_only
class FactDiffResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def diff_text(self, server: str | None = None) -> str:
        """
        The diff in text format.

        Returned when: always
        """
        return self.acquire(server, 'diff_text')

    def diff_lines(self, server: str | None = None) -> list[Incomplete]:
        """
        The *diff_text* split into lines.

        Returned when: always
        """
        return self.acquire(server, 'diff_lines')


@type_check_only
class UpdateFactResults(RunnerResults):
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
class ValidateResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> str:
        """
        The msg indicates if the *data* is valid as per the *criteria*.

        In case data is valid return success message **all checks passed**.

        In case data is invalid return error message **Validation errors were
        found** along with more information on error is available.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def errors(self, server: str | None = None) -> list[Incomplete]:
        """
        The list of errors in *data* based on the *criteria*.

        Returned when: *data* value is invalid
        """
        return self.acquire(server, 'errors')


#
# ansible.utils end
# ansible.windows start
#


@type_check_only
class WinAclResults(RunnerResults):
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
class WinAclInheritanceResults(RunnerResults):
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
class WinCertificateStoreResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def thumbprints(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of certificate thumbprints that were touched by the module.

        Returned when: success
        """
        return self.acquire(server, 'thumbprints')


@type_check_only
class WinCommandResults(RunnerResults):
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
class WinCopyResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def backup_file(self, server: str | None = None) -> str:
        """
        Name of the backup file that was created.

        Returned when: if backup=yes
        """
        return self.acquire(server, 'backup_file')

    def dest(self, server: str | None = None) -> str:
        """
        Destination file/path.

        Returned when: changed
        """
        return self.acquire(server, 'dest')

    def src(self, server: str | None = None) -> str:
        """
        Source file used for the copy on the target machine.

        Returned when: changed
        """
        return self.acquire(server, 'src')

    def checksum(self, server: str | None = None) -> str:
        """
        SHA1 checksum of the file after running copy.

        Returned when: success, src is a file
        """
        return self.acquire(server, 'checksum')

    def size(self, server: str | None = None) -> int:
        """
        Size of the target, after execution.

        Returned when: changed, src is a file
        """
        return self.acquire(server, 'size')

    def operation(self, server: str | None = None) -> str:
        """
        Whether a single file copy took place or a folder copy.

        Returned when: success
        """
        return self.acquire(server, 'operation')

    def original_basename(self, server: str | None = None) -> str:
        """
        Basename of the copied file.

        Returned when: changed, src is a file
        """
        return self.acquire(server, 'original_basename')


@type_check_only
class WinDnsClientResults(RunnerResults):
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
class WinDomainResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def reboot_required(self, server: str | None = None) -> bool:
        """
        True if changes were made that require a reboot.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class WinDomainControllerResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def reboot_required(self, server: str | None = None) -> bool:
        """
        True if changes were made that require a reboot.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class WinDomainMembershipResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def reboot_required(self, server: str | None = None) -> bool:
        """
        True if changes were made that require a reboot.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class WinDscResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def module_version(self, server: str | None = None) -> str:
        """
        The version of the dsc resource/module used.

        Returned when: always
        """
        return self.acquire(server, 'module_version')

    def reboot_required(self, server: str | None = None) -> bool:
        """
        Flag returned from the DSC engine indicating whether or not the
        machine requires a reboot for the invoked changes to take effect.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')

    def verbose_test(self, server: str | None = None) -> list[Incomplete]:
        """
        The verbose output as a list from executing the DSC test method.

        Returned when: Ansible verbosity is -vvv or greater
        """
        return self.acquire(server, 'verbose_test')

    def verbose_set(self, server: str | None = None) -> list[Incomplete]:
        """
        The verbose output as a list from executing the DSC Set method.

        Returned when: Ansible verbosity is -vvv or greater and a change
        occurred
        """
        return self.acquire(server, 'verbose_set')


@type_check_only
class WinEnvironmentResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def before_value(self, server: str | None = None) -> str:
        """
        the value of the environment key before a change, this is null if it
        didn't exist.

        Returned when: always
        """
        return self.acquire(server, 'before_value')

    def value(self, server: str | None = None) -> str:
        """
        the value the environment key has been set to, this is null if removed.

        Returned when: always
        """
        return self.acquire(server, 'value')

    def values(  # type:ignore[override]
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        dictionary of before and after values; each key is a variable name,
        each value is another dict with ``before``, ``after``, and ``changed``
        keys.

        Returned when: always
        """
        return self.acquire(server, 'values')


@type_check_only
class WinFeatureResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def exitcode(self, server: str | None = None) -> str:
        """
        The stringified exit code from the feature installation/removal
        command.

        Returned when: always
        """
        return self.acquire(server, 'exitcode')

    def feature_result(self, server: str | None = None) -> Incomplete:
        """
        List of features that were installed or removed.

        Returned when: success
        """
        return self.acquire(server, 'feature_result')

    def reboot_required(self, server: str | None = None) -> bool:
        """
        True when the target server indicates a reboot is required (no further
        updates can be installed until after a reboot).

        This my be true even if not change had occurred as the value is
        derived from the server state.

        Returned when: success
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class WinFileResults(RunnerResults):
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
class WinFindResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def examined(self, server: str | None = None) -> int:
        """
        The number of files/folders that was checked.

        Returned when: always
        """
        return self.acquire(server, 'examined')

    def matched(self, server: str | None = None) -> int:
        """
        The number of files/folders that match the criteria.

        Returned when: always
        """
        return self.acquire(server, 'matched')

    def files(self, server: str | None = None) -> Incomplete:
        """
        Information on the files/folders that match the criteria returned as a
        list of dictionary elements for each file matched. The entries are
        sorted by the path value alphabetically.

        Returned when: success
        """
        return self.acquire(server, 'files')


@type_check_only
class WinGetUrlResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def dest(self, server: str | None = None) -> str:
        """
        destination file/path.

        Returned when: always
        """
        return self.acquire(server, 'dest')

    def checksum_dest(self, server: str | None = None) -> str:
        """
        <algorithm> checksum of the file after the download.

        Returned when: success and dest has been downloaded
        """
        return self.acquire(server, 'checksum_dest')

    def checksum_src(self, server: str | None = None) -> str:
        """
        <algorithm> checksum of the remote resource.

        Returned when: force=true or dest did not exist
        """
        return self.acquire(server, 'checksum_src')

    def elapsed(self, server: str | None = None) -> float:
        """
        The elapsed seconds between the start of poll and the end of the
        module.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')

    def size(self, server: str | None = None) -> int:
        """
        size of the dest file.

        Returned when: success
        """
        return self.acquire(server, 'size')

    def url(self, server: str | None = None) -> str:
        """
        requested url.

        Returned when: always
        """
        return self.acquire(server, 'url')

    def msg(self, server: str | None = None) -> str:
        """
        Error message, or HTTP status message from web-server.

        Returned when: always
        """
        return self.acquire(server, 'msg')

    def status_code(self, server: str | None = None) -> int:
        """
        HTTP status code.

        Returned when: always
        """
        return self.acquire(server, 'status_code')


@type_check_only
class WinGroupResults(RunnerResults):
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
class WinGroupMembershipResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def name(self, server: str | None = None) -> str:
        """
        The name of the target local group.

        Returned when: always
        """
        return self.acquire(server, 'name')

    def added(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of members added when ``state`` is ``present`` or ``pure``;
        this is empty if no members are added.

        Returned when: success and ``state`` is ``present``
        """
        return self.acquire(server, 'added')

    def removed(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of members removed when ``state`` is ``absent`` or ``pure``;
        this is empty if no members are removed.

        Returned when: success and ``state`` is ``absent``
        """
        return self.acquire(server, 'removed')

    def members(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of all local group members at completion; this is empty if the
        group contains no members.

        Returned when: success
        """
        return self.acquire(server, 'members')


@type_check_only
class WinHostnameResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def old_name(self, server: str | None = None) -> str:
        """
        The original hostname that was set before it was changed.

        Returned when: always
        """
        return self.acquire(server, 'old_name')

    def reboot_required(self, server: str | None = None) -> bool:
        """
        Whether a reboot is required to complete the hostname change.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class WinOptionalFeatureResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def reboot_required(self, server: str | None = None) -> bool:
        """
        True when the target server requires a reboot to complete updates.

        Returned when: success
        """
        return self.acquire(server, 'reboot_required')


@type_check_only
class WinOwnerResults(RunnerResults):
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
class WinPackageResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def log(self, server: str | None = None) -> str:
        """
        The contents of the MSI or MSP log.

        Returned when: installation/uninstallation failure for MSI or MSP
        packages
        """
        return self.acquire(server, 'log')

    def rc(self, server: str | None = None) -> int:
        """
        The return code of the package process.

        Returned when: change occurred
        """
        return self.acquire(server, 'rc')

    def reboot_required(self, server: str | None = None) -> bool:
        """
        Whether a reboot is required to finalise package. This is set to true
        if the executable return code is 3010.

        Returned when: always
        """
        return self.acquire(server, 'reboot_required')

    def stdout(self, server: str | None = None) -> str:
        """
        The stdout stream of the package process.

        Returned when: failure during install or uninstall
        """
        return self.acquire(server, 'stdout')

    def stderr(self, server: str | None = None) -> str:
        """
        The stderr stream of the package process.

        Returned when: failure during install or uninstall
        """
        return self.acquire(server, 'stderr')


@type_check_only
class WinPathResults(RunnerResults):
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
class WinPingResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def ping(self, server: str | None = None) -> str:
        """
        Value provided with the data parameter.

        Returned when: success
        """
        return self.acquire(server, 'ping')


@type_check_only
class WinPowershellResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def result(self, server: str | None = None) -> Incomplete:
        """
        The values that were set by ``$Ansible.Result`` in the script.

        Defaults to an empty dict but can be set to anything by the script.

        Returned when: always
        """
        return self.acquire(server, 'result')

    def host_out(self, server: str | None = None) -> str:
        """
        The strings written to the host output, typically the stdout.

        This is not the same as objects sent to the output stream in
        PowerShell.

        Returned when: always
        """
        return self.acquire(server, 'host_out')

    def host_err(self, server: str | None = None) -> str:
        """
        The strings written to the host error output, typically the stderr.

        This is not the same as objects sent to the error stream in PowerShell.

        Returned when: always
        """
        return self.acquire(server, 'host_err')

    def output(self, server: str | None = None) -> list[Incomplete]:
        """
        A list containing all the objects outputted by the script.

        The list elements can be anything as it is based on what was ran.

        Returned when: always
        """
        return self.acquire(server, 'output')

    def error(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of error records created by the script.

        Returned when: always
        """
        return self.acquire(server, 'error')

    def warning(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of warning messages created by the script.

        Warning messages only appear when ``$WarningPreference = 'Continue'``.

        Returned when: always
        """
        return self.acquire(server, 'warning')

    def verbose(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of warning messages created by the script.

        Verbose messages only appear when ``$VerbosePreference = 'Continue'``.

        Returned when: always
        """
        return self.acquire(server, 'verbose')

    def debug(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of warning messages created by the script.

        Debug messages only appear when ``$DebugPreference = 'Continue'``.

        Returned when: always
        """
        return self.acquire(server, 'debug')

    def information(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of information records created by the script.

        The information stream was only added in PowerShell v5, older versions
        will always have an empty list as a value.

        Returned when: always
        """
        return self.acquire(server, 'information')


@type_check_only
class WinRebootResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def rebooted(self, server: str | None = None) -> bool:
        """
        True if the machine was rebooted.

        Returned when: always
        """
        return self.acquire(server, 'rebooted')

    def elapsed(self, server: str | None = None) -> float:
        """
        The number of seconds that elapsed waiting for the system to be
        rebooted.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')


@type_check_only
class WinRegStatResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def changed(self, server: str | None = None) -> bool:
        """
        Whether anything was changed.

        Returned when: always
        """
        return self.acquire(server, 'changed')

    def exists(self, server: str | None = None) -> bool:
        """
        States whether the registry key/property exists.

        Returned when: success and path/property exists
        """
        return self.acquire(server, 'exists')

    def properties(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        A dictionary containing all the properties and their values in the
        registry key.

        Returned when: success, path exists and property not specified
        """
        return self.acquire(server, 'properties')

    def sub_keys(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of all the sub keys of the key specified.

        Returned when: success, path exists and property not specified
        """
        return self.acquire(server, 'sub_keys')

    def raw_value(self, server: str | None = None) -> str:
        """
        Returns the raw value of the registry property, REG_EXPAND_SZ has no
        string expansion, REG_BINARY or REG_NONE is in hex 0x format.
        REG_NONE, this value is a hex string in the 0x format.

        Returned when: success, path/property exists and property specified
        """
        return self.acquire(server, 'raw_value')

    def type(self, server: str | None = None) -> str:
        """
        The property type.

        Returned when: success, path/property exists and property specified
        """
        return self.acquire(server, 'type')

    def value(self, server: str | None = None) -> str:
        """
        The value of the property.

        Returned when: success, path/property exists and property specified
        """
        return self.acquire(server, 'value')


@type_check_only
class WinRegeditResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def data_changed(self, server: str | None = None) -> bool:
        """
        Whether this invocation changed the data in the registry value.

        Returned when: success
        """
        return self.acquire(server, 'data_changed')

    def data_type_changed(self, server: str | None = None) -> bool:
        """
        Whether this invocation changed the datatype of the registry value.

        Returned when: success
        """
        return self.acquire(server, 'data_type_changed')


@type_check_only
class WinServiceResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def exists(self, server: str | None = None) -> bool:
        """
        Whether the service exists or not.

        Returned when: success
        """
        return self.acquire(server, 'exists')

    def name(self, server: str | None = None) -> str:
        """
        The service name or id of the service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'name')

    def display_name(self, server: str | None = None) -> str:
        """
        The display name of the installed service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'display_name')

    def state(self, server: str | None = None) -> str:
        """
        The current running status of the service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'state')

    def start_mode(self, server: str | None = None) -> str:
        """
        The startup type of the service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'start_mode')

    def path(self, server: str | None = None) -> str:
        """
        The path to the service executable.

        Returned when: success and service exists
        """
        return self.acquire(server, 'path')

    def can_pause_and_continue(self, server: str | None = None) -> bool:
        """
        Whether the service can be paused and unpaused.

        Returned when: success and service exists
        """
        return self.acquire(server, 'can_pause_and_continue')

    def description(self, server: str | None = None) -> str:
        """
        The description of the service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'description')

    def username(self, server: str | None = None) -> str:
        """
        The username that runs the service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'username')

    def desktop_interact(self, server: str | None = None) -> bool:
        """
        Whether the current user is allowed to interact with the desktop.

        Returned when: success and service exists
        """
        return self.acquire(server, 'desktop_interact')

    def dependencies(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of services that is depended by this service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'dependencies')

    def depended_by(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of services that depend on this service.

        Returned when: success and service exists
        """
        return self.acquire(server, 'depended_by')


@type_check_only
class WinServiceInfoResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def exists(self, server: str | None = None) -> bool:
        """
        Whether any services were found based on the criteria specified.

        Returned when: always
        """
        return self.acquire(server, 'exists')

    def services(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of service(s) that were found based on the criteria.

        Will be an empty list if no services were found.

        Returned when: always
        """
        return self.acquire(server, 'services')


@type_check_only
class WinShareResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def actions(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of action cmdlets that were run by the module.

        Returned when: success
        """
        return self.acquire(server, 'actions')


@type_check_only
class WinShellResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def msg(self, server: str | None = None) -> bool:
        """
        Changed.

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


@type_check_only
class WinStatResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def changed(self, server: str | None = None) -> bool:
        """
        Whether anything was changed.

        Returned when: always
        """
        return self.acquire(server, 'changed')

    def stat(self, server: str | None = None) -> Incomplete:
        """
        dictionary containing all the stat data.

        Returned when: success
        """
        return self.acquire(server, 'stat')


@type_check_only
class WinTempfileResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def path(self, server: str | None = None) -> str:
        """
        The absolute path to the created file or directory.

        Returned when: success
        """
        return self.acquire(server, 'path')


@type_check_only
class WinTemplateResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def backup_file(self, server: str | None = None) -> str:
        """
        Name of the backup file that was created.

        Returned when: if backup=true
        """
        return self.acquire(server, 'backup_file')


@type_check_only
class WinUpdatesResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def reboot_required(self, server: str | None = None) -> bool:
        """
        True when the target server requires a reboot to complete updates (no
        further updates can be installed until after a reboot).

        Returned when: success
        """
        return self.acquire(server, 'reboot_required')

    def rebooted(self, server: str | None = None) -> bool:
        """
        Set to ``true`` when the target Windows host has been rebooted by
        ``win_updates``.

        Returned when: success
        """
        return self.acquire(server, 'rebooted')

    def updates(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        Updates that were found/installed.

        The key for each update is the ``id`` of the update.

        Returned when: success
        """
        return self.acquire(server, 'updates')

    def filtered_updates(
        self,
        server: str | None = None
    ) -> dict[str, Incomplete]:
        """
        Updates that were found but were filtered based on *blacklist*,
        *whitelist* or *category_names*. The return value is in the same form
        as *updates*, along with *filtered_reason*.

        Returned when: success
        """
        return self.acquire(server, 'filtered_updates')

    def found_update_count(self, server: str | None = None) -> int:
        """
        The number of updates found needing to be applied.

        Returned when: success
        """
        return self.acquire(server, 'found_update_count')

    def installed_update_count(self, server: str | None = None) -> int:
        """
        The number of updates successfully installed or downloaded.

        Returned when: success
        """
        return self.acquire(server, 'installed_update_count')

    def failed_update_count(self, server: str | None = None) -> int:
        """
        The number of updates that failed to install.

        Returned when: always
        """
        return self.acquire(server, 'failed_update_count')


@type_check_only
class WinUriResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def elapsed(self, server: str | None = None) -> float:
        """
        The number of seconds that elapsed while performing the download.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')

    def url(self, server: str | None = None) -> str:
        """
        The Target URL.

        Returned when: always
        """
        return self.acquire(server, 'url')

    def status_code(self, server: str | None = None) -> int:
        """
        The HTTP Status Code of the response.

        Returned when: success
        """
        return self.acquire(server, 'status_code')

    def status_description(self, server: str | None = None) -> str:
        """
        A summary of the status.

        Returned when: success
        """
        return self.acquire(server, 'status_description')

    def content(self, server: str | None = None) -> str:
        """
        The raw content of the HTTP response.

        Returned when: success and return_content is True
        """
        return self.acquire(server, 'content')

    def content_length(self, server: str | None = None) -> int:
        """
        The byte size of the response.

        Returned when: success
        """
        return self.acquire(server, 'content_length')

    def json(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        The json structure returned under content as a dictionary.

        Returned when: success and Content-Type is "application/json" or
        "application/javascript" and return_content is True
        """
        return self.acquire(server, 'json')


@type_check_only
class WinUserResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def account_disabled(self, server: str | None = None) -> bool:
        """
        Whether the user is disabled.

        Returned when: user exists
        """
        return self.acquire(server, 'account_disabled')

    def account_locked(self, server: str | None = None) -> bool:
        """
        Whether the user is locked.

        Returned when: user exists
        """
        return self.acquire(server, 'account_locked')

    def description(self, server: str | None = None) -> str:
        """
        The description set for the user.

        Returned when: user exists
        """
        return self.acquire(server, 'description')

    def fullname(self, server: str | None = None) -> str:
        """
        The full name set for the user.

        Returned when: user exists
        """
        return self.acquire(server, 'fullname')

    def groups(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of groups and their ADSI path the user is a member of.

        Returned when: user exists
        """
        return self.acquire(server, 'groups')

    def name(self, server: str | None = None) -> str:
        """
        The name of the user.

        Returned when: always
        """
        return self.acquire(server, 'name')

    def password_expired(self, server: str | None = None) -> bool:
        """
        Whether the password is expired.

        Returned when: user exists
        """
        return self.acquire(server, 'password_expired')

    def password_never_expires(self, server: str | None = None) -> bool:
        """
        Whether the password is set to never expire.

        Returned when: user exists
        """
        return self.acquire(server, 'password_never_expires')

    def path(self, server: str | None = None) -> str:
        """
        The ADSI path for the user.

        Returned when: user exists
        """
        return self.acquire(server, 'path')

    def sid(self, server: str | None = None) -> str:
        """
        The SID for the user.

        Returned when: user exists
        """
        return self.acquire(server, 'sid')

    def user_cannot_change_password(self, server: str | None = None) -> bool:
        """
        Whether the user can change their own password.

        Returned when: user exists
        """
        return self.acquire(server, 'user_cannot_change_password')


@type_check_only
class WinUserRightResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def added(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of accounts that were added to the right, this is empty if no
        accounts were added.

        Returned when: success
        """
        return self.acquire(server, 'added')

    def removed(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of accounts that were removed from the right, this is empty if
        no accounts were removed.

        Returned when: success
        """
        return self.acquire(server, 'removed')


@type_check_only
class WinWaitForResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def wait_attempts(self, server: str | None = None) -> int:
        """
        The number of attempts to poll the file or port before module finishes.

        Returned when: always
        """
        return self.acquire(server, 'wait_attempts')

    def elapsed(self, server: str | None = None) -> float:
        """
        The elapsed seconds between the start of poll and the end of the
        module. This includes the delay if the option is set.

        Returned when: always
        """
        return self.acquire(server, 'elapsed')


@type_check_only
class WinWhoamiResults(RunnerResults):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def authentication_package(self, server: str | None = None) -> str:
        """
        The name of the authentication package used to authenticate the user
        in the session.

        Returned when: success
        """
        return self.acquire(server, 'authentication_package')

    def user_flags(self, server: str | None = None) -> str:
        """
        The user flags for the logon session, see UserFlags in
        `reference <https://msdn.microsoft.com/en-us/library/windows/desktop/aa380128>`__.

        Returned when: success
        """  # noqa: E501
        return self.acquire(server, 'user_flags')

    def upn(self, server: str | None = None) -> str:
        """
        The user principal name of the current user.

        Returned when: success
        """
        return self.acquire(server, 'upn')

    def logon_type(self, server: str | None = None) -> str:
        """
        The logon type that identifies the logon method, see
        `reference <https://msdn.microsoft.com/en-us/library/windows/desktop/aa380129.aspx>`__.

        Returned when: success
        """  # noqa: E501
        return self.acquire(server, 'logon_type')

    def privileges(self, server: str | None = None) -> dict[str, Incomplete]:
        """
        A dictionary of privileges and their state on the logon token.

        Returned when: success
        """
        return self.acquire(server, 'privileges')

    def label(self, server: str | None = None) -> Incomplete:
        """
        The mandatory label set to the logon session.

        Returned when: success
        """
        return self.acquire(server, 'label')

    def impersonation_level(self, server: str | None = None) -> str:
        """
        The impersonation level of the token, only valid if ``token_type`` is
        ``TokenImpersonation``, see
        `reference <https://msdn.microsoft.com/en-us/library/windows/desktop/aa379572.aspx>`__.

        Returned when: success
        """  # noqa: E501
        return self.acquire(server, 'impersonation_level')

    def login_time(self, server: str | None = None) -> str:
        """
        The logon time in ISO 8601 format.

        Returned when: success
        """
        return self.acquire(server, 'login_time')

    def groups(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of groups and attributes that the user is a member of.

        Returned when: success
        """
        return self.acquire(server, 'groups')

    def account(self, server: str | None = None) -> Incomplete:
        """
        The running account SID details.

        Returned when: success
        """
        return self.acquire(server, 'account')

    def login_domain(self, server: str | None = None) -> str:
        """
        The name of the domain used to authenticate the owner of the session.

        Returned when: success
        """
        return self.acquire(server, 'login_domain')

    def rights(self, server: str | None = None) -> list[Incomplete]:
        """
        A list of logon rights assigned to the logon.

        Returned when: success and running user is a member of the local
        Administrators group
        """
        return self.acquire(server, 'rights')

    def logon_server(self, server: str | None = None) -> str:
        """
        The name of the server used to authenticate the owner of the logon
        session.

        Returned when: success
        """
        return self.acquire(server, 'logon_server')

    def logon_id(self, server: str | None = None) -> int:
        """
        The unique identifier of the logon session.

        Returned when: success
        """
        return self.acquire(server, 'logon_id')

    def dns_domain_name(self, server: str | None = None) -> str:
        """
        The DNS name of the logon session, this is an empty string if this is
        not set.

        Returned when: success
        """
        return self.acquire(server, 'dns_domain_name')

    def token_type(self, server: str | None = None) -> str:
        """
        The token type to indicate whether it is a primary or impersonation
        token.

        Returned when: success
        """
        return self.acquire(server, 'token_type')
