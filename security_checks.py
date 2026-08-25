import re
from typing import List, Dict, Any


class SecurityChecks:
    def __init__(self):
        self.credential_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'passwd\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'api_key\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
        ]
        self.weak_crypto_patterns = [
            r'\bmd5\b', r'\bsha1\b',
            r'hashlib\.md5', r'hashlib\.sha1',
        ]
        self.cmd_injection_patterns = [
            r'os\.system\s*\(',
            r'subprocess\.call\s*\(.*shell\s*=\s*True',
            r'subprocess\.Popen\s*\(.*shell\s*=\s*True',
            r'eval\s*\(', r'exec\s*\(',
        ]
        self.path_traversal_patterns = [
            r'\.\./\.\.', r'open\s*\(\s*request',
        ]
        self.deserialization_patterns = [
            r'pickle\.loads', r'pickle\.load',
            r'yaml\.load\s*\(', r'marshal\.loads',
        ]

    def _find(self, patterns, content, filename, type_, severity):
        findings = []
        for p in patterns:
            for m in re.finditer(p, content, re.IGNORECASE):
                ln = content[:m.start()].count('\n') + 1
                findings.append({
                    'type': type_, 'severity': severity,
                    'file': filename, 'line': ln,
                    'detail': m.group()[:80]
                })
        return findings

    def check_hardcoded_credentials(self, c, f):
        return self._find(self.credential_patterns, c, f, 'Hardcoded Credential', 'HIGH')

    def check_weak_crypto(self, c, f):
        return self._find(self.weak_crypto_patterns, c, f, 'Weak Cryptography', 'MEDIUM')

    def check_command_injection(self, c, f):
        return self._find(self.cmd_injection_patterns, c, f, 'Command Injection Risk', 'HIGH')

    def check_path_traversal(self, c, f):
        return self._find(self.path_traversal_patterns, c, f, 'Path Traversal', 'MEDIUM')

    def check_insecure_deserialization(self, c, f):
        return self._find(self.deserialization_patterns, c, f, 'Insecure Deserialization', 'HIGH')

    def run_all_checks(self, c, f):
        results = []
        for fn in [self.check_hardcoded_credentials, self.check_weak_crypto,
                   self.check_command_injection, self.check_path_traversal,
                   self.check_insecure_deserialization]:
            results.extend(fn(c, f))
        return results
