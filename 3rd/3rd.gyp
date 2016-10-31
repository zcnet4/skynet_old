# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This is the "public" ppapi.gyp file, which must have dependencies on the
# redistributable portions of PPAPI only. This prevents circular dependencies
# in the .gyp files (since ppapi_internal depends on parts of Chrome).

{
  'variables': {
    'chromium_code': 1,  # Use higher warning level.
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
		# ����ȫ�ֿ���Ŀ¼��
		#'..',
		#'../common',
    ],
	#Ŀ�깤��Ԥ����궨��
	'defines': [
		#'DEFINE_ZC_VALUE=ZC',
		#'NOMINMAX',
	],
  },
  'includes': [
	'posix_win/posix.gypi',
  ],
  'targets': [
    {
	  # Ŀ�깤����
      'target_name': 'lua',
      'type': 'shared_library',
	  'product_name':'lua53',
	  #Ŀ�깤��C++ includeĿ¼
      'include_dirs': [
		'../skynet-src',
      ],
	  #Ŀ�깤��Դ����·��
      'sources': [
		"lua/lapi.c",
		"lua/lapi.h",
		"lua/lauxlib.c",
		"lua/lauxlib.h",
		"lua/lbaselib.c",
		"lua/lbitlib.c",
		"lua/lcode.c",
		"lua/lcode.h",
		"lua/lcorolib.c",
		"lua/lctype.c",
		"lua/lctype.h",
		"lua/ldblib.c",
		"lua/ldebug.c",
		"lua/ldebug.h",
		"lua/ldo.c",
		"lua/ldo.h",
		"lua/ldump.c",
		"lua/lfunc.c",
		"lua/lfunc.h",
		"lua/lgc.c",
		"lua/lgc.h",
		"lua/linit.c",
		"lua/liolib.c",
		"lua/llex.c",
		"lua/llex.h",
		"lua/llimits.h",
		"lua/lmathlib.c",
		"lua/lmem.c",
		"lua/lmem.h",
		"lua/loadlib.c",
		"lua/lobject.c",
		"lua/lobject.h",
		"lua/lopcodes.c",
		"lua/lopcodes.h",
		"lua/loslib.c",
		"lua/lparser.c",
		"lua/lparser.h",
		"lua/lprefix.h",
		"lua/lstate.c",
		"lua/lstate.h",
		"lua/lstring.c",
		"lua/lstring.h",
		"lua/lstrlib.c",
		"lua/ltable.c",
		"lua/ltable.h",
		"lua/ltablib.c",
		"lua/ltm.c",
		"lua/ltm.h",
		#"lua/lua.c",
		"lua/lua.h",
		"lua/lua.hpp",
		"lua/luac.c",
		"lua/luaconf.h",
		"lua/lualib.h",
		"lua/lundump.c",
		"lua/lundump.h",
		"lua/lutf8lib.c",
		"lua/lvm.c",
		"lua/lvm.h",
		"lua/lzio.c",
		"lua/lzio.h",
      ],
      'direct_dependent_settings': {
        'include_dirs': [
		  'lua',
        ],
      },
	  'conditions': [
        ['OS=="win"', {
			#Ŀ�깤��Ԥ����궨��
			'defines': [
				'LUA_BUILD_AS_DLL',
			],
			'include_dirs': [
				'posix_win',
			],
			# Ŀ�깤����������
			'dependencies': [
				'posix_win',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'posix_win',
				],
			},
		}, { # OS != "win",
		  'defines': [
			'LUA_USE_LINUX'
		  ],
		  'libraries': [
			'-ldl',
			'-lrt',
			'-lm',
		  ],
		  'scons_variable_settings': {'SHLIBPREFIX':'lib',},
        }]
      ],
    },
	{
	  # Ŀ�깤����
      'target_name': 'md5',
      'type': 'loadable_module',
	  # Ŀ�깤����������
      'dependencies': [
		'lua',
      ],
	  #Ŀ�깤��Ԥ����궨��
      'defines': [
      ],
	  #Ŀ�깤��C++ includeĿ¼
      'include_dirs': [
		'lua',
      ],
	  #Ŀ�깤��Դ����·��
      'sources': [
		"lua-md5/compat-5.2.c",
		"lua-md5/md5.c",
		"lua-md5/md5lib.c",
		"lua-md5/compat-5.2.h",
		"lua-md5/md5.h",
	  ],
	  'conditions': [
        ['OS=="win"', {
		  'sources': [
			"lua-md5/md5.def",
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
	  # Ŀ�깤����
      'target_name': 'lpeg',
      'type': 'loadable_module',
	  # Ŀ�깤����������
      'dependencies': [
		'lua',
      ],
	  #Ŀ�깤��Ԥ����궨��
      'defines': [
      ],
	  #Ŀ�깤��C++ includeĿ¼
      'include_dirs': [
		'lua',
      ],
	  #Ŀ�깤��Դ����·��
      'sources': [
		"lpeg/lpeg.def",
		"lpeg/lpvm.c",
		"lpeg/lptree.c",
		"lpeg/lpprint.c",
		"lpeg/lpcode.c",
		"lpeg/lpcap.c",
	  ],
    },
	{
	  # Ŀ�깤����
      'target_name': 'cjson',
      'type': 'loadable_module',
	  # Ŀ�깤����������
      'dependencies': [
		'lua',
      ],
	  #Ŀ�깤��Ԥ����궨��
      'defines': [
      ],
	  #Ŀ�깤��C++ includeĿ¼
      'include_dirs': [
		'lua',
      ],
	  #Ŀ�깤��Դ����·��
      'sources': [
		"lua-cjson/fpconv.c",
		"lua-cjson/lua_cjson.c",
		"lua-cjson/strbuf.c",
	  ],
	  'conditions': [
        ['OS=="win"', {
		  'sources': [
			"lua-cjson/cjson.def",
		  ],
        }, { # OS != "win",
          'defines': [
            
          ],
        }]
      ],
    },
	{
      'target_name': 'tar',
      'type': 'static_library',
      'dependencies': [
		'posix_win',
      ],
      'defines': [
      ],
      'include_dirs': [
		'posix_win',
      ],
      'sources': [
		"tar/tar.cc",
		"tar/tar.h",
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
  ],
  
}
