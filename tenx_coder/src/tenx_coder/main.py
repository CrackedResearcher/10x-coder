#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from .crew import TenxCoder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'clients_project_description': '''
    I want to build a platform where content creators can schedule, manage, and auto-post short-form videos (like Reels or TikToks) across multiple platforms (Instagram, TikTok, YouTube Shorts).

The tool should allow users to upload a video, select the platforms they want to post to, schedule a time, and optionally add captions or hashtags per platform.

Bonus: If it can suggest best times to post based on platform data, that would be great.

I'd also like analytics — views, likes, shares — to be pulled back into a dashboard for users to track performance.

Auth should be simple (Google or email login). This is a SaaS platform, so eventually I'll need billing too.
''',
'current_year': '20 April 2025'

    }
    
    try:
        TenxCoder().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

