/* -------------------------------------------------------------------------
//	FileName		£º	D:\yy_code\strife\trunk\src\ChatServer\src\skynet_proto.h
//	Creator			£º	(zc) <zcnet4@gmail.com>
//	CreateTime	£º	2016-4-8 14:10
//	Description	£º	
//
// -----------------------------------------------------------------------*/
#ifndef SKYNET_PROTO_H_
#define SKYNET_PROTO_H_
#include <stdint.h>
// -------------------------------------------------------------------------
#ifdef __cplusplus
extern "C" {
#endif

typedef struct lua_State lua_State;
int _skynet_proto_pack(lua_State* L);
int _skynet_proto_unpack(lua_State *L);

void _skynet_proto_pack_session(uint32_t session, unsigned char** buf, int* buf_size);
void _skynet_proto_unpack_session(uint32_t* session, const unsigned char** buf, int* buf_size);

// return proto_buf
unsigned char* _skynet_proto_pack_content(lua_State* L, int from, int to, int* buf_size);
int _skynet_proto_unpack_content(lua_State* L, const unsigned char* buf, int buf_size);

unsigned char* _skynet_proto_gen_auth(lua_State* L, int* auth_size);
int _skynet_proto_auth(lua_State* L);

unsigned char* _skynet_proto_content_offset(unsigned char* proto_buf, int proto_buf_size, int* proto_content_size);
int _skynet_proto_tochat(lua_State* L);
#ifdef __cplusplus
}
#endif
// -------------------------------------------------------------------------
#endif /* SKYNET_PROTO_H_ */
