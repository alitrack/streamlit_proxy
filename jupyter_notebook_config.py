# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'streamlit_hello': {
        'command': ['streamlit', 'hello'],
        'timeout': 0,
        'launcher_entry': {
            'enabled': True,
            'title': 'streamlit_hello',
        },
    },
}
