# 3rd.gypi
{
  'targets': [
	{
      'target_name': 'tar',
      'type': 'static_library',
      'dependencies': [
		'posix_win',
      ],
      'defines': [
      ],
      'include_dirs': [
		'../posix_win',
      ],
      'sources': [
		"tar.c",
		"tar.h",
	  ],
	  'conditions': [
        ['OS=="win"', {
		  'sources': [
			
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
      'target_name': 'tar_bin',
      'type': 'executable',
      'dependencies': [
		'posix_win',
		'tar',
      ],
      'defines': [
      ],
      'include_dirs': [
		'tar',
		'../posix_win',
      ],
      'sources': [
		"main.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
		  'sources': [
			
		  ],
		  # Add the default import libs.
        'msvs_settings':{
          'VCLinkerTool': {
            'MinimumRequiredVersion' : '5.01',
            'AdditionalDependencies': [
              'User32.lib',
			  'Ws2_32.lib',
            ],
          },
        },
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
  ],
}
