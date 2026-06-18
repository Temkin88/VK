import shlex
import subprocess

SSH_BASE = [
    "ssh",
    "-p", "22",
    "-o", "UserKnownHostsFile=/dev/null",
    "-o", "StrictHostKeyChecking=no",
    "-o", "ServerAliveInterval=30",
    "-o", "ServerAliveCountMax=3",
    "-J", "teledev",
]

SCP_BASE = [
    "scp",
    "-P", "22",
    "-o", "UserKnownHostsFile=/dev/null",
    "-o", "StrictHostKeyChecking=no",
    "-o", "ServerAliveInterval=30",
    "-o", "ServerAliveCountMax=3",
    "-J", "teledev",
]

def ssh_run_sh(host, user, cmd, *, check=True, capture_output=False, text=True):
    return subprocess.run(
        SSH_BASE + [f"{user}@{host}", "bash", "-lc", cmd],
        check=check,
        capture_output=capture_output,
        text=text,
    )

def ssh_run(host, user, remote_argv, *, check=True, capture_output=False, text=True, stdin=None):
    return subprocess.run(
        SSH_BASE + [f"{user}@{host}", "--"] + remote_argv,
        check=check,
        capture_output=capture_output,
        text=text,
        stdin=stdin,
    )

def ssh_run_helmwave(host, user, remote_argv, *, check=True, capture_output=False, text=True, stdin=None):
    remote_cmd = shlex.join(remote_argv)
    return subprocess.run(
        SSH_BASE + [f"{user}@{host}", "--"] + [remote_cmd],
        check=check,
        capture_output=capture_output,
        text=text,
        stdin=stdin,
    )

def scp_run(src, dst, *, check=False, capture_output=True, text=True):
    return subprocess.run(
        SCP_BASE + [src, dst],
        check=check,
        capture_output=capture_output,
        text=text
    )
