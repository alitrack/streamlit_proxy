# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['streamlit', 'run', 'https://raw.githubusercontent.com/streamlit/demo-self-driving/master/app.py'],
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'title': 'demo-self-driving',
        },
    },
}
