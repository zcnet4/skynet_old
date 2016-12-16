# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This is the "public" ppapi.gyp file, which must have dependencies on the
# redistributable portions of PPAPI only. This prevents circular dependencies
# in the .gyp files (since ppapi_internal depends on parts of Chrome).

{
  'variables': {
    'chromium_code': 1,  # Use higher warning level.
    'c99':1,
  },
  'target_defaults': {
    'conditions': [
      # Linux shared libraries should always be built -fPIC.
      #
      # TODO(ajwong): For internal pepper plugins, which are statically linked
      # into chrome, do we want to build w/o -fPIC?  If so, how can we express
      # that in the build system?
      #['os_posix == 1 and OS != "mac" and OS != "android"', {
      #  'cflags': ['-fPIC', '-fvisibility=default'],

        # This is needed to make the Linux shlib build happy. Without this,
        # -fvisibility=hidden gets stripped by the exclusion in common.gypi
        # that is triggered when a shared library build is specified.
      #  'cflags/': [['include', '^-fvisibility=default$']],
	  #	'scons_variable_settings': {'SHLIBPREFIX':'',},
      #}],
    ],
	'include_dirs': [
		# 配置全局开发目录。
		#'..',
		#'../common',
    ],
	#目标工程预处理宏定义
	'defines': [
		#'DEFINE_ZC_VALUE=ZC',
		#'NOMINMAX',
	],
  },
  'targets': [
	{
	  # 目标工程名
      'target_name': 'bson',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-bson.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"bson.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  # Add the default import libs.
        'msvs_settings':{
          'VCLinkerTool': {
            #'MinimumRequiredVersion' : '5.01',
            'AdditionalDependencies': [
              #'User32.lib',
			  'Ws2_32.lib',
            ],
          },
        },
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'crypt',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-crypt.c",
		"lsha1.c",
		"sha256.c",
		"sha256.h",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"crypt.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'debugchannel',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-debugchannel.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"debugchannel.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'mongo',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-mongo.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"mongo.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'mysqlaux',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-mysqlaux.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"mysqlaux.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'netpack',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-netpack.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"netpack.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'profile',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-profile.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"profile.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'sharedata',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-sharedata.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"sharedata.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'sproto',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"sproto/lsproto.c",
		"sproto/sproto.c",
		"sproto/sproto.h",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"sproto.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'stm',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-stm.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"stm.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # 目标工程名
      'target_name': 'multicast',
      'type': 'loadable_module',
	  # 目标工程依赖工程
      'dependencies': [
		'../3rd/3rd.gyp:lua',
      ],
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
		'../skynet-src',
      ],
	  #目标工程源代码路径
      'sources': [
		"lua-multicast.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'sources': [
			"multicast.def",
		  ],
		  'msvs_disabled_warnings': [
			'4204'
		  ],
		  'dependencies': [	
			'../3rd/3rd.gyp:posix_win',
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
  ],
  
}
