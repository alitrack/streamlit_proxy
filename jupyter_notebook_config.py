# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'demo-self-driving': {
        'command': ['streamlit', 'run', 'https://raw.githubusercontent.com/streamlit/demo-self-driving/master/app.py',"--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"],
        'port':8507
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'title': 'demo self driving',
        },
    },
    'hello': {
        'command': ['streamlit', 'hello', "--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"],
        'port':8508
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'title': 'streamlit hello',
        },
    },    
}
