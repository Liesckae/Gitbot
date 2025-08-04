import subprocess
import logging
from pathlib import Path

class Cmmand:
    def __init__(self,repo_path="."):
        self.repo_path = Path(repo_path).resolve()
        return 0
    
    def _run_git(self,args):
        try:
            result = subprocess.run(
                ["git"] + args,
                cwd=self.repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode != 0:
                raise Exception(result.stderr.strip)
            return result.stdout.strip()
        except Exception as e:
            logging.error(f"Git command failed:{args} -> {str(e)}")
            return None

    def _get_branch(self):
        return self._run_git(["rev-parse","--abbrev-rev","HEAD"])
    
    def _get_status(self):
        return self._run_git(["status","--short"])
    
    def execute(self):
        return self._run_git(["log", "-1", "--pretty=format:%h %s (%cr) by %an"])