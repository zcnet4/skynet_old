/* -------------------------------------------------------------------------
//	FileName		:	d:\yx_code\yx\skynet\service-src\embed_resouce_loader.h
//	Creator			:	(zc)
//	CreateTime	:	2016-11-1 11:48
//	Description	:	
//
// -----------------------------------------------------------------------*/
#ifndef EMBED_RESOUCE_LOADER_H_
#define EMBED_RESOUCE_LOADER_H_
#include <stdbool.h>
// -------------------------------------------------------------------------

static int _loader_lua(lua_State *L) {
  const char *filename = luaL_checkstring(L, 1);
  printf("%s\n", filename);
  return 0;
}

bool EmbedResouceLoader(lua_State *L) {
  int top = lua_gettop(L);

  lua_getglobal(L, "table");
  lua_getfield(L, -1, "insert");
#ifdef LUA_COMPAT_LOADERS
  lua_getglobal(L, "package");
  lua_getfield(L, -1, "loaders");
  lua_remove(L, -2); // ÒÆ³ýpackage
#else
  lua_getglobal(L, "package");
  lua_getfield(L, -1, "searchers");
  lua_remove(L, -2); // ÒÆ³ýpackage
#endif
  lua_pushinteger(L, 1);
  lua_pushcfunction(L, _loader_lua);

  bool success = (LUA_OK == lua_pcall(L, 3, 0, 0));

  lua_settop(L, top);
  //
  return success;
}


// -------------------------------------------------------------------------
#endif /* EMBED_RESOUCE_LOADER_H_ */
