# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'streamlit_hello': {
        'command': ['streamlit', 'run','hello.py'],
        'timeout': 10000,
        'launcher_entry': {
            'enabled': True,
            'title': 'streamlit_hello',
        },
    },
}
