#!/usr/bin/env python3
"""Check native loading in Agent Zero's framework runtime without LLM requests."""
import asyncio
from pathlib import Path
import sys

from agent import AgentContext, LoopData
from helpers import files, projects, runtime, skills, subagents
from initialize import initialize_agent
from tools.skills_tool import SkillsTool

from install import ROLES, SKILLS, install

PROJECT = Path(__file__).resolve().parents[1].name


async def main():
    runtime.initialize()
    root = Path(files.get_abs_path("."))
    count, _ = install(root, check=True)
    assert PROJECT in {p["name"] for p in projects.get_active_projects_list()}
    header = projects.load_basic_project_data(PROJECT)
    assert header["include_agents_md"] is True
    instructions = projects.build_system_prompt_vars(PROJECT)["project_instructions"]
    assert "# A0 Engineering Team DOX" in instructions
    assert "# Project operations" in instructions
    assert "defaults to the hosting instance" in instructions
    available = subagents.get_available_agents_dict(PROJECT)
    for profile in ROLES:
        assert profile in available, profile
        config = initialize_agent()
        config.profile = profile
        config.mcp_servers = ""
        context = AgentContext(config=config, name="Team loading check",
                               data={projects.CONTEXT_DATA_KEY_PROJECT: PROJECT})
        try:
            agent = context.agent0
            specifics = agent.read_prompt("agent.system.main.specifics.md")
            assert "{{" not in specifics
            assert "references/team-contract.md" in specifics
            assert "configured target, otherwise the hosting instance" in specifics
            if profile in ("chief-of-staff", "delivery-manager"):
                assert "references/planning-questions.md" in specifics
            default_dirs = [files.get_abs_path("agents/default/prompts"),
                            files.get_abs_path("prompts")]
            for inherited in ("agent.system.main.role.md", "agent.system.main.communication.md",
                              "agent.system.main.solving.md"):
                expected = files.read_prompt_file(inherited, default_dirs, _agent=agent).rstrip("\n")
                assert agent.read_prompt(inherited) == expected, (profile, inherited)
            loop_data = LoopData()
            rendered = "\n\n".join(await agent.get_system_prompt(loop_data))
            assert available[profile].title in rendered
            assert "### response" in rendered
            protocol = loop_data.protocol_persistent["project_instructions"]
            assert "# Project operations" in protocol
            assert "# A0 Engineering Team DOX" in protocol
            assert "defaults to the hosting instance" in protocol
            for name in SKILLS:
                skill = skills.find_skill(name, agent=agent, include_content=True)
                assert skill and skill.path == root / "usr/skills" / name
                assert not skills.validate_skill(skill), name
                tool = SkillsTool(agent=agent, name="skills_tool", method=None, args={},
                                  message="", loop_data=LoopData())
                loaded = await tool.execute(action="load", skill_name=name)
                assert loaded.additional["skill_instructions"]["content_included"]
                for reference in sorted(skill.path.glob("references/*.md")):
                    read = await tool.execute(action="read_file", skill_name=name,
                                              file_path="references/" + reference.name)
                    assert not read.message.startswith("Error") and len(read.message) > 100
                    if reference.name == "team-contract.md":
                        assert "defaults to the hosting instance" in read.message
                        assert "without silently falling back" in read.message
            print(f"PASS: {profile}, native prompt inheritance and skill load/reference reads")
        finally:
            AgentContext.remove(context.id)
    print(f"PASS: {count} deployed ordinary files, {len(ROLES)} profiles, "
          f"{len(SKILLS)} skills, native project discovery/instructions; no model call")


if __name__ == "__main__":
    if sys.flags.optimize:
        raise SystemExit("Run without -O so assertions remain enabled")
    asyncio.run(main())
