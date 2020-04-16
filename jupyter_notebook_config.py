# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'streamlit_hello': {
        'command': ['streamlit', 'run','hello.py','--browser.serverAddress=0.0.0.0', '--browser.gatherUsageStats=False', '--server.enableCORS=False'],
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'title': 'streamlit_hello',
        },
    },
}
