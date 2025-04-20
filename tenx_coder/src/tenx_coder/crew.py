from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TenxCoder():
    """TenxCoder crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            verbose=True
        )
    
    @agent
    def frontend_dev(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_dev'],
            verbose=True
        )
    
    @agent
    def backend_dev(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_dev'],
            verbose=True
        )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def project_manager_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_manager_task'],
        )
    
    @task
    def frontend_dev_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_dev_task'],
        )
    
    @task
    def backend_dev_task(self) -> Task:
        return Task(
            config=self.tasks_config['backend_dev_task'],
        )
    




    @crew
    def crew(self) -> Crew:
        """Creates the TenxCoder crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
