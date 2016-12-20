{
  'targets': [
    {
      'target_name': 'jemalloc',
      'type': 'none',
	  'conditions': [
        ['OS=="win"', {
		
        }, { # OS != "win",
		  'actions': [
		  {
            'action_name': 'generate header',
            'action': ['./build.sh'],
		    'message': 'Generating manpage'
          },
         ],
        }
		]
      ],
	},
  ],
}
