"""
Test: VS Code and Terminal Warm-Up

Validates that students completed the hands-on practice exercise:
- practice.yml file exists in the challenge directory
- practice.yml is valid YAML
- practice.yml contains the required project and tools structure
- project section has the required keys (name, version)
- an author key has been added (Step 4 of the exercise)
- tools list contains the three required entries (dbt, duckdb, vscode)
"""

import pytest
import yaml
from pathlib import Path


@pytest.fixture
def challenge_dir():
    """Get the challenge root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def practice_file(challenge_dir):
    """Get the practice.yml file path, asserting it exists."""
    path = challenge_dir / "practice.yml"
    assert path.exists(), (
        "❌ practice.yml not found in the challenge directory.\n"
        "   Did you complete Step 1 of the Hands-On Practice section?\n"
        "   Create the file with: touch practice.yml\n"
        "   Then open and fill it in VS Code: code practice.yml"
    )
    return path


@pytest.fixture
def practice_content(practice_file):
    """Parse practice.yml and return the content as a dict."""
    with open(practice_file, "r") as f:
        raw = f.read()

    assert raw.strip(), (
        "❌ practice.yml exists but is empty.\n"
        "   Did you complete Step 2 of the Hands-On Practice section?\n"
        "   Open the file in VS Code and add the required YAML content."
    )

    try:
        content = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        pytest.fail(
            f"❌ practice.yml has a YAML syntax error:\n"
            f"   {str(e)}\n"
            f"   Common causes:\n"
            f"   - Using tabs instead of spaces for indentation\n"
            f"   - Missing space after a colon (e.g. 'name:value' should be 'name: value')\n"
            f"   - Inconsistent indentation — use exactly 2 spaces per level"
        )

    return content


class TestPracticeFile:
    """Tests for the practice.yml hands-on exercise."""

    def test_practice_file_exists(self, practice_file):
        """practice.yml must exist in the challenge directory."""
        assert practice_file.exists(), (
            "❌ practice.yml not found.\n"
            "   Did you complete Step 1 of Section 8 (Hands-On Practice)?"
        )

    def test_practice_file_is_valid_yaml(self, practice_content):
        """practice.yml must be valid YAML."""
        # If we got here, the fixture already parsed it successfully
        assert practice_content is not None, (
            "❌ practice.yml parsed as empty.\n"
            "   Did you save your changes? (Cmd+S or Ctrl+S)"
        )

    def test_project_section_exists(self, practice_content):
        """practice.yml must have a 'project' section."""
        assert "project" in practice_content, (
            "❌ Missing 'project' section in practice.yml.\n"
            "   Did you add the YAML content from Step 2?\n"
            "   Your file should start with:\n"
            "     project:\n"
            "       name: warm_up_practice"
        )

    def test_project_name(self, practice_content):
        """project.name must be 'warm_up_practice'."""
        project = practice_content.get("project", {}) or {}
        assert project.get("name") == "warm_up_practice", (
            f"❌ project.name should be 'warm_up_practice', found: '{project.get('name')}'\n"
            "   Did you copy the YAML content exactly from Step 2?"
        )

    def test_project_version(self, practice_content):
        """project.version must be set."""
        project = practice_content.get("project", {}) or {}
        assert "version" in project, (
            "❌ Missing 'version' key inside the 'project' section.\n"
            "   Did you copy the full YAML content from Step 2?"
        )

    def test_author_added(self, practice_content):
        """project.author must be present — added in Step 4."""
        project = practice_content.get("project", {}) or {}
        assert "author" in project, (
            "❌ Missing 'author' key inside the 'project' section.\n"
            "   Did you complete Step 4 of Section 8?\n"
            "   Add this line under 'version':\n"
            "     author: \"Your Name\""
        )

    def test_author_is_not_placeholder(self, practice_content):
        """project.author must not still be the placeholder 'Your Name'."""
        project = practice_content.get("project", {}) or {}
        author = project.get("author", "")
        assert str(author).strip().lower() not in ("your name", ""), (
            "❌ Replace the placeholder with your actual name.\n"
            "   Change: author: \"Your Name\"\n"
            "   To:     author: \"Ada Lovelace\"  (or your own name!)"
        )

    def test_tools_section_exists(self, practice_content):
        """practice.yml must have a 'tools' section."""
        assert "tools" in practice_content, (
            "❌ Missing 'tools' section in practice.yml.\n"
            "   Did you copy the full YAML content from Step 2?\n"
            "   Your file should include a 'tools:' list after the 'project:' section."
        )

    def test_tools_is_a_list(self, practice_content):
        """tools must be a list."""
        tools = practice_content.get("tools")
        assert isinstance(tools, list), (
            f"❌ 'tools' should be a YAML list, but found: {type(tools).__name__}\n"
            "   Each tool should start with '  - name:' (2 spaces, then a dash)"
        )

    def test_tools_has_three_entries(self, practice_content):
        """tools list must have at least 3 entries."""
        tools = practice_content.get("tools") or []
        assert len(tools) >= 3, (
            f"❌ Expected at least 3 tools, found {len(tools)}.\n"
            "   Did you include dbt, duckdb, and vscode in the tools list?"
        )

    def test_tools_contain_required_names(self, practice_content):
        """tools list must include dbt, duckdb, and vscode."""
        tools = practice_content.get("tools") or []
        tool_names = [str(t.get("name", "")).lower() for t in tools if isinstance(t, dict)]
        required = ["dbt", "duckdb", "vscode"]
        missing = [t for t in required if t not in tool_names]
        assert not missing, (
            f"❌ Missing tools in practice.yml: {missing}\n"
            "   Did you copy all three tools from Step 2?\n"
            f"   Found: {tool_names}"
        )
